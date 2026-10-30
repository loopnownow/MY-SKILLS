---
name: medical-scientific-writing
description: >
 Advanced SCI original-article prose layer (Aitor / Aitor-format / de-AI / pre-submit consistency).
 Triggers: 润色, 去AI, de-AI, 写论文, 引言, Discussion, Aitor-format, 投稿前一致性.
 Live writing skills supply generic capability; this layer is the advanced upper
 layer and final wording authority. Literature research → 03. Figures → 02.
 Reviewer response → 07. Do not use for 评阅 or 回复审稿人.
---

# Scientific Writing — advanced upper layer

## Purpose

Convert **validated** research information into precise, publication-ready original-article prose.
**Never invent** sample sizes, P values, effects, CIs, procedures, ethics IDs, citations, or claims.

Ownership: see `00_orchestrator/references/ownership-contract.md`. Decidable issues from 06: Lee annotates for Aitee to TC-fix; 05 applies those Track Changes. Apply Track Changes only after the user picks on undecidable issues.

**Lab priority:** data truth > journal format > Aitor voice > generic ornate English.

**Every SCI full paper uses `advanced/Aitor-format.md` as the only Aitor-format.** If a rule is unclear, **ask the user**. Do not invent a second format.

## Layer model (2026-10-30 rebind)

**Flow:** base thin-contract first pass (`05_manuscript/base/`: scope, bans, phase names, pointers) -> **00 QC** (score, cite the advanced anchor) -> post-QC revise **via `05_manuscript/advanced/`** -> re-gate at 00.
Layering and `qc/` invocation SSOT: `00_orchestrator/references/base-vs-advanced-top-loops.md`. Gates: `00_orchestrator/gates.md`. Checks: `qc/README.md`.

| Layer | Owns |
|---|---|
| `base/` | Thin contract: `write-paper` scope + bans; vocab data under `05_manuscript/base/vocab/`. De-AI contract+procedure: `advanced/process/polisher-sections.md` section De-AI pass (absorbed retired `humanize`) |
| `qc/` | `check-reporting/` at `qc/check-reporting/` (TRIPOD / CLAIM / CLEAR; qc-only, not a registry fine id); scorecards and deduction codes that cite advanced anchors |
| 00 | Final QC |
| `advanced/` | Every recipe: Aitor-format beats/bands/typography, voice, de-AI procedure, evidence and citation protocol; final wording authority |

## Advanced assets

| Task | Path |
|---|---|
| Aitor-format | `advanced/Aitor-format.md` |
| Voice portrait | `advanced/voice-portrait.md` |
| Route | `advanced/route.md` |
| Handoff (other skills) | `advanced/handoff.md` |
| L1 / L2 / L3 vocabulary | `05_manuscript/base/vocab/` (`advanced/vocab/` = advanced L1 overrides + L2 advanced table) |
| Lab-STE (CM-01 ZH comments) | `05_manuscript/base/vocab/L3/lab-ste.md` (`05_manuscript/advanced/vocab/` = overrides only) |
| Process (evidence / citation / polish) | `advanced/process/` |
| Manuscript QC checklists | `qc/manuscript-local-qc.md` (invoked only by 00) |
| Diff harvest | `{code_write_paper}\diff_harvest.py` |


## Live capability ids (bodies in `05_manuscript/base/`; reporting checks under `qc/` are qc-only, not a registry fine ids)

**This-run pick:** do not load any live id until the 00 session-fine-id pick is confirmed for this run. Registry `LIVE` = available, not attached.

- `write-paper` — manuscript/report draft and journal templates / house style while writing (`05_manuscript/base/write-paper/`). Not journal selection / 选刊. Not Aitor-format. `clinical-reports` is not this id.
- Reporting checks (absorbed retired fine id `check-reporting`): `05_manuscript/qc/check-reporting/` (TRIPOD / CLAIM / CLEAR). Not session-picked; Gate G-05 loads via `qc/`.
- De-AI / language lint (absorbed retired `humanize`): `05_manuscript/advanced/process/polisher-sections.md` section De-AI pass. Report-only Intro/Discussion lint, then the de-AI pass. Not venue house style (that is `write-paper`); does **not** replace `advanced/route.md` + `05_manuscript/base/vocab/L1/ban-phrases.md`. Not a registry fine id.

选刊 → 03 `find-journal`; house style → `05_manuscript/base/write-paper/`. Advanced de-AI stays in A (`advanced/`).

## Figures

**Figures → `02_data-processing`** (live `plot-figures` / `draw-flowchart`, + `02_data-processing/advanced/analysis/figures.md`). 05 writes captions and body callouts; it does not own the figure pack.

## Literature

Literature search/evidence retrieval for Introduction/Discussion is executed through `03_research`. 05 consumes verified evidence (`advanced/process/evidence.md`) and applies Aitor quotas. Live packs may only raise an Evidence Request card (`advanced/process/evidence.md`); they do not choose the final citation. A 05 advanced owns Accept / Weaken / Delete after 03 returns candidates. Before the deliverable is done, call/require 03 citation-verify — do not self-certify lit (`03_research/advanced/citation-verify.md`). 选题 stays in 03 (`find-journal` / `design-study` for question framing). 选刊 / where to submit → `03_research` (`03_research/advanced/journal-selection.md`); not this skill.

**Introduction handoff.** For each endpoint 05 raises the four Introduction cards (`guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`). 03 answers with an Evidence Pack (`03_research/advanced/intro-evidence-pack.md`). 05 drafts elements 2-5 only after every card has an exit. Reporting guidelines (TRIPOD and others) are writing standards and stay out of the Introduction. Independent scoring uses `05_manuscript/qc/manuscript-local-qc.md`.


## Core rule

Write from evidence and supplied results. Missing info → Word comment (author **A**); never yellow fill; never invent.

## Lab voice (Aitor) — summary

- Highly standardized · clinically oriented · quantitatively precise · objectively cautious
- Numbers attached to claims (`n`, AUC, 95% CI, *P*)
- Observational → avoid causal overclaim (*associated with*)
- Forbidden fluff: `05_manuscript/base/vocab/L1/ban-phrases.md`
- Prediction-model full papers: patient-level split (training / test; validation set = external only); dual-set main metrics; LASSO+RadScore formula in prose; `95% CI: X-X`; no em-dash punctuation; Vancouver+DOI as required

Word counts, citation placement, typography, and Table 1 layout live only in **`advanced/Aitor-format.md`**. If that file and any other note disagree, `advanced/Aitor-format.md` wins.

## Not this skill

- Pre-submission / 模拟审稿 / 评阅 → `06_review` (response -> `07_response`)
- Response letter / 回复审稿人 → `07_response`
- Statistics / figures → `02_data-processing`
- Literature landscape / 选刊 / where to submit → `03_research` (`03_research/advanced/journal-selection.md`)


## Internal calls (not entry points)

05 advanced may request siblings via `00_orchestrator/templates/handoff.yaml`. Do not silently edit other skills' files.

- Literature / 选刊 / evidence → `03_research`
- Numbers / figures → `02_data-processing`
- Tables / imaging prep → `02_data-processing`
- Pre-review / response entry → `06_review` (response -> `07_response`)
- Cross-skill or exit QC → `00_orchestrator` decides whether to invoke

## Edit unit and comments

- Ownership: see `00_orchestrator/references/ownership-contract.md`. When 06 marks a decidable fix, apply Track Changes here.
- Revise at **word or sentence** unit. Never rewrite a whole paragraph to satisfy one comment.
- Do **not** change Word format on an existing `.docx`. If a sentence differs from the last agent wording, ask the user; do not restore the old sentence. HTML / PDF / scripts are out of scope (`06_review/advanced/word-edit.md`).
- After a 05/06 Word pass, append the project `ref/manuscript-revision.md`. Do not re-polish logged sections.
- Project `ref/` subfolders: follow `00_orchestrator/references/project-ref-layout.md` (keep manuscript-revision + settings.ini at root).
- Word comments: author **A**, never yellow. Tag source (`[advanced]`, `[advanced:de-AI]`, …).
- Fine id advice vs lab rules: put conflict + before/after sentence in the comment; **user decides** before applying.
- Literature verify fail: follow `advanced/process/evidence.md` exits when a card exists; always comment with G-LIT dual plan (revise/weaken/delete sentence; keep sentence + ask 00 whether to call 03 for substitute refs). Do not invent citations.
- **New citation numbers:** before inserting `[n]`, scan the manuscript for existing `[digits]`, take `max + 1`, and confirm the new `n` is unused (grep). Never reuse a number that already points at another paper. When swapping a ref, do not copy the old paper’s unique numbers into the new paper.

## Writing QC (domain)

terminology · tense · numbers match sources · no unsupported causality · abbreviations at first use · figure/table cites · refs coherent · abstract matches main text · de-AI ban list clean · Aitor-format QC · `05_manuscript/qc/manuscript-local-qc.md` (comment number conflicts; no pipeline tokens or placeholders in final prose)

Overall Final QC and local recovery are owned by `00_orchestrator`.
