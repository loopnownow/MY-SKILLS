---
name: skill-discovery-integration
description: >
  Discover, evaluate, and mount external Skills. Use for finding a new Skill,
  checking mounted capability coverage, integrating an approved external Skill,
  or resolving missing capability. Infrastructure only. Never literature research,
  statistics, manuscript writing, or peer review. Mount pointers live only here.
  Default mount is B (MY-SKILLS-capabilities). Never auto-mount a non-B source.
---

# Skill Discovery & Integration

## Purpose

Infrastructure for Skill discovery and mounting. Professional work stays in 02–06.
This layer only resolves **where a capability comes from**.
**All mount pointers live here.** Machine: `registry.yaml` + one yaml per external source under `sources/`. Human board: `mounts/` (`mounts.html` index, `mounts-b.html` / `mounts-ars.html` / `mounts-medsci.html`). Unmapped extras stay on each source page, not a fifth HTML file. Domain skills call ids; they do not keep a second pointer table.

## Default mount

**Default source is B:** [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities).
ARS (`Imbad0202/academic-research-skills`) and MedSci (`Aperivue/medsci-skills`) are **backup candidates only**.

Preset maps live in `sources/ars.proposed.yaml` and `sources/medsci.proposed.yaml` (scanned 2026-09-03). Use those A-id → path tables instead of re-searching the backup repos for the 12 ids. **Mapping is not a mount.** Status stays `PROPOSED` until the user confirms a switch.


## Empty-mount protocol

If a listed mount is empty (path missing, zero files, clone failed, id points nowhere):

1. **Notify the user first.** Do not silently skip, substitute, or fall back.
2. Re-search (B first, then GitHub / network; if no network, ask for a local path).
3. **Confirm with the user** before changing `registry.yaml` or switching source.

Never silently fall back to ARS/MedSci or invent a local copy.

## Resolution order

1. Read this skill's `registry.yaml` (pointers + `mounts:`).
2. Resolve each id against its `source` in `registry.yaml`. Default source is B. Two user-named exceptions mount from MedSci: `04-explainability`, `05-humanize`.
3. If that path is empty or missing → empty-mount protocol (notify → re-search → confirm).
4. Only after confirmation may a *different* backup candidate be proposed. Do not silently switch the other 12 ids to MedSci because these two already point there.
5. Evaluate capability, boundaries, dependencies, and overlap.
6. New non-B sources stay `PROPOSED` until explicit approval. Silence is not approval.
7. After approval: `APPROVED` → `MOUNTED`. Update `registry.yaml` and `MOUNTED_SKILLS.md`.

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review.
- Never auto-install or auto-mount a **non-B** Skill.
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal layer because an external Skill is more general.
- `PROPOSED` is not `MOUNTED`.
- Personal de-AI (`05_manuscript/personal/`) is not a B mount. Generic de-AI is `05-humanize` (MedSci). The personal forbidden list still wins.

## Capability evaluation

For every candidate record: what it provides; what it does not; inputs/outputs; dependencies; conflicts/overlap; target layer (02–06); maintenance/version; replace vs complement.

## Registry

`registry.yaml` = lifecycle index (canonical). `sources/<source>.yaml` = one config per external source. `mounts/` = human interface board. `interface.yaml` = capability-contract template.
Lifecycle: `DISCOVERED → EVALUATED → PROPOSED → APPROVED → MOUNTED`, with `DISABLED` or `REJECTED`.
**Layout rule:** one external source → one yaml. Do not split B into 12 files; do not mix B + ARS + MedSci in one file.
