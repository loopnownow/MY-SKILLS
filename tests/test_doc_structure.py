
"""Document layout: pack dirs, headers, registry state, one H1.

Merged from: `test_module_headers.py`, `test_docs_match_registry_state.py`, `test_qc_five_fixes.py`.
"""
from __future__ import annotations

from pathlib import Path
import re
import unittest
import yaml

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

SKILL_DIRS = (
    "00_orchestrator",
    "02_data-processing",
    "03_research",
    "05_manuscript",
    "06_review",
    "07_response",
)
DOCS = ("README.md", "ARCHITECTURE.md")

class ModuleHeaderTests(unittest.TestCase):
    def test_layout_core_and_archive(self):
        self.assertFalse((ROOT / "core").exists(), "core/ must be lifted to repo root")
        self.assertFalse((ROOT / "archive").exists(), "empty archive/ stub removed")
        root_dirs = {p.name for p in ROOT.iterdir() if p.is_dir()}
        for expected in SKILL_DIRS:
            self.assertIn(expected, root_dirs)
        self.assertNotIn("skill-harvest", root_dirs)
        self.assertNotIn("01_automation", root_dirs)
        self.assertNotIn("02_imaging", root_dirs)
        self.assertTrue((ROOT / "02_data-processing" / "personal" / "extract.md").is_file())
        self.assertTrue((ROOT / "02_data-processing" / "personal" / "coding.md").is_file())
        self.assertFalse((ROOT / "02_data-processing" / "personal" / "coding-qc.md").is_file())
        self.assertFalse((ROOT / "02_data-processing" / "personal" / "workspace.md").is_file())
        self.assertTrue((ROOT / "02_data-processing" / "qc" / "coding-qc.md").is_file())
        self.assertFalse((ROOT / "02_data-processing" / "fill-protocol" / "SKILL.md").is_file())
        # A stub removed 2026-10-17; body lives in B
        self.assertFalse((ROOT / "03_research" / "fill-protocol" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "03_research" / "personal" / "fill-protocol" / "README.md").is_file())
        self.assertTrue((ROOT / "03_research" / "personal" / "clinical-translation").is_dir())
        self.assertTrue((ROOT / "00_orchestrator" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "00_orchestrator" / "registry.yaml").is_file())
        for banned in ("markitdown", "tool-environment-setup", "imaging-omics-ml"):
            self.assertFalse(any(ROOT.rglob(banned)), banned)

    def test_no_forbidden_a_directories(self):
        self.assertFalse((ROOT / "01_automation").exists())
        self.assertFalse((ROOT / "02_imaging").exists())
        self.assertFalse((ROOT / "core").exists())
        self.assertFalse(any(p for p in ROOT.rglob("bundles") if ".git" not in p.parts), "A must not contain bundles/")
        self.assertFalse((ROOT / "05_manuscript" / "figure-engine").exists())
        fig = [p for p in (ROOT / "05_manuscript").rglob("*figure-engine*") if ".git" not in p.parts]
        self.assertEqual(fig, [])
        self.assertFalse((ROOT / "skill-harvest" / "evolution" / "proposals").exists())
        self.assertFalse((ROOT / "05_manuscript" / "writing-generic").exists())
        self.assertFalse((ROOT / "05_manuscript" / "de-ai").exists())
        self.assertFalse((ROOT / "06_review" / "review-generic").exists())
        self.assertFalse((ROOT / "04_analysis").exists(), "04_analysis retired into 02_data-processing")

    def test_core_max_five_path_parts(self):
        """skill / category-or-pack / (scripts|references|personal) / optional-leaf / file — max five parts."""
        violations = []
        for skill in SKILL_DIRS:
            base = ROOT / skill
            for p in base.rglob("*"):
                if not p.is_file():
                    continue
                if "__pycache__" in p.parts or ".git" in p.parts:
                    continue
                rel = p.relative_to(ROOT)
                # Annual journal datasets lived under A find-journal/data; stub removed — pools in 0doc / B
                parts = rel.parts
                data_year_ok = (
                    len(parts) == 5
                    and parts[0] == "03_research"
                    and parts[1] == "find-journal"
                    and parts[2] == "data"
                    and parts[3].isdigit()
                    and len(parts[3]) == 4
                )
                # 2026-10-17: domain bodies under NN_slug/base/ may nest deeper than five parts.
                base_pilot_ok = len(parts) >= 2 and parts[1] == "base"
                if len(rel.parts) > 5 and not data_year_ok and not base_pilot_ok:
                    violations.append((len(rel.parts), str(rel)))
        self.assertEqual(violations, [], msg=str(violations))

    def test_registry_is_in_repo_index(self):
        text = (ROOT / "00_orchestrator" / "registry.yaml").read_text(encoding="utf-8")
        self.assertNotIn("default_source:", text)
        self.assertIn("source: my-skills", text)
        self.assertIn("notify-then-research-confirm", text)
        self.assertIn("session_fine_id_pick: ask-each-run", text)
        self.assertIn("session_pick_unit: fine_id", text)
        self.assertIn("write-paper", text)
        self.assertIn("humanize", text)
        self.assertIn("draw-flowchart", text)
        self.assertNotIn("04-explainability", text)
        self.assertNotIn("05-de-ai", text)
        self.assertNotIn("Imbad0202/academic-research-skills", text)
        self.assertNotIn("role: default-candidate", text)
        self.assertNotIn("fine_ids: []", text)
        self.assertNotIn("\narchived:\n", text)
        self.assertFalse((ROOT / "00_orchestrator" / "_history").exists())
        self.assertFalse((ROOT / "00_orchestrator" / "fine_ids").exists())
        self.assertFalse((ROOT / "00_orchestrator" / "references" / "MIGRATION_v3_to_v4.md").exists())

    def test_fine_ids_board(self):
        """00 keeps registry/index/workflows — no fine_id-package board under fine_ids/."""
        d = ROOT / "00_orchestrator"
        refs = d / "references"
        skill = (d / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: medical-research-orchestrator", skill)
        self.assertIn("my-skills", skill)
        self.assertIn("NN_slug/base", skill)
        self.assertIn("routing index", skill.lower())
        self.assertNotIn("`fine_ids/`", skill)
        # 2026-10-25: the 01 index seat merged here; registry / aliases / workflows live under 00.
        self.assertTrue((d / "registry.yaml").is_file())
        self.assertTrue((d / "legacy_aliases.yaml").is_file())
        self.assertTrue((d / "workflows" / "README.md").is_file())
        self.assertFalse((ROOT / "01_skill-integration").exists())
        self.assertFalse((d / "fine_ids").exists())
        self.assertFalse((d / "sources").exists())
        self.assertFalse((d / "fine_ids" / "MIGRATION_v3_to_v4.md").exists())
        # No separate capability-pack source yaml; bodies in-repo under NN_slug/base/.
        self.assertFalse((d / "sources" / "b-my-skills-base.yaml").exists())
        self.assertFalse((refs / "presets").exists())
        self.assertFalse((d / "MOUNTED_SKILLS.md").exists())


    def test_b_fine_id_paths_unique(self):
        import yaml
        reg = yaml.safe_load(
            (ROOT / "00_orchestrator" / "registry.yaml").read_text(encoding="utf-8")
        )
        a_paths = []
        b_paths = []
        for m in reg.get("fine_ids") or []:
            if m.get("path_shared"):
                continue
            path = m.get("path")
            if not path:
                continue
            if m.get("source") == "my-skills-base":
                b_paths.append(path)
            elif m.get("source") == "my-skills":
                a_paths.append(path)
        # Domains 02–07 in-repo: no my-skills-base primary paths.
        self.assertEqual(b_paths, [], msg=str(b_paths))
        self.assertEqual(len(a_paths), len(set(a_paths)), msg=str(a_paths))
        self.assertGreaterEqual(len(a_paths), 20)
        self.assertIn("02_data-processing/base/draw-flowchart/", a_paths)
        self.assertIn("03_research/base/design-study/", a_paths)
        self.assertIn("02_data-processing/base/clean-data/", a_paths)
        self.assertIn("02_data-processing/base/stats-analysis/", a_paths)
        self.assertIn("05_manuscript/base/write-paper/", a_paths)
        self.assertIn("06_review/base/self-review/", a_paths)
        self.assertIn("07_response/base/revise/", a_paths)
        self.assertNotIn("04-analysis/figure-engine/", a_paths)
        self.assertNotIn("02-data-processing/tables/", a_paths)
        self.assertNotIn("03-research/literature/", a_paths)

    def test_personal_radiology_stats_stays_in_a(self):
        rs = ROOT / "02_data-processing" / "personal" / "analysis"
        self.assertTrue((rs / "module-notes.md").is_file())  # MODULE.md → module-notes.md
        self.assertTrue((rs / "methods.md").is_file())  # diagnostic-accuracy merged into methods.md
        self.assertTrue((rs / "pipeline.md").is_file())
        self.assertGreaterEqual(len(list(rs.glob("*.md"))), 8)

    def test_no_legacy_manuscript_paths(self):
        skip_names = {
            "INTEGRATION_MAP.md",
            "INTEGRATION_MAP.archive.md",
            "MOUNTED_SKILLS.md",
            "VERSION.txt",
        }
        for p in ROOT.rglob("*.md"):
            if "__pycache__" in p.parts or ".git" in p.parts:
                continue
            if "history" in p.parts:
                # Third-party pack bytes / monthly INTEGRATION_MAP archives.
                # Historical CHG text may mention retired path fragments.
                continue
            if p.name in skip_names:
                continue
            text = p.read_text(encoding="utf-8")
            self.assertNotIn("04_writing", text)
            self.assertNotIn("bundles/matplotlib", text)
            self.assertNotIn("01_research", text, p.as_posix())
            self.assertNotIn("02_analysis", text, p.as_posix())
            self.assertNotIn("03_imaging", text, p.as_posix())
            self.assertNotIn("04_manuscript", text, p.as_posix())
            self.assertNotIn("05_automation", text, p.as_posix())
            self.assertNotIn("01_automation", text, p.as_posix())
            self.assertNotIn("02_imaging", text, p.as_posix())
class DocsMatchRegistry(unittest.TestCase):
    def setUp(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        self.fine_ids = [m for m in (reg.get("fine_ids") or []) if isinstance(m, dict)]
        self.proposed = [m for m in self.fine_ids if m.get("status") == "PROPOSED"]

    def test_no_stale_proposed_claim(self) -> None:
        if self.proposed:
            self.skipTest("registry currently has PROPOSED rows")
        for name in DOCS:
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertNotRegex(
                text,
                r"PROPOSED\s*/\s*LIVE",
                f"{name} still claims non-default ids are mixed PROPOSED/LIVE "
                "while the registry has no PROPOSED row",
            )

    def test_live_paths_are_canonical(self) -> None:
        missing: list[str] = []
        for m in self.fine_ids:
            if m.get("status") != "LIVE":
                continue
            path = str(m.get("path") or "")
            if not path:
                missing.append(f"{m.get('id')}: no path")
                continue
            if not (ROOT / path).exists():
                missing.append(f"{m.get('id')}: {path}")
        self.assertEqual(missing, [], "LIVE paths missing:\n" + "\n".join(missing))

    def test_no_archived_section(self) -> None:
        reg = yaml.safe_load((ONE / "registry.yaml").read_text(encoding="utf-8")) or {}
        self.assertNotIn("archived", reg, "registry must not carry archived: bloat")
        self.assertFalse(reg.get("archived"), "archived must be empty/absent")
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


QC_DIRS = (
    "00_orchestrator/qc",
    "02_data-processing/qc",
    "03_research/qc",
    "05_manuscript/qc",
    "06_review/qc",
    "07_response/qc",
)
ROUTE = ROOT / "03_research" / "personal" / "route.md"
PERSONAL = ROOT / "03_research" / "personal"
FENCE_LINE = re.compile(r"^\s*(```|~~~)")
H1_LINE = re.compile(r"^# [^#]")


def h1_lines(path: Path) -> list[tuple[int, str]]:
    """Level-1 headings, ignoring frontmatter, fenced code and indented lines."""
    lines = path.read_text(encoding="utf-8-sig", errors="ignore").splitlines()
    start, in_fence = 0, False
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                start = idx + 1
                break
    found: list[tuple[int, str]] = []
    for idx in range(start, len(lines)):
        line = lines[idx]
        if FENCE_LINE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and H1_LINE.match(line):
            found.append((idx + 1, line.strip()))
    return found


class SingleHeading(unittest.TestCase):
    def test_every_markdown_file_has_exactly_one_h1(self) -> None:
        problems: list[str] = []
        for path in sorted(ROOT.rglob("*.md")):
            if set(path.parts) & {".git", "__pycache__", ".pytest_cache", "fixtures"}:
                continue
            found = h1_lines(path)
            if len(found) != 1:
                rel = path.relative_to(ROOT).as_posix()
                detail = "; ".join(f"L{no}:{text[:50]}" for no, text in found) or "no H1"
                problems.append(f"{rel}: H1={len(found)} :: {detail}")
        self.assertEqual(
            problems, [],
            "one H1 per file (demote sections, drop frontmatter residue):\n"
            + "\n".join(problems[:30]),
        )


class IndexCompleteness(unittest.TestCase):
    def test_qc_readme_lists_every_standard(self) -> None:
        problems: list[str] = []
        for rel in QC_DIRS:
            folder = ROOT / rel
            if not folder.is_dir():
                continue
            readme = folder / "README.md"
            if not readme.is_file():
                problems.append(f"{rel}: no README.md")
                continue
            text = readme.read_text(encoding="utf-8")
            for path in sorted(folder.glob("*.md")):
                if path.name != "README.md" and path.name not in text:
                    problems.append(f"{rel}: {path.name} missing from README.md")
            for name in re.findall(r"`([a-z0-9._-]+\.md)`", text):
                if name != "README.md" and not (folder / name).is_file():
                    problems.append(f"{rel}: README.md points at absent {name}")
        self.assertEqual(problems, [], "qc README ↔ folder drift:\n" + "\n".join(problems[:30]))

    def test_route_lists_every_personal_page(self) -> None:
        text = ROUTE.read_text(encoding="utf-8")
        missing = [
            path.name for path in sorted(PERSONAL.glob("*.md"))
            if path.name not in {"route.md"} and path.name not in text
        ]
        self.assertEqual(
            missing, [],
            "03_research/personal pages absent from route.md: " + ", ".join(missing),
        )
