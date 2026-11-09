---
name: "db-library"
domain: "02_data-processing"
description: >
  _DataBase family library (SQLite) and loose-table merging: dedupe + align + merge
  same-project xlsx/xls/csv into <project>_merged_YYYYMMDD.xlsx, or load into
  <family>\_db\<family>db; originals to {DEL} with sha256 ledger.
  Triggers: 散表合并, 去重, 建库, _db, 短码库, 家族库, 入库, 台账, REVOKED, merged.
owner: "02_data-processing/base/db-library/MODULE.md"
---

# db-library

Capability body: [MODULE.md](MODULE.md). Do not duplicate it here.

Recipes:

- [references/merge-tables.md](references/merge-tables.md) — 散表归并（三类型、表头驱动、坑位、合并簿 sheet 约定、台账）
- [references/build-db.md](references/build-db.md) — 家族库（schema、三层去重、宽表规则、QA、重建）

Hard pointers:

- 路径 / 留痕 / 门禁契约 → `{RULES}\workspace-layout.md`（「家族库 `_db`」「散表归并与表格入库」）
- 临床底表清洗、缺失值、ID 完整性 → `clean-data`（本技能只做库化与归并）
