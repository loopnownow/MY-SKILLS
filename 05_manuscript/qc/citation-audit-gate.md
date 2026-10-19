# Citation audit gate (05 qc · Layer 4 · extends G-CIT)

**Owner:** `00_orchestrator` at G-LIT / G-CIT / Integrity · pre-06.
**Seat:** Victor (03) runs verify; Aitee (05) wording; Lee (06) may require G-CIT-2 inside review.
**Compose existing:** `refs-verified.md` (RV-*), `03_research/personal/citation-verify.md` (G-CIT-1/2). Do not replace them — this gate adds three-axis + six-state emit.
**Distill of:** ARIS `citation-audit`.

## Purpose

Every citation: **exists**, **metadata correct**, **context-appropriate** (supports the surrounding claim).

## When

- After bibliography/claim→ref table stable (not on half-draft placeholders).
- G-CIT-1 before Gate · 05 done; G-CIT-2 inside 06 (G-CIT-1 does not waive G-CIT-2).
- Mandatory emit at `assurance: submission` / `conference-ready`.

## Inputs

- Bib / reference list + citing manuscript sentences
- DOI/Crossref / PubMed lookups (real web — not memory)
- Optional soft-only: freeze bib; rewrite body sentences only (resubmit-style) — P1 note if full whitelist absorb later

## Three axes

| Axis | PASS | FAIL / action |
|---|---|---|
| **Existence** | DOI/PMID/arXiv resolves | REMOVE / hallucinated |
| **Metadata** | author / year / title / venue match canonical | FIX |
| **Context** | cited work actually supports the sentence | REPLACE or soften sentence |

Per-entry ledger: `KEEP` | `FIX` | `REPLACE` | `REMOVE`.

## Pass / fail (overall six-state)

| State | When |
|---|---|
| `PASS` | All KEEP (or FIX already applied) |
| `WARN` | FIX-only metadata drift remaining |
| `FAIL` | Any REPLACE/REMOVE (wrong-context or hallucinated) open |
| `BLOCKED` | Bib/refs unreadable but cites present |
| `NOT_APPLICABLE` | No citations in packet |
| `ERROR` | Lookup/reviewer failure |

Uncited bib entries (optional detect) are **advisory only** — never upgrade overall verdict alone. RV-* Critical unresolved still FAIL via `refs-verified.md`.

## Fail → rollback

- FAIL → 03 Victor (verify/substitute) + 05 Aitee (wording); G-LIT recovery.
- BLOCKED → fix bib path / encoding; re-run.
- 05/06 must **not** self-certify lit.

## Verdict artifact

- `CITATION_AUDIT.json` (+ `.md`)
- `details.per_entry[]` with axis_failures
- Cross-link RV-1…4 and G-CIT claim→ref table in summary

*Attribution: ARIS citation-audit (wanshuiyin/Auto-claude-code-research-in-sleep); lab G-CIT / refs-verified remain authoritative for radiology workflow.*
