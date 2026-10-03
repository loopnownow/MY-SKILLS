"""Control-plane consistency repairs. No LLM."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_repo_qc():
    path = ROOT / "skill-harvest" / "scripts" / "repo_qc.py"
    spec = importlib.util.spec_from_file_location("repo_qc", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class StaleIds(unittest.TestCase):
    def test_known_retired_id_04_figure_engine(self) -> None:
        qc = load_repo_qc()
        canonical = qc.canonical_fine_ids(ROOT)
        aliases = qc.load_alias_map(ROOT)
        self.assertNotIn("04-figure-engine", canonical)
        self.assertNotIn("04-figure-engine", aliases)
        hits = qc.stale_id_hits(
            "Load `04-figure-engine` for this figure.\n",
            canonical,
            aliases,
            workflow=False,
        )
        self.assertEqual(hits, ["1:04-figure-engine"])

    def test_confirmed_alias_resolves_and_is_not_unknown(self) -> None:
        qc = load_repo_qc()
        aliases = qc.load_alias_map(ROOT)
        canonical = qc.canonical_fine_ids(ROOT)
        self.assertEqual(aliases["02-tables"], "clean-data")
        self.assertIn("clean-data", canonical)
        self.assertEqual(qc.resolve_alias("02-tables", aliases), "clean-data")
        hits = qc.stale_id_hits(
            "historical note `02-tables`\n",
            canonical,
            aliases,
            workflow=False,
        )
        self.assertEqual(hits, [])


class RouteContract(unittest.TestCase):
    def test_fast_routing_matches_contract(self) -> None:
        contract = yaml.safe_load((ROOT / "00_orchestrator" / "route-contract.yaml").read_text(encoding="utf-8"))
        skill = (ROOT / "00_orchestrator" / "SKILL.md").read_text(encoding="utf-8")
        start = skill.index("### Fast routing")
        end = skill.index("## 2. Skill chain")
        section = skill[start:end]
        intents = [row["intent"] for row in contract["routes"]]
        self.assertEqual(
            intents,
            ["文献检索", "Excel清洗", "样本量", "写论文", "回复审稿人", "新技能", "技能迭代"],
        )
        for row in contract["routes"]:
            for token in row["contains"]:
                self.assertIn(token, section, row["intent"])


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


if __name__ == "__main__":
    unittest.main()
