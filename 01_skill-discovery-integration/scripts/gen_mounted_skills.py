#!/usr/bin/env python3
"""Generate MOUNTED_SKILLS.md from registry.yaml (routing index).

The session-pick menu is status MOUNTED only. PROPOSED rows are optional
candidates and are not pickable. Do not hand-edit the tables below.

Dependency: PyYAML (`pip install pyyaml`).

Usage:
    python3 01_skill-discovery-integration/scripts/gen_mounted_skills.py [--check]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
SKILL_DIR = HERE.parent
REGISTRY = SKILL_DIR / "registry.yaml"
OUTPUT = SKILL_DIR / "MOUNTED_SKILLS.md"

HEADER = """# Mounted Skills Boundary (v{version})

Canonical pointers live in 01 (`registry.yaml`, the routing index). This file is the human table,
**generated** by `scripts/gen_mounted_skills.py` — do not hand-edit the tables below.
Default chassis: [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).
Non-B fine ids are mixed PROPOSED/MOUNTED per the registry rows below — not "all PROPOSED backups".
OpenClaw is not a default mount source.

Empty mount → notify → re-search → confirm. Never silently fall back.
Never auto-mount a non-B source. `PROPOSED` is not pickable. Nature LICENSE Apache-2.0 verified (ask when a new mount decision is required + bytes).
`ars_openclaw_policy: removed-from-catalog` — never remount; not in session pick.
**Mount decision:** every independent run needs one. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock. Otherwise enter 01. A single-node personal-layer task with no mounted dependency does not ask.
**Pick menu:** status `MOUNTED` only. `PROPOSED` may be listed as optional candidates, separate from the pick menu.
Local bytes: `mounts-cap/` is a verified local cache, not a source of truth. Download ≠ mount ≠ active.
Say 默认挂载 B 包/本仓 — not 空挂.

Generator stamp from `registry.yaml` (do not copy this sentence into hand-written docs): **{coarse} coarse buckets, {fine} fine ids** ({mounted_count} MOUNTED session-pick + {proposed_count} PROPOSED candidates + {ref_count} reference-only). Personal layers stay in A `00`–`06`.
Machine source: `registry.yaml`. Human boards: [mounts/README.md](mounts/README.md).

## Session-pick fine ids (status MOUNTED only)
"""

FOOTER_TEMPLATE = """
## Reference-only (not session mounts)

| Id | Label | Applied to |
|---|---|---|
{ref_rows}

## Archived (not in default menus)

{archived_rows}

## Package notes

- Non-B fine ids follow the registry status on each row (mixed PROPOSED/MOUNTED). Do not describe a whole package as uniformly PROPOSED.
- OpenClaw is not a default mount source (`ars_openclaw_policy: removed-from-catalog`).
- Nature LICENSE Apache-2.0 verified where the registry row says so.

Mapping is not a source-wide mount. `fine_id` is the capability interface; `path` is the physical unit; `path_shared` means one path backs several fine ids — do not split that folder.
"""


def load_registry() -> dict:
    return yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))


def status_label(m: dict) -> str:
    status = m.get("status", "")
    flag = m.get("license_flag")
    return f"{status} · {flag}" if flag else status


def coarse_list(reg: dict) -> list:
    coarse = reg.get("coarse_ids") or []
    if coarse:
        return coarse
    seen = []
    known = set()
    for m in reg.get("mounts") or []:
        cid = m.get("coarse")
        if cid and cid not in known:
            known.add(cid)
            seen.append({"id": cid})
    return seen


def append_table(out: list, rows: list) -> None:
    out.append("| Fine id | Label | Source | Path | Status |")
    out.append("|---|---|---|---|---|")
    for m in rows:
        out.append(
            f"| `{m['id']}` | {m['label']} | {m['source']} | `{m['path']}` | {status_label(m)} |"
        )
    out.append("")


def render(reg: dict) -> str:
    meta = reg.get("meta") or {}
    coarse_ids = coarse_list(reg)
    mounts = reg.get("mounts") or []
    ref_only = reg.get("reference_only") or []
    archived = reg.get("archived") or []

    mounted = [m for m in mounts if m.get("status") == "MOUNTED"]
    proposed = [m for m in mounts if m.get("status") == "PROPOSED"]

    version = str(meta.get("version", ""))
    if version.endswith(".0"):
        version = version[:-2]

    out = [HEADER.format(
        version=version or "?",
        coarse=meta.get("coarse_id_count", len(coarse_ids)),
        fine=meta.get("fine_id_count_canonical", len(mounts)),
        mounted_count=len(mounted),
        proposed_count=len(proposed),
        ref_count=len(ref_only),
    )]

    for coarse in coarse_ids:
        cid = coarse["id"]
        rows = [m for m in mounted if m.get("coarse") == cid]
        if not rows:
            continue
        out.append(f"\n### {cid}\n")
        append_table(out, rows)

    out.append("\n## Optional candidates (status PROPOSED — not pickable)\n")
    out.append("Not a pick menu. List only. Promoting one to MOUNTED is a registry change, not a session pick.\n")
    any_proposed = False
    for coarse in coarse_ids:
        cid = coarse["id"]
        rows = [m for m in proposed if m.get("coarse") == cid]
        if not rows:
            continue
        any_proposed = True
        out.append(f"\n### {cid}\n")
        append_table(out, rows)
    if not any_proposed:
        out.append("\nNone.\n")

    ref_rows = "\n".join(
        f"| `{r['id']}` | {r['label']} | `{r['applied_to']}` |" for r in ref_only
    ) or "| — | — | — |"
    archived_rows = "\n".join(
        f"- `{a['id']}` — {a['reason']}" for a in archived
    ) or "- (none)"

    out.append(FOOTER_TEMPLATE.format(ref_rows=ref_rows, archived_rows=archived_rows))
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    reg = load_registry()
    generated = render(reg)

    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != generated:
            print("MOUNTED_SKILLS.md is stale vs registry.yaml. Run without --check to regenerate.")
            return 1
        print("MOUNTED_SKILLS.md matches registry.yaml.")
        return 0

    OUTPUT.write_text(generated, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
