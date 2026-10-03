"""Five control-plane QC checks. No LLM."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_repo_qc():
    path = ROOT / "skill-harvest" / "scripts" / "repo_qc.py"
    spec = importlib.util.spec_from_file_location("repo_qc_five", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class FiveFixes(unittest.TestCase):
    def test_measured_count_is_52_and_checks_pass(self) -> None:
        qc = load_repo_qc()
        entries, expected = qc.parse_registry(ROOT)
        self.assertEqual(len(entries), 52)
        self.assertEqual(expected, 52)
        self.assertEqual(qc.LIVE_FINE_ID_COUNT, 52)
        results = []
        qc.check_five_fixes(ROOT, results)
        failed = [(name, detail) for status, name, detail in results if status != "PASS"]
        self.assertEqual(failed, [])

    def test_mountq_yes_direct_to_ready_fails(self) -> None:
        qc = load_repo_qc()
        diagram = """
        flowchart TD
        Need02 --> MountQ{session_picked_fine_ids}
        MountQ -->|是| Ready[挂载就绪]
        MountQ -->|否| S01
        S01 --> GA0{{G0}}
        GA0 -->|PASS| Ready
        """
        problems = qc.mount_route_problems(diagram)
        self.assertTrue(problems, problems)
        self.assertTrue(any("Ready" in item for item in problems), problems)

    def test_live_mount_routes_go_through_g0(self) -> None:
        qc = load_repo_qc()
        diagram = (ROOT / "00_orchestrator" / "runtime-flow.mmd").read_text(encoding="utf-8")
        self.assertEqual(qc.mount_route_problems(diagram), [])

    def test_generated_artifact_framework_covers_map_and_mounted_skills(self) -> None:
        qc = load_repo_qc()
        scripts = {spec["script"].as_posix() for spec in qc.GENERATED_CHECKS}
        self.assertIn("00_orchestrator/scripts/gen_repo_map.py", scripts)
        self.assertIn("01_skill-discovery-integration/scripts/gen_mounted_skills.py", scripts)
        results = []
        qc.check_generated_artifacts(ROOT, results)
        failed = [row for row in results if row[0] != "PASS"]
        self.assertEqual(failed, [])
        names = [row[1] for row in results]
        self.assertEqual(names, ["repo-map-generated", "mounted-skills-generated"])

    def test_reseived_study_folder_alias_parses_as_received(self) -> None:
        state = yaml.safe_load(
            (ROOT / "00_orchestrator" / "templates" / "project-state.yaml").read_text(encoding="utf-8")
        )
        aliases = state["study_folder_stage_aliases"]
        self.assertEqual(aliases["reseived"], "received")
        self.assertNotIn("reseived", (state.get("pipeline") or {}).get("stage", ""))


if __name__ == "__main__":
    unittest.main()