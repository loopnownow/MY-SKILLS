# Non-base exceptions — default deny

[总览](README.md) · [registry.yaml](../registry.yaml) · [MOUNTED_SKILLS.md](../MOUNTED_SKILLS.md)

**Default unique runtime source = `my-skills-base` (MY-SKILLS-base).**

Non-base packs (former MedSci / Scientific / AIPOCH / Nature catalogs, ARS, OpenClaw, or any new upstream) are **default deny**:

- Do **not** auto-mount, bulk-download, or offer as a session package menu.
- Do **not** keep a multi-package hybrid narrative in 01.
- Archived registry rows may still name a historical `source` for revive notes; they are **not** pickable.
- Source yamls for dead packs were moved to `D:\0del\01_sources_archive_20261017\` (2026-10-17).
- Board stubs: `medsci.md` / `scientific.md` / `aipoch.md` / `nature.md` — history only.

**Owner exception only:** if the owner explicitly approves one non-base fine-id revive, update `registry.yaml` + restore that source yaml from the archive, then re-run `gen_mounted_skills.py`. Silence is not approval.

**A top layers** are not capability mounts. Flow: B fine-ID first-pass → 00 QC → A re-loops (see `00_orchestrator/references/ab-top-vs-b-loops.md`).
