"""CHG-20260903-013 audit invariants + CHG-20260903-014 选刊→03. No-LLM fixtures."""
from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CAP_ROOT = Path(r"D:\0Grok\0doc\04-lab-reference\mounts-cap")
CLIN = ROOT / "02_data-processing" / "personal"
REG = ROOT / "01_skill-integration" / "registry.yaml"
MOUNTED = ROOT / "01_skill-integration" / "MOUNTED_SKILLS.md"
SKIP_PARTS = {".git", "__pycache__", "history", "mounts-cap"}
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


def registry_mount_ids() -> list[str]:
    text = REG.read_text(encoding="utf-8")
    # mounts: ... until reference_only: (v4) or proposals: (v3)
    m = re.search(r"^mounts:\n(.*?)^(?:reference_only:|archived:|proposals:)", text, re.M | re.S)
    self_block = m.group(1) if m else text
    ids = re.findall(r"^\s+- id:\s*(\S+)\s*$", self_block, re.M)
    return ids


def mounted_md_ids_from(text: str) -> list[str]:
    """Fine ids from MOUNTED_SKILLS table rows in one section."""
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
        reg_doc = yaml.safe_load(REG.read_text(encoding="utf-8"))
        reg = registry_mount_ids()
        text = MOUNTED.read_text(encoding="utf-8")
        pick, rest = text.split("## Optional candidates", 1)
        proposed, _ref = rest.split("## Reference-only", 1)
        md_pick = mounted_md_ids_from(pick)
        md_prop = mounted_md_ids_from(proposed)
        want_pick = [m["id"] for m in reg_doc["mounts"] if m.get("status") == "MOUNTED"]
        want_prop = [m["id"] for m in reg_doc["mounts"] if m.get("status") == "PROPOSED"]
        self.assertEqual(len(reg), len(reg_doc["mounts"]), msg=str(reg))
        self.assertEqual(sorted(md_pick), sorted(want_pick))
        self.assertEqual(sorted(md_prop), sorted(want_prop))
        self.assertEqual(sorted(md_pick + md_prop), sorted(reg))
        self.assertFalse(set(md_pick) & set(md_prop))
        self.assertNotIn("04-figure-engine", reg)
        self.assertNotIn("02-xlsx", reg)
        self.assertNotIn("02-fmri", reg)
        self.assertNotIn("04-explainability", reg)
        self.assertIn("draw-flowchart", reg)
        self.assertIn("plot-figures", reg)
        self.assertIn("imaging-io", reg)
        self.assertIn("lit-search", reg)
        self.assertIn("design-study", reg)  # frontier-hypothesize absorbed round 2
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
    """Single root ARCHITECTURE.md = intent tables + QC/handoff + ownership + live routing keywords."""

    def test_architecture_live_rules(self) -> None:
        text = read("ARCHITECTURE.md")
        low = text.lower()
        self.assertGreater(len(text), 500)
        self.assertRegex(text, r"(five parts|≤\s*5|at most five)")
        self.assertIn("default source", low)
        self.assertIn("my-skills", low)
        self.assertIn("in-repo", low)
        self.assertNotIn("my-skills-base", low)
        self.assertNotIn("MY-SKILLS-base", text)
        self.assertIn("ethics", low)
        self.assertIn("03_research", text)
        self.assertIn("PROPOSED", text)
        self.assertIn("ask-each-run", text)
        self.assertIn("draw-flowchart", text)
        self.assertIn("plot-figures", text)
        self.assertIn("find-journal", text)
        self.assertIn("venue-templates", text)
        self.assertIn("calc-sample-size", text)
        self.assertNotIn("05-write-venue", text)
        self.assertNotIn("04-stats-power", text)
        self.assertIn("01_skill-integration/registry.yaml", text)
        self.assertNotRegex(text, r"52 fine")
        self.assertIn("per registry", low)
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
        self.assertIn("personal/extract.md", text)
        # Full mount/ceiling/Cache section headings stay out of this intent file
        self.assertNotIn("## A/B no-reflow contract", text)
        self.assertNotIn("## Fine-id expansion ceiling", text)
        self.assertNotIn("## Cache ≠ Mount ≠ Active", text)
        self.assertNotIn("## load_priority", text)

    def test_readme_keeps_lab_homes(self) -> None:
        readme = read("README.md")
        self.assertIn("{script_root}", readme)
        self.assertIn("lab", readme.lower())
        self.assertIn("{doc_root}", readme)
        text = read("ARCHITECTURE.md")
        self.assertIn("find-journal", text)
        self.assertIn("fill-protocol", text)


class RoutingFourTuple(unittest.TestCase):
    def test_find_journal_and_fill_protocol_stay_on_03(self) -> None:
        reg = yaml.safe_load(REG.read_text(encoding="utf-8"))
        by_id = {m["id"]: m for m in reg["mounts"]}
        self.assertEqual(by_id["find-journal"]["a_domain"], "03_research")
        self.assertEqual(by_id["fill-protocol"]["a_domain"], "03_research")
        self.assertEqual(by_id["grant-builder"]["a_domain"], "03_research")
        fj_note = by_id["find-journal"]["note"]
        fp_note = by_id["fill-protocol"]["note"]
        self.assertTrue(
            "03-research/find-journal" in fj_note or "03_research/base/find-journal" in fj_note,
            fj_note,
        )
        self.assertTrue(
            "03-research/fill-protocol" in fp_note or "03_research/base/fill-protocol" in fp_note,
            fp_note,
        )
        self.assertNotRegex(read("ARCHITECTURE.md"), r"选刊\s*→\s*05")
        self.assertNotRegex(read("01_skill-integration/SKILL.md"), r"选刊\s*→\s*05")


class DiscoverySurface(unittest.TestCase):
    def test_cursorignore_excludes_mounts_cap(self) -> None:
        text = read(".cursorignore")
        self.assertTrue("mounts-cap" in text or "{mounts_cap}" in text)

    def test_auto_discovery_rule_is_in_00_and_01(self) -> None:
        zero = read("00_orchestrator/SKILL.md")
        one = read("01_skill-integration/SKILL.md")
        life = read("01_skill-integration/references/lifecycle-cache.md")
        self.assertTrue("mounts-cap" in zero or "mounts_cap" in zero)
        self.assertIn("session_picked_fine_ids", zero)
        self.assertIn("session_picked_fine_ids", one)
        # advertised skills = 00–07 (skill-harvest archived → MY-RULES skills.md / skill-evolution)
        self.assertIn('only `00_orchestrator`–`07_response`', zero)
        self.assertNotIn("and `skill-harvest`", zero)
        self.assertTrue("`00`–`06` only" in life or "`00`–`07` only" in life)
        self.assertNotIn("and `skill-harvest` only", life)
        self.assertIn("skills.md", one)

    def test_live_docs_do_not_handwrite_52_fine(self) -> None:
        for rel in (
            "01_skill-integration/references/hybrid-mount-pointers.md",
            "00_orchestrator/workflows/research-exploration-loop.md",
        ):
            self.assertNotRegex(read(rel), r"52 fine", rel)


class RepoMapGenerated(unittest.TestCase):
    """repo-map.html (00_orchestrator/scripts/gen_repo_map.py) is generated
    from registry.yaml, same anti-drift pattern as MOUNTED_SKILLS.md."""

    def test_repo_map_matches_registry(self) -> None:
        script = ROOT / "04_analysis" / "personal" / "visualization" / "scripts" / "gen_repo_map.py"
        if not script.is_file():
            self.skipTest("gen_repo_map.py missing")
        out = Path(r"D:/0Grok/0doc/04-lab-reference/my-skills-viz/repo-map.html")
        if not out.is_file():
            self.skipTest("lab repo-map.html absent; regenerate on lab host")
        result = subprocess.run(
            [sys.executable, str(script), "--check"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class MountedBytesPresent(unittest.TestCase):
    """CHG-20260913-006: `humanize` was declared MOUNTED with zero bytes on
    disk at D:/0Grok/0doc/04-lab-reference/mounts-cap. This makes that manual audit permanent: every
    MOUNTED fine id must have real bytes in CAP_ROOT/<source-dir>/<path>,
    or this fails instead of surviving until the next manual scan."""

    SRC_DIR = {
        "med-sci-skills": "medsci",
        "nature-skills": "nature",
        "scientific-agent-skills": "scientific",
        "aipoch-medical-research-skills": "aipoch",
    }
    # Gitignored pack trees. Empty on a fresh checkout; do not vendor them.
    PACK_DIRS = ("b", "ars", "medsci", "scientific", "openclaw", "aipoch", "nature")

    def _cache_has_pack_bytes(self) -> bool:
        root = CAP_ROOT
        for name in self.PACK_DIRS:
            folder = root / name
            if not folder.is_dir():
                continue
            for path in folder.rglob("*"):
                if path.is_file():
                    return True
        return False

    def test_mounted_fine_ids_have_bytes_on_disk(self) -> None:
        if not self._cache_has_pack_bytes():
            self.skipTest("mounts-cap cache has no pack bytes")
        reg = yaml.safe_load(REG.read_text(encoding="utf-8"))
        missing = []
        for m in reg["mounts"]:
            if m.get("status") != "MOUNTED":
                continue
            src = m.get("source")
            # Pilot 2026-10-17: in-repo source my-skills resolves under A ROOT, not mounts-cap.
            if src == "my-skills":
                full = ROOT / m.get("path", "")
                if not full.exists():
                    missing.append((m["id"], str(full)))
                continue
            folder = self.SRC_DIR.get(src)
            if not folder:
                continue
            full = CAP_ROOT / folder / m.get("path", "")
            if not full.exists():
                missing.append((m["id"], str(full)))
        self.assertEqual(missing, [], f"MOUNTED fine ids with no bytes on disk: {missing}")


class MountedSkillsGenerated(unittest.TestCase):
    """MOUNTED_SKILLS.md used to be a hand-copied table that could drift from
    registry.yaml. It's now generated by scripts/gen_mounted_skills.py;
    this test fails if someone hand-edits MOUNTED_SKILLS.md without
    re-running the generator (or edits registry.yaml without regenerating)."""

    def test_mounted_skills_matches_registry(self) -> None:
        script = ROOT / "01_skill-integration" / "scripts" / "gen_mounted_skills.py"
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
        self.assertIn("样本量 → `04_analysis` (`calc-sample-size`)", fast)
        six = read("06_review/SKILL.md")
        # A06 top layer: journal select out of scope (points to 03), not a fast-routing table
        self.assertIn("03_research", six)
        self.assertNotIn("05-write-venue", six)
        ethics = read("03_research/personal/fill-protocol/README.md")
        # Jinshan PHI pack; capability body is B fill-protocol; journal select not here
        self.assertIn("fill-protocol", ethics)
        self.assertNotIn("05-write-venue", ethics)
        five = read("05_manuscript/SKILL.md")
        self.assertIn("venue-templates", five)
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
        self.assertIn("05-manuscript/vocab/L1/ban-phrases.md", sop)
        self.assertIn("draw-flowchart", sop)
        self.assertIn("plot-figures", sop)
        self.assertNotIn("04-fig-flow", sop)
        self.assertNotIn("de-ai/forbidden-phrases.md", sop)
        four = read("04_analysis/SKILL.md")
        self.assertIn("draw-flowchart", four)
        self.assertNotIn("04-figure-engine", four)



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
        self.assertNotIn("Do not mount ARS", zero)
        self.assertNotIn("academic-pipeline", zero)
        self.assertIn("Do not mount MedSci", zero)
        self.assertIn("orchestrate", zero)
        fast = read("00_orchestrator/references/fast-routing.md")
        self.assertIn("Excel / 批处理 / 0RAD 文件夹 → `02_data-processing`", fast)
        self.assertIn("citation-verify", zero)
        self.assertIn("do not self-certify lit", zero)
        mmd = read("00_orchestrator/runtime-flow.mmd")
        self.assertIn("citation-verify", mmd)
        self.assertIn("claim→ref", mmd)
        self.assertIn("不可跳过", mmd)
        self.assertIn("中途可进", mmd)
        self.assertIn("Lee · 陈述一致", mmd)
        self.assertLess(mmd.index("Lit05"), mmd.index("Gate · 05"))
        self.assertLess(mmd.index("Lit06"), mmd.index("Gate · 06"))
        self.assertIn("不代替 citation-verify", mmd)
        reg = read("01_skill-integration/registry.yaml")
        self.assertIn("citation-verify-on-05-06", reg)
        self.assertIn("status: resolved", reg)

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
        self.assertIn("05-manuscript/vocab/L1/ban-phrases.md", sci)
        wf = read("00_orchestrator/workflows/README.md")
        self.assertIn("gates.md", wf)





class AttributionAndFetch(unittest.TestCase):

    def test_skill_level_prefix_rules(self) -> None:
        style = read("06_review/personal/review.md")
        self.assertIn("[Nature:simulate-reviewers]", style)
        self.assertIn("包内skill-id", style.replace(" ", ""))
        gates = read("00_orchestrator/gates.md")
        self.assertIn("skill-level prefix", gates)
        preset = read("01_skill-integration/references/presets/review-hybrid.yaml")
        self.assertIn("skills: [verify-refs]", preset)
        self.assertIn("skills: [stats-guide]", preset)
        self.assertIn("required: false", preset)
        self.assertIn("skills: [review-critique]", preset)  # self-review; scientific-critical-thinking archived


    def test_author_vs_prefix(self) -> None:
        text = read("06_review/personal/review.md")
        self.assertIn("作者字段", text)
        self.assertIn("作者栏 ≠ 来源标签", text)
        self.assertIn("双标", text)
        self.assertNotIn("[ARS:", text)
        self.assertNotIn("[OpenClaw:", text)
        self.assertIn("[MedSci:", text)
        self.assertIn("[Scientific:", text)
        self.assertIn("同一 DOI", text)
        zero = read("00_orchestrator/SKILL.md")
        self.assertIn("06_review/personal/review.md", zero)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("skill-level prefix", gates)
        five = read("05_manuscript/SKILL.md")
        self.assertIn("New citation numbers", five)

    def test_fetch_merge_helpers(self) -> None:
        fetch = (CAP_ROOT / "fetch.py").read_text(encoding="utf-8")
        self.assertIn("merge_source_state", fetch)
        self.assertIn("Prefer zip", fetch)
        self.assertIn("_state_lock", fetch)
        self.assertIn("via zip", fetch)


class ReviewInteract(unittest.TestCase):
    def test_personal_review_eight_sections(self) -> None:
        text = read("06_review/personal/review.md")
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
        resp = read("07_response/personal/response.md")
        self.assertTrue(len(resp) > 50)

    def test_evidence_request_protocol(self) -> None:
        text = read("05_manuscript/personal/process/evidence.md")
        self.assertIn("Evidence Request", text)
        self.assertIn("Accept", text)
        self.assertIn("Weaken", text)
        self.assertIn("Delete", text)
        self.assertIn("03_research", text)
        self.assertNotIn("B05 = Personal Writing", text)
        skill = read("05_manuscript/SKILL.md")
        self.assertIn("process/evidence.md", skill)
        gates = read("00_orchestrator/gates.md")
        self.assertIn("process/evidence.md", gates)


class MountsCap(unittest.TestCase):
    def test_cache_scaffold(self) -> None:
        self.assertFalse((ROOT / "archive").exists())
        root = CAP_ROOT
        self.assertTrue((root / "README.md").is_file())
        self.assertTrue((root / "INDEX.yaml").is_file())
        self.assertTrue((root / "fetch.py").is_file())
        gi = (CAP_ROOT / ".gitignore").read_text(encoding="utf-8")
        for name in ("b/", "ars/", "medsci/", "scientific/", "openclaw/", "aipoch/", "nature/", "STATE.yaml"):
            self.assertIn(name, gi)
        idx = (CAP_ROOT / "INDEX.yaml").read_text(encoding="utf-8")
        self.assertTrue("on-demand-path-only" in idx or "default-deny" in idx)
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
        one = read("01_skill-integration/SKILL.md")
        self.assertIn("mounts_cap", one)  # alias {mounts_cap} after 0doc move
        self.assertIn("Download is not a mount", one)
        self.assertTrue("bulk-download" in one.lower() or "default deny" in one.lower() or "Non-base" in one)
        fetch = (CAP_ROOT / "fetch.py").read_text(encoding="utf-8")
        self.assertIn("ensure-b", fetch)
        self.assertNotIn("def download_all", fetch)
        self.assertIn("archived:", read("01_skill-integration/SKILL.md"))


class LocalLinkHygiene(unittest.TestCase):
    def test_no_broken_relative_markdown_links(self) -> None:
        errors = []
        skip_parts = {".git", "mounts-cap", "__pycache__", "history"}
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
            "| G-04 | QUALITY |",
            "| G-05 | QUALITY |",
            "| G-06 | QUALITY |",
            "| G-LIT | QUALITY |",
            "| G-CODE | QUALITY |",
        ):
            self.assertIn(row, gates)



if __name__ == "__main__":
    unittest.main()
