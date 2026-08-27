---
name: medical-research-orchestrator
description: >
  Route multi-step medical-research work across the 01–06 domain skills. Use for end-to-end,
  autonomous, multi-stage, or project-level tasks. Do not use for a single bounded task
  when one domain skill is sufficient.
---

# Medical Research Orchestrator

The orchestrator chooses the minimum skill set and preserves handoffs. It does not duplicate
research, statistical, imaging, writing, or automation rules.

## Active routes

| Skill | Primary scope |
|---|---|
| `01_automation` | Excel/CSV, 0RAD workspace, batch file pipelines |
| `02_imaging` | MRI/fMRI, DICOM/NIfTI, segmentation, preprocessing, radiomics, habitat, imaging QC |
| `03_research` | Research question, study design, sample size, evidence, journal/topic selection, grant |
| `04_analysis` | Statistics, prediction models, ML analysis, imputation, validation |
| `05_manuscript` | SCI original-article writing, polishing, de-AI, figures |
| `06_review` | Pre-submission audit, peer review of others, reviewer-response letters |
| `skill-harvest` | Skill maintenance, routing, deduplication, ROI measurement, evolution |

Archive (standalone, not 00–06):

| Skill | Primary scope |
|---|---|
| `code-refactoring` | Soft-coding, dry-run, CONFIG on top, modular scripts |
| `ethics-application-forms` | Hospital IRB / ethics form packs |
| `clinical-data-extraction` | Labs, pathology text, HIS extraction |
| `clinical-translation` | Reader studies, prospective/real-world translation |

## Fast routing

- Excel / 批处理 / 0RAD 文件夹 → `01_automation`
- 软编码 / dry-run / 配置置顶 → `code-refactoring`
- 伦理申请 / 填伦理 → `ethics-application-forms`
- 提取检验 / HIS / 病理全文 → `clinical-data-extraction`
- 转化 / reader study / 读者研究 → `clinical-translation`
- MRI / fMRI / DICOM / NIfTI / registration / segmentation / radiomics / habitat → `02_imaging`
- 选题 / 研究设计 / 选刊 / 样本量 / 文献证据 → `03_research`
- 统计 / AUC / DeLong / DCA / LASSO / survival / imputation / prediction → `04_analysis`
- 写作 / 润色 / 引言 / Discussion / figures → `05_manuscript`
- 预审 / 审稿 / 评阅 / 回复审稿人 → `06_review`
- 整理聊天 / 更新技能 / 技能迭代 / 收益评估 / 边界设计 → `skill-harvest`

## Common composite routes

- Full research project: `03_research → 02_imaging (if imaging) → 04_analysis → 05_manuscript → 06_review → 01_automation as needed`
- Imaging prediction paper: `03_research → 02_imaging → 04_analysis → 05_manuscript` then optional `06_review`
- Manuscript revision: `05_manuscript` for prose; `06_review` for audit/response. Call another domain only for a factual/statistical/imaging defect.
- Reviewer response: `06_review`; `05_manuscript` for changed sentences; call `04_analysis` or `02_imaging` only when the response requires new analysis or imaging verification.

## Boundaries

Do not create a top-level skill for a disease, package, manuscript section, statistical test,
metric, or imaging modality. Add a mode, reference, workflow, or tool inside the existing home
(`core/00`–`06`, `skill-harvest`, plus `archive/` standalone skills).

Do not load all nested material. Load the selected `SKILL.md`, then only the required `MODULE.md`
and references/scripts.

## Final QC

Check objective completion, denominators, numerical claims, imaging parameters, citations,
causality language, file usability, and requested output format.
