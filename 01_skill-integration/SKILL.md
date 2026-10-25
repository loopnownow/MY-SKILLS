---
name: skill-index
description: >
 Registry / session-pick / path resolve / legacy aliases.
 Bodies live in-repo under NN_slug/base/. Use for coarse/fine ids, registry lookup, session pick,
 and resolving fine-id paths. Infrastructure only. Never literature research,
 statistics, manuscript writing, or peer review. Not GitHub discovery.
 Not skill evolution (MY-RULES skills.md). Top layers are not
 capability rows — 00 owns base→QC→personal flow.
---

# Skill Index (01)

Folder path stays `01_skill-integration/` (rename deferred — too many call-site
refs). Skill name / role: **skill-index**.

## Purpose

01 is the **routing index** only (registry / session-pick / path resolve). Capabilities live in personal layers and in-repo `base/`. Session lock key: `session_picked_fine_ids`.

| Concern | Owner |
|---|---|
| Registry / fine-id menu / path resolve / legacy aliases | **01** |
| base fine-ID first-pass → 00 QC → personal top-layer re-loops | **00** |
| Personal / top layers (`00`–`07`) | personal seats — not registered as capability rows |

Professional work stays in 02-07. Capability bodies live in-repo under
`NN_slug/base/` (`source: my-skills`). Domain skills call fine ids; they do not
keep a second pointer table.

## In-repo bodies

**`my-skills`** (in-repo `NN_slug/base/`).

- Session-pick unit = `fine_id` (status `MOUNTED` only). Reuse `session_picked_fine_ids` when they already cover the task.
- Path resolve: `registry.yaml` path. Bodies are under `NN_slug/base/`, except `check-reporting` at `05_manuscript/qc/check-reporting/`.
- Top layers are **not** session picks.

## Pointers

| Path | Role |
|---|---|
| `registry.yaml` | Routing index (coarse / fine / status / path) |
| `legacy_aliases.yaml` | Retired call-site id → canonical fine id |
| `references/id-rules.md` | Canonical ID Rule |
| `references/lifecycle-cache.md` | Index · selected · loaded |
| `references/session-pick.md` | Session pick; empty path; resolve |
| `references/hard-rules.md` | Forbidden combinations; fine-id expansion |
| `references/capability-contract.example.yaml` | Capability-contract template |
| `references/base-vs-personal-top-loops.md` | Pointer to 00 layering |

Retired fine ids live only in `legacy_aliases.yaml` — never session-pick them.

## Architecture notes

- Coarse ids = welded stage buckets. Count: `registry.yaml` `coarse_id_count`.
- Fine ids = session-pick points. Count: `fine_id_count_canonical`.
- `fine_id` = capability interface; `path` = physical unit. They are aligned: every session-pick directory is named after its canonical fine id (2026-10-20), enforced by `tests/test_registry_contract.py`. Writing bodies use `base/<fine_id>/`. `check-reporting` is `05_manuscript/qc/check-reporting/`. Venue house style is in `write-paper`. The only local pack with no fine id of its own (`base/vocab/`) is listed at the bottom of `registry.yaml`.
- `path_shared: true` = one path backs several fine ids — do not split that folder. No live row sets it today; `batch-cohort` was archived into `clean-data` on 2026-10-20.
- Domains stay `00_orchestrator`–`07_response`. Personal layers stay beside `base/`.
- Skill evolution: MY-RULES `skills.md`. journal selection stays Victor / `03_research/base/find-journal/`.

## Red lines (summary)

Full text: [`references/hard-rules.md`](references/hard-rules.md).

- `PROPOSED` is not pickable; personal / top layers are not session picks.
- Empty path → notify → re-search → confirm ([`references/session-pick.md`](references/session-pick.md)).

## Owner text harvest

Default filter for owner-supplied text: `references/text-harvest-by-fine-id.md` (fine-ID → corpus elements / process / cautions). Disk SSOT: `skill-harvest/HARVEST-STANDARD.md` §7.
