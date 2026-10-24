#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bidirectional map: gates.md ids ↔ runtime-flow.mmd nodes."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATES = ROOT / "00_orchestrator" / "gates.md"
MMD = ROOT / "00_orchestrator" / "runtime-flow.mmd"
STATE = ROOT / "00_orchestrator" / "templates" / "project-state.yaml"
HANDOFF = ROOT / "00_orchestrator" / "templates" / "handoff.yaml"

# Canonical gate ids from gates.md table (exclude invented G-HARD / G-QUALITY).
GATE_IDS = ("G0", "G-PHI", "G-FACT", "G-LIT", "G-CODE", "G-04", "G-05", "G-06", "G-07")


def gate_ids_from_gates_md(text: str) -> set[str]:
    found = set()
    for line in text.splitlines():
        m = re.match(r"\|\s*(G0|G-[A-Z0-9]+)\s*\|", line)
        if m:
            found.add(m.group(1))
    return found


def tokens_from_mmd(text: str) -> set[str]:
    """Normalize mmd gate labels to G-* / G0 ids."""
    tokens: set[str] = set()
    for m in re.finditer(r"Gate\s*·\s*(\d+)", text):
        tokens.add(f"G-{m.group(1)}")
    for m in re.finditer(r"\{\{(G0|G-[A-Z0-9]+)", text):
        tokens.add(m.group(1))
    # Plain mentions in node text / comments for HARD/QUALITY gates that are not {{ }}.
    for gid in GATE_IDS:
        if gid == "G0":
            if re.search(r"\bG0\b", text):
                tokens.add("G0")
        elif gid in text:
            tokens.add(gid)
    return tokens


class GateMmdMap(unittest.TestCase):
    def test_gates_md_lists_expected_ids(self) -> None:
        text = GATES.read_text(encoding="utf-8")
        found = gate_ids_from_gates_md(text)
        for gid in GATE_IDS:
            self.assertIn(gid, found, f"gates.md missing table row for {gid}")

    def test_mmd_covers_every_gate_id(self) -> None:
        mmd = MMD.read_text(encoding="utf-8")
        tokens = tokens_from_mmd(mmd)
        missing = [gid for gid in GATE_IDS if gid not in tokens]
        self.assertEqual(missing, [], f"runtime-flow.mmd missing gate tokens: {missing}")

    def test_mmd_gate_dot_maps_to_g_nn(self) -> None:
        mmd = MMD.read_text(encoding="utf-8")
        for n in ("04", "05", "06", "07"):
            self.assertIn(f"Gate · {n}", mmd)
        self.assertIn("Gate · NN ↔ gates.md G-NN", mmd)
        md = (ROOT / "00_orchestrator" / "runtime-flow.md").read_text(encoding="utf-8")
        self.assertIn("Gate · NN` ↔ `gates.md` `G-NN`", md)

    def test_mmd_has_plan_n_nodes_style_lint_and_defect_budget(self) -> None:
        mmd = MMD.read_text(encoding="utf-8")
        for token in (
            "grilling",
            "Plan card",
            "flowchart approval",
            "N2 · G-PHI",
            "N3 WRITE",
            "N4 PREVIEW",
            "style-lint",
            "G-CODE",
            "defects[].rounds",
        ):
            self.assertIn(token, mmd, token)

    def test_state_templates_cover_hard_gates_and_citation(self) -> None:
        state = STATE.read_text(encoding="utf-8")
        hand = HANDOFF.read_text(encoding="utf-8")
        for text, label in ((state, "project-state"), (hand, "handoff")):
            for gid in ("G-FACT", "G-LIT", "G-CODE", "G0", "G-PHI", "G-04", "G-05", "G-06"):
                self.assertIn(gid, text, f"{label} missing {gid}")
        self.assertIn("stage: \"\"          # classify | 02 | 03 | 04 | 05 | 06 | qc | done", state)
        self.assertIn("citation_verify:", state)
        self.assertIn("g_cit_1:", state)
        self.assertIn("g_cit_2:", state)
        self.assertIn("table_path:", state)
        self.assertIn("rounds:", state)  # defects[].rounds documented
        self.assertIn("defects[].rounds", state)


if __name__ == "__main__":
    unittest.main()
