# 预设 MedSci · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 MedSci Skills（2026-09-01 HEAD）。仓库 [Aperivue/medsci-skills](https://github.com/Aperivue/medsci-skills) · 配置 `../sources/medsci.proposed.yaml`

按 30 个 A id 重适配。`present-paper` 不进 05。

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 27 / 30 |
| 空挂 | 3 |
| 扫描 | 2026-09-03 |

## 可挂 skills 接到哪一环

| A id | 对应 B | 来源路径 | 接到 A | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-tables` | `02-data-processing/tables/` | `skills/clean-data/; skills/batch-cohort/; skills/generate-codebook/; skills/define-variables/; skills/version-dataset/; skills/deidentify/` | `02_data-processing` | 已映射 | table/cohort cleaning, not Excel/COM |
| `02-imaging-io` | `02-data-processing/imaging-io/` | `skills/preprocess-imaging/` | `02_data-processing` | 已映射 | preprocess / convert; not QC |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | `skills/profile-imaging/; skills/uncertainty-imaging/` | `02_data-processing` | 已映射 | profile / uncertainty |
| `02-pictures` | `02-data-processing/pictures/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `02-fmri` | `02-data-processing/fmri/` | — | `02_data-processing` | 空挂 | 无对应包 |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | `skills/radiomics-ml/` | `02_data-processing` | 部分 | radiomics+ML; modeling still 04 |
| `03-lit-search` | `03-research/lit-search/` | `skills/search-lit/; skills/lit-sync/` | `03_research` | 已映射 |  |
| `03-lit-fulltext` | `03-research/lit-fulltext/` | `skills/fulltext-retrieval/` | `03_research` | 已映射 |  |
| `03-lit-review` | `03-research/lit-review/` | `skills/ma-scout/` | `03_research` | 部分 | scout/meta, not a dedicated review pack |
| `03-lit-cite` | `03-research/lit-cite/` | `skills/manage-refs/; skills/verify-refs/` | `03_research` | 已映射 |  |
| `03-design-experiment` | `03-research/design-experiment/` | `skills/design-study/; skills/intake-project/; skills/design-ai-benchmarking/` | `03_research` | 已映射 |  |
| `03-design-protocol` | `03-research/design-protocol/` | `skills/write-protocol/; skills/fill-protocol/` | `03_research` | 已映射 |  |
| `03-design-grant` | `03-research/design-grant/` | `skills/grant-builder/` | `03_research` | 已映射 | does not replace A Voice A/B |
| `03-frontier-ideate` | `03-research/frontier-ideate/` | `skills/find-cohort-gap/; skills/architecture-zoo/` | `03_research` | 部分 |  |
| `03-frontier-hypothesize` | `03-research/frontier-hypothesize/` | `skills/find-cohort-gap/; skills/ma-scout/` | `03_research` | 部分 | no hypogenic equivalent |
| `04-stats-guide` | `04-analysis/stats-guide/` | `skills/analyze-stats/` | `04_analysis` | 已映射 | does not replace A 04 personal / 0RAD |
| `04-stats-power` | `04-analysis/stats-power/` | `skills/calc-sample-size/` | `04_analysis` | 已映射 |  |
| `04-stats-models` | `04-analysis/stats-models/` | `skills/meta-analysis/` | `04_analysis` | 部分 | pooling only; 0RAD personal still wins |
| `04-model-eval` | `04-analysis/model-eval/` | `skills/model-evaluation/; skills/model-validation/` | `04_analysis` | 已映射 |  |
| `04-fig-flow` | `04-analysis/fig-flow/` | — | `04_analysis` | 空挂 | make-figures 接到 fig-plot |
| `04-fig-plot` | `04-analysis/fig-plot/` | `skills/make-figures/` | `04_analysis` | 已映射 | POLE gold still B/A |
| `04-explainability` | —（MedSci） | `skills/explainability/` | `04_analysis` | 已映射 | imaging XAI; not in B |
| `05-write-manuscript` | `05-manuscript/write-manuscript/` | `skills/write-paper/` | `05_manuscript` | 已映射 | not Aitor-format; present-paper 不进 05 |
| `05-write-reporting` | `05-manuscript/write-reporting/` | `skills/check-reporting/` | `05_manuscript` | 已映射 |  |
| `05-write-venue` | `05-manuscript/write-venue/` | `skills/find-journal/; skills/add-journal/` | `05_manuscript` | 已映射 | not Aitor-format |
| `05-write-polish` | `05-manuscript/write-polish/` | `skills/polish-language/` | `05_manuscript` | 已映射 | not A personal de-AI |
| `05-humanize` | —（MedSci） | `skills/humanize/` | `05_manuscript` | 已映射 | does not replace A personal de-AI |
| `06-review-peer` | `06-review/review-peer/` | `skills/peer-review/; skills/review-paper/` | `06_review` | 已映射 |  |
| `06-review-critique` | `06-review/review-critique/` | `skills/self-review/` | `06_review` | 已映射 |  |
| `06-review-response` | `06-review/review-response/` | `skills/revise/` | `06_review` | 已映射 |  |

## 仅用当前挂载 · 空挂

**3 个空挂。** `02-pictures`、`02-fmri`、`04-fig-flow`。若只用本套，先通知再检索确认。


## A 没有对应接口



这些 skill 在 MedSci 里存在，但不在 30 个挂载 id 上。分两类：真扩展候选，和 A 已有层/人但没有挂载接口。

### 扩展候选（A 没有对应包）

| 路径 | 做什么 | 以后可接到 |
|---|---|---|
| `skills/academic-aio/` | 面向 AI 检索/RAG 的论文优化 | 新 05 或 03 接口 |
| `skills/author-strategy/` | PubMed 作者画像与发文策略 | 新 03 接口 |
| `skills/cross-national/` | 跨国队列对齐（KNHANES/NHANES/CHNS） | 新 03/04 接口 |
| `skills/fill-icmje-coi/` | ICMJE 利益冲突表 | 新 03；A 伦理包是医院 IRB，不是这张表 |
| `skills/mllm-eval/` | 临床 LLM/MLLM 评测框架 | 新 04 接口 |
| `skills/model-card/` | Model Card / Datasheet | 新 04 接口 |
| `skills/model-scaffold/` | 医学影像 PyTorch 训练仓脚手架 | 新 02/04 接口 |
| `skills/model-sourcing/` | 第三方模型版本/权重审验 | 新 04 接口 |
| `skills/obsidian-paper-vault/` | PDF → Obsidian 文献库 | 新 03 工具接口 |
| `skills/render-pdf-doc/` | Markdown → 发表级 PDF | 新 05 接口 |
| `skills/replicate-study/` | 把已发表队列方法复现到另一数据库 | 新 03 接口 |

### 仅有类比、没有挂载 id

| 路径 | 做什么 | A 侧类比 |
|---|---|---|
| `skills/orchestrate/` | 多步路由到 MedSci skill | `00_orchestrator` |
| `skills/manage-project/` | 课题/稿件项目管理 | `00_orchestrator` |
| `skills/setup-medsci/` | 运行时体检 | `01` |
| `skills/contribute/` | 把本地改动贡献回仓库 | `skill-harvest` / 01 |
| `skills/publish-skill/` | 把个人 skill 发成可分发包 | `skill-harvest` / 01 |
| `skills/sync-submission/` | 投稿清单 / SSOT 对账 | Bai（投稿专员，不是 skill） |

## A 没有对应接口



这些 skill 在 MedSci 里存在，但不在 30 个挂载 id 上。分两类：真扩展候选，和 A 已有层/人但没有挂载接口。

### 扩展候选（A 没有对应包）

| 路径 | 做什么 | 以后可接到 |
|---|---|---|
| `skills/academic-aio/` | 面向 AI 检索/RAG 的论文优化 | 新 05 或 03 接口 |
| `skills/author-strategy/` | PubMed 作者画像与发文策略 | 新 03 接口 |
| `skills/cross-national/` | 跨国队列对齐（KNHANES/NHANES/CHNS） | 新 03/04 接口 |
| `skills/fill-icmje-coi/` | ICMJE 利益冲突表 | 新 03；A 伦理包是医院 IRB，不是这张表 |
| `skills/mllm-eval/` | 临床 LLM/MLLM 评测框架 | 新 04 接口 |
| `skills/model-card/` | Model Card / Datasheet | 新 04 接口 |
| `skills/model-scaffold/` | 医学影像 PyTorch 训练仓脚手架 | 新 02/04 接口 |
| `skills/model-sourcing/` | 第三方模型版本/权重审验 | 新 04 接口 |
| `skills/obsidian-paper-vault/` | PDF → Obsidian 文献库 | 新 03 工具接口 |
| `skills/render-pdf-doc/` | Markdown → 发表级 PDF | 新 05 接口 |
| `skills/replicate-study/` | 把已发表队列方法复现到另一数据库 | 新 03 接口 |

### 仅有类比、没有挂载 id

| 路径 | 做什么 | A 侧类比 |
|---|---|---|
| `skills/orchestrate/` | 多步路由到 MedSci skill | `00_orchestrator` |
| `skills/manage-project/` | 课题/稿件项目管理 | `00_orchestrator` |
| `skills/setup-medsci/` | 运行时体检 | `01` |
| `skills/contribute/` | 把本地改动贡献回仓库 | `skill-harvest` / 01 |
| `skills/publish-skill/` | 把个人 skill 发成可分发包 | `skill-harvest` / 01 |
| `skills/sync-submission/` | 投稿清单 / SSOT 对账 | Bai（投稿专员，不是 skill） |

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
