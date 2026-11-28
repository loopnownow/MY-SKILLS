---
name: "db-library"
domain: "02_data-processing"
description: >
  _DataBase family library (SQLite) and loose-table merging: dedupe + align + merge
  same-project xlsx/xls/csv into <project>_merged_YYYYMMDD.xlsx, or load into
  <family>\_PHI\<family>db; archives to <family>\__zip\<leaf>\ (in-archive tables
  unpacked into the db, non-table members stay with the archive; __zip hierarchy ≤2
  except the thesis branch __zip\thesis\<slug>\; no ethics/raw subfolders; do not
  create _thesis), leaf keeps only 目录说明.md, leaf raw packed per unit,
  originals to {DEL} with sha256 ledger. Single-lab merge (multi-family → 1 lib,
  core-6t schema: 7 real tables + 5 read-only compat views) and in-place db repair
  (entity rebuild/drop, derived sheets, PHI pseudonymisation).
  Triggers: 散表合并, 去重, 建库, _PHI, 短码库, 家族库, 入库, 台账, REVOKED, merged,
  压缩档, 解档, __zip, 叶说明, raw 压档, 单库, 6t, 修库, verify_db.
owner: "02_data-processing/base/db-library/MODULE.md"
---

# db-library

Capability body: [MODULE.md](MODULE.md). Do not duplicate it here.

Recipes:

- [references/merge-tables.md](references/merge-tables.md) — 散表归并（三类型、表头驱动、坑位、合并簿约定＝入库中间件 / 点名交付、版本仲裁、台账三式）
- [references/build-db.md](references/build-db.md) — 家族库（schema、三层去重、宽表规则、解档入库、QA、重建）
- [references/single-lab-db.md](references/single-lab-db.md) — 单库化与 core-6t（结构、身份键 PRIO、分流、拼接四档、7 步、迁移四验）
- [references/db-fix.md](references/db-fix.md) — 库内修库（铁律、四类修法、修后自检、假名纪律）
- [references/load-pipeline.md](references/load-pipeline.md) — 新建库（契约驱动）：先冻结 `map.csv` / `qc_codes.tsv` / `schema.sql`，再建空库、登记源、建身份、清洗、回填、收口。硬约束见 `{RULES}\db-build-contract.md`，判据见 `{RULES}\db-gates.md` D93–D99（尚未机器化 / report-only）

Hard pointers:

- 路径 / 留痕 / 门禁契约 → `{RULES}\zone-database.md`（「家族桶落点」「家族库 `_PHI`」「散表归并与表格入库」「台账落点」）
- 建库硬约束 → `{RULES}\db-build-contract.md`（契 1–10、律 1–5）；本技能不重述禁令，只给步骤
- 临床底表清洗、缺失值、ID 完整性 → `clean-data`（本技能只做库化与归并）

## 家族库两类

- **有 PHI 的家族：** 照旧一 family 一 `<family>\_PHI\<family>db`，身份只落 `id` / `id_number`；PHI 永不下沉子库 `<slug>\<slug>db`。目标态路径在 `{RAW}\Family\<family>\`（现行盘面迁入前仍可能无 `Family\` 层；本批不搬）。家族库不留 `dict` 表，格式真源为 `{RAW}\Family\dict.db`。
- **无 PHI 的家族：** 不建 `id` / `id_number` 身份表，家族库只留 `meta` / `ref_project`（不留 `dict`）；家族级登记用**家族编码**（family code）+ `ref_project` 映射，子库在 `meta.family_code` 记录所属家族编码，跨库引用用家族编码而非 `family_uid`；`id` / `id_number` / `family_uid` 及依赖它们的 D24 / D27 / D54 / D63 / D75 只约束有 PHI 家族。
- **`OTHERS` 按有 PHI 家族对待**（与 `{RULES}\zone-database.md` 一致）：`_PHI\OTHERSdb` 保留 `id` / `id_number`，PHI 不拆进子库；身份不合并到家族级。落点 / 库文件命名 / 门禁 → `{RULES}\zone-database.md`（「家族桶落点」「家族库 `_PHI`」）。
