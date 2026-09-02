import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "core"
ARCHIVE = ROOT / "archive"


class ModuleHeaderTests(unittest.TestCase):
    def test_layout_core_and_archive(self):
        self.assertTrue((ROOT / "core").is_dir())
        self.assertTrue((ROOT / "archive").is_dir())
        core_names = {p.name for p in CORE.iterdir() if p.is_dir()}
        for expected in (
            "00_orchestrator",
            "01_skill-discovery-integration",
            "02_data-processing",
            "03_research",
            "04_analysis",
            "05_manuscript",
            "06_review",
            "skill-harvest",
        ):
            self.assertIn(expected, core_names)
        self.assertNotIn("01_automation", core_names)
        self.assertNotIn("02_imaging", core_names)
        archive_names = {p.name for p in ARCHIVE.iterdir() if p.is_dir()}
        for expected in (
            "ethics-application-forms",
            "code-refactoring",
            "clinical-data-extraction",
            "clinical-translation",
        ):
            self.assertIn(expected, archive_names)
            self.assertTrue((ARCHIVE / expected / "SKILL.md").is_file())
        self.assertTrue((CORE / "01_skill-discovery-integration" / "SKILL.md").is_file())
        self.assertTrue((CORE / "01_skill-discovery-integration" / "registry.yaml").is_file())
        for banned in ("markitdown", "tool-environment-setup", "imaging-omics-ml"):
            self.assertFalse(any(CORE.rglob(banned)), banned)

    def test_no_forbidden_a_directories(self):
        self.assertFalse((CORE / "01_automation").exists())
        self.assertFalse((CORE / "02_imaging").exists())
        self.assertFalse(any(CORE.rglob("bundles")), "A must not contain bundles/")
        self.assertFalse((CORE / "05_manuscript" / "figure-engine").exists())
        fig = list((CORE / "05_manuscript").rglob("*figure-engine*"))
        self.assertEqual(fig, [])
        self.assertFalse((CORE / "skill-harvest" / "evolution" / "proposals").exists())

    def test_core_max_three_directories(self):
        """core + skill + optional one folder (+ file)."""
        violations = []
        for p in CORE.rglob("*"):
            if not p.is_file():
                continue
            rel = p.relative_to(CORE)
            n_dirs_including_core = 1 + len(rel.parts) - 1  # core + parent dirs of file
            # rel.parts = (skill, [folder], file) → dirs = core + parts[:-1]
            n_dirs = 1 + len(rel.parts[:-1])
            if n_dirs > 3:
                violations.append((n_dirs, str(p.relative_to(ROOT))))
        self.assertEqual(violations, [], msg=str(violations))

    def test_registry_not_mounted(self):
        text = (CORE / "01_skill-discovery-integration" / "registry.yaml").read_text(encoding="utf-8")
        self.assertIn("mounts: []", text)
        self.assertIn("Imbad0202/academic-research-skills", text)
        self.assertIn("Aperivue/medsci-skills", text)
        self.assertIn("PROPOSED", text)
        self.assertIn("default-candidate", text)
        self.assertIn("backup-candidate", text)

    def test_personal_radiology_stats_stays_in_a(self):
        rs = CORE / "04_analysis" / "radiology-stats"
        self.assertTrue((rs / "MODULE.md").is_file())
        self.assertTrue((rs / "diagnostic-accuracy.md").is_file())
        self.assertEqual(len(list(rs.glob("*.md"))), 7)

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
            if "archive" in p.parts:
                continue  # archive not migrated this round
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
