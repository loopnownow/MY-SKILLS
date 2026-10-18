"""CHG-20260926-009: hand-kept mirrors of registry.yaml stay in sync."""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "01_skill-integration"


def registry() -> dict:
    return yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))


class RegistryMirrors(unittest.TestCase):
    def test_default_source_in_repo_my_skills(self) -> None:
        """Live mounts use in-repo my-skills; no my-skills-base source id."""
        reg = registry()
        bad = [m["id"] for m in reg["mounts"] if m.get("source") == "my-skills-base"]
        self.assertEqual(bad, [])
        arch_bad = [m["id"] for m in (reg.get("archived") or []) if m.get("source") == "my-skills-base"]
        self.assertEqual(arch_bad, [])
        self.assertFalse((ONE / "sources" / "b-my-skills-base.yaml").exists())
        live_a = [m for m in reg["mounts"] if m.get("source") == "my-skills"]
        self.assertGreaterEqual(len(live_a), 20)
        self.assertEqual(reg["default_source"]["id"], "my-skills")


if __name__ == "__main__":
    unittest.main()
