"""Project-state and handoff templates cover hard gates and citation fields."""
from __future__ import annotations

import unittest

from tests.support import ROOT, read

STATE = ROOT / "00_orchestrator" / "templates" / "project-state.yaml"
HANDOFF = ROOT / "00_orchestrator" / "templates" / "handoff.yaml"
HARD_GATES = ("G-FACT", "G-LIT", "G-CODE", "G0", "G-PHI", "G-STATS", "G-05", "G-06")
STATE_KEYS = (
    'stage: ""',
    "# classify | 02 | 03 | 05 | 06 | qc | done",
    "citation_verify:",
    "g_cit_1:",
    "g_cit_2:",
    "table_path:",
    "rounds:",
    "defects[].rounds",
)


class StateTemplate(unittest.TestCase):
    def test_templates_cover_hard_gates_and_citation(self) -> None:
        for text, label in ((read(STATE), "project-state"), (read(HANDOFF), "handoff")):
            for gid in HARD_GATES:
                self.assertIn(gid, text, f"{label} missing {gid}")
        state = read(STATE)
        for key in STATE_KEYS:
            self.assertIn(key, state, f"project-state missing {key!r}")
