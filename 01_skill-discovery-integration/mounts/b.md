# 预设 B · 当前默认

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 B。来源 [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) · 配置 `../sources/b-my-skills-capabilities.yaml`

| | |
|---|---|
| 状态 | MOUNTED（默认来源） |
| B 包 | 20 个 id 有文件夹（若干 id 共用 literature / design / frontier / stats-generic / writing-generic / review-generic） |
| 空挂 | 0 |
| 双轨 | 03 三包（A 仍留副本） |

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
| `03-lit-search` | `03-research/literature/` | `03_research` | 文献检索 / 全文 | 双轨 | 6 文件 · A 仍留 literature/ |
| `03-lit-review` | `03-research/literature/` | `03_research` | 综述 / 综合 | 双轨 | 同上 |
| `03-lit-cite` | `03-research/literature/` | `03_research` | 引文库 / Zotero | 双轨 | 同上 |
| `03-design-experiment` | `03-research/design/` | `03_research` | 采集前实验设计 | 双轨 | 8 文件 · A 仍留 design/ |
| `03-design-grant` | `03-research/design/` | `03_research` | 标书（通用）；个人 Voice A/B 优先 | 双轨 | 同上 |
| `03-frontier-ideate` | `03-research/frontier/` | `03_research` | 选题 / 头脑风暴 | 双轨 | 7 文件 · A 仍留 frontier/ |
| `03-frontier-hypothesize` | `03-research/frontier/` | `03_research` | 问题化 / 假说 | 双轨 | 同上 |
| `04-stats-guide` | `04-analysis/stats-generic/` | `04_analysis` | 选检验 / 效应量 | 就绪 | 7 文件 · 实验室口径在 A personal/ |
| `04-stats-power` | `04-analysis/stats-generic/` | `04_analysis` | 样本量 / 功效 | 就绪 | 同上 |
| `04-stats-models` | `04-analysis/stats-generic/` | `04_analysis` | 统计/ML 实现层 | 就绪 | 同上 · 0RAD personal 仍赢 |
| `04-figure-engine` | `04-analysis/figure-engine/` | `04_analysis` | 出图 | 就绪 | 22 文件 |
| `05-write-manuscript` | `05-manuscript/writing-generic/` | `05_manuscript` | 论著/报告草稿 | 就绪 | 28 文件 · Aitor-format 在 A |
| `05-write-venue` | `05-manuscript/writing-generic/` | `05_manuscript` | 期刊/会议体例 | 就绪 | 同上 |
| `06-review-peer` | `06-review/review-generic/` | `06_review` | 他审草稿 | 就绪 | 12 文件 · 个人审稿声音在 A |
| `06-review-critique` | `06-review/review-generic/` | `06_review` | 自审 / 证据质量 | 就绪 | 同上 |

## 非 B 接口（接到 MedSci）

| Id | 来源路径 | 接到 A | 做什么 | 对接 |
|---|---|---|---|---|
| `04-explainability` | `skills/explainability/` | `04_analysis` | 影像模型可解释性（Grad-CAM 等） | MedSci |
| `05-humanize` | `skills/humanize/` | `05_manuscript` | 去 AI 痕迹（通用） | MedSci |

## 仅用当前挂载 · 空挂

**无空挂。** 20 个 B 源 id 都有文件夹。03 三包双轨。个人 de-AI 不经 B。

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
