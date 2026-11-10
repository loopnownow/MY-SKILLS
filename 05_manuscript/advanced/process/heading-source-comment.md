# Heading source comments

When this round newly creates or changes citations, record the sources in one Word comment on each affected IMRAD major heading. Do not put paths into the manuscript body.

## Trigger

Add heading comments only when this round newly created or changed citations. That includes:

- Literature citations: in-text `[n]`, bibliography entries, or items taken from paths actually used, such as `ref/refer/`, `references`, or an Evidence Pack.
- Numbers or tables actually taken from paths such as `result.html`, `ref/tables/`, or pipeline outputs.

Pure wording edits that do not touch literature or numbers get no heading comment.

Do not recrawl already-recorded sections just to backfill comments on an old manuscript.

## Placement

- Comment only IMRAD major headings: Introduction, Methods, Results, Discussion.
- If the Abstract has citations this round, also comment the Abstract heading.
- If the reference list was reordered this round, comment the References heading.
- Do not comment 2.1-style subheadings.
- Do not put one comment on every `[n]`.
- One comment per major heading that has new or changed sources this round.
- If a section has no new or changed citations this round, skip it.

## Comment content

- Author field: **A**.
- Tag: `[cite-src]` at the comment lead-in.
- Write only the paths actually used plus the items (newly used `[12][13]`, table numbers, or Evidence Pack).
- Do not invent paths.
- Do not put those paths into the manuscript body.
- Do not paste full text, abstracts, or personal information.
- Remove these comments before the submission package is assembled.

Example shape (items must be real for that round):

```text
[cite-src] Results: result.html (AUC, 95% CI); ref/tables/Table2 (Table 2).
```

## Two source classes

1. Literature: `ref/refer/`, `references`, Evidence Pack.
2. Numbers and tables: `result.html`, `ref/tables/`, pipeline outputs.

Methods, by existing rules (`citation-and-language.md`), does not cite literature. A Methods heading comment is only for numbers or method-source paths.

## Roles

- **Writing:** Aitee (05) puts comments on the manuscript headings.
- **Review:** If the review report itself newly cites literature, put the comment on the review-report major heading. Do not mix it with review comments aimed at the original manuscript. Lee does not edit the manuscript body.
- **Response:** If the response letter newly cites literature, comment the response-letter major heading. New citations added into the manuscript itself are still placed by Aitee on the manuscript headings.
- **HTML manuscripts:** use HTML comments or author notes, not text visible in the submission body.

## QC

If this round changed citations and the matching heading comments are missing, QC emits WARN only. Do not FAIL the gate for this. Do not check or require backfill on old manuscripts. See `05_manuscript/qc/citation-audit-gate.md`.
