#!/usr/bin/env python3
"""Generate MOUNTED_SKILLS.md from registry.yaml (single source of truth).

Problem this fixes: the coarse-id -> fine-id table used to be hand-copied
into MOUNTED_SKILLS.md and had to be kept in sync with registry.yaml by
memory. Run this script after any edit to registry.yaml's `mounts:`,
`reference_only:`, or `archived:` sections, instead of hand-editing the
table in MOUNTED_SKILLS.md.

Dependency: PyYAML (`pip install pyyaml`).

Usage:
    python3 01_skill-discovery-integration/scripts/gen_mounted_skills.py [--check]

    --check   exit 1 if the generated file would differ from what's on disk
              (use in CI / pre-commit instead of writing).
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

Canonical pointers live in 01 (`registry.yaml`). This file is the human table,
**generated** by `scripts/gen_mounted_skills.py` — do not hand-edit the tables below.
Default source: [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).

Empty mount → notify → re-search → confirm. Never silently fall back.
Never auto-mount a non-B source. `PROPOSED` is not `MOUNTED`. Nature LICENSE Apache-2.0 verified (ask-each-run + bytes).
`ars_openclaw_policy: removed-from-catalog` — never remount; not in session pick.
**Every run:** ask which **fine ids** to attach under the relevant coarse buckets (`session_mount: ask-each-run`).
Local bytes: `mounts-cap/` (B full; other sources on-demand). Download ≠ mount.
Say 默认挂载 B 包/本仓 — not 空挂.

v{version}: **{coarse} coarse + {fine} fine** ({mounted_count} session-pick mounts + {ref_count} reference-only). Personal layers stay in A `00`–`06`.
Migration: [mounts/MIGRATION_v3_to_v4.md](mounts/MIGRATION_v3_to_v4.md). Backup: `_history/registry.v3.30.yaml`.

## Session-pick fine ids by coarse bucket
"""

FOOTER_TEMPLATE = """
## Reference-only (not session mounts)

| Id | Label | Applied to |
|---|---|---|
{ref_rows}

## Archived (not in default menus)

{archived_rows}

## Backup candidates

- MedSci / Scientific / AIPOCH / Nature: `PROPOSED` (Nature LICENSE Apache-2.0 verified).
- ARS/OpenClaw: removed from catalog (`ars_openclaw_policy: removed-from-catalog`).

Mapping is not a source-wide mount.
"""


def load_registry() -> dict:
    return yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))


def status_label(m: dict) -> str:
    status = m.get("status", "")
    flag = m.get("license_flag")
    return f"{status} · {flag}" if flag else status


def render(reg: dict) -> str:
    meta = reg["meta"]
    coarse_ids = reg["coarse_ids"]
    mounts = reg["mounts"]
    ref_only = reg.get("reference_only", [])
    archived = reg.get("archived", [])

    mounted_count = sum(1 for m in mounts if m.get("status") == "MOUNTED")
    proposed_count = sum(1 for m in mounts if m.get("status") == "PROPOSED")

    version = meta["version"]
    if version.endswith(".0"):
        version = version[:-2]

    out = [HEADER.format(
        version=version,
        coarse=meta["coarse_id_count"],
        fine=meta["fine_id_count_canonical"],
        mounted_count=len(mounts),
        ref_count=len(ref_only),
    )]

    for coarse in coarse_ids:
        cid = coarse["id"]
        rows = [m for m in mounts if m.get("coarse") == cid]
        if not rows:
            continue
        out.append(f"\n### {cid}\n")
        out.append("| Fine id | Label | Source | Path | Status |")
        out.append("|---|---|---|---|---|")
        for m in rows:
            out.append(
                f"| `{m['id']}` | {m['label']} | {m['source']} | `{m['path']}` | {status_label(m)} |"
            )
        out.append("")

    ref_rows = "\n".join(
        f"| `{r['id']}` | {r['label']} | `{r['applied_to']}` |" for r in ref_only
    )
    archived_rows = "\n".join(
        f"- `{a['id']}` — {a['reason']}" for a in archived
    )

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

    OUTPUT.write_text(generated, encoding="utf-8")
    print(f"Wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
