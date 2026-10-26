# Word edit and delivery (personal)

Ownership: see `00_orchestrator/references/ownership-contract.md`.

## Revisions

- Manuscript body revisions are landed by **Aitee (05)**. Lee (06) defaults to comments only and does not revise the body. Decidable issues become TC-fix comments for Aitee. Undecidable / missing facts: Chinese reason, then one English line starting with `Suggested ...` (or equivalent Suggested wording), and/or suggested literature (Victor supplies literature). Lee does not land manuscript edits; after the user chooses, Aitee applies Track Changes to the body.
- The revision modes below are how **Aitee lands edits**, not Lee's default for rewriting the paper.
- Every change to a `.docx` uses **Track Changes**.

## Revision grain (owner 2026-10-19)

- Edit by **word** or **sentence**; **forbid** wholesale overwrite of whole paragraphs/sections.
- Existing `.docx` always lands text under **Track Changes**; forbid silent plain-text overwrite of a `-copy` shell.
- **User hand-edits win (Word only).** If the current sentence differs from what the agent last wrote, treat it as a user edit. To touch that span again, ask the user first; do not silently revert. This does **not** apply to HTML, PDF, or scripts.
- Unclear spots: **comment (author A)** or ask the user first; no silent direct edits; no unilateral Accept/Reject of revisions.
- **Keep front-matter already in the file:** if corresponding author, funding, ethics (Date/NO), affiliations, etc. are already present, **forbid** overwriting with lab default/template sentences; change only when the user names them. Missing items -> ask via comment; do not fill defaults.

## Files

- **Prefer not creating new files**; revise the existing final the user named.
- **Avoid intermediate files**; if unavoidable, move them into `0del` after the task (local usual `{del_root}`).
- Do not make backup copies unless the user asks.
- After Aitee applies Track Changes, or after Lee comments-only review of Word, append a record to that project's **`ref/manuscript-revision.md`** (date, file, revised / review-only / untouched / open). Later rounds must not re-polish or re-review already recorded spans unless upstream numbers changed, the user named them, or open comments remain.

## Language and layout

- Journal envelope: **English**. Owner-facing summary / internal notes / QC: **Chinese**.
- **Forbid unilateral Word/PDF format changes.** Unless the owner names formatting this turn, revising an existing `.docx`/`.pdf` changes text only (Track Changes / comments). Do not change styles, font, size, alignment, indent, space before/after paragraph, space before/after text, line spacing, text direction, sections, margins, table geometry, or special format. Keep user hand-edited format too.
- **Unified body typography** (manuscript, review shell, response letter): Times New Roman, 12 pt, 1.5 line spacing, space before/after paragraph 0, space before/after text 0, justified, left-to-right, **special format: none**. Structure detail: `05_manuscript/personal/Aitor-format.md`.
- New paragraphs that must carry format (user-named layout, or blank new draft): same unified typography; do not invent another style.

## Handoff

- Condensed review items (**精简**) → Word comments (**批注**) on the manuscript locus (原文); see `review.md` §0.2.
- Localization rules: `review.md` section 0.1.
- Source tags and Chinese reasons: `review.md` section 0.1 (comment lead-in; this file does not copy the rule body).
