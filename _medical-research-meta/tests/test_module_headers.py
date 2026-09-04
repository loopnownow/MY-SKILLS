import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
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
        self.assertFalse((ROOT / "archive").exists(), "empty archive/ stub removed")
        root_dirs = {p.name for p in ROOT.iterdir() if p.is_dir()}
        for expected in SKILL_DIRS:
            self.assertIn(expected, root_dirs)
        self.assertNotIn("01_automation", root_dirs)
        self.assertNotIn("02_imaging", root_dirs)
        self.assertIn("mounts-cap", root_dirs)
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
        self.assertIn("session_mount: ask-each-run", text)
        self.assertIn("05-write-manuscript", text)
        self.assertIn("04-explainability", text)
        self.assertIn("05-humanize", text)
        self.assertNotIn("05-de-ai", text)
        self.assertIn("Imbad0202/academic-research-skills", text)
        self.assertIn("Aperivue/medsci-skills", text)
        self.assertIn("K-Dense-AI/scientific-agent-skills", text)
        self.assertIn("backup-candidate", text)
        self.assertNotIn("role: default-candidate", text)
        self.assertNotIn("mounts: []", text)

    def test_mounts_board(self):
        d = ROOT / "01_skill-discovery-integration"
        md = d / "mounts"
        index = (md / "README.md").read_text(encoding="utf-8")
        b = (md / "b.md").read_text(encoding="utf-8")
        ars = (md / "ars.md").read_text(encoding="utf-8")
        med = (md / "medsci.md").read_text(encoding="utf-8")
        sci = (md / "scientific.md").read_text(encoding="utf-8")
        self.assertFalse((md / "unmapped.html").exists())
        self.assertFalse((md / "mounts.html").exists())
        self.assertFalse((md / "mounts.css").exists())
        leftover_html = list(md.glob("*.html")) + list(md.glob("*.css"))
        self.assertEqual(leftover_html, [])
        self.assertIn("b.md", index)
        self.assertIn("ars.md", index)
        self.assertIn("medsci.md", index)
        self.assertIn("scientific.md", index)
        self.assertIn("05-write-manuscript", b)
        self.assertIn("无空挂", b)
        self.assertIn("23 个空挂", ars)
        self.assertIn("academic-paper/", ars)
        self.assertIn("03-lit-search", ars)
        self.assertIn("deep-research/", ars)
        self.assertIn("02-tables", ars)
        self.assertNotIn("12 / 12 空挂", ars)
        self.assertIn("3 个空挂", med)
        self.assertIn("04-fig-flow", med)
        self.assertIn("02-pictures", med)
        self.assertIn("02-fmri", med)
        self.assertIn("preprocess-imaging", med)
        self.assertIn("analyze-stats", med)
        self.assertNotIn("12 / 12 空挂", med)
        self.assertNotIn("unmapped.html", index)
        self.assertNotIn(".html", index)
        self.assertIn("04-explainability", b)
        self.assertIn("05-humanize", b)
        self.assertIn("04-explainability", med)
        self.assertIn("05-humanize", med)
        self.assertIn("academic-aio", med)
        self.assertIn("9 个空挂", sci)
        self.assertIn("03-lit-fulltext", sci)
        self.assertIn("04-model-eval", sci)
        self.assertIn("06-review-response", sci)
        self.assertIn("02-fmri", sci)
        self.assertIn("02-pictures", sci)
        self.assertIn("03-lit-search", sci)
        self.assertIn("paper-lookup", sci)
        self.assertNotIn("03-literature", sci)
        self.assertIn("skills/xlsx/", sci)
        self.assertIn("02-radiomics-habitat", sci)
        self.assertIn("05-humanize", sci)
        self.assertIn("K-Dense-AI/scientific-agent-skills", sci)
        self.assertFalse((d / "mounts.html").exists())
        self.assertTrue((d / "sources" / "b-my-skills-capabilities.yaml").is_file())
        ars_y = (d / "sources" / "ars.proposed.yaml").read_text(encoding="utf-8")
        med_y = (d / "sources" / "medsci.proposed.yaml").read_text(encoding="utf-8")
        self.assertIn("scan_sha: \"9443623\"", ars_y)
        self.assertIn("path: academic-paper/", ars_y)
        self.assertIn("03-lit-search", ars_y)
        self.assertNotIn("id: 03-literature", ars_y)
        self.assertIn("scan_sha: \"912f7e8\"", med_y)
        self.assertIn("path: skills/make-figures/", med_y)
        self.assertIn("id: 04-fig-plot", med_y)
        self.assertIn("id: 03-lit-fulltext", med_y)
        self.assertIn("fulltext-retrieval", med_y)
        self.assertIn("02-pictures", med_y)
        self.assertIn("02-fmri", med_y)
        self.assertNotIn("empty: []", med_y)
        self.assertIn("id: 03-lit-search", med_y)
        self.assertNotIn("id: 03-literature", med_y)
        self.assertIn("id: 04-explainability", med_y)
        self.assertIn("id: 05-humanize", med_y)
        self.assertIn("skills/explainability/", med_y)
        self.assertIn("skills/humanize/", med_y)
        self.assertIn("kind: expansion", med_y)
        self.assertIn("skills/academic-aio/", med_y)
        self.assertIn("academic-pipeline/", ars_y)
        self.assertIn("04-explainability", ars_y)
        sci_y = (d / "sources" / "scientific-agent-skills.proposed.yaml").read_text(encoding="utf-8")
        self.assertIn("scan_sha: \"1e5eeff\"", sci_y)
        self.assertIn("path: skills/xlsx/", sci_y)
        self.assertIn("03-lit-search", sci_y)
        self.assertIn("paper-lookup", sci_y)
        self.assertNotIn("id: 03-literature", sci_y)
        self.assertIn("02-radiomics-habitat", sci_y)
        self.assertIn("05-humanize", sci_y)
        b_y = (d / "sources" / "b-my-skills-capabilities.yaml").read_text(encoding="utf-8")
        self.assertIn("03-research/lit-search/", b_y)
        self.assertNotIn("03-research/literature/", b_y)
        self.assertIn("05-manuscript/write-venue/", b_y)
        self.assertIn("find-journal", med_y)

    def test_b_mount_paths_unique(self):
        text = (ROOT / "01_skill-discovery-integration" / "registry.yaml").read_text(encoding="utf-8")
        paths = []
        cur_source = None
        for line in text.splitlines():
            if line.strip().startswith("source:"):
                cur_source = line.split(":", 1)[1].strip()
            if line.strip().startswith("path:") and cur_source == "my-skills-capabilities":
                paths.append(line.split(":", 1)[1].strip())
        self.assertEqual(len(paths), len(set(paths)), msg=str(paths))
        self.assertGreaterEqual(len(paths), 28)
        self.assertIn("03-research/lit-search/", paths)
        self.assertIn("02-data-processing/tables/", paths)
        self.assertIn("04-analysis/fig-flow/", paths)
        self.assertNotIn("04-analysis/figure-engine/", paths)
        self.assertNotIn("02-data-processing/imaging/", paths)
        self.assertNotIn("02-data-processing/xlsx/", paths)
        self.assertNotIn("03-research/literature/", paths)

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
