from __future__ import annotations

import base64
import hashlib
import hmac
import json
import secrets
import threading
import time
import uuid
from collections import Counter, deque
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from urllib.parse import urlparse

from .generator import CaseGenerationError, build_test_cases
from .models import Application, AuditEvent, Task, TaskStatus, utc_now


class DomainError(Exception):
    def __init__(self, code: str, message: str, status_code: int = 400) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code


def canonical_body(body: dict[str, Any]) -> str:
    return json.dumps(body, ensure_ascii=True, separators=(",", ":"), sort_keys=True)


def build_signature(secret: str, timestamp: str, nonce: str, body: dict[str, Any]) -> str:
    message = f"{timestamp}.{nonce}.{canonical_body(body)}".encode("utf-8")
    digest = hmac.new(secret.encode("utf-8"), message, hashlib.sha256).digest()
    return base64.b64encode(digest).decode("ascii")


class InMemoryRateLimiter:
    def __init__(self) -> None:
        self._buckets: dict[str, deque[float]] = {}
        self._lock = threading.Lock()

    def check(self, app_id: str, limit: int) -> None:
        now = time.time()
        with self._lock:
            bucket = self._buckets.setdefault(app_id, deque())
            while bucket and now - bucket[0] > 60:
                bucket.popleft()
            if len(bucket) >= limit:
                raise DomainError("RATE_LIMITED", "request rate exceeded", 429)
            bucket.append(now)


@dataclass(slots=True)
class AppRepository:
    apps: dict[str, Application]
    lock: threading.Lock

    def save(self, app: Application) -> Application:
        with self.lock:
            self.apps[app.app_id] = app
        return app

    def get(self, app_id: str) -> Application | None:
        return self.apps.get(app_id)

    def find_by_name(self, name: str) -> Application | None:
        for app in self.apps.values():
            if app.name == name:
                return app
        return None

    def list(self) -> list[Application]:
        with self.lock:
            return list(self.apps.values())


@dataclass(slots=True)
class TaskRepository:
    tasks: dict[str, Task]
    lock: threading.Lock

    def save(self, task: Task) -> Task:
        with self.lock:
            task.updated_at = utc_now()
            self.tasks[task.task_id] = task
        return task

    def get(self, task_id: str) -> Task | None:
        return self.tasks.get(task_id)

    def list(self) -> list[Task]:
        with self.lock:
            return list(self.tasks.values())


class AuditLog:
    def __init__(self) -> None:
        self._events: list[AuditEvent] = []
        self._lock = threading.Lock()

    def record(self, event_type: str, app_id: str | None, detail: dict[str, Any]) -> None:
        with self._lock:
            self._events.append(AuditEvent(event_type=event_type, app_id=app_id, detail=detail))

    def list_events(self) -> list[dict[str, Any]]:
        with self._lock:
            return [event.to_dict() for event in self._events]


class AppService:
    def __init__(self, repository: AppRepository, audit_log: AuditLog) -> None:
        self.repository = repository
        self.audit_log = audit_log

    def create_application(self, payload: dict[str, Any]) -> Application:
        name = str(payload.get("name", "")).strip()
        if not name:
            raise DomainError("INVALID_APP_NAME", "application name is required")
        if self.repository.find_by_name(name):
            raise DomainError("APP_NAME_EXISTS", "application name already exists", 409)

        callback_url = payload.get("callback_url")
        if callback_url:
            parsed = urlparse(str(callback_url))
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                raise DomainError("INVALID_CALLBACK_URL", "callback_url must be a valid http or https url")

        app = Application(
            app_id=f"app_{uuid.uuid4().hex[:12]}",
            name=name,
            description=str(payload.get("description", "")).strip(),
            callback_url=str(callback_url) if callback_url else None,
            contact=str(payload.get("contact", "")).strip() or None,
            api_key_id=f"key_{uuid.uuid4().hex[:12]}",
            api_secret=secrets.token_urlsafe(24),
        )
        self.repository.save(app)
        self.audit_log.record("application.created", app.app_id, {"name": app.name})
        return app

    def get_application(self, app_id: str) -> Application:
        app = self.repository.get(app_id)
        if not app:
            raise DomainError("APP_NOT_FOUND", "application not found", 404)
        return app

    def reset_secret(self, app_id: str) -> Application:
        app = self.get_application(app_id)
        app.api_secret = secrets.token_urlsafe(24)
        self.repository.save(app)
        self.audit_log.record("application.secret_reset", app.app_id, {})
        return app


class AuthService:
    def __init__(self, app_service: AppService) -> None:
        self.app_service = app_service

    def authenticate(self, app_id: str, timestamp: str, nonce: str, signature: str, body: dict[str, Any]) -> Application:
        app = self.app_service.get_application(app_id)
        if not timestamp or not nonce or not signature:
            raise DomainError("AUTH_HEADERS_MISSING", "authentication headers are incomplete", 401)
        expected = build_signature(app.api_secret, timestamp, nonce, body)
        if not hmac.compare_digest(expected, signature):
            raise DomainError("SIGNATURE_INVALID", "signature verification failed", 401)

        try:
            requested_at = datetime.fromtimestamp(int(timestamp), tz=timezone.utc)
        except ValueError as exc:
            raise DomainError("TIMESTAMP_INVALID", "timestamp must be an integer epoch second", 401) from exc

        age = abs((utc_now() - requested_at).total_seconds())
        if age > 300:
            raise DomainError("TIMESTAMP_EXPIRED", "request timestamp is outside the accepted window", 401)
        return app


class TaskService:
    def __init__(
        self,
        repository: TaskRepository,
        rate_limiter: InMemoryRateLimiter,
        audit_log: AuditLog,
    ) -> None:
        self.repository = repository
        self.rate_limiter = rate_limiter
        self.audit_log = audit_log
        self.executor = ThreadPoolExecutor(max_workers=2, thread_name_prefix="caseflow")

    def submit(self, app: Application, payload: dict[str, Any]) -> dict[str, Any]:
        request_id = str(payload.get("request_id", "")).strip()
        title = str(payload.get("title", "")).strip()
        description = str(payload.get("description", "")).strip()
        if not request_id:
            raise DomainError("REQUEST_ID_REQUIRED", "request_id is required")
        if not title or not description:
            raise DomainError("INPUT_REQUIRED", "title and description are required")

        self.rate_limiter.check(app.app_id, app.rate_limit_per_minute)
        task = Task(
            task_id=f"task_{uuid.uuid4().hex[:12]}",
            app_id=app.app_id,
            request_id=request_id,
            title=title,
            description=description,
            generation_mode=str(payload.get("generation_mode", "sync")).strip() or "sync",
            template_id=str(payload.get("template_id", "standard")).strip() or "standard",
            coverage_dimensions=list(payload.get("coverage_dimensions") or []),
            structured_rules=list(payload.get("structured_rules") or []),
            attachments=list(payload.get("attachments") or []),
        )
        self.repository.save(task)
        self.audit_log.record("task.created", app.app_id, {"task_id": task.task_id, "mode": task.generation_mode})

        if task.generation_mode == "async":
            self.executor.submit(self._process_task, task.task_id)
            return {"task_id": task.task_id, "status": task.status.value}

        self._process_task(task.task_id)
        return self.get_task(app.app_id, task.task_id).to_dict()

    def get_task(self, app_id: str, task_id: str) -> Task:
        task = self.repository.get(task_id)
        if not task:
            raise DomainError("TASK_NOT_FOUND", "task not found", 404)
        if task.app_id != app_id:
            raise DomainError("TASK_FORBIDDEN", "task does not belong to the application", 403)
        return task

    def retry(self, app_id: str, task_id: str) -> Task:
        task = self.get_task(app_id, task_id)
        if task.status != TaskStatus.FAILED:
            raise DomainError("TASK_NOT_RETRYABLE", "only failed tasks can be retried", 409)
        task.status = TaskStatus.PENDING
        task.error_code = None
        task.error_message = None
        task.result = []
        self.repository.save(task)
        self.executor.submit(self._process_task, task.task_id)
        self.audit_log.record("task.retried", app_id, {"task_id": task.task_id})
        return task

    def _process_task(self, task_id: str) -> None:
        task = self.repository.get(task_id)
        if not task:
            return

        task.status = TaskStatus.PROCESSING
        self.repository.save(task)
        try:
            task.result = build_test_cases(
                {
                    "title": task.title,
                    "description": task.description,
                    "coverage_dimensions": task.coverage_dimensions,
                    "structured_rules": task.structured_rules,
                    "attachments": task.attachments,
                }
            )
            task.status = TaskStatus.SUCCESS
            self.audit_log.record("task.succeeded", task.app_id, {"task_id": task.task_id, "case_count": len(task.result)})
        except CaseGenerationError as exc:
            task.status = TaskStatus.FAILED
            task.error_code = "GENERATION_INVALID_INPUT"
            task.error_message = str(exc)
            self.audit_log.record("task.failed", task.app_id, {"task_id": task.task_id, "error": str(exc)})
        self.repository.save(task)


class ConsoleService:
    def __init__(self, app_repository: AppRepository, task_repository: TaskRepository, audit_log: AuditLog) -> None:
        self.app_repository = app_repository
        self.task_repository = task_repository
        self.audit_log = audit_log

    def overview(self) -> dict[str, Any]:
        apps = self.app_repository.list()
        tasks = self.task_repository.list()
        events = self.audit_log.list_events()
        success_count = sum(1 for task in tasks if task.status == TaskStatus.SUCCESS)
        failed_count = sum(1 for task in tasks if task.status == TaskStatus.FAILED)
        processing_count = sum(1 for task in tasks if task.status in {TaskStatus.PENDING, TaskStatus.PROCESSING})
        total_cases = sum(len(task.result) for task in tasks)
        app_names = {app.app_id: app.name for app in apps}
        top_apps = Counter(task.app_id for task in tasks).most_common(5)

        return {
            "summary": {
                "app_count": len(apps),
                "task_count": len(tasks),
                "success_count": success_count,
                "failed_count": failed_count,
                "processing_count": processing_count,
                "case_count": total_cases,
                "success_rate": round((success_count / len(tasks)) * 100, 1) if tasks else 0.0,
                "audit_event_count": len(events),
            },
            "recent_tasks": [self._serialize_task(task) for task in self._sorted_tasks(tasks)[:6]],
            "recent_events": list(reversed(events[-8:])),
            "top_apps": [
                {"app_id": app_id, "name": app_names.get(app_id, app_id), "task_count": task_count}
                for app_id, task_count in top_apps
            ],
        }

    def list_apps(self) -> list[dict[str, Any]]:
        tasks = self.task_repository.list()
        task_counts = Counter(task.app_id for task in tasks)
        success_counts = Counter(task.app_id for task in tasks if task.status == TaskStatus.SUCCESS)
        latest_task_by_app: dict[str, Task] = {}
        for task in self._sorted_tasks(tasks):
            latest_task_by_app.setdefault(task.app_id, task)

        result: list[dict[str, Any]] = []
        for app in sorted(self.app_repository.list(), key=lambda item: item.created_at, reverse=True):
            payload = app.public_dict()
            payload["task_count"] = task_counts.get(app.app_id, 0)
            payload["success_count"] = success_counts.get(app.app_id, 0)
            payload["last_task_at"] = latest_task_by_app[app.app_id].to_dict()["updated_at"] if app.app_id in latest_task_by_app else None
            result.append(payload)
        return result

    def get_app_detail(self, app_id: str) -> dict[str, Any]:
        app = self.app_repository.get(app_id)
        if not app:
            raise DomainError("APP_NOT_FOUND", "application not found", 404)
        tasks = [task for task in self.task_repository.list() if task.app_id == app_id]
        payload = app.public_dict()
        payload["task_count"] = len(tasks)
        payload["recent_tasks"] = [self._serialize_task(task) for task in self._sorted_tasks(tasks)[:5]]
        payload["case_count"] = sum(len(task.result) for task in tasks)
        return payload

    def list_tasks(self, app_id: str | None = None, status: str | None = None) -> list[dict[str, Any]]:
        tasks = self.task_repository.list()
        if app_id:
            tasks = [task for task in tasks if task.app_id == app_id]
        if status:
            tasks = [task for task in tasks if task.status.value == status]
        return [self._serialize_task(task) for task in self._sorted_tasks(tasks)]

    def get_task_detail(self, task_id: str) -> dict[str, Any]:
        task = self.task_repository.get(task_id)
        if not task:
            raise DomainError("TASK_NOT_FOUND", "task not found", 404)
        return self._serialize_task(task)

    def list_results(self, app_id: str | None = None, task_id: str | None = None) -> list[dict[str, Any]]:
        records: list[dict[str, Any]] = []
        for task in self._sorted_tasks(self.task_repository.list()):
            if app_id and task.app_id != app_id:
                continue
            if task_id and task.task_id != task_id:
                continue
            if task.status != TaskStatus.SUCCESS:
                continue
            app = self.app_repository.get(task.app_id)
            for case in task.result:
                records.append(
                    {
                        "case_id": case.case_id,
                        "task_id": task.task_id,
                        "app_id": task.app_id,
                        "app_name": app.name if app else task.app_id,
                        "request_id": task.request_id,
                        "title": case.title,
                        "scenario": case.scenario,
                        "coverage_dimension": case.coverage_dimension,
                        "priority": case.priority,
                        "updated_at": task.to_dict()["updated_at"],
                    }
                )
        return records

    def get_case_detail(self, case_id: str) -> dict[str, Any]:
        for task in self.task_repository.list():
            for case in task.result:
                if case.case_id == case_id:
                    app = self.app_repository.get(task.app_id)
                    return {
                        "case": case.to_dict(),
                        "task": self._serialize_task(task),
                        "app": app.public_dict() if app else None,
                    }
        raise DomainError("CASE_NOT_FOUND", "case not found", 404)

    def _serialize_task(self, task: Task) -> dict[str, Any]:
        payload = task.to_dict()
        app = self.app_repository.get(task.app_id)
        payload["app_name"] = app.name if app else task.app_id
        payload["case_count"] = len(task.result)
        return payload

    @staticmethod
    def _sorted_tasks(tasks: list[Task]) -> list[Task]:
        return sorted(tasks, key=lambda item: item.updated_at, reverse=True)


class ApplicationContext:
    def __init__(self) -> None:
        app_repo = AppRepository(apps={}, lock=threading.Lock())
        task_repo = TaskRepository(tasks={}, lock=threading.Lock())
        self.audit_log = AuditLog()
        self.app_service = AppService(app_repo, self.audit_log)
        self.auth_service = AuthService(self.app_service)
        self.task_service = TaskService(task_repo, InMemoryRateLimiter(), self.audit_log)
        self.console_service = ConsoleService(app_repo, task_repo, self.audit_log)
