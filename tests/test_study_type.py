"""Study-type route: coarse writing constraints hooked into the existing 05 route."""
from __future__ import annotations

import unittest

import yaml

from tests.support import ONE, ROOT

STUDY_TYPE = ROOT / "05_manuscript" / "advanced" / "process" / "study-type.md"
WRITE_PAPER_MODULE = ROOT / "05_manuscript" / "base" / "write-paper" / "MODULE.md"
WRITE_PAPER_SKILL = ROOT / "05_manuscript" / "base" / "write-paper" / "SKILL.md"
ROUTE = ROOT / "05_manuscript" / "advanced" / "route.md"


class StudyTypeRouteContract(unittest.TestCase):
    def test_study_type_file_exists(self) -> None:
        self.assertTrue(
            STUDY_TYPE.is_file(),
            "missing 05_manuscript/advanced/process/study-type.md",
        )

    def test_coarse_classes_and_hard_constraints_are_stated(self) -> None:
        text = STUDY_TYPE.read_text(encoding="utf-8")
        lowered = text.lower()
        required = (
            "observational",
            "diagnostic or prognostic model",
            "radiomics",
            "mechanism",
            "associated with",
            "internal validation",
            "external validation",
            "clinical utility",
            "auc",
            "clinical benefit",
            "locked",
            "do not guess",
            "do not invent",
            "strobe",
            "tripod",
            "stard",
            "claim",
            "not a second router",
            "claim-map.md",
        )
        missing = [item for item in required if item not in lowered]
        self.assertEqual(missing, [], "study-type.md missing required tokens")

    def test_entry_and_route_pointers(self) -> None:
        sources = {
            "write-paper MODULE.md": WRITE_PAPER_MODULE,
            "write-paper SKILL.md": WRITE_PAPER_SKILL,
            "route.md": ROUTE,
        }
        missing = [
            label
            for label, path in sources.items()
            if "study-type.md" not in path.read_text(encoding="utf-8")
        ]
        self.assertEqual(missing, [], "study-type.md pointer missing in: " + ", ".join(missing))

    def test_route_says_not_a_second_router(self) -> None:
        text = ROUTE.read_text(encoding="utf-8").lower()
        self.assertIn("study-type.md", text)
        self.assertIn("not a second router", text)

    def test_not_a_new_fine_id(self) -> None:
        registry = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {row["id"] for row in registry.get("fine_ids") or [] if isinstance(row, dict)}
        self.assertNotIn("study-type", ids)
        self.assertNotIn("study_type", ids)
        self.assertNotIn("study-type-route", ids)
