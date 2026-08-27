import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
CORE = ROOT / "core"
ARCHIVE = ROOT / "archive"
class ModuleHeaderTests(unittest.TestCase):
    def test_expected_module_count(self):
        mods=list(CORE.glob("*/bundles/*/MODULE.md"))
        self.assertGreaterEqual(len(mods), 9)
    def test_manuscript_has_two_execution_bundles(self):
        names={p.parent.name for p in (CORE/"05_manuscript"/"bundles").glob("*/MODULE.md")}
        self.assertEqual(names,{"manuscript-core","figure-engine"})
    def test_review_has_quality_bundle(self):
        names={p.parent.name for p in (CORE/"06_review"/"bundles").glob("*/MODULE.md")}
        self.assertEqual(names,{"manuscript-quality"})
    def test_analysis_keeps_impute_nested(self):
        names={p.parent.name for p in (CORE/"04_analysis"/"bundles").glob("*/MODULE.md")}
        self.assertIn("data-impute", names)
    def test_layout_core_and_archive(self):
        self.assertTrue((ROOT/"core").is_dir())
        self.assertTrue((ROOT/"archive").is_dir())
        core_names={p.name for p in CORE.iterdir() if p.is_dir()}
        for expected in (
            "00_orchestrator","01_automation","02_imaging","03_research",
            "04_analysis","05_manuscript","06_review","skill-harvest",
        ):
            self.assertIn(expected, core_names)
        archive_names={p.name for p in ARCHIVE.iterdir() if p.is_dir()}
        for expected in (
            "ethics-application-forms","code-refactoring",
            "clinical-data-extraction","clinical-translation",
        ):
            self.assertIn(expected, archive_names)
            self.assertTrue((ARCHIVE/expected/"SKILL.md").is_file())
        auto_bundles={p.name for p in (CORE/"01_automation"/"bundles").iterdir() if p.is_dir()}
        self.assertEqual(auto_bundles, {"xlsx"})
        img_bundles={p.name for p in (CORE/"02_imaging"/"bundles").iterdir() if p.is_dir()}
        self.assertEqual(img_bundles, {"imaging-preprocessing-qc","radiomics-habitat"})
        for banned in ("markitdown","tool-environment-setup","imaging-omics-ml"):
            self.assertFalse(any(CORE.rglob(banned)), banned)
    def test_no_legacy_manuscript_paths(self):
        skip={ROOT/"_medical-research-meta"/"INTEGRATION_MAP.md"}
        for p in ROOT.rglob("*.md"):
            if p in skip:
                continue
            text=p.read_text(encoding="utf-8")
            self.assertNotIn("04_writing",text)
            self.assertNotIn("bundles/matplotlib",text)
            self.assertNotIn("01_research",text, p.as_posix())
            self.assertNotIn("02_analysis",text, p.as_posix())
            self.assertNotIn("03_imaging",text, p.as_posix())
            self.assertNotIn("04_manuscript",text, p.as_posix())
            self.assertNotIn("05_automation",text, p.as_posix())
if __name__=="__main__": unittest.main()
