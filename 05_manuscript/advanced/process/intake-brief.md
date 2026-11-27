# Intake Brief (writing-entry summary, not a form)

**Owner:** `05_manuscript` advanced, on the existing writing route (`05_manuscript/advanced/route.md`).
**Not a QC gate**, and not a new form, scorecard, fine id, skill, or second router.

## Purpose

Before `write-paper` starts a draft, gather in one short note the research question, the study type, the main claims, the data and analyses already in hand, and any figure or table constraints. The brief is writing context so the draft can open from what is already known. It does not approve a design, and it does not replace study-type, Claim Map, the figure-table plan, or method-experiment alignment.

## When to load

Load first, on the same 05 route, before `draft-section` / `full-imrad`. Then load `05_manuscript/advanced/process/study-type.md` and `05_manuscript/advanced/process/claim-map.md`. Refresh the brief only if a locked aim, a supplied result file, or a user-locked decision changes.

## Fields (keep light)

One compact block. Prefer reading existing files (locked protocol, supplied tables, `*-results.html`, a named 02 handoff, or an already built Claim Map) over asking the user to re-enter the same facts. Leave a cell blank or mark it `missing` when the fact is not in hand. Do not turn this into a long questionnaire.

```text
Intake Brief
------------
Question / aim: ...
Study type (from study-type.md): ...
Main claims (Claim Map labels only): ...
Data / analyses in hand: ...
Figure / table constraints: ...
Locked decisions: ...
Missing / unverified: ...
```

| Field | What to record |
|---|---|
| Question / aim | The locked research question or primary aim, in the user's words |
| Study type | The coarse class already named in `05_manuscript/advanced/process/study-type.md`; do not restate that route's constraints here |
| Main claims | Working labels from the Claim Map (C1, C2, …), not a second claim list |
| Data / analyses in hand | Named tables, result files, or 02 handoffs that actually exist |
| Figure / table constraints | Display needs already planned in `05_manuscript/advanced/process/figure-table-plan.md`, or a brief note if that plan is still empty |
| Locked decisions | Design or statistical choices the user has already locked |
| Missing / unverified | Facts not in hand; mark them `missing` and stop there |

Optional cells (population or n, a named target venue, already confirmed limitations) may be added only when the source already states them. Do not hunt them down to complete a form.

## How to fill gaps

- If a missing item is not needed to start the current section, continue and keep the `missing` mark.
- If a missing item would change the scientific interpretation, raise one most important clarification as a Word comment (author **A**). Do not stack a questionnaire.
- Do not fill a gap by guessing, by "usual practice," or by inventing a result, a sample size, or an unperformed analysis.

## Hard constraints

1. Do not change a user-locked design or statistical plan to make the brief look complete.
2. Do not invent an analysis or a result that was not performed.
3. Do not write an unperformed step into the brief, Methods, or Results for writing convenience.
4. A `missing` cell stays missing until a real source arrives. Guessing is not an allowed fill.

## Call graph

| Direction | File | Role |
|---|---|---|
| Entry | `05_manuscript/base/write-paper/MODULE.md` (and the thin `SKILL.md`) | Load this summary before drafting |
| Downstream | `05_manuscript/advanced/process/study-type.md` | Coarse study type; do not copy those wording rules here |
| Downstream | `05_manuscript/advanced/process/claim-map.md` | Claim-evidence plan; do not copy that map here |
| Downstream | `05_manuscript/advanced/process/figure-table-plan.md` | Which claims need a display; do not copy that plan here |
| Later | `05_manuscript/advanced/process/method-experiment-align.md` | Two-way aim-methods-results trace after drafting starts |

## Out of scope

- New forms, scorecards, fine ids, gates, or a parallel writing flow
- Imported word-count or sentence-count cutoffs, absolute wording bans, or paper-sentence templates
- Copying study-type, Claim Map, figure-table-plan, or alignment rule bodies
- Changing 00 gate composition or editing 02 production rules

*Thin lab rewrite, 2026-11-27, on a writing-entry intake summary (what is already known before drafting, not a new form or gate). Method reference: [gulucaptain/Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill). See `NOTICE`.*
