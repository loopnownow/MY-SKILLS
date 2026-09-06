# 预设 OpenClaw · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md) · [OpenClaw · 备份](openclaw.md) · [AIPOCH · 备份](aipoch.md)

仅用 OpenClaw Medical Skills（2026-07-21 HEAD）。仓库 [FreedomIntelligence/OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) · 配置 `../sources/openclaw-medical-skills.proposed.yaml`

粗 ID 细拆（CHG-20260903-011）。共 30 个 A id。

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 23 / 30（若干部分） |
| 空挂 | 7 |
| 扫描 | 2026-09-06 · `b1f9b6e` |
| 许可 | README 标 MIT；根目录扫描时无 LICENSE 文件 |

**分组叙事（非粗 ID）：** ChatGPT 建议的 LITERATURE / BIOMEDICAL-DATABASE / MEDICAL-IMAGING / CLINICAL-RESEARCH / STATISTICS / SCIENTIFIC-REASONING / PEER-REVIEW 七组，以及 `ocms-*` Mount ID，**只作说明**。机器真源仍是本表 30 个 A id。不单独开 OpenClaw writing 挂载点（写作链仍是 ARS/MedSci/Scientific → A05 → B05）。

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-tables` | `skills/xlsx/; skills/polars/; skills/exploratory-data-analysis/` | `02_data-processing` | 临床表 Excel / CSV（含缺失/异常值） | 已映射 | Excel / DataFrame |
| `02-imaging-io` | `skills/pydicom/; skills/imaging-data-commons/; skills/multimodal-medical-imaging/` | `02_data-processing` | CT/MRI 读写 · DICOM / 多模态影像 | 部分 | no bids; not 0RAD; not fMRI |
| `02-imaging-qc` | — | `02_data-processing` | CT/MRI QC · ROI / 阅片 | 空挂 | 无 ROI/阅片包 |
| `02-pictures` | `skills/histolab/; skills/pathml/; skills/pdf/; skills/tooluniverse-image-analysis/` | `02_data-processing` | 图片 TIFF / PNG / JPG / PDF(图) / 图像分析 | 部分 | WSI + PDF-as-image |
| `02-fmri` | — | `02_data-processing` | fMRI · DICOM / NIfTI | 空挂 | 无对应包 |
| `02-radiomics-habitat` | `skills/radiomics-pathomics-fusion-agent/` | `02_data-processing` | radiomics / 生境准备（建模交 04） | 部分 | agent pack |
| `03-lit-search` | `skills/pubmed-search/; skills/biomedical-search/; skills/research-lookup/; skills/medical-research-toolkit/; skills/clinicaltrials-database/; skills/tooluniverse-literature-deep-research/; skills/search-strategy/; skills/research-literature/` | `03_research` | 文献 / 试验 / 生物医学库检索 | 已映射 | 日常 OCMS 文献栈 |
| `03-lit-fulltext` | — | `03_research` | 全文获取 | 空挂 | 无独立全文包 |
| `03-lit-review` | `skills/literature-review/; skills/medical-imaging-review/` | `03_research` | 综述 / 综合 | 已映射 | imaging review 次要 |
| `03-lit-cite` | `skills/citation-management/; skills/pyzotero/` | `03_research` | DOI→BibTeX | 已映射 |  |
| `03-design-experiment` | `skills/bio-experimental-design-batch-design/; skills/bio-experimental-design-multiple-testing/` | `03_research` | 采集前实验设计 | 部分 | no experimental-design/ |
| `03-design-protocol` | `skills/clinical-trial-protocol-skill/` | `03_research` | 写方案 / 填方案 | 已映射 | 补 Scientific 空挂 |
| `03-design-grant` | `skills/research-grants/` | `03_research` | 标书（通用槽）；个人 Voice A/B 优先 | 已映射 | 不单开 writing 挂载 |
| `03-frontier-ideate` | `skills/scientific-brainstorming/; skills/scientific-problem-selection/` | `03_research` | 选题 / 头脑风暴 | 已映射 |  |
| `03-frontier-hypothesize` | `skills/hypothesis-generation/; skills/hypogenic/` | `03_research` | 问题化 / 假说 | 已映射 | hypogenic secondary |
| `04-stats-guide` | `skills/statistical-analysis/` | `04_analysis` | 选检验 / 效应量 | 已映射 | does not replace A 04 personal / 0RAD |
| `04-stats-power` | `skills/bio-experimental-design-power-analysis/; skills/bio-experimental-design-sample-size/` | `04_analysis` | 样本量 / 功效 | 部分 | no statistical-power/ |
| `04-stats-models` | `skills/statsmodels/; skills/pymc/; skills/scikit-learn/; skills/scikit-survival/; skills/tooluniverse-statistical-modeling/` | `04_analysis` | 统计/ML 拟合 | 已映射 | 0RAD personal still wins |
| `04-model-eval` | `skills/bio-machine-learning-model-validation/` | `04_analysis` | 校准 / 验证 | 部分 | omics-leaning; not DCA/外验证 gold |
| `04-fig-flow` | `skills/scientific-schematics/` | `04_analysis` | STROBE / 入组流程图 | 部分 | schematics, not STROBE gold |
| `04-fig-plot` | `skills/scientific-visualization/; skills/matplotlib/; skills/seaborn/` | `04_analysis` | 统计图 / 影像拼图 | 已映射 | POLE gold still B/A |
| `04-explainability` | `skills/shap/` | `04_analysis` | 影像模型可解释性 | 部分 | tabular SHAP; MedSci 仍优先 |
| `05-write-manuscript` | `skills/scientific-writing/; skills/markdown-mermaid-writing/; skills/scientific-manuscript/` | `05_manuscript` | 论著/报告草稿 | 已映射 | not Aitor-format; clinical-reports 不进 |
| `05-write-reporting` | — | `05_manuscript` | TRIPOD / CLAIM / 报告规范 | 空挂 | 无独立报告规范包 |
| `05-write-venue` | — | `05_manuscript` | 期刊体例 / house style（not 选刊） | 空挂 | 无 venue-templates |
| `05-write-polish` | `skills/scientific-writing/` | `05_manuscript` | 通用学术英语润色 | 部分 | same pack; not de-AI |
| `05-humanize` | — | `05_manuscript` | 去 AI 痕迹（通用） | 空挂 | 个人 de-AI 仍在 A |
| `06-review-peer` | `skills/peer-review/` | `06_review` | 他审草稿 | 已映射 |  |
| `06-review-critique` | `skills/scientific-critical-thinking/` | `06_review` | 自审 / 投稿前找洞 | 已映射 | 无 scholar-evaluation |
| `06-review-response` | — | `06_review` | 回复审稿人 | 空挂 | 无独立回信包 |

## 仅用当前挂载 · 空挂

**7 个空挂：** `02-imaging-qc` · `02-fmri` · `03-lit-fulltext` · `05-write-reporting` · `05-write-venue` · `05-humanize` · `06-review-response`。

若只用本套，这些先通知再检索确认。个人 de-AI 仍在 A `05_manuscript/personal/`。`clinical-reports/` 不进 05。批注前缀用 `[OpenClaw:…]`。

## A 没有对应接口

仓库约 869 个 skill，绝大多数是组学、药物、实验室系统和计算底座，不接到 30 个挂载 id。不逐条抄进 A。按领域归组：

| 领域 | 例子（路径均在 `skills/`） | 备注 |
|---|---|---|
| 组学 / 单细胞 | `scanpy/` · `scvi-tools/` · `anndata/` · `bio-de-deseq2-basics/` | 不是放射学 02/04 |
| 化学 / 药物 | `rdkit/` · `deepchem/` · `torchdrug/` · `tooluniverse-drug-research/` | 不进论文管线 |
| 实验室系统 | `benchling-integration/` · `opentrons-integration/` · `protocolsio-integration/` | 集成，不是挂载 id |
| 计算底座 | `pytorch-lightning/` · `transformers/` · `slurm-job-script-generator/` | 基础设施 |
| 临床流程 / 文书 | `clinical-decision-support/` · `treatment-plans/` · `clinical-reports/` | 不是 02–06 论文管线 |
| 消费健康 | `adhd-daily-planner/` · `sleep-analyzer/` · `weightloss-analyzer/` | 与金山医院放射科研无关 |
| 其它 | `alphafold/` · `spatial-transcriptomics-agent/` · `usmle/` | 宽生物 / 教考包 |

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
