"""Docs must not advertise a registry state that does not exist.

Live registry = MOUNTED mounts only (no PROPOSED / ARCHIVED sections).
"""
from __future__ import annotations

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

    def test_no_archived_section(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        self.assertNotIn("archived", reg, "registry must not carry archived: bloat")
        self.assertFalse(reg.get("archived"), "archived must be empty/absent")


if __name__ == "__main__":
    unittest.main()
