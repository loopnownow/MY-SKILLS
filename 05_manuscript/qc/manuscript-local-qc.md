# Manuscript local QC (standards checklist; gate authority = 00)

**Prior path:** former `advanced/qc/local-checks.md` under 05_manuscript (moved 2026-10-18 into domain `qc/`).
**Gate / scoring authority:** `00_orchestrator` (Gate · 05 / Integrity · pre-06). This file is a **standards checklist** invoked by 00; seats execute but do **not** self-certify. 05 keeps only pointers in `route.md` / `handoff.md`.
**Owner (file seat):** `05_manuscript` (checklist body); gate pass/fail = 00.

---

## Science checks (QCS)

**Class:** QCS (science). The Intro/Discussion scorecards and the voice/structure checks moved to `style-qc/scorecards.md` and `style-qc/style-qc.md` (QCV, soft, S4 only). This file keeps the science pre-submit checks and the standing bans.

---

### Part B — Pre-submit consistency

> **QC routing:** Formal Gate ownership: `00_orchestrator`. This file is the 05 local pre-submit checklist.

---
name: pre-submit-consistency
owner: 05_manuscript
audience: Aitee
role: writing
on_number_conflict: comment_only
voice_report: 05_manuscript/qc/style-qc/style-qc.md
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
  - id: no_causal_overclaim_observational
    class: claim_semantics
---

## Pre-submit consistency (Aitee)

Science QC (S2) runs before any advanced revision; style QCV runs only at S4, after the advanced revision, or on an explicit de-AI / polish request.

Target-journal AI-use disclosure: check the author instructions and match any required AI statement (or confirm the journal asks for none).

Statistical definitions live in `02_data-processing/qc/report-checks.md` and the checkbox list in `02_data-processing/qc/report-checks.md`. Lee's annotation protocol lives in `06_review/qc/cross-manuscript-qc.md`.

Citation rows below are writing actions only. call/require 03 citation-verify — do not self-certify lit (`03_research/advanced/citation-verify.md`).

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

Feature or ROI selection, threshold or cutoff selection, and the group or performance test on the same participants, without an outer nested cross-validation or a bootstrap optimism correction, do not support a confirmatory *P*. Write the result as apparent or descriptive. Do not write "confirmatory", "independently validated", or an unqualified "significantly different" for that test. Lab nested CV is not implemented (`02_data-processing/advanced/analysis/pipeline.md`). Do not write that nested CV was run unless the user confirms it.

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

**Process-negation / disclaimer / CYA / incompleteness (AL-5):** canonical rule and its PASS/FAIL text live in `05_manuscript/qc/anti-leak-placeholders.md` (AL-5). Apply the same rule to response-letter bodies and revised manuscript bodies; this file does not restate it.

Agent must not add new negative gap lists either (`was not tested / measured / examined / included …`). A verifiable negative fact already present in the user's Methods or Limitations may stay. Unresolved items go to a Word comment (author **A**), with an English sentence starting `Suggested …` that supplies the preferred body wording.

#### layout_priority

Layout order: the user's instruction this run, then the target journal guide, then `05_manuscript/advanced/Aitor-format.md` defaults. Paragraphs stay as paragraphs; new paragraphs only on topic change. Abstract labels, Methods/Results subheads, Highlights, and figure/table notes keep their format.

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

The sentence's claim (population, modality, direction of effect) is a claim the cited work makes. A mismatch is weaken or replace via `05_manuscript/advanced/process/evidence.md`, not a decorative citation.

#### no_unverified_cross_copy

A DOI, author list, year, or volume copied from another manuscript is not verification. Each entry is checked against the work (`03_research` / verify-refs) before it stays.

#### year_volume_from_source

A year or volume correction is applied only after the source confirms it. An unverified "correction" stays a comment.

#### no_causal_overclaim_observational

An observational design reports association, not causation (authority: `05_manuscript/advanced/voice-portrait.md` § 2 and `05_manuscript/advanced/process/citation-and-language.md` § Language). *causes*, *proves*, *demonstrates that X leads to* is a fail. Comment only; do not restate the design claim.

## Reporting guidelines (qc-only; post-write)

After major draft or number edits, run `05_manuscript/qc/check-reporting/` (TRIPOD / CLAIM / CLEAR / PROBAST stack) and `reporting-guideline-route.md`. Retired fine id `check-reporting` (non-routable body) — not session-picked; Gate G-05 / Integrity · pre-06 loads this path.
