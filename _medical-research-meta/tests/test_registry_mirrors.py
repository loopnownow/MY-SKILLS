"""CHG-20260926-009: hand-kept mirrors of registry.yaml stay in sync."""
from __future__ import annotations

import collections
import re
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
ONE = ROOT / "01_skill-discovery-integration"


def registry() -> dict:
    return yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8"))


class RegistryMirrors(unittest.TestCase):
    def test_b_source_yaml_matches_registry(self) -> None:
        reg = registry()
        reg_b = {m["id"]: m for m in reg["mounts"] if m["source"] == "my-skills-capabilities"}
        b = yaml.safe_load((ONE / "sources" / "b-my-skills-capabilities.yaml").read_text(encoding="utf-8"))
        yaml_b = {s["id"]: s for s in b["skills"]}
        self.assertEqual(sorted(reg_b), sorted(yaml_b))
        for fid, m in reg_b.items():
            self.assertEqual(yaml_b[fid]["path"], m["path"], fid)
            self.assertEqual(yaml_b[fid]["coarse"], m["coarse"], fid)

    def test_hybrid_pointer_sections_match_registry(self) -> None:
        reg = registry()
        want = collections.Counter(m["coarse"] for m in reg["mounts"])
        text = (ONE / "mounts" / "hybrid-mount-pointers.md").read_text(encoding="utf-8")
        sections = re.split(r"^## (?=\d+\. )", text, flags=re.M)[1:]
        self.assertEqual(len(sections), len(want), msg=str(want))
        seen = []
        for sec in sections:
            head = re.match(r"\d+\. (\S+?)（(\d+)）", sec)
            self.assertIsNotNone(head, sec[:40])
            coarse, n = head.group(1), int(head.group(2))
            rows = re.findall(r"^\| [^|]+ \| [^|]+ \| `([a-z0-9-]+)`", sec, flags=re.M)
            self.assertEqual(n, want[coarse], coarse)
            self.assertEqual(len(rows), n, f"{coarse}: {rows}")
            seen += rows
        self.assertEqual(sorted(seen), sorted(m["id"] for m in reg["mounts"]))


if __name__ == "__main__":
    unittest.main()
