# Ownership contract

Single source for lab roles, manuscript Track Changes, and citation-verify. Other files point here. They do not paste this text.

**Boundary:** After the 2026-10-18 consolidation, this file plus domain `qc/` own standing manuscript/review policy. Standing bans live in `05_manuscript/qc/manuscript-local-qc.md`; review-side consistency in `06_review/qc/cross-manuscript-qc.md`. Rules `My rule.md` keeps only the minimal invariants and a pointer. Do not paste Rules text here.

## Roles

| Role | Seat | Owns |
|---|---|---|
| Aitor | `00_orchestrator` | QC, intent classify, skill chain, gates, local recovery |
| Loopnow | `02_data-processing` | data processing, stats, figures |
| Victor | `03_research` | literature & evidence / study design & exploration / journal selection, Voice B grant, citation-verify / **lit-bank** (NLM ledger) |
| Aitee | `05_manuscript` + `07_response` | manuscript prose, Evidence QC, all manuscript Track Changes (05); response letter final authority (07) |
| Lee | `06_review` | re-review marks/comments; default is not to self-revise manuscript |
| Bai | portal submit after review loop + ethics forms + **0doc library query** | portal submit / Phase-1 checkbox HTML; ethics application **forms** via `03_research/base/fill-protocol/`; **lookup/search/inventory in `{doc_root}`** (Aitor routes/monitors); not the 00 loop. Aitee owns 07 response letter |
| Cursor | external pack | coding / tidying / extraction / form-fill / in-repo frontend-backend (UI, API, tests, PR) and former Cline data/script peers; bot handoff only via 「交给cursor」 (Cursor IDE; Cline may run as IDE plugin for the owner, bots do not call Cline) |

Per-paper channel seats all six (max).

## Dispatch

- One task → one executor (this line is authoritative). Short tasks Aitor can finish locally: do not hand to Cursor.
- Aitee and Lee generally do not call Cursor. Any seat using Cursor needs prior user approval.
- External-pack watch: `00_orchestrator/references/handoff-monitor.md` (only for that task window).

## Word Track Changes

All manuscript Track Changes are owned by Aitee (05). Lee must not self-revise as default. Lee marks/comments; Aitee applies Track Changes.

Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default.

Undecidable / missing-fact issues: state the reason in a Chinese comment, then an English suggestion line that starts with `Suggested …` (or equivalent Suggested wording), and/or suggested literature. Invent or disclaimer language stays in the comment. Never put it in the manuscript body.

Word comments / Track Changes author field is **A** (never `Grok`, never yellow).

**Verify, do not assume.** Before a `.docx` is delivered, run the tracked-changes gate:
`python {SKILLS}\06_review\base\track-changes\scripts\office\validate.py <edited.docx> --original <pre-edit.docx> --author A`.
Exit `0` = every text difference is wrapped in a revision by `A`; exit `1` = a silent overwrite
happened and that span must be redone as a revision. Mechanics → `06_review/base/track-changes/`.

## Citation verify

Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.

Semantic labels: **G-CIT-1** is draft evidence verification before Gate · 05. **G-CIT-2** is post-revision / inside 06. G-CIT-1 does not waive G-CIT-2. These names are labels, not new gate ids.

05 and 06 call/require 03 citation-verify — do not self-certify lit.

Checklist: `03_research/advanced/citation-verify.md`.

## 0doc database lookup

**Owner:** Bai. **Router:** Aitor (does not self-search for general lookup/search/inventory asks).

When the owner asks to search, look up, locate, or inventory materials in the lab document database `{doc_root}` (live tops `_library`, `_bank`, `_code`, `templates`, `mem`, `test`, `skill-harvest`; ethics under `{doc_ethics}`; tree map in `03_research/advanced/0doc-db.md`), Aitor hands the ask to **Bai**.

Bai returns: exact paths, short Chinese summary, and approval numbers / filenames when ethics-related. Treat `{doc_ethics}` as PHI-capable: summarize in chat, do not paste identifiers into public channels or GitHub.

**Does not replace:** Victor (web/literature search); Aitee (manuscript Track Changes); Lee (re-review marks); Loopnow (stats/figures); Cursor when the owner says 「交给cursor」 for bulk scripts. Live project folders under `{lab_root}\` outside `0doc` stay with the seat that owns that workstream.

Procedure: `03_research/advanced/0doc-db.md`.
