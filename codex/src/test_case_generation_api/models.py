from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def to_iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


class TaskStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"


@dataclass(slots=True)
class Application:
    app_id: str
    name: str
    description: str
    callback_url: str | None
    contact: str | None
    api_key_id: str
    api_secret: str
    status: str = "active"
    rate_limit_per_minute: int = 60
    created_at: datetime = field(default_factory=utc_now)

    def public_dict(self, include_secret: bool = False) -> dict[str, Any]:
        payload = asdict(self)
        payload["created_at"] = to_iso(self.created_at)
        if not include_secret:
            payload.pop("api_secret", None)
        return payload


@dataclass(slots=True)
class GeneratedCase:
    case_id: str
    title: str
    scenario: str
    preconditions: list[str]
    steps: list[str]
    expected_results: list[str]
    coverage_dimension: str
    priority: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class Task:
    task_id: str
    app_id: str
    request_id: str
    title: str
    description: str
    generation_mode: str
    template_id: str
    coverage_dimensions: list[str]
    structured_rules: list[str]
    attachments: list[dict[str, Any]]
    status: TaskStatus = TaskStatus.PENDING
    result: list[GeneratedCase] = field(default_factory=list)
    error_code: str | None = None
    error_message: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["status"] = self.status.value
        payload["created_at"] = to_iso(self.created_at)
        payload["updated_at"] = to_iso(self.updated_at)
        payload["result"] = [case.to_dict() for case in self.result]
        return payload


@dataclass(slots=True)
class AuditEvent:
    event_type: str
    app_id: str | None
    detail: dict[str, Any]
    created_at: datetime = field(default_factory=utc_now)

    def to_dict(self) -> dict[str, Any]:
        return {
            "event_type": self.event_type,
            "app_id": self.app_id,
            "detail": self.detail,
            "created_at": to_iso(self.created_at),
        }
