# 0doc 文档库查询（Bai）

**Standing rule (2026-10-21 owner):** searching / looking up / inventorying `{doc_root}` is **Bai’s** job. Aitor routes and monitors.

**Tree revision (2026-10-23):** machine library is **`_library/`** (renamed from `03-research/`; skill seat `03_research` unchanged). SSOT lit index: `_library\lit-corpus\index.csv`. **Method absorb (2026-10-23):** `_library\{lab-ref-method,lit-corpus-method,lab-ste,scanner-registry}` + `study-design\fill-protocol\jinshan-form-pack.md` → digests in `03_research/personal/references/` + `fill-protocol/jinshan-form-pack-digest.md` + expanded `05_manuscript/base/vocab/L3/`；park `{DEL}\_by-project\0doc-library-methods-20261023\`；durable `skill-harvest\sources\library-methods-20261023\`. Live scanner xlsx → `templates\scanner-parameter-registry.xlsx`. Ethics / lab-ref-ranges / lit-corpus data **untouched**.

**Tree revision (2026-10-23 seats):** top-level seats align with MY-SKILLS `03/05/06/07`. Old names (`00-inbox`, `01-thesis`, `02-manuscripts`, `03-review-replies`, `04-lab-reference`, `05-grants`, `06-review-corpus`, `07-ethics`, `doc-word`) are **retired** — do not look for them under `0doc`. Map table: `{doc_root}\README.md` + `STRUCTURE.md`.

## When

Owner (or Aitor handoff) asks to 查 / 找 / 检索 / 盘点 / 定位 anything that lives in:

| Folder | Typical ask |
|---|---|
| `_library` (ex-`03-research`) | 文献库 lit-corpus、选刊、伦理 ethics（含 PHI）、~~lab-ste / lab-ref-method / lit-corpus-method / scanner-registry method~~（→ methods park 20261023） / lab-ref-ranges、study-design（STROBE→templates；fill-protocol digest）、figures；~~papers/fulltext/grants~~ → `{DEL}\_by-project\0doc-library-ftp-20261023\`（digest: grant-* digests under 03_research/personal/references/ + `papers-card-schema.md`；durable `skill-harvest\sources\library-ftp-20261023\`） |
| `05-manuscript` | 学位论文与投稿稿 papers/fulltext/units/quotes；`revision-history` 不可再生 |
| `06-review` | 本人评阅语料：`source/` 原件 + `text/` 提取 |
| `07-response` | 外审意见与回复：`units/`、`flattened/`、`_meta/`、papers/fulltext/links |
| `_corpus` | 机器层 JSONL/FTS/GATES/抢救文本（脚本产出） |
| `_code` | 按技能树 `NN-层\base\细ID` 组织的可运行脚本 |
| `templates` / `mem` | skill 钉死模板金文件；长期备忘 |

**Word 原件**不在 `0doc` 树内：`{DEL}\_by-project\0doc-word-sources\`。

**已迁 0del（勿再当现役）:** `03-research\briefs (historical; now under D:\00db\_lab\originals)`、`07-response\reply-units`、`_corpus\md-build` → `D:\00db\_lab\originals\0doc-struct-20261022\`（2026-10-23 减夹）。

## How

1. Start from README + STRUCTURE + the relevant index file (`{DEL}\_by-project\0doc-library-ftp-20261023\grants\_index\00-master-index.md`（park） / skill `grant-index-digest.md`、`06-review\00-index.csv`、`<主题>\INDEX.md`) when present.
2. Prefer filename + index hits; open files only as needed (read-only).
3. Reply in Chinese: **paths first**, then 2–6 lines of what was found; list approval numbers for ethics.
4. `_library\ethics`: minimize PHI in chat; never commit ethics originals to GitHub. JIEC2025-S79 跟踪审查 locked files — do not edit.

## Out of scope

- Web / PubMed literature → Victor  
- Writing Track Changes on a live manuscript → Aitee  
- Stats / 拼图 → Loopnow  
- Bulk corpus rebuild scripts when owner said「交给cline」→ Cline  

Ownership SSOT: `00_orchestrator/references/ownership-contract.md` §0doc database lookup.
