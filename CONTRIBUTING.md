# Contributing to WhiteBit Python SDK

Thank you for your interest in contributing! This document explains how to report bugs, suggest features, and submit code changes.

---

## Table of Contents

- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Development Setup](#development-setup)
- [Running Tests](#running-tests)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Code Style](#code-style)

---

## Reporting Bugs

Before opening an issue, please search existing issues to avoid duplicates.

When reporting a bug, include:

- Python version (`python --version`)
- SDK version (`pip show python-whitebit-sdk`)
- Minimal code snippet that reproduces the problem
- Full error traceback
- Expected vs actual behaviour

---

## Suggesting Features

Open an issue with the label **enhancement** and describe:

- The use case you are trying to solve
- The API endpoint involved (link to the [WhiteBit API docs](https://whitebit-exchange.github.io/api-docs/) if applicable)
- Any alternative approaches you considered

---

## Development Setup

1. **Fork** the repository and clone your fork:

   ```bash
   git clone https://github.com/YOUR_USERNAME/python-sdk.git
   cd python-sdk
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   pip install -e .
   ```

3. Create a feature branch:

   ```bash
   git checkout -b feature/my-feature
   ```

---

## Running Tests

```bash
python -m pytest tests/ -v
```

All tests use the `responses` library to mock HTTP calls — no real API credentials are required.

When adding a new endpoint or fixing a bug, add or update the corresponding test in `tests/test.py`.

---

## Submitting a Pull Request

1. Make sure all existing tests pass before submitting.
2. Add tests for any new functionality.
3. Keep commits focused — one logical change per commit.
4. Write a clear PR description explaining **what** changed and **why**.
5. Reference any related issue in the PR description (e.g. `Closes #42`).

Once submitted, your PR will be reviewed. Feedback may be requested before merging.

---

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/).
- Use type hints where possible.
- Keep method signatures consistent with existing clients (see `whitebit/trade/` for reference).
- Do not commit API keys, secrets, or any credentials.
