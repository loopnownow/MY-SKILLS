# 预设 Scientific · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md)

仅用 Scientific Agent Skills（2026-09-02 HEAD，v2.66.0，约 163 个 skill）。仓库 [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) · 配置 `../sources/scientific-agent-skills.proposed.yaml`

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 12 / 14（5 部分） |
| 空挂 | 2 |
| 扫描 | 2026-09-03 · `1e5eeff` |
| 许可 | MIT |

## 挂载来源

| 字段 | 值 |
|---|---|
| 来源 | Scientific Agent Skills |
| 扫描 | 2026-09-03 · `1e5eeff` |
| 角色 | 备份 |
| 状态 | PROPOSED |

## 可挂 skills 接到哪一环

| A id | 来源路径 | 接到 A | 做什么 | 覆盖 | 说明 |
|---|---|---|---|---|---|
| `02-xlsx` | `skills/xlsx/` | `02_data-processing` | Excel 工作簿 | 已映射 | 比 MedSci 更接近 Excel 本体 |
| `02-imaging-qc` | `skills/pydicom/` · `histolab/` · `pathml/` · `bids/` · `imaging-data-commons/` | `02_data-processing` | DICOM / 病理切片 / BIDS | 部分 | 不是 0RAD 影像 QC |
| `02-radiomics-habitat` | — | `02_data-processing` | radiomics / 生境准备 | 空挂 | 无对应包 |
| `02-impute` | `skills/exploratory-data-analysis/` · `polars/` | `02_data-processing` | 表探查 / DataFrame | 部分 | 不是独立 impute 包 |
| `02-generic-docs` | `skills/markitdown/` · `pdf/` · `docx/` | `02_data-processing` | 文档转写 | 部分 | 不是影像数据说明 |
| `03-literature` | `skills/literature-review/` · `paper-lookup/` · `citation-management/` · `pyzotero/` · `research-lookup/` | `03_research` | 文献 / 检索 / 引文 | 已映射 | 文献只走 03 |
| `03-design` | `skills/experimental-design/` · `hypothesis-generation/` · `research-grants/` · `scientific-brainstorming/` | `03_research` | 实验设计 / 假说 / 标书 | 已映射 | 不是放射学专项设计 |
| `03-frontier` | `skills/scientific-brainstorming/` · `hypothesis-generation/` · `hypogenic/` | `03_research` | 选题 / 假说 | 部分 | 不是独立前沿地图 |
| `04-stats-generic` | `skills/statistical-analysis/` · `statistical-power/` · `statsmodels/` · `pymc/` · `scikit-learn/` · `scikit-survival/` | `04_analysis` | 统计 / 功效 / 生存 | 已映射 | 不替换 A 04 personal / 0RAD |
| `04-explainability` | `skills/shap/` | `04_analysis` | 表格模型 SHAP | 部分 | 不是影像 Grad-CAM |
| `04-figure-engine` | `skills/scientific-visualization/` · `matplotlib/` · `seaborn/` · `scientific-schematics/` | `04_analysis` | 科学作图 | 已映射 | POLE/STROBE 金标准仍在 B/A |
| `05-writing-generic` | `skills/scientific-writing/` · `venue-templates/` · `markdown-mermaid-writing/` · `clinical-reports/` | `05_manuscript` | 写作 / 期刊体例 | 已映射 | 不是 Aitor-format |
| `05-humanize` | — | `05_manuscript` | 去 AI 痕迹（通用） | 空挂 | 无对应包 · 个人 de-AI 仍在 A |
| `06-review-generic` | `skills/peer-review/` · `scholar-evaluation/` · `scientific-critical-thinking/` | `06_review` | 审稿 / 评议 | 已映射 | 个人审稿声音仍在 A |

## 仅用当前挂载 · 空挂

**2 个空挂：** `02-radiomics-habitat` · `05-humanize`。

若只用本套，这两条先通知再检索确认，不要静默改挂。其余 12 个可按上表路径用。个人 de-AI 仍在 A `05_manuscript/personal/`。

## A 没有对应接口

仓库约 163 个 skill，绝大多数是组学、化学、药物、实验室系统和计算底座，不接到 14 个挂载 id。不逐条抄进 A。按领域归组：

| 领域 | 例子（路径均在 `skills/`） | 备注 |
|---|---|---|
| 组学 / 单细胞 | `scanpy/` · `scvi-tools/` · `bulk-rnaseq/` · `biopython/` · `anndata/` | 不是放射学 02/04 |
| 化学 / 药物 | `rdkit/` · `deepchem/` · `medchem/` · `diffdock/` · `molecular-dynamics/` | 不进论文管线 |
| 实验室系统 | `benchling-integration/` · `opentrons-integration/` · `labarchive-integration/` · `omero-integration/` | 集成，不是挂载 id |
| 计算底座 | `dask/` · `modal/` · `pytorch-lightning/` · `transformers/` | 基础设施 |
| 临床流程 | `clinical-decision-support/` · `treatment-plans/` | 不是 02–06 论文管线 |
| 其它学科 | `astropy/` · `pymatgen/` · `qiskit/` · `geopandas/` | 与金山医院放射科研无关 |

机器真源 `../registry.yaml` · 来源配置 `../sources/*.yaml`。空挂 = 仅用本套时该 A id 在来源里没有对应路径。映射扫自公开 GitHub，不是静默改挂。
