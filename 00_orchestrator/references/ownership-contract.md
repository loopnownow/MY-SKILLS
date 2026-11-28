# Ownership contract

Single source for lab roles, manuscript Track Changes, and citation-verify. Other files point here. They do not paste this text.

**Boundary:** After the 2026-10-18 consolidation, this file plus domain `qc/` own standing manuscript/review policy. Standing bans live in `05_manuscript/qc/manuscript-local-qc.md`; review-side consistency in `06_review/qc/cross-manuscript-qc.md`. Rules `My rule.md` keeps only the minimal invariants and a pointer. Do not paste Rules text here.

## Roles

| Role | Seat | Owns |
|---|---|---|
| Aitor | `00_orchestrator` | QC, intent classify, skill chain, gates, local recovery |
| Loopnow | `02_data-processing` | data processing, stats, figures, **coding / scripts / `MY-CODES`** (the default coding seat) |
| Victor | `03_research` | literature & evidence / study design & exploration / journal selection, Voice B grant, citation-verify / **lit-bank** (NLM ledger) |
| Aitee | `05_manuscript` + `07_response` | manuscript prose, Evidence QC, all manuscript Track Changes (05); response letter final authority (07) |
| Lee | `06_review` | re-review marks/comments; default is not to self-revise manuscript |
| Bai | portal submit after review loop + ethics forms + **_Docs library query** | portal submit / Phase-1 checkbox HTML; ethics application **forms** via `03_research/base/fill-protocol/`; **lookup/search/inventory in `{doc_root}`** (Aitor routes/monitors); not the 00 loop. Aitee owns 07 response letter |
| local DeepSeek (DSH) / Cline | external pack | tidying / extraction / form-fill / in-repo frontend-backend (UI, API, tests, PR) peer work, when the owner says 「交给 DS / DeepSeek / Cline」 or approves their use (desktop app or Cline CLI). Bots may call local DSH and Cline. Cursor IDE is uninstalled; do not route tasks to Cursor IDE, and do not use 「交给cursor」 as a routing trigger. **Not the default coding seat.** Coding / scripts / `MY-CODES` are Loopnow on 02 |

Every role above, plus CloudAgent, carries and obeys `{RULES}`; `{RULES}\My rule.md` is authoritative. This contract governs who may revise what and does not restate Rules text. Skills attach on concrete work only.

Specialist roster is `specialist_hint` on each `coarse_ids` row in [`../registry.yaml`](../registry.yaml). The only executor exception is `fill-protocol` → Bai (body stays under 03). Do not maintain a separate bot-name table.

Per-paper channel seats all six (max).

## Dispatch

- One task → one executor (this line is authoritative). Short tasks Aitor can finish locally: do not hand to local DSH / Cline.
- Before starting a project or task, estimate wall-clock runtime in good faith (do not inflate or deflate the estimate to force or avoid sub-agents). If the estimate exceeds 1 hour, Aitor (00, 总调度) opens sub-agents to accelerate: dispatch parallelizable parts so wall clock shortens. "Sub-agent" means a specialist bot / child agent dispatched by 00 under the current seats (Loopnow / Victor / Aitee / Lee / Bai and on-seat executor sub-agents). Do not create ad-hoc accounts or bypass seats. Each dispatched part still follows one task → one executor. Write-disk authorization and three-repo merge (「合」 / 「推合」) stay in `{RULES}\My rule.md`; this paragraph does not relax those gates. Rule SSOT: `{RULES}\My rule.md` §7.
- Coding / scripts / `MY-CODES` default to **Loopnow** (02). Local DSH / Cline are not the default coding seat; they take tidying / extraction / form-fill / local IDE work when the owner says 「交给 DS / DeepSeek / Cline」 or approves their use.
- Aitee and Lee generally do not call local DSH / Cline. Any seat using local DSH or Cline needs prior user approval. Bots may call local DSH and Cline.
- External-pack watch: `00_orchestrator/references/handoff-monitor.md` (only for that task window).

## Word Track Changes

All manuscript Track Changes are owned by Aitee (05). Lee must not self-revise as default. Lee marks/comments; Aitee applies Track Changes.

05 applies Word Track Changes on the manuscript. 06 only mechanically unpacks, validates, and packs a `.docx` (`06_review/base/track-changes/`). 07 writes response letters; letters never route to 06.

Decidable issues: Lee annotates for Aitee to TC-fix and does not apply the body revisions as default.

Undecidable / missing-fact issues: state the reason in a Chinese comment, then an English suggestion line that starts with `Suggested …` (or equivalent Suggested wording), and/or suggested literature. Invent or disclaimer language stays in the comment. Never put it in the manuscript body.

Helper Word comments / Track Changes use author field **A** (never `Grok`, never yellow). The owner's own author mark is **Adm**; revisions and comments under **Adm** are first-class harvest sources (marks only). Do not treat helper author **A** as the owner's identity.

**Verify, do not assume.** Before a `.docx` is delivered, run the tracked-changes gate:
`python {code_stats}\tools\office\validate.py <edited.docx> --original <pre-edit.docx> --author A`.
Exit `0` = every text difference is wrapped in a revision by `A`; exit `1` = a silent overwrite
happened and that span must be redone as a revision. Mechanics → `06_review/base/track-changes/`.

## Citation verify

Victor owns citation-verify (Lit05/Lit06) and supplies suggested literature for comments when needed.

The literature gate is **G-LIT** only: required before G-05 is done and again inside 06. A 05 pass does not waive the 06 pass. Do not invent G-LIT labels.

05 and 06 call/require 03 citation-verify — do not self-certify lit.

Checklist: `03_research/advanced/verify-refs.md`.

## _Docs database lookup

**Owner:** Bai. **Router:** Aitor (does not self-search for general lookup/search/inventory asks).

When the owner asks to search, look up, locate, or inventory materials in the lab document database `{doc_root}` (live tops `_library`（含 `glossary`）, `templates`, `mem`, `test`, `harvest`; ethics under `{doc_ethics}`; tree map in `03_research/advanced/docs-db.md`), Aitor hands the ask to **Bai**.

Bai returns: exact paths, short Chinese summary, and approval numbers / filenames when ethics-related. Treat `{doc_ethics}` as PHI-capable: summarize in chat, do not paste identifiers into public channels or GitHub.

**Does not replace:** Victor (web/literature search); Aitee (manuscript Track Changes); Lee (re-review marks); Loopnow (stats/figures/scripts/coding). Local DSH / Cline take work when the owner says 「交给 DS / DeepSeek / Cline」 or approves their use (tidying / extraction / form-fill / IDE work), never as the script or coding default. Live project folders under `{lab_root}\` outside `_Docs` stay with the seat that owns that workstream.

Procedure: `03_research/advanced/docs-db.md`.
