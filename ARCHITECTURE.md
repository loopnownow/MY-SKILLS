# Architecture and Handoff Contract

This file is **integration metadata**: lab intent tables, handoff/QC loop, and ownership phrases pinned by tests.

**Architecture SSOT** for this repo: this file (layers, lab homes, fine-id ceiling, base/advanced contract).

**Routing SSOT:** `00_orchestrator/registry.yaml` — the **id SSOT**: ids, paths, statuses and counts are settled there.

**Bot route SSOT:** `00_orchestrator/references/bot-route.md` — coarse id → bot and LIVE fine id → bot. Tables live there; this file names a bot only where a seat has a named specialist and does not duplicate the tables. Ownership (who may revise what) stays `00_orchestrator/references/ownership-contract.md`.

Live rules: A skill path at most five parts from repo root (exception: `NN_slug/base/**` for in-repo capability bodies); bodies are in-repo `my-skills` under `NN_slug/base/` (exception: `check-reporting` at `05_manuscript/qc/check-reporting/`); ethics in `03_research`; menu shape is `00_orchestrator/registry.yaml` (not `fine ids: []`; do not restate totals here); no separate `figure-engine` skill (figures are live fine ids `draw-flowchart` / `plot-figures`); `session_fine_id_pick: ask-each-run`; G-FACT consistency; harvest-qc passive. One fine id uses one in-repo path. Journal selection via 03 `find-journal`; venue style via `05_manuscript/base/write-paper/`. sample size: `calc-sample-size`.

---

## Skill selection

The orchestrator classifies the task and selects the **smallest** set of skills that can complete it.

| Intent | Route |
|---|---|
| Skill index / session pick | `00_orchestrator` (Aitor) |
| Excel / batch workspace / cleaning / imaging prep / impute / extraction / coding / scripts / MY-CODES | `02_data-processing` (Loopnow; default coding seat) |
| Literature research / evidence / study design / journal selection / citation-verify / translational design / ethics forms | `03_research` (Victor; ethics forms → **Bai**) |
| Statistics / prediction / **figures** / sample size | `02_data-processing` (Loopnow) |
| Scientific writing / advanced style / de-AI | `05_manuscript` (Aitee) |
| Peer review / re-review | `06_review` (Lee) |
| Reviewer response / response letter | `07_response` (Aitee) |
| Evolution governance | MY-RULES `{RULES}\skills.md` (skill-evolution) |

Grants (Voice A reviewing others' proposals / Voice B your own) is an advanced 03 path (`03_research/advanced/intake.md`), not a LIVE fine id.

### Lab-specific flows (Aitor)

| Intent | Route |
|--------|--------|
| Polish in my voice / SCI writing | `05_manuscript` (Aitee) |
| Write Introduction / Discussion (prose) | `03_research` retrieves (Victor); `05_manuscript` writes (Aitee) (`05_manuscript/advanced/process/evidence.md`) |
| Pre-submit find issues / dealbreaker | `06_review` (Lee) |
| Reply to reviewers | `07_response` only as entry (Aitee) |
| Topic / literature / journal selection | `03_research` (Victor) |
| Journal selection | `03_research` (`03_research/advanced/journal-selection.md`). Journal selection via 03 `find-journal`; venue style via `05_manuscript/base/write-paper/` |
| sample size | `02_data-processing` (`calc-sample-size`) |
| AUC / DeLong / DCA / stats plan / figures | `02_data-processing` (Loopnow) |
| Radiomics / ROI / leakage audit / preprocess | `02_data-processing` (Loopnow) |
| Soft coding / dry-run / scripts | `02_data-processing` (Loopnow, default coding seat) → `02_data-processing/advanced/coding.md` |
| Batch / Excel folders | `{RULES}/workspace-layout.md` |
| VAL_MODE / pairwise compare / subgroup ROC | `02_data-processing` → `02_data-processing/advanced/analysis/pipeline.md` |
| Ethics application form fill | `03_research` → `base/fill-protocol/` — **executor Bai** (`a_domain` `03_research`, the one route exception) |
| 0doc library lookup / portal submit | **Bai** (Aitor routes; off the 00 main loop; `03_research/advanced/0doc-db.md`) |
| Clinical extraction (exported text) | `02_data-processing` → `02_data-processing/advanced/extract.md` |
| Translational / reader study | `03_research` → `clinical-translation/` |
| Journal-grade ROC/calibration/DCA figures | `02_data-processing` (`plot-figures` + `{doc_root}\\_library\\figures\\lab-palettes.md`) |
| STROBE / patient-flow / Figure 1 | `02_data-processing` (`draw-flowchart`) |

---

## Final QC (handoff folded in)

`00_orchestrator` owns the QC closed loop: intent classify → skill chain → file check → integrity gate → local recovery. Completeness: deliverable exists; consistency checks pass; assumptions visible; limitations stated; files usable.

Detail: `00_orchestrator/gates.md`. Handoff schema: `00_orchestrator/templates/handoff.yaml`. State fields: `pipeline`, `qc`, `defects` in `project-state.yaml`.

Handoff payload when crossing skills: objective, inputs inspected, decisions, assumptions, completed outputs, exclusions, unresolved issues, required downstream actions.

**Local recovery:** if QC finds a localized defect, identify the responsible skill and send **only the erroneous portion** back. Max 3 rounds, then `unresolved`. Do not rerun already-correct stages.

`plan → execute node → file check → integrity gate → localized defect → responsible skill → re-run that node (max 3) → gate → output`

Interactive by default (plan card before multi-node dispatch). Prose repairs are word/sentence units. Assistant vs lab conflicts go to Word comments with an edit plan; the user decides. Lit-verify fail uses a dual plan; 00 decides whether to call 03.

---

## Ownership (pinned; agrees with ownership-contract; seats 05/06/07)

Ownership: see `00_orchestrator/references/ownership-contract.md`. Requires 03 citation-verify (cannot skip). Lee owns statement then data consistency; lit accuracy is joint with Victor.

---

## Domain boundaries (lab intent)

Who executes a coarse id or a LIVE fine id: `00_orchestrator/references/bot-route.md` (coarse|fine → bot). Who may revise what: `00_orchestrator/references/ownership-contract.md`.

- `02_data-processing`: raw → analysis-ready → statistical analysis / model evaluation / figures (`draw-flowchart` / `plot-figures`). **Loopnow**. Coding / scripts / `MY-CODES` also default here: Loopnow is the default coding seat, and Cursor takes coding only on 「交给cursor」. Upstream data repair must remain traceable; do not silently modify upstream inputs during analysis. Ethics forms are not here.
- `03_research`: design, literature/evidence, ethics **forms** path (`fill-protocol` — `a_domain` `03_research` but **executor Bai**, the one route exception), translational design, **journal selection**, **citation-verify** before 05 done and inside 06. **Victor is the default bot**; the ethics-form exception does not move the body out of 03. Manuscript prose is not its role. Victor does not fill ethics forms.
- `05_manuscript`: advanced writing layer (**Aitee**). Literature retrieval and journal selection → `03_research`; figures → `02_data-processing`. de-AI at `05_manuscript/advanced/`. Mid-entry does not waive citation-verify.
- `06_review`: advanced review / re-review layer (**Lee**). Changed wording → `05_manuscript`.
- `07_response`: advanced response-letter layer (**Aitee**). Changed wording → `05_manuscript`. Tone-only polish is an on-demand mode of `tighten-response`. Point-by-point structure stays `revise`.

---

## Session pick (pointer)

Session pick steps live in `00_orchestrator/SKILL.md` (§0 registry) + `00_orchestrator/references/session-pick.md` / `00_orchestrator/references/lifecycle-cache.md`.

Order: `ask-each-run` fine-id pick → resolve against `registry.yaml` (in-repo `NN_slug/base/`) → empty path: notify, re-search, confirm.
