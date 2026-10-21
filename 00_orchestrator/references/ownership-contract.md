# Ownership contract

Single source for lab roles, manuscript Track Changes, and citation-verify. Other files point here. They do not paste this text.

**Boundary:** After the 2026-10-18 consolidation, this file plus domain `qc/` own standing manuscript/review policy. Standing bans live in `05_manuscript/qc/manuscript-local-qc.md`; review-side consistency in `06_review/qc/cross-manuscript-qc.md`. Rules `My rule.md` keeps only the minimal invariants and a pointer. Do not paste Rules text here.

Ownership: see `00_orchestrator/references/ownership-contract.md` (this file).

## Roles

| Role | Seat | Owns |
|---|---|---|
| Aitor | `00_orchestrator` | QC, intent classify, skill chain, gates, local recovery |
| Loopnow | `02_data-processing` + `04_analysis` | data processing, stats, figures |
| Victor | `03_research` | 文献与证据 / 研究设计与探索 / 选刊, Voice B grant, citation-verify / **lit-corpus** (NLM ledger) |
| Aitee | `05_manuscript` + `07_response` | manuscript prose, Evidence QC, all manuscript Track Changes (05); response letter final authority (07) |
| Lee | `06_review` | re-review marks/comments; default is not to self-revise manuscript |
| Bai | 投稿 after review loop + ethics forms + **0doc 文档库查询** | portal submit / Phase-1 checkbox HTML; ethics application **forms** via `03_research/base/fill-protocol/`; **lookup/search/inventory in `D:\0Grok\0doc`** (Aitor routes/monitors); not the 00 loop. Aitee owns 07 response letter |
| Cursor | 外挂 | 仓库内前端/后端（UI、API、测试、PR）；仅用户说「交给cursor」才交 |
| Cline | 外挂 | 数据准备及同类（xlsx、归档、批处理、非仓库数据）；用户说「交给cline」或一般数据/脚本交接 |

Per-paper channel seats all six (max).

## Dispatch

- 一个任务只交一个执行方（one executor；本条权威处）。Aitor 能在本地做完的短任务，不交 Cursor，不交 Cline。
- Aitee、Lee 一般不调用 Cursor 或 Cline。任何座位要用 Cursor，必须用户先批准。
- 外挂盯梢：`00_orchestrator/references/handoff-monitor.md`（仅该次任务期间）。

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

## 0doc database lookup

**Owner:** Bai. **Router:** Aitor (does not self-search for general 查/找/盘点 asks).

When the owner asks to search, look up, locate, or inventory materials in the lab document database `D:\0Grok\0doc` (any of `00-inbox` … `07-ethics`, including indexes under `_index` / `02-flattened` / `revision-history`), Aitor hands the ask to **Bai**.

Bai returns: exact paths, short Chinese summary, and approval numbers / filenames when ethics-related. Treat `07-ethics` as PHI-capable: summarize in chat, do not paste identifiers into public channels or GitHub.

**Does not replace:** Victor (web/literature search); Aitee (manuscript Track Changes); Lee (re-review marks); Loopnow (stats/figures); Cline when the owner explicitly says「交给cline」for bulk scripts. Live project folders under `D:\0Grok\` outside `0doc` stay with the seat that owns that workstream.

Procedure: `03_research/personal/0doc-db.md`.
