"""CHG-20260926-009: hand-kept mirrors of registry.yaml stay in sync."""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ONE = ROOT / "01_skill-integration"


def registry() -> dict:
    return yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))


class RegistryMirrors(unittest.TestCase):
    def test_b_source_yaml_retired(self) -> None:
        """Remote B source yaml retired; live mounts use in-repo my-skills."""
        reg = registry()
        live_b = [m["id"] for m in reg["mounts"] if m.get("source") == "my-skills-base"]
        self.assertEqual(live_b, [])
        self.assertFalse((ONE / "sources" / "b-my-skills-base.yaml").exists())
        live_a = [m for m in reg["mounts"] if m.get("source") == "my-skills"]
        self.assertGreaterEqual(len(live_a), 20)
        self.assertEqual(reg["default_source"]["id"], "my-skills")


if __name__ == "__main__":
    unittest.main()
