# Mounted Skills Boundary

Canonical **pointers live in 01** (`registry.yaml` is source of truth; this file is the human table).
Default source: [`loopnownow/MY-SKILLS-capabilities`](https://github.com/loopnownow/MY-SKILLS-capabilities) (**B**).

Empty mount → notify the user, then re-search and confirm. Do not silently fall back to ARS/MedSci/Scientific.
Never auto-mount a non-B source. `PROPOSED` is not `MOUNTED`.
**Every run:** ask which of these ids to attach this session (`session_mount: ask-each-run`). Unpicked = not loaded.
Local bytes: `mounts-cap/` (B full; other sources on-demand). Download is not a mount.

30 coarse ids (CHG-20260903-011). Personal de-AI stays in A. Generic de-AI is `05-humanize` (MedSci), not B.

## Default mounts (B)

| Id | B path | Layer | Status |
|---|---|---|---|
| `02-tables` | `02-data-processing/tables/` | 02 | MOUNTED |
| `02-imaging-io` | `02-data-processing/imaging-io/` | 02 | MOUNTED |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | 02 | MOUNTED |
| `02-pictures` | `02-data-processing/pictures/` | 02 | MOUNTED |
| `02-fmri` | `02-data-processing/fmri/` | 02 | MOUNTED |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | 02 | MOUNTED |
| `03-lit-search` | `03-research/lit-search/` | 03 | MOUNTED |
| `03-lit-fulltext` | `03-research/lit-fulltext/` | 03 | MOUNTED |
| `03-lit-review` | `03-research/lit-review/` | 03 | MOUNTED |
| `03-lit-cite` | `03-research/lit-cite/` | 03 | MOUNTED |
| `03-design-experiment` | `03-research/design-experiment/` | 03 | MOUNTED |
| `03-design-protocol` | `03-research/design-protocol/` | 03 | MOUNTED |
| `03-design-grant` | `03-research/design-grant/` | 03 | MOUNTED |
| `03-frontier-ideate` | `03-research/frontier-ideate/` | 03 | MOUNTED |
| `03-frontier-hypothesize` | `03-research/frontier-hypothesize/` | 03 | MOUNTED |
| `04-stats-guide` | `04-analysis/stats-guide/` | 04 | MOUNTED |
| `04-stats-power` | `04-analysis/stats-power/` | 04 | MOUNTED |
| `04-stats-models` | `04-analysis/stats-models/` | 04 | MOUNTED |
| `04-model-eval` | `04-analysis/model-eval/` | 04 | MOUNTED |
| `04-fig-flow` | `04-analysis/fig-flow/` | 04 | MOUNTED |
| `04-fig-plot` | `04-analysis/fig-plot/` | 04 | MOUNTED |
| `05-write-manuscript` | `05-manuscript/write-manuscript/` | 05 | MOUNTED |
| `05-write-reporting` | `05-manuscript/write-reporting/` | 05 | MOUNTED |
| `05-write-venue` | `05-manuscript/write-venue/` | 05 | MOUNTED |
| `05-write-polish` | `05-manuscript/write-polish/` | 05 | MOUNTED |
| `06-review-peer` | `06-review/review-peer/` | 06 | MOUNTED |
| `06-review-critique` | `06-review/review-critique/` | 06 | MOUNTED |
| `06-review-response` | `06-review/review-response/` | 06 | MOUNTED |

## MedSci-only interfaces (not in B)

| Id | MedSci path | Layer | Status |
|---|---|---|---|
| `04-explainability` | `skills/explainability/` | 04 | MOUNTED |
| `05-humanize` | `skills/humanize/` | 05 | MOUNTED |

## Backup candidates

- ARS `PROPOSED` · 7 mapped / 23 empty.
- MedSci `PROPOSED` · 27 mapped / 3 empty (02-pictures, 02-fmri, 04-fig-flow).
- Scientific `PROPOSED` · 21 mapped / 9 empty.

Mapping is not a source-wide mount.
