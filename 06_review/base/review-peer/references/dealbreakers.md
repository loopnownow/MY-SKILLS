# Dealbreakers — the issues that decide the outcome

Detect these first. Any one can cause desk-reject or major revision. For each: how to spot it,
and the fix to hand back.

| Dealbreaker | How to detect | Fix to hand back |
|---|---|---|
| **Data leakage** | Selection/normalisation/harmonisation on full cohort; augmentation across split; test-set tuning | Re-fit all data-dependent steps inside training; re-run; report honestly (→ mounted `02-radiomics-habitat` leakage-audit) |
| **No patient-level split** | Slice/lesion-level split; same patient in train+test | Re-split at patient level; re-evaluate |
| **No external validation (when the claim needs it)** | Only internal CV; generalisability claimed | Add external/temporal/geographic cohort, or bound the claim to internal (→ `03-design-experiment`) |
| **Undefined / circular labels** | Reference standard vague; model learns from the report it replaces | Define ground truth, readers, blinding; remove circularity |
| **Unclear segmentation** | No reader info, no reproducibility, no stability filter | Add reader protocol + ICC/Dice + stability filter (→ mounted `02-imaging-qc` / `02-radiomics-habitat` `references/reader-protocol.md` and `reproducibility-qc.md` |
| **Incomplete statistics** | AUC only; no CIs; no calibration/DCA; multiplicity ignored | Add CIs, calibration, decision-curve, multiplicity control (→ `04-stats-guide` / `04-model-eval`) |
| **Overclaiming** | "Clinically applicable" from retrospective AUC; "causal"/"first" | Re-word to bounded claims (→ `05-write-manuscript` / `05-write-polish`) |
| **Weak/absent baseline** | DL "wins" vs a strawman or nothing | Add a fair, tuned baseline (radiomics/clinical/radiologist) |
| **Prevalence/spectrum mismatch** | Artificial 1:1; enriched cohort claimed as screening | Report real prevalence; bound the setting |
| **Data/code unavailable without reason** | Bare "on request"; no accession | Provide repository/accession or a justified controlled-access route (→ `02-imaging-io` (`data.md`) |
| **Ethics inconsistency** | Sharing promise exceeds consent; no approval | Align ethics ↔ availability; supply approval/consent (→ `05-write-manuscript` `radiology-ethics/approval-consent.md`) |

## Triage rule

1. Scan for the table above **before** detailed review.
2. If a Blocker exists, say so up front — cosmetic comments are secondary until it's resolved.
3. Pair every Blocker with the concrete fix and the skill that produces it.
