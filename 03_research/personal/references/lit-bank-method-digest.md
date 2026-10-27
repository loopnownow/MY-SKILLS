# lit-bank-method-digest

**Absorbed:** 2026-10-23 from `_library/lit-bank-method/README.md`.
**Role:** how to rebuild / verify the lit bank. **No literature rows, no author names.**
**Procedure SSOT (skills):** `03_research/personal/lit-bank.md`

## Live pointers (after move)

| Role | Path |
|---|---|
| Durable original | `{DEL}\_by-project\skill-harvest-sources-20261024\sources\library-methods-20261023\lit-bank-method\` |
| Park | `{DEL}\_by-project\0doc-library-methods-20261023\lit-bank-method\` |
| Data SSOT (stays live) | `{doc_root}\_library\lit-bank\` (`index.csv`, `themes.md`, layer READMEs) |
| CSV header template | `03_research/personal/references/lit-bank-index.template.csv` |
| One-shot scripts (not in skills) | `{DEL}\_by-project\lit-bank\*.py` |

## Invariant rules

1. **No PDF/HTML/XML full text** in the bank — only `index.csv`, `themes.md`, short cards.
2. **`index.csv` is the only formal metadata ingress** (SSOT). Layer folders hold notes/cards only — **do not duplicate CSV**.
3. **`doi` primary key** (lowercase, normalized); one DOI → one row.
4. Every row needs `result_conclusion` as `结果：…；结论：…；限制：…` (限制 optional; fullwidth `；`). Ban: paste abstract; infer from title; correlation→causation.
5. Store **NLM** in `citation_nlm` (+ trailing `doi:`); convert to **Vancouver** at cite time — no second stored string.
6. `base` rows require `verified_at` (ISO date of last metadata verify).
7. Layers/windows: group SCI → `personal` (keep all); external DOI-verified → `base` (research year ≥ now−5; guidelines/standards = current edition + `kind`/`edition`); QC moves research >10y to `_archived`.

## Rebuild order (one full round)

```text
1  prepare_base / survey_todo / analyze_personal      # local inventory
2  gen_selection / gen_todo / gen_base_batches        # batch todos
3  fetch_personal --net | verify_crossref --net | verify_base --net
4  merge_ann / merge_base_ann
5  fix_base_rc / fix_base_tags
6  build_index / build_base
7  check_index / validate_index / make_report
```

Batch artifacts (`ann-NN.tsv`, `batch-NN.txt`, `base-todo.csv`) live under `{DEL}\_by-project\lit-bank\` — never inside `_library\lit-bank\`.

## Script groups (26 one-shots — path pointers only)

| Group | Examples | Net? |
|---|---|---|
| A candidates | `prepare_base`, `survey_*`, `gen_*`, `analyze_personal`, `list_*` | no |
| B metadata | `fetch_personal`, `fetch_base_abstracts`, `verify_crossref`, `verify_base` | **`--net` required** |
| C annotate/fix | `merge_ann`, `merge_base_ann`, `fix_base_rc`, `fix_base_tags`, `gen_needs_check` | no |
| D ingest/QC | `build_index`, `build_base`, `validate_index`, `check_index`, `make_report` | no (report → 0del) |

Hosts when `--net`: `eutils.ncbi.nlm.nih.gov:443`, `api.crossref.org:443` only. Scripts default `NET_ENABLED = False`. Fail → leave field empty + `notes=待补`; **never invent** DOI/pages/authors. Log each round: host, port, data class, whether written.

## Do not put in skills / `_library` method tree

- The 26 script bodies (middleware → 0del park)
- Intermediate TSV/JSONL/xlsx batches
- Identity-filter person/org specifics (keep in `lit-bank.md` / personal data only)
- Any PDF / full text

## Related

- Skill procedure: `../lit-bank.md`
- Needs-owner shortlist (data tree): `_library\lit-bank\needs-owner-check.md`
