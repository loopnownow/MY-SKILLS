# mounts-cap

Local **byte cache** for B and backup plugin packs. Not a domain skill. Pointers stay in `01_skill-discovery-integration`.

| On disk | Source | What is fetched |
|---|---|---|
| `b/` | `loopnownow/MY-SKILLS-capabilities` | **Always** the full B tree. Missing → download. Present → compare GitHub SHA, update if needed. |
| `medsci/` `scientific/` `aipoch/` `nature/` | backup repos (catalog) | **Only the skill path(s) for ids picked this run.** Never clone the whole backup. ARS / OpenClaw removed from catalog — do not cache. |
| `STATE.yaml` | local | Recorded SHAs. Gitignored. |

Download is **not** a mount. Backup fetches prefer zip/codeload; `STATE.yaml` merges under lock so parallel `ensure --id` does not clobber keys. Session pick and empty-mount protocol still apply. Never auto-mount a non-B source because a folder appeared here.

Canonical B path is `mounts-cap/b/`. If a leftover sibling `MY-SKILLS-capabilities/` exists, run `python mounts-cap/fetch.py migrate-b` (moves it into `b/`). New fetches always write here.

```text
python mounts-cap/fetch.py ensure-b
python mounts-cap/fetch.py ensure --id humanize
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

### Audit 2026-09-24 (CHG-20260924-004)

- STATE paths vs disk: **0 missing**.
- Removed from STATE (keys only): MedSci legacy `self-review` / `peer-review` / `review-paper` / `check-reporting` / `model-evaluation` / `model-validation` (live mounts stay under B).
- Removed Nature **non-registry** cache dirs + STATE keys: `nature-statistics`, `nature-citation`, `nature-ref-verifier` (phantom; verify-refs uses Scientific `citation-management`).
- Kept: Nature `nature-figure` / `nature-reviewer` / `nature-response` + dependency `nature-shared`; MedSci `humanize`; Scientific / AIPOCH recorded caches.
- PROPOSED Nature ids (`nature-academic-search`, `nature-data`, `nature-polishing`, `nature-proposal-writer`) stay uncached until session-picked + `fetch.py ensure`.

## Nature shared cache

`nature-figure` and `nature-reviewer` (and related Nature skills) expect a local `mounts-cap/nature/skills/nature-shared/` cache when those fine ids are mounted. If `nature-shared` is already present (see `STATE.yaml`), reuse it. **Do not** download large Nature galleries or whole-repo trees unless the user picked those ids and bytes are missing.

## MedSci legacy STATE keys

`STATE.yaml` may still list MedSci folder names such as `skills/self-review/`, `skills/peer-review/`, `skills/check-reporting/`, `skills/model-evaluation/`, `skills/model-validation/`, `skills/review-paper/` from older force_b / MedSci layouts. Live registry mounts those capabilities under **B** paths (`06-review/...`, `05-manuscript/write-reporting/`, `04-analysis/model-eval/`, …), not MedSci fine-id paths.

Safe local hygiene (does **not** delete pack bytes): remove those six keys from the `med-sci-skills:` block in `STATE.yaml` when the matching folders are unused leftovers, or leave them if you still keep evaluation clones on disk. Re-fetch only via `fetch.py ensure` for ids actually picked this run.

## Nature dependency cache

MOUNTED Nature fine ids (`nature-figure`, `nature-reviewer`, `nature-response`) read `../nature-shared/...`. Keep `mounts-cap/nature/skills/nature-shared/` populated (shared core + journal-formats). Missing `nature-shared` breaks relative links inside those packs — restore from a known-good cache or re-fetch the Nature skill set; do not strip galleries from `nature-figure` as a substitute for `nature-shared`.

