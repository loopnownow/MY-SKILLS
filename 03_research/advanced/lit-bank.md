# 实验室文献库（lit-bank）

**Standing (2026-10-21 owner):** maintain a reusable citation bank — **no PDF/full text**. Store bibliographic records in **NLM** form; when inserting into a manuscript, render as **Vancouver**. Every record must carry a short **主要结果|结论** line for next-time reuse.

**Owner:** Victor (ingest / QC / theme tags). **Router:** Aitor. **Path lookup in 0doc:** Bai.

## SSOT location (0doc)

```
{doc_root}\_library\lit-bank\
  README.md
  index.csv                 # master ledger (one row per DOI)
  _archived\                # base 过窗研究文（可选）
```

Skills hold **this procedure only** — never mirror the CSV into MY-SKILLS. Create the `lit-bank\` tree on 0doc only after owner consent (folder-create rule).

## Layout note (2026-10-23)

On disk under `_library\lit-bank\` the old `advanced\` / `base\` **directory wrappers were flattened**. `layer=advanced|base` remains a **CSV column**, not a folder. Method docs: skill `advanced/references/lit-bank-method-digest.md` (absorbed 2026-10-23; originals in **archive leftover** `{raw_root}\_lab\originals\0doc-library-methods-20261023\lit-corpus-method\` — folder still named lit-corpus-method; `{DEL}` methods park / lit-bank-method path **absent**; live bank name remains **lit-bank**).

## Layers

| Layer | Who / what | Keep |
|---|---|---|
| `advanced` | SCI with group authors **Aitor** (published author forms on group papers), **Qiang Jinwei / 强金伟**, **Shi Haifeng / 石海峰** (any co-author position) | All years; tag `themes[]` by research direction |
| `base` | External refs that passed DOI verify (`verify-refs` / citation-verify) | Research: **publication year ≥ now−5**. **Guideline / diagnostic standard:** latest edition only (may be older than 5y); set `kind=guideline` or `standard` + `edition` |

Own-group papers live in **advanced** only (do not duplicate into base).

## Storage vs cite-time formats

| Moment | Format | Rule |
|---|---|---|
| In `index.csv` / cards | **NLM** | One string field `citation_nlm` (author list, title, journal abbrev, year, volume(issue):pages, doi) |
| In manuscript / response | **Vancouver** | Convert from the NLM row at cite time (numbered list as venue requires); do not store a second full string unless a project needs a frozen Vancouver dump |

**Forbidden:** PDF, HTML full text, publisher XML dumps, or any full-text archive under lit-bank.

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
| `result_conclusion` | **Required.** Chinese or English, 1-3 sentences: main result **then** conclusion (use `\|` or `；` between 结果 and 结论). No abstract dump. |
| `themes` | Pipe-separated tags, e.g. `ASL\|DSI` / `sarcopenia` / `RC` / `organoid-IF` |
| `layer` | `advanced` \| `base` |
| `kind` | `research` \| `guideline` \| `standard` \| `other` |
| `edition` | Guideline/standard edition or year label; empty for research |
| `verified_at` | ISO date when DOI verify passed; required for `base` |
| `source_project` | Project id that triggered ingest (optional for advanced backfill) |
| `group_authors` | For advanced: which of Aitor/Qiang/Shi appear, e.g. `Aitor\|Shi` (Aitor row = owner's published name forms) |
| `notes` | Short only |

Optional per-DOI note file (still no PDF): `advanced\<doi-or-slug>.md` or `base\<doi-or-slug>.md` with the same NLM line + `result_conclusion` — only when the CSV cell is too tight; CSV remains SSOT.

## Ingest pipelines

### A. New group SCI → `advanced`

1. Confirm author match (Aitor's published name forms + 强金伟 / 石海峰).
2. Build `citation_nlm` from Crossref/PubMed (no invented fields).
3. Write `result_conclusion` from abstract or owner-supplied bullets (1-3 sentences).
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

## Prefer-cite (standing)

When drafting Introduction / Related Work / Discussion needs **group evidence**, **prefer citing `layer=advanced`** (owner-group published SCI in `{doc_root}\_library\lit-bank\index.csv`) **before** external `layer=base`. Still verify claim↔source; do not invent results; do not dump the CSV into skills.

## Cite-time use

1. Filter `index.csv` by `themes` / `layer` / `year`. For group evidence, apply **Prefer-cite** (`advanced` before `base`).
2. Read `result_conclusion` to decide if the claim fits.
3. Emit **Vancouver** in the manuscript; keep NLM in the bank unchanged.
4. Literature search still → Victor; path inventory in 0doc → Bai.

## Out of scope

- Live project `ref/citation/` working sets (per-project; may cite bank rows by DOI)
- `05-manuscript` submission Word archive
- Web search scratch lists that never passed DOI verify

## ORCID / advanced publication pointer

- ORCID iD (public): `0000-0001-5062-0230` — works via `https://pub.orcid.org/v3.0/0000-0001-5062-0230/works`
- Data SSOT: `{doc_root}\_library\lit-bank\index.csv` (`layer=advanced`). Skills hold **procedure only** — never mirror the paper list here.
- ORCID iD roster: `{doc_root}\mem\NL.xlsx`（城城指定；含 ORCID 列）。Works backfill (2026-10-27 Asia/Shanghai): 48 ORCID work-groups → **42** already/newly in `index.csv`; disposition ledger `{doc_root}\_library\lit-bank\orcid-works-20261027\personal-works.csv` (+ README). CN journals excluded; SSRN/Research Square preprints noted, not ingested as SCI.
- Prefer-cite: see section above (`layer=advanced` before `base`).

## Pointers

- Verify body: `03_research/base/verify-refs/`
- Advanced verify protocol: `03_research/advanced/citation-verify.md`
- 0doc map: `{doc_root}\README.md` (add lit-bank row when folder exists)
