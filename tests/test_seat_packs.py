"""Seat packs, routing, review interaction and pack dedupe.

Merged from: `test_audit_invariants.py`, `test_lab_rules.py`, `test_rule_landing.py`, `test_pre_submit_checks.py`, `test_advanced_mirror_dedupe.py`.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import subprocess
import unittest
import yaml

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

CLIN = ROOT / "02_data-processing" / "advanced"
REG = ROOT / "00_orchestrator" / "registry.yaml"
SKIP_PARTS = {".git", "__pycache__", "history"}
SKIP_NAMES = {
    "INTEGRATION_MAP.md",
    "INTEGRATION_MAP.archive.md",
    "VERSION.txt",
    "changelog.md",
    "CHANGELOG.md",
}
RETIRED_IDS = (
    "02-xlsx",
    "02-imaging",
    "02-impute",
    "02-generic-docs",
    "03-literature",
    "03-design",
    "03-frontier",
    "04-stats-generic",
    "04-figure-engine",
    "05-writing-generic",
    "06-review-generic",
)
RETIRED_RE = re.compile(
    r"(?<![\w-])(" + "|".join(re.escape(i) for i in RETIRED_IDS) + r")(?![\w-])"
)
ALLOW_RETIRED_LINE = re.compile(
    r"(?i)retir|no live|not live|not a live|umbrella|former |gone |"
    r"do not |don't |must not|never |history|historical|legacy"
)
HIS_ASSIGN_RE = re.compile(r"^\s*(USERNAME|PASSWORD)\s*=", re.M)
ID_TICK_RE = re.compile(r"`([0-9]{2}-[a-z0-9-]+|[a-z][a-z0-9-]*)`")
FINE_ID_RE = re.compile(r"`([a-z][a-z0-9-]*)`")
def iter_text_files():
    for p in ROOT.rglob("*"):
        if any(s in p.parts for s in SKIP_PARTS):
            continue
        if not p.is_file():
            continue
        if p.name in SKIP_NAMES:
            continue
        if p.suffix.lower() not in {".md", ".py", ".yaml", ".yml", ".txt", ".html"}:
            continue
        yield p
def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")
def registry_fine_ids() -> list[str]:
    text = REG.read_text(encoding="utf-8")
    # fine_ids: ... until reference_only: (v4) or proposals: (v3)
    m = re.search(r"^fine_ids:\n(.*?)^(?:local_packs:|reference_only:|archived:|proposals:)", text, re.M | re.S)
    self_block = m.group(1) if m else text
    ids = re.findall(r"^\s+- id:\s*(\S+)\s*$", self_block, re.M)
    return ids
SKILLS = Path(__file__).resolve().parents[1]
BASE_VOCAB = SKILLS / "05_manuscript" / "base"
def lab_rules_read(*parts: str) -> str:
    return (SKILLS.joinpath(*parts)).read_text(encoding="utf-8")
def t(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")
pre_submit_checks_BASE_VOCAB = ROOT / "05_manuscript" / "base"
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
    "agent_disclaimer_and_incomplete_claims_banned",
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
# 05-only writing-craft checks (Introduction / Discussion shape); not part of the
# cross-manuscript set that 06 re-runs, so they are asserted on the 05 file only.
WRITING_ONLY_IDS = (
    "intro_funnel_five_para",
    "intro_discussion_loop",
    "discussion_inverted_funnel",
    "no_causal_overclaim_observational",
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
def pre_submit_checks_read(rel: str) -> str:
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
MIRRORS = (
    ("03_research/base/design-study/MODULE.md", "03_research/advanced/radiology-design.md"),
)
MIN_CHARS = 200
def _paragraphs(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    out = set()
    for para in re.split(r"\n\s*\n", text):
        norm = re.sub(r"\s+", " ", para).strip()
        if len(norm) >= MIN_CHARS:
            out.add(norm)
    return out

class HisHygiene(unittest.TestCase):
    def test_no_his_host_or_password_assignments(self) -> None:
        self.assertTrue(CLIN.is_dir())
        self.assertFalse((CLIN / "scripts" / "query_patient.py").exists())
        for p in CLIN.rglob("*"):
            if not p.is_file():
                continue
            if "__pycache__" in p.parts:
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            self.assertNotIn("172.16.9.68", text, p.as_posix())
            self.assertIsNone(HIS_ASSIGN_RE.search(text), p.as_posix())
            self.assertNotIn("from selenium", text, p.as_posix())
            self.assertNotIn("query_patient.py", text, p.as_posix())
class RetiredIds(unittest.TestCase):
    def test_retired_ids_are_not_live_routes(self) -> None:
        violations = []
        for p in iter_text_files():
            if "tests" in p.parts:
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            rel = p.relative_to(ROOT).as_posix()
            for i, line in enumerate(text.splitlines(), 1):
                if ALLOW_RETIRED_LINE.search(line):
                    continue
                for m in RETIRED_RE.finditer(line):
                    violations.append(f"{rel}:{i}:{m.group(1)}")
        self.assertEqual(violations, [], msg="\n".join(violations[:40]))
class SessionPick(unittest.TestCase):
    def test_workflows_ask_session_fine_id_pick(self) -> None:
        for rel in (
            "00_orchestrator/workflows/sci-manuscript.md",
            "00_orchestrator/workflows/statistics.md",
            "00_orchestrator/workflows/README.md",
        ):
            text = read(rel).lower()
            self.assertTrue(
                "session fine-id pick" in text or "session-fine-id pick" in text,
                f"{rel} must ask session fine-id pick",
            )
            self.assertIn("do not auto-load", text, rel)
class RegistryMenu(unittest.TestCase):
    def test_registry_live_ids_are_unique(self) -> None:
        """registry.yaml is SSOT; no generated MOUNTED_SKILLS.md mirror."""
        reg_doc = yaml.safe_load(REG.read_text(encoding="utf-8"))
        fine_ids = reg_doc.get("fine_ids") or []
        ids = [m["id"] for m in fine_ids]
        self.assertEqual(len(ids), len(set(ids)), msg=str(ids))
        want_pick = [m["id"] for m in fine_ids if m.get("status") == "LIVE"]
        self.assertGreaterEqual(len(want_pick), 10)
        self.assertFalse((ROOT / "00_orchestrator" / "MOUNTED_SKILLS.md").exists())
class ArchitectureSsot(unittest.TestCase):
    """Single root ARCHITECTURE.md = intent tables + QC/handoff + ownership + live routing keywords."""

    def test_architecture_live_rules(self) -> None:
        text = read("ARCHITECTURE.md")
        low = text.lower()
        self.assertGreater(len(text), 500)
        self.assertRegex(text, r"(five parts|≤\s*5|at most five)")
        self.assertIn("my-skills", low)
        self.assertIn("in-repo", low)
        self.assertNotIn("my-skills-base", low)
        self.assertNotIn("MY-SKILLS-base", text)
        self.assertIn("ethics", low)
        self.assertIn("03_research", text)
        self.assertIn("ask-each-run", text)
        self.assertIn("draw-flowchart", text)
        self.assertIn("plot-figures", text)
        self.assertIn("find-journal", text)
        self.assertIn("05_manuscript/base/write-paper/", text)
        self.assertNotIn("write-venue", text)
        self.assertIn("calc-sample-size", text)
        self.assertNotIn("05-write-venue", text)
        self.assertNotIn("04-stats-power", text)
        self.assertIn("00_orchestrator/registry.yaml", text)
        self.assertNotRegex(text, r"52 fine")
        self.assertNotRegex(low, r"≤\s*3")
        self.assertNotIn("role: default-candidate", text)
        self.assertNotIn("Default candidate: `Imbad0202", text)

    def test_architecture_owns_intent_and_qc(self) -> None:
        text = read("ARCHITECTURE.md")
        self.assertIn("## Skill selection", text)
        self.assertIn("Lab-specific flows", text)
        self.assertIn("## Final QC", text)
        self.assertIn("Local recovery", text)
        self.assertIn("fill-protocol", text)
        self.assertIn("advanced/extract.md", text)
        # Full fine-id/ceiling/Cache section headings stay out of this intent file
        self.assertNotIn("## A/B no-reflow contract", text)
        self.assertNotIn("## Fine-id expansion ceiling", text)
        self.assertNotIn("## Cache ≠ Live ≠ Active", text)
        self.assertNotIn("## load_priority", text)

    def test_readme_keeps_lab_homes(self) -> None:
        readme = read("README.md")
        self.assertIn("{code_root}", readme)
        self.assertIn("lab", readme.lower())
        self.assertIn("{doc_root}", readme)
        text = read("ARCHITECTURE.md")
        self.assertIn("find-journal", text)
        self.assertIn("fill-protocol", text)
class RoutingFourTuple(unittest.TestCase):
    def test_find_journal_and_fill_protocol_stay_on_03(self) -> None:
        reg = yaml.safe_load(REG.read_text(encoding="utf-8"))
        by_id = {m["id"]: m for m in reg["fine_ids"]}
        self.assertEqual(by_id["find-journal"]["a_domain"], "03_research")
        self.assertEqual(by_id["fill-protocol"]["a_domain"], "03_research")
        self.assertEqual(by_id["lit-fulltext"]["a_domain"], "03_research")
        fj_note = by_id["find-journal"]["note"]
        fp_note = by_id["fill-protocol"]["note"]
        self.assertTrue(
            "03_research/base/find-journal" in fj_note,
            fj_note,
        )
        self.assertTrue(
            "03_research/base/fill-protocol" in fp_note,
            fp_note,
        )
        self.assertNotRegex(read("ARCHITECTURE.md"), r"(选刊|journal selection)\s*→\s*05")
        self.assertNotRegex(read("00_orchestrator/SKILL.md"), r"(选刊|journal selection)\s*→\s*05")
class DiscoverySurface(unittest.TestCase):
    def test_auto_discovery_rule_is_in_00(self) -> None:
        zero = read("00_orchestrator/SKILL.md")
        life = read("00_orchestrator/references/lifecycle-cache.md")
        evo = read("00_orchestrator/references/skill-evolution.md")
        self.assertIn("session_picked_fine_ids", zero)
        self.assertIn('only `00_orchestrator`-`07_response`', zero)
        self.assertNotIn("and `skill-harvest`", zero)
        self.assertIn("`00`-`07` only", life)
        self.assertNotIn("and `skill-harvest` only", life)
        self.assertIn("skills.md", evo)

    def test_live_docs_do_not_handwrite_52_fine(self) -> None:
        rel = "00_orchestrator/workflows/research-exploration-loop.md"
        self.assertNotRegex(read(rel), r"52 fine", rel)
class ReadmeSsot(unittest.TestCase):
    """CHG-20260913-002: README.md drifted to stale '30-id' wording while
    registry.yaml/ARCHITECTURE.md had already moved to v4 (10 coarse + 52
    fine). ArchitectureSsot only checked the two ARCHITECTURE.md files;
    this closes that blind spot for both README.md files."""

    def test_readme_match_v4(self) -> None:
        text = read("README.md")
        self.assertIn("registry.yaml", text)
        self.assertNotRegex(text, r"52 fine")
        self.assertNotIn("30-id", text)
        self.assertNotIn("30 coarse", text)
class FastRouting(unittest.TestCase):
    def test_venue_and_power_routes(self) -> None:
        zero = read("00_orchestrator/SKILL.md")
        self.assertIn("references/fast-routing.md", zero)
        fast = read("00_orchestrator/references/fast-routing.md")
        self.assertIn("选刊 → `03_research`", fast)
        self.assertNotIn("选刊 → `05_manuscript` (`05-write-venue`)", fast)
        self.assertIn("样本量 → `02_data-processing` (`calc-sample-size`)", fast)
        six = read("06_review/SKILL.md")
        # 06 top layer: journal select out of scope (points to 03), not a fast-routing table
        self.assertIn("03_research", six)
        self.assertNotIn("05-write-venue", six)
        ethics = read("03_research/advanced/fill-protocol/README.md")
        # Jinshan PHI pack; capability body is B fill-protocol; journal select not here
        self.assertIn("fill-protocol", ethics)
        self.assertNotIn("05-write-venue", ethics)
        five = read("05_manuscript/SKILL.md")
        self.assertIn("write-paper", five)
        self.assertIn("05_manuscript/base/write-paper/", five)
        self.assertNotIn("write-venue", five)
        self.assertNotIn("05-write-venue", five)
        self.assertIn("journal templates / house style", five)
        self.assertNotIn("选刊 is `05-write-venue`", five)
        three = read("03_research/SKILL.md")
        self.assertIn("journal-selection.md", three)
        self.assertIn("lit-search", three)
        self.assertNotIn("03-lit-search", three)
        self.assertIn("选刊走 03 `find-journal`", three)
class DeAiAndFigures(unittest.TestCase):
    def test_sci_manuscript_paths(self) -> None:
        sop = read("00_orchestrator/workflows/sci-manuscript.md")
        self.assertIn("05_manuscript/base/vocab/L1/ban-phrases.md", sop)
        self.assertIn("draw-flowchart", sop)
        self.assertIn("plot-figures", sop)
        self.assertNotIn("04-fig-flow", sop)
        self.assertNotIn("de-ai/forbidden-phrases.md", sop)
        stats_skill = read("02_data-processing/SKILL.md")
        self.assertIn("draw-flowchart", stats_skill)
        self.assertNotIn("04-figure-engine", stats_skill)
class OrchestratorLoop(unittest.TestCase):
    def test_intent_chain_qc_in_skill(self) -> None:
        zero = read("00_orchestrator/SKILL.md")
        low = zero.lower()
        self.assertIn("intent classify", low)
        self.assertIn("skill chain", low)
        self.assertIn("QC closed loop", zero)
        self.assertIn("Never `--e2e`", zero)
        self.assertIn("Literature enters 03 only", zero)
        self.assertIn("Reviewer response enters 07 only", zero)
        self.assertNotIn("Do not adopt ARS", zero)
        self.assertNotIn("academic-pipeline", zero)
        self.assertIn("Do not adopt an external", zero)
        self.assertIn("orchestrate", zero)
        fast = read("00_orchestrator/references/fast-routing.md")
        self.assertIn("Excel / 批处理 → `02_data-processing`", fast)
        self.assertIn("citation-verify", zero)
        self.assertIn("do not self-certify lit", zero)
        mmd = read("00_orchestrator/runtime-flow.mmd")
        self.assertIn("citation-verify", mmd)
        self.assertIn("claim→ref", mmd)
        self.assertIn("mandatory", mmd)
        self.assertIn("mid-entry OK", mmd)
        self.assertIn("Lee · statement", mmd)
        self.assertLess(mmd.index("Lit05"), mmd.index("Gate · 05"))
        self.assertLess(mmd.index("Lit06"), mmd.index("Gate · 06"))
        self.assertIn("does not replace citation-verify", mmd)
        # t1123: citation-verify ownership lives in ownership-contract, not registry meta
        own = read("00_orchestrator/references/ownership-contract.md")
        self.assertIn("citation-verify", own.lower())
        self.assertTrue(
            "Lit05" in own or "Lit06" in own or "05" in own,
            "ownership-contract should cover 05/06 citation-verify",
        )

    def test_gates_and_handoff_exist(self) -> None:
        gates = read("00_orchestrator/gates.md")
        for token in ("G0", "G-PHI", "G-STATS", "G-05", "G-06", "Development set", "VAL_MODE", "DeLong"):
            self.assertIn(token, gates)
        hand = read("00_orchestrator/templates/handoff.yaml")
        self.assertIn("qc_gate:", hand)
        self.assertIn("outputs:", hand)
        state = read("00_orchestrator/templates/project-state.yaml")
        self.assertIn("pipeline:", state)
        self.assertIn("stage:", state)
        self.assertIn("defects:", state)

    def test_sops_wired_by_html(self) -> None:
        rad = read("00_orchestrator/workflows/statistics.md")
        sci = read("00_orchestrator/workflows/sci-manuscript.md")
        self.assertIn("sci-manuscript", rad)
        self.assertIn("G-STATS", rad)
        self.assertIn("G-05", sci)
        self.assertIn("G-06", sci)
        self.assertIn("05_manuscript/base/vocab/L1/ban-phrases.md", sci)
        wf = read("00_orchestrator/workflows/README.md")
        self.assertIn("gates.md", wf)
class AttributionAndFetch(unittest.TestCase):

    def test_skill_level_prefix_rules(self) -> None:
        style = read("06_review/advanced/review.md")
        self.assertIn("[Nature:simulate-reviewers]", style)
        self.assertIn("包内skill-id", style.replace(" ", ""))
        gates = read("00_orchestrator/gates.md")
        self.assertIn("skill-level prefix", gates)

    def test_author_vs_prefix(self) -> None:
        text = read("06_review/advanced/review.md")
        self.assertIn("作者字段", text)
        self.assertIn("作者栏 ≠ 来源标签", text)
        self.assertIn("双标", text)
        self.assertNotIn("[ARS:", text)
        self.assertIn("[Nature:simulate-reviewers]", text)
        self.assertIn("[self-review]", text)
        self.assertIn("同一 DOI", text)
        zero = read("00_orchestrator/SKILL.md")
        self.assertIn("06_review/advanced/review.md", zero)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("skill-level prefix", gates)
        five = read("05_manuscript/SKILL.md")
        self.assertIn("New citation numbers", five)
class ReviewInteract(unittest.TestCase):
    def test_advanced_review_eight_sections(self) -> None:
        text = read("06_review/advanced/review.md")
        for h in (
            "1. Title",
            "2. Abstract",
            "3. Introduction",
            "4. Methods",
            "5. Results",
            "6. Discussion",
            "7. References",
            "8. Figures & Tables",
        ):
            self.assertIn(h, text)
        self.assertIn("Major Issues", text)
        self.assertIn("用户决定", text)
        self.assertIn("词或句", text)
        self.assertNotIn("mode-2-prereview.md", text)

    def test_00_05_06_interact_rules(self) -> None:
        zero = read("00_orchestrator/SKILL.md")
        self.assertIn("Plan card", zero)
        self.assertIn("G-LIT", zero)
        self.assertIn("word/sentence", zero)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("G-LIT", gates)
        self.assertIn("G-FACT", gates)
        five = read("05_manuscript/SKILL.md")
        self.assertIn("Internal calls", five)
        self.assertIn("word or sentence", five)
        six = read("06_review/SKILL.md")
        self.assertIn("re-review", six.lower())
        self.assertIn("07_response", six)
        resp = read("07_response/advanced/response.md")
        self.assertTrue(len(resp) > 50)

    def test_evidence_request_protocol(self) -> None:
        text = read("05_manuscript/advanced/process/evidence.md")
        self.assertIn("Evidence Request", text)
        self.assertIn("Accept", text)
        self.assertIn("Weaken", text)
        self.assertIn("Delete", text)
        self.assertIn("03_research", text)
        self.assertNotIn("B05 = Advanced Writing", text)
        skill = read("05_manuscript/SKILL.md")
        self.assertIn("process/evidence.md", skill)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("process/evidence.md", gates)
class LocalLinkHygiene(unittest.TestCase):
    def test_no_broken_relative_markdown_links(self) -> None:
        errors = []
        skip_parts = {".git", "__pycache__", "history"}
        for p in ROOT.rglob("*.md"):
            if skip_parts & set(p.parts):
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
            for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
                target = m.group(1).split("#", 1)[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:", "<")):
                    continue
                if not (p.parent / target).resolve().exists():
                    errors.append(f"{p.relative_to(ROOT)} -> {target}")
        self.assertEqual(errors, [], msg="\n".join(errors))
class GateMetadata(unittest.TestCase):
    """Live gates.md class rows (was under HarvestHygiene; does not need skill-harvest)."""

    def test_gate_class_metadata(self) -> None:
        gates = read("00_orchestrator/gates.md")
        self.assertIn("Gate class", gates)
        self.assertIn("HARD", gates)
        self.assertIn("QUALITY", gates)
        # Existing ids only — no invented G-HARD / G-QUALITY gate ids
        self.assertNotIn("| G-HARD |", gates)
        self.assertNotIn("| G-QUALITY |", gates)
        for row in (
            "| G0 | HARD |",
            "| G-PHI | HARD |",
            "| G-FACT | HARD |",
            "| G-STATS | QUALITY |",
            "| G-05 | QUALITY |",
            "| G-06 | QUALITY |",
            "| G-LIT | QUALITY |",
            "| G-CODE | QUALITY |",
        ):
            self.assertIn(row, gates)
class DeAI(unittest.TestCase):
    SAMPLE = (
        "This paper delves into the landscape of radiomics. "
        "The pivotal and robust model is comprehensive. "
        "Interestingly, we leverage a groundbreaking approach."
    )

    def test_sample_hits_forbidden_table(self) -> None:
        table = (BASE_VOCAB / "vocab" / "L1" / "ban-phrases.md").read_text(encoding="utf-8").lower()
        hits = []
        for word in (
            "delve", "landscape", "pivotal", "robust", "comprehensive",
            "interestingly", "leverage", "groundbreaking",
        ):
            if word in self.SAMPLE.lower():
                self.assertIn(word, table, f"{word} must be listed in ban-phrases")
                hits.append(word)
        self.assertGreaterEqual(len(hits), 6)

    def test_compared_and_attenuated_wording(self) -> None:
        banned = (BASE_VOCAB / "vocab" / "L1" / "ban-phrases.md").read_text(encoding="utf-8")
        patterns = (BASE_VOCAB / "vocab" / "L1" / "patterns.md").read_text(encoding="utf-8")
        lang = lab_rules_read("05_manuscript", "advanced", "process", "citation-and-language.md")
        for text in (banned, patterns, lang):
            self.assertIn("attenuated", text)
            self.assertIn("Compared", text)
            self.assertIn("relative CBF", text)
            self.assertIn("relCBF", text)
        self.assertIn("reduced", banned)
        self.assertIn("decreased", banned)
        self.assertIn("attenuation correction", banned)
        self.assertIn("comparison word", banned)

    def test_de_ai_is_advanced_not_a_fine_id(self) -> None:
        five = lab_rules_read("05_manuscript", "SKILL.md")
        self.assertNotIn("05-de-ai", five)
        self.assertIn("write-paper", five)
        self.assertNotIn("05-write-manuscript", five)
        self.assertFalse((SKILLS / "05_manuscript" / "de-ai").exists())
        self.assertTrue((BASE_VOCAB / "vocab" / "L1" / "ban-phrases.md").is_file())
class Aitor(unittest.TestCase):
    def test_methods_have_no_citations(self) -> None:
        text = lab_rules_read("05_manuscript", "advanced", "Aitor-format.md")
        self.assertIn("Methods: no citations", text)

    def test_table1_is_training_vs_test(self) -> None:
        text = lab_rules_read("05_manuscript", "advanced", "Aitor-format.md")
        self.assertRegex(text, r"Table 1\s*=\s*training vs test")
class ValMode(unittest.TestCase):
    def test_test_set_does_not_reselect_features(self) -> None:
        text = lab_rules_read("02_data-processing", "advanced", "analysis", "pipeline.md")
        self.assertIn("VAL_MODE", text)
        self.assertRegex(text, r"[Rr]e-select features on the test set")
        self.assertIn("no new screening", text)
        self.assertIn("\u4e0d\u91cd\u7b5b", text)
class Routing(unittest.TestCase):
    def test_index_seat_is_00_not_excel(self) -> None:
        readme = (SKILLS / "README.md").read_text(encoding="utf-8")
        self.assertIn("00_orchestrator", readme)
        self.assertIn("registry / index / session-pick", readme)
        self.assertNotIn("01_automation", readme)
        zero = lab_rules_read("00_orchestrator", "SKILL.md")
        self.assertIn("00_orchestrator", zero)
        fast = lab_rules_read("00_orchestrator", "references", "fast-routing.md")
        self.assertIn("Excel / \u6279\u5904\u7406", fast)
        self.assertRegex(
            fast,
            r"Excel / \u6279\u5904\u7406 \u2192 `02_data-processing`",
        )

    def test_figures_route_to_02(self) -> None:
        fast = lab_rules_read("00_orchestrator", "references", "fast-routing.md")
        self.assertIn("\u51fa\u56fe", fast)
        five = lab_rules_read("05_manuscript", "SKILL.md")
        self.assertIn("02_data-processing", five)
        self.assertIn("plot-figures", five)
        self.assertIn("draw-flowchart", five)
        self.assertNotIn("04-fig-flow", five)
        self.assertNotIn("bundles/figure-engine", five)

    def test_session_fine_id_pick(self) -> None:
        one = lab_rules_read("00_orchestrator", "SKILL.md")
        zero = lab_rules_read("00_orchestrator", "SKILL.md")
        reg = lab_rules_read("00_orchestrator", "registry.yaml")
        pick = lab_rules_read("00_orchestrator", "references", "session-pick.md")
        self.assertIn("Session fine-id pick", pick)
        self.assertIn("session-pick.md", one)
        self.assertIn("ask-each-run", reg)
        self.assertIn("session fine-id pick", zero.lower())
        five = lab_rules_read("05_manuscript", "SKILL.md")
        self.assertIn("This-run pick", five)

    def test_literature_to_03_response_to_07(self) -> None:
        zero = lab_rules_read("00_orchestrator", "SKILL.md")
        self.assertIn("Literature enters 03 only", zero)
        self.assertIn("Reviewer response enters 07 only", zero)
        fast = lab_rules_read("00_orchestrator", "references", "fast-routing.md")
        self.assertIn("回复审稿人", fast)
        self.assertIn("07_response", fast)
        self.assertIn("- **回复审稿人** → `07_response`", fast)
        self.assertNotIn("预审 / 审稿 / **回复审稿人** → `06_review`", fast)
        self.assertIn("- 预审 / 审稿 → `06_review`", fast)
        gates = lab_rules_read("00_orchestrator", "gates.md")
        self.assertIn("after Lee pre-review or re-review only", gates)
        self.assertNotIn("after pre-review or reviewer response", gates)
        self.assertIn("07 / `07_response`", gates)
class LabSte(unittest.TestCase):
    def test_pointer_and_no_vendor(self) -> None:
        lab = (BASE_VOCAB / "vocab" / "L3" / "lab-ste.md").read_text(encoding="utf-8")
        self.assertIn("{doc_lab_ste}", lab)
        self.assertIn("Do not", lab)
        self.assertIn("vendor", lab.lower())
        self.assertIn("conventional_passive", lab)
        self.assertIn("Compared", lab)
        self.assertIn("attenuated", lab)
        five = lab_rules_read("05_manuscript", "SKILL.md")
        self.assertIn(
            "05_manuscript/base/vocab/L3/lab-ste.md",
            five,
        )
        self.assertNotIn(
            "05-manuscript/vocab/L3/lab-ste.md",
            five,
        )
        self.assertTrue((BASE_VOCAB / "vocab" / "L2" / "approved-en.tsv").is_file())
        self.assertFalse((SKILLS / "lab-ste").exists())
class RuleLanding(unittest.TestCase):
    def test_new_references_exist_and_linked(self) -> None:
        hm = ROOT / "00_orchestrator/references/handoff-monitor.md"
        se = ROOT / "00_orchestrator/references/skill-evolution.md"
        self.assertTrue(hm.is_file(), "handoff-monitor.md missing")
        self.assertTrue(se.is_file(), "skill-evolution.md missing")
        skill = t("00_orchestrator/SKILL.md")
        self.assertIn("handoff-monitor.md", skill)
        self.assertIn("skill-evolution.md", skill)

    def test_standing_delivery_drop_points(self) -> None:
        sd = t("00_orchestrator/references/standing-delivery.md")
        for needle in ("subproject root", "derivatives", "Asia/Shanghai"):
            self.assertIn(needle, sd, f"standing-delivery missing {needle}")
        # 0result retired as standard deliverable folder (2026-10-24)
        self.assertIn("do **not** use a live `0result", sd)

    def test_manuscript_local_qc_bans(self) -> None:
        ml = t("05_manuscript/qc/manuscript-local-qc.md")
        for needle in ("cannot_invent", "Do not invent", "[Figure N near here]", "layout_priority"):
            self.assertIn(needle, ml, f"manuscript-local-qc missing {needle}")

    def test_response_hard_rules(self) -> None:
        rp = t("07_response/advanced/response.md")
        for needle in ("Please", "past tense", "ACCEPT-"):
            self.assertIn(needle, rp, f"response.md missing {needle}")

    def test_workspace_layout_points_at_rules(self) -> None:
        self.assertFalse((ROOT / "02_data-processing/advanced/workspace.md").is_file())
        skill = t("02_data-processing/SKILL.md")
        self.assertIn("{RULES}/workspace-layout.md", skill)
        self.assertNotIn("advanced/workspace.md", skill)
        sd = t("00_orchestrator/references/standing-delivery.md")
        self.assertIn("{RULES}/workspace-layout.md", sd)
        self.assertNotIn("`{WORK_A}", sd)
        self.assertNotIn("`{WORK_B}", sd)
        self.assertNotIn("## A-class", sd)
        self.assertNotIn("## B-class", sd)

    def test_ownership_dispatch(self) -> None:
        oc = t("00_orchestrator/references/ownership-contract.md")
        self.assertIn("## Dispatch", oc)
        self.assertIn("one executor", oc.lower())
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
        expected = tuple(REQUIRED_IDS) + WRITING_ONLY_IDS
        self.assertCountEqual(ids, expected)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertCountEqual(set(classes), REQUIRED_CLASSES)
        for cid in expected:
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
        five = pre_submit_checks_read("05_manuscript/SKILL.md")
        six = pre_submit_checks_read("06_review/SKILL.md")
        stats_skill = pre_submit_checks_read("02_data-processing/SKILL.md")
        gates = pre_submit_checks_read("00_orchestrator/gates.md")
        self.assertIn("manuscript-local-qc.md", five)
        self.assertIn("cross-manuscript-qc.md", six)
        self.assertIn("05_manuscript/qc/manuscript-local-qc.md", stats_skill)
        self.assertIn("manuscript-local-qc.md", gates)
        self.assertIn("cross-manuscript-qc.md", gates)

    def test_extended_advanced_files_hold_the_rules(self) -> None:
        # Wave2: stats-consistency + stats-checklist merged into report-checks.md
        stats = pre_submit_checks_read("02_data-processing/qc/report-checks.md")
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

        voice = pre_submit_checks_read("05_manuscript/advanced/voice-portrait.md")
        self.assertIn("Paragraph lock", voice)
        self.assertIn("manuscript-local-qc.md", voice)
        self.assertIn("training set", voice)
        self.assertIn("opening paragraph", voice.lower())

        cites = pre_submit_checks_read("05_manuscript/advanced/process/citation-and-language.md")
        for token in (
            "consecutive_same_cite",
            "claim_matches_source",
            "no_unverified_cross_copy",
            "year_volume_from_source",
        ):
            self.assertIn(token, cites, token)
        self.assertIn("Methods: **no citations**", cites)

        banned = (pre_submit_checks_BASE_VOCAB / "vocab" / "L1" / "ban-phrases.md").read_text(encoding="utf-8")
        for token in (
            "TRAIN_RATIO",
            "as stated by the source",
            "\u5f85\u8865",
            "\u6807\u7b7e\u672a\u4e0e\u65b9\u6848\u6838\u5bf9",
            "framework",
            "approach",
        ):
            self.assertIn(token, banned, token)

        aitor = pre_submit_checks_read("05_manuscript/advanced/Aitor-format.md")
        self.assertIn("Methods: no citations", aitor)
        self.assertIn("intro_opening_has_citations", aitor)
        self.assertIn("training set", aitor)

        # Wave2: introduction-scorecard absorbed into manuscript-local-qc Part A
        score = pre_submit_checks_read("05_manuscript/qc/manuscript-local-qc.md")
        for code in ("FLU-4", "CIT-5", "CIT-6", "CIT-7"):
            self.assertIn(code, score, code)

        # Wave2: advanced-review-style.md -> review.md
        style = pre_submit_checks_read("06_review/advanced/review.md")
        self.assertIn("### 4.9 Pre-submit consistency requests", style)
        self.assertIn("cross-manuscript-qc.md", style)
        self.assertIn("Do not invent the number", style)
        self.assertIn("voxel-wise or cluster-forming", style)

        # Wave2: structures.md archived; paragraph_lock lives in manuscript-local-qc
        structures = pre_submit_checks_read("05_manuscript/qc/manuscript-local-qc.md")
        self.assertIn("paragraph_lock", structures)
        # Wave2: de-ai.md archived; TRAIN_RATIO / approach stay in ban-phrases
        deai = (pre_submit_checks_BASE_VOCAB / "vocab" / "L1" / "ban-phrases.md").read_text(encoding="utf-8")
        self.assertIn("TRAIN_RATIO", deai)
        self.assertIn("approach", deai)
class CitationVerifyRequired(unittest.TestCase):
    PHRASE = "call/require 03 citation-verify \u2014 do not self-certify lit"

    def test_checklist_frontmatter_parses(self) -> None:
        path = ROOT / "03_research" / "advanced" / "citation-verify.md"
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
            "05_manuscript/advanced/process/citation-and-language.md",
            "05_manuscript/qc/manuscript-local-qc.md",
            "06_review/SKILL.md",
            "06_review/qc/cross-manuscript-qc.md",
            "00_orchestrator/SKILL.md",
            "00_orchestrator/workflows/sci-manuscript.md",
        ):
            self.assertIn(self.PHRASE, pre_submit_checks_read(rel), rel)
class WordTrackChangesOwnership(unittest.TestCase):
    """Aitee owns manuscript Track Changes. Lee comments; he does not self-revise."""

    CONTRACT = "00_orchestrator/references/ownership-contract.md"
    POINTER = "00_orchestrator/references/ownership-contract.md"
    PHRASES = (
        "All manuscript Track Changes are owned by Aitee (05).",
        "Lee must not self-revise as default.",
        "Lee marks/comments; Aitee applies Track Changes.",
        "does not apply the body revisions as default",
        "state the reason in a Chinese comment, then an English suggestion line that starts with `Suggested \u2026` (or equivalent Suggested wording), and/or suggested literature.",
        "Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.",
    )
    FILES = (
        "06_review/SKILL.md",
        "06_review/advanced/review.md",
        "06_review/advanced/word-edit.md",
        "07_response/advanced/response.md",
        "07_response/SKILL.md",
        "06_review/qc/cross-manuscript-qc.md",
        "05_manuscript/SKILL.md",
        "05_manuscript/advanced/Aitor-format.md",
        "03_research/SKILL.md",
        "03_research/advanced/citation-verify.md",
        "00_orchestrator/SKILL.md",
        "00_orchestrator/gates.md",
        "00_orchestrator/workflows/sci-manuscript.md",
        "00_orchestrator/runtime-flow.md",
        "00_orchestrator/runtime-flow.mmd",
        # ARCHITECTURE.md is live ownership SSOT (scanned below)
        "ARCHITECTURE.md",
        "00_orchestrator/registry.yaml",
    )
    SCAN_SKIP = {
        CONTRACT,
    }

    def test_contract_holds_full_sentences(self) -> None:
        text = pre_submit_checks_read(self.CONTRACT)
        for phrase in self.PHRASES:
            self.assertIn(phrase, text, f"contract missing {phrase!r}")
        for name in ("Aitor", "Aitee", "Lee", "Victor", "Loopnow", "Bai"):
            self.assertIn(name, text, name)
        self.assertIn("G-CIT-1", text)
        self.assertIn("G-CIT-2", text)

    def test_wired_files_point_at_contract(self) -> None:
        for rel in self.FILES:
            self.assertIn(self.POINTER, pre_submit_checks_read(rel), f"{rel} missing ownership pointer")

    def test_full_sentences_appear_only_in_contract(self) -> None:
        hits = {phrase: [] for phrase in self.PHRASES}
        try:
            tracked = subprocess.check_output(
                ["git", "-c", "core.quotepath=false", "ls-files"],
                cwd=ROOT,
                text=True,
                encoding="utf-8",
            ).splitlines()
        except (OSError, subprocess.CalledProcessError):
            # Not a git worktree (the runtime tree is a plain copy) -> walk instead.
            tracked = [
                p.relative_to(ROOT).as_posix()
                for p in ROOT.rglob("*")
                if p.is_file()
                and not any(x in p.parts for x in (".git", "__pycache__", ".pytest_cache"))
            ]
        for rel in tracked:
            if not rel or rel in self.SCAN_SKIP or rel.startswith("tests/"):
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
            text = pre_submit_checks_read(rel)
            for old in retired:
                self.assertNotIn(old, text, f"{rel} still says {old!r}")
        # t1123: Track Changes ownership SSOT is ownership-contract, not registry meta
        own = pre_submit_checks_read("00_orchestrator/references/ownership-contract.md")
        self.assertIn("Track Changes", own)
        self.assertIn("Aitee", own)
        self.assertIn("Lee", own)
        mmd = pre_submit_checks_read("00_orchestrator/runtime-flow.mmd")
        self.assertIn("Lee · statement", mmd)
        self.assertLess(mmd.index("Lit05"), mmd.index("Gate \u00b7 05"))
        self.assertLess(mmd.index("Lit06"), mmd.index("Gate \u00b7 06"))
class AdvancedMirrorDedupe(unittest.TestCase):
    def test_no_cross_file_long_paragraph(self) -> None:
        seen: dict[str, str] = {}
        hits: list[str] = []
        skip = {".git", "__pycache__", ".pytest_cache", "fixtures"}
        for path in ROOT.rglob("*.md"):
            if set(path.parts) & skip:
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel == "INTEGRATION_MAP.md":
                continue
            for para in re.split(r"\n\s*\n", path.read_text(encoding="utf-8-sig", errors="ignore")):
                norm = re.sub(r"\s+", " ", para).strip()
                if len(norm) < MIN_CHARS:
                    continue
                if norm in seen and seen[norm] != rel:
                    hits.append(f"{rel} duplicates {seen[norm]}: {norm[:70]}")
                seen.setdefault(norm, rel)
        self.assertEqual(hits, [], "shared long paragraphs:\n" + "\n".join(hits[:10]))

    def test_mirror_pairs_share_no_long_paragraph(self) -> None:
        problems = []
        for base_rel, advanced_rel in MIRRORS:
            shared = _paragraphs(ROOT / base_rel) & _paragraphs(ROOT / advanced_rel)
            for text in sorted(shared):
                problems.append(f"{advanced_rel} duplicates {base_rel}: {text[:90]}")
        self.assertEqual(problems, [], "verbatim mirror:\n" + "\n".join(problems[:10]))


ADVANCED_VOCAB = ROOT / "05_manuscript" / "advanced" / "vocab"
HARVEST_SCRIPT = ADVANCED_VOCAB / "scripts" / "harvest_write_phrases.py"
ADVANCED_L2 = ADVANCED_VOCAB / "L2" / "preferred-advanced.md"


def _load_harvest():
    import importlib.util

    spec = importlib.util.spec_from_file_location("harvest_under_test", HARVEST_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class AdvancedL2PhraseTable(unittest.TestCase):
    """The owner's L2 table and its counter stay wired to the live vocab layers."""

    def test_table_exists_with_tiers_and_columns(self) -> None:
        text = ADVANCED_L2.read_text(encoding="utf-8")
        for needle in ("| A |", "| B |", "| C |", "| **Locked** |"):
            self.assertIn(needle, text)
        # Column headers are English; the Chinese form is kept as an accepted legacy shape.
        self.assertTrue(
            "| 表达 | 次数 | 篇数 |" in text or "| Phrase | Count | Docs |" in text,
            "advanced L2 table must expose Phrase / Count / Docs columns",
        )
        # Banned words are never restated here; the yaml is the only authority.
        self.assertIn("05_manuscript/base/vocab/L1/ban-terms.yaml", text)

    def test_base_readmes_point_at_the_advanced_table(self) -> None:
        for rel in (
            "05_manuscript/base/vocab/README.md",
            "05_manuscript/base/vocab/MODULE.md",
            "05_manuscript/advanced/route.md",
            "05_manuscript/advanced/voice-portrait.md",
        ):
            self.assertIn("preferred-advanced.md", (ROOT / rel).read_text(encoding="utf-8"), rel)

    def test_counter_is_cited_and_offline(self) -> None:
        cited = ADVANCED_L2.read_text(encoding="utf-8") + (
            ADVANCED_VOCAB / "README.md").read_text(encoding="utf-8")
        self.assertIn(HARVEST_SCRIPT.name, cited)
        source = HARVEST_SCRIPT.read_text(encoding="utf-8")
        imports = {
            line.split()[1].split(".")[0]
            for line in source.splitlines()
            if line.startswith("import ") or line.startswith("from ")
        }
        self.assertLessEqual(
            imports, {"__future__", "argparse", "collections", "json", "pathlib", "re", "sys"},
            "counter must stay stdlib only: %s" % sorted(imports),
        )
        self.assertNotIn("write_text(", source.split("def main")[0])

    def test_one_span_is_counted_once_per_sentence(self) -> None:
        """An overlapping head/tail window must not double the count."""
        harvest = _load_harvest()
        # 7 CJK chars: the 8-char window trims to the same string as the 7-char one.
        zh = Counter(harvest.zh_phrases("建议补充校准曲线。"))
        self.assertEqual(zh["建议补充校准曲线"], 1, dict(zh))
        en = Counter(harvest.en_phrases("Thank you for the suggestion."))
        self.assertEqual(en["thank you for the suggestion"], 1, dict(en))

    def test_doc_frequency_counts_papers_not_paragraphs(self) -> None:
        """One paper repeating a phrase ten times still counts as one paper.

        The phrase has to sit at a sentence edge: only edge windows are collected,
        which is what keeps mid-sentence fragments out of the table.
        """
        harvest = _load_harvest()
        sentence = ("This study has several limitations and the retrospective design "
                    "may have introduced selection bias in our cohort.")
        docs = [("Discussion", "doc1", sentence)] * 10 + [("Discussion", "doc2", sentence)]
        occurrences, presence, _sections, distinct = harvest.harvest(docs, "both")
        phrase = "this study"
        self.assertEqual(presence[phrase], 2, "篇数 must be 2 papers, not 11 paragraphs")
        self.assertGreater(occurrences[phrase], presence[phrase], "次数 must stay occurrences")
        self.assertEqual(distinct["Discussion"], 2)
        self.assertNotIn("the retrospective design", occurrences,
                         "mid-sentence spans must not be collected")
        self.assertIn("this study has several limitations", occurrences,
                      "sentence-head openers must survive the tail filter")

    def test_locked_rows_are_never_dropped_by_frequency(self) -> None:
        """`could assist [task]` is a mandated replacement, so a 0 count keeps it."""
        text = ADVANCED_L2.read_text(encoding="utf-8")
        self.assertIn("could assist [task]", text)
        self.assertIn("格式锁", text, "the Locked tier must be documented in the table")
        self.assertIn("Frequency never overrides a lock", text)


class BaseContractOnly(unittest.TestCase):
    """Owner lock 2026-10-30 (t1408u/t1409u): base is a thin contract, detail lives in advanced."""

    BASE_MODULES = sorted(
        p for p in ROOT.rglob("base/*/MODULE.md")
        if not any(part in SKIP_PARTS for part in p.parts)
    )

    def test_every_base_module_declares_the_contract(self) -> None:
        self.assertGreaterEqual(len(self.BASE_MODULES), 20)
        missing = []
        for path in ROOT.rglob("*/base/**/MODULE.md"):
            if any(part in SKIP_PARTS for part in path.parts):
                continue
            text = path.read_text(encoding="utf-8")
            if "Contract only" not in text and "thin contract" not in text.lower():
                missing.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(missing, [], "base MODULE without a contract line: " + ", ".join(missing))

    def test_qc_does_not_restate_the_fix_recipe(self) -> None:
        offenders = []
        for path in ROOT.rglob("*/qc/**/*.md"):
            if any(part in SKIP_PARTS for part in path.parts):
                continue
            if "Fix at writing time" in path.read_text(encoding="utf-8"):
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(offenders, [], "qc still carries a fix recipe column: " + ", ".join(offenders))

    def test_runtime_docs_state_the_loop(self) -> None:
        loops = (ROOT / "00_orchestrator/references/base-vs-advanced-top-loops.md").read_text(
            encoding="utf-8")
        flow = (ROOT / "00_orchestrator/runtime-flow.md").read_text(encoding="utf-8")
        for text, label in ((loops, "base-vs-advanced-top-loops.md"), (flow, "runtime-flow.md")):
            self.assertIn("post-QC revise", text, label)
            self.assertIn("`advanced/`", text, label)
        self.assertNotIn("Advanced layers do not host long procedure bodies", loops)
