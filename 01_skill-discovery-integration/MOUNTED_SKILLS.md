# Mounted Skills Boundary

Canonical **pointers live in 01** (`registry.yaml` is source of truth; this file is the human table).
Default source: [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).

Empty mount → notify the user, then re-search and confirm. Do not silently fall back to ARS/MedSci.
Never auto-mount a non-B source. `PROPOSED` is not `MOUNTED`.

Rule: mounted Skill owns generic capability; MY-SKILLS owns orchestration, personalization, constraints, and Final QC.
de-AI is personal (`05_manuscript/personal/`); not mounted from B.

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

## Backup candidates (not mounted; only after empty-mount notify + confirm)

- `https://github.com/Imbad0202/academic-research-skills` (`PROPOSED`, backup). Preset map: `sources/ars.proposed.yaml` (scanned `9443623`). 4 mapped / 8 empty.
- `https://github.com/Aperivue/medsci-skills` (`PROPOSED`, backup). Preset map: `sources/medsci.proposed.yaml` (scanned `912f7e8`). 12 mapped (4 partial) / 0 empty.

Mapping is not a mount. Use the yaml path table instead of re-searching those repos for the 12 A ids.

Unmapped extras (ARS/MedSci skills with no A mount id): [`mounts/unmapped.html`](mounts/unmapped.html).
