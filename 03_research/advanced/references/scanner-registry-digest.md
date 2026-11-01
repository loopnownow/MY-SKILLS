# scanner-registry-digest

**Absorbed (historical):** 2026-10-23 from then-live `_library/scanner-registry/README.md` (method only). That folder is **retired** — do not open `_library\scanner-registry` as a live seat.
**Data workbook:** live copy under `{doc_root}\templates\scanner-parameter-registry.xlsx` (refreshing query table — not vendored into GitHub).

## Live pointers (after move)

| Role | Path |
|---|---|
| Durable original (README + xlsx) | `{doc_skill_harvest}\sources\library-methods-20261023\scanner-registry\` |
| HISTORIC park (cleared; do not resolve) | ~~`{DEL}\_by-project\0doc-library-methods-20261023\scanner-registry\`~~ |
| Live xlsx (query) | `{doc_root}\templates\scanner-parameter-registry.xlsx` |
| Build scripts (MY-CODES tools) | `{code_data_processing}\lab-reference\scanner_registry_{extract,build,rows}.py` |
| Word archives | `{doc_word_archive}`（原 0del word-sources park 已清；t1490u） |

## Coverage snapshot (as of README 2026-10-17)

- 92 rows = study × site × device × sequence; 29 studies (US 5 / CT 8 / MRI 17); 42 devices.
- Source tiers: 01 thesis 31 · 02 manuscript 58 · 03 response 3.
- Verify status: cross-version agree 43 · single-source 45 · conflict 4 (reasons in `备注`).

## Sheet map

| sheet | Role |
|---|---|
| `01_query` | Main query (47 cols; freeze panes + Excel table) |
| `02_devices` | Device dedupe |
| `03_contrast_timing` | Contrast / phase (per study) |
| `04_sources` | Source file index |
| `05_gaps` | Gap ledger |
| `06_dictionary` | Enum dictionary (modality / vendor / sequence / phase / verify status) |

## Method norms (hard)

1. Keep **原文** columns beside **规范** columns; normalize synonyms only — no invented facts.
2. Missing in source → `未标注`. Do not invent vendor country of origin; do not deanonymize centers.
3. `生产地(原文)` is often HQ address ≠ manufacturing site.
4. Numeric cells may hold ranges/multi-values (`4000 或 8000`, `150-320`) — preserve; split before any calc.
5. `核对状态` = four enums only; conflict detail → `备注`.
6. Every row must trace via `来源文件` + `来源位置`; `04_sources` holds full names.
7. Ultrasound = diagnostic/guidance only; exclude NMR spectrometer, LC-MS, DSA, PET. MRS sequences attach to MRI devices.
8. Protocol-level merges: `序列(规范)` may join with `/`; compound values must exist in `06_dictionary`.

## Rebuild / extend (path pointers — do not vendor `.py`)

```text
python {code_data_processing}\lab-reference\scanner_registry_extract.py --stage all
python {code_data_processing}\lab-reference\scanner_registry_build.py
```

Extract scratch → `{DEL}\harvested\scanner-registry\`（t1490u；可清）。 New study: append `ROWS` in `scanner_registry_rows.py` as `记录ID|key=value|…` (ID like `MR17-01`). New enums → `DICT_ROWS`. New field → `COLS` then rebuild; `01_query` row count must equal non-empty `ROWS`.

## Gaps pointer

See workbook `05_gaps` (and parked README) for known missing device/params — not restated here to avoid stale narrative.

## Named gap — MAGNETOM Skyra / SOMATOM Sensation (search 2026-10-19)

Search scope then: 0doc lab-reference scanner-registry, related manuscripts, and the raw DB (`{raw_root}`, formerly 00ds). Record only what that search stated. Do **not** invent protocol parameters.

- **Not found:** the literal model names MAGNETOM Skyra and SOMATOM Sensation, and no protocol table for either.
- Closest hit in that search: manuscripts that name SOMATOM only (64-row / 128-slice). No Sensation subtype. No complete Ultravist / iopromide protocol.
- Do not mix Skyra into the Aitor-format scanner pair Magnetom Verio / Canon Aquilion.
- Until a source row exists, leave kVp, mA, TR/TE, contrast dose, and any other Skyra or Sensation parameter as `未标注` (method norm 2). Do not write guessed numbers into this skill.
