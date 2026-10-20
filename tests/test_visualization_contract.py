"""Visualization architecture v1.0: contract, IR shape, mount policy; 07_response allowed."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "04_analysis" / "personal" / "visualization" / "scripts" / "gen_visualization.py"
VIZ_OUT = Path(r"D:/0Grok/0doc/04-lab-reference/my-skills-viz")
FORBIDDEN_FACT_SOURCES = (
    "LLM inference",
    "generated HTML",
    "previous generated HTML",
    "arbitrary mounted-file crawling",
    "filename alone",
    "visual appearance",
    "unvalidated JSON",
)


def load_generator():
    spec = importlib.util.spec_from_file_location("gen_visualization", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class VisualizationContract(unittest.TestCase):
    def test_contract_files_exist(self) -> None:
        for rel in (
            "04_analysis/personal/visualization/visualization-architecture.md",
            "04_analysis/personal/visualization/archify-version.yaml",
            "04_analysis/personal/visualization/visualization-source-contract.yaml",
            "04_analysis/personal/visualization/scripts/gen_visualization.py",
            # ".github/workflows/visualization.yml",  # archived with .github/ 2026-10-17 to 0del
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_version_record_pins_archify(self) -> None:
        record = yaml.safe_load((ROOT / "04_analysis" / "personal" / "visualization" / "archify-version.yaml").read_text(encoding="utf-8"))
        self.assertEqual(record["source"], "tt-a1i/archify")
        self.assertEqual(record["expected_version"], "3.0.1")
        self.assertEqual(record["update_policy"], "check")
        self.assertIs(record["auto_update"], False)
        self.assertIs(record["visualization_only"], True)
        self.assertEqual(record["schema_pins"]["architecture"]["schema_version"], 1)
        self.assertEqual(record["schema_pins"]["workflow"]["schema_version"], 2)

    def test_forbidden_fact_sources_are_listed(self) -> None:
        text = (ROOT / "04_analysis" / "personal" / "visualization" / "visualization-source-contract.yaml").read_text(encoding="utf-8")
        for phrase in FORBIDDEN_FACT_SOURCES:
            self.assertIn(phrase, text)

    def test_ir_json_parses_and_matches_pins(self) -> None:
        record = yaml.safe_load((ROOT / "04_analysis" / "personal" / "visualization" / "archify-version.yaml").read_text(encoding="utf-8"))
        arch = json.loads((VIZ_OUT / "architecture/architecture.json").read_text(encoding="utf-8"))
        wf = json.loads((VIZ_OUT / "workflow/runtime.workflow.json").read_text(encoding="utf-8"))
        self.assertEqual(arch["diagram_type"], "architecture")
        self.assertEqual(wf["diagram_type"], "workflow")
        self.assertEqual(arch["schema_version"], record["schema_pins"]["architecture"]["schema_version"])
        self.assertEqual(wf["schema_version"], record["schema_pins"]["workflow"]["schema_version"])
        for key in ("components", "boundaries", "connections"):
            self.assertIn(key, arch)
        for key in ("lanes", "phases", "groups", "mainPath", "nodes", "edges"):
            self.assertIn(key, wf)
        self.assertGreaterEqual(len(arch["components"]), 6)
        self.assertLessEqual(len(arch["components"]), 12)
        node_ids = {node["id"] for node in wf["nodes"]}
        self.assertIn("lit05", node_ids)
        self.assertIn("lit06", node_ids)
        labels = " ".join(edge.get("label", "") for edge in wf["edges"])
        self.assertIn("mid-entry", labels)
        self.assertTrue((VIZ_OUT / "index.html").is_file())
        module = load_generator()
        built = module.build()
        home = built["files"]["index.html"]
        self.assertIn("generated: true", home)
        self.assertIn("ir-render: local", home)
        self.assertIn('href="architecture/status.html"', home)
        self.assertIn('href="workflow/status.html"', home)
        self.assertIn("打开 Architecture 状态页", home)
        self.assertIn("打开 Workflow 状态页", home)
        for rel, ir in (
            ("architecture/status.html", "architecture.json"),
            ("workflow/status.html", "runtime.workflow.json"),
        ):
            page = built["files"][rel]
            self.assertIn("ir-render: local", page, rel)
            self.assertIn(ir, page, rel)
            self.assertNotIn("archify-render: diagrams", page, rel)
        history = (VIZ_OUT / "design-history/index.html").read_text(encoding="utf-8")
        self.assertIn("这不是文档首页", history)

    def test_openclaw_is_not_a_default_mount(self) -> None:
        reg = yaml.safe_load((ROOT / "01_skill-integration" / "registry.yaml").read_text(encoding="utf-8"))
        default = reg["default_source"]
        self.assertEqual(default["id"], "my-skills")
        self.assertNotIn("openclaw", default["id"].lower())
        self.assertNotIn("openclaw", str(default["source"]).lower())
        for mount in reg["mounts"]:
            blob = " ".join(str(mount.get(key, "")) for key in ("id", "source", "atomic_package")).lower()
            self.assertNotIn("openclaw", blob, mount.get("id"))
        contract = yaml.safe_load(
            (ROOT / "04_analysis" / "personal" / "visualization" / "visualization-source-contract.yaml").read_text(encoding="utf-8")
        )
        self.assertIn("OpenClaw", contract["forbidden_default_atomic_mount_sources"])
        page = (VIZ_OUT / "mounts/index.html").read_text(encoding="utf-8")
        self.assertIn("Default atomic mount source", page)
        self.assertIn("my-skills", page)
        self.assertIn("OpenClaw is not a default atomic mount source", page)
        self.assertNotIn("openclaw-medical-skills", page)
        arch = (VIZ_OUT / "architecture/architecture.json").read_text(encoding="utf-8").lower()
        self.assertNotIn("openclaw", arch)

    def test_no_new_top_level_07_skill(self) -> None:
        names = [path.name for path in ROOT.iterdir() if path.is_dir()]
        # 07_response is the intentional response seat; forbid other 07_* (e.g. visualization).
        other_07 = [name for name in names if name.startswith("07") and name != "07_response"]
        self.assertFalse(other_07)
        self.assertIn("07_response", names)
        self.assertFalse((ROOT / "07_visualization").exists())
        arch = json.loads((VIZ_OUT / "architecture/architecture.json").read_text(encoding="utf-8"))
        for component in arch["components"]:
            label = str(component["label"])
            if label.startswith("07"):
                self.assertTrue(
                    label.startswith("07_response") or "response" in label.lower(),
                    f"unexpected viz component label {label!r}",
                )
                if component["id"] == "c07":
                    self.assertIn("response", label.lower())

    def test_delta_lists_structural_facts_only(self) -> None:
        module = load_generator()
        before = {
            "components": {"c00": "00"},
            "connections": {},
            "nodes": {},
            "edges": {},
        }
        after = {
            "components": {"c00": "00 Control / QC", "c01": "01 skill-integration / Registry"},
            "connections": {},
            "nodes": {"task": "Task"},
            "edges": {},
        }
        delta = module.structural_delta(before, after)
        self.assertEqual(delta["added"]["components"], ["c01"])
        self.assertEqual(delta["removed"]["components"], [])
        self.assertEqual(delta["changed"]["components"][0]["id"], "c00")
        self.assertEqual(delta["note"], "structural facts only")
        blob = json.dumps(delta)
        self.assertNotIn("merge_safety", blob)
        self.assertNotIn("severity", blob)
        page = (VIZ_OUT / "changes/latest-delta.html").read_text(encoding="utf-8")
        self.assertIn("Added", page)
        self.assertIn("Removed", page)
        self.assertIn("Changed", page)
        self.assertIn("structural identifier and label changes only", page)

    def test_check_matches_committed_outputs(self) -> None:
        # The external renderer is gone; pages it produced carry this meta tag.
        # Regenerate the lab OUT once, then this compare is live again.
        rendered = VIZ_OUT / "architecture" / "index.html"
        if rendered.is_file() and 'content="archify 3.0.1"' in rendered.read_text(encoding="utf-8"):
            self.skipTest(
                "lab OUT still holds renderer-produced pages; "
                "regenerate once with gen_visualization.py (no --check)"
            )
        before = (VIZ_OUT / "architecture/architecture.json").read_bytes()
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(before, (VIZ_OUT / "architecture/architecture.json").read_bytes())

    def test_shape_failure_does_not_publish(self) -> None:
        module = load_generator()
        arch = json.loads((VIZ_OUT / "architecture/architecture.json").read_text(encoding="utf-8"))
        wf = json.loads((VIZ_OUT / "workflow/runtime.workflow.json").read_text(encoding="utf-8"))
        arch["schema_version"] = 9
        with self.assertRaises(module.GateFailure):
            module.validate_ir(arch, wf)

if __name__ == "__main__":
    unittest.main()
