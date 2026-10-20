"""Every legacy alias must point at a canonical id that still exists.

Catches typo'd or orphaned alias targets (e.g. an alias pointing at an id that
was itself archived away). Direction stays alias -> canonical; never reverse.
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
        ids = set()
        for m in reg.get("mounts") or []:
            if isinstance(m, dict) and m.get("id"):
                ids.add(m["id"])
        for a in reg.get("archived") or []:
            if isinstance(a, dict) and a.get("id"):
                ids.add(a["id"])
        self.assertGreaterEqual(len(ids), 40, "registry ids not parsed")

        la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8")) or {}
        bad = [
            f"{k} -> {v}"
            for k, v in (la.get("aliases") or {}).items()
            if str(v) not in ids
        ]
        self.assertEqual(bad, [], "alias targets that are not registry ids:\n" + "\n".join(bad))

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
