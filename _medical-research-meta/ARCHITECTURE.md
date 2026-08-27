# Architecture and Handoff Contract

## Skill selection

The orchestrator selects the **smallest** set of skills that can complete the task.

### Typical flows

| Flow | Route |
|------|--------|
| Intro/Discussion literature → manuscript | `05_manuscript` (`intro-discussion-evidence`) |
| Literature → manuscript | `03_research` 选题选刊 → `05_manuscript` I/D 检索成文 |
| Imaging study design | `03_research` → `02_imaging` → `04_analysis` → `05_manuscript` |
| Prediction-model paper | `03_research` → `04_analysis` → `05_manuscript` → optional `06_review` |
| Imaging prediction model | SOP `../core/00_orchestrator/workflows/radiomics-study.md` then `sci-manuscript.md` |
| Pre-submission audit only | `06_review` (manuscript-quality) |
| Response to reviewers | `06_review` (manuscript-quality) → `05_manuscript` polish |
| Coding / batch / office | `01_automation` for Excel/workspace; `code-refactoring` for soft-coding |
| Radiomics pipeline code | `02_imaging` (radiomics-habitat) + `code-refactoring` |

### Lab-specific flows (Ying Li)

| Intent | Route |
|--------|--------|
| 按我的风格润色 / SCI 写作 | `05_manuscript` |
| 写引言 / 写讨论 / 补文献 | `05_manuscript` → `intro-discussion-evidence.md` |
| 投稿前找问题 / dealbreaker | `06_review` |
| 回复审稿人 | `06_review` (`manuscript-quality`) |
| 选题 / 选刊 | `03_research` |
| AUC / DeLong / DCA / 统计计划 | `04_analysis` |
| 组学 / ROI / 泄漏审计 | `02_imaging` |
| 软编码 / dry-run | `code-refactoring` |
| 批处理 / Excel | `01_automation` |
| 0RAD 文件夹 / exc / 假分类 | `01_automation` → `../core/01_automation/references/0rad-workspace.md` |
| VAL_MODE / 两两比较 / 亚组 ROC | `04_analysis` → `../core/04_analysis/references/0rad-pipeline-rules.md` |
| 伦理申请表填写 | `ethics-application-forms` |
| 临床提取 / HIS | `clinical-data-extraction` |
| 转化 / reader study | `clinical-translation` |
| 期刊级 ROC/校准/DCA 图 | `05_manuscript` (`figure-engine` / `lab-palettes.md`) |

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

These are modes, tools, or reference files inside `core/01`–`06`, except the four `archive/` standalone skills.

`skill-harvest` writes into core/archive. It is not a research domain.

## Frozen layout (P0)

Live tree: `skills/core/` (00–06 + harvest) and `skills/archive/` (four standalone skills). **Do not add `07_`.** Nested `data-impute` and `figure-engine` stay modules. New work is a bundle under an existing core domain, or an approved archive skill.

Target depth: `0X_domain/bundles/<package>/MODULE.md` (Domain → Bundle → Module). References and scripts live **inside that bundle**, not a second copy on the parent. Cross-bundle: relative path only, no file duplicate.

P1: optional `ref/project-state.yaml` (template in `00_orchestrator/templates/`); SOPs in `00_orchestrator/workflows/` (`radiomics-study`, `sci-manuscript`). 「全线」still **asks which SOP**.

P2: bundle `MODULE.md` YAML (`name/domain/trigger/inputs/outputs/tools/quality_control/owner`). `trigger` is documentation only. Evals: `_medical-research-meta/tests/` (no LLM). Nested `references/merged/**/MODULE.md` stay headerless.
