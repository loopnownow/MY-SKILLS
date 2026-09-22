# mounts-cap

Local **byte cache** for B and backup plugin packs. Not a domain skill. Pointers stay in `01_skill-discovery-integration`.

| On disk | Source | What is fetched |
|---|---|---|
| `b/` | `loopnownow/MY-SKILLS-capabilities` | **Always** the full B tree. Missing → download. Present → compare GitHub SHA, update if needed. |
| `ars/` `medsci/` `scientific/` | backup repos | **Only the skill path(s) for ids picked this run.** Never clone the whole backup. |
| `STATE.yaml` | local | Recorded SHAs. Gitignored. |

Download is **not** a mount. Backup fetches prefer zip/codeload; `STATE.yaml` merges under lock so parallel `ensure --id` does not clobber keys. Session pick and empty-mount protocol still apply. Never auto-mount a non-B source because a folder appeared here.

Canonical B path is `mounts-cap/b/`. If a leftover sibling `MY-SKILLS-capabilities/` exists, run `python mounts-cap/fetch.py migrate-b` (moves it into `b/`). New fetches always write here.

```text
python mounts-cap/fetch.py ensure-b
python mounts-cap/fetch.py ensure --id 04-explainability
python mounts-cap/fetch.py check
```

Do not vendor unpublished texts, PHI, HIS credentials, or 0RAD trees.

## Sync warning (local A)

Never robocopy /MIR or git clean -xfd the whole skills tree onto mounts-cap/ — pack dirs (b/, scientific/, …) and STATE.yaml are gitignored and will be deleted. Sync A sources excluding mounts-cap pack trees, or restore via python mounts-cap/fetch.py ensure-b.

## Cache ≠ Mount ≠ Active · Registry = index

- **Cache** = this directory (`mounts-cap/<pack>/`). External skill **bytes** live here (SSOT for Scientific / Nature / AIPOCH / MedSci / …).
- **Mount** = a fine id chosen for the session in `01_skill-discovery-integration/registry.yaml`.
- **Active** = bytes actually loaded into context this run.
- **Registry** indexes paths; it does not store skill bodies. B `stub_in_b` / `cross-pack/` entries are **pointers** into this cache — do not duplicate full entity trees there.

Download / `fetch.py ensure` is **not** a mount and does **not** make a skill Active.

## STATE.yaml orphan note

`STATE.yaml` is gitignored and may list paths that no longer exist on disk (or omit folders left from prior evaluation clones). **Do not wipe pack bytes** or blank `STATE.yaml` to “fix” orphans. Document the mismatch here or in INTEGRATION_MAP; re-fetch with `fetch.py ensure --id …` only for ids actually picked this run.

Harmless orphans (unreferenced cache folders with no registry fine id) may be deleted in a dedicated cleanup CHG — not as a side effect of architecture docs.

## Nature shared cache

`nature-figure` and `nature-reviewer` (and related Nature skills) expect a local `mounts-cap/nature/skills/nature-shared/` cache when those fine ids are mounted. If `nature-shared` is already present (see `STATE.yaml`), reuse it. **Do not** download large Nature galleries or whole-repo trees unless the user picked those ids and bytes are missing.
