# DOCX comment and placeholder repair

Open when filling `[PLACEHOLDER: …]` slots in a Word manuscript, batch-inserting or
cleaning review comments, or verifying that claimed changes really are tracked edits.
Mechanics only: letter wording stays `mode-3-response.md` / `rebuttal-protocol.md`,
journal proof queries stay `proof-mode.md`.

## Comment object model

A `comments` part holds one record per comment: id, author, anchor (`rangeStart` /
`rangeEnd`), and text. Lab and editor rounds use different author names — read the
author field before deciding which round a comment belongs to.

Insert and clean in dry-run first: print each planned action as `id + paragraph head +
comment text`, apply only after the mapping reads correctly, and finish with the saved
path.

## Read-back contract (before claiming done)

| Check | Expectation |
|---|---|
| comments part | `has_comments_part` true |
| anchors | one `rangeStart` / `rangeEnd` pair per comment, count matches |
| relationships | comment reference targets resolve (`rel_ok`), content type correct |
| reopen | the document still opens through python-docx; paragraph and table counts match the pre-edit file |

Report the comment count, anchor count, and paragraph/table counts in the delivery note.

## Placeholder fill

- Replace `[PLACEHOLDER: …]` at run level; print one `OK P<n> 'old' -> 'new'` line per hit
  and the saved path at the end.
- The same slot can appear more than once (an ethics block duplicated at two paragraph
  indices): replace every occurrence, then grep the saved file for `[PLACEHOLDER` to prove
  none remains.
- Adjacent runs can concatenate into one string, so a replacement may appear glued to its
  neighbour (`…Hospital2025-02-262025K014`). Verify against the accepted full text, never
  per-run fragments.
- Type an approval date or number only after reading it from the approval letter; if the
  letter is missing, leave the slot and raise a comment (author **A**) with the question.

## Insert / clean / repair lifecycle

| Step | Action | Evidence to report |
|---|---|---|
| insert | dry-run the mapping, then apply | `comments added=N`, saved path |
| clean resolved | remove comment-reference marks **and** definitions in one pass | `marks removed=N`, `defs removed=[…]`, `remaining ids=[…]` |
| repair | diff `referenced` / `have` / `missing` ids, re-insert only missing definitions | before/after id lists |

Deleting a definition without its reference (or the reverse) leaves an orphan and breaks
the file in Word; always handle the pair.

## Tracked-change check

- Count `w:ins` / `w:del` and paragraph/table totals; compare with the previous version.
- Confirm every claimed change is locatable as a tracked edit or a replaced figure — the
  same test as the proof-mode "claimed equals done" gate.
- When the letter quotes revised text, italics are part of the response-letter format
  (`07_response/base/tighten-response/references/response-structure.md`), not of the
  manuscript edit.

## Moving revision artifacts

- Plan first: the cleanup mover takes a scan TSV, defaults to dry-run, and writes to a
  dated destination only with an explicit apply flag.
- Byte-identical copies are reported for human confirmation and are never moved
  automatically.
- Keep the version scheme (`Manuscript_<slug>_V<n>`, `Response_<slug>_V<n>`); retired
  versions stay in the project's `ref/tmp`, not in a new tree.

## Hard rules

- Never invent an approval date, number, funder ID, or software version to clear a slot.
- Never delete an unresolved reviewer or editor comment.
- Comment text and comment dumps may carry manuscript data or reviewer identities; they
  do not enter skill bodies, shared notes, or evidence files.
