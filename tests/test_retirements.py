"""Retired ids, seats, packs and absorption residue stay dead.

Merged from: `test_no_retired_ids.py`, `test_no_retired_seat_04.py`, `test_no_b_pack_residue.py`, `test_consistency_repair.py`.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess
import unittest
import yaml

from tests.support import (
    GATES,
    ONE,
    ROOT,
)

HIST_LINE = re.compile(
    r"archived|historical|legacy|absorb|absorbed|formerly|old_path|"
    r"status_note|covers former|round\s*[123]|勿建|do not recreate|归档|archive|archived|was\s+B|retired|"
    r"not on disk|do not recreate|do not adopt|not a live",
    re.I,
)
ALLOW_FILES = {
    "00_orchestrator/registry.yaml",
    "00_orchestrator/legacy_aliases.yaml",
    "00_orchestrator/references/id-rules.md",
    "VERSION.txt",
    "INTEGRATION_MAP.md",
    "02_data-processing/base/README.md",  # archived — do not recreate list
    "03_research/base/README.md",  # archived — do not recreate list
}
PATH_UNIT_ALIAS_KEYS: set[str] = set()
def _retired_ids() -> set[str]:
    # t1123: retired set = legacy_aliases keys (registry no longer lists archived).
    la = yaml.safe_load((ONE / "legacy_aliases.yaml").read_text(encoding="utf-8"))
    alias_keys = set((la.get("aliases") or {}).keys())
    # Keep path-style / still-on-disk unit names out of the retired scan set.
    alias_keys -= PATH_UNIT_ALIAS_KEYS
    return alias_keys
def _scan_paths() -> list[Path]:
    out: list[Path] = []
    for pat in (
        "*_*/SKILL.md",
        "*_*/advanced/route.md",
        "*_*/base/**/MODULE.md",
        "00_orchestrator/gates.md",
        "00_orchestrator/runtime-flow.mmd",
        "ARCHITECTURE.md",
        "README.md",
    ):
        out.extend(ROOT.glob(pat))
    return sorted({p.resolve() for p in out if p.is_file()})
HANDOFF_HEAD = re.compile(
    r"^#{1,6}\s*(handoffs?\b|routes?\b|next steps?\b|open when\b)", re.I
)
def _routing_lines(path: Path, text: str) -> list[tuple[int, str]]:
    rows: list[tuple[int, str]] = []
    in_section = False
    for i, line in enumerate(text.splitlines(), 1):
        if re.match(r"^#{1,6}\s", line):
            in_section = bool(HANDOFF_HEAD.match(line))
            continue
        if in_section:
            rows.append((i, line))
    return rows
no_retired_seat_04_ALLOW_FILES = {
    "INTEGRATION_MAP.md",
    "VERSION.txt",
    "00_orchestrator/legacy_aliases.yaml",
}
SKIP_PREFIXES = ("tests/",)
SUFFIXES = {".md", ".yaml", ".yml", ".txt", ".py", ".mmd", ".json", ".ini", ".mermaid"}
PATTERNS = (
    ("folder", re.compile(r"04_analysis")),
    ("gate", re.compile(r"G-04(?![0-9])")),
    ("node", re.compile(r"Need04|\bP04\b|GF04|GA04")),
)
DUP_FORM = re.compile(r"02\s*[/+→]\s*02|02\s+02")
def tracked_files() -> list[str]:
    """git ls-files; falls back to a filesystem walk when .git is absent (zip export)."""
    try:
        out = subprocess.run(["git", "-C", str(ROOT), "ls-files"], check=True,
                             capture_output=True, text=True, encoding="utf-8").stdout
        files = [line for line in out.splitlines() if line.strip()]
        if files:
            return files
    except (OSError, subprocess.CalledProcessError):
        pass
    return sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*")
                  if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts)
B_PAT = re.compile(r"(?:\bB\s+0[0-7]-[a-z0-9-]+/?\b|\bforce_b\b|\bMY-SKILLS-base\b)")
no_b_pack_residue_ALLOW_FILES = {
    "00_orchestrator/registry.yaml",
    "00_orchestrator/legacy_aliases.yaml",
    "00_orchestrator/references/id-rules.md",
    "VERSION.txt",
    "INTEGRATION_MAP.md",
}
ALLOW_LINE = re.compile(
    r"archived|historical|legacy|old_path|was\s+B|formerly|0del|"
    r"not restored|do not sync|\.grok/skills|assertNotIn|retired",
    re.I,
)

class NoRetiredIds(unittest.TestCase):
    def test_control_plane_has_no_live_retired_ids(self) -> None:
        retired = _retired_ids()
        self.assertGreaterEqual(len(retired), 30)
        violations: list[str] = []
        for path in _scan_paths():
            rel = path.relative_to(ROOT).as_posix()
            if rel in ALLOW_FILES:
                continue
            text = path.read_text(encoding="utf-8")
            if rel.endswith("MODULE.md"):
                rows = _routing_lines(path, text)
            else:
                rows = list(enumerate(text.splitlines(), 1))
            for i, line in rows:
                if HIST_LINE.search(line):
                    continue
                for rid in retired:
                    if re.search(
                        r"(?<![A-Za-z0-9_./-])" + re.escape(rid) + r"(?![A-Za-z0-9_-])",
                        line,
                    ):
                        violations.append(f"{rel}:{i}: {rid} :: {line.strip()[:100]}")
        self.assertEqual(violations, [], "live retired-id mentions:\n" + "\n".join(violations[:40]))
class NoRetiredSeat04(unittest.TestCase):
    def test_folder_is_gone(self) -> None:
        self.assertFalse((ROOT / "04_analysis").exists(), "04_analysis retired into 02_data-processing")
        self.assertTrue((ROOT / "02_data-processing" / "SKILL.md").is_file())
        for pack in ("stats-analysis", "plot-figures", "draw-flowchart", "calc-sample-size"):
            self.assertTrue((ROOT / "02_data-processing" / "base" / pack).is_dir(), pack)
            self.assertTrue(
                (ROOT / "02_data-processing" / "advanced" / "analysis" / "route.md").is_file()
            )

    def test_no_stale_references(self) -> None:
        violations: list[str] = []
        for rel in tracked_files():
            if rel in no_retired_seat_04_ALLOW_FILES or rel.startswith(SKIP_PREFIXES):
                continue
            if Path(rel).suffix.lower() not in SUFFIXES:
                continue
            path = ROOT / rel
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for label, pattern in PATTERNS:
                for m in pattern.finditer(text):
                    line_no = text.count("\n", 0, m.start()) + 1
                    violations.append(f"{rel}:{line_no}: {label} {m.group(0)}")
        self.assertEqual(violations, [], "stale 04 seat references:\n" + "\n".join(violations[:40]))

    def test_no_duplicate_seat_forms(self) -> None:
        violations: list[str] = []
        for rel in tracked_files():
            if rel.startswith(SKIP_PREFIXES) or Path(rel).suffix.lower() not in SUFFIXES:
                continue
            path = ROOT / rel
            if not path.is_file():
                continue
            for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
                if DUP_FORM.search(line):
                    violations.append(f"{rel}:{i}: {line.strip()[:100]}")
        self.assertEqual(violations, [], "duplicate 02 seat forms:\n" + "\n".join(violations[:40]))
class NoBPackResidue(unittest.TestCase):
    def test_no_live_b_pack_residue(self) -> None:
        violations: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file():
                continue
            if path.suffix.lower() not in {".md", ".yaml", ".yml", ".py", ".txt"}:
                continue
            if any(part in {".git", "__pycache__", ".pytest_cache"} for part in path.parts):
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel in no_b_pack_residue_ALLOW_FILES or rel.startswith(("_", "tests/")):
                continue
            if rel.endswith("test_no_b_pack_residue.py"):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for i, line in enumerate(text.splitlines(), 1):
                if not B_PAT.search(line):
                    continue
                if ALLOW_LINE.search(line):
                    continue
                violations.append(f"{rel}:{i}: {line.strip()[:120]}")
        self.assertEqual(
            violations,
            [],
            "B-pack residue outside allowlist:\n" + "\n".join(violations[:40]),
        )
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
    def test_schema_names_fine_id_provenance_fields(self) -> None:
        fields = ["fine_id", "source", "resolved_commit", "path", "content_hash", "checked_at"]
        for rel in (
            "00_orchestrator/templates/project-state.yaml",
            "00_orchestrator/templates/handoff.yaml",
            "00_orchestrator/gates.md",
        ):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertIn("fine_id_provenance", text, rel)
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
        block = (ROOT / "00_orchestrator" / "references" / "id-rules.md").read_text(encoding="utf-8")
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
        header = (ROOT / "00_orchestrator" / "registry.yaml").read_text(encoding="utf-8").split("meta:", 1)[0]
        self.assertIn("Canonical ID Rule", header)
        self.assertIn("must never be used to infer", header)
        rad = (ROOT / "00_orchestrator" / "workflows" / "statistics.md").read_text(encoding="utf-8")
        self.assertLess(rad.index("`clean-data`"), rad.index("`preprocess-imaging`"))
        self.assertLess(rad.index("`preprocess-imaging`"), rad.index("`stats-analysis`"))
        self.assertNotIn("`radiomics-ml`", rad)
        for banned in ("02-tables", "02-imaging-qc", "02-radiomics-habitat"):
            self.assertNotIn(banned, rad)
        aliases = yaml.safe_load((ROOT / "00_orchestrator" / "legacy_aliases.yaml").read_text(encoding="utf-8"))["aliases"]
        self.assertEqual(aliases["02-tables"], "clean-data")
