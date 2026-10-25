---
name: "revise"
domain: "07_response"
trigger: ["回复审稿人", "point-by-point", "回信", "rebuttal"]
outputs: ["response_letter", "revision_checklist"]
owner: "07_response/base/revise/MODULE.md"
---

# trigger is documentation only; not independently discoverable.

# Reviewer response (point-by-point)

Draft a submittable point-by-point letter. Self-audit is `self-review`. Other-paper
review is `peer-review`. Personal letter voice stays in **A personal**.

## When to open

| File | Open when |
|---|---|
| [mode-3-response.md](references/mode-3-response.md) | Letter skeleton and workflow |
| [rebuttal-protocol.md](references/rebuttal-protocol.md) | Full protocol: atomize, three hard gates, analysis triad, journal default, checklist + claim-audit handoff |
| [action-mapping.md](references/action-mapping.md) | Map each comment to a manuscript action |
| [response-audit-gate.md](references/response-audit-gate.md) | Provenance / commitment / coverage gates + locatable ledger |
| [response.md](references/response.md) | Common imaging-AI comment routes |
| [external-principles.md](references/external-principles.md) | Cross-pack principles (non-mount): reviewer isolation + anti-bloat |

## Hard rules

- One comment → one response. Do not invent unrun experiments.
- Sentence rewrites → `write-paper` / `humanize`.
- Tone-only softening of an existing letter → `tighten-response` mode `tone-polish`. This pack keeps point-by-point structure.
- After letter changes numbers → `06_review/base/self-review/references/paper-claim-audit.md`.
- **Negation / incompleteness (owner 2026-10-23):** Process 否定句 that flag work not done or CYA hedges (e.g. 「某某未做」「我们未做」「未进行…»; *we did not* / *not performed* / *was not done* / *not examined*) **must not appear in 正文** (manuscript, revised manuscript, or response letter). Put them **only** in Word 批注 (author **A**), and every such 批注 **must** include **建议修改后内容**. Bare flags fail. Does **not** ban empirical negative findings that are study results (e.g. *no significant difference*, *X was not associated with Y*). Canonical: `05_manuscript/qc/anti-leak-placeholders.md` AL-5; `07_response/qc/disclaimer-comment-only.md`.
