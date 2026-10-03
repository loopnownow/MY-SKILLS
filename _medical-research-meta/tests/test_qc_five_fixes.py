"""Five control-plane QC checks. No LLM."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()