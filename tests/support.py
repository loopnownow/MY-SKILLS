"""Shared fixtures for the contract test suite.

Config
------
ROOT / ONE / GATES : repository root, control-plane folder, gate table
read               : UTF-8-sig tolerant file reader

Run
---
    python -B -m unittest discover -s tests -v
"""
from __future__ import annotations

import os
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "00_orchestrator"
GATES = ROOT / "00_orchestrator" / "gates.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="ignore")


ALLOW_MISSING_SIBLINGS_ENV = "MY_SKILLS_ALLOW_MISSING_SIBLINGS"


def allow_missing_siblings() -> bool:
    """True only when MY_SKILLS_ALLOW_MISSING_SIBLINGS is set (partial checkout)."""
    return os.environ.get(ALLOW_MISSING_SIBLINGS_ENV, "").strip().lower() in (
        "1",
        "true",
        "yes",
    )


def require_resolved(value, what: str, hint: str = ""):
    """Return `value` when resolved; skip only on an explicit partial checkout.

    Default is fail: a missing MY-CODES tool or sibling checkout must redden the
    suite, never go green as a silent skip.
    """
    if value is not None:
        return value
    if allow_missing_siblings():
        raise unittest.SkipTest(f"{what} absent (allowed by {ALLOW_MISSING_SIBLINGS_ENV})")
    raise AssertionError(
        f"{what} not found{hint}; clone the sibling repo or set "
        f"{ALLOW_MISSING_SIBLINGS_ENV}=1 only on a partial checkout"
    )
