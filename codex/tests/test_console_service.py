import unittest

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from test_case_generation_api.services import ApplicationContext


class ConsoleServiceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.context = ApplicationContext()
        self.app = self.context.app_service.create_application({"name": "console-app"})
        self.context.task_service.submit(
            self.app,
            {
                "request_id": "console-req-1",
                "title": "Generate console cases",
                "description": "Create test cases for console service output.",
                "generation_mode": "sync",
                "coverage_dimensions": ["normal", "exception"],
            },
        )

    def test_overview_contains_summary_and_recent_records(self) -> None:
        overview = self.context.console_service.overview()

        self.assertEqual(1, overview["summary"]["app_count"])
        self.assertEqual(1, overview["summary"]["task_count"])
        self.assertEqual(2, overview["summary"]["case_count"])
        self.assertEqual(1, len(overview["recent_tasks"]))

    def test_case_detail_can_be_loaded_from_flattened_results(self) -> None:
        results = self.context.console_service.list_results()
        case_id = results[0]["case_id"]

        detail = self.context.console_service.get_case_detail(case_id)

        self.assertEqual(case_id, detail["case"]["case_id"])
        self.assertEqual(self.app.app_id, detail["task"]["app_id"])
