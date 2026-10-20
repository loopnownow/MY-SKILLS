"""Visualization architecture v1.0: contract, IR shape, mount policy; 07_response allowed."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "04_analysis" / "personal" / "visualization" / "scripts" / "gen_visualization.py"
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
            "04_analysis/personal/visualization/visualization-source-contract.yaml",
            "04_analysis/personal/visualization/scripts/gen_visualization.py",
            # ".github/workflows/visualization.yml",  # archived with .github/ 2026-10-17 to 0del
        ):
            self.assertTrue((ROOT / rel).is_file(), rel)

    def test_ir_schema_versions_are_fixed(self) -> None:
        built = load_generator().build()
        self.assertEqual(built["architecture"]["schema_version"], 1)
        self.assertEqual(built["workflow"]["schema_version"], 2)
        self.assertEqual(built["files"]["build-manifest.json"].count('"schema_version"'), 1)

    def test_forbidden_fact_sources_are_listed(self) -> None:
        text = (ROOT / "04_analysis" / "personal" / "visualization" / "visualization-source-contract.yaml").read_text(encoding="utf-8")
        for phrase in FORBIDDEN_FACT_SOURCES:
            self.assertIn(phrase, text)

if __name__ == "__main__":
    unittest.main()
