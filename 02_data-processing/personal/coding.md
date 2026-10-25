# Code optimization and refactor

Personal layer: `02_data-processing/personal/coding.md` (moved from `code-refactoring/SKILL.md`; complexity ladder merged below).
Deep code QC detail: `../qc/coding-qc.md`. Do not create a new top-level skill or register a coarse id outside the five seats.

## When it applies
- Soft-coding (CONFIG on top)
- Large trim / remove dead parts
- Checkpoint resume / parallel / CUDA
- dry-run
- **Deep review / Deep QC / modules code QC** (five axes + medical integrity **by reference** to 02)
- Write-time code ladder / post-write complexity check (stable method absorption, not an external fine id)
- Research data-processing scripts (R/Python/MATLAB/shell; raw→analysis-ready) release-ready QC

## Capability map

| Task | Path |
|---|---|
| Soft-coding + dry-run template | `{code_root}\_infra\_templates\soft_code_template.py` |
| Deep code QC (five axes / severity / Critical + Code QC Core) | `../qc/coding-qc.md` |
| Write-time ladder + intensity / guardrails | “Complexity ladder” below |

Medical / Statistical Integrity: **only reference** `02_data-processing/qc/report-checks.md` and `02_data-processing/personal/analysis/pipeline.md`; do not copy gold standards into this skill.

## Core principles

Authoritative standing rules (CONFIG on top / comment only config + how-to-run / no fallback / multi-module optional via config / dry-run / checkpoint resume) → MY-RULES `My rule.md` §3. Below is the skill-side expansion and template pointers.

### 1. Soft-coding (CONFIG on top)
- Paths, keywords, and params live in a top-of-file config block (config before logic)
- Avoid hard-coding; comment config fields
- Multi-module OK; modules may be optional via config switches

### 2. Brevity + ladder
- Minimal necessary code; do not build abstractions for one-off use
- Before writing, stop at the first “yes” on the Complexity ladder below
- Medical entrypoints: **ultra** intensity disabled

### 3. Checkpoint resume
- Skip already-processed results; check intermediate files or done markers

### 4. Parallel / CUDA
- Independent tasks may run in parallel; watch memory

### 5. Comment rules
- **2026-10-24 decision kept**: comments = config-field meaning + how to run; **do not** write long business “why”. Authority → `{RULES}` `My rule.md` §3.
- Comment **only**: (a) config-field meaning; (b) how to run the script. No long business-logic comments.

### 5b. No fallback
- No fallback / silent degrade; do not try-except-swallow then take a default path; failures must be loud

### 6. Dry Run
- Trial run first; print the operations that would run for confirmation

### 7. Deep QC
- Triggers, severity, Preflight→Verdict, Data Safety / Reproducibility: `../qc/coding-qc.md`
- Scrap → `0del`, submodule dry-run, no silent success: `../qc/coding-qc.md`
- Critical/Required/Optional are primary labels; P0–P3 are report aliases
- Boundary: ≠ archived `skill-harvest/qc` / MY-RULES skills.md (skill-evolution); ≠ `preprocess-imaging`; ≠ 02 model/figure QC; ≠ Copilot playbooks/`quality/`
- Do not vendor the whole `{code_modules}` tree
- 00 routing: `gates.md` **G-CODE**

## Bundled template
- `{code_root}\_infra\_templates\soft_code_template.py` — soft-coding + checkpoint resume + dry-run template

---

## Complexity ladder (absorbed from complexity-ladder.md)

Absorbed stable consensus (Ponytail-style lazy ladder). **Not** a registry fine id / coarse id.

## When writing (stop at first yes)

1. **YAGNI** — Is this needed? If no, skip.
2. **Reuse in-repo** — Same capability already in the project?
3. **Stdlib** — Language standard library enough?
4. **Platform native** — OS / runtime already provides it?
5. **Existing dependency** — Already in env/`requirements`? Do not add deps lightly.
6. **One-liner** — Clear few-line expression enough?
7. **Minimal new code** — Only then write the smallest working code.

Aligns with: soft-coding, dry-run, CONFIG-on-top, no one-off abstractions.

## After writing (complexity check)

Remove/merge when medically unnecessary:

- Extra new dependencies
- Duplicate logic already in-repo
- Speculative wrappers / factories used once
- Dead "maybe later" features
- Needless indirection / over-config

Severity: usually **Optional**; clear duplicate of an existing module may be **Required**. Never outrank **Critical** (leakage, dry-run broken, startup failure, QC bypass).

## Intensity

| Mode | When | Behavior |
|---|---|---|
| **full** (default) | Refactors / figure scripts | Strict ladder, few new deps |
| **lite** | User confirmed new feature | Suggest lazier options; do not block confirmed need |
| **ultra** | — | **Disabled** for medical/stats entrypoints |

## Medical guardrails (hard)

Do **not** delete or weaken for shortness:

- train/test (/ external) isolation; seeds; artifacts / reproducibility dumps
- dry-run / `--execute`; CONFIG-on-top; checkpoint
- Stats & data QC (point to `02_data-processing/personal/analysis/pipeline.md` / `report-checks.md`; do not rewrite gold standards here)
- Registration / habitat hard QC; Pictologics constraints

**Minimal necessary complexity ≠ fewest lines.** Correctness, reproducibility, auditability first.
