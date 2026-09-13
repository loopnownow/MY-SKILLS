---
name: skill-discovery-integration
description: >
  Discover, evaluate, and mount external Skills. Use for finding a new Skill,
  checking mounted capability coverage, integrating an approved external Skill,
  or resolving missing capability. Infrastructure only. Never literature research,
  statistics, manuscript writing, or peer review. Mount pointers live only here.
  Default mount is B (MY-SKILLS-capabilities). Every run: ask which fine ids to
  mount this session under relevant coarse buckets. Never auto-mount a non-B source.
  OpenClaw is never an atomic mount source.
---

# Skill Discovery & Integration

## Purpose

Infrastructure for Skill discovery and mounting. Professional work stays in 02–06.
This layer only resolves **where a capability comes from**.
**All mount pointers live here.** Machine: `registry.yaml` + one yaml per external source under `sources/`.
Human board: `mounts/` (`README.md`, `MIGRATION_v3_to_v4.md`, `hybrid-mount-pointers.md`, `presets.md` + `presets/*.yaml`, `b.md` / `ars.md` / `medsci.md` / `scientific.md` / `openclaw.md` / `aipoch.md` / `nature.md`).
Domain skills call fine ids; they do not keep a second pointer table.

## Architecture (v4 · CHG-20260913-001)

- **10 coarse ids** = welded stage buckets（文献检索 … 审稿回复）. Not A folder renames.
- **52 fine ids** = session-pick mount points (48 mounts + 4 reference-only).
- **Hybrid mount:** different fine ids may use different packages; never mix packages inside one fine id.
- A domains stay `00_orchestrator` … `06_review` (+ skill-harvest). Personal layers stay in A.
- 选刊 stays Victor / `03_research/medical-journal-submit` — do not move into 05.
- Backup of 30-id registry: `registry.v3.30.yaml`.

## Default mount

**Default session recipe (review / pre-review):** `review-hybrid-default` in `mounts/presets.md` (machine core `mounts/presets/review-hybrid.yaml`) — B chassis, Nature fine-id overlays (license 需核实), Scientific critique fine id. Still ask each run; user may change picks. Attribution and fetch are **per pack skill** (see preset `skills:`), not whole source. ARS and OpenClaw are not in the default recipe.

**Default source is B:** [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities).
ARS, MedSci, Scientific, AIPOCH, Nature are **backup candidates** (PROPOSED). OpenClaw is **license-risk-reference-only** — never atomic source.
Nature fine ids stay PROPOSED until license verified; do not claim MOUNTED if bytes absent.

**Mapping is not a mount.** Status stays `PROPOSED` until the user confirms.

## Local cache (`mounts-cap/`)

Bytes live at repo-root `mounts-cap/` (gitignored pack trees). Pointers stay in this skill.

- **B** (`mounts-cap/b/`): **canonical** full tree. Missing → `python mounts-cap/fetch.py ensure-b`.
- **ARS / MedSci / Scientific / AIPOCH / Nature**: download **only the path(s) of fine ids picked this run**. Never clone wholesale. OpenClaw: do not fetch for mount.
- `python mounts-cap/fetch.py ensure --id <fine-id>` after the session pick. Download is not a mount. Empty after fetch → empty-mount protocol.

## Session mount pick（每次运行必问 · 细 ID 多选）

Registry `MOUNTED` / `PROPOSED` = **available to pick**, not attached for this run.
**Every MY-SKILLS run** (00 composite or a single 02–06 skill) must ask before loading any mounted pack.

1. Classify the task. Propose **relevant coarse bucket(s)** then **candidate fine ids** (not all 52 unless 全线).
2. Show each candidate as one line: **粗 ID · 细 ID · 源 · 包内 skill** · 做什么。默认源多为 B。审稿混合配方行必须写出 skill 名（如 `nature-ref-verifier`）。
3. **Ask the user to multi-select fine ids**. For 预审/审稿/回复审稿, **pre-check `review-hybrid-default`** then allow edits. Also offer: 用审稿混合默认配方 / 候选全用 B / 只要个人层不外挂 / 换源（MedSci / Scientific / AIPOCH / Nature，仅当该细 ID 有路径；**OpenClaw 不提供**；ARS 默认不提供）.
4. Load **only** the picked fine ids (and for non-B overrides, **only the preset/skill paths** listed). Ensure bytes in `mounts-cap/` first. Unpicked stay unloaded — do not prefetch a whole Nature/Scientific tree. Never bulk-download.
5. If a picked path is empty → empty-mount protocol. Do not silently substitute another source.
6. Do not change `registry.yaml` just because this run picked a backup source.

Silence is not approval. Never auto-mount a non-B source. Personal layers (Aitor-format, de-AI, 0RAD, Voice A/B) are not mount picks.
Say **默认挂载 B 包/本仓**, not 空挂.

## Empty-mount protocol

If a listed mount is empty (path missing, zero files, clone failed, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search (B first, then GitHub / network; if no network, ask for a local path).
3. **Confirm with the user** before changing `registry.yaml` or switching source.

Never silently fall back to ARS/MedSci/Scientific/OpenClaw/AIPOCH/Nature or invent a local copy.

## Resolution order

1. Read this skill's `registry.yaml` (coarse buckets + fine `mounts:`).
2. Resolve each fine id against its `source`. Default source is B. `humanize` mounts from MedSci. Archived ids are not in the default menu (includes former `04-explainability`).
3. If that path is empty or missing → empty-mount protocol.
4. Only after confirmation may a *different* backup candidate be proposed.
5. Evaluate capability, boundaries, dependencies, and overlap.
6. New non-B sources stay `PROPOSED` until explicit approval. Nature needs license confirmation.
7. After approval: `APPROVED` → `MOUNTED`. Update `registry.yaml` and `MOUNTED_SKILLS.md`.

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review.
- Never auto-install or auto-mount a **non-B** Skill.
- Never bulk-download ARS / MedSci / Scientific / OpenClaw / AIPOCH / Nature. On-demand paths only, after a pick.
- **Never mount OpenClaw** as an atomic skill source.
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal layer because an external Skill is more general.
- `PROPOSED` is not `MOUNTED`.
- Personal de-AI (`05_manuscript/personal/`) is not a B mount. Generic de-AI is `humanize` (MedSci). The personal forbidden list still wins.

## Capability evaluation

For every candidate record: what it provides; what it does not; inputs/outputs; dependencies; conflicts/overlap; target layer (02–06); maintenance/version; replace vs complement.

## Registry

`registry.yaml` = lifecycle index (canonical). `sources/<source>.yaml` = one config per external source. `mounts/*.md` = human interface board. `interface.yaml` = capability-contract template.
Lifecycle: `DISCOVERED → EVALUATED → PROPOSED → APPROVED → MOUNTED`, with `DISABLED` / `ARCHIVED` / `REJECTED`.
**Layout rule:** one external source → one yaml. Fine ids are the mount points; coarse ids are stage buckets only.
