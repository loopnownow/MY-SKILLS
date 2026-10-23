"""Five control-plane QC checks. No LLM."""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class FiveFixes(unittest.TestCase):
    def test_reseived_study_folder_alias_parses_as_accepted(self) -> None:
        state = yaml.safe_load(
            (ROOT / "00_orchestrator" / "templates" / "project-state.yaml").read_text(encoding="utf-8")
        )
        aliases = state["study_folder_stage_aliases"]
        self.assertEqual(aliases["preparing"], "drafting")
        self.assertEqual(aliases["polishing"], "pre-submit")
        self.assertEqual(aliases["submitting"], "in-review")
        self.assertEqual(aliases["reseived"], "accepted")
        self.assertEqual(aliases.get("received"), "accepted")
        self.assertNotIn("reseived", (state.get("pipeline") or {}).get("stage", ""))
        self.assertNotIn("preparing", (state.get("pipeline") or {}).get("stage", ""))


if __name__ == "__main__":
    unittest.main()
