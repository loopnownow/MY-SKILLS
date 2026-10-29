---
name: "lit-fulltext"
domain: "03_research"
trigger: ["lit-fulltext", "全文", "fulltext", "PDF download", "open access PDF"]
outputs: ["fulltext_files", "retrieval_report"]
owner: "03_research/base/lit-fulltext/MODULE.md"
---

Batch open-access full-text retrieval for a DOI/PMID worklist.
True-absorbed from Aperivue medsci-skills/skills/fulltext-retrieval on 2026-10-30.
Not mounted. Seat: 03_research.

> **Source**: [https://github.com/Aperivue/medsci-skills/tree/main/skills/fulltext-retrieval](https://github.com/Aperivue/medsci-skills/tree/main/skills/fulltext-retrieval)

# lit-fulltext

## Project-start chain

Fixed order (do not skip when this id is on the chain):

1. `design-study` (light: keywords; materials prefer `ref/refer/`, else ask owner)
2. `lit-search`
3. `verify-refs`
4. `lit-fulltext` (gate below)
5. Return to `design-study` when the design must change

## Gate (every run on the chain)

Inspect `ref/refer/` for non-duplicate fulltext files (`.pdf` | `.html` | `.md`).

Skip download and only ledger/account when **all** hold:

- distinct fulltext file count >= 5 (dedupe by DOI, PMID, and file hash)
- set covers highly relevant papers from the last 5 years
- set includes latest diagnostic criteria
- set includes latest international guideline

Otherwise fill gaps via OA resolvers and land files under `ref/refer/`.
Paywalled items go to a `manual_needed` list. Never bypass a paywall.

## Scripts

Vendor upstream bodies into `scripts/` from
https://github.com/Aperivue/medsci-skills/tree/main/skills/fulltext-retrieval
(`fetch_oa.py`, `pdf_to_md.py`) before the first live run. Until then only the
MODULE/gate and registry row are live.

```bash
python scripts/fetch_oa.py dois.txt --output ref/refer/ --email <contact-email>
python scripts/pdf_to_md.py ref/refer/ -v
```

See [SKILL.md](SKILL.md), [scripts/VENDOR.md](scripts/VENDOR.md), and [references/upstream-skill.yml](references/upstream-skill.yml).

## Handoffs

- Need citations / NLM + abstracts only -> `verify-refs`
- Need search expansion -> `lit-search`
- Design change after reading full text -> `design-study`
