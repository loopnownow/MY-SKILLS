# Ownership contract

Single source for lab roles, manuscript Track Changes, and citation-verify. Other files point here. They do not paste this text.

**Boundary:** Rules `{RULES}\manuscript-and-review.md` owns standing manuscript/review policy (body vs comment, TC author field, deliverable prefs). This file owns seat/role ownership and the skills-layer TC / citation-verify operational contract. Point to Rules for standing bans; do not paste or fork them here.

Ownership: see `00_orchestrator/references/ownership-contract.md` (this file).

## Roles

| Role | Seat | Owns |
|---|---|---|
| Aitor | `00_orchestrator` | QC, intent classify, skill chain, gates, local recovery |
| Loopnow | `02_data-processing` + `04_analysis` | data processing, stats, figures |
| Victor | `03_research` | 文献与证据 / 研究设计与探索 / 选刊, Voice B grant, citation-verify |
| Aitee | `05_manuscript` + `07_response` | manuscript prose, Evidence QC, all manuscript Track Changes (05); response letter final authority (07) |
| Lee | `06_review` | re-review marks/comments; default is not to self-revise manuscript |
| Bai | 投稿 after review loop (06 re-review and/or 07 response as needed; not “after 06” as sole gate) + ethics forms | portal submit / Phase-1 checkbox HTML; ethics application **forms** via `MY-SKILLS-base/03-research/fill-protocol/` (Aitor routes/monitors); not the 00 loop. Aitee owns 07 response letter |

Per-paper channel seats all six (max).

## Word Track Changes

All manuscript Track Changes are owned by Aitee (05). Lee must not self-revise as default. Lee marks/comments; Aitee applies Track Changes.

Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default.

Undecidable / missing-fact issues: Chinese 批注 reason, then an English suggestion line that starts with `Suggested …` (or equivalent Suggested wording), and/or suggested literature. Invent or disclaimer language stays in the comment. Never put it in the manuscript body.

Word comments / Track Changes author field is **A** (never `Grok`, never yellow).

## Citation verify

Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.

Semantic labels: **G-CIT-1** is draft evidence verification before Gate · 05. **G-CIT-2** is post-revision / inside 06. G-CIT-1 does not waive G-CIT-2. These names are labels, not new gate ids.

05 and 06 call/require 03 citation-verify — do not self-certify lit.

Checklist: `03_research/personal/citation-verify.md`.
