"""Gate table, mmd map and verdict vocabulary contract.

Merged from: `test_gate_table_parity.py`, `test_gate_mmd_map.py`, `test_verdict_vocabulary.py`.
"""
from __future__ import annotations

from pathlib import Path
import re
import unittest

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

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
MMD = ROOT / "00_orchestrator" / "runtime-flow.mmd"
STATE = ROOT / "00_orchestrator" / "templates" / "project-state.yaml"
HANDOFF = ROOT / "00_orchestrator" / "templates" / "handoff.yaml"
GATE_IDS = ("G0", "G-PHI", "G-FACT", "G-LIT", "G-CODE", "G-STATS", "G-05", "G-06", "G-07")
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
BAD = re.compile(r"N/A|(?<![A-Za-z])n/a|(?i:not applicable)|(?<![A-Za-z])SKIP(?![A-Za-z])")
EXEMPT_LINE = (
    re.compile(r"#N/A"),        # Excel error code in a vendored pack
    re.compile(r"SKIP_[A-Z]"),  # configuration token, not a verdict
)
EXEMPT_PAIRS = (
    # Quoted manuscript sentence showing correct English usage.
    ("05_manuscript/personal/Aitor-format.md", "were not applicable"),
)

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
        for n in ("05", "06", "07"):
            self.assertIn(f"Gate · {n}", mmd)
        self.assertIn("Gate · STATS", mmd)
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
class VerdictVocabulary(unittest.TestCase):
    def test_no_variant_verdict_tokens(self) -> None:
        violations: list[str] = []
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("tests/"):
                continue
            for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if not BAD.search(line):
                    continue
                if any(rx.search(line) for rx in EXEMPT_LINE):
                    continue
                if any(rel == f and snippet in line for f, snippet in EXEMPT_PAIRS):
                    continue
                violations.append(f"{rel}:{i}: {line.strip()[:110]}")
        self.assertEqual(
            violations,
            [],
            "use NOT_APPLICABLE (assurance-verdicts.md):\n" + "\n".join(violations[:40]),
        )
