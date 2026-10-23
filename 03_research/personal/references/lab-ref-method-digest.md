# lab-ref-method-digest

**Absorbed:** 2026-10-23 from `_library/lab-ref-method/ADVICE.md` (methodology only; no RI values).
**Role:** 稿件 / 同行评审数字合理性核对 — **不是**临床决策，**不替代**医院 LIS RI。

## Live pointers (after move)

| Role | Path |
|---|---|
| Durable original | `{doc_root}\_corpus\skill-harvest\sources\library-methods-20261023\lab-ref-method\` |
| Park (pending purge) | `{DEL}\_by-project\0doc-library-methods-20261023\lab-ref-method\` |
| Data SSOT (stays live) | `{doc_root}\_library\lab-ref-ranges\` (`README` + `schema.yaml` + xlsx + `qc\gate-hooks.md`) |
| Related method | `scanner-registry-digest.md`（抽取结构先例）; Lab-STE = 语言 only |

## Corpus facts (snapshot 2026-10-19; not estimates)

- 75 docx: indicators appear as narrative + embedded Word tables — **no** cohort-level xlsx/csv in bodies.
- Indicator-family hits (any alias): special 39 · coag 29 · liver 28 · pathology 27 · renal 19 · tumor 17 · heme 14 · clinical 9.
- Theme skew imaging-first; labs often covariates / secondary endpoints.
- Magnitude after synonym merge: ~**40–80** independent concepts (not hundreds of fillable mean/SD/IQR rows).

## Feasibility bans (why full mean/SD/IQR/min/max per indicator usually fails)

1. Table 1 = **cohort summary**, not CLSI/IFCC population RI; disease distribution ≠ diagnostic cutoff.
2. No patient-level tables in body → cannot derive IQR/extrema/method-specific RI.
3. Method / unit / analyzer-dependent (ALT, creatinine, AFP, D-dimer); fabricating a "normal range" for QC is unsafe.
4. Pathology (FIGO, grade, LVI, Ki-67%) is classification / assay-specific — not lab RI.
5. Selection bias: hospital cohorts are not healthy RI donors.
6. Many papers never publish institutional RI — only binary cutoffs.

### What local papers/manuscripts *can* yield

| Product | OK? | Tag |
|---|---|---|
| Indicator inventory (aliases, units as written) | Yes | follow scanner-registry extract pattern |
| Cohort descriptive stats **with citation** | Yes | `source_type=cohort_table` — **not** `ri` |
| Author cutoff (e.g. AFP > X) | Sometimes | `study_cutoff` — not institutional RI |
| Population RI (healthy vs disease) | **No** from local corpus alone | need SOP / guideline / lit |
| Method-specific RI | Rare in body | prefer hospital SOP / IFU |
| "Normal" IQR / extrema | Only with raw or complete report | **forbid** reverse-engineering from mean±SD |

## Asia / Shanghai policy (hard)

- Prefer CN / East-Asia adults + WS/T · CMA · CSCO · OB/GYN · lab guidance when filling gaps.
- Local Shanghai hospital RI → `population=Asia/Shanghai`; national generic → `Asia/CN`.
- Western guideline RI → **separate row** `population=EU/US`; **must not overwrite** CN rows.
- Lab-facing timestamps: Asia/Shanghai (UTC+8).

## Hard bans (carry from ADVICE §4)

1. Do not invent mean/SD/IQR/min/max/ref_low/ref_high — leave blank + `04_gaps`.
2. Do not treat Table 1 disease/control means as "normal RI".
3. Do not mix assay methods in one RI row (e. of Jaffe vs enzymatic creatinine; D-dimer unit mismatch).
4. Not clinical decision support — README + xlsx header must say so.
5. Do not merge EU/US with Asia without separate `population` rows.
6. Do not rewrite `scanner-registry`; do not stuff numeric RI into Lab-STE (language only).
7. Do not auto-rewrite manuscript numbers from this library (detect → name locus → human edits).
8. Do not ingest identifiable LIS/PHI into research library / GitHub.
9. Do not bulk-fill the workbook without a signed schema.

## Not in this digest

- Concrete reference values, workbook rows, schema enums → live `lab-ref-ranges\`.
- Product/layout/pipeline history already landed 2026-10-23 — not re-copied.
