"""Gate ids must be registered in both the registry and the 00 route table.

Historical defect (2026-10-20): G-07 existed in gates.md and runtime-flow.mmd
but was missing from 00/SKILL.md, and 07_response/SKILL.md never mentioned a
gate at all, so the last gate could be skipped by anyone reading only the table.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATES = ROOT / "00_orchestrator" / "gates.md"
ZERO = ROOT / "00_orchestrator" / "SKILL.md"
SEVEN = ROOT / "07_response" / "SKILL.md"

ROW = re.compile(r"^\|\s*\**\s*(G0|G-[A-Z0-9]+(?:-[A-Z0-9]+)*)\s*\**\s*\|")


def gate_rows(text: str) -> set[str]:
    ids = set()
    for line in text.splitlines():
        m = ROW.match(line)
        if m:
            ids.add(m.group(1))
    return ids


class GateTableParity(unittest.TestCase):
    def test_every_registry_gate_is_in_the_route_table(self) -> None:
        registry = gate_rows(GATES.read_text(encoding="utf-8"))
        table = gate_rows(ZERO.read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(registry), 8, registry)
        self.assertEqual(
            sorted(registry - table),
            [],
            "gates.md gates missing from 00/SKILL.md route table",
        )

    def test_route_table_has_no_unregistered_gate(self) -> None:
        registry = gate_rows(GATES.read_text(encoding="utf-8"))
        table = gate_rows(ZERO.read_text(encoding="utf-8"))
        self.assertEqual(
            sorted(table - registry),
            [],
            "00/SKILL.md table names a gate that gates.md does not define",
        )

    def test_g07_is_named_by_the_response_skill(self) -> None:
        text = SEVEN.read_text(encoding="utf-8")
        self.assertIn("G-07", text)
        self.assertIn("gates.md", text)


if __name__ == "__main__":
    unittest.main()
