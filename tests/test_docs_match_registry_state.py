"""Docs must not advertise a registry state that does not exist.

2026-10-20: registry holds MOUNTED + ARCHIVED only (0 PROPOSED), but README and
ARCHITECTURE still said non-default fine ids were "mixed PROPOSED/MOUNTED".
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "01_skill-integration"
DOCS = ("README.md", "ARCHITECTURE.md")


class DocsMatchRegistry(unittest.TestCase):
    def setUp(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        self.mounts = [m for m in (reg.get("mounts") or []) if isinstance(m, dict)]
        self.proposed = [m for m in self.mounts if m.get("status") == "PROPOSED"]

    def test_no_stale_proposed_claim(self) -> None:
        if self.proposed:
            self.skipTest("registry currently has PROPOSED rows")
        for name in DOCS:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotRegex(
                text,
                r"PROPOSED\s*/\s*MOUNTED",
                f"{name} still claims non-default ids are mixed PROPOSED/MOUNTED "
                "while the registry has no PROPOSED row",
            )

    def test_mounted_paths_are_canonical(self) -> None:
        missing: list[str] = []
        for m in self.mounts:
            if m.get("status") != "MOUNTED":
                continue
            path = str(m.get("path") or "")
            if not path:
                missing.append(f"{m.get('id')}: no path")
                continue
            if not (ROOT / path).exists():
                missing.append(f"{m.get('id')}: {path}")
        self.assertEqual(missing, [], "MOUNTED paths missing:\n" + "\n".join(missing))

    def test_archived_ids_survive_only_as_history(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        archived = {a["id"] for a in (reg.get("archived") or []) if isinstance(a, dict)}
        mounted = {m["id"] for m in self.mounts}
        overlap = archived & mounted
        self.assertEqual(overlap, set(), f"id both MOUNTED and ARCHIVED: {sorted(overlap)}")


if __name__ == "__main__":
    unittest.main()
