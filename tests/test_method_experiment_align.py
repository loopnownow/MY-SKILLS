"""Method-experiment alignment: thin two-way trace, not a new gate."""
from __future__ import annotations

import unittest

import yaml

from tests.support import ONE, ROOT

ALIGN = ROOT / "05_manuscript" / "advanced" / "process" / "method-experiment-align.md"
WRITE_PAPER_MODULE = ROOT / "05_manuscript" / "base" / "write-paper" / "MODULE.md"
WRITE_PAPER_SKILL = ROOT / "05_manuscript" / "base" / "write-paper" / "SKILL.md"
METHODS = ROOT / "05_manuscript" / "base" / "write-paper" / "radiology-writing" / "methods.md"
RESULTS = ROOT / "05_manuscript" / "base" / "write-paper" / "radiology-writing" / "results.md"
ROUTE = ROOT / "05_manuscript" / "advanced" / "route.md"
CLAIM_MAP = ROOT / "05_manuscript" / "advanced" / "process" / "claim-map.md"
STUDY_TYPE = ROOT / "05_manuscript" / "advanced" / "process" / "study-type.md"
RESULT_TO_CLAIM = ROOT / "05_manuscript" / "qc" / "result-to-claim.md"


class MethodExperimentAlignContract(unittest.TestCase):
    def test_align_file_exists(self) -> None:
        self.assertTrue(
            ALIGN.is_file(),
            "missing 05_manuscript/advanced/process/method-experiment-align.md",
        )

    def test_hard_constraints_and_two_way_check_are_stated(self) -> None:
        text = ALIGN.read_text(encoding="utf-8")
        lowered = text.lower()
        required = (
            "not a qc gate",
            "two-way check",
            "pre-stated reason",
            "corresponding method",
            "traced to an analysis described in methods",
            "traced to results or to verified literature",
            "was not described in methods",
            "exploratory analysis",
            "confirmatory",
            "feature selection",
            "data leakage",
            "internal validation",
            "external validation",
            "do not invent",
            "user-locked",
            "unperformed step",
            "result-to-claim.md",
            "reporting-guideline-route.md",
            "ml-experiment-checklist.md",
        )
        missing = [item for item in required if item not in lowered]
        self.assertEqual(missing, [], "method-experiment-align.md missing required tokens")

    def test_entry_and_host_pointers(self) -> None:
        sources = {
            "write-paper MODULE.md": WRITE_PAPER_MODULE,
            "write-paper SKILL.md": WRITE_PAPER_SKILL,
            "methods.md": METHODS,
            "results.md": RESULTS,
            "route.md": ROUTE,
            "claim-map.md": CLAIM_MAP,
            "study-type.md": STUDY_TYPE,
            "result-to-claim.md": RESULT_TO_CLAIM,
        }
        missing = [
            label
            for label, path in sources.items()
            if "method-experiment-align.md" not in path.read_text(encoding="utf-8")
        ]
        self.assertEqual(missing, [], "method-experiment-align.md pointer missing in: " + ", ".join(missing))

    def test_not_a_new_fine_id(self) -> None:
        registry = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {row["id"] for row in registry.get("fine_ids") or [] if isinstance(row, dict)}
        self.assertNotIn("method-experiment-align", ids)
        self.assertNotIn("method_experiment_align", ids)
        self.assertNotIn("method-experiment-alignment", ids)
