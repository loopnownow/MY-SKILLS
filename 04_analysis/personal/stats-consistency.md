# Stats consistency (reported results)

Use when polishing or reviewing **already reported** numbers (Table 1, NHST lines, HR/OR with CI).  
Raw measurement tables → `02_data-processing/table-qc/`.

## Division of labor

| Mechanism | Owns |
|---|---|
| G-FACT (00) | Pipeline number drift across 02→04→05→06 |
| This note | Academic reporting consistency signals |
| `table-qc` (02) | Raw measurement tables |
| `stats-checklist.md` | Lab reporting style (body/figures) |

## Checks

### GRIM / Table 1 mean vs N
- See skill-library extract / scrutiny: https://github.com/lorenz-walthert/scrutiny
- Flag means that cannot arise from integer sum / N at the reported decimals
- Integer-sum models only; not every continuous physical mean

### NHST vs reported p
- Upstream: https://github.com/hplisiecki/statcheck_python
- Consistency error: statistic and p disagree
- Decision error: significance call flips after recompute

### Effect size 95% CI vs p
- Log-scale SE ≈ (ln U − ln L) / (2×1.96); Z ≈ ln(effect)/SE
- Signal if CI crosses null while p is called significant (or magnitude mismatch)
- Rounding / one-sided / adjusted p can explain mild gaps

### Optional batch p-curve
- Pile-up of significant p near 0.04–0.05 is a selective-reporting **risk signal** in a batch
- Not a default gate for a single small study

## Into 06

Self-review / peer-review: cite this note; do not restate algorithms in 06.
Runnable helpers stay with Loopnow/Build — not A repo scripts.
