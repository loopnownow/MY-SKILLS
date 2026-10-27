---
name: "track-changes"
domain: "06_review"
description: Word Track Changes mechanics - unpack, edit, verify every change is tracked by author A, repack. Proves the no-silent-overwrite rule instead of trusting it.
owner: "06_review/base/track-changes/MODULE.md"
---

# track-changes

Capability body: [MODULE.md](MODULE.md). Do not duplicate it here.

Hard gate: `validate.py --original <pre-edit.docx> --author A` must exit `0`. Exit `1` means a
silent overwrite — redo that span as a revision.

Rules this enforces → MY-RULES `My rule.md` §5.1; `06_review/personal/word-edit.md`.
