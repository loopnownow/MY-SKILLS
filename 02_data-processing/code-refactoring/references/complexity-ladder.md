# Complexity ladder (absorbed methodology)

Absorbed stable consensus (Ponytail-style lazy ladder). **Not** a 01 mount / B coarse id.

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
- Stats & data QC (point to `04_analysis`; do not rewrite gold standards here)
- Registration / habitat hard QC; Pictologics constraints

**Minimal necessary complexity ≠ fewest lines.** Correctness, reproducibility, auditability first.
