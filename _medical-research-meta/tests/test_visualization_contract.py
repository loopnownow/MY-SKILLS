"""Visualization architecture v1.0: contract, IR shape, mount policy, no 07 skill."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "00_orchestrator" / "scripts" / "gen_visualization.py"
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
            "00_orchestrator/visualization-architecture.md",
            "00_orchestrator/archify-version.yaml",
            "00_orchestrator/visualization-source-contract.yaml",
            "00_orchestrator/scripts/gen_visualization.py",
            ".github/workflows/visualization.yml",
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_version_record_pins_archify(self) -> None:
        record = yaml.safe_load((ROOT / "00_orchestrator" / "archify-version.yaml").read_text(encoding="utf-8"))
        self.assertEqual(record["source"], "tt-a1i/archify")
        self.assertEqual(record["expected_version"], "3.0.1")
        self.assertEqual(record["update_policy"], "check")
        self.assertIs(record["auto_update"], False)
        self.assertIs(record["visualization_only"], True)
        self.assertEqual(record["schema_pins"]["architecture"]["schema_version"], 1)
        self.assertEqual(record["schema_pins"]["workflow"]["schema_version"], 2)

    def test_forbidden_fact_sources_are_listed(self) -> None:
        text = (ROOT / "00_orchestrator" / "visualization-source-contract.yaml").read_text(encoding="utf-8")
        for phrase in FORBIDDEN_FACT_SOURCES:
            self.assertIn(phrase, text)

    def test_ir_json_parses_and_matches_pins(self) -> None:
        record = yaml.safe_load((ROOT / "00_orchestrator" / "archify-version.yaml").read_text(encoding="utf-8"))
        arch = json.loads((ROOT / "docs/architecture/architecture.json").read_text(encoding="utf-8"))
        wf = json.loads((ROOT / "docs/workflow/runtime.workflow.json").read_text(encoding="utf-8"))
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
        self.assertTrue((ROOT / "docs/index.html").is_file())
        home = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        self.assertIn("generated: true", home)
        self.assertIn("archify-render: not-run", home)
        history = (ROOT / "docs/design-history/index.html").read_text(encoding="utf-8")
        self.assertIn("这不是文档首页", history)

    def test_openclaw_is_not_a_default_mount(self) -> None:
        reg = yaml.safe_load((ROOT / "01_skill-discovery-integration" / "registry.yaml").read_text(encoding="utf-8"))
        default = reg["default_source"]
        self.assertEqual(default["id"], "my-skills-capabilities")
        self.assertNotIn("openclaw", default["id"].lower())
        self.assertNotIn("openclaw", str(default["source"]).lower())
        for mount in reg["mounts"]:
            blob = " ".join(str(mount.get(key, "")) for key in ("id", "source", "atomic_package")).lower()
            self.assertNotIn("openclaw", blob, mount.get("id"))
        contract = yaml.safe_load(
            (ROOT / "00_orchestrator" / "visualization-source-contract.yaml").read_text(encoding="utf-8")
        )
        self.assertIn("OpenClaw", contract["forbidden_default_atomic_mount_sources"])
        page = (ROOT / "docs/mounts/index.html").read_text(encoding="utf-8")
        self.assertIn("Default atomic mount source", page)
        self.assertIn("my-skills-capabilities", page)
        self.assertIn("OpenClaw is not a default atomic mount source", page)
        self.assertNotIn("openclaw-medical-skills", page)
        arch = (ROOT / "docs/architecture/architecture.json").read_text(encoding="utf-8").lower()
        self.assertNotIn("openclaw", arch)

    def test_no_new_top_level_07_skill(self) -> None:
        names = [path.name for path in ROOT.iterdir() if path.is_dir()]
        self.assertFalse([name for name in names if name.startswith("07")])
        self.assertFalse((ROOT / "07_visualization").exists())
        arch = json.loads((ROOT / "docs/architecture/architecture.json").read_text(encoding="utf-8"))
        for component in arch["components"]:
            self.assertFalse(str(component["label"]).startswith("07"))
            self.assertNotEqual(component["id"], "c07")

    def test_delta_lists_structural_facts_only(self) -> None:
        module = load_generator()
        before = {
            "components": {"c00": "00"},
            "connections": {},
            "nodes": {},
            "edges": {},
        }
        after = {
            "components": {"c00": "00 Control / QC", "c01": "01 Discovery / Registry"},
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
        page = (ROOT / "docs/changes/latest-delta.html").read_text(encoding="utf-8")
        self.assertIn("Added", page)
        self.assertIn("Removed", page)
        self.assertIn("Changed", page)
        self.assertIn("structural identifier and label changes only", page)

    def test_check_matches_committed_outputs(self) -> None:
        before = (ROOT / "docs/architecture/architecture.json").read_bytes()
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(before, (ROOT / "docs/architecture/architecture.json").read_bytes())

    def test_shape_failure_does_not_publish(self) -> None:
        module = load_generator()
        arch = json.loads((ROOT / "docs/architecture/architecture.json").read_text(encoding="utf-8"))
        wf = json.loads((ROOT / "docs/workflow/runtime.workflow.json").read_text(encoding="utf-8"))
        arch["schema_version"] = 9
        with self.assertRaises(module.GateFailure):
            module.validate_ir(arch, wf)

    def test_ci_does_not_fetch_or_publish_pages(self) -> None:
        text = (ROOT / ".github" / "workflows" / "visualization.yml").read_text(encoding="utf-8")
        self.assertIn("auto_update is false", text)
        self.assertIn("Fail closed", text)
        self.assertIn("--check", text)
        self.assertNotIn("actions/deploy-pages", text)
        self.assertNotIn("actions/upload-pages-artifact", text)
        self.assertNotIn("npm install", text)
        lowered = text.lower()
        self.assertNotIn("curl ", lowered)
        self.assertNotIn("wget ", lowered)


if __name__ == "__main__":
    unittest.main()
