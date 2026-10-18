"""Pre-submit consistency checks are YAML-parseable and wired into 04/05/06.

Failure classes come from the SSD scoring-report lessons (stats/text, sister
papers, circular analysis, process language, inclusion scale, citation hygiene,
paragraph lock). The test locks the check ids, not any manuscript's numbers.

Wave2 path map (2026-10-17 reorg) + domain qc/ (2026-10-18):
- 05_manuscript/personal/pre-submit-consistency.md -> 00 refs -> 05_manuscript/qc/manuscript-local-qc.md (Part B)
- 06_review/personal/cross-manuscript-qc.md -> 00 refs -> 06_review/qc/cross-manuscript-qc.md
- stats-consistency/stats-checklist -> 04_analysis/qc/report-checks.md
- forbidden-phrases -> 05_manuscript/base/vocab/L1/ban-phrases.md
- introduction-scorecard -> manuscript-local-qc.md Part A
- personal-review-style -> 06_review/personal/review.md
- word-edit-rules -> 06_review/personal/word-edit.md
- personal-response-style -> 07_response/personal/response.md
- structures.md / de-ai.md / review-resolution.md / review-comment-habits.md -> archived under 0del
"""
from __future__ import annotations

import re
import subprocess
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE_VOCAB = ROOT / "05_manuscript" / "base"

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

WRITING = ROOT / "05_manuscript" / "qc" / "manuscript-local-qc.md"
REVIEW = ROOT / "06_review" / "qc" / "cross-manuscript-qc.md"


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def embedded_frontmatter(path: Path, *, name: str | None = None) -> tuple[dict, str]:
    """Parse the first YAML frontmatter block, even if a banner precedes it."""
    text = path.read_text(encoding="utf-8")
    if name:
        marker = f"---\nname: {name}\n"
        start = text.find(marker)
        if start < 0:
            raise AssertionError(f"{path.name} missing embedded frontmatter name={name}")
    else:
        m = re.search(r"^---\nname:\s*.+\n", text, flags=re.M)
        if not m:
            raise AssertionError(f"{path.name} has no embedded name: frontmatter")
        start = m.start()
        marker = text[start : m.end()]
    end = text.find("\n---\n", start + len(marker))
    if end < 0:
        raise AssertionError(f"{path.name} frontmatter is not closed")
    data = yaml.safe_load(text[start + 4 : end])
    if not isinstance(data, dict):
        raise AssertionError(f"{path.name} frontmatter did not parse to a mapping")
    return data, text


class PreSubmitFrontmatter(unittest.TestCase):
    def test_writing_checks_parse_and_cover_every_class(self) -> None:
        data, body = embedded_frontmatter(WRITING, name="pre-submit-consistency")
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
        data, body = embedded_frontmatter(REVIEW, name="cross-manuscript-qc")
        self.assertEqual(data["owner"], "06_review")
        self.assertEqual(data["audience"], "Lee")
        self.assertEqual(data["order"], ["statement_consistency", "data_consistency"])
        self.assertEqual(data["on_number_conflict"], "annotate_only")
        self.assertEqual(data["journal_language"], "en")
        self.assertEqual(data["user_summary_language"], "zh")
        self.assertEqual(
            data["runs_checks_from"],
            "05_manuscript/qc/manuscript-local-qc.md",
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
        self.assertIn("manuscript-local-qc.md", five)
        self.assertIn("cross-manuscript-qc.md", six)
        self.assertIn("05_manuscript/qc/manuscript-local-qc.md", four)
        self.assertIn("manuscript-local-qc.md", gates)
        self.assertIn("cross-manuscript-qc.md", gates)

    def test_extended_personal_files_hold_the_rules(self) -> None:
        # Wave2: stats-consistency + stats-checklist merged into report-checks.md
        stats = read("04_analysis/qc/report-checks.md")
        checklist = stats  # single current file holds both id tables
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
        self.assertIn("manuscript-local-qc.md", voice)
        self.assertIn("training set", voice)
        self.assertIn("opening paragraph", voice.lower())

        cites = read("05_manuscript/personal/process/citation-and-language.md")
        for token in (
            "consecutive_same_cite",
            "claim_matches_source",
            "no_unverified_cross_copy",
            "year_volume_from_source",
        ):
            self.assertIn(token, cites, token)
        self.assertIn("Methods: **no citations**", cites)

        banned = (BASE_VOCAB / "vocab" / "L1" / "ban-phrases.md").read_text(encoding="utf-8")
        for token in (
            "TRAIN_RATIO",
            "as stated by the source",
            "\u5f85\u8865",
            "\u6807\u7b7e\u672a\u4e0e\u65b9\u6848\u6838\u5bf9",
            "framework",
            "approach",
        ):
            self.assertIn(token, banned, token)

        aitor = read("05_manuscript/personal/Aitor-format.md")
        self.assertIn("Methods: no citations", aitor)
        self.assertIn("intro_opening_has_citations", aitor)
        self.assertIn("training set", aitor)

        # Wave2: introduction-scorecard absorbed into manuscript-local-qc Part A
        score = read("05_manuscript/qc/manuscript-local-qc.md")
        for code in ("FLU-4", "CIT-5", "CIT-6", "CIT-7"):
            self.assertIn(code, score, code)

        # Wave2: personal-review-style.md -> review.md
        style = read("06_review/personal/review.md")
        self.assertIn("### 4.9 Pre-submit consistency requests", style)
        self.assertIn("cross-manuscript-qc.md", style)
        self.assertIn("Do not invent the number", style)
        self.assertIn("voxel-wise or cluster-forming", style)

        # Wave2: structures.md archived; paragraph_lock lives in manuscript-local-qc
        structures = read("05_manuscript/qc/manuscript-local-qc.md")
        self.assertIn("paragraph_lock", structures)
        # Wave2: de-ai.md archived; TRAIN_RATIO / approach stay in ban-phrases
        deai = (BASE_VOCAB / "vocab" / "L1" / "ban-phrases.md").read_text(encoding="utf-8")
        self.assertIn("TRAIN_RATIO", deai)
        self.assertIn("approach", deai)


class CitationVerifyRequired(unittest.TestCase):
    PHRASE = "call/require 03 citation-verify \u2014 do not self-certify lit"

    def test_checklist_frontmatter_parses(self) -> None:
        path = ROOT / "03_research" / "personal" / "citation-verify.md"
        data, body = embedded_frontmatter(path)
        # citation-verify opens with frontmatter; embedded helper still works
        self.assertEqual(data["owner"], "03_research")
        self.assertEqual(data["audience"], "Victor")
        self.assertEqual(data["self_certify"], "forbidden")
        self.assertEqual(data["required_before"], ["gate_05_done", "gate_06"])
        self.assertIn("claim_ref_table", data["outputs"])
        self.assertIn("strong_claim_spot_check", data["outputs"])
        self.assertIn("claim\u2192ref", body)
        self.assertIn(self.PHRASE, body)

    def test_05_and_06_require_03_and_do_not_self_certify(self) -> None:
        for rel in (
            "03_research/SKILL.md",
            "05_manuscript/SKILL.md",
            "05_manuscript/personal/process/citation-and-language.md",
            "05_manuscript/qc/manuscript-local-qc.md",
            "06_review/SKILL.md",
            "06_review/qc/cross-manuscript-qc.md",
            "00_orchestrator/SKILL.md",
            "00_orchestrator/workflows/sci-manuscript.md",
        ):
            self.assertIn(self.PHRASE, read(rel), rel)


class WordTrackChangesOwnership(unittest.TestCase):
    """Aitee owns manuscript Track Changes. Lee comments; he does not self-revise."""

    CONTRACT = "00_orchestrator/references/ownership-contract.md"
    POINTER = "00_orchestrator/references/ownership-contract.md"
    PHRASES = (
        "All manuscript Track Changes are owned by Aitee (05).",
        "Lee must not self-revise as default.",
        "Lee marks/comments; Aitee applies Track Changes.",
        "does not apply the body revisions as default",
        "Chinese \u6279\u6ce8 reason, then an English suggestion line that starts with `Suggested \u2026` (or equivalent Suggested wording), and/or suggested literature.",
        "Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.",
    )
    FILES = (
        "06_review/SKILL.md",
        "06_review/personal/review.md",
        "06_review/personal/word-edit.md",
        "07_response/personal/response.md",
        "07_response/SKILL.md",
        "06_review/qc/cross-manuscript-qc.md",
        "05_manuscript/SKILL.md",
        "05_manuscript/personal/Aitor-format.md",
        "03_research/SKILL.md",
        "03_research/personal/citation-verify.md",
        "00_orchestrator/SKILL.md",
        "00_orchestrator/gates.md",
        "00_orchestrator/workflows/sci-manuscript.md",
        "00_orchestrator/runtime-flow.md",
        "00_orchestrator/runtime-flow.mmd",
        # "ARCHITECTURE.md",  # root stub only; ownership lives in meta copy
        "ARCHITECTURE.md",
        "01_skill-integration/registry.yaml",
    )
    SCAN_SKIP = {
        CONTRACT,
        "tests/test_pre_submit_checks.py",
    }

    def test_contract_holds_full_sentences(self) -> None:
        text = read(self.CONTRACT)
        for phrase in self.PHRASES:
            self.assertIn(phrase, text, f"contract missing {phrase!r}")
        for name in ("Aitor", "Aitee", "Lee", "Victor", "Loopnow", "Bai"):
            self.assertIn(name, text, name)
        self.assertIn("G-CIT-1", text)
        self.assertIn("G-CIT-2", text)

    def test_wired_files_point_at_contract(self) -> None:
        for rel in self.FILES:
            self.assertIn(self.POINTER, read(rel), f"{rel} missing ownership pointer")

    def test_full_sentences_appear_only_in_contract(self) -> None:
        hits = {phrase: [] for phrase in self.PHRASES}
        tracked = subprocess.check_output(
            ["git", "-c", "core.quotepath=false", "ls-files"],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
        )
        for rel in tracked.splitlines():
            if not rel or rel in self.SCAN_SKIP:
                continue
            if rel.startswith("mounts-cap/"):
                continue
            path = ROOT / rel
            # Wave2: git index still lists archived paths (.github/, old 01_*, etc.)
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".yaml", ".yml", ".mmd", ".py", ".txt"}:
                continue
            text = path.read_text(encoding="utf-8")
            for phrase in self.PHRASES:
                if phrase in text:
                    hits[phrase].append(rel)
        leftover = {p: files for p, files in hits.items() if files}
        self.assertEqual(leftover, {}, msg=str(leftover))

    def test_lee_does_not_apply_decidable_track_changes(self) -> None:
        retired = (
            "\u672a\u70b9\u5934\u4e0d\u6539\u7a3f",
            "\u7528\u6237\u786e\u8ba4\u540e\u518d\u7528\u4fee\u8ba2\u6a21\u5f0f\u6539\u4fe1\u5c01\u6b63\u6587",
            "may attach 1\u20132 **reference-only** revised sentences",
        )
        for rel in self.FILES:
            text = read(rel)
            for old in retired:
                self.assertNotIn(old, text, f"{rel} still says {old!r}")
        reg = read("01_skill-integration/registry.yaml")
        self.assertIn("word-tc-owned-by-aitee", reg)
        self.assertIn("Lee no longer applies body Track Changes on decidable fixes.", reg)
        mmd = read("00_orchestrator/runtime-flow.mmd")
        self.assertIn("Lee \u00b7 \u9648\u8ff0\u4e00\u81f4", mmd)
        self.assertLess(mmd.index("Lit05"), mmd.index("Gate \u00b7 05"))
        self.assertLess(mmd.index("Lit06"), mmd.index("Gate \u00b7 06"))


if __name__ == "__main__":
    unittest.main()
