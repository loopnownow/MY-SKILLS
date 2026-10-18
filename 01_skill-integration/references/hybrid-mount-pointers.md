# Non-base exceptions — default deny

[registry.yaml](../registry.yaml) · [MOUNTED_SKILLS.md](../MOUNTED_SKILLS.md) · [session-pick.md](session-pick.md)

**Default unique runtime source = `my-skills-base` (MY-SKILLS-base).**

Non-base packs (former MedSci / Scientific / AIPOCH / Nature catalogs, ARS, OpenClaw, or any new upstream) are **default deny**:

- Do **not** auto-mount, bulk-download, or offer as a session package menu.
- Do **not** keep a multi-package hybrid narrative or mount-package board in 01.
- Archived registry rows may still name a historical `source` for revive notes; they are **not** pickable.
- Source yamls for dead packs were moved to `D:\0del\01_sources_archive_20261017\` (2026-10-17).
- Former `mounts/*.md` package stubs (medsci / scientific / aipoch / nature / b) were deleted 2026-10-17 — 01 keeps registry/index only; capabilities via A+B only.

**Owner exception only:** if the owner explicitly approves one non-base fine-id revive, update `registry.yaml` + restore that source yaml from the archive, then re-run `gen_mounted_skills.py`. Silence is not approval.

**A top layers** are not capability mounts. Flow: B fine-ID first-pass → 00 QC → A re-loops (see `00_orchestrator/references/ab-top-vs-b-loops.md`).

## Pilot: domain 02 in-repo base (2026-10-17)

Domain `02_data-processing` capability bodies were copied from B into A
`02_data-processing/base/` (tables, imaging-io, imaging-qc, README).
Fine ids `clean-data`, `batch-cohort`, `imaging-io`, `preprocess-imaging` use
registry `source: my-skills` (in-repo) with paths under `02_data-processing/base/`.
Personal top layer and domain `SKILL.md` stay in A. B repo is **not** deleted;
domains 03–07 are **not** migrated in this pilot.

