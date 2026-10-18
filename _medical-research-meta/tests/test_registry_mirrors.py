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
    def test_b_source_yaml_matches_registry(self) -> None:
        reg = registry()
        reg_b = {m["id"]: m for m in reg["mounts"] if m["source"] == "my-skills-base"}
        b = yaml.safe_load((ONE / "sources" / "b-my-skills-base.yaml").read_text(encoding="utf-8"))
        yaml_b = {s["id"]: s for s in b["skills"]}
        self.assertEqual(sorted(reg_b), sorted(yaml_b))
        for fid, m in reg_b.items():
            self.assertEqual(yaml_b[fid]["path"], m["path"], fid)
            self.assertEqual(yaml_b[fid]["coarse"], m["coarse"], fid)


if __name__ == "__main__":
    unittest.main()
