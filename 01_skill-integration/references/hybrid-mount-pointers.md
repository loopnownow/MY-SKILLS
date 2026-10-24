# Non-base exceptions -- default deny

[registry.yaml](../registry.yaml) · [session-pick.md](session-pick.md)

**Default unique runtime source = `my-skills` (in-repo `NN_slug/base/`).**

Non-base packs (MedSci / Scientific / AIPOCH / Nature catalogs, ARS, OpenClaw, or any new upstream) are **default deny**:

- Do **not** auto-mount, bulk-download, or offer as a session package menu.
- Do **not** keep a multi-package hybrid narrative or mount-package board in 01.
- Archived registry rows may still name a historical upstream `source` for revive notes; they are **not** pickable.
- 01 keeps registry/index only (no per-pack mount stubs).

**Owner exception only:** if the owner explicitly approves one non-base fine-id revive, update that fine id in `registry.yaml` only (no `sources/` yaml seat; registry is SSOT). Silence is not approval.

**Personal top layers** are not capability mounts. Flow: base fine-ID first-pass -> 00 QC -> personal/top re-loops (see `00_orchestrator/references/base-vs-personal-top-loops.md`).

## In-repo base (domains 02-07)

Capability bodies for domains `02_data-processing`--`07_response` live under `NN_slug/base/`.
Fine ids use registry `source: my-skills` with paths under those folders.
Personal top layers and domain `SKILL.md` stay in this monorepo.
