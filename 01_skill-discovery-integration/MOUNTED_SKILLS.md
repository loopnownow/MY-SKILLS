# Mounted Skills Boundary

Canonical **pointers live in 01** (`registry.yaml` is source of truth; this file is the human table).
Default source: [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).

Empty mount → notify the user, then re-search and confirm. Do not silently fall back to ARS/MedSci/Scientific.
Never auto-mount a non-B source. `PROPOSED` is not `MOUNTED`.

Rule: mounted Skill owns generic capability; MY-SKILLS owns orchestration, personalization, constraints, and Final QC.
Personal de-AI stays in A (`05_manuscript/personal/`). Generic de-AI is `05-humanize` (MedSci), not B.

Coarse ids follow Scientific Agent Skills jobs (CHG-20260903-008). B folders are 1:1 with those ids (CHG-20260903-009). Retired umbrellas: `03-literature`, `03-design`, `03-frontier`, `04-stats-generic`, `05-writing-generic`, `06-review-generic`.

## Default mounts (B)

| Id | B path | Layer | Status |
|---|---|---|---|
| `02-xlsx` | `02-data-processing/xlsx/` | 02 | MOUNTED |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | 02 | MOUNTED |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | 02 | MOUNTED |
| `02-impute` | `02-data-processing/impute/` | 02 | MOUNTED |
| `02-generic-docs` | `02-data-processing/generic-docs/` | 02 | MOUNTED |
| `03-lit-search` | `03-research/lit-search/` | 03 | MOUNTED |
| `03-lit-review` | `03-research/lit-review/` | 03 | MOUNTED |
| `03-lit-cite` | `03-research/lit-cite/` | 03 | MOUNTED |
| `03-design-experiment` | `03-research/design-experiment/` | 03 | MOUNTED |
| `03-design-grant` | `03-research/design-grant/` | 03 | MOUNTED |
| `03-frontier-ideate` | `03-research/frontier-ideate/` | 03 | MOUNTED |
| `03-frontier-hypothesize` | `03-research/frontier-hypothesize/` | 03 | MOUNTED |
| `04-stats-guide` | `04-analysis/stats-guide/` | 04 | MOUNTED |
| `04-stats-power` | `04-analysis/stats-power/` | 04 | MOUNTED |
| `04-stats-models` | `04-analysis/stats-models/` | 04 | MOUNTED |
| `04-figure-engine` | `04-analysis/figure-engine/` | 04 | MOUNTED |
| `05-write-manuscript` | `05-manuscript/write-manuscript/` | 05 | MOUNTED |
| `05-write-venue` | `05-manuscript/write-venue/` | 05 | MOUNTED |
| `06-review-peer` | `06-review/review-peer/` | 06 | MOUNTED |
| `06-review-critique` | `06-review/review-critique/` | 06 | MOUNTED |

## MedSci-only interfaces (not in B)

| Id | MedSci path | Layer | Status |
|---|---|---|---|
| `04-explainability` | `skills/explainability/` | 04 | MOUNTED |
| `05-humanize` | `skills/humanize/` | 05 | MOUNTED |

## Backup candidates (source-wide switch still needs empty-mount notify + confirm)

- `https://github.com/Imbad0202/academic-research-skills` (`PROPOSED`). `sources/ars.proposed.yaml` · 6 mapped / 16 empty. ARS still has only 4 packs; several A ids share one ARS folder.
- `https://github.com/Aperivue/medsci-skills` (`PROPOSED`). `sources/medsci.proposed.yaml` · 22 mapped / 0 empty.
- `https://github.com/K-Dense-AI/scientific-agent-skills` (`PROPOSED`). `sources/scientific-agent-skills.proposed.yaml` · 20 mapped / 2 empty (`02-radiomics-habitat`, `05-humanize`).

Mapping is not a source-wide mount. Unmapped extras are listed on each source page under `mounts/`.
