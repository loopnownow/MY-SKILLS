# 预设 MedSci · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md)

仅用 MedSci Skills（2026-09-01 HEAD）。仓库 [Aperivue/medsci-skills](https://github.com/Aperivue/medsci-skills) · 配置 `../sources/medsci.proposed.yaml`

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 14 / 14（4 部分） |
| 空挂 | 0 |
| 扫描 | 2026-09-03 · `912f7e8` |

## 挂载来源

| 字段 | 值 |
|---|---|
| 来源 | MedSci Skills |
| 扫描 | 2026-09-03 · `912f7e8` |
| 角色 | 备份 |
| 状态 | PROPOSED |

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-xlsx` | `skills/clean-data/` · `batch-cohort/` · `generate-codebook/` | `02_data-processing` | 表/队列清洗 | 部分 | 不是 Excel/COM 自动化 |
| `02-imaging-qc` | `skills/preprocess-imaging/` · `profile-imaging/` · `uncertainty-imaging/` | `02_data-processing` | 影像预处理与 QC | 已映射 | |
| `02-radiomics-habitat` | `skills/radiomics-ml/` | `02_data-processing` | radiomics（含 ML） | 部分 | 建模仍走 04；生境薄于 B |
| `02-impute` | `skills/clean-data/` | `02_data-processing` | 缺失处理 | 部分 | 夹在清洗里，无独立 impute 包 |
| `02-generic-docs` | `skills/deidentify/` · `define-variables/` · `version-dataset/` · `generate-codebook/` | `02_data-processing` | 去标识 / 变量 / 版本 | 已映射 | |
| `03-literature` | `skills/search-lit/` · `fulltext-retrieval/` · `find-journal/` · `manage-refs/` · `verify-refs/` … | `03_research` | 检索 / 全文 / 选刊 / 核引 | 已映射 | |
| `03-design` | `skills/design-study/` · `write-protocol/` · `intake-project/` · `grant-builder/` … | `03_research` | 设计 / 方案 / 立项 | 已映射 | |
| `03-frontier` | `skills/find-cohort-gap/` · `ma-scout/` · `architecture-zoo/` | `03_research` | 缺口 / scout | 部分 | 不是独立前沿地图 |
| `04-stats-generic` | `skills/analyze-stats/` · `calc-sample-size/` · `meta-analysis/` · `model-evaluation/` | `04_analysis` | 统计 / 样本量 / 模型评价 | 已映射 | 不替换 A 04 personal / 0RAD |
| `04-explainability` | `skills/explainability/` | `04_analysis` | 影像模型可解释性 | 已映射 | A 04 接口；不经 B |
| `04-figure-engine` | `skills/make-figures/` | `04_analysis` | 发表图 | 已映射 | POLE/STROBE 金标准仍在 B/A |
| `05-humanize` | `skills/humanize/` | `05_manuscript` | 去 AI 痕迹（通用） | 已映射 | 不替换 A personal de-AI 禁词表 |
| `05-writing-generic` | `skills/write-paper/` · `polish-language/` · `check-reporting/` · `present-paper/` | `05_manuscript` | 写作 / 报告规范 | 已映射 | 不是 Aitor-format；个人 de-AI 禁词表仍在 A |
| `06-review-generic` | `skills/peer-review/` · `review-paper/` · `self-review/` · `revise/` | `06_review` | 审稿 / 自审 / 改稿 | 已映射 | |

额外不计入 14 id：`orchestrate/` ≈ 00；`sync-submission/` ≈ 投稿（Bai 仍不点同意投稿、不付版面费）。

## 仅用当前挂载 · 空挂

**无空挂。** 14 个 A id 都能指到 MedSci 路径（含 `04-explainability` / `05-humanize`）。其中 `02-xlsx` / `02-radiomics-habitat` / `02-impute` / `03-frontier` 是部分覆盖。部分覆盖不够用时，先通知再检索，不要静默改挂。

## A 没有对应接口

这些 skill 在 MedSci 里存在，但不在 14 个挂载 id 上。分两类：真扩展候选，和 A 已有层/人但没有挂载接口。

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
