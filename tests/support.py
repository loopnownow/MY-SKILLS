"""Shared fixtures for the contract test suite.

Config
------
ROOT / ONE / GATES : repository root, control-plane folder, gate table
REGISTRY / ALIASES : routing index and retired-id alias map
ALLOW_*            : documented exceptions used by the path and hygiene guards

Run
---
    python -B -m unittest discover -s tests -v
"""
from __future__ import annotations

import functools
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "00_orchestrator"
GATES = ROOT / "00_orchestrator" / "gates.md"
REGISTRY = ONE / "registry.yaml"
ALIASES = ONE / "legacy_aliases.yaml"
VERSION = ROOT / "VERSION.txt"
INTEGRATION_MAP = ROOT / "INTEGRATION_MAP.md"
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "fixtures"}
ALLOW_MISSING_PREFIXES = ("docs/",)
ALLOW_LINE_MARKERS = ("<!-- negative-example -->",)
ALLOW_HISTORICAL_FILES = ("INTEGRATION_MAP.md",)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="ignore")


def md_files() -> list[Path]:
    """Tracked markdown files outside SKIP_DIRS, stable order."""
    return sorted(
        path for path in ROOT.rglob("*.md")
        if not (set(path.relative_to(ROOT).parts) & SKIP_DIRS)
    )


@functools.cache
def load_yaml(name: str) -> dict:
    return load_yaml_file(ONE / name)


@functools.cache
def load_yaml_file(path: Path) -> dict:
    return yaml.safe_load(read(path)) or {}


@functools.cache
def load_registry() -> dict:
    return load_yaml_file(REGISTRY)


@functools.cache
def load_aliases() -> dict:
    return (load_yaml_file(ALIASES) or {}).get("aliases") or {}
