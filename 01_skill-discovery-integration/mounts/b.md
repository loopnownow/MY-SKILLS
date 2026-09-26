# 预设 B · 当前默认（v4）

[总览](README.md) · [迁移](MIGRATION_v3_to_v4.md) · [B · 当前默认](b.md)

仅用 B 作为默认来源。[loopnownow/MY-SKILLS-capabilities](https://github.com/loopnownow/MY-SKILLS-capabilities) · `../sources/b-my-skills-capabilities.yaml`

| | |
|---|---|
| 状态 | MOUNTED（默认来源） |
| 结构 | 10 粗 ID 桶；细 ID 为挂载点 |
| 新增挂载 | `intake-project` · `design-ai-benchmarking` · `architecture-zoo` · `fill-protocol` |
| 跨包 stub | `cross-pack/{{scientific,aipoch,nature}}/`（非默认挂载） |
| 空挂 | 对 B-default 细 ID：无空挂（说默认挂载 B 包/本仓） |

## B-default / 新增挂载细 ID

| Fine id | Label | B path | Coarse |
|---|---|---|---|
| `find-cohort-gap` | 队列选题空白发现 | `03-research/frontier-ideate/` | 选题探索 |
| `ma-scout` | MA选题可行性 | `03-research/lit-review/` | 选题探索 |
| `lit-search` | 文献检索与公开数据集 | `03-research/lit-search/` | 文献检索 |
| `frontier-hypothesize` | 假设形成 | `03-research/frontier-hypothesize/` | 选题探索 |
| `intake-project` | 项目启动分类 | `03-research/intake-project/` | 选题探索 |
| `design-study` | 研究设计审查 | `03-research/design-experiment/` | 研究设计 |
| `design-ai-benchmarking` | AI专家评估设计 | `03-research/design-ai-benchmarking/` | 研究设计 |
| `architecture-zoo` | 模型架构选型 | `03-research/architecture-zoo/` | 研究设计 |
| `write-protocol` | IRB方案撰写 | `03-research/design-protocol/` | 研究设计 |
| `fill-protocol` | IRB方案填表 | `03-research/fill-protocol/` | 研究设计 |
| `write-paper` | IMRAD正文起草 | `05-manuscript/write-manuscript/` | 正文写作 |
| `check-reporting` | 报告规范核验 | `05-manuscript/write-reporting/` | 正文写作 |
| `grant-builder` | 基金标书-方法论 | `03-research/design-grant/` | 正文写作 |
| `find-journal` | 选刊推荐 | `05-manuscript/write-venue/` | 正文写作 |
| `polish-language` | 一致性硬规则lint | `05-manuscript/write-polish/` | 语言润色 |
| `clean-data` | 三阶段确认式清洗 | `02-data-processing/tables/` | 数据处理 |
| `batch-cohort` | 批量队列分析生成 | `02-data-processing/tables/` | 数据处理 |
| `imaging-io` | CT/MRI DICOM与NIfTI读写 | `02-data-processing/imaging-io/` | 数据处理 |
| `preprocess-imaging` | ROI与读者质控 | `02-data-processing/imaging-qc/` | 数据处理 |
| `analyze-stats` | 检验方法选择与加权调查数据 | `04-analysis/stats-guide/` | 统计分析 |
| `meta-analysis` | Meta分析抗数据操纵 | `04-analysis/stats-models/` | 统计分析 |
| `radiomics-ml` | 放射组学建模pipeline审计 | `02-data-processing/radiomics-habitat/` | 统计分析 |
| `model-evaluation` | 模型-任务正确指标选择 | `04-analysis/model-eval/` | 统计分析 |
| `model-validation` | 模型-确定性泄漏门禁 | `04-analysis/model-eval/` | 统计分析 |
| `calc-sample-size` | 样本量计算 | `04-analysis/stats-power/` | 统计分析 |
| `make-figures` | 患者流程图 | `04-analysis/fig-flow/` | 图表呈现 |
| `fig-plot` | 统计图与影像面板 | `04-analysis/fig-plot/` | 图表呈现 |
| `peer-review-pdf-scan` | PDF注入攻击扫描 | `06-review/review-peer/` | 稿件评阅 |
| `peer-review` | 审稿意见生成 | `06-review/review-peer/` | 稿件评阅 |
| `self-review` | 数值级自审核算 | `06-review/review-critique/` | 稿件评阅 |
| `revise` | 修回分诊与数字血统追踪 | `06-review/review-response/` | 审稿回复 |

## 非 B 但默认菜单可见

| Fine id | Source | Notes |
|---|---|---|
| `humanize` | MedSci | 去 AI 味（通用）；个人 de-AI 仍在 A |

ARCHIVED 旧接口 `04-explainability` 已移出默认菜单（见迁移图）。

机器真源 `../registry.yaml`。
