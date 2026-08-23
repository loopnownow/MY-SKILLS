---
name: medical-research-orchestrator
description: >
  Route multi-step Ying Li lab work across 01–06 (data → stats → manuscript → pre-review).
  Use when: 全线, 从数据到写稿, 这个项目做到投稿, 组学+统计+写稿, 端到端,
  自动, 自主, 自己做, 组学, 打开项目, 进入工程.
  Also use when the user only cds into a 0RAD project and no 01–06 verb is present
  (then ask which skill to fire). Do not use for a single 润色, 单查文献, or 单评阅.
---

# Medical Research Orchestrator (integrated)

## Purpose

Top-level router for a medical / imaging-research workspace. Convert the objective into a
bounded workflow, select the **minimum** skill set, preserve handoffs, final QC.

Does **not** replace domain expertise. Decides **what, in what order, which skill**.

## Core routing map

| Skill | Use for |
|-------|---------|
| `01_research` | Literature, evidence synthesis, research question, study design, sample size, bias, reporting framework choice, journal selection, frontier |
| `02_analysis` | Statistics, survival, prediction models, ML, feature selection, validation, imputation, reverse reconstruction |
| `03_imaging` | Radiomics, ROI/annotation, MRI/rs-fMRI, DL design, DICOM/NIfTI/ops, radiogenomics, leakage in imaging pipelines |
| `04_writing` | Manuscript draft/polish (Ying Li voice), de-AI, figure legends, journal figures, translation |
| `05_review` | Pre-submission dealbreakers, peer-review simulation, formal reviewer response letters |
| `06_automation` | Python/R coding rules (soft-coding, dry-run), batch pipelines, Excel, ethics form fill, skill engineering |

## Ying Li lab shortcut map

| User says / intent | Route |
|--------------------|--------|
| 自动 / 自主 / 自己做 / 全线 / 组学（整项） | `00` 再分到 02/03/04 |
| 只打开/cd 进某个工程、没有 01–06 触发词 | **先问选哪个技能**，不要直接开干 |
| 润色 / 按我的风格写 / 我的风格 / SCI写作 / 去AI / 去除AI / 英文论著 / Aitor-format | `04_writing`（全文先加载 `Aitor-format.md`） |
| 投稿前预审 / 评阅 / 评审 / 审稿 / 审阅 / 批判性意见 / 25-30条 | `05_review`（SCI 全文：25–30 问 + 改稿前选择题） |
| 批处理 SCI 稿 / 润色后审再改 | `04_writing` 版式润色 → `05_review` 25–30 问 → 用户选择题 → `04_writing` 改稿 |
| 回复审稿人 / response letter | `05_review` |
| 查文献 / PubMed / DOI / 找文献 / 选题 / 选刊 / 系统综述 | `01_research` |
| 统计 / 插补 / AUC / DeLong / 套公式 / 两两比较 | `02_analysis` |
| 图像 / 图像处理 / DICOM / NIfTI / 分割 / 配准 | `03_imaging` |
| 软编码 / dry-run / 批处理 / 合并表 / 对齐 / 英文化 / 伦理申请 | `06_automation` |
| 整理聊天记录 / 更新技能 / 从会话提取 / /skill-harvest | `skill-harvest`（写入 00–06，不新建病种技能） |
| exc / 假分类 / 文件夹命名 | `06_automation` → `references/0rad-workspace.md` |
| 锁定阈值 / 套公式 / 两两比较 / VAL_MODE / 亚组 ROC / 分层评估 | `02_analysis` → `references/0rad-pipeline-rules.md` |
| 伦理申请表 | `06_automation` |
| 作图 ROC/校准/DCA | `04_writing` (figures bundle) |
| 配色 / 色板 / FIG_PALETTE | `04_writing` → `ly-figures/references/lab-palettes.md` |
| 流程图 / STROBE / 入组图 / Figure 1 flow | `04_writing` → `ly-figures/bundles/strobe-flowchart`（不画纳入标准；训练/验证下连分析行） |
| 读片会 PPT / `.pptx` | system `pptx` |
| 评阅 / 评阅论文 / 评审 / 审稿 / 审阅 / 审这篇 / 帮我评这篇 / 点评稿件 / 模拟审稿 | `05_review` |

## Project open, no skill (lab rule)

If the user only enters a project (`cd D:\0Grok\0RAD\<name>`, “打开 xlm_LG”, a bare project path) and **no** 01–06 trigger from the shortcut map is present:

1. Do **not** start analysis, writing, or file edits.
2. Ask which skill to fire. Offer at least:

| 选项 | 技能 |
|------|------|
| 自主 / 全线做完 | `00` → 再分 02/03/04 |
| 查文献 / 选题选刊 | `01_research` |
| 统计 / 插补 / AUC | `02_analysis` |
| 图像 / 图像处理 | `03_imaging` |
| 按我的风格写 / 润色 | `04_writing` |
| 评阅 / 审稿 | `05_review` |
| 合并表 / 对齐 / 软编码 / 伦理 | `06_automation` |
| 先不触发，只看目录 | 无 |

3. Wait for the pick, then load that skill’s `SKILL.md`.

## Workflow

1. Identify final deliverable. If this turn is “project open, no skill”, stop at the choice above.
2. Extract inputs, constraints, population, modality, outcomes, format.
3. Classify: single-skill | sequential multi-skill | iterative multi-skill.
4. Select minimum skills; load each skill's `SKILL.md`, then the relevant `bundles/*/MODULE.md` (modules are not independently discoverable).
5. Explicit handoffs (completed work, assumptions, files, decisions to preserve).
6. Execute in dependency order; do not stop early if the goal is broader.
7. Final QC: n/denominators, stats claims, imaging params, citations, causality language, file usability.
8. Report completed work and material unresolved issues.

## Routing rules (keyword)

- Literature-heavy → `01_research`
- Numerical/statistical → `02_analysis`
- NIfTI/DICOM/MRI/radiomics/DL design → `03_imaging`
- Manuscript/prose/polish/figures → `04_writing`
- Review / find flaws / reply to reviewers → `05_review`
- Code/data/file/pipeline/LLM automation → `06_automation`

## Important boundaries

Do **not** create new skills for diseases, packages, manuscript sections, individual tests, or metrics.
Treat as modes/tools inside the seven-skill architecture.

## Final QC checklist

- Answers the original objective?
- Sample sizes consistent?
- Statistical claims supported?
- Imaging parameters consistent?
- Literature claims traceable?
- Causality avoided when design forbids it?
- Requested file format present and usable?

## Progressive disclosure (medium compression)

Only the seven top-level skills are registered for discovery. Nested material is `MODULE.md` + `references/` + `scripts/`. Load modules on demand after the top-level skill is selected — do not treat library modules as separate skills.
