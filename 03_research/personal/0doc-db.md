# 0doc document-library lookup (Bai)

**Standing rule (2026-10-21 owner):** searching / looking up / inventorying `{doc_root}` is **Bai’s** job. Aitor routes and monitors.

**Tree revision (2026-10-23):** machine library is **`_library/`** (renamed from `03-research/`; skill seat `03_research` unchanged). SSOT lit index: `_library\lit-bank\index.csv`. **Method absorb (2026-10-23):** `_library\{lab-ref-method,lit-bank-method,lab-ste,scanner-registry}` + `study-design\fill-protocol\jinshan-form-pack.md`（已吸收；原路径已不在 `_library`） → digests in `03_research/personal/references/` + `fill-protocol/jinshan-form-pack-digest.md` + expanded `05_manuscript/base/vocab/L3/`; methods **archive leftover** `{raw_root}\_lab\originals\0doc-library-methods-20261023\` (`lit-corpus-method\` etc.; `{DEL}\_by-project\0doc-library-methods-20261023\` **absent**); durable `{DEL}\_by-project\skill-harvest-sources-20261024\sources\library-methods-20261023\` (includes `lit-bank-method\`). Live scanner xlsx → `templates\scanner-parameter-registry.xlsx`. Ethics / lab-ref-ranges / lit-bank data **untouched**.

**Live tops (owner standing 2026-10-24):** lookup starts at `_library`, `_bank`, `_code`, `templates`, `mem`, `GitHub`, `test`, `skill-harvest`. Older names (`00-inbox`, `01-thesis`, `02-manuscripts`, `03-review-replies`, `04-lab-reference`, `05-grants`, `06-review-bank`, `07-ethics`, `doc-word`) are **retired**. Human seats `03-research` / `05-manuscript` / `06-review` / `07-response` are **retired** (parked under `{raw_root}\_lab\originals\0doc-03-07-seats-20261023`) — do not treat those folder names as live `{doc_root}` tops. Map table: `{doc_root}\README.md` + `STRUCTURE.md`.

## When

Owner (or Aitor handoff) asks to 查 / 找 / 检索 / 盘点 / 定位 anything that lives in:

| Folder | Typical ask |
|---|---|
| `_library` (ex-`03-research`) | lit-bank library, 选刊, ethics (incl. PHI), ~~lab-ste / lab-ref-method / lit-bank-method / scanner-registry method~~ (→ methods park 20261023) / lab-ref-ranges, study-design (STROBE→templates; fill-protocol digest), figures; ~~papers/fulltext/grants~~ → `{DEL}\_by-project\0doc-library-ftp-20261023\` (digest: grant-* digests under `03_research/personal/references/` + `papers-card-schema.md`; durable `{DEL}\_by-project\skill-harvest-sources-20261024\sources\library-ftp-20261023\`). Scanner gap (Skyra / Sensation **not found**; do not invent parameters): `references/scanner-registry-digest.md` |
| `_bank` | machine layer JSONL/FTS/GATES/recovery text. Live review text `{doc_review_bank}\bank\review-text.jsonl` (+ `REVIEW-TEXT.tsv`); live replies `{doc_review_replies}\bank\flattened.jsonl` |
| `_code` | runnable scripts by skill tree `NN-layer\<fine-id>` (**no** `base\` under `_code` 02–07). Do not vendor `.py` into MY-SKILLS. Stats library `{code_stats}` |
| `templates` | skill-pinned gold templates; live scanner xlsx `templates\scanner-parameter-registry.xlsx` |
| `mem` | long-term memos (not a second Rules/Skills tree) |
| `GitHub` | clones: MY-SKILLS `{skills_git}`, MY-RULES `{rules_git}`; stats modules master `{code_modules_master}` (local git only) |
| `test` | bank QC `{code_bank_qc}` |
| `skill-harvest` | harvest SSOT `{doc_skill_harvest}` |

**Word originals** are not inside the `0doc` tree: `{DEL}\_by-project\0doc-word-sources\`.

**Moved to 0del (not live):** `03-research\briefs (historical; now under D:\00db\_lab\originals)`, `07-response\reply-units`, `_bank\md-build` → `D:\00db\_lab\originals\0doc-struct-20261022\` (folder shrink 2026-10-23). Former `05-manuscript` / `06-review` / `07-response` human seats are in that same park class (`{raw_root}\_lab\originals\0doc-03-07-seats-20261023`), not live tops.

## How

1. Start from README + STRUCTURE + the relevant index when present: park grants `{DEL}\_by-project\0doc-library-ftp-20261023\grants\_index\00-master-index.md` / skill `grant-index-digest.md`; live review text `{doc_review_bank}\bank\review-text.jsonl`; `<topic>\INDEX.md`. Do not open retired `06-review\00-index.csv` as a live index.
2. Prefer filename + index hits; open files only as needed (read-only).
3. Reply in Chinese: **paths first**, then 2–6 lines of what was found; list approval numbers for ethics.
4. `_library\ethics`: minimize PHI in chat; never commit ethics originals to GitHub. JIEC2025-S79 follow-up review locked files — do not edit.

## Out of scope

- Web / PubMed literature → Victor
- Writing Track Changes on a live manuscript → Aitee
- Stats / puzzle assembly (拼图) → Loopnow
- Bulk bank rebuild scripts when owner said「交给cline」→ Cline

Ownership SSOT: `00_orchestrator/references/ownership-contract.md` §0doc database lookup.
