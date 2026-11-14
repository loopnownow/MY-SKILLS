# English peer-review envelope (generic templates)

Generic letter envelope and per-chapter attack points for an English review. Moved out of `06_review/advanced/review.md` on 2026-11-14: base keeps the envelope, advanced keeps the house hard rules (§0-§0.2), the opener/AI-disclosure voice (§3), the pre-submit consistency asks (§4.9), the tone/forbidden lists (§5-§6) and the comment habits (Part B). Section numbers are preserved, so `§2` / `§4.7` anchors still mean the same thing.

## 2. Default envelope (2024-2026)

Issue items by the owner's eight-chapter template. Inside each chapter: **Major Issues** first, then **Minor Issues**. Major = can change conclusions / reproducibility / ethics / data consistency; Minor = wording, format, legend completion.

```text
[Opening 2-4 sentences: design + clinical question + overall value + the methodological catch]

1. Title
Major Issues: [Lines n-m: / Section, paragraph, line: + defect + Please fix]  (source tags go in comments; see `06_review/advanced/review.md` §0.1)
Minor Issues: …

2. Abstract
Major Issues:
Minor Issues:

3. Introduction
Major Issues:
Minor Issues:

4. Methods
Major Issues:
Minor Issues:

5. Results
Major Issues:
Minor Issues:

6. Discussion
Major Issues:
Minor Issues:

7. References
Major Issues:
Minor Issues:

8. Figures & Tables
Major Issues:
Minor Issues:
```

Add a `Major Comments` line when needed. Do not write a 25-item questionnaire (unless the editorial form forces it). Empty chapters: write `None` or omit — do not pad.

**Per item:** `Lines n-m:` (or section) → defect → **Please** with a clear fix. Source tags and Chinese reasons go in comments (`06_review/advanced/review.md` §0.1). Do not invent experiments not done; do not invent AUCs for the authors.

---


## 4. Chapter review focus (template) and high-frequency attack points

Scan by chapter when writing; write what applies, skip the rest. English = polite imperatives.

#### 4.1 Title
**Focus:** accurately reflects core content and study type (RCT / cohort / diagnostic / prediction model).
- Major: title mismatches body; temporal split labeled as external validation.
- Minor: fluff words; abbreviation not expanded.

#### 4.2 Abstract
**Focus:** complete structure; objective/methods/key numbers (OR/HR, 95% CI, *P*) and conclusion match the body.
- Major: hides low specificity; missing 95% CI; numbers disagree with the body. (~10 hits)
- Minor: word count; first-use expansion of abbreviations.

#### 4.3 Introduction
**Focus:** background leads to a gap; hypothesis and aim are clear.
- Major: last paragraph lacks a clear hypothesis. (~5 hits) `Please clearly state the research hypothesis in the last paragraph of the Introduction.`
- Minor: background too long; citation stacking (pre-review: do not delete real refs; note over-quota only).
- Minor: opening paragraph has citable evidence but 0 refs; two consecutive sentences cite the same paper with no new claim. See `06_review/advanced/review.md` §4.9. Aim paragraph still takes no citations.

#### 4.4 Methods
**Focus:** design matches the question; controls sensible; sample-size rationale; inclusion/exclusion tight; tech/sequence/software versions reproducible; IRB/consent/registration.
- Major (high frequency):
  - ROI / segmentation reproducibility (~23)
  - sample size / consecutive enrollment / missing-record handling (~19)
  - ethics placeholders / missing ethics ID (~18)
  - feature-selection leakage / LASSO λ / nested-in-fold (~12)
  - scan parameters / multi-vendor consistency (~12)
  - “external” that is same-hospital temporal split (~11)
- Minor: reagent vendor, software version, parameter completion.
- Major: same cohort used for screening, thresholding, and between-group tests, yet *P* is written as confirmatory. Relabel as descriptive, or provide nested CV / bootstrap that was actually run. Do not invent nested CV for the authors.
- Major: inclusion cutoff contradicts the enrolled group's median, Q1, or minimum; IQR outside the scale range. Comment only; do not change numbers.
- Major: empty search string, or scan parameters still placeholders. See `06_review/advanced/review.md` §4.9.

#### 4.5 Results
**Focus:** stats match distributions; body matches figures/tables; no selective reporting; no over-reading non-significant results.
- Major: overfitting (near-perfect train, drop on test, ~13); no comparison to conventional/clinical models (DeLong, calibration, DCA, ~15); p disagrees with tables.
- Major: *t*/*F*/*z* cannot meet the named voxel or cluster threshold; correlation *r* and *P* imply an *n* that disagrees with the analysis *n*; many ROI correlations without multiple-comparison control; relative metrics without a defined denominator. Flag contradictions only; do not invent numbers. See `06_review/advanced/review.md` §4.9.
- Minor: table notes omit Mean±SD / Median(IQR).

#### 4.6 Discussion
**Focus:** conclusions supported by data; no correlation-as-causation; compared with prior work; limitations stated objectively.
- Major: limitations unclear (~24); causal wording vs retrospective design (~8).
- Minor: loose structure; repeats Results.

#### 4.7 References
**Focus:** representative; key literature from last 2-3 years; format; no duplicate entries.
- Major: 同一 DOI / same title twice → Major: merge numbers or swap the reference; when swapping, **do not** copy numbers unique to the old paper (case counts, AUC, …) onto the new one.
- Major: citation verify failed → comment with the **dual-track plan** (below); 00 QC decides whether to call `03_research`; do not invent PMIDs.
- Minor: format, missing DOI.
- Major: author list, DOI, year, or volume copied from another manuscript, or year/volume changed without checking the source. Verify against the source. Do not fill “correct” years from memory. See `06_review/advanced/review.md` §4.9.
- Literature accuracy is shared with Victor. call/require 03 citation-verify — do not self-certify lit. Lee does not sign the claim→ref table.

**Citation-verify failure (dual track; write into the comment; user decides):**
1. **Change-the-prose plan** (word/sentence): before / after.
2. **Keep-the-prose plan:** hand off to 03 to find a replacement that supports the current sentence (real PMID/DOI).
Whether 03 is actually called → **00 decides at QC**; if unsure, ask the user one question. The replacement carries only that paper's real info; old-paper numbers do not migrate.

#### 4.8 Figures & Tables
**Focus:** self-explanatory; consistent with body; resolution, scale bar, legends, stats symbols.
- Major: figure count disagrees with body; Figure 1 has no inclusion box yet claims STROBE flow.
- Minor: missing scale bar; Table 1 omits Mean±SD / Median(IQR).
- Major: table identical to another manuscript without stating sample overlap.
- Minor: legend still has `TRAIN_RATIO` or other pipeline tokens. See `06_review/advanced/review.md` §4.9.

Reusable short lines (placeholders; no unpublished numbers):
- `Please specify if this is a retrospective or a prospective study.`
- `Please acknowledge and describe how cases were consecutively or randomly selected.`
- `Please provide the exclusion criteria.`
- `It is unclear how the authors performed the ROI drawing.`
- `Please report 95% confidence intervals for all AUC values and include them in the Results and Discussion.`
- `Please comply with the STROBE / TRIPOD reporting guidelines.`
- `Please discuss how the model would be used in practice.`
- `The authors should more clearly justify the clinical utility given the modest discriminative performance.`

