from __future__ import annotations

import json
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse

from .services import ApplicationContext, DomainError


FRONTEND_DIR = Path(__file__).resolve().parent / "frontend"


def json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict[str, Any]) -> None:
    raw = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(raw)))
    handler.end_headers()
    handler.wfile.write(raw)


def file_response(handler: BaseHTTPRequestHandler, path: Path) -> None:
    raw = path.read_bytes()
    content_type, _ = mimetypes.guess_type(path.name)
    handler.send_response(HTTPStatus.OK)
    handler.send_header("Content-Type", content_type or "application/octet-stream")
    handler.send_header("Content-Length", str(len(raw)))
    handler.end_headers()
    handler.wfile.write(raw)


class CaseFlowRequestHandler(BaseHTTPRequestHandler):
    context = ApplicationContext()

    def do_GET(self) -> None:  # noqa: N802
        self._dispatch("GET")

    def do_POST(self) -> None:  # noqa: N802
        self._dispatch("POST")

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _dispatch(self, method: str) -> None:
        try:
            parsed = urlparse(self.path)
            path = parsed.path
            query = parse_qs(parsed.query)
            if method == "GET" and path == "/":
                file_response(self, FRONTEND_DIR / "index.html")
                return
            if method == "GET" and path.startswith("/assets/"):
                asset_path = FRONTEND_DIR / path.removeprefix("/assets/")
                if not asset_path.is_file():
                    raise DomainError("NOT_FOUND", "resource not found", 404)
                file_response(self, asset_path)
                return
            if method == "GET" and path == "/favicon.ico":
                self.send_response(HTTPStatus.NO_CONTENT)
                self.end_headers()
                return
            if method == "GET" and path == "/healthz":
                json_response(self, HTTPStatus.OK, {"status": "ok"})
                return
            if method == "GET" and path == "/api/v1/console/overview":
                json_response(self, HTTPStatus.OK, {"data": self.context.console_service.overview()})
                return
            if method == "GET" and path == "/api/v1/console/apps":
                json_response(self, HTTPStatus.OK, {"data": self.context.console_service.list_apps()})
                return
            if method == "GET" and path.startswith("/api/v1/console/apps/"):
                app_id = path.split("/")[-1]
                json_response(self, HTTPStatus.OK, {"data": self.context.console_service.get_app_detail(app_id)})
                return
            if method == "GET" and path == "/api/v1/console/tasks":
                app_id = query.get("app_id", [None])[0]
                status = query.get("status", [None])[0]
                json_response(self, HTTPStatus.OK, {"data": self.context.console_service.list_tasks(app_id, status)})
                return
            if method == "GET" and path.startswith("/api/v1/console/tasks/"):
                task_id = path.split("/")[-1]
                json_response(self, HTTPStatus.OK, {"data": self.context.console_service.get_task_detail(task_id)})
                return
            if method == "GET" and path == "/api/v1/console/results":
                app_id = query.get("app_id", [None])[0]
                task_id = query.get("task_id", [None])[0]
                json_response(self, HTTPStatus.OK, {"data": self.context.console_service.list_results(app_id, task_id)})
                return
            if method == "GET" and path.startswith("/api/v1/console/cases/"):
                case_id = path.split("/")[-1]
                json_response(self, HTTPStatus.OK, {"data": self.context.console_service.get_case_detail(case_id)})
                return
            if method == "POST" and path == "/api/v1/apps":
                body = self._read_json()
                app = self.context.app_service.create_application(body)
                json_response(self, HTTPStatus.CREATED, {"data": app.public_dict(include_secret=True)})
                return
            if method == "GET" and path.startswith("/api/v1/apps/"):
                app_id = path.split("/")[-1]
                app = self.context.app_service.get_application(app_id)
                json_response(self, HTTPStatus.OK, {"data": app.public_dict()})
                return
            if method == "POST" and path.startswith("/api/v1/apps/") and path.endswith("/reset-secret"):
                app_id = path.split("/")[-2]
                app = self.context.app_service.reset_secret(app_id)
                json_response(self, HTTPStatus.OK, {"data": app.public_dict(include_secret=True)})
                return
            if method == "POST" and path == "/api/v1/tasks/generate":
                body = self._read_json()
                app = self._authenticate(body)
                result = self.context.task_service.submit(app, body)
                json_response(self, HTTPStatus.OK, {"data": result})
                return
            if method == "GET" and path.startswith("/api/v1/tasks/"):
                task_id = path.split("/")[-1]
                app_id = self.headers.get("X-App-Id", "")
                if not app_id:
                    raise DomainError("APP_ID_REQUIRED", "X-App-Id header is required", 401)
                task = self.context.task_service.get_task(app_id, task_id)
                json_response(self, HTTPStatus.OK, {"data": task.to_dict()})
                return
            if method == "POST" and path.startswith("/api/v1/tasks/") and path.endswith("/retry"):
                body = self._read_json()
                app = self._authenticate(body)
                task_id = path.split("/")[-2]
                task = self.context.task_service.retry(app.app_id, task_id)
                json_response(self, HTTPStatus.ACCEPTED, {"data": task.to_dict()})
                return
            if method == "GET" and path == "/api/v1/audit-events":
                json_response(self, HTTPStatus.OK, {"data": self.context.audit_log.list_events()})
                return
            raise DomainError("NOT_FOUND", "resource not found", 404)
        except DomainError as exc:
            json_response(self, exc.status_code, {"error": {"code": exc.code, "message": exc.message}})
        except json.JSONDecodeError:
            json_response(
                self,
                HTTPStatus.BAD_REQUEST,
                {"error": {"code": "INVALID_JSON", "message": "request body must be valid json"}},
            )

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length else b"{}"
        return json.loads(raw.decode("utf-8"))

    def _authenticate(self, body: dict[str, Any]):
        app_id = self.headers.get("X-App-Id", "")
        timestamp = self.headers.get("X-Timestamp", "")
        nonce = self.headers.get("X-Nonce", "")
        signature = self.headers.get("X-Signature", "")
        return self.context.auth_service.authenticate(app_id, timestamp, nonce, signature, body)


def create_server(host: str = "127.0.0.1", port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), CaseFlowRequestHandler)
