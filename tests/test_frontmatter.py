"""YAML/frontmatter parses and cited contract files exist.

Merged from: `test_visualization_contract.py`, `test_yaml_valid.py`.
"""
from __future__ import annotations

from pathlib import Path
import importlib.util
import unittest
import yaml

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

SCRIPT = ROOT / "02_data-processing" / "advanced" / "visualization" / "scripts" / "gen_visualization.py"
FORBIDDEN_FACT_SOURCES = (
    "LLM inference",
    "generated HTML",
    "previous generated HTML",
    "arbitrary external-file crawling",
    "filename alone",
    "visual appearance",
    "unvalidated JSON",
)
def load_generator():
    spec = importlib.util.spec_from_file_location("gen_visualization", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
SKIP_PARTS = {".git", "__pycache__", "node_modules"}
def repo_yaml_files() -> list[Path]:
    """Enumerate YAML on disk. Do not trust git ls-files after reorg ghosts."""
    files = []
    for p in list(ROOT.rglob("*.yaml")) + list(ROOT.rglob("*.yml")):
        rel = p.relative_to(ROOT)
        if SKIP_PARTS & set(rel.parts):
            continue
        files.append(p)
    return files

class VisualizationContract(unittest.TestCase):
    def test_contract_files_exist(self) -> None:
        for rel in (
            "02_data-processing/advanced/visualization/visualization-architecture.md",
            "02_data-processing/advanced/visualization/visualization-source-contract.yaml",
            "02_data-processing/advanced/visualization/scripts/gen_visualization.py",
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_ir_schema_versions_are_fixed(self) -> None:
        built = load_generator().build()
        self.assertEqual(built["architecture"]["schema_version"], 1)
        self.assertEqual(built["workflow"]["schema_version"], 2)
        self.assertEqual(built["files"]["build-manifest.json"].count('"schema_version"'), 1)

    def test_forbidden_fact_sources_are_listed(self) -> None:
        text = (ROOT / "02_data-processing" / "advanced" / "visualization" / "visualization-source-contract.yaml").read_text(encoding="utf-8")
        for phrase in FORBIDDEN_FACT_SOURCES:
            self.assertIn(phrase, text)
    def test_workflow_must_show_requires_07(self) -> None:
        mod = load_generator()
        built = mod.build()
        labels = [n["label"] for n in built["workflow"]["nodes"]]
        ids = {n["id"] for n in built["workflow"]["nodes"]}
        self.assertTrue(any(str(x).startswith("07") for x in labels), labels)
        self.assertIn("p07", ids)
        self.assertIn("ga07", ids)
        self.assertTrue(any("G-07" in str(n.get("sublabel", "")) or "Gate" in str(n.get("label", "")) for n in built["workflow"]["nodes"] if n["id"] == "ga07"))
        edge_labels = [str(e.get("label", "")) for e in built["workflow"]["edges"]]
        self.assertTrue(any("G-07" in lab for lab in edge_labels), edge_labels)
        self.assertNotIn("p04", ids)
        self.assertIn("p02_stats", ids)

    def test_workflow_missing_07_fails_validate(self) -> None:
        mod = load_generator()
        arch = mod.architecture_ir()
        wf = mod.workflow_ir()
        mod.validate_ir(arch, wf)
        wf["nodes"] = [n for n in wf["nodes"] if n["id"] != "p07"]
        wf["edges"] = [e for e in wf["edges"] if e["from"] != "p07" and e["to"] != "p07"]
        # drop semantic edges that require p07 so must_show is the failure mode
        checks = wf["semanticChecks"]
        checks["requiredEdges"] = [
            e for e in checks["requiredEdges"] if e.get("to") != "p07" and e.get("from") != "p07"
        ]
        checks["requiredPaths"] = [
            p for p in checks["requiredPaths"] if p.get("from") != "p07" and p.get("to") != "p07"
        ]
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch, wf)
        self.assertIn("07", str(ctx.exception))

    def test_workflow_missing_g07_fails_validate(self) -> None:
        mod = load_generator()
        arch = mod.architecture_ir()
        wf = mod.workflow_ir()
        mod.validate_ir(arch, wf)
        wf["nodes"] = [n for n in wf["nodes"] if n["id"] != "ga07"]
        wf["edges"] = [e for e in wf["edges"] if e["from"] != "ga07" and e["to"] != "ga07"]
        # Keep p07 completable without G-07 so the failure is missing G-07, not an extra terminal.
        wf["edges"].append(
            {
                "id": "e-07-done-bypass",
                "from": "p07",
                "to": "done",
                "label": "response complete",
                "role": "branch",
            }
        )
        checks = wf["semanticChecks"]
        checks["requiredEdges"] = [
            e
            for e in checks["requiredEdges"]
            if e.get("to") != "ga07" and e.get("from") != "ga07"
        ]
        checks["requiredPaths"] = [
            p
            for p in checks["requiredPaths"]
            if p.get("to") != "ga07" and p.get("from") != "ga07"
        ]
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch, wf)
        self.assertIn("G-07", str(ctx.exception))

    def test_required_paths_are_reachable(self) -> None:
        mod = load_generator()
        arch = mod.architecture_ir()
        wf = mod.workflow_ir()
        # Positive: validate_ir itself enforces requiredPaths reachability.
        mod.validate_ir(arch, wf)

    def test_required_path_edge_drop_fails_validate(self) -> None:
        mod = load_generator()
        arch = mod.architecture_ir()
        wf = mod.workflow_ir()
        mod.validate_ir(arch, wf)
        # Drop a required-path edge (p05 -> lit05) and assert GateFailure from validate_ir.
        wf["edges"] = [
            e for e in wf["edges"] if not (e["from"] == "p05" and e["to"] == "lit05")
        ]
        # Keep requiredEdges list intact so the failure is structural / path-based.
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch, wf)
        msg = str(ctx.exception)
        self.assertTrue(
            "required" in msg.lower() or "reachable" in msg.lower() or "edge" in msg.lower(),
            msg,
        )

    def test_duplicate_ids_fail_validate(self) -> None:
        mod = load_generator()
        arch = mod.architecture_ir()
        wf = mod.workflow_ir()
        mod.validate_ir(arch, wf)
        wf["nodes"].append(dict(wf["nodes"][0], id=wf["nodes"][0]["id"], lane="qc", col=0))
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch, wf)
        self.assertIn("duplicate", str(ctx.exception).lower())

        wf = mod.workflow_ir()
        wf["edges"].append(dict(wf["edges"][0], id=wf["edges"][0]["id"]))
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch, wf)
        self.assertIn("duplicate", str(ctx.exception).lower())

        arch2 = mod.architecture_ir()
        arch2["connections"].append(dict(arch2["connections"][0], id=arch2["connections"][0]["id"]))
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch2, mod.workflow_ir())
        self.assertIn("duplicate", str(ctx.exception).lower())

    def test_facts_from_ir_rejects_duplicate_ids(self) -> None:
        mod = load_generator()
        wf = mod.workflow_ir()
        wf["nodes"].append(dict(wf["nodes"][0], id=wf["nodes"][0]["id"], lane="qc", col=0))
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.facts_from_ir(mod.architecture_ir(), wf)
        self.assertIn("duplicate", str(ctx.exception).lower())

    def test_extra_root_fails_validate(self) -> None:
        mod = load_generator()
        arch = mod.architecture_ir()
        wf = mod.workflow_ir()
        mod.validate_ir(arch, wf)
        # Add an isolated indegree-0 node outside allowedRoots.
        wf["nodes"].append(
            {
                "id": "orphan",
                "lane": "qc",
                "col": 0,
                "type": "backend",
                "label": "Orphan",
                "sublabel": "bad root",
                "width": 176,
                "height": 64,
            }
        )
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch, wf)
        self.assertTrue(
            "allowedRoots" in str(ctx.exception) or "orphan" in str(ctx.exception),
            str(ctx.exception),
        )

class YamlValid(unittest.TestCase):
    def test_all_repo_yaml_parses(self) -> None:
        files = repo_yaml_files()
        self.assertGreaterEqual(len(files), 10, msg=str([str(p.relative_to(ROOT)) for p in files]))
        bad = []
        for p in files:
            try:
                yaml.safe_load(p.read_text(encoding="utf-8"))
            except yaml.YAMLError as exc:
                bad.append(f"{p.relative_to(ROOT)}: {exc}")
        self.assertEqual(bad, [], msg="\n".join(bad))
