"""Every legacy alias must point at a canonical id that still exists.

Catches typo'd or orphaned alias targets. Direction stays alias -> canonical;
never reverse. After t1123, canonical = live mounts only (archived section removed).
"""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ONE = ROOT / "01_skill-integration"


class AliasTargets(unittest.TestCase):
    def test_alias_values_are_known_ids(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {
            m["id"]
            for m in (reg.get("mounts") or [])
            if isinstance(m, dict) and m.get("id")
        }
        self.assertGreaterEqual(len(ids), 20, "registry mounts not parsed")

        la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
        bad = [
            f"{k} -> {v}"
            for k, v in (la.get("aliases") or {}).items()
            if str(v) not in ids
        ]
        self.assertEqual(bad, [], "alias targets that are not live mount ids:\n" + "\n".join(bad))

    def test_coarse_alias_values_are_registry_coarse(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        coarse = {
            m.get("coarse") for m in (reg.get("mounts") or []) if isinstance(m, dict)
        }
        coarse.discard(None)
        for c in reg.get("coarse_ids") or []:
            if isinstance(c, dict) and c.get("id"):
                coarse.add(c["id"])
        la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
        bad = [
            f"{k} -> {v}"
            for k, v in (la.get("coarse_aliases") or {}).items()
            if str(v) not in coarse
        ]
        self.assertEqual(bad, [], "coarse alias targets not in registry:\n" + "\n".join(bad))


if __name__ == "__main__":
    unittest.main()
