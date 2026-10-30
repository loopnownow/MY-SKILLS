---
name: medical-manuscript-review
description: >
  Advanced review upper layer (post-QC re-review). Entry for review / pre-review / peer-review / re-review.
  Response letter goes to 07_response (not here).
  Statement consistency before data consistency. Cross-manuscript overlap is commented, not invented.
  May internally call 02/03/05/07. Does not write manuscript body.
---

# Manuscript Review -- advanced upper layer (re-review)

**Route:** `advanced/route.md`. **Handoff:** `advanced/handoff.md`.

## Purpose

Find defects, write journal-system peer reviews, and run **post-QC re-review**.
Never invent rescue experiments, missing AUCs, ethics IDs, or unrun analyses.
Do not rewrite the manuscript here -- changed sentences go to `05_manuscript`.
Ownership: see `00_orchestrator/references/ownership-contract.md`.
05 and 06 call/require 03 citation-verify — do not self-certify lit.

**Reviewer response enters through `07_response` only.**

## Layer model (2026-10-30 rebind)

Flow: base thin-contract first pass (`simulate-reviewers` isolation -> `self-review` || `peer-review`; contracts in `06_review/base/`) -> **00 QC** (score, cite the `advanced/` anchor) -> **06 advanced re-review only** -> re-gate at 00.
Layering and `qc/` invocation SSOT: `00_orchestrator/references/base-vs-advanced-top-loops.md`. Gates: `00_orchestrator/gates.md`. Checks: `qc/README.md`.

Base packs may raise findings; **06 advanced owns the recipe and the English peer-review envelope** (`advanced/review.md`: opener templates, comment habits, statement-then-data protocol).
Resolution status for response letters -> **07**.

## Advanced assets

| Task | Path |
|---|---|
| English peer-review voice | `advanced/review.md` |
| Review comment habits | `advanced/review.md` |
| Cross-manuscript QC | `qc/cross-manuscript-qc.md` (invoked only by 00) |
| Word comment delivery | `advanced/word-edit.md` |
| Track Changes verify (unpack / validate / pack) | `base/track-changes/` (fine id `track-changes`) |
| Dual-review isolation workflow | `advanced/review-isolation.md` |
| Thesis review | `advanced/review.md` § Thesis review digest |
| Chinese journal score sheet | `advanced/review.md` § Chinese journal score digest |
| Response letter / resolution | **`07_response/advanced/response.md`** (moved 2026-10-17) |

## Live capability ids

- `peer-review`, `self-review`, `simulate-reviewers` -- review first-pass (`06_review/base/`)
- `revise` / `tighten-response` -- response path; **final authority 07**; bodies in `07_response/base/` (tone-polish is on-demand inside tighten-response)

## Modes

- `pre-review` / `peer-review` / `re-review` (post-QC only)
- `thesis-review` / Chinese journal score sheet
- `response` -- **moved to `07_response`**

## Internal calls

- Response letter -> `07_response`
- Wording -> `05_manuscript`
- Stats -> `02_data-processing`
- Imaging -> `02_data-processing`
- Literature -> `03_research`
- Exit -> `00_orchestrator`

## Comments / Track Changes

See `advanced/review.md` section 0. Response / re-audit resolution status -> `07_response/advanced/response.md` (07 judges).

## Not this skill

- Response letter -> `07_response`
- Manuscript prose / polish -> `05_manuscript`
- Literature / journal select -> `03_research`
- Stats / figures -> `02_data-processing`
