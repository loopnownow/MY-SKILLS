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

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "00_orchestrator"
GATES = ROOT / "00_orchestrator" / "gates.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="ignore")
