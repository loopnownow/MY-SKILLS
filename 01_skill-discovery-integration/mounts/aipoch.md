# 预设 AIPOCH · 备份

[总览](README.md) · [B · 当前默认](b.md) · [ARS · 备份](ars.md) · [MedSci · 备份](medsci.md) · [Scientific · 备份](scientific.md) · [OpenClaw · 备份](openclaw.md) · [AIPOCH · 备份](aipoch.md) · [Nature · 备份](nature.md)

仅用 AIPOCH Medical Research Skills（钉 `f5ef65b`）。仓库 [aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills) · 配置 `../sources/aipoch-medical-research-skills.proposed.yaml`

粗 ID 细拆（CHG-20260903-011）。共 30 个 A id。

| | |
|---|---|
| 状态 | PROPOSED（备份候选；映射已写好，仍未改挂） |
| 已映射 | 25 / 30 |
| 空挂 | 5：`02-imaging-qc` · `02-radiomics-habitat` · `05-humanize` · `05-write-reporting` · `06-review-critique` |
| 扫描 | 2026-09-06 · `f5ef65b` |
| 许可 | MIT（根目录 LICENSE） |
| 索引树 | `scientific-skills/`（本扫 463 个 SKILL.md）；`awesome-med-research-skills/` 为精选子集 |

**分组叙事（非粗 ID）：** ChatGPT 建议的 A01–A08（Evidence Retrieval / Verification / Study Design / Stats / Omics / Imaging / Manuscript / Peer Review）以及 `aipoch-*` Mount ID，**只作说明**。机器真源仍是本表 30 个 A id。不单独开 AIPOCH writing 挂载点；写作/回审包只当 worker，权威在 Aitee/Lee。

## 可挂 skills 接到哪一环

| A id | 来源路径（scientific-skills/…） | 接到 A | 覆盖 | 说明 |
|---|---|---|---|---|
| `02-tables` | `Data Analysis/baseline-extraction-for-clinical-trials/; Data Analysis/clinical-data-cleaner/; Data Analysis/data-transform/ (+4)` | `02_data-processing` | 已映射 | EDA / clean / impute helpers; not HIS |
| `02-imaging-io` | `Data Analysis/pydicom/; Other/dicom-anonymizer/` | `02_data-processing` | 部分 | thin; not 0RAD gold |
| `02-imaging-qc` | `—` | `02_data-processing` | 空挂 | 空挂 |
| `02-pictures` | `Data Analysis/facs-gating-viz-style/; Data Analysis/flowio/; Data Analysis/histolab/ (+2)` | `02_data-processing` | 已映射 | pathology / flow-ish; not radiomics habitat |
| `02-fmri` | `Data Analysis/neuropixels-analysis/` | `02_data-processing` | 部分 | neuropixels-leaning if present; not radiology pipeline |
| `02-radiomics-habitat` | `—` | `02_data-processing` | 空挂 | 空挂 |
| `03-lit-search` | `Evidence Insight/arxiv-database/; Evidence Insight/biopython-entrez/; Evidence Insight/biorxiv-database/ (+19)` | `03_research` | 已映射 | high-value for Victor / Evidence Request |
| `03-lit-fulltext` | `Evidence Insight/research-paper-downloader/; Data Analysis/meta-screening-fulltext/; Other/fulltext-fetcher/` | `03_research` | 部分 | few OA downloaders; empty-ish risk |
| `03-lit-review` | `Evidence Insight/clinical-study-info-extractor/; Evidence Insight/patent-landscape/; Evidence Insight/research-hotspot-analysis/ (+4)` | `03_research` | 已映射 | gap / landscape / screener — prefer over writing packs |
| `03-lit-cite` | `Evidence Insight/citation-chasing-mapping/; Evidence Insight/citation-management/; Evidence Insight/citation-network/ (+7)` | `03_research` | 已映射 | citation integrity / formatters |
| `03-design-experiment` | `Protocol Design/experiment-design/; Protocol Design/inclusion-criteria-gen/; Protocol Design/randomization-gen/` | `03_research` | 部分 | thin vs protocol planners |
| `03-design-protocol` | `Evidence Insight/tooluniverse-clinical-trial-matching/; Protocol Design/INPLASY-registration-helper/; Protocol Design/adaptive-trial-simulator/ (+18)` | `03_research` | 已映射 | many disease-specific planners — selective use only |
| `03-design-grant` | `Evidence Insight/funding-trend-forecaster/; Evidence Insight/grant-funding-scout/; Evidence Insight/grant-gantt-chart-gen/ (+6)` | `03_research` | 已映射 | NIH-style helpers; Voice A/B still A personal |
| `03-frontier-ideate` | `Evidence Insight/cross-disciplinary-bridge-finder/; Evidence Insight/emerging-topic-scout/; Other/brainstorming/` | `03_research` | 部分 | gap / novelty helpers |
| `03-frontier-hypothesize` | `Protocol Design/hypogenic/; Protocol Design/hypothesis-generation/` | `03_research` | 部分 | hypogenic / hypothesis packs |
| `04-stats-guide` | `Evidence Insight/diagnostic-study-quality-assessment-quadas-2/; Evidence Insight/rct-bias-assessment-rob2/; Data Analysis/data-stats-analysis/ (+9)` | `04_analysis` | 已映射 | appraisal scales; does not replace 0RAD personal |
| `04-stats-power` | `Protocol Design/sample-size-basic/; Academic Writing/sample-size-power-calculator/; Other/clinic-sample-size/` | `04_analysis` | 部分 | sample-size helpers; 04-stats-power gold still B/A |
| `04-stats-models` | `Data Analysis/epidemiology/; Data Analysis/meta-analysis/; Data Analysis/scikit-survival/ (+3)` | `04_analysis` | 已映射 | ML / survival utilities; 0RAD personal wins |
| `04-model-eval` | `Data Analysis/forest-plot-styler/; Data Analysis/meta-funnel-plot/; Academic Writing/meta-results-forest-plot-analyzer/ (+3)` | `04_analysis` | 已映射 | ROC/DCA/nomogram workers; lab VAL_MODE/HL still A |
| `04-fig-flow` | `Data Analysis/mechanism-flowchart/` | `04_analysis` | 部分 | weak; STROBE gold stays B/A POLE |
| `04-fig-plot` | `Data Analysis/circos-plot-generator/; Data Analysis/cnv-caller-plotter/; Data Analysis/heatmap-beautifier/ (+15)` | `04_analysis` | 已映射 | many viz helpers; POLE gold still B/A |
| `04-explainability` | `Data Analysis/shap/` | `04_analysis` | 部分 | thin SHAP-like; MedSci preferred for explainability |
| `05-write-manuscript` | `Evidence Insight/pathway-introduction-expert/; Evidence Insight/phenotype-introduction/; Data Analysis/graphical-abstract-wizard/ (+10)` | `05_manuscript` | 已映射 | worker only — Aitee 05 personal owns authority |
| `05-write-reporting` | `—` | `05_manuscript` | 空挂 | 空挂 |
| `05-write-venue` | `Evidence Insight/venue-templates/; Academic Writing/journal-cover-prompter/` | `05_manuscript` | 部分 | journal matcher / preflight; journal pick still Victor/03 |
| `05-write-polish` | `Academic Writing/medical-email-polisher/; Academic Writing/medical-translation/; Academic Writing/response-tone-polisher/ (+1)` | `05_manuscript` | 部分 | English / consistency workers; not de-AI |
| `05-humanize` | `—` | `05_manuscript` | 空挂 | 空挂 |
| `06-review-peer` | `Academic Writing/medical-review-writer-architect/; Academic Writing/peer-review/` | `06_review` | 部分 | peer-review pack — Lee owns judgment |
| `06-review-critique` | `—` | `06_review` | 空挂 | 空挂 |
| `06-review-response` | `Academic Writing/blind-review-sanitizer/; Academic Writing/peer-review-response-drafter/; Other/sci-paper-reviewer/` | `06_review` | 部分 | response drafter — Lee + review-resolution owns status |

## 空挂

若只用本套，这些先通知再检索确认。个人 de-AI 仍在 A `05_manuscript/personal/`。批注前缀用 `[AIPOCH:…]`。

## 明确不进菜单（EXCLUDE / 未映射组）

- 实验室运营（试剂/库存/CO₂/危废）
- 医学教育 / SOAP / 出院小结 / USMLE
- 办公杂件（PPTX/CV/会议纪要）
- 纯化合物/对接大库（非本影像管线）——需要时走任务点名，不占粗 ID

**Meta-skill：** 若包内自带 systematic-review 类编排器，只可当 worker，**不得**抢走 `00_orchestrator` 调度权。
