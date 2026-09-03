# 预设 Scientific · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 Scientific Agent Skills（2026-09-02 HEAD，v2.66.0）。仓库 [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 配置 `../sources/scientific-agent-skills.proposed.yaml`

粗 ID 按本库的活重分（CHG-20260903-008）。

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 19 / 22（若干部分） |
| 空挂 | 3 |
| 扫描 | 2026-09-03 · `1e5eeff` |
| 许可 | MIT |

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-tables` | `skills/xlsx/; skills/polars/; skills/exploratory-data-analysis/` | `02_data-processing` | 临床表 Excel / CSV | 已映射 | Excel / DataFrame |
| `02-imaging` | `skills/pydicom/; skills/bids/; skills/imaging-data-commons/` | `02_data-processing` | CT/MRI · DICOM / NIfTI / NII | 部分 | not 0RAD QC; not fMRI |
| `02-pictures` | `skills/histolab/; skills/pathml/; skills/pdf/` | `02_data-processing` | 图片 TIFF / PNG / JPG / PDF(图) | 部分 | WSI + PDF-as-image |
| `02-fmri` | — | `02_data-processing` | fMRI · DICOM / NIfTI | 空挂 | 无对应包 |
| `02-radiomics-habitat` | — | `02_data-processing` | radiomics / 生境准备（建模交 04） | 空挂 | 无对应包 |
| `03-lit-search` | `skills/paper-lookup/; skills/research-lookup/` | `03_research` | 文献检索 / 全文 | 已映射 |  |
| `03-lit-review` | `skills/literature-review/` | `03_research` | 综述 / 综合 | 已映射 |  |
| `03-lit-cite` | `skills/citation-management/; skills/pyzotero/` | `03_research` | 引文库 / Zotero | 已映射 |  |
| `03-design-experiment` | `skills/experimental-design/` | `03_research` | 采集前实验设计 | 已映射 | pre-data collection design |
| `03-design-grant` | `skills/research-grants/` | `03_research` | 标书（通用）；个人 Voice A/B 优先 | 已映射 | does not replace A Voice A/B |
| `03-frontier-ideate` | `skills/scientific-brainstorming/` | `03_research` | 选题 / 头脑风暴 | 已映射 |  |
| `03-frontier-hypothesize` | `skills/hypothesis-generation/; skills/hypogenic/` | `03_research` | 问题化 / 假说 | 已映射 | hypogenic is secondary (ChicagoHAI) |
| `04-stats-guide` | `skills/statistical-analysis/` | `04_analysis` | 选检验 / 效应量 | 已映射 | does not replace A 04 personal / 0RAD |
| `04-stats-power` | `skills/statistical-power/` | `04_analysis` | 样本量 / 功效 | 已映射 |  |
| `04-stats-models` | `skills/statsmodels/; skills/pymc/; skills/scikit-learn/; skills/scikit-survival/` | `04_analysis` | 统计/ML 实现层 | 已映射 |  |
| `04-figure-engine` | `skills/scientific-visualization/; skills/matplotlib/; skills/seaborn/; skills/scientific-schematics/` | `04_analysis` | 出图 | 已映射 | POLE/STROBE gold still B/A |
| `04-explainability` | `skills/shap/` | `04_analysis` | 影像模型可解释性 | 部分 | tabular SHAP, not imaging Grad-CAM |
| `05-write-manuscript` | `skills/scientific-writing/; skills/markdown-mermaid-writing/` | `05_manuscript` | 论著/报告草稿 | 已映射 | not Aitor-format; clinical-reports not included |
| `05-write-venue` | `skills/venue-templates/` | `05_manuscript` | 期刊/会议体例 | 已映射 | not Aitor-format |
| `05-humanize` | — | `05_manuscript` | 去 AI 痕迹（通用） | 空挂 | 无对应包 · 个人 de-AI 仍在 A |
| `06-review-peer` | `skills/peer-review/` | `06_review` | 他审草稿 | 已映射 |  |
| `06-review-critique` | `skills/scientific-critical-thinking/; skills/scholar-evaluation/` | `06_review` | 自审 / 证据质量 | 已映射 | grant Voice A stays in 03 personal |

## 仅用当前挂载 · 空挂

**3 个空挂：** `02-fmri` · `02-radiomics-habitat` · `05-humanize`。

若只用本套，这三条先通知再检索确认。个人 de-AI 仍在 A `05_manuscript/personal/`。`clinical-reports/` 不进 05。

## A 没有对应接口

仓库约 163 个 skill，绝大多数是组学、化学、药物、实验室系统和计算底座，不接到 22 个挂载 id。不逐条抄进 A。按领域归组：

| 领域 | 例子（路径均在 `skills/`） | 备注 |
|---|---|---|
| 组学 / 单细胞 | `scanpy/` · `scvi-tools/` · `bulk-rnaseq/` · `biopython/` · `anndata/` | 不是放射学 02/04 |
| 化学 / 药物 | `rdkit/` · `deepchem/` · `medchem/` · `diffdock/` · `molecular-dynamics/` | 不进论文管线 |
| 实验室系统 | `benchling-integration/` · `opentrons-integration/` · `labarchive-integration/` · `omero-integration/` | 集成，不是挂载 id |
| 计算底座 | `dask/` · `modal/` · `pytorch-lightning/` · `transformers/` | 基础设施 |
| 临床流程 | `clinical-decision-support/` · `treatment-plans/` | 不是 02–06 论文管线 |
| 其它学科 | `astropy/` · `pymatgen/` · `qiskit/` · `geopandas/` | 与金山医院放射科研无关 |

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
