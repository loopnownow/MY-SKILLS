# Proof (校样) mode, a branch of `revise`

**Open when:** the journal returns a typeset proof (MDPI / Wiley / Elsevier / Springer) with layout queries in comment balloons and asks for confirmation or correction before printing.
**Output:** answers written in the proof's own comment balloons plus Track Changes in the proof file. **No separate response letter.**

## Boundary against the letter mode

| Item | letter (main `revise` path) | proof (this mode) |
|---|---|---|
| Input | numbered reviewer / editor comments | layout queries, mostly confirms, wording and metadata |
| Output | response letter + revised manuscript | answers in the proof + tracked edits |
| Freedom | new analyses allowed, sections may be rebuilt | **no** layout change, no comment deletion, no authorship or affiliation re-assignment, no EndNote reference re-ordering |
| Window | per revision deadline | usually 48 to 72 h; if a fix cannot be made, explain instead of silence |

## Query taxonomy (classify before editing)

| Type | Recognise by | Default action | Reply skeleton |
|---|---|---|---|
| Confirm-only | "We revised X, please confirm", "please confirm the accuracy of names" | verify first, then answer | `Confirmed.` |
| Wording / format | hyphen to minus, abbreviation singular or plural, date format, bold | change text or table per journal style | `Confirmed. ... has been revised as requested.` |
| Supply metadata | software version, manufacturer city/state/country, URL access date, funder ID, supplementary captions | add at first mention; never invent a version number | `Confirmed. The version number and the manufacturer information ... have been added at first mention.` |
| Figure content | text inside a figure, overlapping elements, subpanel descriptions, symbol form | re-export from the source file; edit the bitmap only when no source exists | `Confirmed. ... has been replaced ... and the corrected figure has been inserted.` |
| Informational | Notes for Authors, "figure positions may change", "do not use EndNote" | no reply needed, or one line `Noted.`; the content still binds | `Noted, no action required.` |

## Three gates (any FAIL blocks the return)

| Gate | Test | Failure seen in practice |
|---|---|---|
| G-P1 every query answered | every journal comment has an author reply, and the reply is **not empty** | an empty reply balloon |
| G-P2 claimed equals done | every "added / revised / replaced" in a reply is locatable as a tracked edit or a replaced figure | reply claims access dates added, URL format still inconsistent |
| G-P3 no self-contradiction | the same fact agrees across replies and between reply and text | reply says no software is mentioned, Methods lists seven packages |

## Metadata checklist (most common supply-metadata items)

- [ ] Software: version plus vendor (city, state abbreviation, country) at first mention
- [ ] Instruments, commercial reagents, cell lines: full manufacturer address; state explicitly if no chemicals were used
- [ ] URLs: `URL (accessed on Day Month Year)`
- [ ] Affiliations: subordinate to superior; split into separate entries only when addresses differ; author superscripts match the affiliation numbers
- [ ] Abbreviations: table body, table footnote and abbreviation list use the same form
- [ ] Symbols: the same glyph in text, tables and figures (hyphen is not a minus, U+2212)
- [ ] Dates, bold necessity, supplementary captions, leftover reference fields (EndNote and similar)

## Operating notes

- Re-extract the comment-id map from every new proof file; ids are renumbered and must not be reused from a previous round.
- Read-only first: deliver a status plus action opinion, edit only after the owner approves.
- Mechanics: Track Changes unpack and repack are `06_review/base/track-changes/`; the `P` filename token is `05_manuscript/advanced/Aitor-format.md`; OOXML or pixel scripts belong to `{code_root}`, not here.
