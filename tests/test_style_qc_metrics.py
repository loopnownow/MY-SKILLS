"""Style QC locatable metrics and section checks: same QCV report, not a second score."""
from __future__ import annotations

import unittest

import yaml

from tests.support import ONE, ROOT

STYLE_QC = ROOT / "05_manuscript" / "qc" / "style-qc" / "style-qc.md"
SCORECARDS = ROOT / "05_manuscript" / "qc" / "style-qc" / "scorecards.md"
QC_README = ROOT / "05_manuscript" / "qc" / "README.md"


class StyleQcMetricsContract(unittest.TestCase):
    def test_style_qc_file_exists(self) -> None:
        self.assertTrue(STYLE_QC.is_file(), "missing 05_manuscript/qc/style-qc/style-qc.md")

    def test_not_a_second_scoring_system(self) -> None:
        text = STYLE_QC.read_text(encoding="utf-8")
        lowered = text.lower()
        self.assertIn("not a second scoring system", lowered)
        self.assertIn("pass", lowered)
        self.assertIn("warn", lowered)
        self.assertIn("fail-soft", lowered)
        # existing scorecards remain the only numeric totals
        self.assertIn("QCV-SCORE-1", text)
        self.assertIn("QCV-SCORE-2", text)
        cards = SCORECARDS.read_text(encoding="utf-8").lower()
        self.assertIn("same pass / warn / fail-soft", cards)
        self.assertIn("do not add a third scorecard", cards)

    def test_locatable_metrics_and_issue_rows_are_stated(self) -> None:
        text = STYLE_QC.read_text(encoding="utf-8")
        lowered = text.lower()
        required = (
            "qcv-len-2",
            "qcv-conn-1",
            "qcv-abbr-1",
            "qcv-num-1",
            "qcv-rep-1",
            "sentence-pattern repetition",
            "template phrases",
            "abbreviation",
            "auc format",
            "vocabulary over-repetition",
            "id | location | type | excerpt | reason | direction | verdict",
            "do not import an external",
            "labeled",
            "locked",
        )
        missing = [item for item in required if item not in lowered]
        self.assertEqual(missing, [], "style-qc.md missing locatable-metric tokens")

    def test_section_differences_and_no_blanket_limitation_ban(self) -> None:
        text = STYLE_QC.read_text(encoding="utf-8").lower()
        required = (
            "qcv-sec-1",
            "qcv-sec-2",
            "qcv-sec-3",
            "front-load a mechanism",
            "prior evidence",
            "proven clinical benefit",
            "do not impose a blanket ban on limitations",
        )
        missing = [item for item in required if item not in text]
        self.assertEqual(missing, [], "style-qc.md missing section-difference tokens")

    def test_human_judgement_is_not_auto_verdict(self) -> None:
        text = STYLE_QC.read_text(encoding="utf-8").lower()
        required = (
            "do not auto-assign",
            "whether the argument actually holds",
            "scientifically reasonable",
            "tone is too strong",
            "factually accurate",
            "target journal",
        )
        missing = [item for item in required if item not in text]
        self.assertEqual(missing, [], "style-qc.md missing human-judgement tokens")

    def test_readme_still_points_at_existing_style_qc(self) -> None:
        readme = QC_README.read_text(encoding="utf-8")
        self.assertIn("style-qc/style-qc.md", readme)
        self.assertIn("not a second score", readme.lower())

    def test_not_a_new_fine_id(self) -> None:
        registry = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        ids = {row["id"] for row in registry.get("fine_ids") or [] if isinstance(row, dict)}
        self.assertNotIn("style-metrics", ids)
        self.assertNotIn("style_metrics", ids)
        self.assertNotIn("style-qc-metrics", ids)
