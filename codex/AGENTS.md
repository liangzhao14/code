# Repository Guidelines

## Project Structure & Module Organization
This repository is currently a minimal scaffold with no application code checked in yet. Keep the root clean and organize new work under clear top-level directories:

- `src/` for production code
- `tests/` for automated tests
- `docs/` for design notes or contributor-facing documentation
- `assets/` for static files such as images or sample data

Prefer feature-focused modules inside `src/` (for example, `src/auth/` or `src/api/`) rather than large mixed directories.

## Build, Test, and Development Commands
No build tooling is configured yet. When adding a language runtime or framework, expose the common workflows through documented commands and keep them stable.

Examples to add once tooling exists:

- `npm install` or `pip install -r requirements.txt` to install dependencies
- `npm run dev` or `python -m app` to run locally
- `npm test` or `pytest` to execute tests
- `npm run lint` or `ruff check .` to enforce style

Record the authoritative commands in `README.md` whenever tooling is introduced.

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
