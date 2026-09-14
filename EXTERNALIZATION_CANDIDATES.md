# Externalization Candidates

These **A-local generic copies** remain until a mounted Skill is confirmed to cover the capability.
Do not delete them solely because they are listed here. Personal files are **not** candidates.

Status: **not mounted**. After a mount covers an item, delete the A copy only with explicit user approval.

## M18 — 03 Research (retired 2026-09-13; remaining files kept for documented reasons)

B folders (CHG-20260903-009) are 1:1: `lit-search/` `lit-fulltext/` `lit-review/` `lit-cite/` `design-experiment/` `design-protocol/` `design-grant/` `frontier-ideate/` `frontier-hypothesize/`.

**Retired 2026-09-13** — verified line-for-line against the current B path (diffs were only legacy-pointer-name updates, e.g. `radiology-stats` → `04-stats-guide`; no content lost) and deleted:

- `03_research/design/`: `study-design.md`, `study-blueprints.md`, `feasibility-triage.md`, `validation.md`, `validation-strategy.md`, `endpoints-and-estimands.md`, `ai-radiogenomics-12-24-roadmap.md` → superseded by mounted `design-study` (`03-research/design-experiment/`)
- `03_research/frontier/`: `frontier.md`, `frontier-themes.md`, `frontier-patterns-2023-2026.md`, `ai-radiogenomics-frontier-map.md` → superseded by mounted `find-cohort-gap` (`03-research/frontier-ideate/`)
- `03_research/literature/literature-evidence-2023-2026.md` → superseded by mounted `ma-scout` (`03-research/lit-review/`)

**Kept — permanent home, not a duplicate:**
- `03_research/literature/journal-selection.md` — 选刊's canonical location (`选刊 is 03, not 05-write-venue`); B has no 选刊 fine id.
- `03_research/literature/journal-patterns-2023-2026.md` — checked against B's same-named file under `05-manuscript/write-venue/`; **not equivalent**. B's copy was deliberately narrowed to venue-family *writing* patterns only ("This is not a 选刊 SOP"); it dropped this file's journal-tier table, do-not-submit list, and Red Lines section that support the actual 选刊 decision. Keep the A version; do not retire on a filename match alone.

**Kept — B counterpart exists but has no live mount point (orphaned in registry, not reachable via session pick):**
- `03_research/design/radiology-design.md`, `03_research/frontier/radiology-frontier.md` — no matching filename anywhere under `mounts-cap/b/` at all; unique A content, not a duplicate.
- `03_research/frontier/evidence-layer.md`, `03_research/frontier/idea-to-question.md` — B has same-named files under `03-research/frontier-hypothesize/`, but **no fine id in `registry.yaml` mounts that path** (not even PROPOSED). Retiring the A copy would make this content unreachable through the session-pick mechanism.
- `03_research/literature/literature.md`, `sources.md`, `public-datasets.md` — B has same-named files under `03-research/lit-search/`, same problem: **no fine id mounts `lit-search/`**.

**Follow-up recommendation (not actioned — needs your call):** either add fine ids for `frontier-hypothesize` and `lit-search` to `registry.yaml` (coarse 选题探索 / 文献检索 respectively) so that content becomes reachable, or if you don't intend to use it, these three A files stop being "temporary duplicates" and should just be reclassified as permanent A content in this file.

Not candidates (personal, stay in A): `03_research/personal/`, `03_research/clinical-translation/`, `03_research/ethics-application-forms/`.

## Already moved to B (not retained in A)

- `02-tables`, `02-imaging-io`, `02-imaging-qc`, `02-pictures`, `02-fmri`, `02-radiomics-habitat`
- `04-stats-guide` / `04-stats-power` / `04-stats-models` / `04-model-eval` / `04-fig-flow` / `04-fig-plot`
- `05-write-manuscript` / `05-write-reporting` / `05-write-venue` / `05-write-polish`
- `06-review-peer` / `06-review-critique` / `06-review-response`

`04_analysis/personal/` (lab radiology-stats + 0RAD rules + palettes) stays in A. It is not in B.

`05_manuscript/personal/` includes de-AI (returned from B 2026-09-02). It is not a B mount.
