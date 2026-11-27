---
name: "db-library"
domain: "02_data-processing"
description: >
  _DataBase family library (SQLite) and loose-table merging: dedupe + align + merge
  same-project xlsx/xls/csv into <project>_merged_YYYYMMDD.xlsx, or load into
  <family>\_PHI\<family>db; archives to <family>\__zip\<leaf>\ (in-archive tables
  unpacked into the db, non-table members stay with the archive; __zip hierarchy ≤2,
  no ethics/thesis/raw subfolders; thesis raw in <family>\_thesis\<slug>\), leaf
  keeps only 目录说明.md, leaf raw packed per unit,
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

Hard pointers:

- 路径 / 留痕 / 门禁契约 → `{RULES}\workspace-layout.md`（「家族桶三类落点」「家族库 `_PHI`」「散表归并与表格入库」）
- 临床底表清洗、缺失值、ID 完整性 → `clean-data`（本技能只做库化与归并）

## 家族库两类（2026-11-27）

- **有 PHI 的家族：** 照旧一 family 一 `<family>\_PHI\<family>db`，身份只落 `id` / `id_number`；PHI 永不下沉子库 `<slug>\<slug>db`。
- **无 PHI 的家族**（如 `OTHERS` 这类汇编族）：不建 `id` / `id_number` 身份表，家族库只留 `meta` / `dict` / `ref_project`；家族级登记用**家族编码**（family code）+ `ref_project` 映射，子库在 `meta.family_code` 记录所属家族编码，跨库引用用家族编码而非 `family_uid`；`id` / `id_number` / `family_uid` 及依赖它们的 D24 / D27 / D54 / D63 / D75 只约束有 PHI 家族。落点 / 库文件命名 / 门禁 → `{RULES}\workspace-layout.md`（「家族桶三类落点」「家族库 `_PHI`」）。
