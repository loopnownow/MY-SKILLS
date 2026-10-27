# Lab modules deep code QC — reusable rules

Subtitle: also covers a light **Code QC Core** for research data-processing scripts (R / Python / MATLAB / shell; raw → analysis-ready), adapted from stable awesome-copilot-style principles for medical research.

Source: 2026-09-07 Deep Code QC Report (`modules.zip` / `{code_modules}`) + 2026-09-22 Code QC Core absorption plan
Home: `02_data-processing/qc/coding-qc.md` (moved from `code-refactoring/references/code-qc.md`)
**Do not** put this into: MY-RULES skills.md (skill-evolution) / archived skill-harvest/qc (repo governance), `preprocess-imaging` (imaging QC), a new top-level skill, fine-id menus, parallel `02_data-processing/code-qc.md` / `coding-principles.md` <!-- negative-example -->, fine id Copilot `playbooks/quality/` / Council / CI.

## When to trigger
- Review / deep review / Deep QC / code QC for `modules` / lab stats library
- Before release; re-test after major pipeline/console/radiomics/clinical/impute changes
- Same entry as soft-coding / dry-run / refactor (`02_data-processing/advanced/coding.md`): QC first, then change, or re-test after change
- Research data-processing scripts (raw→analysis-ready) release-ready / deep review

00 only routes: see `00_orchestrator/gates.md` **G-CODE**; detail lives only in this file.

## Five axes + medical axis (Deep QC kept)
| Axis | What to review |
|------|----------------|
| Correctness | Startup, default params, formula/test choice, comment↔implementation consistency; misaligned filter/compute, wrong output, data leakage |
| Architecture | Oversized functions, coupled responsibilities, testable boundaries (**keep fully**; do not narrow to “02-only boundary”) |
| Data Safety (Security extended) | PHI/PII; secrets/tokens in code/logs/outputs; do not overwrite raw without explicit ask and versioning; output pollution; **keep** local console CORS and whether paths are project-scoped |
| Performance | High-dim correlation matrices, repeated full-table scans, needless full precompute; do not optimize without a clear perf problem |
| Testability / Verification | Unit / smoke / synthetic regression; for research scripts prefer sanity (n, dims, NA, ranges, output counts) and edge cases — **do not require** production-grade coverage |
| Medical / Statistical Integrity | **Only point to** `02_data-processing/advanced/analysis/pipeline.md` and `02_data-processing/qc/report-checks.md`; do not rewrite methods in this skill |
| Reproducibility (Core add) | Inputs, params, env, seeds, paths, outputs enough to reproduce; pin when possible; confirm train/test separation on split |
| Boundary (P2 add-on) | 02 must not own statistical modeling / manuscript writing / review QC (→ 02 / 05 / 06) |

Medical axis must cross-check (pointers; body in `02_data-processing/advanced/analysis/pipeline.md` / `report-checks.md`):
- AUC 95% CI = 1000 bootstrap; paired DeLong is a **p**, not a CI
- LASSO / pre-filter / impute / scale / NZV / corr filter: fit **inside folds**; forbid full-training-set pre-filter then CV
- VAL_MODE ∈ {refit, apply_formula, lock_threshold}; do not re-select features
- Internal split = training/test; external validation = outside hospital; ban “Development set”
- Cox optional, default off; claiming MICE requires true multiple imputation + Rubin, else rename
- Stratified impute must not use outcome-derived Group; fit transformers on train, then apply to test

## Severity (primary label + report alias)
| Primary (prefer in report) | Alias (P0–P3) | Meaning |
|---|---|---|
| **Critical** | P0 BLOCK | Startup failure, CV leakage, local console can read/write across projects, wrong/corrupt/leaked results, unsafe data handling, key step not reproducible → not release-/model-ready until fixed; **stop on Critical/P0** |
| **Required** | P1 FIX | Stats implementation boundary, selection bias, silent except, no tests, missing lock, material reliability/verification gap → fix then re-test |
| **Optional** | P2 WARN / P3 NOTE | Style/naming/small opts; maintainability, clear perf, Boundary; P3 = optional note |

Output: HTML or tabular report (ID / level[+P alias] / axis / issue / evidence path / impact / suggestion). Lead the conclusion with whether it can be a formal modeling build.
Verdict: `PASS` / `PASS_WITH_WARNINGS` / `FAIL`.

## Minimal flow (Preflight → Verdict)
```
Code / Script
    ↓
0. Preflight — I/O / env / deps + Existing Pattern First
    ↓
1. P0 Critical QC — Correctness / Data Safety / Reproducibility
                 + Medical axis when relevant
    ↓  (stop on Critical/P0)
2. P1 Verification — sanity: n, dims, NA, ranges, output counts; edge cases
    ↓
3. P1 Maintainability — naming, duplication, error handling, function duties, key comments
    ↓
4. P2 Performance / Boundary
    ↓
Verdict — PASS / PASS_WITH_WARNINGS / FAIL
```

Do not require a full run every time; large imaging, batch transforms, train/test builds prioritize P0/P1; small format conversions may take a light path.

### Existing Pattern First
Before structural change, check the project’s existing conventions (layout, naming, CONFIG style, logging and path habits); do not force an external coding style.

### Findings rules
- Cite **file / function / line** when possible
- Explain mechanism + downstream impact; do not only restate the rule name
- Insufficient evidence → **QUESTION**, not BUG
- Do not invent missing requirements
- No pure style nits when there is no reliability / reproducibility / maintainability impact
- Do not optimize without a clear perf problem

## Also record what already passed
compileall syntax, no obvious os.system/exec/pickle, list-form subprocess, patient-level split checks, VAL_MODE design intent — keep a separate “Passed” block so the report is not only findings.

## Relation to coding.md principles
Keep: CONFIG-on-top, dry-run, checkpoint, modularity, brevity, comments.
Add: deep-review flow and severity; Code QC Core (Data Safety, Reproducibility, Preflight→Verdict, P0–P3 aliases); refactor advice still “separate refactor from behavior change”.

### Submodule dry-run and no silent success
- Every reviewed submodule must have a dry-run path, or an equivalent unit-testable dry path.
- Do not swallow errors with bare `except Exception: pass` (or equivalent) so a failed run looks successful; failures must be visible.

### QC scrap → 0del
- After Deep QC / modules QC, unused caches and one-shot intermediates: class A under `{del_root}\<project>\`; others under `{del_root}` (or project `0del`). Do not leave them in `modules/` or the project root. Do not vendor the whole tree into this skill.

## Explicit do-nots
- Do not vendor whole-tree `.py` / patient tables / project Excel into GitHub
- Do not turn the Medical axis into a second copy of 02 gold standards
- Do not conflate archived skill-harvest `repo_qc.py` with this flow
- ≠ archived skill-harvest/qc; ≠ imaging-qc; ≠ 02 model/figure QC; ≠ fine id Copilot playbooks/`quality/` / Council / CI
- Do not add `02_data-processing/code-qc.md`, `coding-principles.md`, or `code-qc/` / `quality/` / `testing/` directories <!-- negative-example -->

## Post-write complexity check (stable ladder consensus)

See `coding.md` “Complexity ladder”. In Deep QC reports this may appear under Architecture / Optional (or Required when duplicating an existing module); **must not** outrank Critical.

## Critical checklist (from 2026-09-07 modules deep review; changing modules needs an explicit user ask)

- **C-01**: incomplete config-fallback keys without `settings.ini` → stats import fails (startup)
- **C-02**: full-training-set impute/scale/NZV/corr + AUC top-k before LASSO CV → fold leakage
- **C-03**: console `CORS=*` + `under_root` limited only by `GROK_ROOT` → cross-project path risk

Path pointer (do not vendor): `{code_modules}`
