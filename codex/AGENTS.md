# Repository Guidelines

## Project Structure & Module Organization
This repository now contains a Python MVP for the test case generation API. Keep the root clean and organize work under these top-level directories:

- `src/` for production code
- `tests/` for automated tests
- `docs/` for design notes or contributor-facing documentation
- `assets/` for static files such as images or sample data
- `scripts/` for local developer entrypoints such as server startup helpers

The current implementation lives in `src/test_case_generation_api/` and is split by responsibility (`models.py`, `generator.py`, `services.py`, `server.py`). Prefer extending that pattern instead of creating broad utility dumps.

## Build, Test, and Development Commands
Use the following authoritative local commands:

- `python scripts/run_server.py` to start the API service locally
- `python -m unittest discover -s tests -v` to execute the automated test suite

If new tooling is introduced, add the stable command here and mirror it in `README.md`.

## Coding Style & Naming Conventions
Use 4 spaces for Python and 2 spaces for JavaScript, TypeScript, JSON, YAML, and Markdown lists. Prefer descriptive file and module names such as `user_service.py` or `task-runner.ts`.

- Python: `snake_case` for functions and modules, `PascalCase` for classes
- JS/TS: `camelCase` for variables/functions, `PascalCase` for components/classes
- Markdown: short sections, sentence-case bullets, fenced code blocks with language tags

Adopt a formatter and linter with any new stack and run them before opening a PR.

## Testing Guidelines
Place tests under `tests/` and mirror the source layout where possible. Name test files after the unit under test, such as `tests/test_auth.py` or `tests/auth.spec.ts`.

Aim for meaningful coverage on new code and include at least one happy-path test plus one edge-case test for each new module.

## Commit & Pull Request Guidelines
Git history is not available in this workspace, so use a simple, consistent convention: imperative, present-tense commit messages such as `Add auth token validator`.

Pull requests should include:

- a short summary of what changed
- linked issue or task reference, if available
- test evidence or reproduction steps
- screenshots for UI changes

## Agent-Specific Notes
Keep contributor instructions current. If you introduce new tooling, directories, or workflows, update this file in the same change set.
