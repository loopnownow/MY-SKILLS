"""Figure/table plan: thin display-need note hooked into the existing 05 route."""
from __future__ import annotations

import unittest

import yaml

from tests.support import ONE, ROOT

PLAN = ROOT / "05_manuscript" / "advanced" / "process" / "figure-table-plan.md"
WRITE_PAPER_MODULE = ROOT / "05_manuscript" / "base" / "write-paper" / "MODULE.md"
WRITE_PAPER_SKILL = ROOT / "05_manuscript" / "base" / "write-paper" / "SKILL.md"
ROUTE = ROOT / "05_manuscript" / "advanced" / "route.md"
CLAIM_MAP = ROOT / "05_manuscript" / "advanced" / "process" / "claim-map.md"


class FigureTablePlanContract(unittest.TestCase):
    def test_plan_file_exists(self) -> None:
        self.assertTrue(
            PLAN.is_file(),
            "missing 05_manuscript/advanced/process/figure-table-plan.md",
        )

    def test_hard_constraints_and_seat_split_are_stated(self) -> None:
        text = PLAN.read_text(encoding="utf-8")
        lowered = text.lower()
        required = (
            "serves claim",
            "awaiting data",
            "do not simulate",
            "locked",
            "do not invent",
            "plot-figures",
            "draw-flowchart",
            "claim-map.md",
            "not a qc gate",
            "why a display is needed",
        )
        missing = [item for item in required if item not in lowered]
        self.assertEqual(missing, [], "figure-table-plan.md missing required tokens")

    def test_entry_claim_map_and_route_pointers(self) -> None:
        sources = {
            "write-paper MODULE.md": WRITE_PAPER_MODULE,
            "write-paper SKILL.md": WRITE_PAPER_SKILL,
            "route.md": ROUTE,
            "claim-map.md": CLAIM_MAP,
        }
        missing = [
            label
            for label, path in sources.items()
            if "figure-table-plan.md" not in path.read_text(encoding="utf-8")
        ]
        self.assertEqual(missing, [], "figure-table-plan.md pointer missing in: " + ", ".join(missing))

    def test_not_a_new_fine_id(self) -> None:
        registry = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {row["id"] for row in registry.get("fine_ids") or [] if isinstance(row, dict)}
        self.assertNotIn("figure-table-plan", ids)
        self.assertNotIn("figure_table_plan", ids)
