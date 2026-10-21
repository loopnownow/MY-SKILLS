# 实验室文献库（lit-corpus）

**Standing (2026-10-21 owner):** maintain a reusable citation corpus — **no PDF/full text**. Store bibliographic records in **NLM** form; when inserting into a manuscript, render as **Vancouver**. Every record must carry a short **主要结果|结论** line for next-time reuse.

**Owner:** Victor (ingest / QC / theme tags). **Router:** Aitor. **Path lookup in 0doc:** Bai.

## SSOT location (0doc)

```
D:\0Grok\0doc\04-lab-reference\lit-corpus\
  README.md
  index.csv                 # master ledger (one row per DOI)
  personal\                 # 本组已发 SCI（Aitor / 强金伟 / 石海峰）
  base\                     # DOI 审过的外源文献（近 5 年；或现行指南/诊断标准）
  _archived\                # base 过窗研究文（可选）
```

Skills hold **this procedure only** — never mirror the CSV into MY-SKILLS. Create the `lit-corpus\` tree on 0doc only after owner consent (folder-create rule).

## Layers

| Layer | Who / what | Keep |
|---|---|---|
| `personal` | SCI with group authors **Aitor** (published author forms on group papers), **Qiang Jinwei / 强金伟**, **Shi Haifeng / 石海峰** (any co-author position) | All years; tag `themes[]` by research direction |
| `base` | External refs that passed DOI verify (`verify-refs` / citation-verify) | Research: **publication year ≥ now−5**. **Guideline / diagnostic standard:** latest edition only (may be older than 5y); set `kind=guideline` or `standard` + `edition` |

Own-group papers live in **personal** only (do not duplicate into base).

## Storage vs cite-time formats

| Moment | Format | Rule |
|---|---|---|
| In `index.csv` / cards | **NLM** | One string field `citation_nlm` (author list, title, journal abbrev, year, volume(issue):pages, doi) |
| In manuscript / response | **Vancouver** | Convert from the NLM row at cite time (numbered list as venue requires); do not store a second full string unless a project needs a frozen Vancouver dump |

**Forbidden:** PDF, HTML full text, publisher XML dumps, or any full-text archive under lit-corpus.

## Required fields (`index.csv`)

Header (UTF-8):

```text
doi,pmid,year,citation_nlm,result_conclusion,themes,layer,kind,edition,verified_at,source_project,group_authors,notes
```

| Field | Rule |
|---|---|
| `doi` | Primary key; lowercase; required for research articles when DOI exists |
| `pmid` | Optional |
| `year` | Publication year |
| `citation_nlm` | Full NLM citation string |
| `result_conclusion` | **Required.** Chinese or English, 1–3 sentences: main result **then** conclusion (use `\|` or `；` between 结果 and 结论). No abstract dump. |
| `themes` | Pipe-separated tags, e.g. `ASL\|DSI` / `sarcopenia` / `RC` / `organoid-IF` |
| `layer` | `personal` \| `base` |
| `kind` | `research` \| `guideline` \| `standard` \| `other` |
| `edition` | Guideline/standard edition or year label; empty for research |
| `verified_at` | ISO date when DOI verify passed; required for `base` |
| `source_project` | Project id that triggered ingest (optional for personal backfill) |
| `group_authors` | For personal: which of Aitor/Qiang/Shi appear, e.g. `Aitor|Shi` (Aitor row = owner's published name forms) |
| `notes` | Short only |

Optional per-DOI note file (still no PDF): `personal\<doi-or-slug>.md` or `base\<doi-or-slug>.md` with the same NLM line + `result_conclusion` — only when the CSV cell is too tight; CSV remains SSOT.

## Ingest pipelines

### A. New group SCI → `personal`

1. Confirm author match (Aitor's published name forms + 强金伟 / 石海峰).
2. Build `citation_nlm` from Crossref/PubMed (no invented fields).
3. Write `result_conclusion` from abstract or owner-supplied bullets (1–3 sentences).
4. Assign `themes`; append one row to `index.csv`.
5. Do not download PDF.

### B. DOI verify pass → `base`

1. Trigger: `verify-refs` / citation-verify row status pass for an external cite.
2. Gate: if `kind=research` and `year < current_year - 5` → **skip** (or send to `_archived` only if owner asks to keep history).
3. If guideline/standard: keep only latest `edition`; retire older editions to `_archived`.
4. Fill `citation_nlm` + `result_conclusion` + `verified_at`; `layer=base`.
5. Dedup on `doi`: update in place, never second row.

### C. Annual prune (base)

- Research rows older than 5 years → `_archived/` or drop from active `index.csv` (owner choice that year).
- Guidelines: drop superseded editions.

## Cite-time use

1. Filter `index.csv` by `themes` / `layer` / `year`.
2. Read `result_conclusion` to decide if the claim fits.
3. Emit **Vancouver** in the manuscript; keep NLM in the corpus unchanged.
4. Literature search still → Victor; path inventory in 0doc → Bai.

## Out of scope

- Live project `ref/citation/` working sets (per-project; may cite corpus rows by DOI)
- `02-manuscripts` submission Word archive
- Web search scratch lists that never passed DOI verify

## Pointers

- Verify body: `03_research/base/verify-refs/`
- Personal verify protocol: `03_research/personal/citation-verify.md`
- 0doc map: `D:\0Grok\0doc\README.md` (add lit-corpus row when folder exists)
