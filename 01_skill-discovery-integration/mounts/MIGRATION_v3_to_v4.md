# MIGRATION v3.30 → v4 (CHG-20260913-001)

Option B accepted: **10 coarse stage buckets + 52 fine IDs (hybrid mount)**.
A package folders stay `00_orchestrator` … `06_review` (+ `skill-harvest`). Chinese names are **coarse/fine IDs in the registry**, not A top-level renames.

## Specialist domain map (unchanged A hooks)

| Specialist | A domains | v4 coarse buckets |
|---|---|---|
| Victor | `03_research` (+ 选刊 `medical-journal-submit`) | 文献检索 · 选题探索 · 研究设计 |
| Loopnow / Aitee | `02_data-processing` · `04_analysis` | 数据处理 · 统计分析 · 图表呈现 |
| Lee | `05_manuscript` · `06_review` | 正文写作 · 语言润色 · 稿件评阅 · 审稿回复 |

选刊 stays Victor / `03_research/medical-journal-submit`. Do not move into 05.

## Old 30 coarse ids → new fine ids

| Old id | New fine id(s) | Coarse | Notes |
|---|---|---|---|
| `02-tables` | clean-data, batch-cohort | 数据处理 | MOUNTED via tables/ |
| `02-imaging-io` | imaging-io | 数据处理 | MOUNTED; pydicom stays PROPOSED for tag-level anonymization |
| `02-imaging-qc` | preprocess-imaging | 数据处理 | MOUNTED; profile-imaging and uncertainty-imaging archived |
| `02-pictures` | — | ARCHIVED | see archived 02-pictures |
| `02-fmri` | — | ARCHIVED | see archived 02-fmri |
| `02-radiomics-habitat` | radiomics-ml | 统计分析 | MOUNTED (a_domain 04) |
| `03-lit-search` | paper-lookup (PROPOSED Scientific); verify-refs/manage-refs/lit-sync cover cite side | 文献检索 | breadth → paper-lookup |
| `03-lit-fulltext` | — | ARCHIVED | archived 03-lit-fulltext |
| `03-lit-review` | ma-scout (选题探索); full review flow ARCHIVED | 选题探索 / ARCHIVED | partial |
| `03-lit-cite` | verify-refs, manage-refs, lit-sync, retraction-watcher | 文献检索 | MOUNTED + PROPOSED |
| `03-design-experiment` | design-study, design-ai-benchmarking, architecture-zoo | 研究设计 | wetlab DOE archived |
| `03-design-protocol` | write-protocol, fill-protocol, clinic-research-design | 研究设计 |  |
| `03-design-grant` | grant-builder; nature-proposal-writer PROPOSED | 正文写作 | grant under 正文写作 coarse |
| `03-frontier-ideate` | find-cohort-gap, intake-project | 选题探索 |  |
| `03-frontier-hypothesize` | frontier-hypothesize | 选题探索 | MOUNTED; hypothesis-generation archived |
| `04-stats-guide` | analyze-stats | 统计分析 |  |
| `04-stats-power` | calc-sample-size (coarse 研究设计); statistical-power PROPOSED | 研究设计 | open decision default 研究设计 |
| `04-stats-models` | meta-analysis, scikit-survival | 统计分析 |  |
| `04-model-eval` | model-evaluation, model-validation | 统计分析 |  |
| `04-fig-flow` | make-figures | 图表呈现 | MOUNTED; label 患者流程图 |
| `04-fig-plot` | fig-plot | 图表呈现 | MOUNTED |
| `04-explainability` | — | ARCHIVED | archived |
| `05-write-manuscript` | write-paper | 正文写作 |  |
| `05-write-reporting` | check-reporting; nature-data PROPOSED | 正文写作 |  |
| `05-write-venue` | find-journal (选刊 engine); venue-templates PROPOSED; 选刊 A stays 03 | 正文写作 | NOT move journal-selection to 05 |
| `05-write-polish` | polish-language; nature-polishing PROPOSED | 语言润色 |  |
| `05-humanize` | humanize | 语言润色 | still MedSci source |
| `06-review-peer` | peer-review-pdf-scan, peer-review | 稿件评阅 |  |
| `06-review-critique` | self-review; scientific-critical-thinking PROPOSED | 稿件评阅 |  |
| `06-review-response` | revise; response-tone-polisher PROPOSED | 审稿回复 |  |

## Archived / DISABLED (removed from default session menus)

| Id | Reason | Revive |
|---|---|---|
| `02-fmri` | 假匹配已核实——AIPOCH neuropixels≠fMRI | 研究方向扩展至fMRI/电生理时重评 |
| `02-pictures` | 场景错位——病理全切片非通用图片 | 数字病理时重评 histolab/pathml |
| `03-design-experiment-wetlab` | 仅归档外部湿实验室DOE；MedSci design-study等已入研究设计 | 前瞻性/湿实验需求时评估外部DOE |
| `04-explainability` | 用户不使用；Grad-CAM vs SHAP不可互替 | 可解释性论文时复活 |
| `03-lit-fulltext` | 用户不使用批量全文 | 需批量PDF尤其中文核心时复活 |
| `03-lit-review-full` | 不写综述全流程；ma-scout保留在选题探索 | 系统综述委托时复活 |
| `deidentify` | 导出已人工脱敏 | 非脱敏实时院内系统时复活 |
| `05-write-venue-add-journal` | add-journal是维护工具非产出技能 | 不适用 |

## Session pick protocol change

- **Before:** ask which of 30 coarse ids to mount.
- **After:** classify task → propose relevant **coarse bucket(s)** → multi-select **fine ids** under those buckets.
- Registry `MOUNTED` / `PROPOSED` = available to pick, not attached this run.
- Never auto-mount non-B. Nature stays PROPOSED until license verified. OpenClaw never atomic source.
- Empty mount → notify → research → confirm. Say 默认挂载 B 包/本仓 not 空挂.

## Open decision

样本量 (`calc-sample-size` / `statistical-power`) defaulted to coarse **研究设计** (B path still `04-analysis/stats-power/`). Alternative: 统计分析.

## Files

- Backup: `../_history/registry.v3.30.yaml`
- Live: `../registry.yaml`
