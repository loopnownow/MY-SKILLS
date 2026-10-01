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

# Pre-submit consistency (Aitee)

Load on every full-paper draft, polish, and house.docx pass, after `Aitor-format.md` and `voice-portrait.md`.

Statistical definitions live in `04_analysis/personal/stats-consistency.md` and the checkbox list in `04_analysis/personal/stats-checklist.md`. Lee's annotation protocol lives in `06_review/personal/cross-manuscript-qc.md`.

Citation rows below are writing actions only. call/require 03 citation-verify — do not self-certify lit (`03_research/personal/citation-verify.md`).

**Number conflict:** Word comment, author **A**. Do not choose a replacement *n*, *P*, *t*, cutoff, quartile, or overlap count. A back-calculated critical value, implied *n*, or adjusted *P* may appear in a comment only if it is labeled an estimate. It does not enter the manuscript.

Split names stay **training set / test set / validation set**.

## Checks

### stat_vs_threshold

A reported *t*, *F*, or *z* must be compatible with the voxel-wise or cluster-forming threshold named in Methods (same α, same df or approximation the paper claims). A statistic that only meets a looser α contradicts the threshold sentence. Flag both loci. Do not rewrite either number.

### correlation_implied_n

The *n* implied by a reported *r* or ρ and its *P* must match the *n* of that analysis (the analyzed subset, not an enrollment total from another sentence). Recompute the two-sided *P* from *r* and the stated *n*, or invert *n* when the paper omits it. Disagreement beyond rounding means the stated *n* is not the analysis *n*. Say so in a comment. Do not invent a complete-case *n*.

### multiplicity_disclosure

A family of ROI-wise or voxel-wise correlations states the family size and the correction (FWE, FDR, Holm, Bonferroni) or is labeled uncorrected and exploratory. Silence is a fail. Do not apply a correction the paper did not run.

### relative_denominator

Any quantity called relative, normalized, ratio, or scaled names its denominator in Methods before Results interpret the spread (global mean, reference region, cerebellar value, or the real divisor). Units of the reported values are stated. An undefined "relative" measure is not interpretable. Comment; do not guess the divisor.

### overlap_statement_and_citation

Same hospital, same scanner, or the same ethics approval as another lab paper: Methods contains one explicit overlap sentence (no shared participants, partial overlap, or overlap not yet quantified) and cites the sister paper. Unknown counts stay unknown in a comment. Do not invent overlap counts. Missing the sentence is a split-publication risk.

### shared_table_sample_overlap

A table reused with the same cells in another manuscript is evidence of shared participants until the overlap sentence says otherwise. Write the overlap sentence. Do not leave the table looking independent.

### sister_paper_p_reconciliation

The same biomarker and contrast with a materially different *P* or effect in a sister paper needs a reconciliation note (different *n*, covariates, threshold, or subset) or a comment that the conflict is unresolved. Do not average the *P* values or silently keep one.

### no_confirmatory_p_same_cohort

Feature or ROI selection, threshold or cutoff selection, and the group or performance test on the same participants, without an outer nested cross-validation or a bootstrap optimism correction, do not support a confirmatory *P*. Write the result as apparent or descriptive. Do not write "confirmatory", "independently validated", or an unqualified "significantly different" for that test. Lab nested CV is not implemented (`04_analysis/personal/0rad-pipeline-rules.md`). Do not write that nested CV was run unless the user confirms it.

### nested_roi_collinearity

Parent regions and their subregions in one model or one uncorrected family are not independent tests. Name the nesting and the dependence. Do not report them as separate confirmatory findings.

### score_transform_identity

If a named score is a linear or other transform of a single metric, the same sentence says so and gives the transform. The score is not a second biomarker and does not get its own confirmatory test. An undefined score name is a comment, not a new construct.

### pipeline_tokens_banned

Final body and figure legends do not contain pipeline tokens (`TRAIN_RATIO`, `VAL_MODE`, `settings.ini` keys, internal column codes). Write the procedure in words, or comment if the value is unknown.

### source_attribution_banned

Final prose does not say "as stated by the source", "according to the HTML", or "the source says". State the fact. The lab file stays off the page.

### placeholder_and_internal_labels_banned

Final prose does not contain 待补, 待补充, TBD, XX, bracketed parameter slots, or internal QC labels such as 标签未与方案核对. Missing facts become a Word comment (author **A**).

### repeated_disclaimer

The same disclaimer or limitation sentence appears once. A second copy in the body or a legend is a fail. Collapse to one locus.

### empty_retrieval_and_scan_placeholders

A search sentence names the databases and the actual query. An empty query, `""`, `[query]`, or 待补 is unfinished. Do not invent the query. Scanner and sequence parameters that the modality needs (vendor, field strength, sequence, timing, resolution, or the real list) are values from the protocol or a comment. "Standard protocol" does not replace them.

### cutoff_vs_included_distribution

State the direction of each entry cutoff. Median, first quartile, and minimum of each included group must sit on the included side of that cutoff. A summary on the excluded side is a contradiction. Flag the cutoff sentence and the table cell. Do not change either number.

### iqr_scale_sanity

IQR (Q3−Q1) lies inside the instrument's possible range. An IQR wider than the scale, or a quartile that contradicts the cutoff, is a comment. Do not replace the quartile.

### consecutive_same_cite

Do not cite the same paper in consecutive sentences unless the second sentence adds a distinct claim that paper supports. Neighbouring sentences that share one source cite once (`citation-and-language.md`).

### claim_matches_source

The sentence's claim (population, modality, direction of effect) is a claim the cited work makes. A mismatch is weaken or replace via `evidence-request.md`, not a decorative citation.

### no_unverified_cross_copy

A DOI, author list, year, or volume copied from another manuscript is not verification. Each entry is checked against the work (`03_research` / verify-refs) before it stays.

### year_volume_from_source

A year or volume correction is applied only after the source confirms it. An unverified "correction" stays a comment.

### paragraph_lock

One fact per sentence is allowed. Related sentences stay in the same paragraph. IMRAD body is not one sentence per line and not one sentence per paragraph. Abstract labels, Methods and Results subheadings, Highlights, and table or figure notes keep `Aitor-format.md`.

### intro_opening_has_citations

The Introduction opening paragraph cites when a verified source exists for that claim. Zero citations there is a fail. Element 6 (aim / hypothesis) stays uncited. Discussion first paragraph stays uncited.

### split_names_are_sets

Internal splits are the **training set**, the **test set**, and, when external, the **validation set**. Do not rename them as groups.

### approach_not_framework

Vague methodological "framework" is "approach" (`forbidden-phrases.md`). A named software library may keep its own name.
