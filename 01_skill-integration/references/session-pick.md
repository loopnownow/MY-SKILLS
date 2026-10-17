# Default mount · Session pick · Empty-mount · Resolution

## Default mount

**Session recipes:** `review-hybrid-default` (R-style); also `evidence-deep-L2`, `manuscript-final-W2`, `external-review-R1` in `mounts/presets.md`. Default review recipe: in `mounts/presets.md` (machine core `mounts/presets/review-hybrid.yaml`) — B chassis, Scientific `verify-refs` (`citation-management`), and B `analyze-stats` (`stats-guide`). Scientific `scientific-critical-thinking` is an optional PROPOSED overlay. This preset has no Nature overlay. Still ask each run; user may change picks. Attribution and fetch are **per pack skill** (see preset `skills:`), not whole source.

**Default source is B:** [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities).
MedSci, Scientific, AIPOCH, and Nature are hybrid sources: each fine id is PROPOSED or MOUNTED as the registry row says, never "all PROPOSED backups". OpenClaw is not a default mount source (`ars_openclaw_policy: removed-from-catalog` — never remount; not in session pick).
Nature LICENSE Apache-2.0 verified 2026-09-14; MOUNTED fine ids still need ask-each-run + `{mounts_cap}/` bytes — do not claim MOUNTED if bytes absent.

**Mapping is not a mount.** Status stays `PROPOSED` until the user confirms.

## Session mount pick（独立运行一次决定 · 细 ID 多选）

Registry status `MOUNTED` = catalog-approved and session-selectable. It is not attached until this run selects it.
`PROPOSED` is not pickable. It may be shown as optional candidates, separate from the pick menu.
`session_picked_fine_ids` = selected this run. Active = actually loaded.

Every independent run needs a mount decision. If `session_picked_fine_ids` already covers the fine ids this task needs, reuse the session lock and do not ask. Otherwise enter this section. A single-node personal-layer task with no mounted dependency does not ask (example: polish one sentence).

1. Classify the task. Propose **relevant coarse bucket(s)** then **MOUNTED candidate fine ids** (not the whole menu unless 全线). Optional PROPOSED names stay off the pick menu.
2. Show each candidate as one line: **粗 ID · 细 ID · 源 · 包内 skill** · 做什么。默认源多为 B。审稿混合配方行必须写出 skill 名（如 `simulate-reviewers`）。
3. **Ask the user to multi-select fine ids**. Default is **hybrid** (B chassis; non-B only where the recipe lists a path). For 写稿/润色/修订论著, **pre-check `manuscript-final-W2`**. For 预审/审稿/回复审稿, **pre-check `review-hybrid-default`**. Then allow edits. Also offer: 用该默认配方 / 候选全用 B / 只要个人层不外挂 / 换源（MedSci / Scientific / AIPOCH / Nature，仅当该细 ID 有路径）. Empty picked path → tell the user; do not silent-fallback.
4. Load **only** the picked fine ids (and for non-B overrides, **only the preset/skill paths** listed). Ensure bytes in `{mounts_cap}/` first. Unpicked stay unloaded — do not prefetch a whole Nature/Scientific tree. Never bulk-download.
5. If a picked path is empty → empty-mount protocol. Do not silently substitute another source.
6. Do not change `registry.yaml` just because this run picked a backup source.

Silence is not approval. Never auto-mount a non-B source. Personal layers (Aitor-format, de-AI, 0RAD, Voice A/B) are not mount picks.
Say **默认挂载 B 包/本仓**, not 空挂.

## Empty-mount protocol

If a listed mount is empty (path missing, zero files, clone failed, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search (B first, then GitHub / network; if no network, ask for a local path).
3. **Confirm with the user** before changing `registry.yaml` or switching source.

Never silently fall back to MedSci/Scientific/AIPOCH/Nature or invent a local copy.

## Resolution order

1. Read this skill's `registry.yaml` (coarse buckets + fine `mounts:`).
2. Resolve each fine id against its `source`. Default source is B. `humanize` mounts from MedSci. Archived ids (registry `archived:`) are not in the default menu.
3. If that path is empty or missing → empty-mount protocol.
4. Only after confirmation may a *different* backup candidate be proposed.
5. Evaluate capability, boundaries, dependencies, and overlap.
6. New non-B sources stay `PROPOSED` until explicit approval. Nature LICENSE verified Apache-2.0; still ask-each-run + bytes.
7. After approval the registry status becomes `MOUNTED` (or stays `PROPOSED` if not approved). `APPROVED` is the confirmation in this workflow, not a registry field. Update `registry.yaml` and regenerate `MOUNTED_SKILLS.md`.
