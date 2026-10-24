# English peer review (style + habits)

> **Post-QC re-review (2026-10-17):** A06 runs after base isolation + 00 QC. See `review-isolation.md`. Response letters -> `07_response`.


## Part A — English peer-review envelope

# Personal peer-review style (English peer review)

Source: 2014–2026 self-authored journal-review full-text corpus, 57 deduplicated files. Keep structure, tone, and high-frequency attack points only — do not ingest others' unpublished titles, data, ethics IDs, or patient identifiers.

On-disk corpus (internal review; source of the owner's comment style): `{doc_review_corpus}\`. This file does not copy the corpus body.

This file serves **English journal peer review** only (letters written for others and submittable to the system; lab pre-review may reuse the same chapter skeleton). The two tasks below use other templates — do not mix them into this envelope:

| Task | File |
|---|---|
| Thesis / dissertation review | this file § Thesis review digest |
| Chinese-journal 1–5 scores + A–F / academic review form | this file § Chinese journal score digest |

Early Chinese review forms can be blunt («并无新意» / «选择偏倚» / «未交代»). **Do not import that bluntness into English.** English uses polite, direct, actionable imperatives.

**Mode entry:** `06_review/SKILL.md` (`pre-review` / `peer-review` / `response`). Do not cite deleted `mode-2-*.md`.

---

**Corpus harvest (2026-10-23):** checklist themes in `personal/references/corpus-review-habits.md` (methods / consistency / overclaim). Envelope rules in this file win on conflict.

## 0. Comments and conflicts (lab hard rules)

Ownership: see `00_orchestrator/references/ownership-contract.md`.

- Word / 稿面批注 **作者字段** is always **A**. No yellow highlight. 作者栏 ≠ 来源标签.
- Source goes only in the comment **body prefix** (lead-in): which layer this judgment came from — not an envelope label.
  - **Format (mounted items):** `[源:包内skill-id]`. Forbid source-only tags (bare `[Nature:]` / `[Scientific:]`). B uses v4 fine IDs: `[B:peer-review]`.
  - Examples: `[A:personal]` · `[B:peer-review]` · `[Nature:simulate-reviewers]` · `[self-review]` · `[peer-review]` · `[lit-search]` (personal / fine-ID tasks)
  - Mount + personal both apply → **双标** (dual tag), e.g. `[Nature:simulate-reviewers] [A:personal]` / `[self-review] [A:personal]`
- **Mandatory:** when this round mounts an external review source (Nature / peer-review / self-review, or non-personal B), every finding/gate/checklist item from that mount **must** carry a **skill-level** tag in the prefix (e.g. `[Nature:simulate-reviewers]`), not source-only. Forbid rewriting everything as `[A:personal]` just because the personal eight-chapter envelope was used. **Forbid defaulting to `[A:personal]`** (Rules: `My rule.md` §5.1 + this file §0).
- With no mount, empty source prefixes must not appear. Pure lab sentence edits (grammar, Aitor punctuation) take `[A:personal]` only. Use `[A:personal]` only when the source cannot be determined.
- **When a mount suggestion conflicts with lab doctrine:** do not silently adopt the mount fix. Put everything in the comment: conflict point + **fix plan** (before/after sentence, or “keep sentence + swap reference”). **最终由用户决定.** After the user agrees, Aitee still lands Track Changes; Lee comments only.
- **Decidable issues:** Lee writes a clear comment (locus, defect, 词或句 to change) and hands Aitee a TC-fix. Lee does not edit the body by default.
- Undecidable facts (missing n, ethics, analysis not done): mark `cannot_invent`, ask the user. Chinese comment plus English suggested wording and/or suggested literature (see ownership-contract). Victor supplies suggested literature. Lee does not land manuscript edits; after the user chooses, Aitee applies Track Changes to the body.
- **Process-negation / not-done class (owner 2026-10-23):** Process-negation sentences that flag work not done («未做 / 未进行 / 我们未…» or similar CYA) **must not enter the body** (manuscript, revision, response letter). Word **comments** only (author **A**), and every comment must include **建议修改后内容** (suggested revised content); bare flags are forbidden. True negative study results (e.g. *no significant difference*, *was not associated with*) are not banned by this rule. QC: `05_manuscript/qc/anti-leak-placeholders.md` AL-5; `07_response/qc/disclaimer-comment-only.md`.
- Edit unit: **word or sentence**; forbid whole-paragraph rewrites.

---


## 0.1 Opinion-item localization (hard rules)

- Every Major / Minor **body**: `Lines n–m:` (or figure/table/section locus) + what is wrong + Please how to fix.
- **Prefer:** Proof/manuscript line numbers, e.g. `Lines 76–79:` / `Line 216:`.
- **When no reliable line numbers:** `Introduction, paragraph 2, line 3:`; or `Table 1 legend:` / `Figure 5A:` / `Section 2.3, paragraph 1:`.
- **If line numbers are given, do not restate or quote the manuscript sentence.**
- **Source tags** (e.g. `[B:self-review][A:personal]`) go only at the Word **comment** lead-in; author field **A**. Write the Chinese reason in the same comment after the source tag. `cannot_invent` / G-LIT dual-track also go in comments only (not the envelope body).
- **Forbid** burying line numbers mid-sentence or at the end; forbid unlocalized vague attacks (Opening summary excepted — Opening may omit line numbers).
- **When the locus is uncertain:** do not invent precise line numbers. In the Word **comment**, state why it is uncertain + suggested locator + suggested revision; comment **author field = A**. After the user confirms, change only that item in the review **envelope**. Do not Track-Change the manuscript body here (see ownership-contract).
- If the user pastes a source sentence: align line numbers on Proof/plain first, then write into the matching chapter; do not spawn a new review docx.

## 1. Era layering (picks the envelope; does not import Chinese bluntness into English)

| Approx. years | Form | How English peer review uses it |
|---|---|---|
| 2014–2018 | Chinese-journal review form | **Do not** use as an English-letter template. Use this file § Chinese journal score digest |
| 2019–2023 | `Dear Editor` + line-number-first items (Lines n–m / Section, paragraph, line) | Only when the invitation/system still requires a salutation |
| 2024–2026 | No salutation or one-line invite thanks; Opening → chapter Major/Minor | **Default envelope** |

Do not put Accept / Reject / Major revision scores in the body; scores go in internal notes or the Chinese review form.

---

## 2. Default envelope (2024–2026)

Issue items by the owner's eight-chapter template. Inside each chapter: **Major Issues** first, then **Minor Issues**. Major = can change conclusions / reproducibility / ethics / data consistency; Minor = wording, format, legend completion.

```text
[Opening 2–4 sentences: design + clinical question + overall value + the methodological catch]

1. Title
Major Issues: [Lines n–m: / Section, paragraph, line: + defect + Please fix]  (source tags go in comments; see §0.1)
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

**Per item:** `Lines n–m:` (or section) → defect → **Please** with a clear fix. Source tags and Chinese reasons go in comments (§0.1). Do not invent experiments not done; do not invent AUCs for the authors.

---

## 3. Opening (2–4 sentences)

Name the design + clinical question → overall value or not → but methods still have a catch. Avoid empty praise (*interesting*).

**Default:**
```text
This [design] study [does X] to [clinical question]. The topic is clinically relevant, but methodological limitations—particularly [theme], [theme], and [theme]—currently weaken the strength of the conclusions.
```

Variant (stronger manuscript): `While the study is methodologically sound and clinically promising, a few key areas would benefit from further revision.`

Variant (reproducibility focus): `This study had certain clinical usefulness. However, the method was not rigorous. Details should be provided for the repeatability. These are my comments.`

**Dear Editor (when the system still wants a salutation):**
```text
Dear Editor:
Thank you for inviting me to evaluate this article. The purpose of this study was to …. However, details for explanation of replicability of the methods should be provided.
```

Do not put Accept/Reject in the Opening. Recent years may keep the footnote `AI was used to refine the readability of the peer review comments, all of which came from the reviewer.` — polish syntax only; do not change the judgment.

---

## 4. Chapter review focus (template) and high-frequency attack points

Scan by chapter when writing; write what applies, skip the rest. English = polite imperatives.

### 4.1 Title
**Focus:** accurately reflects core content and study type (RCT / cohort / diagnostic / prediction model).
- Major: title mismatches body; temporal split labeled as external validation.
- Minor: fluff words; abbreviation not expanded.

### 4.2 Abstract
**Focus:** complete structure; objective/methods/key numbers (OR/HR, 95% CI, *P*) and conclusion match the body.
- Major: hides low specificity; missing 95% CI; numbers disagree with the body. (~10 hits)
- Minor: word count; first-use expansion of abbreviations.

### 4.3 Introduction
**Focus:** background leads to a gap; hypothesis and aim are clear.
- Major: last paragraph lacks a clear hypothesis. (~5 hits) `Please clearly state the research hypothesis in the last paragraph of the Introduction.`
- Minor: background too long; citation stacking (pre-review: do not delete real refs; note over-quota only).
- Minor: opening paragraph has citable evidence but 0 refs; two consecutive sentences cite the same paper with no new claim. See §4.9. Aim paragraph still takes no citations.

### 4.4 Methods
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
- Major: empty search string, or scan parameters still placeholders. See §4.9.

### 4.5 Results
**Focus:** stats match distributions; body matches figures/tables; no selective reporting; no over-reading non-significant results.
- Major: overfitting (near-perfect train, drop on test, ~13); no comparison to conventional/clinical models (DeLong, calibration, DCA, ~15); p disagrees with tables.
- Major: *t*/*F*/*z* cannot meet the named voxel or cluster threshold; correlation *r* and *P* imply an *n* that disagrees with the analysis *n*; many ROI correlations without multiple-comparison control; relative metrics without a defined denominator. Flag contradictions only; do not invent numbers. See §4.9.
- Minor: table notes omit Mean±SD / Median(IQR).

### 4.6 Discussion
**Focus:** conclusions supported by data; no correlation-as-causation; compared with prior work; limitations stated objectively.
- Major: limitations unclear (~24); causal wording vs retrospective design (~8).
- Minor: loose structure; repeats Results.

### 4.7 References
**Focus:** representative; key literature from last 2–3 years; format; no duplicate entries.
- Major: 同一 DOI / same title twice → Major: merge numbers or swap the reference; when swapping, **do not** copy numbers unique to the old paper (case counts, AUC, …) onto the new one.
- Major: citation verify failed → comment with the **dual-track plan** (below); 00 QC decides whether to call `03_research`; do not invent PMIDs.
- Minor: format, missing DOI.
- Major: author list, DOI, year, or volume copied from another manuscript, or year/volume changed without checking the source. Verify against the source. Do not fill “correct” years from memory. See §4.9.
- Literature accuracy is shared with Victor. call/require 03 citation-verify — do not self-certify lit. Lee does not sign the claim→ref table.

**Citation-verify failure (dual track; write into the comment; user decides):**
1. **Change-the-prose plan** (word/sentence): before / after.
2. **Keep-the-prose plan:** hand off to 03 to find a replacement that supports the current sentence (real PMID/DOI).  
Whether 03 is actually called → **00 decides at QC**; if unsure, ask the user one question. The replacement carries only that paper's real info; old-paper numbers do not migrate.

### 4.8 Figures & Tables
**Focus:** self-explanatory; consistent with body; resolution, scale bar, legends, stats symbols.
- Major: figure count disagrees with body; Figure 1 has no inclusion box yet claims STROBE flow.
- Minor: missing scale bar; Table 1 omits Mean±SD / Median(IQR).
- Major: table identical to another manuscript without stating sample overlap.
- Minor: legend still has `TRAIN_RATIO` or other pipeline tokens. See §4.9.

Reusable short lines (placeholders; no unpublished numbers):
- `Please specify if this is a retrospective or a prospective study.`
- `Please acknowledge and describe how cases were consecutively or randomly selected.`
- `Please provide the exclusion criteria.`
- `It is unclear how the authors performed the ROI drawing.`
- `Please report 95% confidence intervals for all AUC values and include them in the Results and Discussion.`
- `Please comply with the STROBE / TRIPOD reporting guidelines.`
- `Please discuss how the model would be used in practice.`
- `The authors should more clearly justify the clinical utility given the modest discriminative performance.`

### 4.9 Pre-submit consistency requests

Chapter scans above point here. Full check ids: `05_manuscript/qc/manuscript-local-qc.md`. Run order and sister-paper rules: `06_review/qc/cross-manuscript-qc.md`. Statement consistency first, then data. On a conflict, annotate. Do not invent the number.

Reusable requests (no unpublished results in the sentence):

- `Please show that the reported statistic meets the voxel-wise or cluster-forming threshold named in Methods, or correct the threshold statement.`
- `Please state the n for each correlation and confirm that it matches the reported r and P. Please name the multiple-comparison procedure, or label the correlations uncorrected and exploratory.`
- `Please define the denominator and the units of any relative measure before interpreting its spread.`
- `Feature selection, threshold selection, and the group comparison appear to use the same participants. Please relabel these P values as descriptive, or provide the nested cross-validation or bootstrap correction that was actually run.`
- `Please state whether this score is a transform of a single metric, and whether nested regions were entered as independent tests.`
- `Please remove pipeline tokens, source-attribution hedges, and placeholder text from the manuscript and the figure legends.`
- `Please reconcile the inclusion cutoff with the reported median, quartile, and IQR.`
- `These manuscripts appear to share a site, a scanner, or an ethics approval. Please state the participant overlap and cite the related paper.`
- `This table matches another manuscript. Please state whether the samples overlap.`
- `The same biomarker is reported with a different P in a related manuscript. Please reconcile the difference.`
- `Please cite the opening background claim, or weaken it. Please do not cite the same paper in consecutive sentences unless the second sentence adds a distinct claim.`
- `Please verify this reference against the source. Do not copy the author list, DOI, year, or volume from another manuscript.`

---

## 5. Tone and quality self-check

- Polite, direct, actionable. Facts first, then why it matters, then what the author should change.
- Do not invent experiments not done; do not invent AUCs; do not restate identifiable unpublished result tables in the opinion.
- Score-only with no fix = forbidden.
- English **must not** import blunt Chinese-form translations (*no novelty* / *selection bias* as insults). Write the same fact as an actionable request.

Pre-submit self-check (four axes):
1. **Precise and actionable** — has Lines n–m / Section, paragraph, line (or section) + a clear fix.
2. **Clear structure** — Major / Minor separated.
3. **Constructive** — academic respect; even a reject suggestion names improvement directions.
4. **Editor-helpful** — Opening already summarizes core strengths and key weaknesses.

---

## 6. Forbidden

- Putting others' manuscript PDFs, supplements, CSVs, or unpublished titles into the skill or a public repo
- Putting thesis-review or national-self-eval boilerplate into English peer review
- Pasting whole Chinese-journal A–F score blocks into the English letter
- Empty praise (*interesting*); emoji; padded compliments
- Silently adopting mount fixes that conflict with the lab (must go into comments; user decides)


---

## Part B — Comment habits

# Review comment habits (Aitor / Jinshan)

Personal upper layer for **review** / pre-submission pre-review (find defects, emit comments and actionable requests).  
Journal-facing English envelope stays in `review.md`.  
This file is the **consistency-first** habit layer.

**Locks (2026-09-24):** do **not** teach minimal `?` / bare “核实” as the house style. Lead with **statement consistency**, then **data consistency**, then integrity stops.

**Locks (2026-10-02):** on a data conflict, annotate every locus. Do not invent a replacement number. Pre-submit classes and sister-paper checks: `06_review/qc/cross-manuscript-qc.md`. Check ids: `05_manuscript/qc/manuscript-local-qc.md`. call/require 03 citation-verify — do not self-certify lit.

**Locks (Word revise ownership):** Ownership: see `00_orchestrator/references/ownership-contract.md`.

---

## 1. Overall portrait (reviewer side)

Review like a careful editor + statistician: numbers, abbreviations, reference hygiene, legend placement, and causal vs association wording.

- Prefer **actionable** comments: what is wrong, where, and what to do.
- Prefer finite choices at decision points; still stop for real ambiguity.
- Uncertain facts: mark `cannot_invent` / ask — never pick a number silently.
- Mount vs lab conflict: write both options in the comment; **user decides** (`review.md` §0).

---

## 2. Statement consistency (first pass)

Before arguing about a new analysis, check whether the manuscript **agrees with itself**:

| Check | Fail examples | Comment action |
|---|---|---|
| Same claim, same wording | Abstract vs Results vs Discussion disagree on what was compared | Point to both loci; ask which wording is intended |
| Comparison object explicit | “higher risk” without naming who vs whom | Require “A vs B” (or named groups) in Methods/Results |
| Endpoint / label boundaries | Pseudoprogression vs multi-horizon ORR conflated | Ask for one clarifying sentence; do not invent the endpoint |
| Time / follow-up arithmetic | Follow-up window conflicts with enrollment dates | Ask to reconcile from source calendar; do not invent dates |
| Co-author comment vs body | Reviewer/co-author note does not match current text | Say the mismatch plainly; force version sync |
| Section misplacement | Discussion sentence that belongs in Introduction (or reverse) | Relocate request; do not rewrite content here (prose → 05) |

Comments stay concrete (locator + ask). Avoid empty style lectures.

---

## 3. Data consistency (second pass)

| Check | Fail examples | Comment action |
|---|---|---|
| Cross-surface numbers | AUC / *n* / *P* differ across Abstract, body, tables, figures | Flag all loci; **do not choose** which number is “right” |
| CI pairing | AUC without 95% CI; training reported without test (when both exist) | Request paired reporting from `*-results.html` |
| Table ↔ prose | Prose invents a cell the table does not have (or contradicts it) | Prefer table as file truth unless HTML says otherwise |
| Extreme / perfect patterns | Identical counts across splits; AUC = 1.000 with no caveat | Stop and raise integrity concern before more polish |
| Stats method label | `multivariate` used for multi-predictor regression | Request `multivariable` unless multiple outcomes are meant |
| Display rules | *P* decimals / mean±SD format drift mid-paper | One house rule end-to-end (`Aitor-format` / 04) |
| Statistic vs threshold | Printed *t*/*F*/*z* cannot meet the voxel or cluster *P* named in Methods | Flag both loci; do not replace either number |
| Correlation *n* | *n* implied by *r* and *P* disagrees with the stated analysis *n* | Flag; do not invent *n* |
| Table → *p* spot-check | Primary between-group rows report mean±SD (or counts) and *n*, but the printed *P* cannot be roughly recovered | Back-calculate an approximate *p* (two-sample *t* from mean/SD/*n*, or χ²/Fisher from counts). In the Word comment: cite the cells used, name the approximation, label the value an **estimate**. Green = same direction + same order of magnitude; yellow = within ~1 order of magnitude or rounding ambiguity; red = opposite direction or report *p*<0.05 while estimate ≫0.2 (or the reverse). **Comment only** — do not rewrite table cells or *P*. Missing SD/*n* → `cannot_invent`. Welch / continuity correction / survival / multivariable: annotate method mismatch; escalate formal recompute to **04**. Scope: primary result tables (spot-check Table 1); do not hand-calc every multiplicity *p*. |
| Multiplicity | Many ROI or voxel correlations with no correction and no exploratory label | Ask for the family and the method, or an uncorrected label |
| Relative unit | A relative measure whose denominator is undefined | Ask for the denominator; do not interpret the variance |
| Inclusion vs scale | Cutoff excludes values that the included group's median, Q1, or minimum still shows; IQR wider than the scale | Flag; do not rewrite the cutoff or the quartile |
| Circular *P* | Selection, threshold, and group test on one cohort, *P* written as confirmatory | Ask to relabel as descriptive, or to show nested CV / bootstrap if it was run. Do not invent a corrected *P* |
| Score identity | A named score is only a transform of one metric, or nested ROIs are treated as independent | Ask to name the transform and the dependence |
| Process language | `TRAIN_RATIO`, "as stated by the source", 待补, internal labels, empty queries, placeholder scan parameters, repeated disclaimers | Ask to delete them from the body and legends. Missing facts stay comments |
| Sister papers | Shared site, scanner, or ethics; an identical table; the same biomarker with a different *P* | `06_review/qc/cross-manuscript-qc.md`. Comment the conflict; do not average *P* or invent overlap counts |

**Hard rule:** when Abstract / body / table / sister paper disagree, **comment only**. Never silently pick a value for the author. A back-calculated *n*, critical value, or table→*p* estimate in the comment is labeled an **estimate** (see §3.1).

### 3.1 Table → *p* recipes

Spot-check primary between-group rows (e.g. Table 1). Comment only; never rewrite cells or *P*.

| Band | Meaning |
|---|---|
| Green | Same direction + same order of magnitude as printed *P* |
| Yellow | Within ~1 order of magnitude, or rounding / method ambiguity |
| Red | Opposite direction, or printed *p*<0.05 while estimate ≫0.2 (or the reverse) |

Formula map (schematic):

- mean±SD + *n* (two groups) → approximate two-sample *t* → *p*
- contingency counts → χ² or Fisher → *p*
- rates / proportions → binomial CI magnitude check
- 3+ groups / Welch / continuity / survival / multivariable → magnitude-only note; escalate formal recompute to **04**

Missing SD/*n* → `cannot_invent`. Do not hand-calc every multiplicity *p*.

---


## 4. Data-integrity protocol (stop conditions)

1. Number conflict across surfaces → annotate every locus; wait for author/HTML truth.
2. Missing IRB / author / CI slots → comment (author **A**); do not fill; do not yellow-fill body.
3. Suspicious perfect patterns or possible leakage → raise before continuing polish.
4. Material defects stay in the open (comments / Major issues). Do not “quiet-fix” them away.

---

## 5. Where the long form lives

`06_review/qc/cross-manuscript-qc.md` is the run order (statement, then data, then sister papers). `05_manuscript/qc/manuscript-local-qc.md` is the check-id list. `04_analysis/qc/report-checks.md` is the statistic definition. This file stays the habit: statement first, then data, annotate only.

## 5.1 Who revises the manuscript

Ownership: see `00_orchestrator/references/ownership-contract.md`.

Decidable issues: Lee annotates for Aitee to TC-fix. The note is concrete (locator, what is wrong, the word or sentence to change) so Aitee can apply Track Changes without guessing.

Undecidable issues: Chinese 批注 plus English suggested wording and/or suggested literature (see ownership-contract). Do not invent the missing fact. call/require 03 citation-verify — do not self-certify lit. After the user picks, Aitee applies Track Changes.

---

## 5.2 Chinese manuscript-comment five slots (稿面批注; Lab-STE CM-01)

Journal English envelope stays in `review.md` (`Lines n–m:` + defect + Please…).  
**Chinese Word face comments** (author field still **A**; source tag at text start) use five fixed slots, one problem per comment:

1. **位置** — line range, or `节 第n段第m句`, or Figure/Table id. Prefer precise patterns; coarse location-only wording (e.g. methods section alone) is should_fix.
2. **问题** — what is wrong, one sentence. One problem only (no stacking multiple unrelated defects in one comment).
3. **依据** — start with 依据; name a rule id and/or data source (结果页 / 术语表 / 课题锁定 / HTML / settings.ini).
4. **修改建议** — lead with an action verb (补写 / 删除 / 改为 / 替换 / 拆分 / 合并 / 核对 / 补充数值 / 写明 / 统一 / 移至 / 重算 / 增加 / 标注 / 改用). Ban vague 酌情 / 适当 / 进一步完善 / 提升规范性 / 注意语言润色.
5. **严重度** — `must_fix` / `should_fix` / `hint`.

**Severity crosswalk (mode and G-06 ↔ CM-01).** `pre-review` and G-06 grade Blocking / Major / Minor. The fifth slot grades `must_fix` / `should_fix` / `hint`. Judge G-06 with this map:

| Mode and G-06 | CM-01 严重度 |
|---|---|
| Blocking | `must_fix` |
| Major | `should_fix` |
| Minor | `hint` |

Strip leading source tags like `[A:personal]` before counting slots; tags stay at the comment start for delivery. Quoted paste-in rewrite text is exempt from sentence-length checks.

**Example:**

> [A:personal] Methods 第 2 段第 1 句。未写连续入组。依据 ZH-TERM01 与结果页队列句。补写：连续纳入 2019 年 1 月至 2022 年 12 月的病例。must_fix。

**Bad:** 方法部分整体不够清晰，建议完善并提升规范性，同时注意语言润色。

Full thresholds and regexes: `{doc_lab_ste}\` (`config.yaml` comment_schema; `Lab-STE-SPEC.md` CM-01). Summary pointer: `05_manuscript/base/vocab/L3/lab-ste.md`. Do not vendor the lab-ste tree.

Internal-review corpus (the user's own comments; style source only): `{doc_review_corpus}\`. Do not vendor.

## 6. What this file is not

- Not a license for one-character `?` comments as the default voice.
- Not the English peer-review envelope (use `review.md`).
- Not manuscript prose rewrite (changed sentences → `05_manuscript`).
- Not reviewer-response letters (use `response.md`).
