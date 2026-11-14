---
name: "simulate-reviewers"
domain: "06_review"
trigger: ["simulate-reviewers", "多审稿人", "blind review", "nature-reviewer"]
outputs: ["skill_output"]
owner: "06_review/base/simulate-reviewers/MODULE.md"
---

# Nature Reviewer Assessment Skill

Thin contract for multi-reviewer blind simulation: stance, isolation rules, bans, and pointers. The generic review envelope is `06_review/base/peer-review/references/review-envelope.md`; opener voice and comment habits are `06_review/advanced/review.md`; the scores are `06_review/qc/`. Sibling of `peer-review`; isolation principles also in `06_review/base/peer-review/references/external-principles.md`.

Absorbed from Nature `skills/nature-reviewer/` on 2026-10-17 (Apache-2.0). Source: [https://github.com/Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills)

## Mission

Simulate a `Nature`-style referee package from the reviewer side: 3 mutually blind reviewer reports plus 1 synthesis, each grounded only in the supplied packet and verifiable evidence. It is not author rebuttal drafting (route to `07_response`) and not an editorial decision letter.

## Scope / Out of scope

In: reviewer-style assessment of a full draft, abstract/summary text, section excerpts, figure legends/notes, or author positioning notes; bounded review with an explicit assessment boundary when material is partial. Out: rebuttal writing, editorial decisions, journal-fit certainty, and any shared concern ledger before reports are frozen.

## Input

Minimum: the manuscript material + the journal criteria + the requested reviewer count (default 3 + synthesis). If the packet is partial, state what is missing and what became unassessable; never pad with invented context.

## Workflow (decision nodes)

1. **Scope**: confirm this is reviewer-style assessment, not rebuttal; record the assessment boundary.
2. **Build one immutable packet**: supplied manuscript, verified source anchors, boundary, common journal criteria. No analytical conclusions, no suspected concerns.
3. **Define emphasis briefs** and the reviewer count before launching anyone; briefs are working lenses, not identities or specialties.
4. **Run each reviewer in an isolated context** (subagent/process/invocation). Pass only the packet, that reviewer's brief, the common skeleton and grounding rules. If isolation is impossible, state that mutual blindness cannot be guaranteed.
5. **Freeze** each report; never show a partial or complete report to another reviewer; never redistribute concerns to control overlap.
6. **Forensic audit** (separate pass, after freezing) via `references/forensic-consistency-audit.md`; findings do not flow back into reviewer contexts.
7. **Synthesize** in a separate pass: reconcile concerns to shared keys, label consensus only when at least two frozen reports independently raise the same underlying concern; keep consensus and audit findings separate.
8. **QA** isolation, severity/blocking calibration, evidence anchoring, groundedness, coverage, role boundaries, non-invention.

## Constraints (never)

- Never invent reviewer identities, specialty roles, or selection history.
- Never let one reviewer read, cite, anticipate, or respond to another review.
- Never build or distribute a shared concern ledger before reports are frozen.
- Never rewrite independent reports after comparison to reduce duplication or manufacture disagreement.
- Never call reports mutually blind when they were generated in a shared context without an explicit limitation notice.
- Never invent experiments, validations, controls, citations, figure details, line numbers, or prior-work distinctions absent from the input.
- Never silently turn assessment into rebuttal drafting, or present the output as an editorial decision letter.
- Never state journal fit (`Nature`) as settled fact.
- Never omit technical failings the supplied evidence cannot establish, and never create concerns to fill a quota.
- Never downgrade a core evidence/validity/ethics/integrity problem to Minor, or upgrade a local presentation issue to sound severe.
- Never label a numerical anomaly a confirmed error without arithmetic proof or source data; never hide a confirmed internal contradiction no reviewer raised.
- Punctuation: avoid em dashes, and avoid colons/semicolons as routine clause connectors (en dash allowed in numeric ranges such as `95% CI: X–X`; Unicode minus U+2212 allowed for signed numbers; ASCII hyphen fine); rule home `05_manuscript/base/vocab/L1/ban-phrases.md`, t1683u / t1761u. Preserve punctuation in titles, quotations, formulas, identifiers, URLs, times, and required machine-readable syntax.

## Output and handoff

Return, unless another format is requested: review setup (scope, boundary, shared claim summary, visible evidence, missing materials), then per reviewer — overall assessment, interested readership, strengths, Major Concerns with ID/severity/blocking/axis/claim pointer/evidence pointer/resolution test, Minor Comments, technical failings, criteria assessment, recommendation posture — then a cross-review synthesis (consensus, differences in emphasis, forensic findings, minor-revision checklist) and a risk/unsupported section. Section anatomy: `references/report-structure.md`.

Handoff: to `06_review` base/`peer-review` for single-reviewer work; to `07_response` when the author wants a reply; to `00` at G-06.

## Calibration and sources

- Real rounds keep one file per reviewer and the editor as a separate seat; keep that separation. Preserve legitimate disagreement on form items; never average or reassign to look consistent.
- Isolation input is the blinded manuscript plus the review form only; exclude prior rounds, other reports and the response.
- Compare concern types and coverage (recall), never wording.

Source order: `references/editorial criteria and processes.md` → user-supplied manuscript facts → `references/06-source-basis.md` → `references/domain-specific-review-gates.md`. Beyond this local source, state the limit instead of improvising journal policy.

## Related files

| File | Open when |
|---|---|
| [references/06-source-basis.md](references/06-source-basis.md) | provenance and source-vs-implementation boundaries |
| [references/reviewer-workflow.md](references/reviewer-workflow.md) | invocation order, fact-base extraction, synthesis rules |
| [references/review-axes.md](references/review-axes.md) | evaluation axes and weighting |
| [references/technical-concern-taxonomy.md](references/technical-concern-taxonomy.md) | 12-axis coverage, concern ledger, pointer rules |
| [references/domain-specific-review-gates.md](references/domain-specific-review-gates.md) | chemistry/engineering/materials/atmospheric/climate-ecology/hydrology/remote-sensing chains |
| [references/report-structure.md](references/report-structure.md) | default output contract |
| [references/role-boundaries.md](references/role-boundaries.md) | reviewer differences and editor-versus-reviewer boundary |
| [references/06-qa-checklist.md](references/06-qa-checklist.md) | groundedness and non-invention checks |
| [references/forensic-consistency-audit.md](references/forensic-consistency-audit.md) | mandatory post-review arithmetic/provenance audit |
| [references/editorial criteria and processes.md](<references/editorial criteria and processes.md>) | primary local Nature source text |
