---
name: cross-manuscript-qc
owner: 06_review
audience: Lee
role: review
order:
  - statement_consistency
  - data_consistency
on_number_conflict: annotate_only
journal_language: en
user_summary_language: zh
runs_checks_from: 05_manuscript/personal/pre-submit-consistency.md
---

# Cross-manuscript and pre-submit QC (Lee)

Load on every pre-review and peer-review, after `review-comment-habits.md`. Journal-facing envelope stays English (`personal-review-style.md`). The reason inside the Word comment stays Chinese, after the source tag. A user-facing pre-review summary stays Chinese. Do not swap that split.

Run **statement consistency first** (the manuscript agrees with itself), then **data consistency**. Check ids and writing actions are the list in `05_manuscript/personal/pre-submit-consistency.md`. Statistical definitions are in `04_analysis/personal/stats-consistency.md`.

**Data conflict:** annotate every locus. Do not invent *n*, *P*, *t*, cutoff, quartile, overlap count, or a corrected statistic. Do not pick which of two printed numbers is right. A back-calculation in the comment is labeled an estimate and does not enter the manuscript.

## Order

1. Statement consistency (`review-comment-habits.md` §2).
2. Data consistency inside this manuscript (§3 there, plus the classes below).
3. Sister-paper cohort risk (this file).
4. Circular analysis and score identity.
5. Process language and placeholders, including figure legends.
6. Citation hygiene.
7. Integrity stop. Do not quiet-fix.

## Sister papers

Treat papers as related when they share a hospital, a scanner, or an ethics approval, or when the user names them as a set.

### overlap_statement_and_citation

Each related paper needs an explicit overlap sentence (none, partial, or not yet quantified) and a citation of the other paper. Absence is a Major comment: split publication is unexplained. Ask for the sentence. Do not invent who was shared.

### shared_table_sample_overlap

The same table (same cells) in two manuscripts is a Major until overlap is stated. Ask the authors to say whether the samples are the same participants. Do not assume independence.

### sister_paper_p_reconciliation

The same biomarker and contrast with a conflicting *P* or effect across sister papers is a Major. Ask for a reconciliation note (different *n*, covariates, threshold, or subset) or an admission that the conflict is unresolved. Do not average the *P* values. Do not replace one paper's *P* with the other's.

## Inside one manuscript

Use the check ids in `pre-submit-consistency.md`. Review actions:

| Id | Review action |
|---|---|
| stat_vs_threshold | Major if the printed statistic cannot meet the named voxel or cluster threshold. Point at both sentences. Do not replace either value. |
| correlation_implied_n | Major if *r* and *P* imply an *n* other than the stated analysis *n*. Ask which *n* was analyzed. |
| multiplicity_disclosure | Major when many ROI or voxel correlations omit both a correction and an exploratory label. |
| relative_denominator | Major when a relative measure has no denominator. Ask for the divisor and the units. |
| no_confirmatory_p_same_cohort | Major when selection, thresholding, and the group test share one cohort and the *P* is written as confirmatory. Ask for descriptive wording, or for nested CV / bootstrap if it was actually run. Do not write a nested-CV sentence the lab did not run. |
| nested_roi_collinearity | Major when nested ROIs are treated as independent tests. |
| score_transform_identity | Major when a score is an unnamed transform of one metric, or is tested as a separate biomarker. |
| pipeline_tokens_banned | Minor in one legend, Major if pipeline tokens remain in the body the authors call final. |
| source_attribution_banned | Minor. Delete "as stated by the source" and its cousins. The fact stays; the hedge goes. |
| placeholder_and_internal_labels_banned | Major. 待补, TBD, XX, and internal labels such as 标签未与方案核对 do not survive in the body. |
| repeated_disclaimer | Minor unless the same caveat is doing the work of a missing analysis. Keep one copy. |
| empty_retrieval_and_scan_placeholders | Major. Empty queries and missing scan parameters are unfinished Methods. |
| cutoff_vs_included_distribution | Major when an included group's median, Q1, or minimum falls on the excluded side of the entry cutoff. |
| iqr_scale_sanity | Major when IQR exceeds the instrument range or contradicts the cutoff. |
| consecutive_same_cite | Minor. Cite once unless the next sentence adds a distinct claim. |
| claim_matches_source | Major when the sentence asserts something the cited work does not claim. Dual plan per `personal-review-style.md` §4.7. |
| no_unverified_cross_copy | Major. An author list or DOI copied from a sister manuscript is unverified. |
| year_volume_from_source | Major if a year or volume was changed without a source check. Ask to verify. Do not supply the "correct" year from memory. |
| paragraph_lock | Minor. Short sentences may stay; one sentence per line or per paragraph in the body may not. |
| intro_opening_has_citations | Minor, or Major if the opening claim is doing evidential work with no source. Element 6 stays uncited. |
| split_names_are_sets | Minor. Training, test, and validation stay **set**. |
| approach_not_framework | Minor. Vague "framework" becomes "approach". |

## Comment shape

English envelope line: locator, defect, Please-request (`personal-review-style.md` §4.9). Chinese reason in the Word comment after the source tag. `cannot_invent` when the fix needs a number the files do not contain.
