"""Intake Brief: thin writing-entry summary, not a new form or gate."""
from __future__ import annotations

import unittest

import yaml

from tests.support import ONE, ROOT

BRIEF = ROOT / "05_manuscript" / "advanced" / "process" / "intake-brief.md"
WRITE_PAPER_MODULE = ROOT / "05_manuscript" / "base" / "write-paper" / "MODULE.md"
WRITE_PAPER_SKILL = ROOT / "05_manuscript" / "base" / "write-paper" / "SKILL.md"
ROUTE = ROOT / "05_manuscript" / "advanced" / "route.md"
HANDOFF = ROOT / "05_manuscript" / "advanced" / "handoff.md"
CLAIM_MAP = ROOT / "05_manuscript" / "advanced" / "process" / "claim-map.md"
STUDY_TYPE = ROOT / "05_manuscript" / "advanced" / "process" / "study-type.md"


class IntakeBriefContract(unittest.TestCase):
    def test_brief_file_exists(self) -> None:
        self.assertTrue(
            BRIEF.is_file(),
            "missing 05_manuscript/advanced/process/intake-brief.md",
        )

    def test_thin_summary_and_hard_constraints_are_stated(self) -> None:
        text = BRIEF.read_text(encoding="utf-8")
        lowered = text.lower()
        required = (
            "not a qc gate",
            "not a new form",
            "research question",
            "study type",
            "main claims",
            "data / analyses in hand",
            "figure / table constraints",
            "locked decisions",
            "missing / unverified",
            "do not fill a gap by guessing",
            "do not invent",
            "user-locked",
            "unperformed step",
            "study-type.md",
            "claim-map.md",
            "figure-table-plan.md",
        )
        missing = [item for item in required if item not in lowered]
        self.assertEqual(missing, [], "intake-brief.md missing required tokens")

    def test_entry_and_route_pointers(self) -> None:
        sources = {
            "write-paper MODULE.md": WRITE_PAPER_MODULE,
            "write-paper SKILL.md": WRITE_PAPER_SKILL,
            "route.md": ROUTE,
            "handoff.md": HANDOFF,
            "claim-map.md": CLAIM_MAP,
            "study-type.md": STUDY_TYPE,
        }
        missing = [
            label
            for label, path in sources.items()
            if "intake-brief.md" not in path.read_text(encoding="utf-8")
        ]
        self.assertEqual(missing, [], "intake-brief.md pointer missing in: " + ", ".join(missing))

    def test_not_a_new_fine_id(self) -> None:
        registry = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {row["id"] for row in registry.get("fine_ids") or [] if isinstance(row, dict)}
        self.assertNotIn("intake-brief", ids)
        self.assertNotIn("intake_brief", ids)
        self.assertNotIn("manuscript-intake-brief", ids)
