"""Banned leftover vocabulary in the live tree.

Historical names may live in tests/retired_ids.py, CHANGELOG.md (brief notes),
route-contract must_not_contain lists, and LICENSE_NOTE provenance. They must
not reappear as live pack slugs, layer names, env vars, or triggers.
"""
from __future__ import annotations

from pathlib import Path
import re
import unittest

from tests.support import ROOT

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "tests"}
SCAN_SUFFIXES = {".md", ".yaml", ".yml", ".txt", ".tsv", ".py", ".json"}

# Brief CHANGELOG notes may mention a retired word once as history.
CHANGELOG_ALLOW = ROOT / "CHANGELOG.md"
REGISTRY_ALLOW = ROOT / "00_orchestrator" / "registry.yaml"
ROUTE_CONTRACT = ROOT / "00_orchestrator" / "route-contract.yaml"

HUMANIZE = re.compile(r"(?i)\bhumanize\b")

LITERALS = (
    "01_skill-integration",
    "04_analysis",
    "write-venue",
    "response-tone-polisher",
    "ODOC_CODE",
    "G-04",
    "G-CIT",
    "0doc",
    "0del",
    "0Grok",
    "00ds",
)

PERSONAL_LAYER = re.compile(
    r"(?i)("
    r"个人修订层"
    r"|personal layer"
    r"|`personal` layer"
    r"|layer name `personal`"
    r"|layer（personal"
    r"|layer \(personal"
    r"|advanced/personal style"
    r"|retired `personal` layer"
    r")"
)
MOUNT_WORDS = re.compile(r"(?i:(\bmount(?:ed)?\b)|\bMOUNTED\b)|\bPROPOSED\b")
HOUSE_TRIGGER = re.compile(r"(?i)(_house|Manuscript_\*?_house)")
JINSHAN_SLUG = re.compile(
    r"(?i)(jinshan-form-pack|jinshanyiyuan|jinshanquweijianwei|jinshan-form)"
)

PROVENANCE_NAMES = {"LICENSE_NOTE.txt", "polite_expressions.json"}


def _iter_files():
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SCAN_SUFFIXES:
            continue
        if SKIP_DIRS & set(path.parts):
            continue
        yield path


class BannedWords(unittest.TestCase):
    def test_retired_tokens_absent_from_live_tree(self) -> None:
        bad: list[str] = []
        for path in _iter_files():
            rel = path.relative_to(ROOT).as_posix()
            text = path.read_text(encoding="utf-8", errors="ignore")
            is_changelog = path.resolve() == CHANGELOG_ALLOW.resolve()
            is_registry = path.resolve() == REGISTRY_ALLOW.resolve()
            is_route = path.resolve() == ROUTE_CONTRACT.resolve()
            is_prov = path.name in PROVENANCE_NAMES
            for i, line in enumerate(text.splitlines(), 1):
                loc = f"{rel}:{i}: {line.strip()[:160]}"
                for lit in LITERALS:
                    if lit not in line:
                        continue
                    if is_changelog:
                        continue
                    if is_route and lit in {"write-venue", "response-tone-polisher"}:
                        continue
                    if is_prov and lit == "response-tone-polisher":
                        continue
                    bad.append(loc)
                if HUMANIZE.search(line) and not is_changelog:
                    bad.append(loc)
                if PERSONAL_LAYER.search(line) and not is_changelog:
                    bad.append(loc)
                if MOUNT_WORDS.search(line):
                    if is_changelog:
                        continue
                    if is_registry and re.search(r"\bPROPOSED\b", line) and not re.search(r"(?i)\b(mount|mounted|MOUNTED)\b", line):
                        continue
                    # route / tests already skipped; allow "unmount" ? not listed
                    bad.append(loc)
                if HOUSE_TRIGGER.search(line) and not is_changelog:
                    bad.append(loc)
                if JINSHAN_SLUG.search(line) and not is_changelog:
                    bad.append(loc)
        # de-dup while preserving order
        seen = []
        seen_set = set()
        for item in bad:
            if item in seen_set:
                continue
            seen_set.add(item)
            seen.append(item)
        self.assertEqual(
            seen,
            [],
            "banned leftover vocabulary in the live tree:\n" + "\n".join(seen[:60]),
        )
