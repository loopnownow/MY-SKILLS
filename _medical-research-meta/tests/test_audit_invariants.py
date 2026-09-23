"""CHG-20260903-013 audit invariants + CHG-20260903-014 选刊→03. No-LLM fixtures."""
from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

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


def registry_mount_ids() -> list[str]:
    text = REG.read_text(encoding="utf-8")
    # mounts: ... until reference_only: (v4) or proposals: (v3)
    m = re.search(r"^mounts:\n(.*?)^(?:reference_only:|archived:|proposals:)", text, re.M | re.S)
    self_block = m.group(1) if m else text
    ids = re.findall(r"^\s+- id:\s*(\S+)\s*$", self_block, re.M)
    return ids


def mounted_md_ids() -> list[str]:
    """Fine ids from MOUNTED_SKILLS session-pick tables (backtick slugs)."""
    text = MOUNTED.read_text(encoding="utf-8")
    # Prefer table rows under session-pick section
    ids = []
    for line in text.splitlines():
        if not line.startswith("| `"):
            continue
        m = re.match(r"^\| `([^`]+)` \|", line)
        if not m:
            continue
        fid = m.group(1)
        if fid in {"Id", "Fine id"}:
            continue
        # skip archived section markers later — only collect until Reference-only
        ids.append(fid)
    # Truncate at reference-only heading by re-parse
    if "## Reference-only" in text:
        head = text.split("## Reference-only")[0]
        ids = []
        for line in head.splitlines():
            m = re.match(r"^\| `([^`]+)` \|", line)
            if m and m.group(1) not in {"Id", "Fine id"}:
                ids.append(m.group(1))
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
    def test_registry_matches_mounted_skills_v4(self) -> None:
        reg = registry_mount_ids()
        md = mounted_md_ids()
        self.assertEqual(len(reg), 52, msg=str(reg))
        self.assertEqual(sorted(reg), sorted(md), msg=f"reg={reg}\nmd={md}")
        self.assertNotIn("04-figure-engine", reg)
        self.assertNotIn("02-xlsx", reg)
        self.assertNotIn("02-fmri", reg)
        self.assertNotIn("04-explainability", reg)
        self.assertIn("make-figures", reg)
        self.assertIn("fig-plot", reg)
        self.assertIn("imaging-io", reg)
        self.assertIn("lit-search", reg)
        self.assertIn("frontier-hypothesize", reg)
        self.assertIn("calc-sample-size", reg)
        self.assertIn("humanize", reg)
        self.assertIn("write-paper", reg)
        # ARS/OpenClaw purged from catalog; never remount
        blob = REG.read_text(encoding="utf-8")
        mount_blob = blob.split("mounts:")[1].split("reference_only:")[0]
        self.assertNotIn("openclaw", mount_blob.lower())
        self.assertNotIn("academic-research-skills", mount_blob.lower())
        self.assertIn("ars_openclaw_policy: removed-from-catalog", blob)
        self.assertNotIn("openclaw_policy: never-mount-as-atomic-source", blob)
        self.assertNotIn("id: openclaw-medical-skills", blob)
        self.assertNotIn("id: academic-research-skills", blob)
        self.assertIn("session_pick_unit: fine_id", blob)


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
            self.assertRegex(text, r"52 fine", label)
            self.assertNotRegex(low, r"≤\s*3", label)
            self.assertNotIn("role: default-candidate", text, label)
            self.assertNotIn("Default candidate: `Imbad0202", text, label)


class RepoMapGenerated(unittest.TestCase):
    """repo-map.html (00_orchestrator/scripts/gen_repo_map.py) is generated
    from registry.yaml, same anti-drift pattern as MOUNTED_SKILLS.md."""

    def test_repo_map_matches_registry(self) -> None:
        script = ROOT / "00_orchestrator" / "scripts" / "gen_repo_map.py"
        result = subprocess.run(
            [sys.executable, str(script), "--check"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class MountedBytesPresent(unittest.TestCase):
    """CHG-20260913-006: `humanize` was declared MOUNTED with zero bytes on
    disk at mounts-cap/. This makes that manual audit permanent: every
    MOUNTED fine id must have real bytes in mounts-cap/<source-dir>/<path>,
    or this fails instead of surviving until the next manual scan."""

    SRC_DIR = {
        "my-skills-capabilities": "b",
        "med-sci-skills": "medsci",
        "nature-skills": "nature",
        "scientific-agent-skills": "scientific",
        "aipoch-medical-research-skills": "aipoch",
    }

    def test_mounted_fine_ids_have_bytes_on_disk(self) -> None:
        reg = yaml.safe_load(REG.read_text(encoding="utf-8"))
        missing = []
        for m in reg["mounts"]:
            if m.get("status") != "MOUNTED":
                continue
            folder = self.SRC_DIR.get(m.get("source"))
            if not folder:
                continue
            full = ROOT / "mounts-cap" / folder / m.get("path", "")
            if not full.exists():
                missing.append((m["id"], str(full.relative_to(ROOT))))
        self.assertEqual(missing, [], f"MOUNTED fine ids with no bytes on disk: {missing}")


class MountedSkillsGenerated(unittest.TestCase):
    """MOUNTED_SKILLS.md used to be a hand-copied table that could drift from
    registry.yaml. It's now generated by scripts/gen_mounted_skills.py;
    this test fails if someone hand-edits MOUNTED_SKILLS.md without
    re-running the generator (or edits registry.yaml without regenerating)."""

    def test_mounted_skills_matches_registry(self) -> None:
        script = ROOT / "01_skill-discovery-integration" / "scripts" / "gen_mounted_skills.py"
        result = subprocess.run(
            [sys.executable, str(script), "--check"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class ReadmeSsot(unittest.TestCase):
    """CHG-20260913-002: README.md drifted to stale '30-id' wording while
    registry.yaml/ARCHITECTURE.md had already moved to v4 (10 coarse + 52
    fine). ArchitectureSsot only checked the two ARCHITECTURE.md files;
    this closes that blind spot for both README.md files."""

    def test_root_and_meta_readme_match_v4(self) -> None:
        root = read("README.md")
        meta = read("_medical-research-meta/README.md")
        for label, text in (("root", root), ("meta", meta)):
            self.assertRegex(text, r"52 fine", label)
            self.assertNotIn("30-id", text, label)
            self.assertNotIn("30 coarse", text, label)


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



class OrchestratorLoop(unittest.TestCase):
    def test_intent_chain_qc_in_skill(self) -> None:
        zero = read("00_orchestrator/SKILL.md")
        low = zero.lower()
        self.assertIn("intent classify", low)
        self.assertIn("skill chain", low)
        self.assertIn("QC closed loop", zero)
        self.assertIn("Never `--e2e`", zero)
        self.assertIn("Literature enters 03 only", zero)
        self.assertIn("reviewer response only here", zero)
        self.assertNotIn("Do not mount ARS", zero)
        self.assertNotIn("academic-pipeline", zero)
        self.assertIn("Do not mount MedSci", zero)
        self.assertIn("orchestrate", zero)
        self.assertIn("Excel / 批处理 / 0RAD 文件夹 → `02_data-processing`", zero)

    def test_gates_and_handoff_exist(self) -> None:
        gates = read("00_orchestrator/gates.md")
        for token in ("G0", "G-PHI", "G-04", "G-05", "G-06", "Development set", "VAL_MODE", "DeLong"):
            self.assertIn(token, gates)
        hand = read("00_orchestrator/templates/handoff.yaml")
        self.assertIn("qc_gate:", hand)
        self.assertIn("outputs:", hand)
        state = read("00_orchestrator/templates/project-state.yaml")
        self.assertIn("pipeline:", state)
        self.assertIn("stage:", state)
        self.assertIn("defects:", state)

    def test_sops_wired_by_html(self) -> None:
        rad = read("00_orchestrator/workflows/radiomics-study.md")
        sci = read("00_orchestrator/workflows/sci-manuscript.md")
        self.assertIn("sci-manuscript", rad)
        self.assertIn("G-04", rad)
        self.assertIn("G-05", sci)
        self.assertIn("G-06", sci)
        self.assertIn("05_manuscript/personal/forbidden-phrases.md", sci)
        wf = read("00_orchestrator/workflows/README.md")
        self.assertIn("gates.md", wf)





class AttributionAndFetch(unittest.TestCase):

    def test_skill_level_prefix_rules(self) -> None:
        style = read("06_review/personal/personal-review-style.md")
        self.assertIn("[Nature:nature-reviewer]", style)
        self.assertIn("包内skill-id", style.replace(" ", ""))
        gates = read("00_orchestrator/gates.md")
        self.assertIn("skill-level prefix", gates)
        preset = read("01_skill-discovery-integration/mounts/presets/review-hybrid.yaml")
        self.assertIn("skills: [citation-management]", preset)
        self.assertIn("skills: [stats-guide]", preset)
        self.assertIn("required: false", preset)
        self.assertIn("skills: [scientific-critical-thinking]", preset)


    def test_author_vs_prefix(self) -> None:
        text = read("06_review/personal/personal-review-style.md")
        self.assertIn("作者字段", text)
        self.assertIn("作者栏 ≠ 来源标签", text)
        self.assertIn("双标", text)
        self.assertNotIn("[ARS:", text)
        self.assertNotIn("[OpenClaw:", text)
        self.assertIn("[MedSci:", text)
        self.assertIn("[Scientific:", text)
        self.assertIn("同一 DOI", text)
        zero = read("00_orchestrator/SKILL.md")
        self.assertIn("personal-review-style.md` §0", zero)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("skill-level prefix", gates)
        five = read("05_manuscript/SKILL.md")
        self.assertIn("New citation numbers", five)

    def test_fetch_merge_helpers(self) -> None:
        fetch = read("mounts-cap/fetch.py")
        self.assertIn("merge_source_state", fetch)
        self.assertIn("Prefer zip", fetch)
        self.assertIn("_state_lock", fetch)
        self.assertIn("via zip", fetch)


class ReviewInteract(unittest.TestCase):
    def test_review_resolution_protocol(self) -> None:
        text = read("06_review/personal/review-resolution.md")
        self.assertIn("Review Issue", text)
        for s in ("resolved", "partially_resolved", "unresolved", "new_issue"):
            self.assertIn(s, text)
        self.assertIn("A 06 personal", text)
        self.assertIn("B06 upgrade", text)
        skill = read("06_review/SKILL.md")
        self.assertIn("review-resolution.md", skill)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("review-resolution.md", gates)

    def test_personal_review_eight_sections(self) -> None:
        text = read("06_review/personal/personal-review-style.md")
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
        self.assertIn("Personal review layout", six)
        self.assertIn("User decides", six)
        resp = read("06_review/personal/personal-response-style.md")
        self.assertIn("词或句", resp)

    def test_evidence_request_protocol(self) -> None:
        text = read("05_manuscript/personal/evidence-request.md")
        self.assertIn("Evidence Request", text)
        self.assertIn("Accept", text)
        self.assertIn("Weaken", text)
        self.assertIn("Delete", text)
        self.assertIn("03_research", text)
        self.assertNotIn("B05 = Personal Writing", text)
        skill = read("05_manuscript/SKILL.md")
        self.assertIn("evidence-request.md", skill)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("evidence-request.md", gates)


class MountsCap(unittest.TestCase):
    def test_cache_scaffold(self) -> None:
        self.assertFalse((ROOT / "archive").exists())
        root = ROOT / "mounts-cap"
        self.assertTrue((root / "README.md").is_file())
        self.assertTrue((root / "INDEX.yaml").is_file())
        self.assertTrue((root / "fetch.py").is_file())
        gi = read("mounts-cap/.gitignore")
        for name in ("b/", "ars/", "medsci/", "scientific/", "openclaw/", "aipoch/", "nature/", "STATE.yaml"):
            self.assertIn(name, gi)
        idx = read("mounts-cap/INDEX.yaml")
        self.assertIn("on-demand-path-only", idx)
        self.assertIn("never_bulk_backup", idx)
        self.assertNotIn("openclaw-medical-skills: openclaw", idx)
        self.assertNotIn("academic-research-skills: ars", idx)
        self.assertIn("aipoch-medical-research-skills: aipoch", idx)
        self.assertIn("nature-skills: nature", idx)
        # Local fetch cache dirs may exist on a developer box; they must stay gitignored.
        git_dir = ROOT / ".git"
        if not git_dir.exists():
            self.skipTest("Git metadata is not present in exported ZIP; tracked-file assertion requires a Git checkout")
        tracked = subprocess.check_output(
            ["git", "ls-files", "mounts-cap/b", "mounts-cap/openclaw", "mounts-cap/aipoch", "mounts-cap/nature"],
            cwd=ROOT,
            text=True,
        ).strip()
        self.assertEqual(tracked, "")

    def test_01_uses_cache_not_bulk(self) -> None:
        one = read("01_skill-discovery-integration/SKILL.md")
        self.assertIn("mounts-cap/", one)
        self.assertIn("Download is not a mount", one)
        self.assertIn("Never bulk-download", one)
        fetch = read("mounts-cap/fetch.py")
        self.assertIn("ensure-b", fetch)
        self.assertNotIn("def download_all", fetch)
        self.assertIn("04-explainability", read("01_skill-discovery-integration/SKILL.md"))


class LocalLinkHygiene(unittest.TestCase):
    def test_no_broken_relative_markdown_links(self) -> None:
        errors = []
        skip_parts = {".git", "mounts-cap", "__pycache__"}
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


class HarvestHygiene(unittest.TestCase):
    def test_harvest_orchestrator_slim(self) -> None:
        text = read("skill-harvest/SKILL.md")
        # Batch2: SKILL is orchestrator only (SCAN→PROPOSE→APPROVAL→MEASURE); detail in references/
        for token in ("SCAN", "PROPOSE", "USER APPROVAL", "MEASURE"):
            self.assertIn(token, text)
        low = text.lower()
        for token in ("decide", "modify", "deploy"):
            self.assertIn(token, low)
        for ref in (
            "references/evolution-policy.md",
            "references/benefit-metrics.md",
            "references/keep-merge-delete.md",
            "references/boundary-contract.md",
            "references/route-map.md",
        ):
            self.assertIn(ref, text)
        n = len(text.splitlines())
        self.assertGreaterEqual(n, 160)
        self.assertLessEqual(n, 260)
        self.assertTrue((ROOT / "skill-harvest" / "references" / "keep-merge-delete.md").is_file())

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
            "| G-04 | QUALITY |",
            "| G-05 | QUALITY |",
            "| G-06 | QUALITY |",
            "| G-LIT | QUALITY |",
            "| G-CODE | QUALITY |",
        ):
            self.assertIn(row, gates)

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
        self.assertIn("CHG-20260913-001", text)
        self.assertIn("v4", text.lower())
        self.assertIn("fine", text.lower())


    def test_integration_map_has_this_chg(self) -> None:
        text = read("_medical-research-meta/INTEGRATION_MAP.md")
        self.assertIn("CHG-20260906-003", text)
        self.assertIn("CHG-20260906-006", text)
        self.assertIn("CHG-20260906-007", text)
        self.assertIn("CHG-20260906-008", text)
        self.assertIn("CHG-20260906-009", text)
        self.assertIn("CHG-20260907-001", text)
        self.assertIn("CHG-20260907-002", text)
        self.assertIn("CHG-20260906-002", text)
        self.assertIn("CHG-20260906-001", text)
        self.assertIn("CHG-20260913-001", text)


    def test_skills_map_html_gone(self) -> None:
        self.assertFalse((ROOT / "SKILLS_map.html").exists())
        readme = read("README.md")
        self.assertNotIn("SKILLS_map.html", readme)
        self.assertNotIn("mounts: []", readme)


    def test_harvest_qc_lean(self) -> None:
        self.assertTrue((ROOT / "skill-harvest" / "qc" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "skill-harvest" / "qc" / "rules.md").is_file())
        self.assertTrue((ROOT / "skill-harvest" / "templates" / "qc-evolution.html").is_file())
        self.assertTrue((ROOT / "skill-harvest" / "data" / "qc-events" / "README.md").is_file())
        qc = read("skill-harvest/qc/SKILL.md")
        self.assertIn("Never auto-modify", qc)
        self.assertIn("Do **not** create `07_QC`", qc)
        self.assertIn("OBSERVED", read("skill-harvest/qc/SKILL.md"))


if __name__ == "__main__":
    unittest.main()
