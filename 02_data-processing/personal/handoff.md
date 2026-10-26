# 02 handoff -- raw -> analysis-ready

Loopnow owns **02 execution** (clean, extract, imaging QC, soft-coding scripts, leakage first-pass). This skill **does not** do statistical modelling / feature selection / manuscript numbers.

| Need | Seat / skill |
|---|---|
| Methods / which test / pipeline / reported numbers | same skill, analysis half: `02_data-processing/personal/analysis/pipeline.md`, `02_data-processing/qc/report-checks.md` |
| Literature / Evidence Pack | `03_research` |
| Manuscript prose / Track Changes | `05_manuscript` |
| Review annotate | `06_review` |
| Response letter | `07_response` |
| Exit QC / Gates | `00_orchestrator` |

## Boundary

- **Receives:** raw clinical / imaging / picture / fMRI exports; user scripts under `{code_data_processing}` / `{code_root}`.
- **Gives:** analysis-ready tables, QC logs, extraction outputs, leakage/split notes -- then **handoff to the 02 analysis half** (`02_data-processing/personal/analysis/handoff.md`).
- **Does not:** feature selection, model fitting, Table 1 / NHST ownership, IMRAD prose.

## Note

Capability bodies for 02 fine ids live in `02_data-processing/base/` (pilot 2026-10-17). 02 personal top layer stays route/handoff + true personal files above.
