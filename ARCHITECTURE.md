# Architecture and Handoff Contract

This file is **integration metadata**: lab intent tables, handoff/QC loop, and ownership phrases pinned by tests.

**Architecture SSOT** for this repo: this file (layers, mounts, lab homes, fine-id ceiling, base/personal contract, Cache≠Mount, load_priority).

**Routing SSOT:** `01_skill-integration/registry.yaml` 
**Generated mount index:** `01_skill-integration/MOUNTED_SKILLS.md`

Live rules: A skill path at most five parts from repo root (exception: `NN_slug/base/**` for in-repo capability bodies); default source my-skills (in-repo base); ethics in `03_research`; menu shape is `01_skill-integration/registry.yaml` (not `mounts: []`; do not restate totals here); no live figure engine; non-base packages are mixed PROPOSED/MOUNTED per registry; OpenClaw is not a default mount source; `session_mount: ask-each-run`; G-FACT consistency; harvest-qc passive. Hybrid mount stays (never mix packages inside one fine id). Figures: `draw-flowchart` / `plot-figures`. 选刊走 03 `find-journal`；体例走 `05_manuscript/base/write-venue/`. 样本量: `calc-sample-size`.

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
| Peer review / re-review | `06_review` (Lee) |
| Reviewer response / response letter | `07_response` (Aitee) |
| Evolution governance | MY-RULES `skills.md` (skill-evolution; former skill-harvest archived) |

### Lab-specific flows (Aitor)

| Intent | Route |
|--------|--------|
| 按我的风格润色 / SCI 写作 | `05_manuscript` |
| 写引言 / 写讨论（成文） | `03_research` retrieves; `05_manuscript` writes (`personal/process/evidence.md`) |
| 投稿前找问题 / dealbreaker | `06_review` |
| 回复审稿人 | `07_response` only as entry (Aitee) |
| 选题 / 文献 / 选刊 | `03_research` |
| 选刊 | `03_research` (`personal/journal-selection.md`). 选刊走 03 `find-journal`；体例走 `05_manuscript/base/write-venue/` |
| 样本量 | `04_analysis` (`calc-sample-size`) |
| AUC / DeLong / DCA / 统计计划 / 出图 | `04_analysis` |
| 组学 / ROI / 泄漏审计 / 预处理 | `02_data-processing` |
| 软编码 / dry-run | `02_data-processing` → `personal/coding.md` |
| 批处理 / Excel / 0RAD 文件夹 | `02_data-processing` → `personal/workspace.md` |
| VAL_MODE / 两两比较 / 亚组 ROC | `04_analysis` → `personal/pipeline.md` |
| 伦理申请表填写 | `03_research` → `base/fill-protocol/` |
| 临床提取（已导出文本） | `02_data-processing` → `personal/extract.md` |
| 转化 / reader study | `03_research` → `clinical-translation/` |
| 期刊级 ROC/校准/DCA 图 | `04_analysis` (mounted `plot-figures` + `{doc_root}\\templates\\lab-palettes.md`) |
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

## Ownership (pinned; agrees with ownership-contract; seats 05/06/07)

Ownership: see `00_orchestrator/references/ownership-contract.md`. Requires 03 citation-verify (cannot skip). Lee owns statement then data consistency; lit accuracy is joint with Victor.

---

## Domain boundaries (lab intent)

- `02_data-processing`: raw → analysis-ready. Statistics/model fitting is not its role. Ethics forms are not here.
- `03_research`: design, literature/evidence, ethics **forms** path (`fill-protocol`, **seat Bai**), translational design, **选刊**, **citation-verify** before 05 done and inside 06. Manuscript prose is not its role. Victor does not fill ethics forms.
- `04_analysis`: statistics and visualization (`draw-flowchart` / `plot-figures`). Upstream data repair is not its role.
- `05_manuscript`: personal writing layer. Literature retrieval and 选刊 → `03_research`; figures → `04_analysis`. de-AI at `05_manuscript/personal/`. Mid-entry does not waive citation-verify.
- `06_review`: personal review / re-review layer (**Lee**). Changed wording → `05_manuscript`.
- `07_response`: personal response-letter layer (**Aitee**). Changed wording → `05_manuscript`.

---

## Mount resolution (pointer)

Session pick and mount steps live in `01_skill-integration/SKILL.md` (thin) + `references/session-pick.md` / `references/lifecycle-cache.md` (this file has no Mounts section).

Order: `ask-each-run` fine-id pick → resolve against `registry.yaml` (default source my-skills (in-repo base); MedSci-only `humanize`; archived ids off menu) → empty path: notify, re-search, confirm → network discovery for **new** capability → evaluate → explicit user approval → mount. Never auto-mount a non-base source. Local cache: lab `{mounts_cap}/` (verified cache, not SSOT; see `.gitignore` / lab-paths).
