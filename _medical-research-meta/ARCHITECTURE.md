# Architecture and Handoff Contract

## Skill selection

The orchestrator classifies the task and selects the **smallest** set of skills that can complete it.

| Intent | Route |
|---|---|
| Skill discovery / new external capability | `01_skill-discovery-integration` |
| Excel / 0RAD workspace / cleaning / imaging prep / impute / extraction / coding principles / ethics forms (temp) | `02_data-processing` |
| Literature research / evidence / study design / grants / translational design | `03_research` |
| Statistics / prediction / **figures** | `04_analysis` |
| Scientific writing / personal style / de-AI | `05_manuscript` |
| Peer review / **reviewer response** | `06_review` |
| Evolution governance | `skill-harvest` |

### Lab-specific flows (Ying Li)

| Intent | Route |
|--------|--------|
| 按我的风格润色 / SCI 写作 | `05_manuscript` |
| 写引言 / 写讨论（成文） | `03_research` retrieves; `05_manuscript` writes (`personal/intro-discussion-evidence.md`) |
| 投稿前找问题 / dealbreaker | `06_review` |
| 回复审稿人 | `06_review` only as entry |
| 选题 / 选刊 / 文献 | `03_research` |
| AUC / DeLong / DCA / 统计计划 / 出图 | `04_analysis` |
| 组学 / ROI / 泄漏审计 / 预处理 | `02_data-processing` |
| 软编码 / dry-run | `02_data-processing` → `code-refactoring/` |
| 批处理 / Excel / 0RAD 文件夹 | `02_data-processing` → `0rad-workspace.md` |
| VAL_MODE / 两两比较 / 亚组 ROC | `04_analysis` → `personal/0rad-pipeline-rules.md` |
| 伦理申请表填写 | `02_data-processing` → `ethics-application-forms/`（暂时挂在 02，真正家园仍是 03 伦理设计） |
| 临床提取 / HIS | `02_data-processing` → `clinical-data-extraction/` |
| 转化 / reader study | `03_research` → `clinical-translation/` |
| 期刊级 ROC/校准/DCA 图 | `04_analysis` (mounted `04-figure-engine` + `personal/lab-palettes.md`) |
| 新外接技能 | `01_skill-discovery-integration` |

## Final QC (handoff folded in)

`00_orchestrator` owns the final QC gate. Completeness: deliverable exists; consistency checks pass; assumptions visible; limitations stated; files usable.

Handoff payload when crossing skills: objective, inputs inspected, decisions, assumptions, completed outputs, exclusions, unresolved issues, required downstream actions.

**Local recovery:** if QC finds a localized defect, identify the responsible skill and send **only the erroneous portion** back. Do not rerun already-correct stages.

`workflow → final QC → localized defect → responsible skill → re-run that node → final QC → output`

## External Skill mounting

`01_skill-discovery-integration` resolves capabilities in this order:

1. mounted Skills;
2. approved default external mounts (none until APPROVED);
3. network/GitHub discovery;
4. if network is unavailable, request a local Skill/repository path;
5. evaluate capability and boundaries;
6. propose mount;
7. require explicit user approval;
8. mount.

Default candidate: `Imbad0202/academic-research-skills`. Backup: `Aperivue/medsci-skills`.
`mounts: []` — PROPOSED is not MOUNTED. No automatic mounting.

## Domain boundaries

- `02_data-processing`: raw data → analysis-ready data. Statistics/model fitting is not its role.
- `03_research`: research design and literature/evidence. Manuscript prose is not its role.
- `04_analysis`: statistical analysis and visualization. Upstream data repair is not its role.
- `05_manuscript`: personal writing layer. Literature retrieval → `03_research`; figure generation → `04_analysis`.
- `06_review`: personal review/response layer. Changed wording → `05_manuscript`.

## Externalization policy

Generic local capabilities marked in `EXTERNALIZATION_CANDIDATES.md` remain available until an approved mounted Skill is confirmed to cover them. Personal rules, personal scripts, and personal style assets are not removed merely because a generic external capability exists.

## Rehomed packs

Former `archive/` standalones now live under domain skills (CHG-20260902-004). `archive/` is empty of skills.

## Invariants

**One fact → one authoritative home.**
**One task → one entry point.**
**An A skill path ≤ 3 directories from repo root (`<skill>/<optional-folder>/file`). No `core/`.**
**User approval is mandatory for mounting or evolution.**
