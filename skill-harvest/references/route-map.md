# Harvest route map — framework A (2026-09-02)

Write harvested facts into an existing business skill. `skill-harvest` owns maintenance, not research content.
`01_skill-discovery-integration` mounts external Skills; harvest proposes evolution. Do not mix the jobs.

| User intent / artifact | Authoritative home | Exclude / hand off |
|---|---|---|
| Discover / evaluate / mount an external Skill | `01_skill-discovery-integration` | Never literature/stats/writing/review here |
| Excel/CSV, 0RAD workspace, batch tables, imaging prep, impute | `02_data-processing` | Soft-coding → `02_data-processing/code-refactoring`; modeling → `04_analysis` |
| Soft-coding, dry-run, CONFIG-on-top refactor | `02_data-processing/code-refactoring` | Statistical methods → `04_analysis`; imaging prep → `02_data-processing` |
| Clinical text / HIS / pathology extraction | `02_data-processing/clinical-data-extraction` | Imputation → `02_data-processing` (`02-impute`) |
| Hospital IRB / ethics form packs | `03_research/ethics-application-forms` | Ethics prose in a manuscript → `05_manuscript`; protocol ethics → `03_research/personal/ethics.md` |
| MRI/fMRI preprocessing/QC, radiomics **preparation**, habitat prep | `02_data-processing` | Stats/figures → `04_analysis`; radiogenomics design → `03_research` |
| Clinical translation / reader studies | `03_research/clinical-translation` | Stats → `04_analysis`; figures → `04_analysis` |
| Study design, **literature**, journal selection, grants | `03_research` | Manuscript-specific I/D wording → `05_manuscript` |
| Statistical analysis, prediction, **figures** | `04_analysis` | Imaging prep → `02_data-processing` |
| SCI original-article writing, Aitor style, de-AI | `05_manuscript` | Figures → `04_analysis`; pre-review / response → `06_review`; literature → `03_research` |
| Pre-submission audit, peer review, **reviewer-response letters** | `06_review` | Sentence rewrite → `05_manuscript`; new analysis → `04_analysis`; imaging verification → `02_data-processing` |
| Cross-skill SOPs and task orchestration | `00_orchestrator` | Do not create a new domain skill |
| Harvest/evolution/ROI/boundary governance | `skill-harvest` | Never copy this governance into domain skills |

## Ownership rules

1. One fact has one authoritative home.
2. Parent skills may contain only a short pointer to a deeper reference or a **mounted id**.
3. A project-specific fact belongs in project state or handoff notes, not a permanent Skill.
4. Deterministic repeated work belongs in a script/tool.
5. A repeatable multi-skill procedure belongs in `00_orchestrator/workflows/`.
6. No new top-level research domain without an explicit architecture decision.
7. Do not harvest into deleted `bundles/` paths.

## Routing examples

- “查文献写 Introduction/Discussion” → literature `03_research`; wording `05_manuscript`.
- “设计 radiomics/habitat pipeline” → prep `02_data-processing`; statistical model comparison `04_analysis`.
- “修改 SCI / 润色 / 写引言讨论” → `05_manuscript`; “模拟审稿、评阅、回复 reviewer” → `06_review`.
- “处理 Excel / 0RAD 文件夹” → `02_data-processing`; “修 Python/软编码” → `02_data-processing/code-refactoring`.
- “画 ROC/流程图” → `04_analysis` (mounted `04-figure-engine`).
