#!/usr/bin/env python3
"""Read-only visualization compiler for MY-SKILLS.

Reads registry, preset metadata, and 00 runtime-flow. Writes Archify IR and
generated HTML under docs/. Does not read mounts-cap. Does not fetch Archify.

Shape checks follow the pins in archify-version.yaml (tt-a1i/archify v3.0.1:
architecture schema_version 1, new workflow schema_version 2). This script is
a mapping checker, not a copy of the Archify schema.

Usage:
    python3 00_orchestrator/scripts/gen_visualization.py
    python3 00_orchestrator/scripts/gen_visualization.py --check
    python3 00_orchestrator/scripts/gen_visualization.py \\
        --delta-against /path/to/base/docs --delta-out /tmp/delta.html
"""
from __future__ import annotations

import argparse
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
ROOT = HERE.parent.parent
CAP = (ROOT / "mounts-cap").resolve()
REGISTRY = ROOT / "01_skill-discovery-integration" / "registry.yaml"
SOURCES = ROOT / "01_skill-discovery-integration" / "sources"
PRESETS = ROOT / "01_skill-discovery-integration" / "mounts" / "presets"
RUNTIME_MMD = ROOT / "00_orchestrator" / "runtime-flow.mmd"
RUNTIME_MD = ROOT / "00_orchestrator" / "runtime-flow.md"
GATES = ROOT / "00_orchestrator" / "gates.md"
ARCH_MD = ROOT / "ARCHITECTURE.md"
VERSION = ROOT / "00_orchestrator" / "archify-version.yaml"
CONTRACT = ROOT / "00_orchestrator" / "visualization-source-contract.yaml"

SKILL_TOPS = (
    "00_orchestrator",
    "01_skill-discovery-integration",
    "02_data-processing",
    "03_research",
    "04_analysis",
    "05_manuscript",
    "06_review",
    "skill-harvest",
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
    "中途可进",
    "Gate · 02",
    "Gate · 05",
    "Gate · 06",
    "独立文献",
    "已有统计结果",
    "已有稿件",
    "mounted_fine_ids",
    "citation-verify",
)
REBUILD = "python3 00_orchestrator/scripts/gen_visualization.py"

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


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def read_text(path: Path) -> str:
    resolved = path.resolve()
    if resolved == CAP or CAP in resolved.parents:
        raise GateFailure("G-VIZ-01", f"refusing to read mounts-cap: {path}")
    return path.read_text(encoding="utf-8")


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
        if any(part in {".git", "mounts-cap", "docs", "__pycache__"} for part in path.parts):
            continue
        top = path.relative_to(ROOT).parts[0]
        if top not in SKILL_TOPS:
            raise GateFailure("G-VIZ-01", f"SKILL.md outside 00-06 and skill-harvest: {path}")
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
        SOURCES,
        RUNTIME_MMD,
        RUNTIME_MD,
        GATES,
        ARCH_MD,
        VERSION,
        CONTRACT,
    ]
    # SOURCES is a directory; replace it with files below.
    paths = [p for p in paths if p.is_file()]
    paths.extend(sorted(SOURCES.glob("*.yaml")))
    paths.extend(sorted(PRESETS.glob("*.yaml")))
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


def require_anchors(mmd: str, gates: str, architecture: str) -> None:
    missing = [token for token in MMD_ANCHORS if token not in mmd]
    if missing:
        raise GateFailure("G-VIZ-01", "runtime-flow.mmd missing " + ", ".join(missing))
    for token in ("G0", "G-LIT", "G-05", "G-06"):
        if token not in gates:
            raise GateFailure("G-VIZ-01", f"gates.md missing {token}")
    for folder in SKILL_TOPS:
        if folder not in architecture:
            raise GateFailure("G-VIZ-01", f"ARCHITECTURE.md missing {folder}")
        if not (ROOT / folder).is_dir():
            raise GateFailure("G-VIZ-01", f"missing directory {folder}")
    for entry in ROOT.iterdir():
        if entry.is_dir() and entry.name.startswith("07"):
            raise GateFailure("G-VIZ-01", f"top-level 07 skill is present: {entry.name}")


def check_registry(reg: dict) -> None:
    default = reg.get("default_source") or {}
    if default.get("id") != "my-skills-capabilities":
        raise GateFailure("G-VIZ-01", "default atomic mount source is not my-skills-capabilities")
    if "openclaw" in str(default.get("id", "")).lower() or "openclaw" in str(default.get("source", "")).lower():
        raise GateFailure("G-VIZ-01", "OpenClaw is listed as the default mount source")
    if reg.get("ars_openclaw_policy") != "removed-from-catalog":
        raise GateFailure("G-VIZ-01", "ars_openclaw_policy is not removed-from-catalog")
    mounts = reg.get("mounts") or []
    meta = reg.get("meta") or {}
    if len(mounts) != meta.get("fine_id_count_canonical"):
        raise GateFailure(
            "G-VIZ-01",
            f"mount count {len(mounts)} != fine_id_count_canonical {meta.get('fine_id_count_canonical')}",
        )
    for mount in mounts:
        blob = " ".join(
            str(mount.get(key, ""))
            for key in ("id", "source", "atomic_package", "path")
        ).lower()
        if "openclaw" in blob:
            raise GateFailure("G-VIZ-01", f"OpenClaw appeared on mount {mount.get('id')}")
    for proposal in reg.get("proposals") or []:
        if "openclaw" in str(proposal.get("id", "")).lower():
            raise GateFailure("G-VIZ-01", "OpenClaw appeared in registry proposals")


def check_version(record: dict, contract: dict) -> None:
    if record.get("source") != "tt-a1i/archify":
        raise GateFailure("G-VIZ-01", "Archify source is not tt-a1i/archify")
    if record.get("auto_update") is not False:
        raise GateFailure("G-VIZ-01", "auto_update must be false")
    if record.get("update_policy") != "check":
        raise GateFailure("G-VIZ-01", "update_policy must be check")
    if record.get("visualization_only") is not True:
        raise GateFailure("G-VIZ-01", "visualization_only must be true")
    if record.get("network_at_build") is not False:
        raise GateFailure("G-VIZ-01", "network_at_build must be false")
    pins = record.get("schema_pins") or {}
    arch_pin = (pins.get("architecture") or {}).get("schema_version")
    wf_pin = (pins.get("workflow") or {}).get("schema_version")
    if arch_pin != 1:
        raise GateFailure("G-VIZ-01", "architecture schema_version pin must stay 1 for the v3.0.1 schema")
    if wf_pin != 2:
        raise GateFailure("G-VIZ-01", "workflow schema_version pin must stay 2 for a new workflow")
    phrases = contract.get("forbidden_fact_sources") or []
    required = [
        "LLM inference",
        "generated HTML",
        "previous generated HTML",
        "arbitrary mounted-file crawling",
        "filename alone",
        "visual appearance",
        "unvalidated JSON",
    ]
    for phrase in required:
        if phrase not in phrases:
            raise GateFailure("G-VIZ-01", f"contract missing forbidden source {phrase!r}")
    forbidden_mounts = contract.get("forbidden_default_atomic_mount_sources") or []
    if "OpenClaw" not in forbidden_mounts:
        raise GateFailure("G-VIZ-01", "contract does not forbid OpenClaw as a default atomic mount")


def architecture_ir() -> dict:
    components = [
        {"id": "c00", "type": "security", "label": "00 Control / QC", "sublabel": "entry, gate, recovery", "row": 0, "col": 0},
        {"id": "c01", "type": "backend", "label": "01 Discovery / Registry", "sublabel": "version and mount index", "row": 0, "col": 1},
        {"id": "mounts", "type": "external", "label": "External mounts", "sublabel": "registry pointers; not architecture facts", "row": 0, "col": 2},
        {"id": "c02", "type": "backend", "label": "02 Data", "sublabel": "analysis-ready data", "row": 1, "col": 0},
        {"id": "c03", "type": "backend", "label": "03 Literature", "sublabel": "literature and citation-verify", "row": 1, "col": 1},
        {"id": "c04", "type": "backend", "label": "04 Statistics", "sublabel": "statistics and figures", "row": 1, "col": 2},
        {"id": "c05", "type": "backend", "label": "05 Writing", "sublabel": "manuscript", "row": 2, "col": 0},
        {"id": "c06", "type": "backend", "label": "06 Review", "sublabel": "review and response", "row": 2, "col": 1},
        {"id": "harvest", "type": "backend", "label": "skill-harvest", "sublabel": "proposals only; not a domain layer", "row": 2, "col": 2},
    ]
    return {
        "schema_version": 1,
        "diagram_type": "architecture",
        "meta": {
            "title": "MY-SKILLS Architecture",
            "subtitle": "Source, registry, skills, QC",
            "locale": "zh-CN",
            "output": "docs/architecture/index.html",
        },
        "layout": {"mode": "grid", "cols": 3},
        "components": components,
        "boundaries": [
            {
                "kind": "region",
                "label": "A ownership",
                "wraps": ["c00", "c01", "c02", "c03", "c04", "c05", "c06", "harvest"],
            },
            {
                "kind": "region",
                "label": "External mount index",
                "wraps": ["mounts"],
            },
        ],
        "connections": [
            {"id": "need-mount", "from": "c00", "to": "c01", "label": "session mount when fine ids are missing"},
            {"id": "index-mounts", "from": "c01", "to": "mounts", "label": "registry pointers only"},
            {"id": "dispatch-02", "from": "c00", "to": "c02", "label": "dispatch"},
            {"id": "dispatch-03", "from": "c00", "to": "c03", "label": "dispatch"},
            {"id": "dispatch-04", "from": "c00", "to": "c04", "label": "dispatch"},
            {"id": "dispatch-05", "from": "c00", "to": "c05", "label": "dispatch"},
            {"id": "dispatch-06", "from": "c00", "to": "c06", "label": "dispatch"},
            {"id": "handoff-04", "from": "c02", "to": "c04", "label": "analysis-ready handoff"},
            {"id": "results-05", "from": "c04", "to": "c05", "label": "results into writing"},
            {"id": "lit05", "from": "c03", "to": "c05", "label": "Lit05 citation-verify"},
            {"id": "lit06", "from": "c03", "to": "c06", "label": "Lit06 citation-verify"},
            {"id": "manuscript-06", "from": "c05", "to": "c06", "label": "manuscript into review"},
            {"id": "propose", "from": "harvest", "to": "c01", "label": "evolution proposal", "variant": "dashed"},
        ],
    }


def workflow_ir() -> dict:
    lanes = [
        {"id": "control", "label": "00 control"},
        {"id": "mount", "label": "01 mount"},
        {"id": "produce", "label": "Domain chain"},
        {"id": "literature", "label": "03 literature"},
        {"id": "qc", "label": "QC loop", "variant": "exception"},
    ]
    nodes = [
        {"id": "task", "lane": "control", "col": 0, "type": "external", "label": "Task", "sublabel": "entry"},
        {"id": "detect", "lane": "control", "col": 1, "type": "security", "label": "00 Detect / Gate", "sublabel": "intent and entry"},
        {"id": "single", "lane": "control", "col": 4, "type": "backend", "label": "Single-domain skill", "sublabel": "named one-domain entry"},
        {"id": "done", "lane": "control", "col": 5, "type": "backend", "label": "stage done", "sublabel": "terminal PASS"},
        {"id": "mountcheck", "lane": "mount", "col": 1, "type": "security", "label": "mounted_fine_ids", "sublabel": "coverage check"},
        {"id": "s01", "lane": "mount", "col": 2, "type": "backend", "label": "01 Mount", "sublabel": "session mount"},
        {"id": "dispatch", "lane": "mount", "col": 3, "type": "backend", "label": "Dispatch", "sublabel": "after G0 or already covered"},
        {"id": "p02", "lane": "produce", "col": 2, "type": "backend", "label": "02 Data", "sublabel": "processing"},
        {"id": "p04", "lane": "produce", "col": 3, "type": "backend", "label": "04 Statistics", "sublabel": "stats and figures"},
        {"id": "p05", "lane": "produce", "col": 4, "type": "backend", "label": "05 Writing", "sublabel": "manuscript"},
        {"id": "p06", "lane": "produce", "col": 5, "type": "backend", "label": "06 Review", "sublabel": "review and response"},
        {"id": "p03", "lane": "literature", "col": 2, "type": "backend", "label": "03 Literature", "sublabel": "independent entry or evidence"},
        {"id": "lit05", "lane": "literature", "col": 4, "type": "security", "label": "Lit05 citation-verify", "sublabel": "before Gate 05"},
        {"id": "lit06", "lane": "literature", "col": 5, "type": "security", "label": "Lit06 citation-verify", "sublabel": "inside 06"},
        {"id": "locate", "lane": "qc", "col": 3, "type": "security", "label": "Locate failure", "sublabel": "smallest responsible node"},
        {"id": "rework", "lane": "qc", "col": 4, "type": "security", "label": "Local or rollback", "sublabel": "affected chain only"},
        {"id": "escalate", "lane": "qc", "col": 5, "type": "security", "label": "unresolved", "sublabel": "budget exhausted"},
    ]
    edges = [
        {"id": "e-task-detect", "from": "task", "to": "detect", "label": "task enters", "role": "main"},
        {"id": "e-detect-mount", "from": "detect", "to": "mountcheck", "label": "before specialist", "role": "main"},
        {"id": "e-mount-gap", "from": "mountcheck", "to": "s01", "label": "fine ids missing", "role": "branch"},
        {"id": "e-g0-pass", "from": "s01", "to": "dispatch", "label": "G0 PASS", "role": "main"},
        {"id": "e-g0-fail", "from": "s01", "to": "locate", "label": "G0 FAIL", "role": "error"},
        {"id": "e-covered", "from": "mountcheck", "to": "dispatch", "label": "fine ids already covered", "role": "main"},
        {"id": "e-d02", "from": "dispatch", "to": "p02", "label": "entry 02", "role": "branch"},
        {"id": "e-d03", "from": "dispatch", "to": "p03", "label": "entry 03 independent literature", "role": "branch"},
        {"id": "e-d04", "from": "dispatch", "to": "p04", "label": "entry 04 or mid-entry", "role": "branch"},
        {"id": "e-d05", "from": "dispatch", "to": "p05", "label": "entry 05 or mid-entry", "role": "branch"},
        {"id": "e-d06", "from": "dispatch", "to": "p06", "label": "entry 06 or mid-entry", "role": "branch"},
        {"id": "e-dsingle", "from": "dispatch", "to": "single", "label": "named single domain", "role": "branch"},
        {"id": "e-02-04", "from": "p02", "to": "p04", "label": "Gate 02 PASS, not terminal", "role": "main"},
        {"id": "e-04-05", "from": "p04", "to": "p05", "label": "Gate 04 PASS, not terminal", "role": "main"},
        {"id": "e-05-lit", "from": "p05", "to": "lit05", "label": "required before Gate 05", "role": "main"},
        {"id": "e-lit-06", "from": "lit05", "to": "p06", "label": "Gate 05 PASS, not terminal", "role": "main"},
        {"id": "e-06-lit", "from": "p06", "to": "lit06", "label": "required inside 06", "role": "main"},
        {"id": "e-lit-done", "from": "lit06", "to": "done", "label": "Gate 06 PASS at terminal", "role": "main"},
        {"id": "e-03-05", "from": "p03", "to": "p05", "label": "evidence does not replace Lit05", "role": "branch", "variant": "dashed"},
        {"id": "e-03-06", "from": "p03", "to": "p06", "label": "evidence does not replace Lit06", "role": "branch", "variant": "dashed"},
        {"id": "e-02-done", "from": "p02", "to": "done", "label": "terminal PASS", "role": "branch"},
        {"id": "e-03-done", "from": "p03", "to": "done", "label": "terminal PASS", "role": "branch"},
        {"id": "e-04-done", "from": "p04", "to": "done", "label": "terminal PASS", "role": "branch"},
        {"id": "e-lit05-done", "from": "lit05", "to": "done", "label": "Gate 05 terminal PASS", "role": "branch"},
        {"id": "e-single-done", "from": "single", "to": "done", "label": "target gate PASS", "role": "branch"},
        {"id": "e-fail-02", "from": "p02", "to": "locate", "label": "Gate 02 FAIL", "role": "error"},
        {"id": "e-fail-03", "from": "p03", "to": "locate", "label": "Gate 03 FAIL", "role": "error"},
        {"id": "e-fail-04", "from": "p04", "to": "locate", "label": "Gate 04 FAIL", "role": "error"},
        {"id": "e-fail-lit05", "from": "lit05", "to": "locate", "label": "Lit05 FAIL", "role": "error"},
        {"id": "e-fail-06", "from": "p06", "to": "locate", "label": "Gate 06 FAIL", "role": "error"},
        {"id": "e-fail-lit06", "from": "lit06", "to": "locate", "label": "Lit06 FAIL", "role": "error"},
        {"id": "e-fail-single", "from": "single", "to": "locate", "label": "target gate FAIL", "role": "error"},
        {"id": "e-locate-rework", "from": "locate", "to": "rework", "label": "local rework or rollback", "role": "error"},
        {"id": "e-rework-mount", "from": "rework", "to": "mountcheck", "label": "re-enter affected node", "role": "return"},
        {"id": "e-locate-escalate", "from": "locate", "to": "escalate", "label": "budget exhausted", "role": "error"},
    ]
    return {
        "schema_version": 2,
        "diagram_type": "workflow",
        "meta": {
            "title": "MY-SKILLS Workflow",
            "subtitle": "Task, gates, mounts, mid-entry, Lit05, Lit06, QC loop",
            "locale": "zh-CN",
            "output": "docs/workflow/index.html",
        },
        "lanes": lanes,
        "phases": [
            {"id": "intake", "label": "Detect", "fromCol": 0, "toCol": 1},
            {"id": "session", "label": "Mount", "fromCol": 1, "toCol": 3},
            {"id": "domains", "label": "02-06", "fromCol": 2, "toCol": 5},
        ],
        "groups": [
            {"id": "forward", "label": "PASS forward", "lane": "produce", "fromCol": 2, "toCol": 5},
            {"id": "lit-gates", "label": "Lit05 Lit06", "lane": "literature", "fromCol": 4, "toCol": 5},
            {"id": "qc-loop", "label": "QC loop", "lane": "qc", "fromCol": 3, "toCol": 5, "variant": "dashed"},
        ],
        "mainPath": ["task", "detect", "mountcheck", "dispatch", "p02", "p04", "p05", "lit05", "p06", "lit06", "done"],
        "semanticChecks": {
            "allowedRoots": ["task"],
            "allowedTerminals": ["done", "escalate"],
            "requiredEdges": [
                {"from": "p05", "to": "lit05"},
                {"from": "p06", "to": "lit06"},
                {"from": "dispatch", "to": "p03"},
                {"from": "dispatch", "to": "p04"},
                {"from": "dispatch", "to": "p05"},
                {"from": "dispatch", "to": "p06"},
            ],
            "requiredPaths": [
                {"from": "task", "to": "done"},
                {"from": "task", "to": "p03"},
                {"from": "p05", "to": "lit05"},
                {"from": "p06", "to": "lit06"},
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
        if str(comp["label"]).startswith("07"):
            raise GateFailure("G-VIZ-02", "architecture label starts a 07 skill")
    known = set(ids)
    for boundary in arch["boundaries"]:
        if boundary["kind"] not in {"region", "security-group"}:
            raise GateFailure("G-VIZ-02", "bad boundary kind")
        if not boundary.get("wraps"):
            raise GateFailure("G-VIZ-02", "boundary wraps is empty")
        for item in boundary["wraps"]:
            if item not in known:
                raise GateFailure("G-VIZ-02", f"boundary wraps unknown id {item}")
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
    for node in wf["nodes"]:
        _check_id(node["id"], "node")
        if node["lane"] not in lanes:
            raise GateFailure("G-VIZ-02", f"node {node['id']} lane missing")
        if not isinstance(node["col"], int) or not 0 <= node["col"] <= 5:
            raise GateFailure("G-VIZ-02", f"node {node['id']} col out of range")
        if node["type"] not in COMPONENT_TYPES or not node.get("label"):
            raise GateFailure("G-VIZ-02", f"bad node {node['id']}")
        slot = (node["lane"], node["col"])
        if slot in seen_slot:
            raise GateFailure("G-VIZ-02", f"duplicate lane/col {slot}")
        seen_slot.add(slot)
        node_ids.add(node["id"])
    for edge in wf["edges"]:
        _check_id(edge["id"], "edge")
        if edge["from"] not in node_ids or edge["to"] not in node_ids:
            raise GateFailure("G-VIZ-02", f"edge {edge['id']} endpoint missing")
        if edge.get("role") not in EDGE_ROLES:
            raise GateFailure("G-VIZ-02", f"edge {edge['id']} role missing")
        if "variant" in edge and edge["variant"] not in VARIANTS:
            raise GateFailure("G-VIZ-02", f"bad edge variant {edge['id']}")
    if len(wf["mainPath"]) < 2 or any(item not in node_ids for item in wf["mainPath"]):
        raise GateFailure("G-VIZ-02", "mainPath is not a list of node ids")
    edge_pairs = {(e["from"], e["to"]) for e in wf["edges"]}
    for left, right in zip(wf["mainPath"], wf["mainPath"][1:]):
        if (left, right) not in edge_pairs:
            raise GateFailure("G-VIZ-02", f"mainPath has no edge {left} -> {right}")
    for phase in wf["phases"] + wf["groups"]:
        if not 0 <= phase["fromCol"] <= phase["toCol"] <= 5:
            raise GateFailure("G-VIZ-02", f"bad column span {phase['id']}")
    for group in wf["groups"]:
        if group["lane"] not in lanes:
            raise GateFailure("G-VIZ-02", f"group lane missing {group['id']}")
    checks = wf["semanticChecks"]
    for key in ("allowedRoots", "allowedTerminals"):
        if any(item not in node_ids for item in checks[key]):
            raise GateFailure("G-VIZ-02", f"semanticChecks.{key} references an unknown node")
    for rel in checks["requiredEdges"] + checks["requiredPaths"]:
        if rel["from"] not in node_ids or rel["to"] not in node_ids:
            raise GateFailure("G-VIZ-02", "semanticChecks relation references an unknown node")
        if (rel["from"], rel["to"]) not in edge_pairs and rel in checks["requiredEdges"]:
            raise GateFailure("G-VIZ-02", f"required edge missing {rel['from']} -> {rel['to']}")
    json.loads(dump_json(arch))
    json.loads(dump_json(wf))


def facts_from_ir(arch: dict, wf: dict) -> dict:
    return {
        "components": {c["id"]: c["label"] for c in arch["components"]},
        "connections": {
            c["id"]: {"from": c["from"], "to": c["to"], "label": c.get("label", "")}
            for c in arch["connections"]
        },
        "nodes": {n["id"]: n["label"] for n in wf["nodes"]},
        "edges": {
            e["id"]: {"from": e["from"], "to": e["to"], "label": e.get("label", "")}
            for e in wf["edges"]
        },
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
<!-- archify_version: {esc(version)} -->
<!-- source_fingerprint: {esc(digest)} -->
<!-- build_status: ir-shape-checked -->
<!-- archify-render: not-run -->
<!-- github_pages: not-published -->
<header>
  <h1>{esc(title)}</h1>
  <p class="muted">Generated artifact. Rebuild with <code>{esc(REBUILD)}</code>. Do not edit this file by hand.</p>
  <nav>{nav}</nav>
</header>
<main>
  <p class="banner">生成时间 @@GENERATED_AT@@。Archify {esc(version)}。构建状态 ir-shape-checked。Archify 渲染未执行。GitHub Pages 未发布。事实源是 MY-SKILLS，不是本页。</p>
  {body}
</main>
<footer>
  <p>source fingerprint <code>{esc(digest)}</code></p>
  <p>设计历史不是首页。规格在 <code>00_orchestrator/visualization-architecture.md</code>。</p>
</footer>
</body>
</html>
"""


NAV = (
    '<a href="{home}">首页</a>'
    '<a href="{arch}">Architecture 状态</a>'
    '<a href="{wf}">Workflow 状态</a>'
    '<a href="{skills}">Skill 索引</a>'
    '<a href="{mounts}">Mounts</a>'
    '<a href="{delta}">Delta</a>'
    '<a href="{history}">设计历史</a>'
)


def nav_for(home: str, arch: str, wf: str, skills: str, mounts: str, delta: str, history: str) -> str:
    return NAV.format(home=home, arch=arch, wf=wf, skills=skills, mounts=mounts, delta=delta, history=history)


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
            "<p>正文仍在源 SKILL.md。本页只取 frontmatter，不把正文画成图。</p>"
        )
        links = {
            "home": "../index.html",
            "arch": "../architecture/index.html",
            "wf": "../workflow/index.html",
            "skills": "index.html",
            "mounts": "../mounts/index.html",
            "delta": "../changes/latest-delta.html",
            "history": "../design-history/index.html",
        }
        files[f"docs/skills/{skill['name']}.html"] = shell(
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
        "arch": "../architecture/index.html",
        "wf": "../workflow/index.html",
        "skills": "index.html",
        "mounts": "../mounts/index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    files["docs/skills/index.html"] = shell(
        "Skill index",
        "<p>按 00–06 与 skill-harvest 索引。页面来自 SKILL.md frontmatter。</p>" + "".join(sections),
        version,
        digest,
        nav_for(**links),
    )
    return files


def render_mounts(reg: dict, sources: list[dict], presets: list[dict], version: str, digest: str) -> str:
    default = reg["default_source"]
    mounts = reg["mounts"]
    mounted = sum(1 for item in mounts if item.get("status") == "MOUNTED")
    proposed = sum(1 for item in mounts if item.get("status") == "PROPOSED")
    coarse_rows = []
    for coarse in reg.get("coarse_ids") or []:
        count = sum(1 for item in mounts if item.get("coarse") == coarse.get("id"))
        domains = ", ".join(coarse.get("a_domains") or [])
        coarse_rows.append(
            f"<tr><td>{esc(coarse.get('id'))}</td><td><code>{esc(coarse.get('slug'))}</code></td>"
            f"<td>{esc(domains)}</td><td>{esc(coarse.get('specialist_hint'))}</td><td>{count}</td></tr>"
        )
    mount_rows = []
    for item in mounts:
        mount_rows.append(
            "<tr>"
            f"<td><code>{esc(item.get('id'))}</code></td>"
            f"<td>{esc(item.get('label'))}</td>"
            f"<td>{esc(item.get('coarse'))}</td>"
            f"<td>{esc(item.get('source'))}</td>"
            f"<td>{esc(item.get('status'))}</td>"
            f"<td>{esc(item.get('atomic_package', ''))}</td>"
            f"<td>{esc(item.get('a_domain', ''))}</td>"
            f"<td>{esc(item.get('load_priority', ''))}</td>"
            f"<td><code>{esc(item.get('path', ''))}</code></td>"
            "</tr>"
        )
    source_rows = "".join(
        f"<tr><td><code>{esc(item['source_id'])}</code></td><td>{esc(item.get('role', ''))}</td>"
        f"<td>{esc(item.get('status', ''))}</td><td>{esc(item.get('repo', ''))}</td></tr>"
        for item in sources
    )
    preset_rows = "".join(
        f"<tr><td><code>{esc(item['preset_id'])}</code></td><td>{esc(item.get('status', ''))}</td>"
        f"<td>{esc(item.get('version', ''))}</td><td>{esc(item.get('chassis_source', ''))}</td></tr>"
        for item in presets
    )
    proposal_rows = "".join(
        f"<tr><td><code>{esc(item.get('id'))}</code></td><td>{esc(item.get('status'))}</td>"
        f"<td>{esc(item.get('role'))}</td></tr>"
        for item in (reg.get("proposals") or [])
    )
    body = f"""
    <section class="card">
      <h2>Default atomic mount source</h2>
      <p><code>{esc(default.get('id'))}</code></p>
      <p>{esc(default.get('source'))}</p>
      <p>OpenClaw is not a default atomic mount source. Policy <code>{esc(reg.get('ars_openclaw_policy'))}</code>.</p>
      <p class="muted">MOUNTED {mounted} · PROPOSED {proposed} · fine ids {len(mounts)}. Counts come from registry.yaml. This page does not read mounts-cap.</p>
    </section>
    <h2>Coarse buckets</h2>
    <table><thead><tr><th>coarse</th><th>slug</th><th>a_domains</th><th>specialist</th><th>fine ids</th></tr></thead>
    <tbody>{''.join(coarse_rows)}</tbody></table>
    <h2>Fine ids</h2>
    <table><thead><tr><th>id</th><th>label</th><th>coarse</th><th>source</th><th>status</th><th>package</th><th>a_domain</th><th>priority</th><th>registry path</th></tr></thead>
    <tbody>{''.join(mount_rows)}</tbody></table>
    <h2>Source records</h2>
    <table><thead><tr><th>source_id</th><th>role</th><th>status</th><th>repo</th></tr></thead>
    <tbody>{source_rows}</tbody></table>
    <h2>Presets</h2>
    <table><thead><tr><th>preset</th><th>status</th><th>version</th><th>chassis source</th></tr></thead>
    <tbody>{preset_rows}</tbody></table>
    <h2>Proposals</h2>
    <table><thead><tr><th>id</th><th>status</th><th>role</th></tr></thead><tbody>{proposal_rows}</tbody></table>
    """
    links = {
        "home": "../index.html",
        "arch": "../architecture/index.html",
        "wf": "../workflow/index.html",
        "skills": "../skills/index.html",
        "mounts": "index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    return shell("External mounts", body, version, digest, nav_for(**links))


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
        "arch": "../architecture/index.html",
        "wf": "../workflow/index.html",
        "skills": "../skills/index.html",
        "mounts": "../mounts/index.html",
        "delta": "latest-delta.html",
        "history": "../design-history/index.html",
    }
    return shell("Architecture Delta", body, version, digest, nav_for(**links))


def load_sidecar_metadata() -> tuple[list[dict], list[dict]]:
    sources = []
    for path in sorted(SOURCES.glob("*.yaml")):
        data = read_yaml(path)
        source_id = str(data.get("source_id", ""))
        if "openclaw" in source_id.lower():
            raise GateFailure("G-VIZ-01", f"OpenClaw source record {path.name}")
        sources.append(
            {
                "source_id": source_id,
                "role": data.get("role", ""),
                "status": data.get("status", ""),
                "repo": data.get("repo", ""),
            }
        )
    presets = []
    for path in sorted(PRESETS.glob("*.yaml")):
        data = read_yaml(path)
        chassis = data.get("chassis") or {}
        presets.append(
            {
                "preset_id": data.get("preset_id", path.stem),
                "status": data.get("status", ""),
                "version": data.get("version", ""),
                "chassis_source": chassis.get("source", ""),
            }
        )
    return sources, presets


def build() -> dict:
    record = read_yaml(VERSION)
    contract = read_yaml(CONTRACT)
    check_version(record, contract)
    reg = read_yaml(REGISTRY)
    check_registry(reg)
    mmd = read_text(RUNTIME_MMD)
    gates = read_text(GATES)
    architecture = read_text(ARCH_MD)
    read_text(RUNTIME_MD)
    require_anchors(mmd, gates, architecture)
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
    # Emitted schema_version values come from the pinned record, not a second guess.
    arch["schema_version"] = record["schema_pins"]["architecture"]["schema_version"]
    wf["schema_version"] = record["schema_pins"]["workflow"]["schema_version"]
    validate_ir(arch, wf)
    digest = fingerprint(source_paths())
    version = str(record["expected_version"])
    home_links = {
        "home": "index.html",
        "arch": "architecture/index.html",
        "wf": "workflow/index.html",
        "skills": "skills/index.html",
        "mounts": "mounts/index.html",
        "delta": "changes/latest-delta.html",
        "history": "design-history/index.html",
    }
    root_links = {
        "home": "../index.html",
        "arch": "index.html",
        "wf": "../workflow/index.html",
        "skills": "../skills/index.html",
        "mounts": "../mounts/index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    wf_links = {
        "home": "../index.html",
        "arch": "../architecture/index.html",
        "wf": "index.html",
        "skills": "../skills/index.html",
        "mounts": "../mounts/index.html",
        "delta": "../changes/latest-delta.html",
        "history": "../design-history/index.html",
    }
    comp_rows = [(c["id"], c["label"]) for c in arch["components"]]
    node_rows = [(n["id"], n["label"]) for n in wf["nodes"]]
    arch_extra = (
        "<p>本页是 IR 状态页，不是 Archify 画出的架构图。IR 文件是 "
        "<a href=\"architecture.json\"><code>architecture.json</code></a>。"
        f" schema_version {arch['schema_version']}。字段 components / boundaries / connections。</p>"
    )
    wf_extra = (
        "<p>本页是 IR 状态页，不是 Archify 画出的流程图。IR 文件是 "
        "<a href=\"runtime.workflow.json\"><code>runtime.workflow.json</code></a>。"
        f" schema_version {wf['schema_version']}。字段 lanes / phases / groups / mainPath / nodes / edges。"
        " 03、Lit05、Lit06 与 mid-entry 在节点和边上。</p>"
    )
    home_body = (
        "<div class=\"grid\">"
        "<section class=\"card\"><h2>Architecture</h2><p>系统组成与边界。状态页链接到 IR。</p>"
        "<p><a href=\"architecture/index.html\">打开 Architecture 状态</a></p></section>"
        "<section class=\"card\"><h2>Workflow</h2><p>任务如何运行，含中途入口、Lit05、Lit06 与 QC 环。</p>"
        "<p><a href=\"workflow/index.html\">打开 Workflow 状态</a></p></section>"
        "<section class=\"card\"><h2>Mounts</h2>"
        f"<p>默认原子挂载源 <code>{esc(reg['default_source']['id'])}</code>。"
        "OpenClaw is not a default atomic mount source.</p>"
        "<p><a href=\"mounts/index.html\">打开 mount 索引</a></p></section>"
        "<section class=\"card\"><h2>Skills</h2><p>00–06 与 skill-harvest 的 frontmatter 页面。</p>"
        "<p><a href=\"skills/index.html\">打开 Skill 索引</a></p></section>"
        "</div>"
        "<h2>Build</h2><dl>"
        f"<dt>Archify</dt><dd><code>{esc(record['source'])}</code> {esc(version)}</dd>"
        "<dt>auto_update</dt><dd>false</dd>"
        "<dt>update_policy</dt><dd>check</dd>"
        "<dt>schema_version</dt><dd>architecture 1 · workflow 2</dd>"
        "<dt>build_status</dt><dd>ir-shape-checked</dd>"
        "<dt>archify_render</dt><dd>not-run</dd>"
        "<dt>github_pages</dt><dd>not-published</dd>"
        f"<dt>fingerprint</dt><dd><code>{esc(digest)}</code></dd>"
        "</dl>"
        "<p><a href=\"build-manifest.json\">build-manifest.json</a> · "
        "<a href=\"changes/latest-delta.html\">structural Delta</a></p>"
    )
    history_body = (
        "<p>这不是文档首页。首页是 <a href=\"../index.html\">docs/index.html</a>。</p>"
        "<p>批准的规格在 <a href=\"../../00_orchestrator/visualization-architecture.md\">00_orchestrator/visualization-architecture.md</a>。</p>"
        "<p>本索引由生成器写出，规格正文不是生成物。</p>"
    )
    after = facts_from_ir(arch, wf)
    delta = structural_delta(empty_facts(), after)
    manifest = {
        "generated": True,
        "rebuild_command": REBUILD,
        "generated_at": "@@GENERATED_AT@@",
        "archify": {
            "source": record["source"],
            "expected_version": version,
            "tag": record.get("tag"),
            "commit": record.get("commit"),
            "auto_update": False,
            "update_policy": "check",
            "visualization_only": True,
        },
        "schema_version": {"architecture": 1, "workflow": 2},
        "build_status": "ir-shape-checked",
        "archify_render": "not-run",
        "github_pages": "not-published",
        "source_fingerprint": digest,
        "sources": [path.relative_to(ROOT).as_posix() for path in source_paths()],
    }
    files = {
        "docs/build-manifest.json": dump_json(manifest),
        "docs/architecture/architecture.json": dump_json(arch),
        "docs/workflow/runtime.workflow.json": dump_json(wf),
        "docs/index.html": shell("MY-SKILLS", home_body, version, digest, nav_for(**home_links)),
        "docs/architecture/index.html": render_status(
            "Architecture IR status",
            "Stable system components from ARCHITECTURE.md and the 00-06 directories.",
            comp_rows,
            arch_extra,
            version,
            digest,
            root_links,
        ),
        "docs/workflow/index.html": render_status(
            "Workflow IR status",
            "Structural mapping of runtime-flow.mmd, including mid-entry, Lit05, and Lit06.",
            node_rows,
            wf_extra,
            version,
            digest,
            wf_links,
        ),
        "docs/mounts/index.html": render_mounts(reg, sources, presets, version, digest),
        "docs/changes/latest-delta.html": render_delta(
            delta, after, version, digest, "none (no baseline snapshot supplied)"
        ),
        "docs/design-history/index.html": shell(
            "Design history",
            history_body,
            version,
            digest,
            nav_for(
                home="../index.html",
                arch="../architecture/index.html",
                wf="../workflow/index.html",
                skills="../skills/index.html",
                mounts="../mounts/index.html",
                delta="../changes/latest-delta.html",
                history="index.html",
            ),
        ),
    }
    files.update(render_skills(skills, version, digest))
    return {"files": files, "architecture": arch, "workflow": wf, "version": version, "fingerprint": digest}


def publish(files: dict[str, str]) -> None:
    staging = Path(tempfile.mkdtemp(prefix="viz-stage-"))
    try:
        for rel, text in files.items():
            dest = staging / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text, encoding="utf-8")
        json.loads((staging / "docs/architecture/architecture.json").read_text(encoding="utf-8"))
        json.loads((staging / "docs/workflow/runtime.workflow.json").read_text(encoding="utf-8"))
        for rel, text in files.items():
            target = ROOT / rel
            if target.exists():
                current = target.read_text(encoding="utf-8")
                if "archify-rendered: true" in current:
                    continue
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix(target.suffix + ".tmp")
            temporary.write_text(text, encoding="utf-8")
            temporary.replace(target)
        expected_names = {Path(rel).name for rel in files if rel.startswith("docs/skills/") and rel.endswith(".html")}
        skills_dir = ROOT / "docs" / "skills"
        if skills_dir.exists():
            for path in skills_dir.glob("*.html"):
                if path.name not in expected_names and "generated: true" in path.read_text(encoding="utf-8"):
                    path.unlink()
    finally:
        shutil.rmtree(staging, ignore_errors=True)


def check(files: dict[str, str]) -> int:
    missing = []
    differ = []
    for rel, text in files.items():
        path = ROOT / rel
        if not path.exists():
            missing.append(rel)
            continue
        if normalize(path.read_text(encoding="utf-8")) != normalize(text):
            differ.append(rel)
    extras = []
    skills_dir = ROOT / "docs" / "skills"
    expected = {rel for rel in files if rel.startswith("docs/skills/") and rel.endswith(".html")}
    if skills_dir.exists():
        for path in skills_dir.glob("*.html"):
            rel = path.relative_to(ROOT).as_posix()
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
    print("visualization outputs match sources.")
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
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(page, encoding="utf-8")
    print(f"Wrote delta {dest}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate MY-SKILLS visualization IR and docs")
    parser.add_argument("--check", action="store_true", help="compare outputs; do not write")
    parser.add_argument("--delta-against", type=Path, help="base docs directory for a structural delta")
    parser.add_argument("--delta-out", type=Path, help="write only the delta HTML here")
    args = parser.parse_args(argv)
    if args.check and args.delta_against:
        print("use only one of --check and --delta-against", file=sys.stderr)
        return 2
    try:
        built = build()
    except GateFailure as exc:
        print(exc, file=sys.stderr)
        return 1
    if args.delta_against:
        return emit_delta(built, args.delta_against, args.delta_out)
    when = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    files = {rel: text.replace("@@GENERATED_AT@@", when) for rel, text in built["files"].items()}
    if args.check:
        return check(files)
    publish(files)
    print(f"Wrote {len(files)} visualization files. Archify render was not run.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
