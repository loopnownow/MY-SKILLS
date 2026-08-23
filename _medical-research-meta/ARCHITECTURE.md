# Architecture and Handoff Contract

## Skill selection

The orchestrator selects the **smallest** set of skills that can complete the task.

### Typical flows

| Flow | Route |
|------|--------|
| Literature → manuscript | `01_research` → `04_writing` |
| Imaging study design | `01_research` → `03_imaging` → `02_analysis` → `04_writing` |
| Prediction-model paper | `01_research` → `02_analysis` → `04_writing` → `05_review` |
| Imaging prediction model | `01_research` → `03_imaging` → `02_analysis` → `04_writing` → `05_review` |
| Pre-submission audit only | `05_review` (ly-prereview) |
| Response to reviewers | `05_review` (ly-response) → optional `04_writing` polish |
| Coding / batch / office | `06_automation` (+ domain skill if methods) |
| Radiomics pipeline code | `03_imaging` (radiomics-pipeline-toolkit) + `06_automation` (ly-rules) |

### Lab-specific flows (Ying Li)

| Intent | Route |
|--------|--------|
| 按我的风格润色 / SCI 写作 | `04_writing` |
| 投稿前找问题 / dealbreaker | `05_review` |
| 回复审稿人 | `05_review` |
| 查文献 / DOI / Zotero | `01_research` |
| AUC / DeLong / DCA / 统计计划 | `02_analysis` |
| 组学 / ROI / 泄漏审计 | `03_imaging` |
| 软编码 / dry-run / 批处理脚本 | `06_automation` |
| 0RAD 文件夹 / exc / 假分类 | `06_automation` → `references/0rad-workspace.md` |
| VAL_MODE / 两两比较 / 亚组 ROC | `02_analysis` → `references/0rad-pipeline-rules.md` |
| 伦理申请表填写 | `06_automation` (ethics-application-forms) |
| 读片会 PPT | system `pptx` |
| 期刊级 ROC/校准/DCA 图 | `04_writing` (ly-figures) |

## Handoff contract

When handing work to another skill, provide:

- Objective
- Inputs inspected
- Decisions made
- Assumptions
- Completed outputs
- Exclusions
- Unresolved issues
- Required downstream actions

## Completion contract

A task is complete only when:

1. the requested deliverable exists;
2. major internal consistency checks pass;
3. important assumptions are visible;
4. limitations or unresolved issues are stated;
5. requested files are usable.

## Boundary rules (do not create new top-level skills for)

- diseases / organ systems
- individual software packages (PyTorch, PyRadiomics, SPSS…)
- individual manuscript sections
- individual statistical tests
- individual imaging metrics

These are modes, tools, or reference files inside the seven skills.

`skill-harvest` is the only extra top-level skill: it **writes into** 00–06. It is not a research domain.
