# Test Case Generation API

This repository now contains a runnable MVP of the "test case generation open service" described in the existing PRD and UED assets under `docs/`.

## Project layout

- `src/test_case_generation_api/` production code
- `tests/` unit tests
- `docs/` product, architecture, and detailed design documents
- `assets/` reserved for future static assets
- `scripts/` local developer entrypoints

## Development commands

- `python scripts/run_server.py` starts the local HTTP server on `127.0.0.1:8000`
- `python -m unittest discover -s tests -v` runs the unit test suite

## Implemented MVP scope

- application access creation and lookup
- HMAC signature authentication for API calls
- synchronous and asynchronous test case generation
- task status query and failed task retry
- in-memory rate limiting and audit logging

## Notes

- Data is stored in memory for the current process only.
- The implementation intentionally stays dependency-light so it can run in the current workspace without extra installation steps.
