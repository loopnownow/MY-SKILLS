# 预设 ARS · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 Academic Research Skills（2026-09-01 HEAD）。仓库 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) · 配置 `../sources/ars.proposed.yaml`

按 30 个 A id 重适配。ARS 仍只有 4 个包，所以若干 id 共用一个 ARS 文件夹。

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 7 / 30 |
| 空挂 | 23 |
| 扫描 | 2026-09-03 |

## 可挂 skills 接到哪一环

| A id | 对应 B | 来源路径 | 接到 A | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-tables` | `02-data-processing/tables/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `02-imaging-io` | `02-data-processing/imaging-io/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `02-pictures` | `02-data-processing/pictures/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `02-fmri` | `02-data-processing/fmri/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `03-lit-search` | `03-research/lit-search/` | `deep-research/` | `03_research` | 已映射 | paper search / source verification |
| `03-lit-fulltext` | `03-research/lit-fulltext/` | — | `03_research` | 空挂 | 无对应包 |
| `03-lit-review` | `03-research/lit-review/` | `deep-research/` | `03_research` | 已映射 | systematic review inside deep-research |
| `03-lit-cite` | `03-research/lit-cite/` | — | `03_research` | 空挂 | 无对应包 |
| `03-design-experiment` | `03-research/design-experiment/` | `deep-research/` | `03_research` | 部分 | methodology / RQ framing |
| `03-design-protocol` | `03-research/design-protocol/` | — | `03_research` | 空挂 | 无对应包 |
| `03-design-grant` | `03-research/design-grant/` | — | `03_research` | 空挂 | 无对应包 |
| `03-frontier-ideate` | `03-research/frontier-ideate/` | — | `03_research` | 空挂 | 无对应包 |
| `03-frontier-hypothesize` | `03-research/frontier-hypothesize/` | — | `03_research` | 空挂 | 无对应包 |
| `04-stats-guide` | `04-analysis/stats-guide/` | — | `04_analysis` | 空挂 | 无对应包 |
| `04-stats-power` | `04-analysis/stats-power/` | — | `04_analysis` | 空挂 | 无对应包 |
| `04-stats-models` | `04-analysis/stats-models/` | — | `04_analysis` | 空挂 | 无对应包 |
| `04-model-eval` | `04-analysis/model-eval/` | — | `04_analysis` | 空挂 | 无对应包 |
| `04-fig-flow` | `04-analysis/fig-flow/` | — | `04_analysis` | 空挂 | 无对应包 |
| `04-fig-plot` | `04-analysis/fig-plot/` | — | `04_analysis` | 空挂 | 无对应包 |
| `04-explainability` | —（MedSci） | — | `04_analysis` | 空挂 | 无对应包 |
| `05-write-manuscript` | `05-manuscript/write-manuscript/` | `academic-paper/` | `05_manuscript` | 已映射 | write / plan / outline; not Aitor-format |
| `05-write-reporting` | `05-manuscript/write-reporting/` | — | `05_manuscript` | 空挂 | 无对应包 |
| `05-write-venue` | `05-manuscript/write-venue/` | `academic-paper/` | `05_manuscript` | 部分 | format / style calibration |
| `05-write-polish` | `05-manuscript/write-polish/` | `academic-paper/` | `05_manuscript` | 部分 | style calibration; not de-AI |
| `05-humanize` | —（MedSci） | — | `05_manuscript` | 空挂 | 无对应包 |
| `06-review-peer` | `06-review/review-peer/` | `academic-paper-reviewer/` | `06_review` | 已映射 | multi-persona peer review |
| `06-review-critique` | `06-review/review-critique/` | — | `06_review` | 空挂 | 无对应包 |
| `06-review-response` | `06-review/review-response/` | — | `06_review` | 空挂 | 无对应包 |

## 仅用当前挂载 · 空挂

**23 个空挂。** `02-tables`、`02-imaging-io`、`02-imaging-qc`、`02-pictures`、`02-fmri`、`02-radiomics-habitat`、`03-lit-fulltext`、`03-lit-cite`、`03-design-protocol`、`03-design-grant`、`03-frontier-ideate`、`03-frontier-hypothesize`、`04-stats-guide`、`04-stats-power`、`04-stats-models`、`04-model-eval`、`04-fig-flow`、`04-fig-plot`、`04-explainability`、`05-write-reporting`、`05-humanize`、`06-review-critique`、`06-review-response`。若只用本套，先通知再检索确认。

额外：`academic-pipeline/` 对应 00 调度，不计入领域 id。


机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
