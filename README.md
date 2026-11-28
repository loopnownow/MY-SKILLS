# MY-SKILLS

Live medical and imaging research skill library. Seats `00`, `02`, `03`, `05`, `06`, and `07` are stable ids, not a sequence.

## Three repositories

| Repo | Holds | Does not hold |
|---|---|---|
| **MY-RULES** | Standing operating policy: layout, delivery destinations, no-build zones, network red lines, skill-library contract | Professional skill bodies, runnable code |
| **MY-SKILLS** (this repo) | Professional skills: `NN_slug/base/` capability bodies + `advanced/` revision layer (voice, habits, confirmed methods) + `qc/` gate standards (**prose SSOT**). Seats and `00_orchestrator` may keep **thin helpers** under `**/scripts/` | Heavy analysis or cleaning code; patient data |
| **MY-CODES** | Runnable code: `modules/` plus modeling/validation CLIs plus `tools/` — the 02 scripting half | Skill prose; project config; patient data |

Rule of thumb: frequently used operating policy goes in RULES, professional skills go in SKILLS, heavy or reusable analysis goes in MY-CODES / `{code_root}`.
This repo treats prose as SSOT. Thin helpers (lint, flowchart drawer, citation check, viz generator) may live under seat `**/scripts/` and `00_orchestrator/scripts/`. Heavy analysis, cleaning, and modeling CLIs are cited only as path aliases (`{code_stats}` / `{code_modules}` / `{code_model_validation}` / `{code_root}`); this repo does not vendor those trees.
`{RULES}\skills.md` governs how this repo is changed (propose-only + PR). `{RULES}\My rule.md` is the global priority policy.

## Seats

| Seat | Folder | Role |
|------|--------|------|
| 00 orchestrator | `00_orchestrator` | Intent, skill chain, QC closed loop; registry / index / session-pick |
| 02 data-processing | `02_data-processing` | Raw → analysis-ready; Excel and batch workspace; imaging prep; extraction; coding principles; statistics, prediction, figures (`draw-flowchart` / `plot-figures`) |
| 03 research | `03_research` | Study design, literature, journal selection, grants, ethics forms |
| 05 manuscript | `05_manuscript` | Scientific writing and de-AI |
| 06 review | `06_review` | Peer review (Lee) |
| 07 response | `07_response` | Reviewer response (Aitee) |

Capability bodies for seats 02-07 live in-repo under `NN_slug/base/`. The routing index is `00_orchestrator/registry.yaml`. Lab path aliases (`{code_root}`, `{doc_root}`, `STATS_ROOT`, and the rest) are in `00_orchestrator/references/lab-paths.yaml`. Heavy / reusable analysis stays on `{code_root}` (02 operations) and `{code_stats}` (stats engine + modeling CLIs); human docs stay on `{doc_root}`. This repo may keep **thin helper scripts** under seat `**/scripts/` and `00_orchestrator/scripts/`; it is not a vendor of the MY-CODES library.

Paths under the six seat roots (`00_orchestrator`, `02_data-processing`, `03_research`, `05_manuscript`, `06_review`, `07_response`) are at most five parts from the repo root, except `NN_slug/base/**`.

License: MIT (`LICENSE`). Third-party notices: `NOTICE`. Release notes: `CHANGELOG.md`. Version number: `VERSION.txt`.

Tests: `python -B -m pytest tests/` (or `unittest discover -s tests`; `-B` keeps `__pycache__` out; needs `pyyaml`).

## Architecture and handoff contract

Repo architecture lives here (skill layout, lab homes, fine-id ceiling, path rules). The three-layer contract (base / qc / advanced) is SSOT in `00_orchestrator/references/base-vs-advanced-top-loops.md`. Routing SSOT is `00_orchestrator/registry.yaml` — the **id SSOT**: ids, paths, statuses and counts are settled there.

**Specialist roster:** `00_orchestrator/registry.yaml` (`specialist_hint` on each coarse id). The only executor exception is `fill-protocol` → Bai. Do not maintain a separate bot-name table. Ownership (who may revise what) stays `00_orchestrator/references/ownership-contract.md`.

Live rules: A skill path at most five parts from repo root (exception: `NN_slug/base/**` for in-repo capability bodies); bodies are in-repo `my-skills` under `NN_slug/base/` (exception: the non-routable `check-reporting` body at `05_manuscript/qc/check-reporting/`); ethics in `03_research`; menu shape is `00_orchestrator/registry.yaml` (not `fine ids: []`; do not restate totals here); no separate `figure-engine` skill (figures are live fine ids `draw-flowchart` / `plot-figures`); `session_fine_id_pick: ask-each-run`; G-FACT consistency; harvest-qc passive. One fine id uses one in-repo path. Journal selection via 03 `find-journal`; venue style via `05_manuscript/base/write-paper/`. sample size: `calc-sample-size`.

## Skill selection

The orchestrator classifies the task and selects the **smallest** set of skills that can complete it.

| Intent | Route |
|---|---|
| Skill index / session pick | `00_orchestrator` |
| Excel / batch workspace / cleaning / imaging prep / impute / extraction / coding / scripts / MY-CODES | `02_data-processing` (Loopnow; default coding seat) |
| Literature research / evidence / study design / journal selection / citation-verify / translational design / ethics forms | `03_research` (Victor; ethics forms → **Bai**) |
| Statistics / prediction / **figures** / sample size | `02_data-processing` (Loopnow) |
| Scientific writing / advanced style / de-AI | `05_manuscript` (Aitee) |
| Peer review / re-review | `06_review` (Lee) |
| Reviewer response / response letter | `07_response` (Aitee) |
| Evolution governance | MY-RULES `{RULES}\skills.md` (skill-evolution) |

Grants (Voice A reviewing others' proposals / Voice B your own) is an advanced 03 path (`03_research/advanced/intake.md`), not a LIVE fine id.

## Lab-specific flows

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
| Library lookup / portal submit | **Bai** (routed off the 00 main loop; `03_research/advanced/docs-db.md`) |
| Clinical extraction (exported text) | `02_data-processing` → `02_data-processing/advanced/extract.md` |
| Translational / reader study | `03_research` → `clinical-translation/` |
| Journal-grade ROC/calibration/DCA figures | `02_data-processing` (`plot-figures`; palettes: `02_data-processing/base/plot-figures/references/lab-palettes.md`) |
| STROBE / patient-flow / Figure 1 | `02_data-processing` (`draw-flowchart`) |

## Final QC

`00_orchestrator` owns the QC closed loop: intent classify → skill chain → file check → integrity gate → local recovery. Completeness: deliverable exists; consistency checks pass; assumptions visible; limitations stated; files usable.

Detail: `00_orchestrator/gates.md`. Handoff schema: `00_orchestrator/templates/handoff.yaml`. State fields: `pipeline`, `qc`, `defects` in `project-state.yaml`.

Handoff payload when crossing skills: objective, inputs inspected, decisions, assumptions, completed outputs, exclusions, unresolved issues, required downstream actions.

**Local recovery:** if QC finds a localized defect, identify the responsible skill and send **only the erroneous portion** back. Max 3 rounds, then `unresolved`. Do not rerun already-correct stages.

`plan → execute node → file check → integrity gate → localized defect → responsible skill → re-run that node (max 3) → gate → output`

Interactive by default (plan card before multi-node dispatch). Prose repairs are word/sentence units. Assistant vs lab conflicts go to Word comments with an edit plan; the user decides. Lit-verify fail uses a dual plan; 00 decides whether to call 03.

## Ownership

Ownership: see `00_orchestrator/references/ownership-contract.md`. Requires 03 citation-verify (cannot skip). Lee owns statement then data consistency; lit accuracy is joint with Victor.

## Domain boundaries

Who executes a seat: `specialist_hint` on `coarse_ids` in `00_orchestrator/registry.yaml` (only exception: `fill-protocol` → Bai). Who may revise what: `00_orchestrator/references/ownership-contract.md`.

- `02_data-processing`: raw → analysis-ready → statistical analysis / model evaluation / figures (`draw-flowchart` / `plot-figures`). **Loopnow**. Coding / scripts / `MY-CODES` also default here: Loopnow is the default coding seat; local DeepSeek (DSH) and Cline take tidying / extraction / form-fill / local IDE work when the owner says so or approves, not as the coding default. Upstream data repair must remain traceable; do not silently modify upstream inputs during analysis. Ethics forms are not here.
- `03_research`: design, literature/evidence, ethics **forms** path (`fill-protocol` — `a_domain` `03_research` but **executor Bai**, the one route exception), translational design, **journal selection**, **citation-verify** before 05 done and inside 06. **Victor is the default bot**; the ethics-form exception does not move the body out of 03. Manuscript prose is not its role. Victor does not fill ethics forms.
- `05_manuscript`: advanced writing layer (**Aitee**). Literature retrieval and journal selection → `03_research`; figures → `02_data-processing`. de-AI at `05_manuscript/advanced/`. Mid-entry does not waive citation-verify.
- `06_review`: advanced review / re-review layer (**Lee**). Changed wording → `05_manuscript`.
- `07_response`: advanced response-letter layer (**Aitee**). Changed wording → `05_manuscript`. Tone-only polish is an on-demand mode of `tighten-response`. Point-by-point structure stays `revise`.

## Session pick

Session pick steps live in `00_orchestrator/SKILL.md` (§0 registry) + `00_orchestrator/references/session-pick.md`.

Order: `ask-each-run` fine-id pick → resolve against `registry.yaml` (in-repo `NN_slug/base/`) → empty path: notify, re-search, confirm.
