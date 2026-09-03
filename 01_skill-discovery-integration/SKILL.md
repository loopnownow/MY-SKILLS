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
**All mount pointers live here.** Machine: `registry.yaml` + one yaml per external source under `sources/`. Human board: `mounts/` (`README.md` index, `b.md` / `ars.md` / `medsci.md` / `scientific.md`). Unmapped extras stay on each source page. Domain skills call ids; they do not keep a second pointer table.

## Default mount

**Default source is B:** [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities).
ARS (`Imbad0202/academic-research-skills`), MedSci (`Aperivue/medsci-skills`), and Scientific (`K-Dense-AI/scientific-agent-skills`) are **backup candidates only**.

Coarse ids follow Scientific Agent Skills jobs (CHG-20260903-008). Preset maps in `sources/*.proposed.yaml`. **Mapping is not a mount.** Status stays `PROPOSED` until the user confirms a source-wide switch.

## Local cache (`mounts-cap/`)

Bytes live at repo-root `mounts-cap/` (gitignored pack trees). Pointers stay in this skill.

- **B** (`mounts-cap/b/`): keep the full tree. Missing → `python mounts-cap/fetch.py ensure-b`. Present → compare GitHub SHA and update if needed. A sibling `MY-SKILLS-capabilities/` is still accepted as legacy B.
- **ARS / MedSci / Scientific**: download **only the path(s) of ids picked this run**. Never clone those repos wholesale. Example: picking `04-explainability` fetches `skills/explainability/` into `mounts-cap/medsci/`, not the rest of MedSci.
- `python mounts-cap/fetch.py ensure --id <coarse-id>` after the session pick. Download is not a mount. Empty after fetch → empty-mount protocol.




## Session mount pick（每次运行必问）

Registry `MOUNTED` = **available to pick**, not attached for this run.
**Every MY-SKILLS run** (00 composite or a single 02–06 skill) must ask before loading any mounted pack.

1. Classify the task. Propose **only the candidate ids** for this job (not all 30 unless the user said 全线).
2. Show each candidate as one line: id · 做什么 · default source (B, except `04-explainability` / `05-humanize` → MedSci).
3. **Ask the user to choose** (multi-select). Also offer: 候选全用默认源 / 只要个人层不外挂 / 换源（ARS / MedSci / Scientific，仅当该源对该 id 有路径）.
4. Load **only** the picked ids, from the picked source. Ensure bytes in `mounts-cap/` first (full B; on-demand path for a non-B pick). Unpicked packs stay unloaded this run — do not prefetch them.
5. If a picked path is empty → empty-mount protocol. Do not silently substitute another source.
6. Do not change `registry.yaml` just because this run picked a backup source. A source-wide switch still needs explicit confirm.

Silence is not approval. Never auto-mount a non-B source. Personal layers (Aitor-format, de-AI, 0RAD, Voice A/B) are not mount picks.

## Empty-mount protocol

If a listed mount is empty (path missing, zero files, clone failed, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search (B first, then GitHub / network; if no network, ask for a local path).
3. **Confirm with the user** before changing `registry.yaml` or switching source.

Never silently fall back to ARS/MedSci/Scientific or invent a local copy.

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
- Never bulk-download ARS / MedSci / Scientific. On-demand paths only, after a pick.
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal layer because an external Skill is more general.
- `PROPOSED` is not `MOUNTED`.
- Personal de-AI (`05_manuscript/personal/`) is not a B mount. Generic de-AI is `05-humanize` (MedSci). The personal forbidden list still wins.

## Capability evaluation

For every candidate record: what it provides; what it does not; inputs/outputs; dependencies; conflicts/overlap; target layer (02–06); maintenance/version; replace vs complement.

## Registry

`registry.yaml` = lifecycle index (canonical). `sources/<source>.yaml` = one config per external source. `mounts/*.md` = human interface board. `interface.yaml` = capability-contract template.
Lifecycle: `DISCOVERED → EVALUATED → PROPOSED → APPROVED → MOUNTED`, with `DISABLED` or `REJECTED`.
**Layout rule:** one external source → one yaml. Do not split B into one file per A id; do not mix B + ARS + MedSci + Scientific in one file. B folders are 1:1 with A ids (CHG-20260903-009), except MedSci-only `04-explainability` / `05-humanize`.
