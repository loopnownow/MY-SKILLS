# Architecture and Handoff Contract

This file is **integration metadata**: lab intent tables, handoff/QC loop, and ownership phrases pinned by tests.

**Architecture SSOT** for this repo: this file (layers, lab homes, fine-id ceiling, base/personal contract).

**Routing SSOT:** `01_skill-integration/registry.yaml`

Live rules: A skill path at most five parts from repo root (exception: `NN_slug/base/**` for in-repo capability bodies); bodies are in-repo `my-skills` under `NN_slug/base/` (exception: `check-reporting` at `05_manuscript/qc/check-reporting/`); ethics in `03_research`; menu shape is `01_skill-integration/registry.yaml` (not `mounts: []`; do not restate totals here); no live figure engine; `session_mount: ask-each-run`; G-FACT consistency; harvest-qc passive. One fine id uses one in-repo path. Figures: `draw-flowchart` / `plot-figures`. Journal selection via 03 `find-journal`; venue style via `05_manuscript/base/write-paper/`. sample size: `calc-sample-size`.

---

## Skill selection

The orchestrator classifies the task and selects the **smallest** set of skills that can complete it.

| Intent | Route |
|---|---|
| Skill index / session pick | `01_skill-integration` |
| Excel / batch workspace / cleaning / imaging prep / impute / extraction / coding principles | `02_data-processing` |
| Literature research / evidence / study design / grants / translational design / ethics forms (Bai seats fill-protocol) | `03_research` |
| Statistics / prediction / **figures** / sample size | `04_analysis` |
| Scientific writing / personal style / de-AI | `05_manuscript` |
| Peer review / re-review | `06_review` (Lee) |
| Reviewer response / response letter | `07_response` (Aitee) |
| Evolution governance | MY-RULES `skills.md` (skill-evolution) |

### Lab-specific flows (Aitor)

| Intent | Route |
|--------|--------|
| Polish in my voice / SCI writing | `05_manuscript` |
| Write Introduction / Discussion (prose) | `03_research` retrieves; `05_manuscript` writes (`personal/process/evidence.md`) |
| Pre-submit find issues / dealbreaker | `06_review` |
| Reply to reviewers | `07_response` only as entry (Aitee) |
| Topic / literature / journal selection | `03_research` |
| Journal selection | `03_research` (`personal/journal-selection.md`). Journal selection via 03 `find-journal`; venue style via `05_manuscript/base/write-paper/` |
| sample size | `04_analysis` (`calc-sample-size`) |
| AUC / DeLong / DCA / stats plan / figures | `04_analysis` |
| Radiomics / ROI / leakage audit / preprocess | `02_data-processing` |
| Soft coding / dry-run | `02_data-processing` → `personal/coding.md` |
| Batch / Excel folders | `{RULES}/workspace-layout.md` |
| VAL_MODE / pairwise compare / subgroup ROC | `04_analysis` → `personal/pipeline.md` |
| Ethics application form fill | `03_research` → `base/fill-protocol/` |
| Clinical extraction (exported text) | `02_data-processing` → `personal/extract.md` |
| Translational / reader study | `03_research` → `clinical-translation/` |
| Journal-grade ROC/calibration/DCA figures | `04_analysis` (`plot-figures` + `{doc_root}\\templates\\lab-palettes.md`) |
| STROBE / patient-flow / Figure 1 | `04_analysis` (`draw-flowchart`) |

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
- `03_research`: design, literature/evidence, ethics **forms** path (`fill-protocol`, **seat Bai**), translational design, **journal selection**, **citation-verify** before 05 done and inside 06. Manuscript prose is not its role. Victor does not fill ethics forms.
- `04_analysis`: statistics and visualization (`draw-flowchart` / `plot-figures`). Upstream data repair is not its role.
- `05_manuscript`: personal writing layer. Literature retrieval and journal selection → `03_research`; figures → `04_analysis`. de-AI at `05_manuscript/personal/`. Mid-entry does not waive citation-verify.
- `06_review`: personal review / re-review layer (**Lee**). Changed wording → `05_manuscript`.
- `07_response`: personal response-letter layer (**Aitee**). Changed wording → `05_manuscript`.

---

## Session pick (pointer)

Session pick steps live in `01_skill-integration/SKILL.md` (thin) + `references/session-pick.md` / `references/lifecycle-cache.md`.

Order: `ask-each-run` fine-id pick → resolve against `registry.yaml` (in-repo `NN_slug/base/`) → empty path: notify, re-search, confirm.
