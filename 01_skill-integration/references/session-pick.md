# Default mount · Session pick · Empty-mount · Resolution

## Default mount

**Default unique runtime source = `my-skills-base`**
([loopnownow/MY-SKILLS-base](https://github.com/loopnownow/MY-SKILLS-base)).

Session recipes in `references/presets/*.yaml` are **first-pass fine-ID lists**, not package menus:
`review-hybrid-default`, `evidence-deep-L2`, `manuscript-final-W2`, `external-review-R1`.
Still ask each run; user may change picks. Attribution is per skill path, not a whole upstream pack.

Non-base sources: **default deny** (`references/hybrid-mount-pointers.md`).
OpenClaw / ARS: `ars_openclaw_policy: removed-from-catalog` — never remount; not in session pick.

**Mapping is not a mount.** Status stays `PROPOSED` until the user confirms (revive is owner-gated).

## Session mount pick（独立运行一次决策 · 细 ID 多选）

Registry status `MOUNTED` = catalog-approved and session-selectable. It is not attached until this run selects it.
`PROPOSED` is not pickable.
`session_picked_fine_ids` = selected this run. Active = actually loaded.

Every independent run needs a mount decision. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock and do not ask. Otherwise enter this section. A single-node personal-layer / A top-layer task with no mounted dependency does not ask (example: polish one sentence). **A top layers are not capability mounts.**

1. Classify the task. Propose **relevant coarse bucket(s)** then **MOUNTED candidate fine ids**.
2. Show each candidate as one line: **粗 ID · 细 ID · B path · 做什么**. Default source is always base.
3. **Ask the user to multi-select fine ids**. For 写稿/润色/修订论著, **pre-check `manuscript-final-W2`**. For 预审/审稿/回复审稿, **pre-check `review-hybrid-default`**. Then allow edits. Also offer: 用该默认配方 / 候选全选 B / 只要个人层不外挂. Do **not** offer a non-base package menu. Empty picked path → tell the user; do not silent-fallback.
4. Load **only** the picked fine ids. Ensure bytes in `{mounts_cap}/b/` (or live B clone) first. Unpicked stay unloaded. Never bulk-download non-base trees.
5. If a picked path is empty → empty-mount protocol. Do not silently substitute another source.
6. Do not change `registry.yaml` just because this run wanted a non-base path.

Silence is not approval. Never auto-mount a non-base source. Personal layers (Aitor-format, de-AI, 0RAD, Voice A/B) and A top layers are not mount picks.
Say **默认挂载 B = 本仓**, not 空挂.

## Empty-mount protocol

If a listed mount is empty (path missing, zero files, clone failed, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search (B first, then ask for a local path).
3. **Confirm with the user** before changing `registry.yaml` or switching source.

Never silently fall back to a non-base pack or invent a local copy.

## Resolution order

1. Read this skill's `registry.yaml` (coarse buckets + fine `mounts:`).
2. Resolve each fine id against `source: my-skills-base` (default unique). Archived ids are not in the default menu.
3. If that path is empty or missing → empty-mount protocol.
4. Non-base revive requires explicit owner approval (default deny).
5. Evaluate capability, boundaries, dependencies, and overlap.
6. After approval the registry status becomes `MOUNTED`. Update `registry.yaml` and regenerate `MOUNTED_SKILLS.md`.
