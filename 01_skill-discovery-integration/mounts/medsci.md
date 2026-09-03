# 预设 MedSci · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 MedSci Skills（2026-09-01 HEAD）。仓库 [Aperivue/medsci-skills](https://github.com/Aperivue/medsci-skills) · 配置 `../sources/medsci.proposed.yaml`

按 B 拆开后的 22 个 A id 重适配。`find-journal/` / `add-journal/` 从 cite 改接到 `05-write-venue`（与 B 选刊包对齐）。

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 22 / 22（若干部分） |
| 空挂 | 0 |
| 扫描 | 2026-09-03 · `912f7e8` |

## 可挂 skills 接到哪一环

| A id | 对应 B | MedSci 路径 | 接到 A | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-xlsx` | `02-data-processing/xlsx/` | `skills/clean-data/; skills/batch-cohort/; skills/generate-codebook/` | `02_data-processing` | 部分 | table/cohort cleaning, not Excel/COM |
| `02-imaging-qc` | `02-data-processing/imaging-qc/` | `skills/preprocess-imaging/; skills/profile-imaging/; skills/uncertainty-imaging/` | `02_data-processing` | 已映射 |  |
| `02-radiomics-habitat` | `02-data-processing/radiomics-habitat/` | `skills/radiomics-ml/` | `02_data-processing` | 部分 | radiomics+ML; modeling still 04 |
| `02-impute` | `02-data-processing/impute/` | `skills/clean-data/` | `02_data-processing` | 部分 | inside cleaning |
| `02-generic-docs` | `02-data-processing/generic-docs/` | `skills/deidentify/; skills/define-variables/; skills/version-dataset/; skills/generate-codebook/` | `02_data-processing` | 已映射 |  |
| `03-lit-search` | `03-research/lit-search/` | `skills/search-lit/; skills/fulltext-retrieval/; skills/lit-sync/` | `03_research` | 已映射 |  |
| `03-lit-review` | `03-research/lit-review/` | `skills/ma-scout/` | `03_research` | 部分 | scout/meta, not a dedicated review pack |
| `03-lit-cite` | `03-research/lit-cite/` | `skills/manage-refs/; skills/verify-refs/` | `03_research` | 已映射 | 选刊包改接到 05-write-venue |
| `03-design-experiment` | `03-research/design-experiment/` | `skills/design-study/; skills/write-protocol/; skills/fill-protocol/; skills/intake-project/; skills/design-ai-benchmarking/` | `03_research` | 已映射 |  |
| `03-design-grant` | `03-research/design-grant/` | `skills/grant-builder/` | `03_research` | 已映射 | does not replace A Voice A/B |
| `03-frontier-ideate` | `03-research/frontier-ideate/` | `skills/find-cohort-gap/; skills/architecture-zoo/` | `03_research` | 部分 |  |
| `03-frontier-hypothesize` | `03-research/frontier-hypothesize/` | `skills/find-cohort-gap/; skills/ma-scout/` | `03_research` | 部分 | no hypogenic equivalent |
| `04-stats-guide` | `04-analysis/stats-guide/` | `skills/analyze-stats/` | `04_analysis` | 已映射 | does not replace A 04 personal / 0RAD |
| `04-stats-power` | `04-analysis/stats-power/` | `skills/calc-sample-size/` | `04_analysis` | 已映射 |  |
| `04-stats-models` | `04-analysis/stats-models/` | `skills/model-evaluation/; skills/model-validation/; skills/meta-analysis/` | `04_analysis` | 已映射 |  |
| `04-figure-engine` | `04-analysis/figure-engine/` | `skills/make-figures/` | `04_analysis` | 已映射 | POLE/STROBE gold still B/A |
| `04-explainability` | — | `skills/explainability/` | `04_analysis` | 已映射 | imaging XAI; not in B |
| `05-write-manuscript` | `05-manuscript/write-manuscript/` | `skills/write-paper/; skills/polish-language/; skills/present-paper/` | `05_manuscript` | 已映射 | not Aitor-format |
| `05-write-venue` | `05-manuscript/write-venue/` | `skills/check-reporting/; skills/find-journal/; skills/add-journal/` | `05_manuscript` | 已映射 | reporting + journal find; not Aitor-format |
| `05-humanize` | — | `skills/humanize/` | `05_manuscript` | 已映射 | does not replace A personal de-AI |
| `06-review-peer` | `06-review/review-peer/` | `skills/peer-review/; skills/review-paper/` | `06_review` | 已映射 |  |
| `06-review-critique` | `06-review/review-critique/` | `skills/self-review/; skills/revise/` | `06_review` | 已映射 |  |

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
