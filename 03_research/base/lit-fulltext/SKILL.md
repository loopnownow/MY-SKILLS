---
name: "lit-fulltext"
description: "OA full-text retrieval for DOI|PMID tables from lit-search/verify-refs; gate then gap-fill into ref/refer/."
---

# lit-fulltext

Capability body: [MODULE.md](MODULE.md).

- Required script: `scripts/fetch_oa.py` (OA only; paywalled -> `manual_needed.txt`; report with `source_identity` / sha256).
- Optional: `scripts/pdf_to_md.py` (AGPL; not required by default).
- Output root: always `ref/refer/`.
- Contact email: Vault only. No Zotero / lit-sync in this pack.
