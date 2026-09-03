# Mounted Skills Boundary

Canonical **pointers live in 01** (`registry.yaml` is source of truth; this file is the human table).
Default source: [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).

Empty mount → notify the user, then re-search and confirm. Do not silently fall back to ARS/MedSci.
Never auto-mount a non-B source. `PROPOSED` is not `MOUNTED`.

Rule: mounted Skill owns generic capability; MY-SKILLS owns orchestration, personalization, constraints, and Final QC.
Personal de-AI stays in A (`05_manuscript/personal/`). Generic de-AI is `05-humanize` (MedSci), not B.

## Default mounts (B)

| Id | B path | Layer | Status |
|---|---|---|---|
| `02-xlsx` | `02-data-processing/xlsx/` | 02 | MOUNTED |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | 02 | MOUNTED |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | 02 | MOUNTED |
| `02-impute` | `02-data-processing/impute/` | 02 | MOUNTED |
| `02-generic-docs` | `02-data-processing/generic-docs/` | 02 | MOUNTED |
| `03-literature` | `03-research/literature/` | 03 | MOUNTED |
| `03-design` | `03-research/design/` | 03 | MOUNTED |
| `03-frontier` | `03-research/frontier/` | 03 | MOUNTED |
| `04-stats-generic` | `04-analysis/stats-generic/` | 04 | MOUNTED |
| `04-figure-engine` | `04-analysis/figure-engine/` | 04 | MOUNTED |
| `05-writing-generic` | `05-manuscript/writing-generic/` | 05 | MOUNTED |
| `06-review-generic` | `06-review/review-generic/` | 06 | MOUNTED |

## MedSci-only interfaces (not in B)

| Id | MedSci path | Layer | Status |
|---|---|---|---|
| `04-explainability` | `skills/explainability/` | 04 | MOUNTED |
| `05-humanize` | `skills/humanize/` | 05 | MOUNTED |

These two are user-named. They do not switch the other 12 ids to MedSci. Personal de-AI is still A `05_manuscript/personal/`.

## Backup candidates (source-wide switch still needs empty-mount notify + confirm)

- `https://github.com/Imbad0202/academic-research-skills` (`PROPOSED`, backup). Preset map: `sources/ars.proposed.yaml` (scanned `9443623`). 4 mapped / 8 empty.
- `https://github.com/Aperivue/medsci-skills` (`PROPOSED`, backup). Preset map: `sources/medsci.proposed.yaml` (scanned `912f7e8`). 14 mapped (4 partial) / 0 empty, including 04-explainability and 05-humanize.

Mapping is not a source-wide mount. Use the yaml path table instead of re-searching those repos. Unmapped extras are listed on `mounts/ars.md` and `mounts/medsci.md`.
