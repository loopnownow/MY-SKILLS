"""Gate table, mmd map, verdict vocabulary, and state-template contract.

Merged from: `test_gate_table_parity.py`, `test_gate_mmd_map.py`, `test_verdict_vocabulary.py`, `test_state_template.py`.
Also hosts Deep-QC P1 Mermaid / viz seat guards.
"""
from __future__ import annotations

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
    text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("%%"))
    tokens: set[str] = set()
    for m in re.finditer(r"Gate\s*·\s*(\d+|[A-Z]+)", text):
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
    ("05_manuscript/advanced/Aitor-format.md", "were not applicable"),
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


class MermaidGraphIntegrity(unittest.TestCase):
    """Deep-QC P1: every referenced mmd node is defined; FineId pick reaches G0."""

    EDGE = re.compile(
        r"(?P<src>[A-Za-z][\w]*)\s*(?:-->|-.->|===|==>)"
        r"\s*(?:\|[^|]*\|\s*)?(?P<dst>[A-Za-z][\w]*)"
    )
    FAN_SRC = re.compile(
        r"(?P<srcs>[A-Za-z][\w]*(?:\s*&\s*[A-Za-z][\w]*)+)"
        r"\s*(?:-->|-.->)\s*(?:\|[^|]*\|\s*)?(?P<dst>[A-Za-z][\w]*)"
    )
    NODE_DEF = re.compile(r"\b([A-Za-z][\w]*)\s*(?:\[|\(\(|\(|\{\{|\{)")

    def _body_lines(self, text: str) -> list[str]:
        return [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith("%%")]

    def _defined_ids(self, text: str) -> set[str]:
        ids: set[str] = set()
        for line in self._body_lines(text):
            for m in self.NODE_DEF.finditer(line):
                ids.add(m.group(1))
        return ids

    def _referenced_ids(self, text: str) -> set[str]:
        refs: set[str] = set()
        for line in self._body_lines(text):
            for m in self.EDGE.finditer(line):
                refs.add(m.group("src"))
                refs.add(m.group("dst"))
            for m in self.FAN_SRC.finditer(line):
                for src in re.findall(r"[A-Za-z][\w]*", m.group("srcs")):
                    refs.add(src)
                refs.add(m.group("dst"))
        return refs

    def test_referenced_nodes_are_defined(self) -> None:
        text = MMD.read_text(encoding="utf-8")
        defined = self._defined_ids(text)
        referenced = self._referenced_ids(text)
        missing = sorted(referenced - defined)
        self.assertEqual(
            missing,
            [],
            "runtime-flow.mmd references undefined nodes (Deep-QC P1):\n" + "\n".join(missing),
        )

    def test_no_retired_seat_01_node_id(self) -> None:
        body = "\n".join(self._body_lines(MMD.read_text(encoding="utf-8")))
        self.assertNotRegex(
            body,
            r"\bS01\b",
            "S01 looks like retired seat 01; use SFineId (or another non-01 id)",
        )

    def test_fineid_pick_reaches_g0(self) -> None:
        body = "\n".join(self._body_lines(MMD.read_text(encoding="utf-8")))
        self.assertIn("SFineId", body)
        self.assertRegex(
            body,
            r"SFineId\s*-->\s*GA0",
            "FineId pick path must reach G0 (SFineId --> GA0); no SFineId dead-end",
        )
        self.assertIn("GA0{{G0}}", body)


class RetiredSeatsBanInActiveViz(unittest.TestCase):
    """P1-02: active viz docs must not present 01/04 as current architecture nodes."""

    VIZ = (
        ROOT
        / "02_data-processing"
        / "advanced"
        / "visualization"
        / "visualization-architecture.md"
    )
    RETIRED_CURRENT = (
        re.compile(r"01[ _]skill-integration", re.I),
        re.compile(r"(?<![A-Za-z0-9-])01 registry\b"),
        re.compile(r"\b04_analysis\b"),
        re.compile(r"(?<![A-Za-z0-9-])01 fine-id registry"),
    )

    def test_visualization_architecture_uses_current_seats(self) -> None:
        text = self.VIZ.read_text(encoding="utf-8")
        bad = []
        for rx in self.RETIRED_CURRENT:
            for m in rx.finditer(text):
                line_start = text.rfind("\n", 0, m.start()) + 1
                line_end = text.find("\n", m.start())
                if line_end < 0:
                    line_end = len(text)
                line = text[line_start:line_end]
                if re.search(r"former|retired|historical|absorbed|was ", line, re.I):
                    continue
                bad.append(line.strip()[:140])
        self.assertEqual(
            bad,
            [],
            "retired seats spoken as current in viz architecture:\n" + "\n".join(bad),
        )
        self.assertIn("00 Control / QC / Registry", text)
        self.assertIn("02 Data", text)
        self.assertIn("07 Response", text)
        self.assertNotIn("01 skill-integration", text)


class StateTemplate(unittest.TestCase):
    """Merged from test_state_template.py."""

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

    def test_templates_cover_hard_gates_and_citation(self) -> None:
        for path, label in ((self.STATE, "project-state"), (self.HANDOFF, "handoff")):
            text = path.read_text(encoding="utf-8")
            for gid in self.HARD_GATES:
                self.assertIn(gid, text, f"{label} missing {gid}")
        state = self.STATE.read_text(encoding="utf-8")
        for key in self.STATE_KEYS:
            self.assertIn(key, state, f"project-state missing {key!r}")
