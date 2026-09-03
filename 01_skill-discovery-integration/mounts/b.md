# 预设 B · 当前默认

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 B。来源 [loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) · 配置 `../sources/b-my-skills-capabilities.yaml`

| | |
|---|---|
| 状态 | MOUNTED（默认来源） |
| B 包 | 28 个 id 各一个文件夹（CHG-20260903-011） |
| 空挂 | 0 |
| 双轨 | 03 A 仍留 `literature/` `design/` `frontier/` 副本 |

## 可挂 skills 接到哪一环

| Id | 来源路径 | 接到 A | 做什么 | 对接 | 仅用本套 |
|---|---|---|---|---|---|
| `02-tables` | `02-data-processing/tables/` | `02_data-processing` | 临床表 Excel / CSV（含缺失/异常值） | 就绪 | 24 文件 |
| `02-imaging-io` | `02-data-processing/imaging-io/` | `02_data-processing` | CT/MRI 读写 · DICOM / NIfTI / NII | 就绪 | 1 文件（槽） |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | `02_data-processing` | CT/MRI QC · ROI / 阅片 | 就绪 | 11 文件 |
| `02-pictures` | `02-data-processing/pictures/` | `02_data-processing` | 图片 TIFF / PNG / JPG / PDF(图) | 就绪 | 1 文件（槽） |
| `02-fmri` | `02-data-processing/fmri/` | `02_data-processing` | fMRI · DICOM / NIfTI | 就绪 | 1 文件（槽） |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | `02_data-processing` | radiomics / 生境准备（建模交 04） | 就绪 | 9 文件 |
| `03-lit-search` | `03-research/lit-search/` | `03_research` | 文献检索 | 双轨 | 4 文件 · A 仍留 literature/ |
| `03-lit-fulltext` | `03-research/lit-fulltext/` | `03_research` | 全文获取 | 就绪 | 1 文件（槽） |
| `03-lit-review` | `03-research/lit-review/` | `03_research` | 综述 / 综合 | 就绪 | 2 文件 |
| `03-lit-cite` | `03-research/lit-cite/` | `03_research` | DOI→BibTeX（无 Zotero 包） | 就绪 | 2 文件 |
| `03-design-experiment` | `03-research/design-experiment/` | `03_research` | 采集前实验设计 | 双轨 | 8 文件 · A 仍留 design/ |
| `03-design-protocol` | `03-research/design-protocol/` | `03_research` | 写方案 / 填方案 | 就绪 | 1 文件（槽） |
| `03-design-grant` | `03-research/design-grant/` | `03_research` | 标书（通用槽）；个人 Voice A/B 优先 | 就绪 | 1 文件（空壳 MODULE） |
| `03-frontier-ideate` | `03-research/frontier-ideate/` | `03_research` | 选题 / 头脑风暴 | 双轨 | 5 文件 · A 仍留 frontier/ |
| `03-frontier-hypothesize` | `03-research/frontier-hypothesize/` | `03_research` | 问题化 / 假说 | 就绪 | 3 文件 |
| `04-stats-guide` | `04-analysis/stats-guide/` | `04_analysis` | 选检验 / 效应量 | 就绪 | 4 文件 |
| `04-stats-power` | `04-analysis/stats-power/` | `04_analysis` | 样本量 / 功效 | 就绪 | 2 文件 |
| `04-stats-models` | `04-analysis/stats-models/` | `04_analysis` | 统计/ML 拟合 | 就绪 | 3 文件 |
| `04-model-eval` | `04-analysis/model-eval/` | `04_analysis` | 校准 / DCA / 外验证 | 就绪 | 1 文件（槽） |
| `04-fig-flow` | `04-analysis/fig-flow/` | `04_analysis` | STROBE / 入组流程图 | 就绪 | 5 文件 |
| `04-fig-plot` | `04-analysis/fig-plot/` | `04_analysis` | 统计图 / 影像拼图 | 就绪 | 18 文件 |
| `05-write-manuscript` | `05-manuscript/write-manuscript/` | `05_manuscript` | 论著/报告草稿 | 就绪 | 16 文件 |
| `05-write-reporting` | `05-manuscript/write-reporting/` | `05_manuscript` | TRIPOD / CLAIM / 报告规范 | 就绪 | 6 文件 |
| `05-write-venue` | `05-manuscript/write-venue/` | `05_manuscript` | 期刊体例 / house style（not 选刊） | 就绪 | 7 文件 |
| `05-write-polish` | `05-manuscript/write-polish/` | `05_manuscript` | 通用学术英语润色 | 就绪 | 3 文件 |
| `06-review-peer` | `06-review/review-peer/` | `06_review` | 他审草稿 | 就绪 | 5 文件 |
| `06-review-critique` | `06-review/review-critique/` | `06_review` | 自审 / 投稿前找洞 | 就绪 | 4 文件 |
| `06-review-response` | `06-review/review-response/` | `06_review` | 回复审稿人 | 就绪 | 5 文件 |

## 非 B 接口（接到 MedSci）

| Id | 来源路径 | 接到 A | 说明 |
|---|---|---|---|
| `04-explainability` | `skills/explainability/` | `04_analysis` | 影像模型可解释性 |
| `05-humanize` | `skills/humanize/` | `05_manuscript` | 去 AI 痕迹（通用） |

## 仅用当前挂载 · 空挂

**无空挂。** 28 个 B id 各有文件夹。若干是通用槽（MODULE 空壳），不是空挂。

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。
