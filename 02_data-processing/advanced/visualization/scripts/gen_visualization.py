#!/usr/bin/env python3
"""Read-only visualization compiler for MY-SKILLS.

Reads registry, preset metadata, and 00 runtime-flow. Writes the typed JSON IR and
generated HTML under the output dir given by --out or env MY_SKILLS_VIZ_OUT
(required; no default, exits non-zero if neither is set). Does not write into
the MY-SKILLS repo (no in-repo docs/ tree). Renders diagrams locally from the IR;
no external renderer package is fetched, unpacked, or verified.

Shape checks use fixed IR schema versions (architecture 1, workflow 2). This
script is a mapping checker, not a copy of any external schema.

workflow_ir() is a hand-maintained typed IR: a structured map of
00_orchestrator/runtime-flow.mmd (and prose anchors in runtime-flow.md), not an
auto-parsed Mermaid AST. require_runtime_ir_mapping() checks key node/edge/Gate/
branch anchors against that map; semantic drift still needs human review.

Usage:
    python3 02_data-processing/advanced/visualization/scripts/gen_visualization.py --out DIR
    python3 02_data-processing/advanced/visualization/scripts/gen_visualization.py --check
    python3 02_data-processing/advanced/visualization/scripts/gen_visualization.py \
        --delta-against /path/to/base/viz --delta-out /tmp/delta.html
"""
from __future__ import annotations

import argparse
import os
import datetime as dt
import hashlib
import html
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
VIZ_DIR = HERE.parent  # 02_data-processing/advanced/visualization
ROOT = VIZ_DIR.parent.parent.parent  # MY-SKILLS repo root
REGISTRY = ROOT / "00_orchestrator" / "registry.yaml"
RUNTIME_MMD = ROOT / "00_orchestrator" / "runtime-flow.mmd"
RUNTIME_MD = ROOT / "00_orchestrator" / "runtime-flow.md"
GATES = ROOT / "00_orchestrator" / "gates.md"
ARCH_MD = ROOT / "ARCHITECTURE.md"
CONTRACT = VIZ_DIR / "visualization-source-contract.yaml"




def resolve_viz_out(cli_out: Path | None = None) -> Path | None:
    """Lab output root; enforced outside-repo (see require_path_outside_repo)."""
    return _resolve_viz_out(cli_out)


def out_fs_path(out: Path, rel: str) -> Path:
    """Map portable relative key onto lab OUT; refuse repo escapes."""
    return _out_fs_path(out, rel)



SKILL_TOPS = (
    "00_orchestrator",
    "02_data-processing",
    "03_research",
    "05_manuscript",
    "06_review",
    "07_response",
)
ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
TS_RE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
COMPONENT_TYPES = {
    "frontend",
    "backend",
    "database",
    "cloud",
    "security",
    "messagebus",
    "external",
}
EDGE_ROLES = {"main", "branch", "async", "return", "error"}
VARIANTS = {"default", "emphasis", "security", "dashed"}
FACT_KEYS = ("components", "connections", "nodes", "edges")
MMD_ANCHORS = (
    "Detect",
    "Lit05",
    "Lit06",
    "mid-entry",
    "02 exit",
    "Gate · 05",
    "Gate · 06",
    "Gate · 07",
    "Standalone lit",
    "Stats/figures exist",
    "existing manuscript",
    "session_picked_fine_ids",
    "citation-verify",
)
# Key runtime-flow.mmd tokens that must map into Workflow IR ids / labels.
# IR remains hand-authored; this is structural consistency, not a Mermaid parser.
RUNTIME_IR_NODE_MAP = (
    ("Lit05", "lit05"),
    ("Lit06", "lit06"),
    ("Lit07", "lit07"),
    ("P07", "p07"),
    ("GA07", "ga07"),
)
RUNTIME_IR_LABEL_NEEDLES = (
    "mid-entry",
    "G-07",
    "Gate · 07",
    "no new cites",
    "cites appear",
)
# runtime-flow.md must participate in G-VIZ-01 (not a dead read).
MD_ANCHORS = (
    "mid-enter",
    "Gate ·",
    "07",
    "response",
    "Lit05",
    "Lit06",
)
REBUILD = "python3 02_data-processing/advanced/visualization/scripts/gen_visualization.py"

CSS = """
:root {
  --bg: #f7f8fa; --surface: #fff; --border: #e2e5ea; --text: #1a1d24;
  --muted: #5b6270; --accent: #3b5bdb; --ok: #2f9e44; --warn: #e8890c; --danger: #c92a2a;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--text);
  font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
}
header, footer { background: var(--surface); padding: 20px 24px; }
header { border-bottom: 1px solid var(--border); }
footer { border-top: 1px solid var(--border); color: var(--muted); font-size: 14px; }
h1 { font-size: 31px; font-weight: 600; margin: 0 0 8px; }
h2 { font-size: 25px; font-weight: 600; margin: 28px 0 8px; }
nav a { margin-right: 14px; }
a { color: var(--accent); }
a:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
main { max-width: 1100px; margin: 0 auto; padding: 20px 24px 48px; }
.banner {
  background: #fff4e6; border: 1px solid var(--border); border-left: 4px solid var(--warn);
  border-radius: 8px; padding: 12px 16px; margin: 16px 0;
}
.card {
  background: var(--surface); border: 1px solid var(--border); border-radius: 8px;
  padding: 16px; margin: 12px 0;
}
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; }
table { width: 100%; border-collapse: collapse; background: var(--surface); }
th, td { border: 1px solid var(--border); padding: 8px 10px; text-align: left; vertical-align: top; }
th { background: #eef1f6; font-weight: 600; }
code { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: 14px; }
.muted { color: var(--muted); }
dl { display: grid; grid-template-columns: 220px 1fr; gap: 6px 12px; }
dt { color: var(--muted); }
@media (prefers-reduced-motion: reduce) { * { transition: none; } }
@media print { nav { display: none; } body { background: #fff; } }
"""


class GateFailure(Exception):
    def __init__(self, gate: str, message: str) -> None:
        self.gate = gate
        super().__init__(f"{gate}: {message}")


def require_path_outside_repo(path: Path, *, what: str) -> Path:
    """Resolve path and refuse if it lands inside (or is) the MY-SKILLS repo.

    Rejects symlink escapes: the realpath after resolve() must stay outside ROOT.
    """
    resolved = path.expanduser().resolve()
    repo = ROOT.resolve()
    try:
        resolved.relative_to(repo)
    except ValueError:
        return resolved
    raise GateFailure(
        "G-VIZ-01",
        f"{what} resolves inside the MY-SKILLS repo ({resolved}); "
        "use a path outside the repo",
    )


def _resolve_viz_out(cli_out: Path | None = None) -> Path | None:
    """Lab output root for generated HTML/IR (not inside the MY-SKILLS repo).

    Order: --out, MY_SKILLS_VIZ_OUT. No default: without either,
    return None so --check can stay in-memory / skip disk compare.
    --out / MY_SKILLS_VIZ_OUT must resolve outside the repo.
    """
    if cli_out is not None:
        return require_path_outside_repo(cli_out, what="--out")
    env = os.environ.get("MY_SKILLS_VIZ_OUT", "").strip()
    if env:
        return require_path_outside_repo(Path(env), what="MY_SKILLS_VIZ_OUT")
    return None


def _out_fs_path(out: Path, rel: str) -> Path:
    """Map a portable relative key onto the lab OUT root; refuse repo escapes."""
    target = out / rel
    parent = target.parent
    if parent.exists():
        require_path_outside_repo(parent, what=f"write target parent for {rel}")
        candidate = parent.resolve() / target.name
    else:
        cur = target
        parts: list[str] = []
        while not cur.exists() and cur != cur.parent:
            parts.append(cur.name)
            cur = cur.parent
        if cur.exists():
            candidate = cur.resolve().joinpath(*reversed(parts))
        else:
            candidate = target.expanduser().resolve()
    return require_path_outside_repo(candidate, what=f"write target for {rel}")


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(read_text(path))
    if not isinstance(data, dict):
        raise GateFailure("G-VIZ-01", f"{path} did not parse as a mapping")
    return data


def dump_json(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def normalize(text: str) -> str:
    return TS_RE.sub("@@GENERATED_AT@@", text)


def skill_files() -> list[Path]:
    found: list[Path] = []
    for path in ROOT.rglob("SKILL.md"):
        if any(part in {".git", "docs", "__pycache__"} for part in path.parts):
            continue
        top = path.relative_to(ROOT).parts[0]
        if top not in SKILL_TOPS:
            raise GateFailure("G-VIZ-01", f"SKILL.md outside 00-07: {path}")
        found.append(path)
    return sorted(found, key=lambda p: (SKILL_TOPS.index(p.relative_to(ROOT).parts[0]), p.as_posix()))


def frontmatter(path: Path) -> dict:
    text = read_text(path)
    if not text.startswith("---"):
        raise GateFailure("G-VIZ-01", f"missing frontmatter: {path}")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise GateFailure("G-VIZ-01", f"unclosed frontmatter: {path}")
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict) or not str(data.get("name", "")).strip():
        raise GateFailure("G-VIZ-01", f"frontmatter name missing: {path}")
    return data


def source_paths() -> list[Path]:
    paths = [
        REGISTRY,
        RUNTIME_MMD,
        RUNTIME_MD,
        GATES,
        ARCH_MD,
        CONTRACT,
    ]
    paths = [p for p in paths if p.is_file()]
    paths.extend(skill_files())
    return paths


def fingerprint(paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(read_text(path).encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def require_anchors(mmd: str, gates: str, architecture: str, runtime_md: str = "") -> None:
    missing = [token for token in MMD_ANCHORS if token not in mmd]
    if missing:
        raise GateFailure("G-VIZ-01", "runtime-flow.mmd missing " + ", ".join(missing))
    for token in ("G0", "G-LIT", "G-05", "G-06", "G-07"):
        if token not in gates:
            raise GateFailure("G-VIZ-01", f"gates.md missing {token}")
    md_missing = [token for token in MD_ANCHORS if token not in runtime_md]
    if md_missing:
        raise GateFailure(
            "G-VIZ-01",
            "runtime-flow.md missing " + ", ".join(md_missing),
        )
    for folder in SKILL_TOPS:
        if folder not in architecture:
            raise GateFailure("G-VIZ-01", f"ARCHITECTURE.md missing {folder}")
        if not (ROOT / folder).is_dir():
            raise GateFailure("G-VIZ-01", f"missing directory {folder}")
    for entry in ROOT.iterdir():
        if entry.is_dir() and entry.name.startswith("07") and entry.name != "07_response":
            raise GateFailure("G-VIZ-01", f"unexpected top-level 07 skill: {entry.name}")


def require_runtime_ir_mapping(mmd: str, wf: dict) -> None:
    """Check key runtime-flow.mmd anchors appear as Workflow IR nodes/labels.

    workflow_ir() is the structured map of runtime-flow; this is not a full
    Mermaid parse. Unmapped semantic drift still needs human confirmation.
    """
    node_ids = {n["id"] for n in wf["nodes"]}
    for mmd_token, ir_id in RUNTIME_IR_NODE_MAP:
        if mmd_token not in mmd:
            raise GateFailure("G-VIZ-01", f"runtime-flow.mmd missing map token {mmd_token}")
        if ir_id not in node_ids:
            raise GateFailure(
                "G-VIZ-02",
                f"Workflow IR missing node {ir_id} mapped from runtime {mmd_token}",
            )
    label_blob = " | ".join(
        f"{n.get('id', '')} {n.get('label', '')} {n.get('sublabel', '')}" for n in wf["nodes"]
    )
    edge_blob = " | ".join(str(e.get("label", "")) for e in wf["edges"])
    blob = f"{label_blob} || {edge_blob}"
    for needle in RUNTIME_IR_LABEL_NEEDLES:
        if needle not in blob:
            raise GateFailure(
                "G-VIZ-02",
                f"Workflow IR missing runtime branch/Gate label {needle!r}",
            )
    # Branch: optional 06→07; 07 completion via G-07; conditional G-LIT (Lit07).
    pairs = {(e["from"], e["to"]) for e in wf["edges"]}
    for frm, to in (
        ("p06", "p07"),
        ("p07", "ga07"),
        ("p07", "lit07"),
        ("lit07", "ga07"),
        ("ga07", "done"),
    ):
        if (frm, to) not in pairs:
            raise GateFailure("G-VIZ-02", f"runtime mapping missing edge {frm} -> {to}")


def check_registry(reg: dict) -> None:
    fine_ids = reg.get("fine_ids") or []
    meta = reg.get("meta") or {}
    if len(fine_ids) != meta.get("fine_id_count_canonical"):
        raise GateFailure(
            "G-VIZ-01",
            f"fine_id count {len(fine_ids)} != fine_id_count_canonical {meta.get('fine_id_count_canonical')}",
        )
    for fine_id in fine_ids:
        if fine_id.get("source") != "my-skills":
            raise GateFailure("G-VIZ-01", f"fine id {fine_id.get('id')} is not an in-repo body")
        path = str(fine_id.get("path") or "")
        if not any(path.startswith(top + "/") for top in SKILL_TOPS):
            raise GateFailure("G-VIZ-01", f"fine id {fine_id.get('id')} path is outside 00-07")


def check_contract(contract: dict) -> None:
    phrases = contract.get("forbidden_fact_sources") or []
    required = [
        "LLM inference",
        "generated HTML",
        "previous generated HTML",
        "arbitrary external-file crawling",
        "filename alone",
        "visual appearance",
        "unvalidated JSON",
    ]
    for phrase in required:
        if phrase not in phrases:
            raise GateFailure("G-VIZ-01", f"contract missing forbidden source {phrase!r}")


def _box(row: int, col: int) -> dict:
    return {"row": row, "col": col, "size": [188, 64]}


def architecture_ir() -> dict:
    components = [
        {"id": "c00", "type": "security", "label": "00 Control", "sublabel": "gate and QC", **_box(0, 0)},
        {"id": "c01", "type": "backend", "label": "00 Index", "sublabel": "registry / workflows", **_box(0, 1)},
        {"id": "fine_ids", "type": "backend", "label": "Fine ids", "sublabel": "in-repo registry", **_box(0, 2)},
        {"id": "c02", "type": "backend", "label": "02 Data / Stats", "sublabel": "processing and figures", **_box(1, 0)},
        {"id": "c03", "type": "backend", "label": "03 Literature", "sublabel": "citation-verify", **_box(1, 1)},
        {"id": "c05", "type": "backend", "label": "05 Writing", "sublabel": "manuscript", **_box(1, 2)},
        {"id": "c06", "type": "backend", "label": "06 Review", "sublabel": "review", **_box(2, 0)},
        {"id": "c07", "type": "backend", "label": "07 Response", "sublabel": "response letter", **_box(2, 1)},
        {"id": "rules", "type": "backend", "label": "MY-RULES", "sublabel": "skill-evolution", **_box(2, 2)},
    ]
    return {
        "schema_version": 1,
        "diagram_type": "architecture",
        "meta": {
            "title": "MY-SKILLS Architecture",
            "subtitle": "Source, registry, skills, QC",
            "locale": "zh-CN",
            "output": "architecture/status.html",
        },
        "layout": {
            "mode": "grid",
            "cols": 3,
            "origin": [48, 88],
            "gapX": 140,
            "gapY": 100,
            "cellW": 200,
            "cellH": 72,
        },
        "components": components,
        "boundaries": [
            {
                "kind": "region",
                "label": "A ownership",
                "wraps": ["c00", "c01", "c02", "c03", "c05", "c06", "c07", "rules"],
            },
            {
                "kind": "region",
                "label": "Fine-id registry (in-repo)",
                "wraps": ["fine_ids"],
            },
        ],
        "connections": [
            {"id": "need-fine_id", "from": "c00", "to": "c01", "label": "fine ids if needed"},
            {"id": "index-fine_ids", "from": "c01", "to": "fine_ids", "label": "pointers"},
            {"id": "dispatch-02", "from": "c00", "to": "c02", "label": "dispatch"},
            {"id": "dispatch-03", "from": "c00", "to": "c03", "label": "dispatch"},
            {"id": "dispatch-05", "from": "c00", "to": "c05", "label": "dispatch"},
            {"id": "dispatch-06", "from": "c00", "to": "c06", "label": "dispatch"},
            {"id": "results-05", "from": "c02", "to": "c05", "label": "results"},
            {"id": "lit05", "from": "c03", "to": "c05", "label": "Lit05"},
            {"id": "lit06", "from": "c03", "to": "c06", "label": "Lit06", "labelDy": 24},
            {"id": "manuscript-06", "from": "c05", "to": "c06", "label": "manuscript"},
            {"id": "dispatch-07", "from": "c00", "to": "c07", "label": "dispatch"},
            {"id": "revise-07", "from": "c06", "to": "c07", "label": "response"},
            {"id": "propose", "from": "rules", "to": "c01", "label": "proposal", "variant": "dashed", "labelDy": 21},
        ],
    }


def workflow_ir() -> dict:
    lanes = [
        {"id": "control", "label": "00 control"},
        {"id": "fine_id", "label": "fine ids"},
        {"id": "produce", "label": "Domain chain"},
        {"id": "literature", "label": "03 literature"},
        {"id": "qc", "label": "QC loop", "variant": "exception"},
    ]

    def node(node_id: str, lane: str, col: int, kind: str, label: str, sublabel: str) -> dict:
        return {
            "id": node_id,
            "lane": lane,
            "col": col,
            "type": kind,
            "label": label,
            "sublabel": sublabel,
            "width": 176,
            "height": 64,
        }

    nodes = [
        node("task", "control", 0, "external", "Task", "entry"),
        node("detect", "control", 1, "security", "00 Detect", "gate"),
        node("single", "control", 4, "backend", "One domain", "named entry"),
        node("done", "control", 6, "backend", "Done", "terminal PASS"),
        node("fine_id_check", "fine_id", 1, "security", "Fine ids", "coverage"),
        node("s_pick", "fine_id", 3, "backend", "Fine ids", "session-pick"),
        node("dispatch", "fine_id", 2, "backend", "Dispatch", "after G0"),
        node("p02", "produce", 2, "backend", "02 Data", "processing"),
        node("p02_stats", "produce", 3, "backend", "02 Statistics", "figures"),
        node("p05", "produce", 4, "backend", "05 Writing", "manuscript"),
        node("p06", "produce", 5, "backend", "06 Review", "review"),
        node("p07", "produce", 6, "backend", "07 Response", "response letter"),
        node("p03", "literature", 2, "backend", "03 Literature", "evidence"),
        node("lit05", "literature", 4, "security", "Lit05", "G-CIT-1 before Gate 05"),
        node("lit06", "literature", 5, "security", "Lit06", "G-CIT-2 inside 06"),
        node("lit07", "literature", 3, "security", "Lit07", "G-LIT when cites"),
        node("ga07", "literature", 6, "security", "Gate · 07", "G-07 response"),
        node("locate", "qc", 1, "security", "Locate", "failed node"),
        node("rework", "qc", 3, "security", "Rework", "local or rollback"),
        node("escalate", "qc", 5, "security", "Unresolved", "budget spent"),
    ]
    edges = [
        {"id": "e-task-detect", "from": "task", "to": "detect", "label": "task enters", "role": "main"},
        {"id": "e-detect-fine_id", "from": "detect", "to": "fine_id_check", "label": "before specialist", "role": "main"},
        {"id": "e-fine_id-gap", "from": "fine_id_check", "to": "s_pick", "label": "fine ids missing", "role": "branch"},
        {"id": "e-g0-pass", "from": "s_pick", "to": "dispatch", "label": "G0 PASS", "role": "main"},
        {"id": "e-g0-fail", "from": "s_pick", "to": "locate", "label": "G0 FAIL", "role": "error"},
        {"id": "e-covered", "from": "fine_id_check", "to": "dispatch", "label": "fine ids already covered", "role": "main"},
        {"id": "e-d02", "from": "dispatch", "to": "p02", "label": "entry 02", "role": "branch"},
        {"id": "e-d03", "from": "dispatch", "to": "p03", "label": "entry 03 independent literature", "role": "branch"},
        {"id": "e-d02_stats", "from": "dispatch", "to": "p02_stats", "label": "entry 02 stats or mid-entry", "role": "branch"},
        {"id": "e-d05", "from": "dispatch", "to": "p05", "label": "entry 05 or mid-entry", "role": "branch"},
        {"id": "e-d06", "from": "dispatch", "to": "p06", "label": "entry 06 or mid-entry", "role": "branch"},
        {"id": "e-d07", "from": "dispatch", "to": "p07", "label": "entry 07 or mid-entry", "role": "branch"},
        {"id": "e-dsingle", "from": "dispatch", "to": "single", "label": "named single domain", "role": "branch"},
        {"id": "e-02-stats", "from": "p02", "to": "p02_stats", "label": "02 exit PASS, not terminal", "role": "main"},
        {"id": "e-stats-05", "from": "p02_stats", "to": "p05", "label": "Gate 02 PASS, not terminal", "role": "main"},
        {"id": "e-05-lit", "from": "p05", "to": "lit05", "label": "required before Gate 05", "role": "main"},
        {"id": "e-lit-06", "from": "lit05", "to": "p06", "label": "Gate 05 PASS, not terminal", "role": "main"},
        {"id": "e-06-lit", "from": "p06", "to": "lit06", "label": "required inside 06", "role": "main"},
        {"id": "e-lit-done", "from": "lit06", "to": "done", "label": "Gate 06 PASS at terminal", "role": "main"},
        {"id": "e-06-07", "from": "p06", "to": "p07", "label": "optional response (06 to 07 conditional; not every review)", "role": "branch", "variant": "dashed"},
        {"id": "e-07-ga07", "from": "p07", "to": "ga07", "label": "no new cites", "role": "branch", "variant": "dashed"},
        {"id": "e-07-lit07", "from": "p07", "to": "lit07", "label": "cites appear", "role": "branch"},
        {"id": "e-lit07-ga07", "from": "lit07", "to": "ga07", "label": "G-LIT PASS", "role": "branch"},
        {"id": "e-ga07-done", "from": "ga07", "to": "done", "label": "G-07 PASS", "role": "branch"},
        {"id": "e-03-05", "from": "p03", "to": "p05", "label": "evidence does not replace Lit05", "role": "branch", "variant": "dashed"},
        {"id": "e-03-06", "from": "p03", "to": "p06", "label": "evidence does not replace Lit06", "role": "branch", "variant": "dashed"},
        {"id": "e-02-done", "from": "p02", "to": "done", "label": "terminal PASS", "role": "branch"},
        {"id": "e-03-done", "from": "p03", "to": "done", "label": "terminal PASS", "role": "branch"},
        {"id": "e-stats-done", "from": "p02_stats", "to": "done", "label": "terminal PASS", "role": "branch"},
        {"id": "e-lit05-done", "from": "lit05", "to": "done", "label": "Gate 05 terminal PASS", "role": "branch"},
        {"id": "e-single-done", "from": "single", "to": "done", "label": "target gate PASS", "role": "branch"},
        {"id": "e-fail-02", "from": "p02", "to": "locate", "label": "02 exit FAIL", "role": "error"},
        {"id": "e-fail-03", "from": "p03", "to": "locate", "label": "03 exit FAIL", "role": "error"},
        {"id": "e-fail-stats", "from": "p02_stats", "to": "locate", "label": "Gate 02 FAIL", "role": "error"},
        {"id": "e-fail-lit05", "from": "lit05", "to": "locate", "label": "Lit05 FAIL", "role": "error"},
        {"id": "e-fail-06", "from": "p06", "to": "locate", "label": "Gate 06 FAIL", "role": "error"},
        {"id": "e-fail-07", "from": "ga07", "to": "locate", "label": "G-07 FAIL", "role": "error"},
        {"id": "e-fail-lit06", "from": "lit06", "to": "locate", "label": "Lit06 FAIL", "role": "error"},
        {"id": "e-fail-lit07", "from": "lit07", "to": "locate", "label": "Lit07 / G-LIT FAIL", "role": "error"},
        {"id": "e-fail-single", "from": "single", "to": "locate", "label": "target gate FAIL", "role": "error"},
        {"id": "e-locate-rework", "from": "locate", "to": "rework", "label": "local rework or rollback", "role": "error"},
        {"id": "e-rework-fine_id", "from": "rework", "to": "fine_id_check", "label": "reuse session lock or re-enter 00 session-pick", "role": "return"},
        {"id": "e-locate-escalate", "from": "locate", "to": "escalate", "label": "budget exhausted", "role": "error"},
    ]
    return {
        "schema_version": 2,
        "diagram_type": "workflow",
        "meta": {
            "title": "MY-SKILLS Workflow",
            "subtitle": "Task, gates, fine ids, mid-entry, Lit05, Lit06, Lit07 (G-LIT when cites), optional 07 Response, QC loop",
            "locale": "zh-CN",
            "output": "workflow/status.html",
        },
        "lanes": lanes,
        "phases": [
            {"id": "intake", "label": "Detect", "fromCol": 0, "toCol": 0},
            {"id": "session", "label": "Fine id", "fromCol": 1, "toCol": 2},
            {"id": "domains", "label": "02-07", "fromCol": 3, "toCol": 6},
        ],
        "groups": [
            {"id": "forward", "label": "PASS forward", "lane": "produce", "fromCol": 2, "toCol": 6},
            {"id": "lit-gates", "label": "Lit05 Lit06 Lit07", "lane": "literature", "fromCol": 3, "toCol": 5},
            {"id": "qc-loop", "label": "QC loop", "lane": "qc", "fromCol": 3, "toCol": 6, "variant": "dashed"},
        ],
        "mainPath": ["task", "detect", "fine_id_check", "dispatch", "p02", "p02_stats", "p05", "lit05", "p06", "lit06", "done"],
        "semanticChecks": {
            "allowedRoots": ["task"],
            "allowedTerminals": ["done", "escalate"],
            "requiredEdges": [
                {"from": "p05", "to": "lit05"},
                {"from": "p06", "to": "lit06"},
                {"from": "dispatch", "to": "p03"},
                {"from": "dispatch", "to": "p02_stats"},
                {"from": "dispatch", "to": "p05"},
                {"from": "dispatch", "to": "p06"},
                {"from": "dispatch", "to": "p07"},
                {"from": "p06", "to": "p07"},
                {"from": "p07", "to": "ga07"},
                {"from": "p07", "to": "lit07"},
                {"from": "lit07", "to": "ga07"},
                {"from": "ga07", "to": "done"},
            ],
            "requiredPaths": [
                {"from": "task", "to": "done"},
                {"from": "task", "to": "p03"},
                {"from": "p05", "to": "lit05"},
                {"from": "p06", "to": "lit06"},
                {"from": "p07", "to": "ga07"},
                {"from": "p07", "to": "done"},
            ],
        },
        "nodes": nodes,
        "edges": edges,
    }


def _check_id(value: str, where: str) -> None:
    if not ID_RE.match(value):
        raise GateFailure("G-VIZ-02", f"bad id {value!r} at {where}")


def _check_output(path: str) -> None:
    if not re.match(r"^[^/]+(?:/[^/]+)*$", path) or not path.endswith(".html"):
        raise GateFailure("G-VIZ-02", f"meta.output is not a portable html path: {path}")
    if any(part in {".", ".."} for part in path.split("/")):
        raise GateFailure("G-VIZ-02", f"meta.output has a dot segment: {path}")



def _enforce_must_show(wf: dict) -> None:
    """Apply visualization-source-contract.yaml views.workflow.must_show to the IR."""
    contract = read_yaml(CONTRACT)
    must = ((contract.get("views") or {}).get("workflow") or {}).get("must_show") or []
    if not must:
        raise GateFailure("G-VIZ-02", "source contract workflow.must_show is empty")
    label_blob = " | ".join(
        f"{n.get('id', '')} {n.get('label', '')} {n.get('sublabel', '')}" for n in wf["nodes"]
    )
    edge_blob = " | ".join(str(e.get("label", "")) for e in wf["edges"])
    blob = f"{label_blob} || {edge_blob}"
    for item in must:
        spec = str(item).strip()
        if spec.startswith("layers 00 through 07"):
            for layer, needle in (
                ("00", "00 "),
                ("02", "02 "),
                ("03", "03 "),
                ("05", "05 "),
                ("06", "06 "),
                ("07", "07 "),
            ):
                if needle not in label_blob:
                    raise GateFailure(
                        "G-VIZ-02",
                        f"must_show missing layer {layer} node (need label containing {needle!r})",
                    )
            continue
        if spec not in blob:
            raise GateFailure("G-VIZ-02", f"must_show missing {spec!r} in workflow IR")


def validate_ir(arch: dict, wf: dict) -> None:
    if arch.get("schema_version") != 1 or arch.get("diagram_type") != "architecture":
        raise GateFailure("G-VIZ-02", "architecture schema_version or diagram_type mismatch")
    if wf.get("schema_version") != 2 or wf.get("diagram_type") != "workflow":
        raise GateFailure("G-VIZ-02", "workflow schema_version or diagram_type mismatch")
    for doc, kind in ((arch, "architecture"), (wf, "workflow")):
        meta = doc.get("meta") or {}
        if not meta.get("title") or not meta.get("output"):
            raise GateFailure("G-VIZ-02", f"{kind} meta requires title and output")
        _check_output(meta["output"])
    components = arch["components"]
    if not 6 <= len(components) <= 12:
        raise GateFailure("G-VIZ-02", f"architecture component count {len(components)} outside 6-12")
    ids = [c["id"] for c in components]
    if len(ids) != len(set(ids)):
        raise GateFailure("G-VIZ-02", "duplicate architecture component id")
    for comp in components:
        _check_id(comp["id"], "component")
        if comp["type"] not in COMPONENT_TYPES or not comp.get("label"):
            raise GateFailure("G-VIZ-02", f"bad component {comp['id']}")
        label = str(comp["label"])
        if label.startswith("07") and not (
            label.startswith("07_response") or "response" in label.lower()
        ):
            raise GateFailure("G-VIZ-02", f"unexpected architecture 07 label: {label}")
    known = set(ids)
    for boundary in arch["boundaries"]:
        if boundary["kind"] not in {"region", "security-group"}:
            raise GateFailure("G-VIZ-02", "bad boundary kind")
        if not boundary.get("wraps"):
            raise GateFailure("G-VIZ-02", "boundary wraps is empty")
        for item in boundary["wraps"]:
            if item not in known:
                raise GateFailure("G-VIZ-02", f"boundary wraps unknown id {item}")
    conn_ids = [c["id"] for c in arch["connections"]]
    if len(conn_ids) != len(set(conn_ids)):
        raise GateFailure("G-VIZ-02", "duplicate architecture connection id")
    for conn in arch["connections"]:
        _check_id(conn["id"], "connection")
        if conn["from"] not in known or conn["to"] not in known:
            raise GateFailure("G-VIZ-02", f"connection {conn['id']} endpoint missing")
        if "variant" in conn and conn["variant"] not in VARIANTS:
            raise GateFailure("G-VIZ-02", f"bad connection variant {conn['id']}")
    lanes = {lane["id"] for lane in wf["lanes"]}
    if len(lanes) != len(wf["lanes"]):
        raise GateFailure("G-VIZ-02", "duplicate workflow lane")
    seen_slot = set()
    node_ids = set()
    node_id_list = []
    for node in wf["nodes"]:
        _check_id(node["id"], "node")
        node_id_list.append(node["id"])
        if node["lane"] not in lanes:
            raise GateFailure("G-VIZ-02", f"node {node['id']} lane missing")
        if not isinstance(node["col"], int) or not 0 <= node["col"] <= 6:
            raise GateFailure("G-VIZ-02", f"node {node['id']} col out of range")
        if node["type"] not in COMPONENT_TYPES or not node.get("label"):
            raise GateFailure("G-VIZ-02", f"bad node {node['id']}")
        slot = (node["lane"], node["col"])
        if slot in seen_slot:
            raise GateFailure("G-VIZ-02", f"duplicate lane/col {slot}")
        seen_slot.add(slot)
        node_ids.add(node["id"])
    if len(node_id_list) != len(node_ids):
        raise GateFailure("G-VIZ-02", "duplicate workflow node id")
    edge_id_list = []
    for edge in wf["edges"]:
        _check_id(edge["id"], "edge")
        edge_id_list.append(edge["id"])
        if edge["from"] not in node_ids or edge["to"] not in node_ids:
            raise GateFailure("G-VIZ-02", f"edge {edge['id']} endpoint missing")
        if edge.get("role") not in EDGE_ROLES:
            raise GateFailure("G-VIZ-02", f"edge {edge['id']} role missing")
        if "variant" in edge and edge["variant"] not in VARIANTS:
            raise GateFailure("G-VIZ-02", f"bad edge variant {edge['id']}")
    if len(edge_id_list) != len(set(edge_id_list)):
        raise GateFailure("G-VIZ-02", "duplicate workflow edge id")
    if len(wf["mainPath"]) < 2 or any(item not in node_ids for item in wf["mainPath"]):
        raise GateFailure("G-VIZ-02", "mainPath is not a list of node ids")
    edge_pairs = {(e["from"], e["to"]) for e in wf["edges"]}
    for left, right in zip(wf["mainPath"], wf["mainPath"][1:]):
        if (left, right) not in edge_pairs:
            raise GateFailure("G-VIZ-02", f"mainPath has no edge {left} -> {right}")
    for phase in wf["phases"] + wf["groups"]:
        if not 0 <= phase["fromCol"] <= phase["toCol"] <= 6:
            raise GateFailure("G-VIZ-02", f"bad column span {phase['id']}")
    for group in wf["groups"]:
        if group["lane"] not in lanes:
            raise GateFailure("G-VIZ-02", f"group lane missing {group['id']}")
    checks = wf["semanticChecks"]
    allowed_roots = set(checks["allowedRoots"])
    allowed_terminals = set(checks["allowedTerminals"])
    for key in ("allowedRoots", "allowedTerminals"):
        if any(item not in node_ids for item in checks[key]):
            raise GateFailure("G-VIZ-02", f"semanticChecks.{key} references an unknown node")
    for rel in checks["requiredEdges"]:
        if rel["from"] not in node_ids or rel["to"] not in node_ids:
            raise GateFailure("G-VIZ-02", "semanticChecks relation references an unknown node")
        if (rel["from"], rel["to"]) not in edge_pairs:
            raise GateFailure("G-VIZ-02", f"required edge missing {rel['from']} -> {rel['to']}")
    adj: dict[str, list[str]] = {nid: [] for nid in node_ids}
    indeg = {nid: 0 for nid in node_ids}
    outdeg = {nid: 0 for nid in node_ids}
    for edge in wf["edges"]:
        adj[edge["from"]].append(edge["to"])
        outdeg[edge["from"]] += 1
        indeg[edge["to"]] += 1

    def _reachable(src: str, dst: str) -> bool:
        seen = {src}
        stack = [src]
        while stack:
            cur = stack.pop()
            if cur == dst:
                return True
            for nxt in adj.get(cur, []):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return False

    def _reachable_any(src: str, targets: set[str]) -> bool:
        seen = {src}
        stack = [src]
        while stack:
            cur = stack.pop()
            if cur in targets:
                return True
            for nxt in adj.get(cur, []):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return False

    actual_roots = {nid for nid in node_ids if indeg[nid] == 0}
    actual_terminals = {nid for nid in node_ids if outdeg[nid] == 0}
    if actual_roots != allowed_roots:
        raise GateFailure(
            "G-VIZ-02",
            "allowedRoots mismatch: actual="
            + ", ".join(sorted(actual_roots))
            + " allowed="
            + ", ".join(sorted(allowed_roots)),
        )
    if actual_terminals != allowed_terminals:
        raise GateFailure(
            "G-VIZ-02",
            "allowedTerminals mismatch: actual="
            + ", ".join(sorted(actual_terminals))
            + " allowed="
            + ", ".join(sorted(allowed_terminals)),
        )

    # Non-isolated nodes must be reachable from an allowed entry root.
    from_roots: set[str] = set()
    stack = list(allowed_roots & node_ids)
    from_roots.update(stack)
    while stack:
        cur = stack.pop()
        for nxt in adj.get(cur, []):
            if nxt not in from_roots:
                from_roots.add(nxt)
                stack.append(nxt)
    for nid in node_ids:
        if indeg[nid] + outdeg[nid] == 0:
            continue
        if nid not in from_roots and nid not in allowed_roots:
            raise GateFailure(
                "G-VIZ-02",
                f"non-isolated node {nid} not reachable from allowedRoots",
            )
        if nid in from_roots and not _reachable_any(nid, allowed_terminals):
            raise GateFailure(
                "G-VIZ-02",
                f"node {nid} cannot reach an allowedTerminal",
            )

    for rel in checks["requiredPaths"]:
        if rel["from"] not in node_ids or rel["to"] not in node_ids:
            raise GateFailure("G-VIZ-02", "semanticChecks relation references an unknown node")
        if not _reachable(rel["from"], rel["to"]):
            raise GateFailure(
                "G-VIZ-02",
                f"required path not reachable {rel['from']} -> {rel['to']}",
            )

    # P07 completion paths (main/branch only) must not bypass G-07.
    # Error/return edges are excluded so the QC loop cannot false-positive.
    if {"p07", "ga07", "done"} <= node_ids:
        adj_no_ga07: dict[str, list[str]] = {
            nid: [] for nid in node_ids if nid != "ga07"
        }
        for edge in wf["edges"]:
            if edge.get("role") not in {"main", "branch"}:
                continue
            if edge["from"] == "ga07" or edge["to"] == "ga07":
                continue
            if edge["from"] in adj_no_ga07:
                adj_no_ga07[edge["from"]].append(edge["to"])
        seen_b = {"p07"}
        stack_b = ["p07"]
        while stack_b:
            cur_b = stack_b.pop()
            if cur_b == "done":
                raise GateFailure(
                    "G-VIZ-02",
                    "p07 can reach done without ga07 (G-07 bypass)",
                )
            for nxt_b in adj_no_ga07.get(cur_b, []):
                if nxt_b not in seen_b:
                    seen_b.add(nxt_b)
                    stack_b.append(nxt_b)

    _enforce_must_show(wf)
    json.loads(dump_json(arch))
    json.loads(dump_json(wf))


def _unique_map(items: list, key: str, value_fn, kind: str) -> dict:
    out: dict = {}
    for item in items:
        item_id = item[key]
        if item_id in out:
            raise GateFailure("G-VIZ-02", f"duplicate {kind} id {item_id}")
        out[item_id] = value_fn(item)
    return out


def facts_from_ir(arch: dict, wf: dict) -> dict:
    return {
        "components": _unique_map(
            arch["components"], "id", lambda c: c["label"], "architecture component"
        ),
        "connections": _unique_map(
            arch["connections"],
            "id",
            lambda c: {"from": c["from"], "to": c["to"], "label": c.get("label", "")},
            "architecture connection",
        ),
        "nodes": _unique_map(wf["nodes"], "id", lambda n: n["label"], "workflow node"),
        "edges": _unique_map(
            wf["edges"],
            "id",
            lambda e: {"from": e["from"], "to": e["to"], "label": e.get("label", "")},
            "workflow edge",
        ),
    }


def empty_facts() -> dict:
    return {key: {} for key in FACT_KEYS}


def structural_delta(before: dict, after: dict) -> dict:
    added: dict = {}
    removed: dict = {}
    changed: dict = {}
    for key in FACT_KEYS:
        old = before.get(key) or {}
        new = after.get(key) or {}
        added[key] = sorted(set(new) - set(old))
        removed[key] = sorted(set(old) - set(new))
        rows = []
        for item in sorted(set(new) & set(old)):
            if old[item] != new[item]:
                rows.append({"id": item, "before": old[item], "after": new[item]})
        changed[key] = rows
    return {"added": added, "removed": removed, "changed": changed, "note": "structural facts only"}


def shell(title: str, body: str, version: str, digest: str, nav: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="generator" content="my-skills-visualization">
<title>{esc(title)}</title>
<style>{CSS}</style>
</head>
<body>
<!-- generated: true -->
<!-- rebuild: {REBUILD} -->
<!-- generated_at: @@GENERATED_AT@@ -->
<!-- ir_schema: architecture 1 / workflow 2 -->
<!-- source_fingerprint: {esc(digest)} -->
<!-- build_status: ir-shape-checked -->
<!-- ir-render: local -->
<!-- github_pages: not-published -->
<header>
  <h1>{esc(title)}</h1>
  <p class="muted">Generated artifact. Rebuild with <code>{esc(REBUILD)}</code>. Do not edit this file by hand.</p>
  <nav>{nav}</nav>
</header>
<main>
  <p class="banner">Generated @@GENERATED_AT@@. This page is HTML built directly from in-repo IR (no external renderer). Build status ir-shape-checked. GitHub Pages not published. Fact source is MY-SKILLS, not this page.</p>
  {body}
</main>
<footer>
  <p>source fingerprint <code>{esc(digest)}</code></p>
  <p>Design history is not the home page. Spec lives in <code>02_data-processing/advanced/visualization/visualization-architecture.md</code>。</p>
</footer>
</body>
</html>
"""


NAV = (
    '<a href="{home}">Home</a>'
    '<a href="{arch}">Architecture status</a>'
    '<a href="{wf}">Workflow status</a>'
    '<a href="{skills}">Skill index</a>'
    '<a href="{fine_ids}">Fine ids</a>'
    '<a href="{delta}">Delta</a>'
    '<a href="{history}">Design history</a>'
)


def nav_for(home: str, arch: str, wf: str, skills: str, fine_ids: str, delta: str, history: str) -> str:
    return NAV.format(home=home, arch=arch, wf=wf, skills=skills, fine_ids=fine_ids, delta=delta, history=history)


def render_status(title: str, intro: str, rows: list[tuple[str, str]], extra: str, version: str, digest: str, links: dict) -> str:
    body_rows = "".join(f"<tr><td><code>{esc(a)}</code></td><td>{esc(b)}</td></tr>" for a, b in rows)
    body = f"<p>{esc(intro)}</p><table><thead><tr><th>id</th><th>label</th></tr></thead><tbody>{body_rows}</tbody></table>{extra}"
    return shell(title, body, version, digest, nav_for(**links))


def render_skills(skills: list[dict], version: str, digest: str) -> dict[str, str]:
    files: dict[str, str] = {}
    grouped: dict[str, list[dict]] = {name: [] for name in SKILL_TOPS}
    for skill in skills:
        grouped[skill["top"]].append(skill)
        body = (
            f"<dl><dt>source</dt><dd><code>{esc(skill['path'])}</code></dd>"
            f"<dt>name</dt><dd><code>{esc(skill['name'])}</code></dd>"
            f"<dt>description</dt><dd>{esc(skill['description'])}</dd></dl>"
            "<p>Body text stays in source SKILL.md. This page takes frontmatter only; it does not draw the body as a diagram.</p>"
        )
        links = {
            "home": "../index.html",
            "arch": "../architecture/status.html",
            "wf": "../workflow/status.html",
            "skills": "index.html",
            "fine_ids": "../fine_ids/index.html",
            "delta": "../changes/latest-delta.html",
            "history": "../design-history/index.html",
        }
        files[f"skills/{skill['name']}.html"] = shell(
            skill["name"], body, version, digest, nav_for(**links)
        )
    sections = []
    for top in SKILL_TOPS:
        items = grouped[top]
        if not items:
            continue
        lis = "".join(
            f"<li><a href=\"{esc(item['name'])}.html\"><code>{esc(item['name'])}</code></a> "
            f"<span class=\"muted\">{esc(item['path'])}</span><br>{esc(item['description'])}</li>"
            for item in items
        )
        sections.append(f"<section><h2><code>{esc(top)}</code></h2><ul>{lis}</ul></section>")
    links = {
        "home": "../index.html",
        "arch": "../architecture/status.html",
        "wf": "../workflow/status.html",
        "skills": "index.html",
        "fine_ids": "../fine_ids/index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    files["skills/index.html"] = shell(
        "Skill index",
        "<p>Indexed by 00-07 (evolution policy: MY-RULES skills.md (skill-evolution)). Pages from SKILL.md frontmatter.</p>" + "".join(sections),
        version,
        digest,
        nav_for(**links),
    )
    return files


def render_fine_ids(reg: dict, sources: list[dict], presets: list[dict], version: str, digest: str) -> str:
    fine_ids = reg["fine_ids"]
    live = sum(1 for item in fine_ids if item.get("status") == "LIVE")
    proposed = sum(1 for item in fine_ids if item.get("status") == "PROPOSED")
    coarse_rows = []
    for coarse in reg.get("coarse_ids") or []:
        count = sum(1 for item in fine_ids if item.get("a_domain") == coarse.get("id"))
        domains = ", ".join(coarse.get("a_domains") or [])
        coarse_rows.append(
            f"<tr><td>{esc(coarse.get('id'))}</td><td><code>{esc(coarse.get('slug'))}</code></td>"
            f"<td>{esc(domains)}</td><td>{esc(coarse.get('specialist_hint'))}</td><td>{count}</td></tr>"
        )
    fine_id_rows = []
    for item in fine_ids:
        fine_id_rows.append(
            "<tr>"
            f"<td><code>{esc(item.get('id'))}</code></td>"
            f"<td>{esc(item.get('label'))}</td>"
            f"<td>{esc(item.get('source'))}</td>"
            f"<td>{esc(item.get('status'))}</td>"
            f"<td>{esc(item.get('atomic_package', ''))}</td>"
            f"<td>{esc(item.get('a_domain', ''))}</td>"
            f"<td>{esc(item.get('load_priority', ''))}</td>"
            f"<td><code>{esc(item.get('path', ''))}</code></td>"
            "</tr>"
        )
    proposal_rows = "".join(
        f"<tr><td><code>{esc(item.get('id'))}</code></td><td>{esc(item.get('status'))}</td>"
        f"<td>{esc(item.get('role'))}</td></tr>"
        for item in (reg.get("proposals") or [])
    )
    body = f"""
    <section class="card">
      <h2>In-repo index</h2>
      <p class="muted">LIVE {live} · PROPOSED {proposed} · fine ids {len(fine_ids)}. Counts come from registry.yaml. Bodies live under NN_slug/base/.</p>
    </section>
    <h2>Seats (coarse id = a_domain)</h2>
    <table><thead><tr><th>seat</th><th>slug</th><th>a_domains</th><th>specialist</th><th>fine ids</th></tr></thead>
    <tbody>{''.join(coarse_rows)}</tbody></table>
    <h2>Fine ids</h2>
    <table><thead><tr><th>id</th><th>label</th><th>source</th><th>status</th><th>package</th><th>a_domain</th><th>priority</th><th>registry path</th></tr></thead>
    <tbody>{''.join(fine_id_rows)}</tbody></table>
    <h2>Source records / presets</h2>
    <p class="muted">Retired: no <code>sources/</code> yaml seat and no <code>references/presets/</code>. Registry is SSOT.</p>
    <h2>Proposals</h2>
    <table><thead><tr><th>id</th><th>status</th><th>role</th></tr></thead><tbody>{proposal_rows}</tbody></table>
    """
    links = {
        "home": "../index.html",
        "arch": "../architecture/status.html",
        "wf": "../workflow/status.html",
        "skills": "../skills/index.html",
        "fine_ids": "index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    return shell("Registry index", body, version, digest, nav_for(**links))


def render_delta(delta: dict, after: dict, version: str, digest: str, before_label: str) -> str:
    def items(names: list) -> str:
        if not names:
            return "<p class=\"muted\">none</p>"
        return "<ul>" + "".join(f"<li><code>{esc(name)}</code></li>" for name in names) + "</ul>"

    def changed(rows: list) -> str:
        if not rows:
            return "<p class=\"muted\">none</p>"
        body = "".join(
            f"<tr><td><code>{esc(row['id'])}</code></td><td>{esc(json.dumps(row['before'], ensure_ascii=False))}</td>"
            f"<td>{esc(json.dumps(row['after'], ensure_ascii=False))}</td></tr>"
            for row in rows
        )
        return f"<table><thead><tr><th>id</th><th>before</th><th>after</th></tr></thead><tbody>{body}</tbody></table>"

    sections = []
    for key in FACT_KEYS:
        sections.append(
            f"<section><h2>{esc(key)}</h2>"
            f"<h3>Added</h3>{items(delta['added'][key])}"
            f"<h3>Removed</h3>{items(delta['removed'][key])}"
            f"<h3>Changed</h3>{changed(delta['changed'][key])}</section>"
        )
    after_rows = []
    for key in FACT_KEYS:
        for item_id, label in after[key].items():
            after_rows.append(f"<li><code>{esc(key)}</code> <code>{esc(item_id)}</code> {esc(label if isinstance(label, str) else json.dumps(label, ensure_ascii=False))}</li>")
    body = (
        f"<p>Before: {esc(before_label)}</p>"
        "<p>Delta lists structural identifier and label changes only. It does not assess merge risk, impact, or whether to merge.</p>"
        + "".join(sections)
        + "<h2>After</h2><ul>"
        + "".join(after_rows)
        + "</ul>"
    )
    links = {
        "home": "../index.html",
        "arch": "../architecture/status.html",
        "wf": "../workflow/status.html",
        "skills": "../skills/index.html",
        "fine_ids": "../fine_ids/index.html",
        "delta": "latest-delta.html",
        "history": "../design-history/index.html",
    }
    return shell("Architecture Delta", body, version, digest, nav_for(**links))


def load_sidecar_metadata() -> tuple[list[dict], list[dict]]:
    """Presets / sources/ yaml seats retired; registry.yaml is SSOT."""
    return [], []


def build() -> dict:
    contract = read_yaml(CONTRACT)
    check_contract(contract)
    reg = read_yaml(REGISTRY)
    check_registry(reg)
    mmd = read_text(RUNTIME_MMD)
    gates = read_text(GATES)
    architecture = read_text(ARCH_MD)
    runtime_md = read_text(RUNTIME_MD)
    require_anchors(mmd, gates, architecture, runtime_md)
    skills = []
    seen_names = set()
    for path in skill_files():
        data = frontmatter(path)
        name = str(data["name"]).strip()
        if name in seen_names:
            raise GateFailure("G-VIZ-01", f"duplicate skill name {name}")
        seen_names.add(name)
        description = re.sub(r"\s+", " ", str(data.get("description") or "")).strip()
        skills.append(
            {
                "name": name,
                "description": description,
                "path": path.relative_to(ROOT).as_posix(),
                "top": path.relative_to(ROOT).parts[0],
            }
        )
    sources, presets = load_sidecar_metadata()
    arch = architecture_ir()
    wf = workflow_ir()
    # Fixed IR schema versions: architecture 1, workflow 2 (see visualization-architecture.md).
    arch["schema_version"] = 1
    wf["schema_version"] = 2
    validate_ir(arch, wf)
    require_runtime_ir_mapping(mmd, wf)
    digest = fingerprint(source_paths())
    version = "local-ir"
    home_links = {
        "home": "index.html",
        "arch": "architecture/status.html",
        "wf": "workflow/status.html",
        "skills": "skills/index.html",
        "fine_ids": "fine_ids/index.html",
        "delta": "changes/latest-delta.html",
        "history": "design-history/index.html",
    }
    root_links = {
        "home": "../index.html",
        "arch": "status.html",
        "wf": "../workflow/status.html",
        "skills": "../skills/index.html",
        "fine_ids": "../fine_ids/index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    wf_links = {
        "home": "../index.html",
        "arch": "../architecture/status.html",
        "wf": "status.html",
        "skills": "../skills/index.html",
        "fine_ids": "../fine_ids/index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    comp_rows = [(c["id"], c["label"]) for c in arch["components"]]
    node_rows = [(n["id"], n["label"]) for n in wf["nodes"]]
    arch_extra = (
        "<p>This page is generated from in-repo IR with no external renderer. Fields below come from the same IR."
        " IR file: <a href=\"architecture.json\"><code>architecture.json</code></a>."
        f" schema_version {arch['schema_version']}. Fields: components / boundaries / connections.</p>"
    )
    wf_extra = (
        "<p>This page is generated from in-repo IR with no external renderer. Fields below come from the same IR."
        " IR file: <a href=\"runtime.workflow.json\"><code>runtime.workflow.json</code></a>."
        f" schema_version {wf['schema_version']}. Fields: lanes / phases / groups / mainPath / nodes / edges."
        " 03, 07 Response, Gate · 07 / G-07, Lit05, Lit06, and mid-entry appear on nodes and edges.</p>"
    )
    home_body = (
        "<div class=\"grid\">"
        "<section class=\"card\"><h2>Architecture</h2><p>System components and boundaries.</p>"
        "<p><a href=\"architecture/status.html\">Open Architecture status</a></p></section>"
        "<section class=\"card\"><h2>Workflow</h2><p>How tasks run, including mid-entry, Lit05, Lit06, and the QC loop.</p>"
        "<p><a href=\"workflow/status.html\">Open Workflow status</a></p></section>"
        "<section class=\"card\"><h2>Registry</h2>"
        "<p>Fine ids are indexed in registry.yaml. Bodies live in-repo under NN_slug/base/.</p>"
        "<p><a href=\"fine_ids/index.html\">Open registry index</a></p></section>"
        "<section class=\"card\"><h2>Skills</h2><p>Frontmatter pages for 00-07.</p>"
        "<p><a href=\"skills/index.html\">Open Skill index</a></p></section>"
        "</div>"
        "<h2>Build</h2><dl>"
        "<dt>schema_version</dt><dd>architecture 1 · workflow 2</dd>"
        "<dt>build_status</dt><dd>ir-shape-checked</dd>"
        "<dt>render</dt><dd>local (in-repo IR to HTML)</dd>"
        "<dt>github_pages</dt><dd>not-published</dd>"
        f"<dt>fingerprint</dt><dd><code>{esc(digest)}</code></dd>"
        "</dl>"
        "<p><a href=\"build-manifest.json\">build-manifest.json</a> · "
        "<a href=\"changes/latest-delta.html\">structural Delta</a></p>"
    )
    history_body = (
        "<p>This is not the docs home page. Home is <a href=\"../index.html\">index.html</a>.</p>"
        "<p>Approved spec: <a href=\"../../02_data-processing/advanced/visualization/visualization-architecture.md\">02_data-processing/advanced/visualization/visualization-architecture.md</a>。</p>"
        "<p>This index is written by the generator; the spec body is not a generated artifact.</p>"
    )
    after = facts_from_ir(arch, wf)
    delta = structural_delta(empty_facts(), after)
    manifest = {
        "generated": True,
        "rebuild_command": REBUILD,
        "generated_at": "@@GENERATED_AT@@",
        "schema_version": {"architecture": 1, "workflow": 2},
        "build_status": "ir-shape-checked",
        "render": "local",
        "github_pages": "not-published",
        "source_fingerprint": digest,
        "sources": [path.relative_to(ROOT).as_posix() for path in source_paths()],
    }
    files = {
        "build-manifest.json": dump_json(manifest),
        "architecture/architecture.json": dump_json(arch),
        "workflow/runtime.workflow.json": dump_json(wf),
        "index.html": shell("MY-SKILLS", home_body, version, digest, nav_for(**home_links)),
        "architecture/status.html": render_status(
            "Architecture IR status",
            "Stable system components from ARCHITECTURE.md and the 00-07 directories.",
            comp_rows,
            arch_extra,
            version,
            digest,
            root_links,
        ),
        "workflow/status.html": render_status(
            "Workflow IR status",
            "Structural mapping of runtime-flow.mmd, including mid-entry, Lit05, Lit06, optional 07 Response, and G-07.",
            node_rows,
            wf_extra,
            version,
            digest,
            wf_links,
        ),
        "fine_ids/index.html": render_fine_ids(reg, sources, presets, version, digest),
        "changes/latest-delta.html": render_delta(
            delta, after, version, digest, "none (no baseline snapshot supplied)"
        ),
        "design-history/index.html": shell(
            "Design history",
            history_body,
            version,
            digest,
            nav_for(
                home="../index.html",
                arch="../architecture/status.html",
                wf="../workflow/status.html",
                skills="../skills/index.html",
                fine_ids="../fine_ids/index.html",
                delta="../changes/latest-delta.html",
                history="index.html",
            ),
        ),
    }
    files.update(render_skills(skills, version, digest))
    return {
        "files": files,
        "architecture": arch,
        "workflow": wf,
        "version": version,
        "fingerprint": digest,
    }


def publish(files: dict[str, str], out: Path) -> None:
    out = require_path_outside_repo(out, what="--out")
    staging = Path(tempfile.mkdtemp(prefix="viz-stage-"))
    try:
        for rel, body in files.items():
            dest = staging / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(body, encoding="utf-8")
        json.loads((staging / "architecture/architecture.json").read_text(encoding="utf-8"))
        json.loads((staging / "workflow/runtime.workflow.json").read_text(encoding="utf-8"))
        out.mkdir(parents=True, exist_ok=True)
        for rel, body in files.items():
            target = out_fs_path(out, rel)
            target.parent.mkdir(parents=True, exist_ok=True)
            # Re-check after mkdir in case a symlink appeared under OUT.
            target = out_fs_path(out, rel)
            temporary = target.with_suffix(target.suffix + ".tmp")
            require_path_outside_repo(temporary, what=f"write tmp for {rel}")
            temporary.write_text(body, encoding="utf-8")
            temporary.replace(target)
            require_path_outside_repo(target, what=f"written file {rel}")
        expected_names = {
            Path(rel).name for rel in files if rel.startswith("skills/") and rel.endswith(".html")
        }
        skills_dir = out / "skills"
        if skills_dir.exists():
            for path in skills_dir.glob("*.html"):
                if path.name not in expected_names and "generated: true" in path.read_text(encoding="utf-8"):
                    path.unlink()
    finally:
        shutil.rmtree(staging, ignore_errors=True)


def check(files: dict[str, str], out: Path | None) -> int:
    """Compare built outputs to lab OUT when present; otherwise in-memory only.

    Linux CI typically has no D:/ lab path: skip disk compare after IR/render gates.
    """
    if out is None or not out.exists():
        print(
            "visualization --check: OUT missing or unset;"
            " in-memory IR/render gates passed; skipping disk compare."
        )
        return 0
    missing = []
    differ = []
    for rel, body in files.items():
        path = out_fs_path(out, rel)
        if not path.exists():
            missing.append(rel)
            continue
        if normalize(path.read_text(encoding="utf-8")) != normalize(body):
            differ.append(rel)
    extras = []
    skills_dir = out / "skills"
    expected = {rel for rel in files if rel.startswith("skills/") and rel.endswith(".html")}
    if skills_dir.exists():
        for path in skills_dir.glob("*.html"):
            rel = path.relative_to(out).as_posix()
            if rel not in expected and "generated: true" in path.read_text(encoding="utf-8"):
                extras.append(rel)
    if missing or differ or extras:
        print("visualization outputs are stale. Refusing to overwrite from --check.", file=sys.stderr)
        for rel in missing:
            print(f"missing {rel}", file=sys.stderr)
        for rel in differ:
            print(f"differs {rel}", file=sys.stderr)
        for rel in extras:
            print(f"extra {rel}", file=sys.stderr)
        return 1
    print(f"visualization outputs match sources under {out}.")
    return 0


def emit_delta(built: dict, baseline: Path, dest: Path | None) -> int:
    arch_path = baseline / "architecture" / "architecture.json"
    wf_path = baseline / "workflow" / "runtime.workflow.json"
    if not arch_path.is_file() or not wf_path.is_file():
        print("baseline is missing architecture or workflow IR", file=sys.stderr)
        return 1
    before = facts_from_ir(
        json.loads(arch_path.read_text(encoding="utf-8")),
        json.loads(wf_path.read_text(encoding="utf-8")),
    )
    after = facts_from_ir(built["architecture"], built["workflow"])
    delta = structural_delta(before, after)
    page = render_delta(
        delta,
        after,
        built["version"],
        built["fingerprint"],
        str(baseline),
    ).replace("@@GENERATED_AT@@", dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    if dest is None:
        print(page)
        return 0
    dest = require_path_outside_repo(dest, what="--delta-out")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest = require_path_outside_repo(dest, what="--delta-out")
    dest.write_text(page, encoding="utf-8")
    print(f"Wrote delta {dest}")
    return 0



def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate MY-SKILLS visualization IR and lab HTML")
    parser.add_argument("--check", action="store_true", help="compare outputs; do not write")
    parser.add_argument(
        "--out",
        type=Path,
        help="output directory (required unless MY_SKILLS_VIZ_OUT is set; no default)",
    )
    parser.add_argument("--delta-against", type=Path, help="base viz directory for a structural delta")
    parser.add_argument("--delta-out", type=Path, help="write only the delta HTML here")
    args = parser.parse_args(argv)
    if args.check and args.delta_against:
        print("use only one of --check and --delta-against", file=sys.stderr)
        return 2
    try:
        out = resolve_viz_out(args.out)
        built = build()
        if args.delta_against:
            return emit_delta(built, args.delta_against, args.delta_out)
    except GateFailure as exc:
        print(exc, file=sys.stderr)
        return 1
    when = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    files = {rel: body.replace("@@GENERATED_AT@@", when) for rel, body in built["files"].items()}
    if args.check:
        return check(files, out)
    if out is None:
        print(
            "error: no output dir; pass --out DIR or set MY_SKILLS_VIZ_OUT"
            " (there is no default output dir)",
            file=sys.stderr,
        )
        return 2
    publish(files, out)
    print(f"Wrote {len(files)} visualization files under {out}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
