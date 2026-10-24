# Forbidden combinations · Hard rules · Fine-id expansion

## Forbidden combinations (mount red lines)

These are **mount-time** bans, not skill deletions:

1. Do **not** offer a multi-package runtime menu. Default unique source = `my-skills` (in-repo `NN_slug/base/`).
2. Do **not** let multiple authoring engines **directly edit** the same manuscript sentences in one pass — one primary authoring authority (A/B05 personal); others are verifier / QC / venue only.
3. Reviewer engines output **findings only**; they must not edit the manuscript bypassing A06.
4. Venue polishing must not overwrite base write-paper / A personal author voice.
5. Do not remount packs purged from catalog (`ars_openclaw_policy: removed-from-catalog`).
6. Non-base exceptions = **default deny** (see `references/hybrid-mount-pointers.md`).

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review (01 is index only).
- Never auto-install or auto-mount a **non-base** Skill.
- Never bulk-download non-base packs.
- Never remount ARS/OpenClaw (removed from catalog).
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal / A top layer because an external Skill is more general.
- `PROPOSED` is not `MOUNTED`.
- Personal de-AI (`05_manuscript/personal/`) is not a base mount. Generic de-AI is `humanize` (`05_manuscript/base/humanize/`). The personal forbidden list still wins.
- A top layers are not capability mounts (00 owns base→QC→A).

## Fine-id expansion

Prefer merge into an existing fine id / sub-capability / same source-path. Do not open a new fine id unless architecture review approves. Live count is `fine_id_count_canonical` in `registry.yaml` (must equal `len(mounts)`). Do not restate the number in prose.


## load_priority

Optional historical metadata. Live mounts no longer carry `load_priority`. Session pick order follows coarse grouping + agent judgment, not P0/P1/P2 folders.

