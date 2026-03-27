from __future__ import annotations

from typing import Any

from .models import GeneratedCase


DEFAULT_DIMENSIONS = ["normal", "exception", "boundary"]


class CaseGenerationError(ValueError):
    """Raised when the generation input is insufficient."""


def build_test_cases(payload: dict[str, Any]) -> list[GeneratedCase]:
    title = str(payload.get("title", "")).strip()
    description = str(payload.get("description", "")).strip()
    if not title or not description:
        raise CaseGenerationError("title and description are required")

    dimensions = payload.get("coverage_dimensions") or DEFAULT_DIMENSIONS
    structured_rules = [str(rule).strip() for rule in payload.get("structured_rules", []) if str(rule).strip()]
    attachments = payload.get("attachments", [])

    scenario_parts = [description]
    if structured_rules:
        scenario_parts.append("Rules: " + "; ".join(structured_rules))
    if attachments:
        scenario_parts.append("Attachments: " + ", ".join(item.get("name", "unnamed") for item in attachments))
    scenario = " ".join(scenario_parts)

    cases: list[GeneratedCase] = []
    for index, dimension in enumerate(dimensions, start=1):
        steps = [
            f"Prepare request context for {title}.",
            f"Submit source material with {dimension} coverage.",
            "Inspect the generated structured case output.",
        ]
        expected = [
            "The service accepts and validates the request.",
            "The generation result includes actionable cases.",
            f"The output highlights {dimension} coverage requirements.",
        ]

        if dimension == "exception":
            steps[1] = f"Submit incomplete or invalid source material for {title}."
            expected[0] = "The service rejects invalid input with a clear error code."
        elif dimension == "boundary":
            steps[1] = f"Submit minimal but valid source material for {title}."
            expected[2] = "The output covers edge constraints and boundary behavior."
        elif dimension == "permission":
            expected[2] = "The output differentiates authorized and unauthorized actors."

        cases.append(
            GeneratedCase(
                case_id=f"TC-{index:03d}",
                title=f"{title} - {dimension}",
                scenario=scenario,
                preconditions=[
                    "A valid application has been provisioned.",
                    "The caller can access the generation endpoint.",
                ],
                steps=steps,
                expected_results=expected,
                coverage_dimension=dimension,
                priority="P0" if dimension in {"normal", "exception", "boundary"} else "P1",
            )
        )

    return cases
