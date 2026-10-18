# Non-base exceptions -- default deny

[registry.yaml](../registry.yaml) · [MOUNTED_SKILLS.md](../MOUNTED_SKILLS.md) · [session-pick.md](session-pick.md)

**Default unique runtime source = `my-skills` (in-repo `NN_slug/base/`).**

Non-base packs (former MedSci / Scientific / AIPOCH / Nature catalogs, ARS, OpenClaw, or any new upstream) are **default deny**:

- Do **not** auto-mount, bulk-download, or offer as a session package menu.
- Do **not** keep a multi-package hybrid narrative or mount-package board in 01.
- Archived registry rows may still name a historical `source` for revive notes; they are **not** pickable.
- Source yamls for dead packs (including retired `b-my-skills-base.yaml`) were moved to `D:\0del\01_sources_archive_20261017\` (2026-10-17).
- Former `mounts/*.md` package stubs (medsci / scientific / aipoch / nature / b) were deleted 2026-10-17 -- 01 keeps registry/index only.

**Owner exception only:** if the owner explicitly approves one non-base fine-id revive, update `registry.yaml` + restore that source yaml from the archive, then re-run `gen_mounted_skills.py`. Silence is not approval.

**A top layers** are not capability mounts. Flow: capability-body fine-ID first-pass -> 00 QC -> A re-loops (see `00_orchestrator/references/ab-top-vs-b-loops.md`).

## In-repo base (domains 02-07) -- 2026-10-17

Capability bodies for domains `02_data-processing`--`07_response` live under A `NN_slug/base/`.
Fine ids use registry `source: my-skills` with paths under those folders.
Personal top layers and domain `SKILL.md` stay in A.
Remote `loopnownow/MY-SKILLS-base` is **retired** (deleted/archived 2026-10-17).
Former `{mounts_cap}/b/` B byte cache is obsolete for live mounts.
