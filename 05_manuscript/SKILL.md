---
name: medical-scientific-writing
description: >
  Personal SCI original-article prose layer (Ying Li / Aitor-format / de-AI / pre-submit consistency).
  Triggers: 润色, 去AI, de-AI, 写论文, 引言, Discussion, Aitor-format, 投稿前一致性.
  Mounted writing skills supply generic capability; this layer is the personal upper
  layer and final wording authority. Literature research → 03. Figures → 04.
  Reviewer response → 06. Do not use for 评阅 or 回复审稿人.
---

# Scientific Writing — personal upper layer

## Purpose

Convert **validated** research information into precise, publication-ready original-article prose.
**Never invent** sample sizes, P values, effects, CIs, procedures, ethics IDs, citations, or claims.

Ownership: see `00_orchestrator/references/ownership-contract.md`. Decidable issues from 06: Lee annotates for Aitee to TC-fix; 05 applies those Track Changes. Apply Track Changes only after the user picks on undecidable issues.

**Lab priority:** data truth > journal format > Ying Li voice > generic ornate English.

**Every SCI full paper uses `personal/Aitor-format.md` as the only Aitor-format.** If a rule is unclear, **ask the user**. Do not invent a second format.

## Layer model

**Mounted writing capability → 05 personal upper layer → 00 Final QC.**

## Personal assets

| Task | Path |
|---|---|
| Aitor-format | `personal/Aitor-format.md` |
| Voice portrait | `personal/voice-portrait.md` |
| Route | `personal/route.md` |
| Handoff (other skills) | `personal/handoff.md` |
| L1 / L2 / L3 vocabulary | `personal/vocab/` |
| Lab-STE (CM-01 ZH comments) | `personal/vocab/L3/lab-ste.md` |
| Process (evidence / citation / polish) | `personal/process/` |
| Manuscript QC checklists | `00_orchestrator/references/manuscript-local-qc.md` (owned by 00) |
| Diff harvest | `{script_write_paper}\diff_harvest.py` |


## Mounted capability ids (generic; not present until mounted)

**This-run pick:** do not load any mounted id until 01 session-mount pick is confirmed for this run. Registry `MOUNTED` = available, not attached.

- `write-paper` — manuscript/report draft. Not Aitor-format. `clinical-reports` is not this id.
- `check-reporting` — TRIPOD / CLAIM / CLEAR in the paper
- `venue-templates` — journal templates / house style while writing. Not journal selection / 选刊.
- `polish-language` — generic academic English. Not de-AI.
- `humanize` — generic de-AI / humanize (B `05-manuscript/humanize/`). Does **not** replace `personal/route.md` + `personal/vocab/L1/ban-phrases.md`.

选刊走 03 `find-journal`；`venue-templates` 只管体例. Personal de-AI stays in A (`personal/`).

## Figures

**Figures → `04_analysis`** (mounted `plot-figures` / `draw-flowchart`, + `04_analysis/personal/figures.md`). 05 writes captions and body callouts; it does not own the figure pack.

## Literature

Literature search/evidence retrieval for Introduction/Discussion is executed through `03_research`. 05 consumes verified evidence (`personal/process/evidence.md`) and applies Aitor quotas. Mounted packs may only raise an Evidence Request card (`personal/process/evidence.md`); they do not choose the final citation. A 05 personal owns Accept / Weaken / Delete after 03 returns candidates. Before the deliverable is done, call/require 03 citation-verify — do not self-certify lit (`03_research/personal/citation-verify.md`). 选题 stays in 03 (`find-cohort-gap`; hypothesis framing via `frontier-hypothesize`). 选刊 / where to submit → `03_research` (`personal/journal-selection.md`); not this skill.

**Introduction handoff.** For each endpoint 05 raises the four Introduction cards (`guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`). 03 answers with an Evidence Pack (`03_research/personal/intro-evidence-pack.md`). 05 drafts elements 2–5 only after every card has an exit. Reporting guidelines (TRIPOD and others) are writing standards and stay out of the Introduction. Independent scoring uses `00_orchestrator/references/manuscript-local-qc.md`.


## Core rule

Write from evidence and supplied results. Missing info → Word comment (author **A**); never yellow fill; never invent.

## Lab voice (Ying Li) — summary

- Highly standardized · clinically oriented · quantitatively precise · objectively cautious
- Numbers attached to claims (`n`, AUC, 95% CI, *P*)
- Observational → avoid causal overclaim (*associated with*)
- Forbidden fluff: `personal/vocab/L1/ban-phrases.md`
- Prediction-model full papers: patient-level split (training / test; validation set = external only); dual-set main metrics; LASSO+RadScore formula in prose; `95% CI: X–X`; no em-dash punctuation; Vancouver+DOI as required

Word counts, citation placement, typography, and Table 1 layout live only in **`personal/Aitor-format.md`**. If that file and any other note disagree, `personal/Aitor-format.md` wins.

## Not this skill

- Pre-submission / 模拟审稿 / 评阅 → `06_review`
- Response letter / 回复审稿人 → `06_review`
- Statistics / figures → `04_analysis`
- Literature landscape / 选刊 / where to submit → `03_research` (`personal/journal-selection.md`)


## Internal calls (not entry points)

05 personal may request siblings via `00_orchestrator/templates/handoff.yaml`. Do not silently edit other skills' files.

- Literature / 选刊 / evidence → `03_research`
- Numbers / figures → `04_analysis`
- Tables / imaging prep → `02_data-processing`
- Pre-review / response entry → `06_review`
- Cross-skill or exit QC → `00_orchestrator` decides whether to invoke

## Edit unit and comments

- Ownership: see `00_orchestrator/references/ownership-contract.md`. When 06 marks a decidable fix, apply Track Changes here.
- Revise at **word or sentence** unit. Never rewrite a whole paragraph to satisfy one comment.
- Do **not** change Word format on an existing `.docx`. If a sentence differs from the last agent wording, ask the user; do not restore the old sentence. HTML / PDF / scripts are out of scope (`06_review/personal/word-edit.md`).
- After a 05/06 Word pass, append the project `ref/manuscript-revision.md`. Do not re-polish logged sections.
- Word comments: author **A**, never yellow. Tag source (`[A:personal]`, `[B:polish-language]`, …).
- Mount advice vs lab rules: put conflict + before/after sentence in the comment; **user decides** before applying.
- Literature verify fail: follow `personal/process/evidence.md` exits when a card exists; always comment with G-LIT dual plan (revise/weaken/delete sentence; keep sentence + ask 00 whether to call 03 for substitute refs). Do not invent citations.
- **New citation numbers:** before inserting `[n]`, scan the manuscript for existing `[digits]`, take `max + 1`, and confirm the new `n` is unused (grep). Never reuse a number that already points at another paper. When swapping a ref, do not copy the old paper’s unique numbers into the new paper.

## Writing QC (domain)

terminology · tense · numbers match sources · no unsupported causality · abbreviations at first use · figure/table cites · refs coherent · abstract matches main text · de-AI ban list clean · Aitor-format QC · `00_orchestrator/references/manuscript-local-qc.md` (comment number conflicts; no pipeline tokens or placeholders in final prose)

Overall Final QC and local recovery are owned by `00_orchestrator`.
