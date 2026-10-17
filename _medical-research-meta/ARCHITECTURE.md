# Architecture and Handoff Contract

This file is **integration metadata**: lab intent tables, handoff/QC loop, and ownership phrases pinned by tests.

**Architecture SSOT** (layers, mounts, lab homes, fine-id ceiling, A/B contract, Cache≠Mount, load_priority): [`../ARCHITECTURE.md`](../ARCHITECTURE.md)

**Routing SSOT:** `01_skill-integration/registry.yaml`  
**Generated mount index:** `01_skill-integration/MOUNTED_SKILLS.md`

Live rules here **must agree** with root `ARCHITECTURE.md`: A skill path at most five parts from repo root; default source B; ethics in `03_research`; menu shape is `01_skill-integration/registry.yaml` (not `mounts: []`; do not restate totals here); no live figure engine; non-B packages are mixed PROPOSED/MOUNTED per registry; OpenClaw is not a default mount source; `session_mount: ask-each-run`; G-FACT consistency; harvest-qc passive. Hybrid mount stays (never mix packages inside one fine id). Figures: `draw-flowchart` / `plot-figures`. 选刊走 03 `find-journal`；`venue-templates` 只管体例. 样本量: `calc-sample-size`.

Do not duplicate root mount policy, fine-id ceiling, Cache≠Mount, load_priority, or A/B contract tables here.

---

## Skill selection

The orchestrator classifies the task and selects the **smallest** set of skills that can complete it.

| Intent | Route |
|---|---|
| Skill mount / index / hybrid recipes | `01_skill-integration` |
| Excel / 0RAD workspace / cleaning / imaging prep / impute / extraction / coding principles | `02_data-processing` |
| Literature research / evidence / study design / grants / translational design / ethics forms (Bai seats fill-protocol) | `03_research` |
| Statistics / prediction / **figures** / 样本量 | `04_analysis` |
| Scientific writing / personal style / de-AI | `05_manuscript` |
| Peer review / **reviewer response** | `06_review` |
| Evolution governance | MY-RULES `skills.md` (skill-evolution; former skill-harvest archived) |

### Lab-specific flows (Ying Li)

| Intent | Route |
|--------|--------|
| 按我的风格润色 / SCI 写作 | `05_manuscript` |
| 写引言 / 写讨论（成文） | `03_research` retrieves; `05_manuscript` writes (`personal/process/evidence.md`) |
| 投稿前找问题 / dealbreaker | `06_review` |
| 回复审稿人 | `06_review` only as entry |
| 选题 / 文献 / 选刊 | `03_research` |
| 选刊 | `03_research` (`literature/journal-selection.md`). 选刊走 03 `find-journal`；`venue-templates` 只管体例 |
| 样本量 | `04_analysis` (`calc-sample-size`) |
| AUC / DeLong / DCA / 统计计划 / 出图 | `04_analysis` |
| 组学 / ROI / 泄漏审计 / 预处理 | `02_data-processing` |
| 软编码 / dry-run | `02_data-processing` → `personal/coding.md` |
| 批处理 / Excel / 0RAD 文件夹 | `02_data-processing` → `personal/workspace.md` |
| VAL_MODE / 两两比较 / 亚组 ROC | `04_analysis` → `personal/pipeline.md` |
| 伦理申请表填写 | `03_research` → `fill-protocol/` |
| 临床提取（已导出文本） | `02_data-processing` → `personal/extract.md` |
| 转化 / reader study | `03_research` → `clinical-translation/` |
| 期刊级 ROC/校准/DCA 图 | `04_analysis` (mounted `plot-figures` + `personal/lab-palettes.md`) |
| STROBE / patient-flow / Figure 1 | `04_analysis` (mounted `draw-flowchart`) |
| 新外接技能 | `01_skill-integration` |

---

## Final QC (handoff folded in)

`00_orchestrator` owns the QC closed loop: intent classify → skill chain → file check → integrity gate → local recovery. Completeness: deliverable exists; consistency checks pass; assumptions visible; limitations stated; files usable.

Detail: `00_orchestrator/gates.md`. Handoff schema: `00_orchestrator/templates/handoff.yaml`. State fields: `pipeline`, `qc`, `defects` in `project-state.yaml`.

Handoff payload when crossing skills: objective, inputs inspected, decisions, assumptions, completed outputs, exclusions, unresolved issues, required downstream actions.

**Local recovery:** if QC finds a localized defect, identify the responsible skill and send **only the erroneous portion** back. Max 3 rounds, then `unresolved`. Do not rerun already-correct stages.

`plan → execute node → file check → integrity gate → localized defect → responsible skill → re-run that node (max 3) → gate → output`

Interactive by default (plan card before multi-node dispatch). Prose repairs are word/sentence units. Mount vs lab conflicts go to Word comments with an edit plan; the user decides. Lit-verify fail uses a dual plan; 00 decides whether to call 03.

---

## Ownership (pinned; agrees with root Core layers 05/06)

Ownership: see `00_orchestrator/references/ownership-contract.md`. Requires 03 citation-verify (cannot skip). Lee owns statement then data consistency; lit accuracy is joint with Victor.

---

## Domain boundaries (lab intent)

- `02_data-processing`: raw → analysis-ready. Statistics/model fitting is not its role. Ethics forms are not here.
- `03_research`: design, literature/evidence, ethics **forms** path (`fill-protocol`, **seat Bai**), translational design, **选刊**, **citation-verify** before 05 done and inside 06. Manuscript prose is not its role. Victor does not fill ethics forms.
- `04_analysis`: statistics and visualization (`draw-flowchart` / `plot-figures`). Upstream data repair is not its role.
- `05_manuscript`: personal writing layer. Literature retrieval and 选刊 → `03_research`; figures → `04_analysis`. de-AI at `05_manuscript/personal/`. Mid-entry does not waive citation-verify.
- `06_review`: personal review/response layer. Changed wording → `05_manuscript`.

---

## Mount resolution (pointer)

Session pick and mount steps live in root `ARCHITECTURE.md` (Mounts) and `01_skill-integration/SKILL.md` (thin) + `references/session-pick.md` / `references/lifecycle-cache.md`.

Order: `ask-each-run` fine-id pick → resolve against `registry.yaml` (default source B; MedSci-only `humanize`; archived ids off menu) → empty path: notify, re-search, confirm → network discovery for **new** capability → evaluate → explicit user approval → mount. Never auto-mount a non-B source. Local cache: repo-root `mounts-cap/` (verified cache, not SSOT).

---

## Externalization

Generic local capabilities in `EXTERNALIZATION_CANDIDATES.md` stay until an approved mounted Skill covers them. Personal rules, scripts, and style assets are not removed merely because a generic external capability exists.

Standalone packs live under domain skills (e.g. ethics fill pack under `03_research/fill-protocol/`).
