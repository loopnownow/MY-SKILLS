# 0doc document-library lookup (Bai)

**Standing rule (2026-10-21 owner):** searching / looking up / inventorying `{doc_root}` is **Bai’s** job. Aitor routes and monitors.

**Tree revision (2026-10-23):** machine library is **`_library/`** (renamed from `03-research/`; skill seat `03_research` unchanged). SSOT lit index: `_library\lit-bank\index.csv`. **Method absorb (2026-10-23):** `_library\{lab-ref-method,lit-bank-method,lab-ste,scanner-registry}` + `study-design\fill-protocol\jinshan-form-pack.md`（已吸收；原路径已不在 `_library`） → digests in `03_research/advanced/references/` + `fill-protocol/jinshan-form-pack-digest.md` + expanded `05_manuscript/base/vocab/L3/`; methods **archive leftover** `{raw_root}\_lab\originals\0doc-library-methods-20261023\` (`lit-corpus-method\` etc.; `{DEL}\_by-project\0doc-library-methods-20261023\` **absent**); durable `{doc_skill_harvest}\sources\library-methods-20261023\` (includes `lit-bank-method\`). Live scanner xlsx → `_library\scanner-registry\scanner-parameter-registry.xlsx` (t1553u; was briefly under `templates\`). Figure palettes → `_library\figures\lab-palettes.md`. Ethics / lab-ref-ranges / lit-bank data **untouched**.

**Live tops (owner standing 2026-11-01):** lookup starts at `_library`（含 `glossary`）, `templates`, `mem`, `test`, `skill-harvest`. `_bank` **retired 2026-11-01** → `_library\glossary`（三层条目 + sections 指针页）+ `_library\glossary\banks`（证据层）；`_code` **retired 2026-11-01** → `{code_stats}`. Older names (`00-inbox`, `01-thesis`, `02-manuscripts`, `03-review-replies`, `04-lab-reference`, `05-grants`, `06-review-bank`, `07-ethics`, `doc-word`) are **retired**. Human seats `03-research` / `05-manuscript` / `06-review` / `07-response` are **retired** (parked under `{raw_root}\_lab\originals\0doc-03-07-seats-20261023`) — do not treat those folder names as live `{doc_root}` tops. Map table: `{doc_root}\README.md` + `STRUCTURE.md`.

## When

Owner (or Aitor handoff) asks to 查 / 找 / 检索 / 盘点 / 定位 anything that lives in:

| Folder | Typical ask |
|---|---|
| `_library` (ex-`03-research`) | lit-bank library, 选刊, ethics (incl. PHI), ~~lab-ste / lab-ref-method / lit-bank-method / scanner-registry method~~ (→ methods park 20261023) / lab-ref-ranges, study-design (STROBE→templates; fill-protocol digest), figures; ~~papers/fulltext/grants~~ → HISTORIC `{DEL}\_by-project\0doc-library-ftp-20261023\`（已清；耐久 `{doc_skill_harvest}\sources\library-ftp-20261023\`） (digest: grant-* digests under `03_research/advanced/references/` + `papers-card-schema.md`; durable `{doc_skill_harvest}\sources\library-ftp-20261023\`). Scanner gap (Skyra / Sensation **not found**; do not invent parameters): `references/scanner-registry-digest.md` |
| `_library\glossary`（ex-`_bank`, 2026-11-01） | 自有写作语料：三层条目 `words/` `sentences/` `paragraphs/` + `sections/` 指针页 + `index.csv` 13 列（全席位根 = `{doc_glossary}`）；证据层 `banks\`（jsonl + `glossary.db` FTS；GATES.md 已清）。审稿文本 `{doc_glossary_banks}\review-text.jsonl`（+ `REVIEW-TEXT.tsv`）；回复 `{doc_glossary_banks}\flattened.jsonl`；段落层 `{doc_glossary_banks}\paras.jsonl` |
| `_code` | runnable scripts by skill tree `NN-layer\<fine-id>` (**no** `base\` under `_code` 02-07). Do not vendor heavy analysis `.py` into MY-SKILLS. Stats library `{code_stats}` |
| `templates` | skill-pinned gold templates (`Aitor-format-gold-response.docx`, `ethics-blank`, STROBE); palettes/scanner xlsx live under `_library\figures\` / `_library\scanner-registry\` |
| `mem` | long-term memos (not a second Rules/Skills tree) |
| `GitHub` | clones: MY-SKILLS `{skills_git}`, MY-RULES `{rules_git}`; stats modules master `{code_modules_master}` (local git only) |
| `test` | bank QC `{code_bank_qc}` |
| `skill-harvest` | harvest SSOT `{doc_skill_harvest}` |

**Word originals** are not inside the `0doc` tree: `{doc_word_archive}`（原 `{DEL}\_by-project\0doc-word-sources\` park 已清；t1490u）。

**Moved to 0del (not live):** `03-research\briefs (historical; now under D:\00db\_lab\originals)`, `07-response\reply-units`, `_bank\md-build` → `D:\00db\_lab\originals\0doc-struct-20261022\` (folder shrink 2026-10-23). Former `05-manuscript` / `06-review` / `07-response` human seats are in that same park class (`{raw_root}\_lab\originals\0doc-03-07-seats-20261023`), not live tops.

## How

1. Start from README + STRUCTURE + the relevant index when present: grant digests under `03_research/advanced/references/`（HISTORIC park grants index cleared；t1490u） / skill `grant-index-digest.md`; live review text `{doc_glossary_banks}\review-text.jsonl`; `<topic>\INDEX.md`. Do not open retired `06-review\00-index.csv` as a live index.
2. Prefer filename + index hits; open files only as needed (read-only).
3. Reply in Chinese: **paths first**, then 2-6 lines of what was found; list approval numbers for ethics.
4. `_library\ethics`: minimize PHI in chat; never commit ethics originals to GitHub. JIEC2025-S79 follow-up review locked files — do not edit.

## Out of scope

- Web / PubMed literature → Victor
- Writing Track Changes on a live manuscript → Aitee
- Stats / puzzle assembly (拼图) → Loopnow
- Bulk bank rebuild scripts when owner said「交给cline」→ Cline

Ownership SSOT: `00_orchestrator/references/ownership-contract.md` §0doc database lookup.
