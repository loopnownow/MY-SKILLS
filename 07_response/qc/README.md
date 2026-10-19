# 07_response / qc

**Owner:** `00_orchestrator` only loads these at Gate time.
**Domains/specialists do not self-certify via this folder.** Response drafting tools stay in `base/` fine-ID packs; these are thin pointers to existing gate-ish references (not duplicated bodies).

| File | Gate(s) / use |
|---|---|
| `response-audit.md` | Pointer to `base/review-response/references/response-audit-gate.md` (00 gate-time audit standard) |
| `tighten-qa.md` | Pointer to `base/tighten-response/references/qa-checklist.md` (00 gate-time tighten QA) |

Capability routing (not qc self-certify): `07_response/base/routing.md` (decision-type × task-mode; Aitee owns 07).

### Soft pointer (ARIS P1)

Text-only resubmit whitelist / failure ledger (not a 07 self-certify gate): `00_orchestrator/qc/resubmit-edit-whitelist.md`. Response letters remain Aitee **07** (`base/routing.md`); do not put resubmit standards under `personal/`.
