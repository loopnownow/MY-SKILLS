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

    def test_registry_not_mounted(self):
        text = (ROOT / "01_skill-discovery-integration" / "registry.yaml").read_text(encoding="utf-8")
        self.assertIn("mounts: []", text)
        self.assertIn("Imbad0202/academic-research-skills", text)
        self.assertIn("Aperivue/medsci-skills", text)
        self.assertIn("PROPOSED", text)
        self.assertIn("default-candidate", text)
        self.assertIn("backup-candidate", text)

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
