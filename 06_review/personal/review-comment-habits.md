# Review comment habits (Ying Li / Jinshan)

Personal upper layer for **审稿** / 投稿前预审（找缺陷、出批注与可执行请求）.  
Journal-facing English envelope stays in `personal-review-style.md`.  
This file is the **consistency-first** habit layer.

**Locks (2026-09-24):** do **not** teach minimal `?` / bare “核实” as the house style. Lead with **statement consistency**, then **data consistency**, then integrity stops.

**Locks (2026-10-02):** on a data conflict, annotate every locus. Do not invent a replacement number. Pre-submit classes and sister-paper checks: `cross-manuscript-qc.md`. Check ids: `05_manuscript/personal/pre-submit-consistency.md`. call/require 03 citation-verify — do not self-certify lit.

**Locks (Word revise ownership):** All manuscript Track Changes are owned by Aitee (05). Lee must not self-revise as default. Lee marks/comments; Aitee applies Track Changes. Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default. Undecidable issues: Chinese 批注 body plus attached English suggested wording and/or suggested literature. Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.

---

## 1. Overall portrait (reviewer side)

Review like a careful editor + statistician: numbers, abbreviations, reference hygiene, legend placement, and causal vs association wording.

- Prefer **actionable** comments: what is wrong, where, and what to do.
- Prefer finite choices at decision points; still stop for real ambiguity.
- Uncertain facts: mark `cannot_invent` / ask — never pick a number silently.
- Mount vs lab conflict: write both options in the comment; **user decides** (`personal-review-style.md` §0).

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
| Multiplicity | Many ROI or voxel correlations with no correction and no exploratory label | Ask for the family and the method, or an uncorrected label |
| Relative unit | A relative measure whose denominator is undefined | Ask for the denominator; do not interpret the variance |
| Inclusion vs scale | Cutoff excludes values that the included group's median, Q1, or minimum still shows; IQR wider than the scale | Flag; do not rewrite the cutoff or the quartile |
| Circular *P* | Selection, threshold, and group test on one cohort, *P* written as confirmatory | Ask to relabel as descriptive, or to show nested CV / bootstrap if it was run. Do not invent a corrected *P* |
| Score identity | A named score is only a transform of one metric, or nested ROIs are treated as independent | Ask to name the transform and the dependence |
| Process language | `TRAIN_RATIO`, "as stated by the source", 待补, internal labels, empty queries, placeholder scan parameters, repeated disclaimers | Ask to delete them from the body and legends. Missing facts stay comments |
| Sister papers | Shared site, scanner, or ethics; an identical table; the same biomarker with a different *P* | `cross-manuscript-qc.md`. Comment the conflict; do not average *P* or invent overlap counts |

**Hard rule:** when Abstract / body / table / sister paper disagree, **comment only**. Never silently pick a value for the author. A back-calculated *n* or critical value in the comment is labeled an estimate.

---

## 4. Data-integrity protocol (stop conditions)

1. Number conflict across surfaces → annotate every locus; wait for author/HTML truth.
2. Missing IRB / author / CI slots → comment (author **A**); do not fill; do not yellow-fill body.
3. Suspicious perfect patterns or possible leakage → raise before continuing polish.
4. Material defects stay in the open (comments / Major issues). Do not “quiet-fix” them away.

---

## 5. Where the long form lives

`cross-manuscript-qc.md` is the run order (statement, then data, then sister papers). `05_manuscript/personal/pre-submit-consistency.md` is the check-id list. `04_analysis/personal/stats-consistency.md` is the statistic definition. This file stays the habit: statement first, then data, annotate only.

## 5.1 Who revises the manuscript

Lee marks/comments; Aitee applies Track Changes. Lee must not self-revise as default.

Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default. The note is concrete (locator, what is wrong, the word or sentence to change) so Aitee can apply Track Changes without guessing.

Undecidable issues: Chinese 批注 body plus attached English suggested wording and/or suggested literature. Do not invent the missing fact. Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed. call/require 03 citation-verify — do not self-certify lit. After the user picks, Aitee applies Track Changes.

---

## 5.2 Chinese 稿面批注五槽 (Lab-STE CM-01)

Journal English envelope stays in `personal-review-style.md` (`Lines n–m:` + defect + Please…).  
**Chinese Word face comments** (author field still **A**; source tag at text start) use five fixed slots, one problem per comment:

1. **位置** — line range, or `节 第n段第m句`, or Figure/Table id. Prefer precise patterns; coarse location-only wording (e.g. methods section alone) is should_fix.
2. **问题** — what is wrong, one sentence. One problem only (no stacking multiple unrelated defects in one comment).
3. **依据** — start with 依据; name a rule id and/or data source (结果页 / 术语表 / 课题锁定 / HTML / settings.ini).
4. **修改建议** — lead with an action verb (补写 / 删除 / 改为 / 替换 / 拆分 / 合并 / 核对 / 补充数值 / 写明 / 统一 / 移至 / 重算 / 增加 / 标注 / 改用). Ban vague 酌情 / 适当 / 进一步完善 / 提升规范性 / 注意语言润色.
5. **严重度** — `must_fix` / `should_fix` / `hint`.

Strip leading source tags like `[A:personal]` before counting slots; tags stay at the comment start for delivery. Quoted paste-in rewrite text is exempt from sentence-length checks.

**Example:**

> [A:personal] Methods 第 2 段第 1 句。未写连续入组。依据 ZH-TERM01 与结果页队列句。补写：连续纳入 2019 年 1 月至 2022 年 12 月的病例。must_fix。

**Bad:** 方法部分整体不够清晰，建议完善并提升规范性，同时注意语言润色。

Full thresholds and regexes: `D:\0Grok\0doc\04_实验室参考\lab-ste\` (`config.yaml` comment_schema; `Lab-STE-SPEC.md` CM-01). Summary pointer: `05_manuscript/personal/lab-ste.md`. Do not vendor the lab-ste tree.

## 6. What this file is not

- Not a license for one-character `?` comments as the default voice.
- Not the English peer-review envelope (use `personal-review-style.md`).
- Not manuscript prose rewrite (changed sentences → `05_manuscript`).
- Not reviewer-response letters (use `personal-response-style.md`).
