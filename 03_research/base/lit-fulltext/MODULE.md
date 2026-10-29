---
name: "lit-fulltext"
domain: "03_research"
trigger: ["lit-fulltext", "全文", "fulltext", "PDF download", "open access PDF"]
outputs: ["fulltext_files", "retrieval_report", "manual_needed"]
owner: "03_research/base/lit-fulltext/MODULE.md"
---

Batch open-access full-text retrieval for a DOI/PMID worklist from `lit-search` / `verify-refs`.
True-absorbed from Aperivue `medsci-skills/skills/fulltext-retrieval` on 2026-10-30.
Not mounted. Seat: `03_research`. Path: `03_research/base/lit-fulltext/`.

> **Source**: [https://github.com/Aperivue/medsci-skills/tree/main/skills/fulltext-retrieval](https://github.com/Aperivue/medsci-skills/tree/main/skills/fulltext-retrieval)

# lit-fulltext

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

- OA PDFs (and optional `.md` conversions) landed in `ref/refer/`
- `ref/refer/retrieval_report.json` — per-DOI report including `source_identity` and `file_sha256`
- `ref/refer/manual_needed.txt` — paywalled / not-OA items (no bypass)

## Scripts

| Script | Role |
|---|---|
| `scripts/fetch_oa.py` | **Required.** OA resolvers only (Unpaywall / PMC / OpenAlex / Crossref / arXiv). Paywalled -> `manual_needed.txt`. |
| `scripts/pdf_to_md.py` | **Optional** (upstream AGPL dependency). Default: do not require; convert only when the same papers will be re-read often. |

Contact email for Unpaywall ToS: read from **Vault** (owner contact / corresponding). Never hard-code an address in this pack.

```bash
python scripts/fetch_oa.py worklist.tsv --output ref/refer/ --email "$(vault-contact-email)"
# optional:
python scripts/pdf_to_md.py ref/refer/ -v
```

## Hard rules

- OA only. Never bypass a paywall or publisher access control.
- Do not attach Zotero "Find Available PDF" or lit-sync flows in this pack.
- Do not blind-download the full ~30 abstract/NLM cite list; gate first, then gap-fill.

## Handoffs

- Need citations / NLM + abstracts only -> `verify-refs`
- Need search expansion -> `lit-search`
- Design change after reading full text -> `design-study`
