"""CHG-20260903-013 audit invariants + CHG-20260903-014 选刊→03. No-LLM fixtures."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CLIN = ROOT / "02_data-processing" / "clinical-data-extraction"
REG = ROOT / "01_skill-discovery-integration" / "registry.yaml"
MOUNTED = ROOT / "01_skill-discovery-integration" / "MOUNTED_SKILLS.md"
SKIP_PARTS = {".git", "__pycache__"}
SKIP_NAMES = {
    "INTEGRATION_MAP.md",
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
ID_TICK_RE = re.compile(r"`([0-9]{2}-[a-z0-9-]+)`")


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


def registry_mount_ids() -> list[str]:
    text = REG.read_text(encoding="utf-8")
    # mounts: ... until proposals:
    m = re.search(r"^mounts:\n(.*)^proposals:", text, re.M | re.S)
    self_block = m.group(1) if m else text
    ids = re.findall(r"^\s+- id:\s*(\S+)\s*$", self_block, re.M)
    return ids


def mounted_md_ids() -> list[str]:
    text = MOUNTED.read_text(encoding="utf-8")
    ids = ID_TICK_RE.findall(text)
    # keep order, unique
    seen = []
    for i in ids:
        if i not in seen:
            seen.append(i)
    return seen


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
    def test_workflows_ask_session_mount_pick(self) -> None:
        for rel in (
            "00_orchestrator/workflows/sci-manuscript.md",
            "00_orchestrator/workflows/radiomics-study.md",
            "00_orchestrator/workflows/README.md",
        ):
            text = read(rel).lower()
            self.assertTrue(
                "session mount pick" in text or "session-mount pick" in text,
                f"{rel} must ask session mount pick",
            )
            self.assertIn("do not auto-load", text, rel)


class RegistryMenu(unittest.TestCase):
    def test_registry_matches_mounted_skills_30(self) -> None:
        reg = registry_mount_ids()
        md = mounted_md_ids()
        self.assertEqual(len(reg), 30, msg=str(reg))
        self.assertEqual(sorted(reg), sorted(md), msg=f"reg={reg}\nmd={md}")
        self.assertNotIn("04-figure-engine", reg)
        self.assertNotIn("02-xlsx", reg)
        self.assertIn("04-fig-flow", reg)
        self.assertIn("04-fig-plot", reg)
        self.assertIn("05-write-venue", reg)
        self.assertIn("04-stats-power", reg)


class ArchitectureSsot(unittest.TestCase):
    def test_root_and_meta_agree_on_live_rules(self) -> None:
        root = read("ARCHITECTURE.md")
        meta = read("_medical-research-meta/ARCHITECTURE.md")
        for label, text in (("root", root), ("meta", meta)):
            low = text.lower()
            self.assertRegex(text, r"(four parts|≤\s*4|at most four)", label)
            self.assertIn("default source", low, label)
            self.assertRegex(low, r"\bb\b", label)
            self.assertIn("ethics", low, label)
            self.assertIn("03_research", text, label)
            self.assertIn("PROPOSED", text, label)
            self.assertIn("ask-each-run", text, label)
            self.assertIn("04-fig-flow", text, label)
            self.assertIn("04-fig-plot", text, label)
            self.assertIn("05-write-venue", text, label)
            self.assertIn("04-stats-power", text, label)
            self.assertNotRegex(low, r"≤\s*3", label)
            self.assertNotIn("role: default-candidate", text, label)
            self.assertNotIn("Default candidate: `Imbad0202", text, label)


class FastRouting(unittest.TestCase):
    def test_venue_and_power_routes(self) -> None:
        zero = read("00_orchestrator/SKILL.md")
        self.assertIn("选刊 → `03_research`", zero)
        self.assertNotIn("选刊 → `05_manuscript` (`05-write-venue`)", zero)
        self.assertIn("样本量 → `04_analysis` (`04-stats-power`)", zero)
        six = read("06_review/SKILL.md")
        self.assertIn("选刊 → `03_research`", six)
        self.assertNotIn("选刊 → `05_manuscript` (`05-write-venue`)", six)
        ethics = read("03_research/ethics-application-forms/SKILL.md")
        self.assertIn("选刊 → `03_research`", ethics)
        self.assertNotIn("选刊 → `05_manuscript` (`05-write-venue`)", ethics)
        self.assertNotIn("radiology-ethics", ethics)
        harvest = read("skill-harvest/references/route-map.md")
        self.assertIn("选刊 → `03_research`", harvest)
        self.assertNotIn("选刊 → `05-write-venue`", harvest)
        self.assertIn("04-stats-power", harvest)
        five = read("05_manuscript/SKILL.md")
        self.assertIn("05-write-venue", five)
        self.assertIn("journal templates / house style", five)
        self.assertNotIn("选刊 is `05-write-venue`", five)
        three = read("03_research/SKILL.md")
        self.assertIn("journal-selection.md", three)
        self.assertIn("03-lit-search", three)
        self.assertIn("Do not send 选刊 to `05-write-venue`", three)


class DeAiAndFigures(unittest.TestCase):
    def test_sci_manuscript_paths(self) -> None:
        sop = read("00_orchestrator/workflows/sci-manuscript.md")
        self.assertIn("05_manuscript/personal/forbidden-phrases.md", sop)
        self.assertIn("04-fig-flow", sop)
        self.assertIn("04-fig-plot", sop)
        self.assertNotIn("de-ai/forbidden-phrases.md", sop)
        four = read("04_analysis/SKILL.md")
        self.assertIn("04-figure-engine", four)
        self.assertIn("Retired:", four)


class HarvestHygiene(unittest.TestCase):
    def test_no_duplicate_section_11(self) -> None:
        text = read("skill-harvest/SKILL.md")
        self.assertEqual(len(re.findall(r"^## 11\.", text, re.M)), 1)
        self.assertIn("## 13. ROI ledger", text)

    def test_keep_vs_skip_no_bundle(self) -> None:
        text = read("skill-harvest/references/keep-vs-skip.md")
        self.assertNotIn("00–06 bundle", text)
        self.assertIn("00–06 skill", text)

    def test_medsci_unmapped_not_duplicated(self) -> None:
        text = read("01_skill-discovery-integration/mounts/medsci.md")
        self.assertEqual(text.count("## A 没有对应接口"), 1)

    def test_project_state_no_yellow(self) -> None:
        text = read("00_orchestrator/templates/project-state.yaml")
        self.assertNotIn("blank = yellow highlight", text.lower())
        self.assertIn("never yellow highlight", text.lower())
        self.assertIn("Word comment", text)

    def test_externalization_has_fulltext_and_protocol(self) -> None:
        text = read("EXTERNALIZATION_CANDIDATES.md")
        self.assertIn("lit-fulltext/", text)
        self.assertIn("design-protocol/", text)

    def test_version_is_this_chg(self) -> None:
        text = read("_medical-research-meta/VERSION.txt")
        self.assertIn("CHG-20260903-014", text)
        self.assertIn("选刊", text)
        self.assertIn("03", text)

    def test_integration_map_has_this_chg(self) -> None:
        text = read("_medical-research-meta/INTEGRATION_MAP.md")
        self.assertIn("CHG-20260903-014", text)
        self.assertIn("CHG-20260903-013", text)
        self.assertIn("CHG-20260903-012", text)

    def test_skills_map_html_gone(self) -> None:
        self.assertFalse((ROOT / "SKILLS_map.html").exists())
        readme = read("README.md")
        self.assertNotIn("SKILLS_map.html", readme)
        self.assertNotIn("mounts: []", readme)


if __name__ == "__main__":
    unittest.main()
