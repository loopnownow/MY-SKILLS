# Resubmit edit-whitelist + failure ledger (standards only)

**Owner:** domain seat (canonical under `07_response/qc/resubmit-edit-whitelist.md`); 00 calls only. when a **text-only / venue-resubmit** microedit mode is declared (not a full rewrite).
**Seats:** Aitee (05) applies allowed prose/TeX microedits; Victor (03) if cite changes are explicitly whitelisted; Lee (06) re-marks; Bai portal. Response letters stay **07**.
**Distill of:** ARIS `resubmit-pipeline` edit-whitelist + master ledger idea. Host-agnostic — **no** ARIS runtime / Overleaf lock-in.
**Compose:** `assurance-verdicts.md` · `05_manuscript/qc/venue-compliance-minima.md` · `venue-currency.md` · assurance layers via `06_review/qc/assurance-audit-chain.md`.

## When

Prior venue packet exists; user wants **microedits only** for a new venue / R&R text pass with structure frozen. If framework/experiment change is needed → leave this mode; use normal 02/05/06 path.

## Edit-whitelist (binding)

Declare allowed paths and forbidden operations **before** microedits. Rejects go to the improvement log; never silent.

Minimal shape (illustrative — adapt to docx/TeX layout):

```yaml
allowed_paths:
  - "sec/*.tex"          # or manuscript body paths
  - "main.tex"
forbidden_paths:
  - "**/*.bib"           # unless user explicitly opens cites
  - "templates/**"
  - "../*Submission/**"  # prior packets immutable
forbidden_operations:
  - new_cite
  - new_bibitem
  - numerical_claim      # no new metrics not in EXPERIMENT / HTML
rationale: "Resubmit: text-only microedits; structure frozen."
```

**PASS:** every diff ⊆ whitelist; `rejected_by_edit_whitelist` listed when blockers hit.
**FAIL:** out-of-whitelist edit applied, or new numerical claim without 02 evidence → rollback **05** (and/or 02).

## Failure / verdict ledger

At `assurance: submission`, keep a master ledger (e.g. `RESUBMIT_REPORT.md` / `.json`) pointing at audits run (claim / citation / kill-argument / compile) + open obligations. Use six-state verdicts from `assurance-verdicts.md` (`PASS`/`WARN`/`FAIL`/`BLOCKED`/`ERROR`/`NOT_APPLICABLE`). Optional runtime pause state `USER_DECISION` for human checkpoints — not a new G-* id.

| Typical FAIL/BLOCK | Recovery |
|---|---|
| Whitelist violation | Revert diff; re-run microedit under whitelist |
| Critical kill-argument still open under text-only | User: relax constraints, change venue, or escalate to full rewrite |
| Missing review bank / prior packet | BLOCKED → supply bank or exit resubmit mode |
| Currency / template stale | `venue-currency.md` → 03 find-journal / 05 write-paper |

## Soft pointers

- Venue minima: `05_manuscript/qc/venue-compliance-minima.md`
- Stage map: `research-stage-artifacts.md`
- Review loop: `06_review/qc/review-loop-state.md`
- 07 response (if letter needed): `07_response/` — not this whitelist

*Attribution: ARIS resubmit-pipeline edit-whitelist + ledger; lab gates/seats authoritative.*
