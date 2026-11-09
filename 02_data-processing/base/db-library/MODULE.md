---
name: "db-library"
domain: "02_data-processing"
trigger: ["散表", "合并", "去重", "_db", "SQLite", "入库", "台账", "REVOKED"]
inputs: ["loose_tables", "family_tree"]
outputs: ["merged_workbook", "family_db", "move_ledger"]
quality_control: "三层去重; sha256 台账; 行数守恒; structure_check 24/24"
owner: "02_data-processing/base/db-library/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Loose tables → merged workbook / family SQLite library

Contract only for db-library: scope, phases, bans, verification, and pointers. Recipes live in
[references/merge-tables.md](references/merge-tables.md) and [references/build-db.md](references/build-db.md).
Path / ledger / gate rules live in `{RULES}\workspace-layout.md` — do not restate them here.

## Scope

| In | Out |
|---|---|
| 家族根 / 叶根散表盘点（文件数、行、列、sha256、版本簇） | 临床底表清洗标准（表头规范、缺失值策略）→ `clean-data` |
| 三类型判定：同构纵并 / 一簿多 sheet / 单件只改名 | 统计分析、建模、图 → `stats-analysis` / `model-evaluation` / `plot-figures` |
| 去重三层（文件 sha → 整表重复/子集 → 行/实体） | 影像 DICOM / NIfTI 处理 → `preprocess-imaging` |
| 合并成 `<项目名>_merged_YYYYMMDD.xlsx` | 压缩档解压 / 拆包（压档不入库、不移动） |
| 建 `<family>\_db\<family>db` + `目录说明.md` | 改 `_diseases.csv` / `_index.csv` 的**语义**（只按既有格式登记事实） |
| 原件 → `{DEL}\_by-function\<batch>\originals\` + `*-MOVED-*.tsv` | 删除原件（禁删；只移 `{DEL}`） |

## Phases

1. **P0 盘点** — 只读扫描目标叶 / 家族根：表格清单（xlsx/xls/csv）、字节、每 sheet 行列、sha256、名称版本簇、mtime 桶。
2. **P1 判定** — 逐项目定处理类型；三层去重预判；列出「需开表核对」清单（版本簇、可疑重复）。
3. **P2 构建（dry-run）** — 只写 `out/`，不动 `_DataBase`；先给用户看清单 / 抽样。
4. **P3 校验** — 行数守恒、键唯一、缺失盘点、sha256 100%、`PRAGMA integrity_check`、抽样查询。
5. **P4 落盘** — merged / 库落位；原件移 `{DEL}` + 台账；叶 / 家族 `目录说明.md` 追加段；`_index.csv` note。
6. **P5 收口** — `cd D:\MyProjects\_Docs && python -B test/structure_check.py` 24/24；批次报告 `<batch>-REPORT.md`。

## Bans

- 不得跳过去重直接拼；不得以 mtime 当新旧或去重依据（迁移刷新 mtime）。
- 不得覆盖 / 删除源文件；原件只移 `{DEL}` 并留 sha256 台账。
- 不得把压缩档入库、不得就地解压（`_share` 压档原样留叶）。
- 不得把 `_DataBase` 的件回流项目树（用户口径：不回流）。
- 未获当轮点名不得写 `_DataBase`（写盘总闸）；不确定即停、先问。
- 手工发现「台账 dst 不存在」时：先取证（回收站 → `E:\Aitor` 冻结快照 → 全盘落点），问过主人再动；确认清除才写 `REVOKED-*.tsv`，不得静默恢复或删除。

## Failure modes（本轮实测）

| 症状 | 原因 | 处理 |
|---|---|---|
| 源文件「漏读」 | 文件名含 U+00A0 等不可见字符 | `norm()` 归一化后再匹配 |
| 合并后行数偏多 / 表头当数据 | 一张表多段拼接、重复表头行 | 表头驱动分段；遇表头建映射，重复表头行丢弃 |
| 年龄 / 性别错列 | 段 2、3 两列与表头互换 | 逐段检测互换并统一到 `COLS` |
| 表头落在第 3 行、留空行 | 有说明行时行号偏移 | `write_sheet` 用 `r0=1` |
| xlrd 报错但文件只有几十字节 | 伪装 `.xls` 的 TSV | 文本回退（按 tab 解析） |
| 年份表读成乱码 | GBK 编码的 `.XLS` | 显式编码回退 |
| 宽表把 fact 撑爆 | 表头数字占比 > 0.6（谱图 / 矩阵） | 只存 sheet blob，不入 fact |
| 同一 sheet 在多文件重复 | 版本簇另存 | L2 只记 `sheet_dup` 边，不存第二份 blob |

## Verification checklist

- [ ] 行数守恒：源行（去重后）= 合并行；差异有逐条理由
- [ ] 键唯一 / 缺失盘点有数（姓名、性别、年龄、部位…）
- [ ] 原件 sha256 全部核验通过，台账行数 = 移动件数
- [ ] 库：`PRAGMA integrity_check` ok；表数 / fact / entity 与报告一致；抽样查询能复现已知值
- [ ] `目录说明.md` 追加段含口径、重算文件数 / 大小、库路径、台账指针
- [ ] `_index.csv` note 追加日期 + 落点，不留悬空 `→` 路径
- [ ] `structure_check.py` 24/24 PASS
