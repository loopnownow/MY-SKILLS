---
name: "lit-fulltext"
domain: "03_research"
trigger: ["lit-fulltext", "全文", "fulltext", "PDF download", "open access PDF"]
outputs: ["fulltext_files", "retrieval_report", "manual_needed"]
owner: "03_research/base/lit-fulltext/MODULE.md"
---

Batch open-access full-text retrieval for a DOI/PMID worklist from `lit-search` / `verify-refs`.
True-absorbed from Aperivue `medsci-skills/skills/fulltext-retrieval` on 2026-10-30.
Seat: `03_research`. Path: `03_research/base/lit-fulltext/`.

> **Source**: [https://github.com/Aperivue/medsci-skills/tree/main/skills/fulltext-retrieval](https://github.com/Aperivue/medsci-skills/tree/main/skills/fulltext-retrieval)

# lit-fulltext

Contract only for lit-fulltext (full-text retrieval): scope, bans, phase names, and pointers. The recipe and the revision authority live in `03_research/advanced/`; this file does not restate a procedure. Pack data (`rules/`, `data/`, `references/`) stays beside it as data.

## Project-start chain

Fixed order (do not skip when this id is on the chain):

1. `design-study` (light: keywords; materials prefer `ref/refer/`, else ask owner)
2. `lit-search`
3. `verify-refs`
4. `lit-fulltext` (gate first, then fetch gaps)
5. Return to `design-study` when full text forces a design change

## Step 0 — gate (every run)

Before any download, inspect `ref/refer/` for non-duplicate fulltext files (`.pdf` | `.html` | `.md`).
Deduplicate by DOI, PMID, and file hash (sha256).

**Skip download and only ledger/account** when **all** hold:

- distinct fulltext file count >= 5
- set covers highly relevant papers from the last 5 years
- set includes the latest diagnostic criteria
- set includes the latest international guideline

Otherwise fill **gaps only** (do not blindly download a ~30-item abstract/NLM cite list).

## Inputs

- Prefer the DOI|PMID table produced by `lit-search` / `verify-refs` (TSV/CSV/Markdown with a `DOI` column; `PMID` / `Title` / `FirstAuthor` when available).
- Do not invent a second worklist.

## Outputs (always under `ref/refer/`)

- OA PDFs landed in `ref/refer/`
- `ref/refer/retrieval_report.json` — per-DOI report including `source_identity` and `file_sha256`
- `ref/refer/manual_needed.txt` — paywalled / not-OA items (one line per item with DOI and/or PMID and Title when known)

## Scripts

| Script | Role |
|---|---|
| `scripts/fetch.py` | **Required.** OA resolvers only (Unpaywall / PMC / EuropePMC / OpenAlex / Crossref / arXiv; optional DOAJ / medRxiv / bioRxiv). Paywalled -> `manual_needed.txt`. |

Contact email for Unpaywall ToS: read from **Vault** (owner contact / corresponding). Never hard-code an address in this pack.

This fine id does **not** convert PDF to Markdown; use a separate skill when needed.

```bash
python scripts/fetch.py worklist.tsv --output ref/refer/ --email "$(vault-contact-email)"
```

## Hard rules

- OA only. Never bypass a paywall or publisher access control.
- Do not attach Zotero "Find Available PDF" or lit-sync flows in this pack.
- Do not blind-download the full ~30 abstract/NLM cite list; gate first, then gap-fill.
- No PDF→md in this pack.
- **No Sci-Hub** and no other shadow / pirate full-text sites. Do not script, link, or automate them.
- Library account credentials stay in **Vault only**. Never write username/password into this pack, `fetch.py`, env examples, or chat-bound skill text.

## Paywalled after OA fail (owner handoff)

When `fetch.py` cannot land OA:

1. Keep the item in `ref/refer/manual_needed.txt` (DOI|PMID|Title).
2. Stop automated download for that item.
3. Owner fetches manually via the institutional library portal or its OpenURL resolver:
   - Portal home: `https://fdjslib.yuntsg.com/official/neindex.html`
   - SSO login (browser): `https://user.tsgyun.com/user/login?insid=1235` — use Vault login; slider captcha is human-only.
4. Optional ILL / document delivery through the same library channels if OpenURL fails.
5. Bots may open the portal for the owner and remind Vault, but must not automate Sci-Hub or embed library secrets in skills.

## Handoffs

- Need citations / NLM + abstracts only -> `verify-refs`
- Need search expansion -> `lit-search`
- Design change after reading full text -> `design-study`
- Paywalled after OA fail -> owner library portal / OpenURL (Vault) / ILL; **not** Sci-Hub
