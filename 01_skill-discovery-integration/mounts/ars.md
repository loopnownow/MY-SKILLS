# 预设 ARS · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 Academic Research Skills（2026-09-01 HEAD）。仓库 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) · 配置 `../sources/ars.proposed.yaml`

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 6 / 22 |
| 空挂 | 16 |
| 扫描 | 2026-09-03 · `9443623` |

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-xlsx` | — | `02_data-processing` | Excel / CSV → 分析可用表 | 空挂 | 无对应包 |
| `02-imaging-qc` | — | `02_data-processing` | 影像预处理与 QC | 空挂 | 无对应包 |
| `02-radiomics-habitat` | — | `02_data-processing` | radiomics / 生境准备（建模交 04） | 空挂 | 无对应包 |
| `02-impute` | — | `02_data-processing` | 缺失 / 异常值 | 空挂 | 无对应包 |
| `02-generic-docs` | — | `02_data-processing` | 通用影像/数据说明 | 空挂 | 无对应包 |
| `03-lit-search` | `deep-research/` | `03_research` | 文献检索 / 全文 | 已映射 | paper search / source verification |
| `03-lit-review` | `deep-research/` | `03_research` | 综述 / 综合 | 已映射 | systematic review inside deep-research |
| `03-lit-cite` | — | `03_research` | 引文库 / Zotero | 空挂 | 无对应包 |
| `03-design-experiment` | `deep-research/` | `03_research` | 采集前实验设计 | 部分 | methodology / RQ framing; not a standalone design pack |
| `03-design-grant` | — | `03_research` | 标书（通用）；个人 Voice A/B 优先 | 空挂 | 无对应包 |
| `03-frontier-ideate` | — | `03_research` | 选题 / 头脑风暴 | 空挂 | 无对应包 |
| `03-frontier-hypothesize` | — | `03_research` | 问题化 / 假说 | 空挂 | 无对应包 |
| `04-stats-guide` | — | `04_analysis` | 选检验 / 效应量 | 空挂 | 无对应包 |
| `04-stats-power` | — | `04_analysis` | 样本量 / 功效 | 空挂 | 无对应包 |
| `04-stats-models` | — | `04_analysis` | 统计/ML 实现层 | 空挂 | 无对应包 |
| `04-figure-engine` | — | `04_analysis` | 出图 | 空挂 | 无对应包 |
| `04-explainability` | — | `04_analysis` | 影像模型可解释性 | 空挂 | 无对应包 |
| `05-write-manuscript` | `academic-paper/` | `05_manuscript` | 论著/报告草稿 | 已映射 | write / plan / outline; not Aitor-format |
| `05-write-venue` | `academic-paper/` | `05_manuscript` | 期刊/会议体例 | 部分 | format / style calibration; not Aitor-format |
| `05-humanize` | — | `05_manuscript` | 去 AI 痕迹（通用） | 空挂 | 无对应包 |
| `06-review-peer` | `academic-paper-reviewer/` | `06_review` | 他审草稿 | 已映射 | multi-persona peer review |
| `06-review-critique` | — | `06_review` | 自审 / 证据质量 | 空挂 | 无对应包 |

额外：`academic-pipeline/` 对应 00 调度，不计入 22 个领域 id。

## 仅用当前挂载 · 空挂

**16 个空挂。** 若只用 ARS，先通知再检索确认。已映射：`03-lit-search` / `03-lit-review` / `03-design-experiment`（部分）/ `05-write-manuscript` / `05-write-venue`（部分）/ `06-review-peer`。

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
