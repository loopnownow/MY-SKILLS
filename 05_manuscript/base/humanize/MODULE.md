---
name: "humanize"
domain: "05_manuscript"
trigger: ["humanize", "去AI味", "de-AI", "AI patterns"]
outputs: ["pattern_scan", "rewritten_prose"]
owner: "05_manuscript/base/humanize/MODULE.md"
---

Generic AI-pattern removal for manuscripts and response letters, plus a report-only language lint.

**Contract only.** This pack owns the phase names, the invariants, and the pointers. The procedure (phase detail, fix rules, gate verdicts, detector status, language-lint table) lives in `05_manuscript/advanced/process/polisher-sections.md` § De-AI pass. Advanced de-AI lists win over this pack.

Not general copy-editing: venue house style is `write-paper`. Not scientific-quality review, not journal formatting, not translation.

Absorbed 2026-10-17 (MIT). See `LICENSE_NOTE.txt`.
Absorbed 2026-10-25: the `polish-language` pack (its Introduction/Discussion lint is the advanced language lint).

# Humanize (thin contract)

## Phase names

`Scan` -> `Report` -> `Fix` -> `Verify`. Numbers, severity bands, density target, verdict codes, and the two detector commands are in the advanced De-AI pass section; do not restate them here.

## Hard bans (invariants)

1. Numbers, statistics, P values, confidence intervals, and clinical facts come out **identical**.
2. Citations are **never** added, removed, or relocated.
3. No new claim, no removed claim, no reinterpretation. A passage that cannot be fixed without changing meaning is left as it is and flagged for the user.
4. Domain terminology stays intact ("convolutional neural network", "apparent diffusion coefficient", "Fleiss' kappa").
5. Out of scope: journal formatting, house style, scientific judgement, translation.
6. de-AI ban lists are not restated here: `05_manuscript/base/vocab/L1/ban-phrases.md` plus the advanced overrides in `05_manuscript/advanced/vocab/`.

## Pointers

| Need | Path |
|---|---|
| Procedure, fix rules, gate verdicts, language lint | `05_manuscript/advanced/process/polisher-sections.md` § De-AI pass |
| All 27 pattern definitions, watch words, examples, detection greps, per-pattern fixes, section priorities | `references/ai_patterns.md` (read before scanning) |
| Runnable checks | `scripts/check_rewrite_fidelity.py`, `scripts/check_sentence_variety.py` |
| Overclaim / hedging sweep while polishing | `references/style-guardrails.md` |
| Number formatting | `references/stat-reporting.md` (house authority: `05_manuscript/advanced/Aitor-format.md`) |
| Scored checklist at gate time | `05_manuscript/qc/manuscript-local-qc.md` |
