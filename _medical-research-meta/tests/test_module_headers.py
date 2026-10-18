import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SKILL_DIRS = (
    "00_orchestrator",
    "01_skill-integration",
    "02_data-processing",
    "03_research",
    "04_analysis",
    "05_manuscript",
    "06_review",
    "07_response",
)


class ModuleHeaderTests(unittest.TestCase):
    def test_layout_core_and_archive(self):
        self.assertFalse((ROOT / "core").exists(), "core/ must be lifted to repo root")
        self.assertFalse((ROOT / "archive").exists(), "empty archive/ stub removed")
        root_dirs = {p.name for p in ROOT.iterdir() if p.is_dir()}
        for expected in SKILL_DIRS:
            self.assertIn(expected, root_dirs)
        self.assertNotIn("skill-harvest", root_dirs)  # archived 2026-10-17 → D:\\0del\\...
        self.assertNotIn("01_automation", root_dirs)
        self.assertNotIn("02_imaging", root_dirs)
        self.assertNotIn("mounts-cap", root_dirs)  # cache moved to 0doc 04-lab-reference/mounts-cap
        self.assertTrue((ROOT / "02_data-processing" / "personal" / "extract.md").is_file())
        self.assertTrue((ROOT / "02_data-processing" / "personal" / "coding.md").is_file())
        self.assertTrue((ROOT / "02_data-processing" / "personal" / "coding-qc.md").is_file())
        self.assertFalse((ROOT / "02_data-processing" / "fill-protocol" / "SKILL.md").is_file())
        # A stub removed 2026-10-17; body lives in B
        self.assertFalse((ROOT / "03_research" / "fill-protocol" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "03_research" / "personal" / "fill-protocol" / "README.md").is_file())
        self.assertTrue((ROOT / "03_research" / "personal" / "clinical-translation").is_dir())
        self.assertTrue((ROOT / "01_skill-integration" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "01_skill-integration" / "registry.yaml").is_file())
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
        self.assertFalse((ROOT / "04_analysis" / "radiology-stats").exists())

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

    def test_registry_default_is_b(self):
        text = (ROOT / "01_skill-integration" / "registry.yaml").read_text(encoding="utf-8")
        self.assertIn("my-skills-base", text)
        self.assertIn("default-mount", text)
        self.assertIn("notify-then-research-confirm", text)
        self.assertIn("session_mount: ask-each-run", text)
        self.assertIn("session_pick_unit: fine_id", text)
        self.assertIn("write-paper", text)
        self.assertIn("humanize", text)
        self.assertIn("draw-flowchart", text)
        self.assertIn("ARCHIVED", text)
        self.assertIn("paperclip", text)  # archived entry
        self.assertNotIn("04-explainability", text)  # v3 archived record removed
        self.assertNotIn("05-de-ai", text)
        self.assertNotIn("Imbad0202/academic-research-skills", text)
        self.assertNotIn("FreedomIntelligence/OpenClaw-Medical-Skills", text)
        self.assertIn("ars_openclaw_policy: removed-from-catalog", text)
        self.assertNotIn("openclaw_policy: never-mount-as-atomic-source", text)
        self.assertNotIn("role: default-candidate", text)
        self.assertNotIn("mounts: []", text)
        self.assertTrue("default deny" in text.lower() or "UNIQUE" in text)
        self.assertFalse((ROOT / "01_skill-integration" / "_history").exists())
        self.assertFalse((ROOT / "01_skill-integration" / "mounts").exists())
        self.assertFalse((ROOT / "01_skill-integration" / "references" / "MIGRATION_v3_to_v4.md").exists())

    def test_mounts_board(self):
        """01 keeps registry/index only — no mount-package board under mounts/."""
        d = ROOT / "01_skill-integration"
        refs = d / "references"
        skill = (d / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("name: skill-index", skill)
        self.assertIn("my-skills-base", skill)
        self.assertIn("references/hybrid-mount-pointers.md", skill)
        self.assertIn("references/presets", skill)
        self.assertNotIn("`mounts/`", skill)
        self.assertFalse((d / "mounts").exists())
        hybrid = (refs / "hybrid-mount-pointers.md").read_text(encoding="utf-8")
        self.assertIn("default deny", hybrid.lower())
        self.assertIn("registry/index only", hybrid.lower())
        # dead source yamls stay archived / absent
        self.assertFalse((d / "sources" / "ars.proposed.yaml").exists())
        self.assertFalse((d / "sources" / "openclaw-medical-skills.proposed.yaml").exists())
        self.assertFalse((d / "sources" / "medsci.proposed.yaml").exists())
        self.assertFalse((d / "sources" / "nature-skills.proposed.yaml").exists())
        self.assertFalse((d / "sources" / "scientific-agent-skills.proposed.yaml").exists())
        self.assertFalse((d / "sources" / "aipoch-medical-research-skills.proposed.yaml").exists())
        self.assertFalse((d / "mounts" / "MIGRATION_v3_to_v4.md").exists())
        preset = refs / "presets" / "review-hybrid.yaml"
        self.assertTrue(preset.is_file())
        yh = preset.read_text(encoding="utf-8")
        self.assertIn("skills: [verify-refs]", yh)
        self.assertIn("skills: [stats-guide]", yh)
        self.assertIn("verify-refs", yh)
        self.assertIn("my-skills-base", yh)
        self.assertNotIn("openclaw-medical-skills", yh)
        self.assertNotIn("academic-research-skills", yh)
        reg_text = (d / "registry.yaml").read_text(encoding="utf-8")
        self.assertIn("references/hybrid-mount-pointers.md", reg_text)
        self.assertIn("removed-from-catalog", reg_text)
        b_y = (d / "sources" / "b-my-skills-base.yaml").read_text(encoding="utf-8")
        # Domains 02–07 bodies in-repo (source my-skills); B source yaml skills empty.
        self.assertIn("skills: []", b_y)
        self.assertNotIn("03-research/lit-search/", b_y)
        self.assertNotIn("id: verify-refs", b_y)
        self.assertTrue((d / "sources" / "b-my-skills-base.yaml").is_file())
        self.assertNotIn("mounts/README.md", b_y)


    def test_b_mount_paths_unique(self):
        text = (ROOT / "01_skill-integration" / "registry.yaml").read_text(encoding="utf-8")
        # Collect primary-owner paths (not path_shared) for live sources.
        b_paths = []
        a_paths = []
        cur = {}
        in_mounts = False
        for line in text.splitlines():
            if line.startswith("mounts:"):
                in_mounts = True
                continue
            if in_mounts and line.startswith("reference_only:"):
                break
            if not in_mounts:
                continue
            if line.startswith("  - id:"):
                if cur.get("path") and not cur.get("path_shared"):
                    if cur.get("source") == "my-skills-base":
                        b_paths.append(cur["path"])
                    elif cur.get("source") == "my-skills":
                        a_paths.append(cur["path"])
                cur = {"id": line.split(":", 1)[1].strip()}
            elif ":" in line and line.startswith("    "):
                k, v = line.strip().split(":", 1)
                cur[k.strip()] = v.strip()
        if cur.get("path") and not cur.get("path_shared"):
            if cur.get("source") == "my-skills-base":
                b_paths.append(cur["path"])
            elif cur.get("source") == "my-skills":
                a_paths.append(cur["path"])
        # Domains 02–07 moved in-repo: no remaining my-skills-base primary paths.
        self.assertEqual(b_paths, [], msg=str(b_paths))
        self.assertEqual(len(a_paths), len(set(a_paths)), msg=str(a_paths))
        self.assertGreaterEqual(len(a_paths), 20)
        self.assertIn("04_analysis/base/fig-flow/", a_paths)
        self.assertIn("03_research/base/design-experiment/", a_paths)
        self.assertIn("02_data-processing/base/tables/", a_paths)
        self.assertIn("04_analysis/base/stats-guide/", a_paths)
        self.assertIn("05_manuscript/base/write-manuscript/", a_paths)
        self.assertIn("06_review/base/review-critique/", a_paths)
        self.assertIn("07_response/base/review-response/", a_paths)
        self.assertNotIn("04-analysis/figure-engine/", a_paths)
        self.assertNotIn("02-data-processing/tables/", a_paths)
        self.assertNotIn("03-research/literature/", a_paths)

    def test_personal_radiology_stats_stays_in_a(self):
        rs = ROOT / "04_analysis" / "personal"
        self.assertTrue((rs / "module-notes.md").is_file())  # MODULE.md → module-notes.md
        self.assertTrue((rs / "methods.md").is_file())  # diagnostic-accuracy merged into methods.md
        self.assertTrue((rs / "pipeline.md").is_file())
        self.assertGreaterEqual(len(list(rs.glob("*.md"))), 8)

    def test_no_legacy_manuscript_paths(self):
        skip_names = {
            "INTEGRATION_MAP.md",
            "INTEGRATION_MAP.archive.md",
            "EXTERNALIZATION_CANDIDATES.md",
            "MOUNTED_SKILLS.md",
            "VERSION.txt",
        }
        for p in ROOT.rglob("*.md"):
            if "__pycache__" in p.parts or ".git" in p.parts:
                continue
            if "mounts-cap" in p.parts or "history" in p.parts:
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


if __name__ == "__main__":
    unittest.main()
