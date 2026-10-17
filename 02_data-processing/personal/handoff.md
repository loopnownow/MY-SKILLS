# 02 handoff — raw → analysis-ready

Loopnow owns **02 execution**（清理、抽取、影像/表 QC、软编码脚本、泄漏初检）。本技能**不做**统计建模 / 特征筛选 / 稿件数字。

| Need | Seat / skill |
|---|---|
| Methods / which test / pipeline / reported numbers | `04_analysis`（`personal/pipeline.md`, `personal/report-checks.md`） |
| Literature / Evidence Pack | `03_research` |
| Manuscript prose / Track Changes | `05_manuscript` |
| Review annotate / response | `06_review` |
| Exit QC / Gates | `00_orchestrator` |

## Boundary

- **Receives:** raw clinical / imaging / picture / fMRI exports; user scripts under `{script_data_processing}` / `{script_root}`.
- **Gives:** analysis-ready tables, QC logs, extraction outputs, leakage/split notes — then **handoff to 04**.
- **Does not:** feature selection, model fitting, Table 1 / NHST ownership, IMRAD prose.
