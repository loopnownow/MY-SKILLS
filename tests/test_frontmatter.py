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

SCRIPT = ROOT / "02_data-processing" / "personal" / "visualization" / "scripts" / "gen_visualization.py"
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
            "02_data-processing/personal/visualization/visualization-architecture.md",
            "02_data-processing/personal/visualization/visualization-source-contract.yaml",
            "02_data-processing/personal/visualization/scripts/gen_visualization.py",
            # ".github/workflows/visualization.yml",  # archived with .github/ 2026-10-17 to 0del
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_ir_schema_versions_are_fixed(self) -> None:
        built = load_generator().build()
        self.assertEqual(built["architecture"]["schema_version"], 1)
        self.assertEqual(built["workflow"]["schema_version"], 2)
        self.assertEqual(built["files"]["build-manifest.json"].count('"schema_version"'), 1)

    def test_forbidden_fact_sources_are_listed(self) -> None:
        text = (ROOT / "02_data-processing" / "personal" / "visualization" / "visualization-source-contract.yaml").read_text(encoding="utf-8")
        for phrase in FORBIDDEN_FACT_SOURCES:
            self.assertIn(phrase, text)
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
