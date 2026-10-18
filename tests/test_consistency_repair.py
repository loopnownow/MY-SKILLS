"""Control-plane consistency repairs. No LLM."""
from __future__ import annotations

import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class RouteContract(unittest.TestCase):
    def test_fast_routing_matches_contract(self) -> None:
        contract = yaml.safe_load((ROOT / "00_orchestrator" / "route-contract.yaml").read_text(encoding="utf-8"))
        skill = (ROOT / "00_orchestrator" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("references/fast-routing.md", skill)
        section = (ROOT / "00_orchestrator" / "references" / "fast-routing.md").read_text(encoding="utf-8")
        routes = contract["routes"]
        self.assertGreaterEqual(len(routes), int(contract.get("min_routes", 20)))
        for row in routes:
            for token in row["contains"]:
                self.assertIn(token, section, row["intent"])
        for row in contract.get("counterexamples") or []:
            for token in row["must_not_contain"]:
                self.assertNotIn(token, section, row["intent"])


class ProvenanceSchema(unittest.TestCase):
    def test_schema_names_mount_provenance_fields(self) -> None:
        fields = ["fine_id", "source", "resolved_commit", "path", "content_hash", "checked_at"]
        for rel in (
            "00_orchestrator/templates/project-state.yaml",
            "00_orchestrator/templates/handoff.yaml",
            "00_orchestrator/gates.md",
        ):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("mount_provenance", text, rel)
            for field in fields:
                self.assertIn(field, text, f"{rel} {field}")


class GateAlignment(unittest.TestCase):
    def test_runtime_flow_has_no_g02_g03_and_names_citation_labels(self) -> None:
        mmd = (ROOT / "00_orchestrator" / "runtime-flow.mmd").read_text(encoding="utf-8")
        md = (ROOT / "00_orchestrator" / "runtime-flow.md").read_text(encoding="utf-8")
        for text in (mmd, md):
            self.assertNotIn("G-02", text)
            self.assertNotIn("G-03", text)
            self.assertIn("G-CIT-1", text)
            self.assertIn("G-CIT-2", text)
        gates = (ROOT / "00_orchestrator" / "gates.md").read_text(encoding="utf-8")
        for token in (
            "event count",
            "missing count",
            "exclusion count",
            "analysis population",
            "primary/secondary endpoint",
            "time origin",
            "reference category",
            "OR/HR direction",
            "units",
            "threshold",
            "95% CI method",
            "model formula",
        ):
            self.assertIn(token, gates)
        self.assertIn("Do not auto-pick numbers", gates)


class CanonicalIdRule(unittest.TestCase):
    def test_rule_text_and_radiomics_chain(self) -> None:
        block = (ROOT / "01_skill-integration" / "references" / "id-rules.md").read_text(encoding="utf-8")
        for phrase in (
            "only runtime and session-pick identifier",
            "must not be used as a fine id",
            "must not be used for routing",
            "session-pick bucket",
            "execution owner",
            "path_shared",
            "does not rename the fine id",
            "explicit registry migration",
            "must never be used to infer an id",
            "only canonical identifier",
            "02-tables` → `clean-data",
        ):
            self.assertIn(phrase, block, phrase)
        header = (ROOT / "01_skill-integration" / "registry.yaml").read_text(encoding="utf-8").split("meta:", 1)[0]
        self.assertIn("Canonical ID Rule", header)
        self.assertIn("must never be used to infer", header)
        rad = (ROOT / "00_orchestrator" / "workflows" / "radiomics-study.md").read_text(encoding="utf-8")
        self.assertLess(rad.index("`clean-data`"), rad.index("`preprocess-imaging`"))
        self.assertLess(rad.index("`preprocess-imaging`"), rad.index("`radiomics-ml`"))
        for banned in ("02-tables", "02-imaging-qc", "02-radiomics-habitat"):
            self.assertNotIn(banned, rad)
        aliases = yaml.safe_load((ROOT / "01_skill-integration" / "legacy_aliases.yaml").read_text(encoding="utf-8"))["aliases"]
        self.assertEqual(aliases["02-tables"], "clean-data")


if __name__ == "__main__":
    unittest.main()
