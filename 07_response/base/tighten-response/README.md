# `nature-response` skill

[English](references/README_EN.md)

`nature-response` drafts, reviews, and revises revision-communication materials: mutually isolated point-by-point reviewer responses, revision cover letters, marked-up revision excerpts, and editable LaTeX templates.

## What it is for

- Parse editorial decision letters, revision emails, and reviewer reports.
- Confirm Major vs Minor Revision first, then choose the matching revise strategy.
- Split comments into stable IDs such as `E.1`, `R1.1`, `R2.3`.
- Treat reviewers as mutually blind by default. Keep an internal master table; each reviewer's reply is a separate document and must not leak other reviewers' opinions, IDs, suggestions, or replies.
- When several reviewers raise the same issue, answer each fully and separately. Coordinate conflicts only internally or in the editor-facing master table — never mention another reviewer's ask to a given reviewer.
- For each comment, set response strategy, manuscript change action, and evidence needs.
- Record separately “which response action was chosen,” “how far the task has progressed,” and “whether the whole reply package is submittable,” and require verifiable artifacts for done status.
- Draft formal, restrained, submittable English point-by-point replies and cover letters.
- Audit rebuttal drafts for missed replies, defensive tone, unsupported claims, and line-number gaps.
- Soften defensive or harsh phrasing in an existing reply without rebuilding the letter (mode `tone-polish`).
- When a reviewer missed content already in the manuscript, treat it as clarity failure — add clarification or move the text — do not reply “already in the manuscript.”
- The letter fully answers reviewers, but manuscript edits keep only what readers need for the central claim; every new main-text sentence is checked for replace / compress / move-to-SI to prevent reviewer-driven accretion.
- For LaTeX revise packs, auto-check letter citations, comment/reply counts, and clean vs marked-up body consistency.

## Typical requests

- “Here are the editor email and reviews — generate a point-by-point reply framework.”
- “Turn my Chinese revision notes into an English reviewer response.”
- “Audit this rebuttal for missing points and defensive tone.”
- “Soften the tone of this reply. Do not change the structure or the scientific position.”
- “Draft the cover letter and isolated R1/R2 replies.”

## What you need to provide

- Decision letter / editor email, reviewer reports, and (when available) the current manuscript or marked revision.
- Known constraints: experiments already run, data unavailable, word limits, venue rules.
- Target: Major or Minor; whether LaTeX templates / marked excerpts are needed.

## Outputs

- Point-by-point English responses (one document per reviewer when isolation applies).
- Optional editor-facing master / cover letter.
- Action and evidence checklist; submittability status.
- Optional LaTeX revise-pack checks.

## What it is not

- Not a substitute for `06_review` pre-submission / peer review.
- Not a place to invent experiments, AUCs, or analyses the study does not contain.
- Not a channel to leak reviewer A’s asks into reviewer B’s letter.
- Not the point-by-point structure owner. That stays `revise`.
- Not a scientific-accuracy check. `tone-polish` preserves the stated position and can over-soften; the author still verifies the stance.
