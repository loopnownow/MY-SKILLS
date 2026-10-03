#!/usr/bin/env python3
"""Deterministic repository-wide QC for MY-SKILLS.

Read-only by design. It scans structure, frontmatter, local Markdown links,
legacy active references, registry mount paths, meta/version consistency, and
optionally the companion capabilities repository. It never edits the repo.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

TOP = (
    "00_orchestrator", "01_skill-discovery-integration", "02_data-processing",
    "03_research", "04_analysis", "05_manuscript", "06_review", "skill-harvest",
)
FORBIDDEN_DIRS = {"core", "archive", "bundles", "merged"}
LEGACY_ACTIVE = ("01_automation", "02_imaging")
REQUIRED = [Path(x) / "SKILL.md" for x in TOP]
SKIP_DIRS = {".git", "__pycache__", "mounts-cap"}
TEXT_EXTS = {".md", ".yaml", ".yml", ".txt", ".html"}
STALE_EXTS = TEXT_EXTS | {".py"}
HISTORICAL_FILES = {Path("_medical-research-meta/INTEGRATION_MAP.md"), Path("_medical-research-meta/INTEGRATION_MAP.archive.md")}
NEGATIVE_WORD_RE = re.compile(r"(?i)\b(?:no|not|never|do not|don't|retired|deleted|historical|legacy|former)\b")


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="ignore")


def files(root: Path, exts=None):
    allowed = TEXT_EXTS if exts is None else exts
    for p in root.rglob("*"):
        if p.is_file() and not (set(p.parts) & SKIP_DIRS) and p.suffix.lower() in allowed:
            yield p



def check_tracked_pycache(root: Path, out: list):
    """FAIL if git tracks __pycache__/ or *.pyc (runtime junk). Light guard."""
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "ls-files"],
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
        )
        tracked = proc.stdout.splitlines() if proc.returncode == 0 else []
    except Exception as e:
        out.append(("SKIP", "tracked-pycache", f"git ls-files unavailable: {e}"))
        return
    bad = [p for p in tracked if "__pycache__" in p.replace("\\", "/") or p.endswith(".pyc")]
    out.append(
        ("FAIL" if bad else "PASS", "tracked-pycache",
         f"tracked runtime junk: {bad[:20]}" if bad else "no tracked __pycache__/ or *.pyc")
    )


def check_structure(root: Path, out: list):
    dirs = {p.name for p in root.iterdir() if p.is_dir()}
    missing = [str(p) for p in REQUIRED if not (root / p).is_file()]
    forbidden = sorted(dirs & FORBIDDEN_DIRS)
    unexpected = sorted((dirs & set(LEGACY_ACTIVE)))
    if missing: out.append(("FAIL", "structure", f"missing required SKILL.md: {missing}"))
    if forbidden: out.append(("FAIL", "structure", f"forbidden top-level dirs: {forbidden}"))
    if unexpected: out.append(("FAIL", "structure", f"legacy top-level dirs present: {unexpected}"))
    if not missing and not forbidden and not unexpected:
        out.append(("PASS", "structure", "top-level architecture is present and legacy dirs are absent"))


def check_frontmatter(root: Path, out: list):
    bad = []
    for rel in REQUIRED:
        s = read(root / rel)
        if not s.startswith("---\n") or "\nname:" not in s[:1000] or "\ndescription:" not in s[:2000]:
            bad.append(str(rel))
    out.append(("FAIL" if bad else "PASS", "frontmatter", f"invalid: {bad}" if bad else "all top-level SKILL.md files have frontmatter name/description"))


def _depth_exempt(rel: Path) -> bool:
    """Allow annual journal datasets: 03_research/medical-journal-submit/data/<YYYY>/file."""
    parts = rel.parts
    if (
        len(parts) == 5
        and parts[0] == "03_research"
        and parts[1] == "medical-journal-submit"
        and parts[2] == "data"
        and parts[3].isdigit()
        and len(parts[3]) == 4
    ):
        return True
    return False


def check_depth(root: Path, out: list):
    bad = []
    for skill in TOP:
        base = root / skill
        for p in base.rglob("*"):
            if p.is_file() and ".git" not in p.parts and "__pycache__" not in p.parts:
                rel = p.relative_to(root)
                n = len(rel.parts)
                if n > 4 and not _depth_exempt(rel):
                    bad.append(str(rel))
    out.append(("FAIL" if bad else "PASS", "depth", f"paths deeper than 4: {bad[:20]}" if bad else "all 00–06/harvest paths are <= 4 components (data/<YYYY>/ exempt)"))


def check_links(root: Path, out: list):
    bad = []
    rx = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for p in files(root):
        if p.suffix.lower() != ".md": continue
        for m in rx.finditer(read(p)):
            target = m.group(1).split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "<")): continue
            if not (p.parent / target).resolve().exists():
                bad.append(f"{p.relative_to(root)} -> {target}")
    out.append(("FAIL" if bad else "PASS", "local-links", f"broken links: {bad[:30]}" if bad else "no broken relative Markdown links"))


def check_legacy_active_refs(root: Path, out: list):
    bad = []
    for p in files(root):
        rel = p.relative_to(root)
        if rel in HISTORICAL_FILES: continue
        for i, line in enumerate(read(p).splitlines(), 1):
            if any(x in line for x in LEGACY_ACTIVE) or re.search(r"(?<![A-Za-z0-9_])(?:bundles/|merged/)", line):
                if NEGATIVE_WORD_RE.search(line):
                    continue
                bad.append(f"{rel}:{i}: {line.strip()}")
    out.append(("FAIL" if bad else "PASS", "legacy-active-refs", f"active legacy references: {bad[:30]}" if bad else "no active legacy path references"))


def parse_registry(root: Path):
    s = read(root / "01_skill-discovery-integration/registry.yaml")
    # Stop at the next top-level key so archived/proposals ids are not menu ids.
    m = re.search(r"^mounts:\n(.*?)(?=^[A-Za-z_])", s, re.M | re.S)
    block = m.group(1) if m else ""
    entries = []
    current = {}
    for line in block.splitlines():
        mm = re.match(r"^\s+- id:\s*(\S+)", line)
        if mm:
            if current: entries.append(current)
            current = {"id": mm.group(1)}
            continue
        for k in ("source", "path", "status"):
            mm = re.match(rf"^\s+{k}:\s*(\S+)", line)
            if mm and current: current[k] = mm.group(1)
    if current: entries.append(current)
    canonical = re.search(r"^  fine_id_count_canonical:\s*(\d+)", s, re.M)
    return entries, int(canonical.group(1)) if canonical else None


def check_registry(root: Path, capabilities: Path | None, out: list):
    entries, expected = parse_registry(root)
    if expected is None:
        out.append(("FAIL", "registry", "fine_id_count_canonical missing"))
        return
    if len(entries) != expected:
        out.append(("FAIL", "registry", f"fine_id_count_canonical is {expected}, parsed mounts: {len(entries)}"))
        return
    out.append(("PASS", "registry", f"{expected} mount menu ids match fine_id_count_canonical"))
    if capabilities:
        missing = []
        for e in entries:
            if e.get("source") != "my-skills-capabilities": continue
            if not (capabilities / e["path"]).exists():
                missing.append(f"{e['id']} -> {e['path']}")
        out.append(("FAIL" if missing else "PASS", "registry-vs-B", f"B paths missing: {missing}" if missing else "all B mount paths exist in companion capabilities package"))
    else:
        out.append(("SKIP", "registry-vs-B", "companion B path check not requested (--capabilities omitted)"))


def check_meta(root: Path, out: list):
    version = read(root / "_medical-research-meta/VERSION.txt")
    vm = re.search(r"(CHG-\d{8}-\d{3})", version)
    map_text = read(root / "_medical-research-meta/INTEGRATION_MAP.md")
    bad = []
    if not vm: bad.append("VERSION.txt has no CHG id")
    else:
        if vm.group(1) not in map_text: bad.append(f"{vm.group(1)} missing from INTEGRATION_MAP.md")
    if map_text.count("```") % 2: bad.append("INTEGRATION_MAP.md has unbalanced fenced blocks")
    out.append(("FAIL" if bad else "PASS", "meta", "; ".join(bad) if bad else f"VERSION and Integration Map agree at {vm.group(1)}"))



ALIAS_FILE = Path("01_skill-discovery-integration/legacy_aliases.yaml")
# Physical path units, not fine ids. A stale-id hit is a backtick token of this shape.
V3_ID_RE = re.compile(r"`(\d{2}-[a-z][a-z0-9-]*)`")
PATH_UNITS = {
    "02-data-processing",
    "03-research",
    "04-analysis",
    "05-manuscript",
    "06-review",
}
WORKFLOW_DIR = Path("00_orchestrator/workflows")


def load_alias_map(root: Path) -> dict:
    """Retired call-site id -> canonical registry fine id. Shared with docs."""
    path = root / ALIAS_FILE
    if not path.is_file():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    raw = data.get("aliases") or {}
    return {str(k): str(v) for k, v in raw.items()}


def canonical_fine_ids(root: Path) -> set:
    entries, _expected = parse_registry(root)
    ids = {e["id"] for e in entries if e.get("id")}
    reg = yaml.safe_load((root / "01_skill-discovery-integration/registry.yaml").read_text(encoding="utf-8"))
    for row in reg.get("archived") or []:
        if row.get("id"):
            ids.add(row["id"])
    return ids


def resolve_alias(token: str, aliases: dict) -> str:
    """Runtime resolution: alias -> canonical. Unknown tokens return themselves."""
    return aliases.get(token, token)


def stale_id_hits(text: str, canonical: set, aliases: dict, *, workflow: bool) -> list:
    """Ids that are neither canonical nor a mapped alias.

    A mapped alias is not an unknown id. Inside 00 workflows it is still a
    call-site error: workflows must cite the canonical id.
    """
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        historical = bool(NEGATIVE_WORD_RE.search(line))
        for m in V3_ID_RE.finditer(line):
            tok = m.group(1)
            if tok in PATH_UNITS or tok in canonical:
                continue
            if tok in aliases:
                if workflow and not historical:
                    hits.append(f"{i}:{tok}->use {aliases[tok]}")
                continue
            if historical:
                continue
            hits.append(f"{i}:{tok}")
    return hits


def check_stale_ids(root: Path, out: list):
    aliases = load_alias_map(root)
    canonical = canonical_fine_ids(root)
    bad_targets = sorted(f"{k}->{v}" for k, v in aliases.items() if v not in canonical)
    if bad_targets:
        out.append(("FAIL", "stale-ids", f"alias targets are not canonical: {bad_targets}"))
        return
    bad = []
    for p in files(root, STALE_EXTS):
        rel = p.relative_to(root)
        if rel in HISTORICAL_FILES or rel == ALIAS_FILE:
            continue
        if "tests" in rel.parts:
            continue
        if p.suffix.lower() not in STALE_EXTS:
            continue
        workflow = WORKFLOW_DIR in rel.parents or rel.parent == WORKFLOW_DIR
        hits = stale_id_hits(p.read_text(encoding="utf-8", errors="ignore"), canonical, aliases, workflow=workflow)
        for hit in hits:
            bad.append(f"{rel.as_posix()}:{hit}")
    out.append((
        "FAIL" if bad else "PASS",
        "stale-ids",
        f"unknown or workflow-alias ids: {bad[:30]}" if bad else "no stale fine ids outside canonical ids and legacy_aliases.yaml",
    ))


def check_qc_scaffold(root: Path, out: list):
    req = [
        "skill-harvest/qc/SKILL.md", "skill-harvest/qc/rules.md", "skill-harvest/qc/repo-qc.md",
        "skill-harvest/scripts/repo_qc.py", "skill-harvest/templates/qc-evolution.html",
        "skill-harvest/data/qc-events/README.md",
    ]
    bad = [x for x in req if not (root / x).is_file()]
    qc = read(root / "skill-harvest/qc/SKILL.md")
    if "Never auto-modify" not in qc or "Do **not** create `07_QC`" not in qc:
        bad.append("qc/SKILL.md governance guard missing")
    out.append(("FAIL" if bad else "PASS", "harvest-qc", f"missing/invalid: {bad}" if bad else "QC scaffold and anti-auto-modification guard are present"))


def run_tests(root: Path, out: list):
    proc = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "_medical-research-meta/tests", "-p", "test_*.py"], cwd=root, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if proc.returncode == 0:
        out.append(("PASS", "unit-tests", "unittest discovery passed"))
    else:
        out.append(("FAIL", "unit-tests", proc.stdout[-4000:]))


LIVE_FINE_ID_COUNT = 52  # measured live registry mounts on 2026-10-03; do not edit the registry to force this
FINE_TOKEN_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`")
RUNTIME_DOC_PATHS = (
    Path("00_orchestrator/runtime-flow.md"),
    Path("00_orchestrator/runtime-flow.mmd"),
    Path("00_orchestrator/route-contract.yaml"),
)
NODE_ID_RE = re.compile(r"([A-Za-z_][A-Za-z0-9_]*)")


def _node_id(token: str) -> str:
    match = NODE_ID_RE.search(token or "")
    return match.group(1) if match else ""


def _filled(value) -> bool:
    if value is None:
        return False
    text = str(value).strip().strip("'\"")
    return text not in {"", "~", "null", "None"}


def markdown_stems(root: Path) -> set:
    stems = set()
    for path in root.rglob("*.md"):
        if set(path.parts) & SKIP_DIRS:
            continue
        stems.add(path.stem)
    return stems


def runtime_doc_paths(root: Path):
    paths = [root / rel for rel in RUNTIME_DOC_PATHS]
    paths.extend(sorted((root / "00_orchestrator" / "workflows").glob("*.md")))
    return [path for path in paths if path.is_file()]


def runtime_fine_id_problems(root: Path) -> list:
    canonical = canonical_fine_ids(root)
    aliases = load_alias_map(root)
    problems = []
    for key, target in sorted(aliases.items()):
        if target not in canonical:
            problems.append(f"alias {key} -> {target} is not in the registry")
    stems = markdown_stems(root)
    for path in runtime_doc_paths(root):
        rel = path.relative_to(root).as_posix()
        for lineno, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if NEGATIVE_WORD_RE.search(line):
                continue
            for token in FINE_TOKEN_RE.findall(line):
                if token in canonical:
                    continue
                if token in aliases and aliases[token] in canonical:
                    continue
                if token in PATH_UNITS or token in stems:
                    continue
                if re.search(rf"`{re.escape(token)}`\s+sub-check", line):
                    continue
                problems.append(f"{rel}:{lineno}:{token}")
    return problems


def session_pick_problems(root: Path) -> list:
    entries, _expected = parse_registry(root)
    by_id = {entry["id"]: entry for entry in entries if entry.get("id")}
    proposed = {entry["id"] for entry in entries if entry.get("status") == "PROPOSED"}
    problems = []
    generated = root / "01_skill-discovery-integration" / "MOUNTED_SKILLS.md"
    text = generated.read_text(encoding="utf-8") if generated.is_file() else ""
    match = re.search(r"^## Session-pick[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not match:
        problems.append("generated MOUNTED_SKILLS.md has no Session-pick section")
    else:
        body = match.group(1)
        if re.search(r"\bPROPOSED\b", body):
            problems.append("PROPOSED appears in the MOUNTED_SKILLS session-pick section")
        for token in FINE_TOKEN_RE.findall(body):
            if token in proposed:
                problems.append(f"session-pick lists PROPOSED id {token}")
    state_path = root / "00_orchestrator" / "templates" / "project-state.yaml"
    try:
        state = yaml.safe_load(state_path.read_text(encoding="utf-8")) or {}
    except Exception as exc:
        problems.append(f"project-state template did not parse: {exc}")
        return problems
    picked = ((state.get("mounts") or {}).get("session_picked_fine_ids") or [])
    if not isinstance(picked, list):
        problems.append("session_picked_fine_ids is not a list")
        return problems
    for token in picked:
        if token in proposed or by_id.get(token, {}).get("status") == "PROPOSED":
            problems.append(f"project-state selected PROPOSED id {token}")
    return problems


def mounted_path_problems(root: Path) -> list:
    entries, _expected = parse_registry(root)
    problems = []
    for entry in entries:
        if entry.get("status") != "MOUNTED":
            continue
        if not _filled(entry.get("path")) or not _filled(entry.get("source")):
            problems.append(entry.get("id", "?"))
    return problems


def repo_map_problems(root: Path) -> list:
    html_path = root / "00_orchestrator" / "repo-map.html"
    if not html_path.is_file():
        return ["repo-map.html missing"]
    text = html_path.read_text(encoding="utf-8", errors="ignore")
    problems = []
    if not re.search(r"Generated \d{4}-\d{2}-\d{2} \d{2}:\d{2}\b", text):
        problems.append("repo-map.html has no generated timestamp")
    script = root / "00_orchestrator" / "scripts" / "gen_repo_map.py"
    proc = subprocess.run(
        [sys.executable, str(script), "--check"],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if proc.returncode != 0:
        detail = (proc.stdout or "gen_repo_map.py --check failed").strip()
        problems.append(detail)
    return problems


def mermaid_edges(text: str):
    edges = []
    for raw in text.splitlines():
        line = raw.split("%%", 1)[0].strip()
        if "-->" not in line:
            continue
        left, right = line.split("-->", 1)
        label = ""
        labeled = re.match(r"\s*\|([^|]*)\|\s*(.*)$", right)
        if labeled:
            label, right = labeled.group(1), labeled.group(2)
        dst = _node_id(right)
        for part in left.split("&"):
            src = _node_id(part)
            if src and dst:
                edges.append((src, dst, label.strip()))
    return edges


def mount_route_problems(text: str) -> list:
    """Mount-dependent routes must reach Ready only through the mount G0 node."""
    edges = mermaid_edges(text)
    problems = []
    mountq = set(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\{[^}\n]*session_picked_fine_ids", text))
    g0 = set(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\{\{G0\}\}", text))
    ready = set(re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\[挂载就绪\]", text))
    ready.update(dst for _src, dst, _label in edges if dst == "Ready")
    if not mountq:
        problems.append("no MountQ node")
    if not g0:
        problems.append("no G0 node")
    if not ready:
        problems.append("no Ready node")
    if problems:
        return problems
    adj = {}
    for src, dst, label in edges:
        adj.setdefault(src, []).append(dst)
        if src in mountq and "是" in label and dst not in g0:
            problems.append(f"MountQ yes edge goes to {dst}, not G0")
        if src in mountq and dst in ready:
            problems.append("MountQ links directly to Ready")
    starts = set(mountq)
    starts.update(src for src, dst, _label in edges if dst in mountq)

    def walk(start: str):
        reached = []

        def visit(node: str, seen: set, passed: bool):
            if node in ready:
                reached.append(passed)
                return
            for nxt in adj.get(node, []):
                if nxt in seen:
                    continue
                visit(nxt, seen | {nxt}, passed or nxt in g0)

        visit(start, {start}, start in g0)
        return reached

    for start in sorted(starts):
        reached = walk(start)
        if start in mountq and not reached:
            problems.append(f"{start} never reaches Ready")
        if any(not passed for passed in reached):
            problems.append(f"{start} reaches Ready without G0")
    return problems


def check_five_fixes(root: Path, out: list):
    entries, expected = parse_registry(root)
    ids = [entry.get("id", "") for entry in entries]
    dupes = sorted({item for item in ids if ids.count(item) > 1})
    count_ok = len(entries) == LIVE_FINE_ID_COUNT and not dupes and expected == LIVE_FINE_ID_COUNT
    out.append((
        "PASS" if count_ok else "FAIL",
        "fine-id-count",
        f"measured live mounts {len(entries)}; canonical field {expected}; expected measured count {LIVE_FINE_ID_COUNT}"
        + (f"; duplicate ids {dupes}" if dupes else ""),
    ))
    unique_ok = len(ids) == len(set(ids)) and all(ids)
    out.append((
        "PASS" if unique_ok else "FAIL",
        "fine-id-unique",
        "mount fine ids are unique" if unique_ok else f"duplicate or blank fine ids: {dupes}",
    ))
    runtime_bad = runtime_fine_id_problems(root)
    out.append((
        "FAIL" if runtime_bad else "PASS",
        "runtime-fine-ids",
        f"unknown runtime fine ids: {runtime_bad[:30]}" if runtime_bad else "runtime docs cite registry ids or aliases whose targets exist",
    ))
    picked_bad = session_pick_problems(root)
    out.append((
        "FAIL" if picked_bad else "PASS",
        "proposed-not-selected",
        f"PROPOSED in a session-pick list: {picked_bad}" if picked_bad else "PROPOSED ids are outside session-pick and project-state selected lists",
    ))
    path_bad = mounted_path_problems(root)
    out.append((
        "FAIL" if path_bad else "PASS",
        "mounted-path-source",
        f"MOUNTED entries missing path or source: {path_bad}" if path_bad else "every MOUNTED entry has a path and a source",
    ))
    map_bad = repo_map_problems(root)
    out.append((
        "FAIL" if map_bad else "PASS",
        "repo-map-generated",
        f"{map_bad}" if map_bad else "repo-map.html has a generated timestamp and gen_repo_map.py --check passed",
    ))
    flow = (root / "00_orchestrator" / "runtime-flow.mmd").read_text(encoding="utf-8")
    route_bad = mount_route_problems(flow)
    out.append((
        "FAIL" if route_bad else "PASS",
        "mount-route-g0",
        f"mount route misses G0: {route_bad}" if route_bad else "every mount-dependent route reaches Ready only through G0",
    ))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".")
    ap.add_argument("--capabilities", help="path to MY-SKILLS-capabilities for registry cross-check")
    ap.add_argument("--no-tests", action="store_true")
    ap.add_argument("--json", dest="json_path")
    ap.add_argument("--report", dest="report_path")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    capabilities = Path(args.capabilities).resolve() if args.capabilities else None
    results = []
    check_structure(root, results)
    check_tracked_pycache(root, results)
    check_frontmatter(root, results)
    check_depth(root, results)
    check_links(root, results)
    check_legacy_active_refs(root, results)
    check_stale_ids(root, results)
    check_registry(root, capabilities, results)
    check_meta(root, results)
    check_qc_scaffold(root, results)
    check_five_fixes(root, results)
    if not args.no_tests: run_tests(root, results)
    fail = any(s == "FAIL" for s, _, _ in results)
    payload = {"repository": str(root), "status": "FAIL" if fail else "PASS", "checks": [{"status": s, "check": c, "detail": d} for s,c,d in results]}
    print(f"REPO-QC: {payload['status']}")
    for s,c,d in results: print(f"[{s}] {c}: {d}")
    if args.json_path: Path(args.json_path).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    if args.report_path:
        lines = [f"# MY-SKILLS Repository QC\n", f"Status: **{payload['status']}**\n"]
        lines += [f"- **{c}** — **{s}**: {d}" for s,c,d in results]
        Path(args.report_path).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 1 if fail else 0

if __name__ == "__main__":
    raise SystemExit(main())
