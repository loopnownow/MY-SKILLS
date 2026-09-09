# Query sources (evolvable)

Prefer **live / official** APIs and journal sites when available. Curated JCR layer CSVs in this pack are a **yearly rebuild screening cache** only — use them for Phase-1 pool membership, not as durable delivery metrics.

This list may grow with user needs. Do not treat it as frozen. Annually updated **values** (IF, quartile, APC, volume, review time, …) are **QUERY ONLY** — never bake into skill text or DB-like files (`persistence.md`).

## Primary evolvable sources (prefer these)

| Source | URL / access | Typical use |
|---|---|---|
| **OpenAlex** | https://openalex.org/ | Works, citations, venue metadata, ~3y volume / similarity |
| **Crossref** | https://www.crossref.org/ | DOI, publisher metadata |
| **Europe PMC** | https://europepmc.org/ | Full-text / abstract search for MJF/fit |
| **Journal / publisher sites** | per title | AIM, author instructions, APC, submission URL (authoritative for Phase 2) |
| **Clarivate JCR** (when licensed) | official API / client | JIF Percentile, JCI, Quartile, annual articles — rebuild input only for raw workbook |

Official JCR client example: https://github.com/clarivate/wosjournals-python-client

## Auxiliary query sources (not fixed dependencies)

LetPub, community notes, and third-party scrapers may **supplement** acceptance/cycle signals when official rates are missing. They are **not** hard dependencies and must not be the sole source of truth.

| Source | URL | Typical use |
|---|---|---|
| LetPub | https://www.letpub.com/ | Acceptance, cycle, community signals (secondary) |
| keros68/sci-select | https://github.com/keros68/sci-select | SCI filter; IF, LetPub acceptance/cycle, warning, OA |
| kkunkunya/journal-research-agent-plugins | https://github.com/kkunkunya/journal-research-agent-plugins | Multi-source check via OpenAlex, Crossref, LetPub archives |
| hitfyd/ShowJCR | https://github.com/hitfyd/ShowJCR | CAS partition, JCR, warning lists, Top markers |
| zengxiaofei/letpub_spider | https://github.com/zengxiaofei/letpub_spider | LetPub historical volume/acceptance/speed notes |
| k-dense-ai/scientific-agent-skills | https://github.com/k-dense-ai/scientific-agent-skills | OpenAlex/Crossref; ~3y volume and paper vectors |

## External journal-recommender (capability provider only)

`zero565656/journal-recommender` (https://github.com/zero565656/journal-recommender) may be used as a **query / candidate-pool** helper (abstract match, metadata scrape).  

**Do not** install or mount it as a MY-SKILLS skill. It is a **data/capability provider**, not the top-level decision maker. Absorb rewritten Fit / Risk / Tier / Evidence methods into module 04; keep current metrics as 03 query-only (`persistence.md` absorb/query/delete table).

## Screening vs display vs persist

| Kind | Role | Persist in pack? |
|---|---|---|
| Layer CSVs (`layer2-*.csv`, `layer3-*.csv`, …) | Yearly screening cache from JCR rebuild | Yes (rebuild yearly; discard raw) |
| JIF / JCR·JCI quartile / annual volume / APC / review time | Runtime display or Phase-2 lookup | **No** durable values — query only |
| Submission URLs | Durable portal links | Yes → `submission-urls.csv` |
| Query-source list (this file) | Framework / workflow | Yes (capability list, not metric tables) |

Monitor ~3–5y volume change for sudden expand/shrink; combine official metrics with auxiliary acceptance when rates are missing; check CAS warning, JCR Top, and Green OA self-archive policy when relevant. Every queried value: `value | source | retrieval_date | confidence`. **Unknown ≠ Low Risk.**
