# 05 route -- vocabulary + post-QC polish chain

**Canonical entry:** `../SKILL.md`.

## Layering (2026-10-30 rebind)

- **base thin first pass:** `write-paper` must **load vocab** (`05_manuscript/base/vocab/`) before drafting; the pack itself carries scope, bans, and pointers only. the non-routable `check-reporting` body (`05_manuscript/qc/check-reporting/`) loads the same vocab before a checklist pass.
- **00 QC** - gates.md checks **(b)** vocab loaded; **(d)** polish / De-AI when requested (advanced De-AI pass); scores come from `05_manuscript/qc/` and cite the advanced anchor to fix at.
- **05 advanced revise loop:** post-QC De-AI (report-only lint, then de-AI) plus Aitor-format / voice. Procedure: `process/polisher-sections.md` section De-AI pass. This layer owns the house voice, the contract, and the authority (no registry fine id).

## Vocabulary (body in base; advanced pointer at `vocab/README.md`)

**Evidence seat (not criteria):** `GLOSSARY_ROOT` = `_Docs\_library\glossary` — **四层** (`words` / `sentences` / `paragraphs` + `sections` pointer pages) + `index.csv`; `banks\` evidence-only. Criteria stay in `base/vocab/` (+ named advanced). Prefer env `GLOSSARY_ROOT`; do not use a separate glossary-banks alias in new text (that alias was retired 2026-11-01; use `GLOSSARY_ROOT\banks` or `{doc_glossary}\banks`).

1. **L1 words:** `05_manuscript/base/vocab/L1/ban-phrases.md` + `ban-terms.yaml`
2. **L1 patterns:** `05_manuscript/base/vocab/L1/patterns.md`
3. **L1 SCI overrides:** `05_manuscript/base/vocab/L1/sci-overrides.md`
4. **L2 preferred:** base `05_manuscript/base/vocab/L2/preferred.md` (thin pointer) + `approved-en.tsv`; personal bank: `05_manuscript/advanced/vocab/L2/preferred-bank.md`; advanced usage with counts: `05_manuscript/advanced/vocab/L2/preferred-advanced.md`
5. **L2 paragraph/set habits:** `voice-portrait.md`; IMRAD/DOCX -- `Aitor-format.md`
6. **L3 specialty + Lab-STE:** `05_manuscript/base/vocab/L3/lab-ste.md`

## Study-type route (writing constraints)

Load `process/study-type.md` before `write-paper` drafting, on this same route (not a second router). It names a coarse study type from the locked design and attaches wording and distinction constraints. Claim planning stays in `process/claim-map.md`. Reporting-guideline completeness stays in `05_manuscript/qc/reporting-guideline-route.md`.

## Process (05-owned)

- `process/intake-brief.md` -- writing-entry summary of known constraints (not a QC gate)
- `process/study-type.md` -- coarse study-type writing constraints (not a second router)
- `process/claim-map.md` -- pre-draft claim-evidence-wording-location plan (not a QC gate)
- `process/figure-table-plan.md` -- which claims need a main-text figure or table (not a QC gate)
- `process/method-experiment-align.md` -- two-way aim-methods-results-interpretation trace (not a QC gate)
- `process/evidence.md` -- evidence request + I/D consumption
- `process/citation-and-language.md`
- `process/polisher-sections.md`

## Post-QC polish chain (05)

When polish requested after 00 QC:

1. Run De-AI pass (report-only lint table first, then the de-AI pass; `process/polisher-sections.md`)
2. Apply / adjudicate with `Aitor-format.md` + `voice-portrait.md` (advanced authority)

## Cooperation

- See `handoff.md` (02/03/06/07/00).
- Manuscript local QC / scoring checklists live in ``qc/`` (invoked only by 00 at Gate time). Disclaimer/CYA/未做-class → `qc/anti-leak-placeholders.md` AL-5 (body forbidden; 批注 + 建议修改后内容).

## Root keep

`Aitor-format.md` / `voice-portrait.md` / `route.md` / `handoff.md` / `vocab/README.md` (pointer) / `process/`

## Bank references (2026-10-23)

- `references/bank-voice.md` — voice habits from quotes (pointer from `voice-portrait.md`)
- `references/bank-patterns.md` — revision-pattern taxonomy (7255-unit summary)

## _Docs writing-rules absorb (2026-10-23)

- Hard constraints: `references/writing-rules-hard.md` (Track Changes; no invented docx/pdf layout; do not alter outcome/cutoff/covariate/missingness semantics).
- Authority map (retargeted after seat move): `references/writing-rules-map.md`.
- Optional base pointer: `../base/write-paper/references/docs-writing-rules-pointer.md`.
