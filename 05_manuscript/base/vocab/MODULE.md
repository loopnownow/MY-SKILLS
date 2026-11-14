---
name: "vocab"
domain: "05_manuscript"
owner: "05_manuscript/base/vocab/MODULE.md"
---

# vocab

Thin contract: layer names, load order, and pointers. The word lists are pack data; the advanced overrides live in `05_manuscript/advanced/vocab/`.

Lab vocabulary capability body. Load layers in order before drafting:

| Layer | Path | Role |
|---|---|---|
| L1 | `L1/` | Ban phrases / terms / patterns (+ SCI overrides pointer) |
| L2 | `L2/` | Preferred / approved English |
| L3 | `L3/` | Specialty nouns (project term-lock) |

See [README.md](README.md) for the live file list. Thin entry: [SKILL.md](SKILL.md).
Glossary evidence seat (four layers + `index.csv`) maintenance and gates:
[references/glossary-maintenance.md](references/glossary-maintenance.md).

`05_manuscript/advanced/vocab/` holds the owner's personal corpus: `05_manuscript/advanced/vocab/L2/preferred-bank.md` (frequency bank), `05_manuscript/advanced/vocab/L2/preferred-advanced.md` (recurring usage), `05_manuscript/advanced/vocab/L3/voice-habits.md` (house overrides and Chinese comment slots), and `05_manuscript/advanced/vocab/L1/sci-overrides.md`. Base keeps the machine-readable lists and the canonical bans; where an advanced row conflicts with a base ban, base wins. Do not duplicate base lists here.
