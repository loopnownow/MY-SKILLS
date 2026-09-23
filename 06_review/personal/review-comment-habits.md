# Review comment habits (Ying Li / Jinshan)

Personal upper layer for **审稿** / 投稿前预审（找缺陷、出批注与可执行请求）.  
Journal-facing English envelope stays in `personal-review-style.md`.  
This file is the **consistency-first** habit layer.

**Locks (2026-09-24):** do **not** teach minimal `?` / bare “核实” as the house style. Lead with **statement consistency**, then **data consistency**, then integrity stops.

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

**Hard rule:** when Abstract / body / table disagree, **comment only**. Never silently pick a value for the author.

---

## 4. Data-integrity protocol (stop conditions)

1. Number conflict across surfaces → annotate every locus; wait for author/HTML truth.
2. Missing IRB / author / CI slots → comment (author **A**); do not fill; do not yellow-fill body.
3. Suspicious perfect patterns or possible leakage → raise before continuing polish.
4. Material defects stay in the open (comments / Major issues). Do not “quiet-fix” them away.

---

## 5. What this file is not

- Not a license for one-character `?` comments as the default voice.
- Not the English peer-review envelope (use `personal-review-style.md`).
- Not manuscript prose rewrite (changed sentences → `05_manuscript`).
- Not reviewer-response letters (use `personal-response-style.md`).
