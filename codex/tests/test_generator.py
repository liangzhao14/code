import unittest

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from test_case_generation_api.generator import CaseGenerationError, build_test_cases


class BuildTestCasesTests(unittest.TestCase):
    def test_generates_cases_for_each_dimension(self) -> None:
        cases = build_test_cases(
            {
                "title": "Generate test cases",
                "description": "Produce structured test cases for API consumers.",
                "coverage_dimensions": ["normal", "exception"],
                "structured_rules": ["Result must be JSON"],
            }
        )

        self.assertEqual(2, len(cases))
        self.assertEqual("normal", cases[0].coverage_dimension)
        self.assertEqual("exception", cases[1].coverage_dimension)

    def test_raises_when_required_fields_missing(self) -> None:
        with self.assertRaises(CaseGenerationError):
            build_test_cases({"title": "", "description": ""})
