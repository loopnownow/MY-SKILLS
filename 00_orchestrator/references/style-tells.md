# style-tells -- AI-tell catalogue behind the G-05 `style-lint` sub-check

Scope: English manuscript prose in Abstract / Introduction / Background / Discussion / Conclusion.
Methods, Results, tables, figure legends and references are NOT scanned (passive voice,
enumerations and numeric reporting are convention there, not AI tells).

The machine-readable lists live in ONE place: `CONFIG` in `00_orchestrator/scripts/style_lint.py`.
This page explains the rules; it does not duplicate the lists (one fact, one home).

## Four scored groups (1 point each; pass = 4/4)
1. **vocabulary** -- ALWAYS-flag words, plus LIMITED words (fine once, damning when repeated)
2. **constructions** -- "not just X, but Y", "more than just", "that's where X comes in",
   stacked hedges ("may potentially"), self-answering questions ("The result?")
3. **dash cadence** -- more than one em-dash in a single sentence (en-dash ranges are fine)
4. **rule-of-three rhythm** -- more than 3 lowercase triples ("faster, smarter, and better");
   parenthetical covariate lists and acronym lists are ignored

## Owner rulings (do not silently reverse)
- `robust`, `landscape`, `leverage`, `labeled`/`labelled`, `locked` are AI vocabulary: flagged everywhere scanned, no default exemption.
- `robustness` is NOT matched: "feature robustness" (ICC / test-retest) is standard radiomics wording.
- `elevate` / `enhance` are not listed: "elevated ALT", "contrast-enhanced".
- Calibrated hedging is house style: one may / suggest is fine; only *stacked* hedges are flagged.
- A genuine term of art (e.g. "high-leverage point") is exempted per phrase via `ALLOW_PHRASES`, never by deleting the rule.

## Fix rule
Use a plainer word, not a synonym. leverage -> use. labeled -> classified as / assigned to / named. locked -> fixed / decided / settled. robust -> say what is stable (e.g. "stable across
scanners", "adjusted for X"). landscape -> name the concrete thing. Never "fix" passive voice in Methods.

## Boundaries
- **Never invent proof** is enforced by G-FACT (every number traces to a source table / result file).
  There is deliberately no number+noun regex here: every manuscript sentence contains numbers.
- **Offline only.** Manuscript text never leaves the machine; there is no rival-model cleanse step.
  A test fails the build if the linter imports anything network- or subprocess-capable.
- **Report, do not rewrite.** Hits become Word comments (author A, source tag `style-lint`); the user decides.

## Provenance
Mechanism and part of the term catalogue adapted from ItsssssJack/SlopMonster (MIT), which is itself
built on Wikipedia "Signs of AI writing" (WikiProject AI Cleanup). Upstream notice retained:
MIT License Copyright (c) 2026 Jack Roberts Permission is hereby granted, free of charge, to any person obtaining a copy
