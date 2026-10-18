---
name: skill-index
description: >
  Registry / session-pick / path resolve / legacy aliases / mounts_cap cache
  boundary. Default unique runtime source is in-repo my-skills (NN_slug/base/). Use for coarse/fine ids, registry lookup, session pick,
  and resolving fine-id paths. Infrastructure only. Never literature research,
  statistics, manuscript writing, or peer review. Not GitHub discovery
  (archived). Not skill evolution (MY-RULES skills.md). A top layers are not
  capability mounts — 00 owns base→QC→A flow. Non-base sources default deny.
---

# Skill Index (01)

Folder path stays `01_skill-integration/` (rename deferred — too many call-site
refs). Skill name / role: **skill-index**.

## Purpose

01 is the **routing index** only (registry / session-pick / path resolve). No mount-package board; capabilities via A (personal + in-repo base/) only. Session lock key: `session_picked_fine_ids`.

| Concern | Owner |
|---|---|
| Registry / fine-id menu / path resolve / legacy aliases | **01** |
| `{mounts_cap}/` pack-cache boundary (former `b/` obsolete for live) | **01** |
| base fine-ID first-pass → 00 QC → A top-layer re-loops | **00** |
| A personal / top layers (`00`–`07`) | **A** — not registered as capability mounts |

Professional work stays in 02-07. Capability bodies live in-repo under
`NN_slug/base/` (`source: my-skills`). Domain skills call fine ids; they do not
keep a second pointer table.

## Default unique runtime source

**`my-skills`** (in-repo A `NN_slug/base/`).

- Session-pick unit = `fine_id` (status `MOUNTED` only). Reuse `session_picked_fine_ids` when they already cover the task.
- Path resolve: `registry.yaml` -> in-repo path under `NN_slug/base/`.
- Non-base sources: **default deny**. See `references/hybrid-mount-pointers.md`.
- ARS / OpenClaw: `ars_openclaw_policy: removed-from-catalog` -- never remount.
- A top layers are **not** mount picks.

## Pointers

| Path | Role |
|---|---|
| `registry.yaml` | Routing index (coarse / fine / status / path) |
| `MOUNTED_SKILLS.md` | Generated session-pick human table |
| `references/hybrid-mount-pointers.md` | Non-base exceptions = default deny |
| `references/presets/*.yaml` | First-pass fine-ID session recipes (not a package board) |
| `sources/README.md` | Source yaml status (B yaml retired) |
| `legacy_aliases.yaml` | Retired call-site id → canonical fine id |
| `scripts/gen_mounted_skills.py` | Regenerates `MOUNTED_SKILLS.md` |
| `references/id-rules.md` | Canonical ID Rule |
| `references/lifecycle-cache.md` | Cache · Mount · Active; base byte cache |
| `references/session-pick.md` | Default base; session pick; empty-mount; resolve |
| `references/hard-rules.md` | Forbidden combinations; ceiling; load_priority |
| `references/capability-contract.example.yaml` | Capability-contract template |
| `references/ab-top-vs-b-loops.md` | Pointer to 00 A/B layering |

Discovery archived; rare need → `D:\0del\00_orchestrator_reorg_20261017\01_discovery-eval.md`
or ask owner. Registry `archived:` ids stay off the pick menu.

## Architecture notes

- Coarse ids = welded stage buckets. Count: `registry.yaml` `coarse_id_count`.
- Fine ids = session-pick mount points. Count: `fine_id_count_canonical`.
- `fine_id` = capability interface; `path` = physical unit; `path_shared: true`
  = one path backs several fine ids — do not split that folder.
- A domains stay `00_orchestrator`–`07_response`. Personal layers stay in A.
- Skill evolution: MY-RULES `skills.md`. 选刊 stays Victor / `03_research/base/find-journal/`.

## Red lines (summary)

Full text: [`references/hard-rules.md`](references/hard-rules.md).

- Never auto-mount a **non-base** source; non-base = default deny.
- Never remount ARS/OpenClaw; never invent a second runtime package menu.
- `PROPOSED` is not pickable; personal / A top layers are not mount picks.
- Empty mount → notify → re-search → confirm ([`references/session-pick.md`](references/session-pick.md)).
- `{mounts_cap}/` is historical pack-cache only; live bodies are in-repo `NN_slug/base/`. Download is not a mount.
