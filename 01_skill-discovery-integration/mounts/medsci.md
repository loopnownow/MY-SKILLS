# 预设 MedSci · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 MedSci Skills（2026-09-01 HEAD）。仓库 [Aperivue/medsci-skills](https://github.com/Aperivue/medsci-skills) · 配置 `../sources/medsci.proposed.yaml`

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 22 / 22（若干部分） |
| 空挂 | 0 |
| 扫描 | 2026-09-03 · `912f7e8` |

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-xlsx` | `skills/clean-data/; skills/batch-cohort/; skills/generate-codebook/` | `02_data-processing` | Excel / CSV → 分析可用表 | 部分 | table/cohort cleaning, not Excel/COM |
| `02-imaging-qc` | `skills/preprocess-imaging/; skills/profile-imaging/; skills/uncertainty-imaging/` | `02_data-processing` | 影像预处理与 QC | 已映射 |  |
| `02-radiomics-habitat` | `skills/radiomics-ml/` | `02_data-processing` | radiomics / 生境准备（建模交 04） | 部分 | radiomics+ML; modeling still 04 |
| `02-impute` | `skills/clean-data/` | `02_data-processing` | 缺失 / 异常值 | 部分 | inside cleaning |
| `02-generic-docs` | `skills/deidentify/; skills/define-variables/; skills/version-dataset/; skills/generate-codebook/` | `02_data-processing` | 通用影像/数据说明 | 已映射 |  |
| `03-lit-search` | `skills/search-lit/; skills/fulltext-retrieval/; skills/lit-sync/` | `03_research` | 文献检索 / 全文 | 已映射 |  |
| `03-lit-review` | `skills/ma-scout/` | `03_research` | 综述 / 综合 | 部分 | scout/meta, not a dedicated review pack |
| `03-lit-cite` | `skills/manage-refs/; skills/verify-refs/; skills/find-journal/; skills/add-journal/` | `03_research` | 引文库 / Zotero | 已映射 |  |
| `03-design-experiment` | `skills/design-study/; skills/write-protocol/; skills/fill-protocol/; skills/intake-project/; skills/design-ai-benchmarking/` | `03_research` | 采集前实验设计 | 已映射 |  |
| `03-design-grant` | `skills/grant-builder/` | `03_research` | 标书（通用）；个人 Voice A/B 优先 | 已映射 | does not replace A Voice A/B |
| `03-frontier-ideate` | `skills/find-cohort-gap/; skills/architecture-zoo/` | `03_research` | 选题 / 头脑风暴 | 部分 |  |
| `03-frontier-hypothesize` | `skills/find-cohort-gap/; skills/ma-scout/` | `03_research` | 问题化 / 假说 | 部分 | no hypogenic equivalent |
| `04-stats-guide` | `skills/analyze-stats/` | `04_analysis` | 选检验 / 效应量 | 已映射 | does not replace A 04 personal / 0RAD |
| `04-stats-power` | `skills/calc-sample-size/` | `04_analysis` | 样本量 / 功效 | 已映射 |  |
| `04-stats-models` | `skills/model-evaluation/; skills/model-validation/; skills/meta-analysis/` | `04_analysis` | 统计/ML 实现层 | 已映射 |  |
| `04-figure-engine` | `skills/make-figures/` | `04_analysis` | 出图 | 已映射 | POLE/STROBE gold still B/A |
| `04-explainability` | `skills/explainability/` | `04_analysis` | 影像模型可解释性 | 已映射 | imaging XAI; not in B |
| `05-write-manuscript` | `skills/write-paper/; skills/polish-language/; skills/present-paper/` | `05_manuscript` | 论著/报告草稿 | 已映射 | not Aitor-format |
| `05-write-venue` | `skills/check-reporting/` | `05_manuscript` | 期刊/会议体例 | 部分 | reporting guidelines, not journal templates |
| `05-humanize` | `skills/humanize/` | `05_manuscript` | 去 AI 痕迹（通用） | 已映射 | does not replace A personal de-AI |
| `06-review-peer` | `skills/peer-review/; skills/review-paper/` | `06_review` | 他审草稿 | 已映射 |  |
| `06-review-critique` | `skills/self-review/; skills/revise/` | `06_review` | 自审 / 证据质量 | 已映射 |  |

## 仅用当前挂载 · 空挂

**无空挂。** 22 个 A id 都能指到 MedSci 路径。部分覆盖不够用时，先通知再检索。

## A 没有对应接口


这些 skill 在 MedSci 里存在，但不在 22 个挂载 id 上。分两类：真扩展候选，和 A 已有层/人但没有挂载接口。

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
