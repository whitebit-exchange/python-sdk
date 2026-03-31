# Contributing to WhiteBit Python SDK

Thank you for your interest in contributing!

---

## Important: Auto-generated Core

The core SDK (`src/whitebit/`) is **automatically generated** from the WhiteBit API definition using [Fern](https://buildwithfern.com). This means:

- **Do not open PRs that modify files inside `src/whitebit/`** — changes will be overwritten on the next generation run.
- To request a new endpoint or fix an incorrect API definition, open an issue instead (see [Reporting Bugs](#reporting-bugs) and [Requesting Features](#requesting-features)).

---

## What you CAN contribute

| Area | How |
|---|---|
| **Bug reports** | Open an issue with reproduction steps |
| **Feature requests** | Open an issue describing the use case |
| **Examples** | Add or improve files in `examples/` |
| **Tests** | Add test cases in `tests/` |
| **Use cases & guides** | Real-world usage patterns, strategies, bots |
| **Documentation** | Fixes and improvements to `README.md` |

---

## Reporting Bugs

Before opening an issue, search existing ones to avoid duplicates.

Include:

- Python version (`python --version`)
- SDK version (`pip show whitebit-python-sdk`)
- Minimal code snippet that reproduces the problem
- Full error traceback
- Expected vs actual behaviour

---

## Requesting Features

Open an issue with the label **enhancement** and describe:

- The use case you are trying to solve
- The API endpoint involved (link to the [WhiteBit API docs](https://docs.whitebit.com/) if applicable)
- Any alternative approaches you considered

---

## Contributing Examples and Tests

Examples and tests are the best place to contribute code directly.

**Examples** live in `examples/` — feel free to add:
- New usage patterns for existing clients
- Real-world trading strategies or bots
- Integration patterns (e.g. asyncio, frameworks)

**Tests** live in `tests/test.py`. All tests use the `responses` library to mock HTTP calls — no real API credentials are needed.

```bash
# Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Run tests
python -m pytest tests/ -v
```

When adding a test:
1. Mock the HTTP call with `@responses.activate`
2. Cover both a success case and an error/missing-credentials case
3. Assert the request URL, method, body, and response

---

## Submitting a Pull Request

1. Fork the repo and create a branch: `git checkout -b feature/my-feature`
2. Make sure all existing tests pass
3. Keep commits focused — one logical change per commit
4. Reference any related issue in the PR description (e.g. `Closes #42`)

---

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use type hints where possible
- Do not commit API keys, secrets, or any credentials
