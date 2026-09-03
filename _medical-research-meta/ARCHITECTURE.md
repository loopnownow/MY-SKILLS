# Architecture and Handoff Contract

Live rules here **must agree** with root `ARCHITECTURE.md`: depth ≤4; default source B; ethics in 03; 30-id menu (not `mounts: []`); no live `04-figure-engine`; ARS/MedSci/Scientific **PROPOSED** backups; `session_mount: ask-each-run`.

## Skill selection

The orchestrator classifies the task and selects the **smallest** set of skills that can complete it.

| Intent | Route |
|---|---|
| Skill discovery / new external capability | `01_skill-discovery-integration` |
| Excel / 0RAD workspace / cleaning / imaging prep / impute / extraction / coding principles | `02_data-processing` |
| Literature research / evidence / study design / grants / translational design / ethics forms | `03_research` |
| Statistics / prediction / **figures** / 样本量 | `04_analysis` |
| Scientific writing / personal style / de-AI / 选刊 | `05_manuscript` |
| Peer review / **reviewer response** | `06_review` |
| Evolution governance | `skill-harvest` |

### Lab-specific flows (Ying Li)

| Intent | Route |
|--------|--------|
| 按我的风格润色 / SCI 写作 | `05_manuscript` |
| 写引言 / 写讨论（成文） | `03_research` retrieves; `05_manuscript` writes (`personal/intro-discussion-evidence.md`) |
| 投稿前找问题 / dealbreaker | `06_review` |
| 回复审稿人 | `06_review` only as entry |
| 选题 / 文献 | `03_research` |
| 选刊 | `05_manuscript` (`05-write-venue`) |
| 样本量 | `04_analysis` (`04-stats-power`) |
| AUC / DeLong / DCA / 统计计划 / 出图 | `04_analysis` |
| 组学 / ROI / 泄漏审计 / 预处理 | `02_data-processing` |
| 软编码 / dry-run | `02_data-processing` → `code-refactoring/` |
| 批处理 / Excel / 0RAD 文件夹 | `02_data-processing` → `0rad-workspace.md` |
| VAL_MODE / 两两比较 / 亚组 ROC | `04_analysis` → `personal/0rad-pipeline-rules.md` |
| 伦理申请表填写 | `03_research` → `ethics-application-forms/` |
| 临床提取（已导出文本） | `02_data-processing` → `clinical-data-extraction/` |
| 转化 / reader study | `03_research` → `clinical-translation/` |
| 期刊级 ROC/校准/DCA 图 | `04_analysis` (mounted `04-fig-plot` + `personal/lab-palettes.md`) |
| STROBE / patient-flow / Figure 1 | `04_analysis` (mounted `04-fig-flow`) |
| 新外接技能 | `01_skill-discovery-integration` |

## Final QC (handoff folded in)

`00_orchestrator` owns the final QC gate. Completeness: deliverable exists; consistency checks pass; assumptions visible; limitations stated; files usable.

Handoff payload when crossing skills: objective, inputs inspected, decisions, assumptions, completed outputs, exclusions, unresolved issues, required downstream actions.

**Local recovery:** if QC finds a localized defect, identify the responsible skill and send **only the erroneous portion** back. Do not rerun already-correct stages.

`workflow → final QC → localized defect → responsible skill → re-run that node → final QC → output`

## External Skill mounting

`01_skill-discovery-integration` resolves capabilities in this order:

1. **Session mount pick** (`ask-each-run`): ask which of the 30 registry `MOUNTED` ids to attach **this run**; load only those.
2. Resolve picked ids against `registry.yaml` (default source B; MedSci-only `04-explainability` / `05-humanize`).
3. If a picked path is empty: notify, re-search, confirm. Never silently fall back.
4. Network/GitHub discovery for **new** capability.
5. If network is unavailable, request a local Skill/repository path.
6. Evaluate capability and boundaries; propose mount; require explicit user approval; then mount.

Default source: `loopnownow/MY-SKILLS-capabilities` (**B**, `role: default-mount`).
Backups: ARS / MedSci / Scientific stay `PROPOSED` (`role: backup-candidate`). Mapping is not a mount.
Registry `MOUNTED` is a **menu of 30 ids**, not `mounts: []`. Never auto-mount a non-B source. No live `04-figure-engine`.

## Domain boundaries

- `02_data-processing`: raw data → analysis-ready data. Statistics/model fitting is not its role. Ethics forms are not here.
- `03_research`: research design, literature/evidence, ethics **forms**, translational design. Manuscript prose is not its role. 选刊 is not here.
- `04_analysis`: statistical analysis and visualization (`04-fig-flow` / `04-fig-plot`). Upstream data repair is not its role.
- `05_manuscript`: personal writing layer + 选刊 (`05-write-venue`). Literature retrieval → `03_research`; figure generation → `04_analysis`. de-AI at `05_manuscript/personal/`.
- `06_review`: personal review/response layer. Changed wording → `05_manuscript`.

## Externalization policy

Generic local capabilities marked in `EXTERNALIZATION_CANDIDATES.md` remain available until an approved mounted Skill is confirmed to cover them. Personal rules, personal scripts, and personal style assets are not removed merely because a generic external capability exists.

## Rehomed packs

Former `archive/` standalones now live under domain skills (CHG-20260902-004). `archive/` is empty of skills. Ethics fill pack is under `03_research/ethics-application-forms/`.

## Invariants

**One fact → one authoritative home.**
**One task → one entry point.**
**An A skill path ≤ 4 directories from repo root (`<skill>/<category-or-pack>/<scripts|references|personal>/file`). No `core/`.**
**User approval is mandatory for mounting or evolution.**
**Default source B. Backups PROPOSED. 30-id menu. session pick each run.**
