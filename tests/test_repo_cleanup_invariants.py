"""Repo cleanup invariants (2026-10-24): detect forbidden structure / jargon.

Fail-now on leftover debt so Batch2 cleanup is forced. Historical NOTICE /
attribution lines are allowlisted where noted.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_PARTS = {".git", "__pycache__", ".pytest_cache", "node_modules"}

STATUS_TOKENS = re.compile(r"\b(MOUNTED|PROPOSED|ARCHIVED)\b")

STATUS_ALLOW_FILES = {
    "01_skill-integration/registry.yaml",
    "01_skill-integration/legacy_aliases.yaml",
    "VERSION.txt",
    "INTEGRATION_MAP.md",
    "ARCHITECTURE.md",
    "README.md",
}

STATUS_ALLOW_PREFIXES = (
    "01_skill-integration/",
    "tests/",
    "04_analysis/personal/visualization/",
)

STATUS_ALLOW_LINE = re.compile(
    r"NOTICE|attribution|historical|legacy|formerly|archived\s+20|"
    r"status_note|do not|not pickable|pytest|assert",
    re.I,
)

STATUS_SCAN_GLOBS = (
    "00_orchestrator/**/*.md",
    "00_orchestrator/**/*.yaml",
    "02_data-processing/**/*.md",
    "03_research/**/*.md",
    "04_analysis/**/*.md",
    "05_manuscript/**/*.md",
    "06_review/**/*.md",
    "07_response/**/*.md",
)

PACK_LABEL = re.compile(
    r"(?:\bMedSci\b|\bAIPOCH\b|\bARIS\b|"
    r"`scientific`|\bScientific\s+(?:pack|catalog|P\d)|"
    r"/\s*Scientific\s*/)"
)
# Chinese pack shorthand labels (kept out of the regex for source encoding safety).
PACK_EXTRA_LITERALS = ("B包", "A包")

PACK_ALLOW_FILES = {
    "01_skill-integration/registry.yaml",
    "VERSION.txt",
    "INTEGRATION_MAP.md",
    "ARCHITECTURE.md",
    "README.md",
}

PACK_ALLOW_PREFIXES = (
    "01_skill-integration/",
    "tests/",
)

PACK_ALLOW_LINE = re.compile(
    r"NOTICE|attribution|Distill of|distilled from|Source:|source_package|"
    r"Backup sources|formerly|archived|historical|legacy|MIT|"
    r"HTML comment|absorb|absorbed|do not install|host-agnostic|"
    r"wanshuiyin|Auto-claude|not vendored|status_note|"
    r"Scientific Reports|Scientific content|Scientific writing|"
    r"Scientific/clinical|Scientific Reviews|Scientific Agent|"
    r"Scientific Writing|Citing Scientific|Soft pointer|ARIS P1|"
    r"ARIS-ish|Source map|Backup:|来源:|原始来源|"
    r"does not install|out of scope",
    re.I,
)

FORBIDDEN_06_NAMES = (
    "chinese-journal-score-sheet.md",
    "thesis-review.md",
)

WORKFLOW_SOP_NAMES = (
    "radiomics-study.md",
    "sci-manuscript.md",
    "research-exploration-loop.md",
    "review-isolation.md",
    "question-to-reference.md",
)
WORKFLOW_HOME = ROOT / "01_skill-integration" / "workflows"
WORKFLOW_FORBIDDEN_DIRS = (
    ROOT / "00_orchestrator" / "workflows",
    ROOT / "03_research" / "workflows",
)

QC00 = ROOT / "00_orchestrator" / "qc"
QC_STUB = re.compile(
    r"(?i)(body moved to|moved to|pointer(?:\s+only)?|see\s+`?\.\./|stub\b)",
)

PROJECT_REF_TEMPLATE = ROOT / "00_orchestrator" / "references" / "project-ref-template"

DEAD_STUBS = (
    ROOT / "00_orchestrator" / "references" / "cross-manuscript-qc.md",
    ROOT / "00_orchestrator" / "references" / "manuscript-local-qc.md",
)


def _iter_files(globs: tuple[str, ...]):
    seen: set[Path] = set()
    for pat in globs:
        for p in ROOT.glob(pat):
            if not p.is_file():
                continue
            if any(part in SKIP_PARTS for part in p.parts):
                continue
            rp = p.resolve()
            if rp in seen:
                continue
            seen.add(rp)
            yield p


class RegistryStatusJargon(unittest.TestCase):
    """MOUNTED/PROPOSED/ARCHIVED only in registry SSOT (+ gen / NOTICE)."""

    def test_status_tokens_not_in_domain_agent_prose(self) -> None:
        violations: list[str] = []
        for path in _iter_files(STATUS_SCAN_GLOBS):
            rel = path.relative_to(ROOT).as_posix()
            if rel in STATUS_ALLOW_FILES:
                continue
            if any(rel.startswith(p) for p in STATUS_ALLOW_PREFIXES):
                continue
            if "NOTICE" in path.name.upper():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for i, line in enumerate(text.splitlines(), 1):
                if not STATUS_TOKENS.search(line):
                    continue
                if STATUS_ALLOW_LINE.search(line):
                    continue
                violations.append(f"{rel}:{i}: {line.strip()[:120]}")
        self.assertEqual(
            violations,
            [],
            "Registry status jargon outside SSOT allowlist:\n"
            + "\n".join(violations[:50]),
        )


class NoLivePackMenuLabels(unittest.TestCase):
    """MedSci/Scientific/AIPOCH/ARIS/A-pack/B-pack not active labels in skill bodies."""

    def test_no_active_pack_menu_labels(self) -> None:
        violations: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".yaml", ".yml", ".txt"}:
                continue
            if any(part in SKIP_PARTS for part in path.parts):
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("tests/"):
                continue
            if rel in PACK_ALLOW_FILES:
                continue
            if any(rel.startswith(pfx) for pfx in PACK_ALLOW_PREFIXES):
                continue
            if "NOTICE" in path.name.upper():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for i, line in enumerate(text.splitlines(), 1):
                if not (
                    PACK_LABEL.search(line)
                    or any(tok in line for tok in PACK_EXTRA_LITERALS)
                ):
                    continue
                if PACK_ALLOW_LINE.search(line):
                    continue
                violations.append(f"{rel}:{i}: {line.strip()[:120]}")
        self.assertEqual(
            violations,
            [],
            "Live pack menu labels outside historical/NOTICE allowlist:\n"
            + "\n".join(violations[:50]),
        )


class Forbidden06StandaloneSheets(unittest.TestCase):
    def test_no_chinese_journal_or_thesis_review_sheets(self) -> None:
        hits: list[str] = []
        review = ROOT / "06_review"
        if not review.is_dir():
            return
        for path in review.rglob("*"):
            if path.is_file() and path.name in FORBIDDEN_06_NAMES:
                hits.append(path.relative_to(ROOT).as_posix())
        self.assertEqual(
            hits,
            [],
            "Forbidden standalone 06_review sheets still present:\n" + "\n".join(hits),
        )


class WorkflowLocation(unittest.TestCase):
    """SOPs live under 01_skill-integration/workflows/; 00/03 workflow dirs absent."""

    def test_sops_home_under_01(self) -> None:
        missing = [
            name
            for name in WORKFLOW_SOP_NAMES
            if not (WORKFLOW_HOME / name).is_file()
        ]
        self.assertEqual(
            missing,
            [],
            "Workflow SOPs missing under 01_skill-integration/workflows/:\n"
            + "\n".join(missing),
        )

    def test_00_and_03_workflow_dirs_absent(self) -> None:
        present = [
            folder.relative_to(ROOT).as_posix()
            for folder in WORKFLOW_FORBIDDEN_DIRS
            if folder.exists()
        ]
        self.assertEqual(
            present,
            [],
            "00_orchestrator/workflows and 03_research/workflows must NOT exist "
            "(call 01_skill-integration/workflows/ directly):\n" + "\n".join(present),
        )


class Qc00PointersOnly(unittest.TestCase):
    """00_orchestrator/qc must NOT exist; bodies live in 02-07/qc only."""

    def test_00_qc_dir_absent(self) -> None:
        self.assertFalse(
            QC00.exists(),
            "00_orchestrator/qc/ must NOT exist "
            "(seat standards under 02-07/qc/; 00 calls them via gates.md)",
        )


class ProjectRefTemplateGone(unittest.TestCase):
    def test_project_ref_template_absent(self) -> None:
        self.assertFalse(
            PROJECT_REF_TEMPLATE.exists(),
            "00_orchestrator/references/project-ref-template/ must not exist",
        )


class DeadOrchestratorQcStubs(unittest.TestCase):
    """Orphan moved-to stubs under 00 references must be deleted (fail-now)."""

    def test_orphan_00_qc_stubs_absent(self) -> None:
        present = [
            p.relative_to(ROOT).as_posix() for p in DEAD_STUBS if p.is_file()
        ]
        self.assertEqual(
            present,
            [],
            "Dead 00 orchestrator QC stubs still present "
            "(bodies already live under domain qc/):\n" + "\n".join(present),
        )


if __name__ == "__main__":
    unittest.main()
