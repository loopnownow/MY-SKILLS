---
name: skill-discovery-integration
description: >
  Discover, evaluate, and mount external Skills. Use for finding a new Skill,
  checking mounted capability coverage, integrating an approved external Skill,
  or resolving missing capability. Infrastructure only. Never literature research,
  statistics, manuscript writing, or peer review. Mount pointers live only here.
  Default mount is B (MY-SKILLS-capabilities). Every run: ask which packs to mount this session. Never auto-mount a non-B source.
---

# Skill Discovery & Integration

## Purpose

Infrastructure for Skill discovery and mounting. Professional work stays in 02–06.
This layer only resolves **where a capability comes from**.
**All mount pointers live here.** Machine: `registry.yaml` + one yaml per external source under `sources/`. Human board: `mounts/` (`README.md` index, `presets.md` + `presets/*.yaml` recipes, `b.md` / `ars.md` / `medsci.md` / `scientific.md` / `openclaw.md` / `aipoch.md` / `nature.md`). Unmapped extras stay on each source page. Domain skills call ids; they do not keep a second pointer table.

## Default mount

**Default session recipe (review / pre-review):** `review-hybrid-default` in `mounts/presets.md` (machine core `mounts/presets/review-hybrid.yaml`) — B chassis, Nature as main external for cite + reported-stats audit paths, Scientific overlay on `06-review-critique`. Still ask each run; user may change picks. Attribution and fetch are **per pack skill** (see preset `skills:`), not whole source. ARS and out-of-band editors are not in the default recipe.

**Default source is B:** [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities).
ARS (`Imbad0202/academic-research-skills`), MedSci (`Aperivue/medsci-skills`), Scientific (`K-Dense-AI/scientific-agent-skills`), OpenClaw (`FreedomIntelligence/OpenClaw-Medical-Skills`), AIPOCH (`aipoch/medical-research-skills`), and Nature (`Yuan1z0825/nature-skills`) are **backup candidates only**.

Coarse ids follow Scientific Agent Skills jobs (CHG-20260903-008). Preset maps in `sources/*.proposed.yaml`. **Mapping is not a mount.** Status stays `PROPOSED` until the user confirms a source-wide switch.

## Local cache (`mounts-cap/`)

Bytes live at repo-root `mounts-cap/` (gitignored pack trees). Pointers stay in this skill.

- **B** (`mounts-cap/b/`): **canonical** full tree. Missing → `python mounts-cap/fetch.py ensure-b` (or `migrate-b` if a leftover sibling `MY-SKILLS-capabilities/` still sits next to A). Do not keep B as a sibling of A.
- **ARS / MedSci / Scientific / OpenClaw / AIPOCH / Nature**: download **only the path(s) of ids picked this run**. Never clone those repos wholesale. Example: picking `04-explainability` fetches `skills/explainability/` into `mounts-cap/medsci/`, not the rest of MedSci. OpenClaw paths land under `mounts-cap/openclaw/`; AIPOCH under `mounts-cap/aipoch/`; Nature under `mounts-cap/nature/`.
- `python mounts-cap/fetch.py ensure --id <coarse-id>` after the session pick. Download is not a mount. Empty after fetch → empty-mount protocol.



## Session mount pick（每次运行必问）

Registry `MOUNTED` = **available to pick**, not attached for this run.
**Every MY-SKILLS run** (00 composite or a single 02–06 skill) must ask before loading any mounted pack.

1. Classify the task. Propose **only the candidate ids** for this job (not all 30 unless the user said 全线).
2. Show each candidate as one line: **粗 ID · 源 · 包内 skill（若有）** · 做什么。默认源多为 B（`04-explainability` / `05-humanize` → MedSci）。审稿混合配方行必须写出 skill 名（如 `nature-ref-verifier`）。
3. **Ask the user to choose** (multi-select). For 预审/审稿/回复审稿, **pre-check `review-hybrid-default`** (see `mounts/presets.md`) then allow edits. Also offer: 用审稿混合默认配方 / 候选全用 B / 只要个人层不外挂 / 换源（MedSci / Scientific / OpenClaw / AIPOCH / Nature，仅当该源对该 id 有路径；ARS 默认不提供）.
4. Load **only** the picked ids (and for non-B overrides, **only the preset/skill paths** listed—not the whole backup repo). Ensure bytes in `mounts-cap/` first (full B; on-demand path for a non-B skill pick). Unpicked skills stay unloaded — do not prefetch a whole Nature/Scientific tree.
5. If a picked path is empty → empty-mount protocol. Do not silently substitute another source.
6. Do not change `registry.yaml` just because this run picked a backup source. A source-wide switch still needs explicit confirm.

Silence is not approval. Never auto-mount a non-B source. Personal layers (Aitor-format, de-AI, 0RAD, Voice A/B) are not mount picks.

## Empty-mount protocol

If a listed mount is empty (path missing, zero files, clone failed, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search (B first, then GitHub / network; if no network, ask for a local path).
3. **Confirm with the user** before changing `registry.yaml` or switching source.

Never silently fall back to ARS/MedSci/Scientific/OpenClaw/AIPOCH/Nature or invent a local copy.

## Resolution order

1. Read this skill's `registry.yaml` (pointers + `mounts:`).
2. Resolve each id against its `source` in `registry.yaml`. Default source is B. Two user-named exceptions mount from MedSci: `04-explainability`, `05-humanize`.
3. If that path is empty or missing → empty-mount protocol (notify → re-search → confirm).
4. Only after confirmation may a *different* backup candidate be proposed. Do not silently switch the other ids to MedSci because these two already point there.
5. Evaluate capability, boundaries, dependencies, and overlap.
6. New non-B sources stay `PROPOSED` until explicit approval. Silence is not approval.
7. After approval: `APPROVED` → `MOUNTED`. Update `registry.yaml` and `MOUNTED_SKILLS.md`.

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review.
- Never auto-install or auto-mount a **non-B** Skill.
- Never bulk-download ARS / MedSci / Scientific / OpenClaw / AIPOCH / Nature. On-demand paths only, after a pick.
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal layer because an external Skill is more general.
- `PROPOSED` is not `MOUNTED`.
- Personal de-AI (`05_manuscript/personal/`) is not a B mount. Generic de-AI is `05-humanize` (MedSci). The personal forbidden list still wins.

## Capability evaluation

For every candidate record: what it provides; what it does not; inputs/outputs; dependencies; conflicts/overlap; target layer (02–06); maintenance/version; replace vs complement.

## Registry

`registry.yaml` = lifecycle index (canonical). `sources/<source>.yaml` = one config per external source. `mounts/*.md` = human interface board. `interface.yaml` = capability-contract template.
Lifecycle: `DISCOVERED → EVALUATED → PROPOSED → APPROVED → MOUNTED`, with `DISABLED` or `REJECTED`.
**Layout rule:** one external source → one yaml. Do not split B into one file per A id; do not mix B + ARS + MedSci + Scientific + OpenClaw + AIPOCH + Nature in one file. B folders are 1:1 with A ids (CHG-20260903-009), except MedSci-only `04-explainability` / `05-humanize`.
