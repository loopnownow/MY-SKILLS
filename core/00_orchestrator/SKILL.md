---
name: medical-research-orchestrator
description: >
  Classify the task, route it, run composite multi-skill workflows, and own Final QC
  plus local recovery. Use for end-to-end or multi-stage work. Do not use when a
  single domain skill is enough. Do not do literature, stats, writing, or review here.
---

# Medical Research Orchestrator

The orchestrator **classifies**, **routes**, **sequences composite workflows**, and owns **Final QC + local recovery**.
It does not duplicate research, statistical, imaging, writing, or discovery rules.

## Classification

Pick the smallest skill set. One bounded task → that domain skill, not 00.

## Routing

| Skill | Primary scope |
|---|---|
| `01_skill-discovery-integration` | Discover / evaluate / mount external Skills. Never literature, stats, writing, or review. |
| `02_data-processing` | Raw → analysis-ready data. Excel/CSV, 0RAD workspace, imaging QC, radiomics prep, imputation. No modeling. |
| `03_research` | Study design, **literature**, evidence, frontier, journal/topic, grants. Literature enters 03 only. |
| `04_analysis` | Statistics, prediction, survival, **figures**. Data repair is not its role. |
| `05_manuscript` | Personal SCI writing / polish / de-AI. Not figures. Not reviewer response. |
| `06_review` | Pre-submission, peer review, **reviewer response only here**. Does not write the paper. |
| `skill-harvest` | Evolution / ROI / boundaries. Not a research domain. |

Archive (standalone, not 00–06; 00 may still route here):

| Skill | Primary scope |
|---|---|
| `code-refactoring` | Soft-coding, dry-run, CONFIG on top |
| `ethics-application-forms` | Hospital IRB / ethics form packs |
| `clinical-data-extraction` | Labs, pathology text, HIS |
| `clinical-translation` | Reader studies, prospective translation |

### Fast routing

- 新技能 / 外接 / 挂载 → `01_skill-discovery-integration`
- Excel / 批处理 / 0RAD 文件夹 → `02_data-processing`
- 软编码 / dry-run → `code-refactoring`
- 伦理申请表 → `ethics-application-forms`
- 提取检验 / HIS → `clinical-data-extraction`
- 转化 / reader study → `clinical-translation`
- MRI / DICOM / NIfTI / 预处理 / radiomics 准备 / 插补 → `02_data-processing`
- 选题 / 研究设计 / **文献** / 选刊 / 样本量 → `03_research`
- 统计 / AUC / DeLong / DCA / **出图** → `04_analysis`
- 写作 / 润色 / 引言 / Discussion / de-AI → `05_manuscript`
- 预审 / 审稿 / **回复审稿人** → `06_review`
- 技能迭代 / 收益评估 → `skill-harvest`

## Composite workflows

SOPs live in `workflows/` (ask which SOP on 「全线」):

- Full project: `03_research` → `02_data-processing` (if data/imaging) → `04_analysis` → `05_manuscript` → `06_review`
- Imaging prediction paper: `03_research` → `02_data-processing` → `04_analysis` → `05_manuscript` → optional `06_review`
- Manuscript revision: `05_manuscript` for prose; `06_review` for audit/response
- Reviewer response: **`06_review` only as entry**; `05_manuscript` for changed sentences; `04_analysis` / `02_data-processing` only if new analysis or imaging verification is required
- New capability: `01_skill-discovery-integration` (network first, then ask for a local path). Never auto-mount.

Project state template: `templates/project-state.yaml`.

## Boundaries

Do not create a top-level skill for a disease, package, manuscript section, statistical test, metric, or imaging modality.
Do not load all nested material. Load the selected `SKILL.md`, then only the required files.
Mounted generic capability lives in `MY-SKILLS-capabilities` (ids in `MOUNTED_SKILLS.md`). Point at **mounted ids**, not deleted `bundles/` paths.

## Final QC (includes handoff + local recovery)

00 owns the last gate. A task is complete only when the requested deliverable exists, major consistency checks pass, assumptions are visible, limitations are stated, and files are usable.

When handing work between skills, the payload is: objective, inputs inspected, decisions, assumptions, completed outputs, exclusions, unresolved issues, required downstream actions.

**Local recovery:** if QC finds a localized defect, identify the responsible skill and re-run **only the broken node**. Do not rerun already-correct stages.

`workflow → final QC → localized defect → responsible skill → re-run that node → final QC → output`
