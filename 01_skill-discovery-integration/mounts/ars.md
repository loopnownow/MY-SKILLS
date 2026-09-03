# 预设 ARS · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md)

仅用 Academic Research Skills（2026-09-01 HEAD）。仓库 [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) · 配置 `../sources/ars.proposed.yaml`

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 4 / 14（含 1 部分） |
| 空挂 | 10 |
| 扫描 | 2026-09-03 · `9443623` |

## 挂载来源

| 字段 | 值 |
|---|---|
| 来源 | Academic Research Skills |
| 扫描 | 2026-09-03 · `9443623` |
| 角色 | 备份 |
| 状态 | PROPOSED |

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-xlsx` | — | `02_data-processing` | Excel / CSV | 空挂 | 无对应包 |
| `02-imaging-qc` | — | `02_data-processing` | 影像 QC | 空挂 | 无对应包 |
| `02-radiomics-habitat` | — | `02_data-processing` | radiomics / 生境准备 | 空挂 | 无对应包 |
| `02-impute` | — | `02_data-processing` | 缺失 / 异常值 | 空挂 | 无对应包 |
| `02-generic-docs` | — | `02_data-processing` | 通用数据说明 | 空挂 | 无对应包 |
| `03-literature` | `deep-research/` | `03_research` | 文献 / 系统综述 / 核源 | 已映射 | lit-review / systematic review |
| `03-design` | `deep-research/` | `03_research` | 方法学 / 问题化 | 部分 | 包在 deep-research 内，不是独立设计包 |
| `03-frontier` | — | `03_research` | 前沿主题 | 空挂 | 无对应包 |
| `04-stats-generic` | — | `04_analysis` | 通用统计 | 空挂 | 无对应包 |
| `04-figure-engine` | — | `04_analysis` | 出图 | 空挂 | 无对应包 |
| `04-explainability` | — | `04_analysis` | 影像模型可解释性 | 空挂 | 无对应包 · 接口在 MedSci |
| `05-writing-generic` | `academic-paper/` | `05_manuscript` | 写作 / 提纲 / 引用检查 | 已映射 | 不是 Aitor-format |
| `05-humanize` | — | `05_manuscript` | 去 AI 痕迹（通用） | 空挂 | 无对应包 · 接口在 MedSci |
| `06-review-generic` | `academic-paper-reviewer/` | `06_review` | 多角色审稿 / 复审 | 已映射 | rebuttal-audit 也在 academic-paper |

额外：`academic-pipeline/` 对应 00 调度（编排 analog），不计入 14 个领域 id。

## 仅用当前挂载 · 空挂

**10 个空挂：** `02-xlsx` · `02-imaging-qc` · `02-radiomics-habitat` · `02-impute` · `02-generic-docs` · `03-frontier` · `04-stats-generic` · `04-figure-engine` · `04-explainability` · `05-humanize`。

这些在 ARS 里没有包。若只用 ARS，先通知再检索确认，不要静默改挂。已映射的 03/05/06 可直接按上表路径用。

## A 没有对应接口

这些 skill 在 ARS 里存在，但不在 14 个挂载 id 上。00 是调度层，不是可挂 id。

| 路径 | 做什么 | 类型 | 以后可接到 |
|---|---|---|---|
| `academic-pipeline/` | 文献→写作→审稿编排 | 类比 | `00_orchestrator`（已有层，无挂载 id） |

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
