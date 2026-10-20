"""Visualization architecture v1.0: contract, IR shape, mount policy; 07_response allowed."""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_FACT_SOURCES = (
    "LLM inference",
    "generated HTML",
    "previous generated HTML",
    "arbitrary mounted-file crawling",
    "filename alone",
    "visual appearance",
    "unvalidated JSON",
)


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

if __name__ == "__main__":
    unittest.main()
