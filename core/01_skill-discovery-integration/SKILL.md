---
name: skill-discovery-integration
description: >
  Discover, evaluate, and mount external Skills. Use for finding a new Skill,
  checking mounted capability coverage, integrating an approved external Skill,
  or resolving missing capability. Infrastructure only. Never literature research,
  statistics, manuscript writing, or peer review. Never auto-mount.
---

# Skill Discovery & Integration

## Purpose

Infrastructure for external Skill discovery and mounting. Professional work stays in 02–06.
This layer only resolves **where a capability comes from**.

## Resolution order

1. Check currently mounted Skills (`core/MOUNTED_SKILLS.md`, `registry.yaml` `mounts:`).
2. Check approved default external mounts (none until a proposal is APPROVED).
3. Search GitHub / the network for a missing capability.
4. If network access is unavailable, **ask the user for a local Skill/repository path**.
5. Evaluate capability, boundaries, dependencies, and overlap.
6. Propose the mount (status `PROPOSED`).
7. **Require explicit user approval.** Silence is not approval.
8. Mount only after approval (`APPROVED` → `MOUNTED`). Update `registry.yaml` and `MOUNTED_SKILLS.md`.

## Hard rules

- Never perform literature research, statistics, manuscript writing, or peer review.
- Never auto-install or auto-mount a Skill.
- Never rewrite MY-SKILLS because an external pack exists.
- Never replace a personal layer because an external Skill is more general.
- `mounts: []` means nothing is mounted. `PROPOSED` is not `MOUNTED`.
- Default candidate: `Imbad0202/academic-research-skills`. Backup: `Aperivue/medsci-skills`.

## Capability evaluation

For every candidate record: what it provides; what it does not; inputs/outputs; dependencies; conflicts/overlap; target layer (02–06); maintenance/version; replace vs complement.

## Registry

`registry.yaml` = lifecycle. `interface.yaml` = capability contract.
Lifecycle: `DISCOVERED → EVALUATED → PROPOSED → APPROVED → MOUNTED`, with `DISABLED` or `REJECTED`.

Mountable capability package (separate repo): `loopnownow/MY-SKILLS-capabilities`.
