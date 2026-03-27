import time
import unittest

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from test_case_generation_api.services import (
    ApplicationContext,
    DomainError,
    build_signature,
)


class ServiceFlowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.context = ApplicationContext()
        self.app = self.context.app_service.create_application({"name": "demo-app"})

    def test_duplicate_application_name_is_rejected(self) -> None:
        with self.assertRaises(DomainError) as context:
            self.context.app_service.create_application({"name": "demo-app"})
        self.assertEqual("APP_NAME_EXISTS", context.exception.code)

    def test_authentication_accepts_valid_signature(self) -> None:
        body = {
            "request_id": "req-1",
            "title": "Generate cases",
            "description": "Need normal and exception coverage.",
            "generation_mode": "sync",
        }
        timestamp = str(int(time.time()))
        signature = build_signature(self.app.api_secret, timestamp, "nonce-1", body)
        authed_app = self.context.auth_service.authenticate(
            self.app.app_id,
            timestamp,
            "nonce-1",
            signature,
            body,
        )
        self.assertEqual(self.app.app_id, authed_app.app_id)

    def test_sync_generation_returns_result(self) -> None:
        result = self.context.task_service.submit(
            self.app,
            {
                "request_id": "req-2",
                "title": "Generate cases",
                "description": "Create API test cases from a requirement summary.",
                "generation_mode": "sync",
                "coverage_dimensions": ["normal", "boundary"],
            },
        )

        self.assertEqual("success", result["status"])
        self.assertEqual(2, len(result["result"]))

    def test_async_generation_completes_and_can_be_queried(self) -> None:
        result = self.context.task_service.submit(
            self.app,
            {
                "request_id": "req-3",
                "title": "Async cases",
                "description": "Generate cases asynchronously.",
                "generation_mode": "async",
            },
        )
        task_id = result["task_id"]
        task = None

        for _ in range(50):
            task = self.context.task_service.get_task(self.app.app_id, task_id)
            if task.status.value == "success":
                break
            time.sleep(0.02)

        self.assertIsNotNone(task)
        self.assertEqual("success", task.status.value)
        self.assertGreaterEqual(len(task.result), 1)

    def test_rate_limit_is_enforced(self) -> None:
        self.app.rate_limit_per_minute = 1
        self.context.task_service.submit(
            self.app,
            {
                "request_id": "req-4",
                "title": "First request",
                "description": "Allowed request.",
                "generation_mode": "sync",
            },
        )

        with self.assertRaises(DomainError) as context:
            self.context.task_service.submit(
                self.app,
                {
                    "request_id": "req-5",
                    "title": "Second request",
                    "description": "Should be rate limited.",
                    "generation_mode": "sync",
                },
            )

        self.assertEqual("RATE_LIMITED", context.exception.code)
