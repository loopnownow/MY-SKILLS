# 预设 B · 当前默认

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 B。来源 [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) · 配置 `../sources/b-my-skills-capabilities.yaml`

| | |
|---|---|
| 状态 | MOUNTED（默认来源） |
| B 包 | 12 / 12 有文件 |
| 空挂 | 0 |
| 双轨 | 3（A 仍留 literature / design / frontier） |

## 挂载来源

| 字段 | 值 |
|---|---|
| 来源 | MY-SKILLS-capabilities（B） |
| 角色 | 默认挂载 |
| 状态 | MOUNTED |
| 仓库 | [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) |
| 配置 | `../sources/b-my-skills-capabilities.yaml` |

## 可挂 skills 接到哪一环

| Id | 来源路径 | 接到 A | 做什么 | 对接 | 仅用本套 |
|---|---|---|---|---|---|
| `02-xlsx` | `02-data-processing/xlsx/` | `02_data-processing` | Excel / CSV → 分析可用表 | 就绪 | 15 文件 |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | `02_data-processing` | 影像预处理与 QC | 就绪 | 6 文件 |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | `02_data-processing` | radiomics / 生境准备（建模交 04） | 就绪 | 9 文件 |
| `02-impute` | `02-data-processing/impute/` | `02_data-processing` | 缺失 / 异常值 | 就绪 | 7 文件 |
| `02-generic-docs` | `02-data-processing/generic-docs/` | `02_data-processing` | 通用影像/数据说明 | 就绪 | 7 文件 |
| `03-literature` | `03-research/literature/` | `03_research` | 文献 / 来源 / 选刊 | 双轨 | 6 文件 · A 仍留 literature/ |
| `03-design` | `03-research/design/` | `03_research` | 研究设计 / 验证 / 蓝图 | 双轨 | 8 文件 · A 仍留 design/ |
| `03-frontier` | `03-research/frontier/` | `03_research` | 前沿主题 / 问题化 | 双轨 | 7 文件 · A 仍留 frontier/ |
| `04-stats-generic` | `04-analysis/stats-generic/` | `04_analysis` | 通用统计百科 | 就绪 | 7 文件 · 实验室口径在 A personal/ |
| `04-figure-engine` | `04-analysis/figure-engine/` | `04_analysis` | 出图 | 就绪 | 22 文件 |
| `05-writing-generic` | `05-manuscript/writing-generic/` | `05_manuscript` | 通用写作 / 报告 / 期刊体例 | 就绪 | 28 文件 · Aitor-format + de-AI 在 A |
| `06-review-generic` | `06-review/review-generic/` | `06_review` | 预审 / 回复机械层 | 就绪 | 12 文件 · 个人审稿声音在 A |

## 非 B 接口（接到 MedSci）

这两条是 A 接口，通用包在 MedSci，不在 B。不算本套空挂。个人 de-AI 仍在 A `05_manuscript/personal/`。

| Id | 来源路径 | 接到 A | 做什么 | 对接 |
|---|---|---|---|---|
| `04-explainability` | `skills/explainability/` | `04_analysis` | 影像模型可解释性（Grad-CAM 等） | MedSci |
| `05-humanize` | `skills/humanize/` | `05_manuscript` | 去 AI 痕迹（通用） | MedSci |

## 仅用当前挂载 · 空挂

**无空挂。** 12 个 A 期望 id 在 B 里都有文件。03 literature / design / frontier 是双轨（A 仍留副本），不是空包。个人 de-AI 不经 B。

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
