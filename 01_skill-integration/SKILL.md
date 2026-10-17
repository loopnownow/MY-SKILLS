---
name: skill-integration
description: >
  Mount and index external Skills. Use for coarse/fine ids, registry lookup,
  session pick, hybrid mount recipes, and the `{mounts_cap}` cache boundary. Infrastructure
  only. Never literature research, statistics, manuscript writing, or peer review.
  Not GitHub discovery (archived). Not skill evolution (MY-RULES skill-evolution).
  Mount pointers live only here. Default mount is B (MY-SKILLS-capabilities).
  Every independent run needs a mount decision; reuse session_picked_fine_ids
  when they already cover the task. Never auto-mount a non-B source. Non-B fine
  ids are mixed per registry status. OpenClaw is not a default mount source.
---

# Skill Integration

## Purpose

Integration ledger only — resolve **where a capability comes from** (coarse/fine ids, registry, mounts, hybrid recipes). Professional work stays in 02–06.
**All mount pointers live here.** Machine: `registry.yaml` + one yaml per external source under `sources/`.
Human board: `mounts/` (`README.md`, **`hybrid-mount-pointers.md`**, `presets.md` + `presets/*.yaml`, `b.md` / `medsci.md` / `scientific.md` / `aipoch.md` / `nature.md`).
Domain skills call fine ids; they do not keep a second pointer table.
`{mounts_cap}/` (`D:/0Grok/0doc/04-lab-reference/mounts-cap`) is a verified local cache boundary (not SSOT). Download is not a mount.

## Architecture (v4 · CHG-20260913-001)

- Coarse ids = welded stage buckets（文献检索 … 审稿回复）. Count lives in `registry.yaml` `coarse_id_count`. Not A folder renames.
- Fine ids = session-pick mount points. Count lives in `fine_id_count_canonical`. The pick menu is status `MOUNTED` only.
- **Hybrid mount:** different fine ids may use different packages; never mix packages inside one fine id. Non-B rows are mixed PROPOSED/MOUNTED per registry, not an all-PROPOSED backup set.
- **`fine_id` is the capability interface. `path` is the physical unit. `path_shared: true` means one path backs several fine ids. Do not split that folder.**
- A domains stay `00_orchestrator` … `06_review`. Personal layers stay in A. Skill evolution policy: MY-RULES `skill-evolution.md`.
- 选刊 stays Victor / `03_research/find-journal` — do not move into 05.

## Pointers

| Path | Role |
|---|---|
| `registry.yaml` | Routing index (coarse / fine / status / path) |
| `MOUNTED_SKILLS.md` | Generated session-pick human table |
| `mounts/` | Human board: presets, per-source notes, hybrid recipe narrative |
| `mounts/hybrid-mount-pointers.md` | Hybrid mount recipes (emphasize) |
| `sources/` | One yaml per external source |
| `legacy_aliases.yaml` | Retired call-site id → canonical fine id |
| `scripts/gen_mounted_skills.py` | Regenerates `MOUNTED_SKILLS.md` |
| `references/id-rules.md` | Canonical ID Rule |
| `references/lifecycle-cache.md` | Cache · Mount · Active; local cache; external mount lifecycle |
| `references/session-pick.md` | Default mount; session pick; empty-mount; resolution order |
| `references/hard-rules.md` | Forbidden combinations; hard rules; fine-id ceiling; load_priority |
| `references/capability-contract.example.yaml` | Capability-contract template (ex-`interface.yaml`) |

Discovery archived; if rare need, see `D:\0del\00_orchestrator_reorg_20261017\01_discovery-eval.md` / ask owner — do not run GitHub discovery from 01 by default. Registry `archived:` ids stay off the pick menu.

## Red lines (summary)

Full text: [`references/hard-rules.md`](references/hard-rules.md).

- Never auto-mount a **non-B** Skill; Never bulk-download MedSci / Scientific / AIPOCH / Nature.
- Never remount ARS/OpenClaw (`removed-from-catalog`); never mix packages inside one fine id.
- `PROPOSED` is not pickable; personal layers are not mount picks; sentence authority stays A/B05 personal.
- Reviewer engines output findings only (no bypass of A06); Nature polish must not overwrite author voice.
- Empty mount → notify → re-search → confirm (see [`references/session-pick.md`](references/session-pick.md)).
- Fine-id ceiling / load_priority: see hard-rules; do not restate counts in prose.
- `{mounts_cap}/` cache only; Download is not a mount.
