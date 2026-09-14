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
        self.assertIn("session_pick_unit: fine_id", text)
        self.assertIn("write-paper", text)
        self.assertIn("humanize", text)
        self.assertIn("make-figures", text)
        self.assertIn("ARCHIVED", text)
        self.assertIn("04-explainability", text)  # archived entry
        self.assertNotIn("05-de-ai", text)
        self.assertIn("Imbad0202/academic-research-skills", text)
        self.assertIn("Aperivue/medsci-skills", text)
        self.assertIn("K-Dense-AI/scientific-agent-skills", text)
        self.assertIn("FreedomIntelligence/OpenClaw-Medical-Skills", text)
        self.assertIn("backup-candidate", text)
        self.assertIn("never-mount-as-atomic-source", text)
        self.assertNotIn("role: default-candidate", text)
        self.assertNotIn("mounts: []", text)
        self.assertTrue((ROOT / "01_skill-discovery-integration" / "_history" / "registry.v3.30.yaml").is_file())
        self.assertTrue((ROOT / "01_skill-discovery-integration" / "mounts" / "MIGRATION_v3_to_v4.md").is_file())

    def test_mounts_board(self):
        d = ROOT / "01_skill-discovery-integration"
        md = d / "mounts"
        index = (md / "README.md").read_text(encoding="utf-8")
        b = (md / "b.md").read_text(encoding="utf-8")
        ars = (md / "ars.md").read_text(encoding="utf-8")
        med = (md / "medsci.md").read_text(encoding="utf-8")
        sci = (md / "scientific.md").read_text(encoding="utf-8")
        oc = (md / "openclaw.md").read_text(encoding="utf-8")
        ap = (md / "aipoch.md").read_text(encoding="utf-8")
        nat = (md / "nature.md").read_text(encoding="utf-8")
        self.assertFalse((md / "unmapped.html").exists())
        self.assertEqual(list(md.glob("*.html")) + list(md.glob("*.css")), [])
        self.assertIn("b.md", index)
        self.assertIn("MIGRATION_v3_to_v4.md", index)
        self.assertIn("10", index)
        self.assertIn("52", index)
        self.assertIn("presets.md", index)
        self.assertTrue((md / "presets" / "review-hybrid.yaml").is_file())
        yh = (md / "presets" / "review-hybrid.yaml").read_text(encoding="utf-8")
        self.assertIn("skills: [nature-ref-verifier]", yh)
        self.assertIn("2026-09-13.1", yh)
        self.assertIn("verify-refs", yh)
        self.assertIn("openclaw-medical-skills", yh)
        self.assertIn("intake-project", b)
        self.assertIn("无空挂", b)
        self.assertIn("23", ars)
        self.assertIn("academic-paper/", ars)
        self.assertIn("03-lit-search", ars)
        self.assertIn("02-tables", ars)
        self.assertIn("humanize", med)
        self.assertIn("preprocess-imaging", med)
        self.assertIn("analyze-stats", med)
        self.assertIn("ARCHIVED", med)
        self.assertIn("paper-lookup", sci)
        self.assertIn("K-Dense-AI/scientific-agent-skills", sci)
        self.assertIn("skills/xlsx/", sci)
        self.assertIn("禁挂载", oc)
        self.assertIn("never", oc.lower())
        self.assertIn("23 / 30", oc)
        self.assertIn("FreedomIntelligence/OpenClaw-Medical-Skills", oc)
        self.assertIn("aipoch/medical-research-skills", ap)
        self.assertIn("retraction-watcher", ap)
        self.assertIn("Yuan1z0825/nature-skills", nat)
        self.assertIn("需核实", nat)
        self.assertIn("13 / 30", nat)
        self.assertIn("第三方", nat)
        oc_y = (d / "sources" / "openclaw-medical-skills.proposed.yaml").read_text(encoding="utf-8")
        self.assertIn("scan_sha: \"b1f9b6e\"", oc_y)
        ap_y = (d / "sources" / "aipoch-medical-research-skills.proposed.yaml").read_text(encoding="utf-8")
        self.assertIn("status: PROPOSED", ap_y)
        nat_y = (d / "sources" / "nature-skills.proposed.yaml").read_text(encoding="utf-8")
        self.assertIn("status: PROPOSED", nat_y)
        self.assertIn("287ee37", nat_y)
        ars_y = (d / "sources" / "ars.proposed.yaml").read_text(encoding="utf-8")
        med_y = (d / "sources" / "medsci.proposed.yaml").read_text(encoding="utf-8")
        sci_y = (d / "sources" / "scientific-agent-skills.proposed.yaml").read_text(encoding="utf-8")
        b_y = (d / "sources" / "b-my-skills-capabilities.yaml").read_text(encoding="utf-8")
        self.assertIn("scan_sha: \"9443623\"", ars_y)
        self.assertIn("path: academic-paper/", ars_y)
        self.assertIn("scan_sha: \"912f7e8\"", med_y)
        self.assertIn("skills/humanize/", med_y)
        self.assertIn("skills/explainability/", med_y)
        self.assertIn("kind: expansion", med_y)
        self.assertIn("scan_sha: \"1e5eeff\"", sci_y)
        self.assertIn("paper-lookup", sci_y)
        self.assertIn("03-research/lit-cite/", b_y)
        self.assertIn("intake-project", b_y)
        self.assertIn("03-research/intake-project/", b_y)
        self.assertTrue((d / "sources" / "b-my-skills-capabilities.yaml").is_file())

    def test_b_mount_paths_unique(self):
        text = (ROOT / "01_skill-discovery-integration" / "registry.yaml").read_text(encoding="utf-8")
        # Collect B paths that are primary owners (not path_shared)
        paths = []
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
                if cur.get("source") == "my-skills-capabilities" and not cur.get("path_shared"):
                    if cur.get("path"):
                        paths.append(cur["path"])
                cur = {"id": line.split(":", 1)[1].strip()}
            elif ":" in line and line.startswith("    "):
                k, v = line.strip().split(":", 1)
                cur[k.strip()] = v.strip()
        if cur.get("source") == "my-skills-capabilities" and not cur.get("path_shared") and cur.get("path"):
            paths.append(cur["path"])
        self.assertEqual(len(paths), len(set(paths)), msg=str(paths))
        self.assertGreaterEqual(len(paths), 20)
        self.assertIn("04-analysis/fig-flow/", paths)
        self.assertIn("03-research/intake-project/", paths)
        self.assertIn("02-data-processing/tables/", paths)
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
            if "mounts-cap" in p.parts:
                # Third-party pack bytes (gitignored cache / verbatim upstream
                # content). Not A's own docs; their internal filenames (e.g. a
                # Nature template's "01_research_canon.md") can coincidentally
                # contain these substrings without meaning the legacy layout.
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
