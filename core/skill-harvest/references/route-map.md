# Harvest route map — Lean v5

Write harvested facts into an existing business skill. `skill-harvest` owns maintenance, not research content.

| User intent / artifact | Authoritative home | Exclude / hand off |
|---|---|---|
| Excel/CSV, 0RAD workspace, batch file pipelines | `01_automation` | Soft-coding → `code-refactoring`; extraction → `clinical-data-extraction`; ethics forms → `ethics-application-forms` |
| Soft-coding, dry-run, CONFIG-on-top refactor | `code-refactoring` | Statistical methods → `04_analysis`; imaging methods → `02_imaging` |
| Clinical text / HIS / pathology extraction | `clinical-data-extraction` | Imputation → `04_analysis` `data-impute` |
| Hospital IRB / ethics form packs | `ethics-application-forms` | Ethics prose in a manuscript → `05_manuscript` |
| MRI/fMRI preprocessing/QC, radiomics, habitat | `02_imaging` | Manuscript prose/figure production → `05_manuscript`; radiogenomics design → `03_research` |
| Clinical translation / reader studies / prospective validation | `clinical-translation` | Stats → `04_analysis`; figures → `05_manuscript` |
| Study design, topic selection, evidence landscape, journal selection, grants | `03_research` | Manuscript-specific I/D evidence → `05_manuscript` |
| Statistical analysis, prediction models, imputation, validation statistics | `04_analysis` | Imaging-specific pipeline → `02_imaging` |
| SCI original-article writing, Aitor style, de-AI, figures | `05_manuscript` | Pre-review / peer review / response → `06_review`; study design → `03_research`; stats execution → `04_analysis` |
| Pre-submission audit, peer review of others, reviewer-response letters | `06_review` | Sentence/layout rewrite → `05_manuscript`; new analysis → `04_analysis`; imaging verification → `02_imaging` |
| Cross-skill SOPs and task orchestration | `00_orchestrator` | Do not create a new domain skill |
| Harvest/evolution/ROI/boundary governance | `skill-harvest` | Never copy this governance into domain skills |

## Ownership rules

1. One fact has one authoritative home.
2. Parent skills may contain only a short pointer to a deeper reference.
3. A project-specific fact belongs in project state or handoff notes, not a permanent Skill.
4. Deterministic repeated work belongs in a script/tool.
5. A repeatable multi-skill procedure belongs in `00_orchestrator/workflows/`.
6. No new top-level research domain without an explicit architecture decision.

## Routing examples

- “查文献写 Introduction/Discussion” → `05_manuscript`; pure topic/journal landscape → `03_research`.
- “设计 radiomics/habitat pipeline” → `02_imaging`; statistical model comparison → `04_analysis`.
- “修改 SCI / 润色 / 写引言讨论” → `05_manuscript`; “模拟审稿、评阅、回复 reviewer” → `06_review`.
- “批量提取临床数据” → `clinical-data-extraction`; “修 Python/软编码” → `code-refactoring`; “处理 Excel” → `01_automation`.
