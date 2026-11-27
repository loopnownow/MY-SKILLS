"""Claim Map wiring: pre-draft plan exists, is pointed to, and is not a new fine id or gate."""
from __future__ import annotations

import unittest

import yaml

from tests.support import ONE, ROOT

CLAIM_MAP = ROOT / "05_manuscript" / "advanced" / "process" / "claim-map.md"
WRITE_PAPER_MODULE = ROOT / "05_manuscript" / "base" / "write-paper" / "MODULE.md"
WRITE_PAPER_SKILL = ROOT / "05_manuscript" / "base" / "write-paper" / "SKILL.md"
EVIDENCE = ROOT / "05_manuscript" / "advanced" / "process" / "evidence.md"
ROUTE = ROOT / "05_manuscript" / "advanced" / "route.md"


class ClaimMapContract(unittest.TestCase):
    def test_claim_map_file_exists(self) -> None:
        self.assertTrue(
            CLAIM_MAP.is_file(),
            "missing 05_manuscript/advanced/process/claim-map.md",
        )

    def test_hard_constraints_and_boundary_are_stated(self) -> None:
        text = CLAIM_MAP.read_text(encoding="utf-8")
        lowered = text.lower()
        required = (
            "weaken",
            "qualify",
            "delete",
            "invent",
            "locked",
            "mechanism",
            "clinical",
            "not a qc gate",
            "result-to-claim",
            "paper-claim-audit-gate",
            "claim-number-align",
            "evidence.md",
        )
        missing = [item for item in required if item not in lowered]
        self.assertEqual(missing, [], "claim-map.md missing required tokens")
        self.assertIn("must **not** emit", text)
        self.assertIn("RESULT_TO_CLAIM.json", text)

    def test_entry_and_evidence_pointers(self) -> None:
        sources = {
            "write-paper MODULE.md": WRITE_PAPER_MODULE,
            "write-paper SKILL.md": WRITE_PAPER_SKILL,
            "evidence.md": EVIDENCE,
            "route.md": ROUTE,
        }
        missing = [
            label
            for label, path in sources.items()
            if "claim-map.md" not in path.read_text(encoding="utf-8")
        ]
        self.assertEqual(missing, [], "claim-map.md pointer missing in: " + ", ".join(missing))

    def test_not_a_new_fine_id(self) -> None:
        registry = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {row["id"] for row in registry.get("fine_ids") or [] if isinstance(row, dict)}
        self.assertNotIn("claim-map", ids)
        self.assertNotIn("claim_map", ids)
