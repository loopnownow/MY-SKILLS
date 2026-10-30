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
        self.assertTrue(any(str(x).startswith("07") for x in labels), labels)
        self.assertIn("p07", {n["id"] for n in built["workflow"]["nodes"]})
        self.assertNotIn("p04", {n["id"] for n in built["workflow"]["nodes"]})
        self.assertIn("p02_stats", {n["id"] for n in built["workflow"]["nodes"]})

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
        with self.assertRaises(mod.GateFailure) as ctx:
            mod.validate_ir(arch, wf)
        self.assertIn("07", str(ctx.exception))

    def test_required_paths_are_reachable(self) -> None:
        mod = load_generator()
        wf = mod.workflow_ir()
        ids = {n["id"] for n in wf["nodes"]}
        adj = {nid: [] for nid in ids}
        for edge in wf["edges"]:
            adj[edge["from"]].append(edge["to"])

        def reachable(src: str, dst: str) -> bool:
            seen = {src}
            stack = [src]
            while stack:
                cur = stack.pop()
                if cur == dst:
                    return True
                for nxt in adj[cur]:
                    if nxt not in seen:
                        seen.add(nxt)
                        stack.append(nxt)
            return False

        for rel in wf["semanticChecks"]["requiredPaths"]:
            self.assertTrue(
                reachable(rel["from"], rel["to"]),
                f"not reachable: {rel['from']} -> {rel['to']}",
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
