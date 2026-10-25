# Manuscript local QC (standards checklist; gate authority = 00)

**Prior path:** former `personal/qc/local-checks.md` under 05_manuscript (moved 2026-10-18 into domain `qc/`).
**Gate / scoring authority:** `00_orchestrator` (Gate · 05 / Integrity · pre-06). This file is a **standards checklist** invoked by 00; seats execute but do **not** self-certify. 05 keeps only pointers in `route.md` / `handoff.md`.
**Owner (file seat):** `05_manuscript` (checklist body); gate pass/fail = 00.

---

﻿# Local QC checklists (Gate → 00)

## Part A — Introduction scorecard

## Introduction scorecard

> **QC routing:** Formal Gate/scoring ownership: `00_orchestrator`. This file is the 05 local checklist.


**Owner (checklist body):** `05_manuscript`. Use as a self-check after drafting and as an independent score before submission. A drafter's own score is provisional; **final Gate / scoring authority = `00_orchestrator`** (seats do not self-certify).

Seven dimensions, 0–10 each, total 70. Start every dimension at 10, apply the deductions below, floor at 0, then apply the caps. Write the deduction codes next to each score.

| # | Dimension | Question |
|---|---|---|
| 1 | Logic | Does each paragraph follow from the last, under one endpoint frame? |
| 2 | Fluency | Does it read as one argument, without listing or repeated frames? |
| 3 | Citation use | Does each literature claim have the right source, verified to the right level? |
| 4 | Prior results | Are the main results of the most relevant studies stated and appraised? |
| 5 | Gap | Is the gap a specific unknown, traceable to the guideline, with what the evidence already shows? |
| 6 | Method link | Could this study's method plausibly address the gap, and does the text say why? |
| 7 | Aim and hypothesis | Are aim, endpoint, set, and comparator explicit and testable? |

### Deduction codes

| Code | Dim | Trigger | Deduct | Fix at writing time |
|---|---|---|---|---|
| LOG-1 | 1 | The Introduction frames a guideline construct, but the aim or Methods name a different endpoint and no clause says how they relate | 1.5 | Fix the frame first: element 2 states the construct, element 6 names the endpoint, one clause states the relation; algorithm details stay in Methods |
| LOG-2 | 1 | A sentence sits where it does for citation numbering or for a writing standard (TRIPOD) rather than for the argument | 1 | Claim–source fit outranks numbering; renumber by script; no reporting standards in the Introduction |
| LOG-3 | 1 | A paragraph reports studies one after another with no group appraisal | 1.5 | One or two sentences: the strength this study keeps, the weakness it targets |
| FLU-1 | 2 | Three or more sentences in a paragraph open with the same words or the same frame | 2 | Change the subject and the structure; put the number inside a comparison |
| FLU-2 | 2 | A run of three sentences that each carry a number and a citation | 1 | Merge into one comparative sentence, or drop the weakest |
| FLU-3 | 2 | More than 10% of sentences outside 10–30 words | 1 per 10%, max 3 | Split or merge |
| FLU-4 | 2 | IMRAD body laid out as one sentence per line or one sentence per paragraph | 2 | Keep short sentences inside a continuous paragraph (`voice-portrait.md` paragraph lock) |
| CIT-1 | 3 | A literature claim with no citation in its sentence or its same-source group | 1 per 2 claims | Cite, weaken, or delete (`05_manuscript/personal/process/evidence.md`) |
| CIT-2 | 3 | More than 15 references without a recorded ranking, or an incomplete entry (volume, pages, DOI) | 1 | Budget before drafting; complete the entry |
| CIT-3 | 3 | Numbers verified below L2, or a guideline definition or appraisal verified below L3 | 1 | Read the full text, or weaken to "reported" |
| CIT-4 | 3 | No retraction and correction check on the reference list | 1 | Run it |
| CIT-5 | 3 | Introduction opening paragraph has no citation although a verified source for that claim exists | 2 | Cite the evidence-pack source; element 6 stays uncited |
| CIT-6 | 3 | Consecutive sentences cite the same paper without a new claim that paper supports | 1 | Cite once, or add the distinct claim |
| CIT-7 | 3 | DOI, author list, year, or volume copied from another manuscript, or a year/volume change without a source check | 2 | Verify against the work before keeping the entry |
| RES-1 | 4 | Only favourable results are reported | 1.5 | Include one weaker or limited result if one exists |
| RES-2 | 4 | Fewer than two of the three result classes covered, or the search log lacks a second source | 1.5 | Raise `missing_prior_result`; log the search |
| GLD-1 | 5 | Element 2 is missing, cites a superseded edition, or the gap is not traceable to the guideline | 2 | Raise `guideline_definition`; mine the open issue |
| GAP-1 | 5 | A scarcity claim with no logged search | 1 | Raise `scarcity_check` |
| GAP-2 | 5 | A field-wide statement drawn from one study | 1 | Write "in the studies we identified", or find a second |
| GAP-3 | 5 | The gap does not say what existing evidence already shows | 1 | State the settled part, then the unknown |
| MET-1 | 6 | No map from gap to method to expected benefit to measured output | 2 | Keep the map in the comment; one hedged sentence in the text |
| MET-2 | 6 | The method is said to solve the gap (*solves*, *overcomes*, *resolves*) | 2 | *may address part of* |
| MET-3 | 6 | The link rests on an assertion with no support and no hedge | 2 | Add a supporting source, or word it as inference |
| AIM-1 | 7 | The endpoint origin is not stated in one clause when it differs from the guideline construct | 2 | See LOG-1 |
| AIM-2 | 7 | The hypothesis has no set or no comparator | 2 | Name the test set and the comparator |
| AIM-3 | 7 | The endpoint name differs between Abstract, Methods, and Introduction | 1 | One name |

### Caps

- No quantified prior result: dimension 4 ≤ 3
- No explicit gap sentence: dimension 5 ≤ 4
- No hypothesis: dimension 7 ≤ 3
- A number in the Introduction that does not match its source: dimension 3 ≤ 4, and stop for correction
- Opening paragraph uncited when a verified source exists: dimension 3 ≤ 5

### Procedure

1. Run the Introduction lint (`humanize`) and keep its table as evidence for FLU and CIT-1.
2. Score each dimension and write the codes.
3. The scorer is not the drafter: a different mount (`simulate-reviewers`, isolated) or the user. A drafter's score is labelled *provisional*.
4. Record the date, manuscript, scorer, and the scores with codes.

### Record: Risk manuscript, first rewrite (2026-09-19, provisional, self-check)

Logic 6 (LOG-1, LOG-2, LOG-3) · Fluency 7 (FLU-1, FLU-2) · Citation use 7 (CIT-2, CIT-3, CIT-4) · Prior results 7 (RES-1, RES-2) · Gap 7 (GAP-1, GAP-2, GAP-3) · Method link 6 (MET-1, MET-3) · Aim 8 (AIM-1) · total 48/70.

The 25% sentence-level uncited gate used at that time is replaced by claim coverage (`05_manuscript/personal/process/evidence.md`). Re-scored with GLD-1 (the rewrite cited the 2016 consensus, not the latest guideline): Gap 5, total 46/70.


---

### Part B — Pre-submit consistency

> **QC routing:** Formal Gate ownership: `00_orchestrator`. This file is the 05 local pre-submit checklist.

---
name: pre-submit-consistency
owner: 05_manuscript
audience: Aitee
role: writing
on_number_conflict: comment_only
checks:
  - id: stat_vs_threshold
    class: stats_text
  - id: correlation_implied_n
    class: stats_text
  - id: multiplicity_disclosure
    class: stats_text
  - id: relative_denominator
    class: stats_text
  - id: overlap_statement_and_citation
    class: cross_manuscript
  - id: shared_table_sample_overlap
    class: cross_manuscript
  - id: sister_paper_p_reconciliation
    class: cross_manuscript
  - id: no_confirmatory_p_same_cohort
    class: circular_analysis
  - id: nested_roi_collinearity
    class: circular_analysis
  - id: score_transform_identity
    class: circular_analysis
  - id: pipeline_tokens_banned
    class: process_language
  - id: source_attribution_banned
    class: process_language
  - id: placeholder_and_internal_labels_banned
    class: process_language
  - id: agent_disclaimer_and_incomplete_claims_banned
    class: process_language
  - id: repeated_disclaimer
    class: process_language
  - id: empty_retrieval_and_scan_placeholders
    class: process_language
  - id: cutoff_vs_included_distribution
    class: inclusion_scale
  - id: iqr_scale_sanity
    class: inclusion_scale
  - id: consecutive_same_cite
    class: citation_hygiene
  - id: claim_matches_source
    class: citation_hygiene
  - id: no_unverified_cross_copy
    class: citation_hygiene
  - id: year_volume_from_source
    class: citation_hygiene
  - id: paragraph_lock
    class: writing_craft
  - id: intro_opening_has_citations
    class: writing_craft
  - id: split_names_are_sets
    class: writing_craft
  - id: approach_not_framework
    class: writing_craft
---

## Pre-submit consistency (Aitee)

Load on every full-paper draft, polish, and house.docx pass, after `Aitor-format.md` and `voice-portrait.md`.

Target-journal AI-use disclosure: check the author instructions and match any required AI statement (or confirm the journal asks for none).

Statistical definitions live in `02_data-processing/qc/report-checks.md` and the checkbox list in `02_data-processing/qc/report-checks.md`. Lee's annotation protocol lives in `06_review/qc/cross-manuscript-qc.md`.

Citation rows below are writing actions only. call/require 03 citation-verify — do not self-certify lit (`03_research/personal/citation-verify.md`).

**Number conflict:** Word comment, author **A**. Do not choose a replacement *n*, *P*, *t*, cutoff, quartile, or overlap count. A back-calculated critical value, implied *n*, or adjusted *P* may appear in a comment only if it is labeled an estimate. It does not enter the manuscript.

Split names stay **training set / test set / validation set**.

### Checks

#### stat_vs_threshold

A reported *t*, *F*, or *z* must be compatible with the voxel-wise or cluster-forming threshold named in Methods (same α, same df or approximation the paper claims). A statistic that only meets a looser α contradicts the threshold sentence. Flag both loci. Do not rewrite either number.

#### correlation_implied_n

The *n* implied by a reported *r* or ρ and its *P* must match the *n* of that analysis (the analyzed subset, not an enrollment total from another sentence). Recompute the two-sided *P* from *r* and the stated *n*, or invert *n* when the paper omits it. Disagreement beyond rounding means the stated *n* is not the analysis *n*. Say so in a comment. Do not invent a complete-case *n*.

#### multiplicity_disclosure

A family of ROI-wise or voxel-wise correlations states the family size and the correction (FWE, FDR, Holm, Bonferroni) or is labeled uncorrected and exploratory. Silence is a fail. Do not apply a correction the paper did not run.

#### relative_denominator

Any quantity called relative, normalized, ratio, or scaled names its denominator in Methods before Results interpret the spread (global mean, reference region, cerebellar value, or the real divisor). Units of the reported values are stated. An undefined "relative" measure is not interpretable. Comment; do not guess the divisor.

#### overlap_statement_and_citation

Same hospital, same scanner, or the same ethics approval as another lab paper: Methods contains one explicit overlap sentence (no shared participants, partial overlap, or overlap not yet quantified) and cites the sister paper. Unknown counts stay unknown in a comment. Do not invent overlap counts. Missing the sentence is a split-publication risk.

#### shared_table_sample_overlap

A table reused with the same cells in another manuscript is evidence of shared participants until the overlap sentence says otherwise. Write the overlap sentence. Do not leave the table looking independent.

#### sister_paper_p_reconciliation

The same biomarker and contrast with a materially different *P* or effect in a sister paper needs a reconciliation note (different *n*, covariates, threshold, or subset) or a comment that the conflict is unresolved. Do not average the *P* values or silently keep one.

#### no_confirmatory_p_same_cohort

Feature or ROI selection, threshold or cutoff selection, and the group or performance test on the same participants, without an outer nested cross-validation or a bootstrap optimism correction, do not support a confirmatory *P*. Write the result as apparent or descriptive. Do not write "confirmatory", "independently validated", or an unqualified "significantly different" for that test. Lab nested CV is not implemented (`02_data-processing/personal/analysis/pipeline.md`). Do not write that nested CV was run unless the user confirms it.

#### nested_roi_collinearity

Parent regions and their subregions in one model or one uncorrected family are not independent tests. Name the nesting and the dependence. Do not report them as separate confirmatory findings.

#### score_transform_identity

If a named score is a linear or other transform of a single metric, the same sentence says so and gives the transform. The score is not a second biomarker and does not get its own confirmatory test. An undefined score name is a comment, not a new construct.

#### pipeline_tokens_banned

Final body and figure legends do not contain pipeline tokens (`TRAIN_RATIO`, `VAL_MODE`, `settings.ini` keys, internal column codes). Write the procedure in words, or comment if the value is unknown.

#### source_attribution_banned

Final prose does not say "as stated by the source", "according to the HTML", or "the source says". State the fact. The lab file stays off the page.

#### placeholder_and_internal_labels_banned

Final prose does not contain 待补, 待补充, TBD, XX, bracketed parameter slots, or internal QC labels such as 标签未与方案核对. Missing facts become a Word comment (author **A**).

#### agent_disclaimer_and_incomplete_claims_banned

Agent-added disclaimers, placeholders, or internal notes never enter the manuscript body or a response letter. Banned strings include `Do not invent…`, `We did not invent…`, `cannot_invent`, `Undecidable pending source`, `will supply from source`, `pending source`, `not in the current files`, and figure/table placeholders such as `[Figure N near here]`.

**Process-negation / disclaimer / CYA / incompleteness (owner 2026-10-21; compose AL-5):** 「某某未做」「我们未做」「未进行…」, *not performed* / *we did not* / *was not done*, and similar hedges that flag work not done **must not appear in 正文**. Same rule for response-letter body and revised manuscript body. Such language may appear **only** in Word 批注 (author **A**), and every such 批注 **must** include **建议修改后内容** (suggested revised body wording)—not a bare flag. Fail → remove from body / move to comment with rewrite (`05_manuscript/qc/anti-leak-placeholders.md` AL-5).

Agent must not add new negative gap lists either (`was not tested / measured / examined / included …`). A verifiable negative fact already present in the user's Methods or Limitations may stay. Unresolved items go to a Word comment (author **A**), with an English sentence starting `Suggested …` that supplies the preferred body wording.

#### layout_priority

Layout order: the user's instruction this run, then the target journal guide, then `05_manuscript/personal/Aitor-format.md` defaults. Paragraphs stay as paragraphs; new paragraphs only on topic change. Abstract labels, Methods/Results subheads, Highlights, and figure/table notes keep their format.

#### repeated_disclaimer

The same disclaimer or limitation sentence appears once. A second copy in the body or a legend is a fail. Collapse to one locus. Prefer **no** disclaimer/CYA/未做-class language in 正文 at all (AL-5 / `agent_disclaimer_and_incomplete_claims_banned`): if it must be recorded, one Word 批注 with suggested rewrite—not repeated body hedges.

#### empty_retrieval_and_scan_placeholders

A search sentence names the databases and the actual query. An empty query, `""`, `[query]`, or 待补 is unfinished. Do not invent the query. Scanner and sequence parameters that the modality needs (vendor, field strength, sequence, timing, resolution, or the real list) are values from the protocol or a comment. "Standard protocol" does not replace them.

#### cutoff_vs_included_distribution

State the direction of each entry cutoff. Median, first quartile, and minimum of each included group must sit on the included side of that cutoff. A summary on the excluded side is a contradiction. Flag the cutoff sentence and the table cell. Do not change either number.

#### iqr_scale_sanity

IQR (Q3−Q1) lies inside the instrument's possible range. An IQR wider than the scale, or a quartile that contradicts the cutoff, is a comment. Do not replace the quartile.

#### consecutive_same_cite

Do not cite the same paper in consecutive sentences unless the second sentence adds a distinct claim that paper supports. Neighbouring sentences that share one source cite once (`citation-and-language.md`).

#### claim_matches_source

The sentence's claim (population, modality, direction of effect) is a claim the cited work makes. A mismatch is weaken or replace via `05_manuscript/personal/process/evidence.md`, not a decorative citation.

#### no_unverified_cross_copy

A DOI, author list, year, or volume copied from another manuscript is not verification. Each entry is checked against the work (`03_research` / verify-refs) before it stays.

#### year_volume_from_source

A year or volume correction is applied only after the source confirms it. An unverified "correction" stays a comment.

#### paragraph_lock

One fact per sentence is allowed. Related sentences stay in the same paragraph. IMRAD body is not one sentence per line and not one sentence per paragraph. Abstract labels, Methods and Results subheadings, Highlights, and table or figure notes keep `Aitor-format.md`.

#### intro_opening_has_citations

The Introduction opening paragraph cites when a verified source exists for that claim. Zero citations there is a fail. Element 6 (aim / hypothesis) stays uncited. Discussion first paragraph stays uncited.

#### split_names_are_sets

Internal splits are the **training set**, the **test set**, and, when external, the **validation set**. Do not rename them as groups.

#### approach_not_framework

Vague methodological "framework" is "approach" (`vocab/L1/ban-phrases.md`). A named software library may keep its own name.
