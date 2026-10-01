"""Pre-submit consistency checks are YAML-parseable and wired into 04/05/06.

Failure classes come from the SSD scoring-report lessons (stats/text, sister
papers, circular analysis, process language, inclusion scale, citation hygiene,
paragraph lock). The test locks the check ids, not any manuscript's numbers.
"""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_IDS = (
    "stat_vs_threshold",
    "correlation_implied_n",
    "multiplicity_disclosure",
    "relative_denominator",
    "overlap_statement_and_citation",
    "shared_table_sample_overlap",
    "sister_paper_p_reconciliation",
    "no_confirmatory_p_same_cohort",
    "nested_roi_collinearity",
    "score_transform_identity",
    "pipeline_tokens_banned",
    "source_attribution_banned",
    "placeholder_and_internal_labels_banned",
    "repeated_disclaimer",
    "empty_retrieval_and_scan_placeholders",
    "cutoff_vs_included_distribution",
    "iqr_scale_sanity",
    "consecutive_same_cite",
    "claim_matches_source",
    "no_unverified_cross_copy",
    "year_volume_from_source",
    "paragraph_lock",
    "intro_opening_has_citations",
    "split_names_are_sets",
    "approach_not_framework",
)

REQUIRED_CLASSES = (
    "stats_text",
    "cross_manuscript",
    "circular_analysis",
    "process_language",
    "inclusion_scale",
    "citation_hygiene",
    "writing_craft",
)

WRITING = ROOT / "05_manuscript" / "personal" / "pre-submit-consistency.md"
REVIEW = ROOT / "06_review" / "personal" / "cross-manuscript-qc.md"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError(f"{path.name} must open with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AssertionError(f"{path.name} frontmatter is not closed")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise AssertionError(f"{path.name} frontmatter did not parse to a mapping")
    return data, text


class PreSubmitFrontmatter(unittest.TestCase):
    def test_writing_checks_parse_and_cover_every_class(self) -> None:
        data, body = frontmatter(WRITING)
        self.assertEqual(data["owner"], "05_manuscript")
        self.assertEqual(data["audience"], "Aitee")
        self.assertEqual(data["on_number_conflict"], "comment_only")
        checks = data["checks"]
        self.assertIsInstance(checks, list)
        ids = [item["id"] for item in checks]
        classes = [item["class"] for item in checks]
        self.assertCountEqual(ids, REQUIRED_IDS)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertCountEqual(set(classes), REQUIRED_CLASSES)
        for cid in REQUIRED_IDS:
            self.assertIn(f"### {cid}", body)

    def test_review_frontmatter_parse_and_load_order(self) -> None:
        data, body = frontmatter(REVIEW)
        self.assertEqual(data["owner"], "06_review")
        self.assertEqual(data["audience"], "Lee")
        self.assertEqual(data["order"], ["statement_consistency", "data_consistency"])
        self.assertEqual(data["on_number_conflict"], "annotate_only")
        self.assertEqual(data["journal_language"], "en")
        self.assertEqual(data["user_summary_language"], "zh")
        self.assertEqual(
            data["runs_checks_from"],
            "05_manuscript/personal/pre-submit-consistency.md",
        )
        for cid in REQUIRED_IDS:
            self.assertIn(cid, body)
        self.assertIn("Do not invent", body)
        self.assertIn("Chinese", body)


class PreSubmitWiring(unittest.TestCase):
    def test_parent_skills_load_the_checklists(self) -> None:
        five = read("05_manuscript/SKILL.md")
        six = read("06_review/SKILL.md")
        four = read("04_analysis/SKILL.md")
        gates = read("00_orchestrator/gates.md")
        self.assertIn("personal/pre-submit-consistency.md", five)
        self.assertIn("personal/cross-manuscript-qc.md", six)
        self.assertIn("05_manuscript/personal/pre-submit-consistency.md", four)
        self.assertIn("05_manuscript/personal/pre-submit-consistency.md", gates)
        self.assertIn("06_review/personal/cross-manuscript-qc.md", gates)

    def test_extended_personal_files_hold_the_rules(self) -> None:
        stats = read("04_analysis/personal/stats-consistency.md")
        checklist = read("04_analysis/personal/stats-checklist.md")
        for token in (
            "stat_vs_threshold",
            "correlation_implied_n",
            "multiplicity_disclosure",
            "relative_denominator",
            "no_confirmatory_p_same_cohort",
            "nested_roi_collinearity",
            "score_transform_identity",
            "cutoff_vs_included_distribution",
            "iqr_scale_sanity",
            "sister_paper_p_reconciliation",
        ):
            self.assertIn(token, stats, token)
            self.assertIn(token, checklist, token)
        self.assertIn("do not invent", stats.lower())

        voice = read("05_manuscript/personal/voice-portrait.md")
        self.assertIn("Paragraph lock", voice)
        self.assertIn("pre-submit-consistency.md", voice)
        self.assertIn("training set", voice)
        self.assertIn("opening paragraph", voice.lower())

        cites = read("05_manuscript/personal/citation-and-language.md")
        for token in (
            "consecutive_same_cite",
            "claim_matches_source",
            "no_unverified_cross_copy",
            "year_volume_from_source",
        ):
            self.assertIn(token, cites, token)
        self.assertIn("Methods: **no citations**", cites)

        banned = read("05_manuscript/personal/forbidden-phrases.md")
        for token in (
            "TRAIN_RATIO",
            "as stated by the source",
            "待补",
            "标签未与方案核对",
            "framework",
            "approach",
        ):
            self.assertIn(token, banned, token)

        aitor = read("05_manuscript/personal/Aitor-format.md")
        self.assertIn("Methods: no citations", aitor)
        self.assertIn("intro_opening_has_citations", aitor)
        self.assertIn("training set", aitor)

        score = read("05_manuscript/personal/introduction-scorecard.md")
        for code in ("FLU-4", "CIT-5", "CIT-6", "CIT-7"):
            self.assertIn(code, score, code)

        habits = read("06_review/personal/review-comment-habits.md")
        self.assertIn("statement consistency", habits.lower())
        self.assertIn("cross-manuscript-qc.md", habits)
        self.assertIn("do not invent", habits.lower())
        self.assertIn("TRAIN_RATIO", habits)

        style = read("06_review/personal/personal-review-style.md")
        self.assertIn("### 4.9 Pre-submit consistency requests", style)
        self.assertIn("cross-manuscript-qc.md", style)
        self.assertIn("Do not invent the number", style)
        self.assertIn("voxel-wise or cluster-forming", style)

        structures = read("05_manuscript/personal/structures.md")
        self.assertIn("paragraph_lock", structures)
        deai = read("05_manuscript/personal/de-ai.md")
        self.assertIn("TRAIN_RATIO", deai)
        self.assertIn("approach", deai)


if __name__ == "__main__":
    unittest.main()
