# Externalization Candidates

These **A-local generic copies** remain until a mounted Skill is confirmed to cover the capability.
Do not delete them solely because they are listed here. Personal files are **not** candidates.

Status: **not mounted**. After a mount covers an item, delete the A copy only with explicit user approval.

## M18 — 03 Research (retired 2026-09-13; remaining files kept for documented reasons)

B folders (CHG-20260903-009) are 1:1: `lit-search/` `lit-fulltext/` `lit-review/` `lit-cite/` `design-experiment/` `design-protocol/` `design-grant/` `frontier-ideate/` `frontier-hypothesize/`.

**Retired 2026-09-13** — verified line-for-line against the current B path (diffs were only legacy-pointer-name updates, e.g. `radiology-stats` → `04-stats-guide`, now `analyze-stats`; no content lost) and deleted:

- `03_research/design/`: `study-design.md`, `study-blueprints.md`, `feasibility-triage.md`, `validation.md`, `validation-strategy.md`, `endpoints-and-estimands.md`, `ai-radiogenomics-12-24-roadmap.md` → superseded by mounted `design-study` (`03-research/design-experiment/`)
- `03_research/frontier/`: `frontier.md`, `frontier-themes.md`, `frontier-patterns-2023-2026.md`, `ai-radiogenomics-frontier-map.md` → superseded by mounted `find-cohort-gap` (`03-research/frontier-ideate/`)
- `03_research/literature/literature-evidence-2023-2026.md` → superseded by mounted `ma-scout` (`03-research/lit-review/`)

**Kept — permanent home, not a duplicate:**
- `03_research/literature/journal-selection.md` — 选刊's canonical location (选刊 is 03, not 05); B has no 选刊 fine id.
- `03_research/literature/journal-patterns-2023-2026.md` — checked against B's same-named file under `05-manuscript/write-venue/`; **not equivalent**. B's copy was deliberately narrowed to venue-family *writing* patterns only ("This is not a 选刊 SOP"); it dropped this file's journal-tier table, do-not-submit list, and Red Lines section that support the actual 选刊 decision. Keep the A version; do not retire on a filename match alone.

**Kept — no B counterpart:**
- `03_research/design/radiology-design.md`, `03_research/frontier/radiology-frontier.md` — no matching filename under `mounts-cap/b/`.

**Retired 2026-09-22** — A copies deleted after a diff against the mounted fine id (pointer renames only):
- `03_research/frontier/evidence-layer.md`, `idea-to-question.md` → `frontier-hypothesize`
- `03_research/literature/literature.md`, `sources.md`, `public-datasets.md` → `lit-search`

Not candidates (personal, stay in A): `03_research/personal/`, `03_research/clinical-translation/`, `03_research/ethics-application-forms/`.

## Already moved to B (not retained in A)

Fine ids first; legacy v3 alias in parentheses.

- `clean-data` / `batch-cohort` (`02-tables`), `imaging-io` (`02-imaging-io`), `preprocess-imaging` (`02-imaging-qc`), `radiomics-ml` (`02-radiomics-habitat`); archived `02-pictures`, `02-fmri`
- `analyze-stats` (`04-stats-guide`) / `calc-sample-size` (`04-stats-power`) / `meta-analysis` (`04-stats-models`) / `model-evaluation` · `model-validation` (`04-model-eval`) / `make-figures` (`04-fig-flow`) / `fig-plot` (`04-fig-plot`)
- `write-paper` (`05-write-manuscript`) / `check-reporting` (`05-write-reporting`) / `find-journal` (`05-write-venue`) / `polish-language` (`05-write-polish`)
- `peer-review` (`06-review-peer`) / `self-review` (`06-review-critique`) / `revise` (`06-review-response`)

`04_analysis/personal/` (lab radiology-stats + 0RAD rules + palettes) stays in A. It is not in B.

`05_manuscript/personal/` includes de-AI (returned from B 2026-09-02). It is not a B mount.
