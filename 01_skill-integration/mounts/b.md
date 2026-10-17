# 预设 B · 当前默认（v4）

[总览](README.md) · [B · 当前默认](b.md)

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
| `lit-search` | 文献检索与公开数据集 | `03-research/lit-search/` | lit-retrieval |
| `design-study` | 研究设计审查（含原 architecture-zoo / design-ai-benchmarking / frontier-hypothesize / find-cohort-gap / intake-project） | `03-research/design-experiment/` | study-design |
| `write-protocol` | IRB方案撰写 | `03-research/design-protocol/` | study-design |
| `fill-protocol` | IRB方案填表 | `03-research/fill-protocol/` | study-design |
| `write-paper` | IMRAD正文起草 | `05-manuscript/write-manuscript/` | manuscript-body |
| `check-reporting` | 报告规范核验 | `05-manuscript/write-reporting/` | manuscript-body |
| `grant-builder` | 基金标书-方法论 | `03-research/design-grant/` | manuscript-body |
| `find-journal` | 选刊推荐 | `05-manuscript/write-venue/` | manuscript-body |
| `polish-language` | 一致性硬规则lint | `05-manuscript/write-polish/` | language-polish |
| `clean-data` | 三阶段确认式清洗 | `02-data-processing/tables/` | data-processing |
| `batch-cohort` | 批量队列分析生成 | `02-data-processing/tables/` | data-processing |
| `imaging-io` | CT/MRI DICOM与NIfTI读写 | `02-data-processing/imaging-io/` | data-processing |
| `preprocess-imaging` | ROI与读者质控 | `02-data-processing/imaging-qc/` | data-processing |
| `analyze-stats` | 检验方法选择与加权调查数据（含原 radiomics-ml 路由） | `04-analysis/stats-guide/` | stats-analysis |
| `meta-analysis` | Meta分析抗数据操纵（含原 scout-meta-analysis） | `04-analysis/stats-models/` | stats-analysis |
| `model-evaluation` | 模型-任务正确指标选择 | `04-analysis/model-eval/` | stats-analysis |
| `model-validation` | 模型-确定性泄漏门禁 | `04-analysis/model-eval/` | stats-analysis |
| `calc-sample-size` | 样本量计算 | `04-analysis/stats-power/` | stats-analysis |
| `draw-flowchart` | 患者流程图 | `04-analysis/fig-flow/` | figures |
| `plot-figures` | 统计图与影像面板（含原 audit-figure-risk / scientific-visualization 原则） | `04-analysis/fig-plot/` | figures |
| `peer-review` | 审稿意见生成（含原 peer-review-pdf-scan） | `06-review/review-peer/` | manuscript-review |
| `self-review` | 数值级自审核算 | `06-review/review-critique/` | manuscript-review |
| `revise` | 修回分诊与数字血统追踪 | `06-review/review-response/` | review-response |
| `humanize` | 去AI味 | `05-manuscript/humanize/` | language-polish |
| `retraction-watcher` | 撤稿检测 | `03-research/retraction-watcher/` | lit-retrieval |
| `response-tone-polisher` | 回复语气软化 | `06-review/response-tone-polisher/` | review-response |

## 非 B 但默认菜单可见

（2026-10-17）`humanize` / `retraction-watcher` / `response-tone-polisher` 已吸收进 B 上表；个人 de-AI 仍在 A `05_manuscript/personal/`。

机器真源 `../registry.yaml`。
