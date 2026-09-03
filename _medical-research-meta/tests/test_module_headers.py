import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "archive"
SKILL_DIRS = (
    "00_orchestrator",
    "01_skill-discovery-integration",
    "02_data-processing",
    "03_research",
    "04_analysis",
    "05_manuscript",
    "06_review",
    "skill-harvest",
)


class ModuleHeaderTests(unittest.TestCase):
    def test_layout_core_and_archive(self):
        self.assertFalse((ROOT / "core").exists(), "core/ must be lifted to repo root")
        self.assertTrue((ROOT / "archive").is_dir())
        root_dirs = {p.name for p in ROOT.iterdir() if p.is_dir()}
        for expected in SKILL_DIRS:
            self.assertIn(expected, root_dirs)
        self.assertNotIn("01_automation", root_dirs)
        self.assertNotIn("02_imaging", root_dirs)
        archive_skill_dirs = {p.name for p in ARCHIVE.iterdir() if p.is_dir()}
        for former in (
            "ethics-application-forms",
            "code-refactoring",
            "clinical-data-extraction",
            "clinical-translation",
        ):
            self.assertNotIn(former, archive_skill_dirs)
            self.assertFalse((ARCHIVE / former / "SKILL.md").is_file())
        self.assertTrue((ROOT / "archive" / "README.md").is_file())
        self.assertTrue((ROOT / "02_data-processing" / "clinical-data-extraction" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "02_data-processing" / "code-refactoring" / "SKILL.md").is_file())
        self.assertFalse((ROOT / "02_data-processing" / "ethics-application-forms" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "03_research" / "ethics-application-forms" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "03_research" / "clinical-translation" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "01_skill-discovery-integration" / "SKILL.md").is_file())
        self.assertTrue((ROOT / "01_skill-discovery-integration" / "registry.yaml").is_file())
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

    def test_core_max_four_path_parts(self):
        """skill / category-or-pack / (scripts|references|personal) / file — no fifth folder."""
        violations = []
        for skill in SKILL_DIRS:
            base = ROOT / skill
            for p in base.rglob("*"):
                if not p.is_file():
                    continue
                if "__pycache__" in p.parts or ".git" in p.parts:
                    continue
                rel = p.relative_to(ROOT)
                if len(rel.parts) > 4:
                    violations.append((len(rel.parts), str(rel)))
        self.assertEqual(violations, [], msg=str(violations))

    def test_registry_default_is_b(self):
        text = (ROOT / "01_skill-discovery-integration" / "registry.yaml").read_text(encoding="utf-8")
        self.assertIn("my-skills-capabilities", text)
        self.assertIn("default-mount", text)
        self.assertIn("notify-then-research-confirm", text)
        self.assertIn("05-writing-generic", text)
        self.assertIn("04-explainability", text)
        self.assertIn("05-humanize", text)
        self.assertNotIn("05-de-ai", text)
        self.assertIn("Imbad0202/academic-research-skills", text)
        self.assertIn("Aperivue/medsci-skills", text)
        self.assertIn("backup-candidate", text)
        self.assertNotIn("role: default-candidate", text)
        self.assertNotIn("mounts: []", text)

    def test_mounts_html_board(self):
        d = ROOT / "01_skill-discovery-integration"
        md = d / "mounts"
        index = (md / "mounts.html").read_text(encoding="utf-8")
        b = (md / "mounts-b.html").read_text(encoding="utf-8")
        ars = (md / "mounts-ars.html").read_text(encoding="utf-8")
        med = (md / "mounts-medsci.html").read_text(encoding="utf-8")
        self.assertFalse((md / "unmapped.html").exists())
        self.assertIn("mounts-b.html", index)
        self.assertIn("mounts-ars.html", index)
        self.assertIn("mounts-medsci.html", index)
        self.assertIn("05-writing-generic", b)
        self.assertIn("无空挂", b)
        self.assertIn("10 个空挂", ars)
        self.assertIn("academic-paper/", ars)
        self.assertIn("deep-research/", ars)
        self.assertIn("02-xlsx", ars)
        self.assertNotIn("12 / 12 空挂", ars)
        self.assertIn("无空挂", med)
        self.assertIn("preprocess-imaging", med)
        self.assertIn("analyze-stats", med)
        self.assertNotIn("12 / 12 空挂", med)
        self.assertNotIn("unmapped.html", index)
        self.assertIn("04-explainability", b)
        self.assertIn("05-humanize", b)
        self.assertIn("04-explainability", med)
        self.assertIn("05-humanize", med)
        self.assertIn("academic-aio", med)
        self.assertNotIn("skills/explainability/</code></td><td>影像模型可解释性（Grad-CAM 等）</td><td>新 04 接口", med)
        self.assertTrue((md / "mounts.css").is_file())
        self.assertFalse((d / "mounts.html").exists())
        self.assertTrue((d / "sources" / "b-my-skills-capabilities.yaml").is_file())
        ars_y = (d / "sources" / "ars.proposed.yaml").read_text(encoding="utf-8")
        med_y = (d / "sources" / "medsci.proposed.yaml").read_text(encoding="utf-8")
        self.assertIn("scan_sha: \"9443623\"", ars_y)
        self.assertIn("path: academic-paper/", ars_y)
        self.assertIn("scan_sha: \"912f7e8\"", med_y)
        self.assertIn("path: skills/make-figures/", med_y)
        self.assertIn("empty: []", med_y)
        self.assertIn("id: 04-explainability", med_y)
        self.assertIn("id: 05-humanize", med_y)
        self.assertIn("skills/explainability/", med_y)
        self.assertIn("skills/humanize/", med_y)
        self.assertIn("kind: expansion", med_y)
        self.assertIn("skills/academic-aio/", med_y)
        self.assertIn("academic-pipeline/", ars_y)
        self.assertIn("04-explainability", ars_y)

    def test_personal_radiology_stats_stays_in_a(self):
        rs = ROOT / "04_analysis" / "personal"
        self.assertTrue((rs / "MODULE.md").is_file())
        self.assertTrue((rs / "diagnostic-accuracy.md").is_file())
        self.assertTrue((rs / "0rad-pipeline-rules.md").is_file())
        self.assertGreaterEqual(len(list(rs.glob("*.md"))), 11)

    def test_no_legacy_manuscript_paths(self):
        skip_names = {
            "INTEGRATION_MAP.md",
            "EXTERNALIZATION_CANDIDATES.md",
            "MOUNTED_SKILLS.md",
            "VERSION.txt",
        }
        for p in ROOT.rglob("*.md"):
            if "__pycache__" in p.parts or ".git" in p.parts:
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
