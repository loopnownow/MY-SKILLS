---
name: paper-claim-audit
description: >
  Zero-context verification that every number, comparison, and scope claim in the
  manuscript matches primary evidence tables/outputs. Fresh reviewer; no prior
  chat or summaries. Medical/clinical manuscript default (Word + tables).
owner: "06_review/base/self-review/MODULE.md"
---

# Paper claim audit (zero-context)

Advisory fidelity check: does the manuscript report primary evidence truthfully and at display precision? Not a scientific-support skill (that is design/stats packs). Not peer review of others' papers (`peer-review`).

## CONFIG (edit per run)

```text
MANUSCRIPT_PATH =   # path to .docx (preferred) or exported markdown
MANUSCRIPT_VIEW = accept   # pandoc: --track-changes=accept | all | reject
                           # State which view was used in the audit report header.
EVIDENCE_GLOBS  = Table*.xlsx, *.csv, *-results.html, R/Python primary outputs
                  # NOT wandb/, metrics.json ML pipeline dumps, executor summaries
ROUNDING_RULE   = display-precision only (standard round-to-shown)
MULTIPLE_TEST   = # e.g. FDR q<0.05 / Bonferroni / none — must be consistent
                  # across abstract, body, and tables
```

## Core principle

**Zero-context fresh reviewer.** Auditor receives only:

- Manuscript text (from Word via `pandoc --track-changes=<MANUSCRIPT_VIEW>`)
- Primary evidence files matching `EVIDENCE_GLOBS`

Auditor must **not** receive:

- Prior chat, executor summaries, improvement logs, narrative reports
- Prior audit verdicts as “expected” answers
- wandb / metrics.json ML pipeline artifacts as medical evidence

Prefer a **fresh session**. Same-family / same-thread review is **interim only** (label the report). FAIL/WARN always need human check against primary tables.

## Workflow

### 1. Collect (paths only — no interpretation)

- Convert docx → text/md with pandoc; record `MANUSCRIPT_VIEW` in the report.
- Gather evidence: Table xlsx/CSV, R/Python primary outputs, `*-results.html`.
- Exclude summaries and chat history.

### 2. Extract every quantitative / scope claim

For each: location, exact paper text, claimed value or comparison.

### 3. Trace to evidence

Per claim:

| Field | Content |
|---|---|
| location | section / table / figure / abstract |
| paper_text | exact quote |
| evidence_file | primary file path |
| evidence_value | value in evidence |
| status | exact_match / rounding_ok / mismatch / missing_evidence / ambiguous / scope_overclaim / … |

### 4. Medical failure modes (check explicitly)

1. **Number inflation** — paper exceeds evidence beyond display-precision rounding
2. **Cherry-pick** — best cutoff / model / subgroup presented as primary without disclosure
3. **Split / cohort mismatch** — train/val/test or cohort definition differs from Methods
4. **N staircase mismatch** — inclusion → exclusion → final N does not add up
5. **Arithmetic error** — AUC delta, OR/HR, % with wrong denominator
6. **Caption vs content** — caption disagrees with table/figure
7. **Scope overclaim** — e.g. 证明 (prove) / 独立预测因子 (independent predictor) / “validates” in single-center retrospective without support

Also check:

- **p vs 95% CI contradiction** (significant p with CI crossing null, or reverse)
- **Multiple-testing threshold** consistent across abstract / body / tables (`MULTIPLE_TEST`)
- **Same number** consistent across abstract / body / tables / response letter

### 5. Verdict (advisory, not blocking)

| Verdict | Meaning |
|---|---|
| PASS | Material claims reconcile |
| WARN | Rounding drift, ambiguous mapping, or minor inconsistency — flag for human |
| FAIL | Material mismatch, inflation, staircase error, or overclaim |

`PASS` / `WARN` / `FAIL` do **not** block the pipeline by themselves. FAIL/WARN → human vs primary tables before submission-ready.

### 6. Report

Write `PAPER_CLAIM_AUDIT.md` (and optional `.json` if useful) with:

- Date (Asia/Shanghai), manuscript path, `MANUSCRIPT_VIEW`, auditor session type (fresh / interim)
- Overall verdict + counts by status
- Issues with location / paper / evidence / fix
- Full claim table

### When to run

- Before submission / after major manuscript number changes
- After revision letter that changes numbers → re-run (handoff from `07_response/base/revise`)
- Not on a wall-clock timer; re-fire only when paper or evidence changed

## Cut from upstream (not in this pack)

- render-html pipeline as required step
- file-hash / submission JSON validators / assurance-contract schemas
- Codex-specific MCP reviewer wiring
- wandb / metrics.json as default evidence
- Blocking submission gates inside this skill

## Key rules

- Display-precision rounding only.
- Fresh session preferred; same-family = interim label.
- Evidence = primary medical tables/outputs, not ML pipeline dumps.
- Verdict advisory; FAIL/WARN need human check.
