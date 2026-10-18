# 02 handoff -- raw -> analysis-ready

Loopnow owns **02 execution** (clean, extract, imaging QC, soft-coding scripts, leakage first-pass). This skill **does not** do statistical modelling / feature selection / manuscript numbers.

| Need | Seat / skill |
|---|---|
| Methods / which test / pipeline / reported numbers | `04_analysis` (`personal/pipeline.md`, `04_analysis/qc/report-checks.md`) |
| Literature / Evidence Pack | `03_research` |
| Manuscript prose / Track Changes | `05_manuscript` |
| Review annotate | `06_review` |
| Response letter | `07_response` |
| Exit QC / Gates | `00_orchestrator` |

## Boundary

- **Receives:** raw clinical / imaging / picture / fMRI exports; user scripts under `{script_data_processing}` / `{script_root}`.
- **Gives:** analysis-ready tables, QC logs, extraction outputs, leakage/split notes -- then **handoff to 04**.
- **Does not:** feature selection, model fitting, Table 1 / NHST ownership, IMRAD prose.

## A/B note

Capability bodies for 02 mounts live in A `02_data-processing/base/` (pilot 2026-10-17). A02 personal top layer stays route/handoff + true personal files above.
