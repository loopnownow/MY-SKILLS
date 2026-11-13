---
name: "db-library"
domain: "02_data-processing"
trigger: ["散表", "合并", "去重", "_db", "SQLite", "入库", "台账", "REVOKED", "压缩档", "_share", "解档", "家族库", "叶说明", "单库", "6t", "修库", "verify_db"]
inputs: ["loose_tables", "family_tree", "share_archives"]
outputs: ["merged_workbook", "family_db", "move_ledger", "archive_map"]
quality_control: "三层去重; sha256 台账; 行数守恒; 叶内只留说明; _share 层级 ≤2; structure_check 全门 PASS; verify_db P0=0"
owner: "02_data-processing/base/db-library/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Loose tables → merged workbook / family SQLite library

Contract only for db-library: scope, phases, bans, verification, and pointers. Recipes live in
[references/merge-tables.md](references/merge-tables.md)（散表归并）、[references/build-db.md](references/build-db.md)（建库）、
[references/single-lab-db.md](references/single-lab-db.md)（单库化与 core-6t）、[references/db-fix.md](references/db-fix.md)（库内修库）。
Path / ledger / gate rules live in `{RULES}\workspace-layout.md`（「家族库 `_db`」「散表归并与表格入库」「`_share` 家族原始件池」）— do not restate them here.

## Scope

| In | Out |
|---|---|
| 家族根 / 叶根散表盘点（文件数、行、列、sha256、版本簇） | 临床底表清洗标准（表头规范、缺失值策略）→ `clean-data` |
| 三类型判定：同构纵并 / 一簿多 sheet / 单件只改名 | 统计分析、建模、图 → `stats-analysis` / `model-evaluation` / `plot-figures` |
| 去重三层（文件 sha → 整表重复/子集 → 行/实体） | 影像 DICOM / NIfTI 处理 → `preprocess-imaging` |
| 合并成 `<项目名>_merged_YYYYMMDD.xlsx`（默认入库中间件 / 点名交付，不落叶根） | 压缩档原档入库（`_db` 只放库 + 说明；档一律 `_share`） |
| 建 `<family>\_db\<family>db` + `目录说明.md`；叶内只留 `目录说明.md` | 档内**非表格**件入库（随档留 `_share`） |
| 单库化（多家族库 → 1 库，core-6t 结构）与库内修库（entity / 结果表 / PHI 整改）；单库切换门同批改 | 先切库后补门（绕过门禁）；库内语义级判断代替人工 QC |
| 压缩档归档 `<family>\_share\<leaf>\`；档内表格解出入库；解包树校验后移 `{DEL}` | 改 `_diseases.csv` / `_index.csv` 的**语义**（只按既有格式登记事实） |
| 叶内非表格 raw 按单元压档上收 `_share\<leaf>\` | 删除原件（禁删；只移 `{DEL}`） |
| 原件 → `{DEL}\_by-function\<batch>\originals\<code>\<family>\<leaf>\` + `*-MOVED-*.tsv` |  |

## Phases

1. **P0 盘点** — 只读扫描目标叶 / 家族根：表格清单（xlsx/xls/csv）、字节、每 sheet 行列、sha256、名称版本簇、mtime 桶。
2. **P1 判定** — 逐项目定处理类型；三层去重预判；列出「需开表核对」清单（版本簇、可疑重复）。
3. **P2 构建（dry-run）** — 只写 `out/`，不动 `_DataBase`；先给用户看清单 / 抽样。
4. **P3 校验** — 行数守恒、键唯一、缺失盘点、sha256 100%、`PRAGMA integrity_check`、抽样查询；档内表另核「档名 + 成员」映射可回溯。
5. **P4 落盘** — 库落 `<family>\_db\<family>db`；压缩档移 `_share\<leaf>\`（原档不进 `_db`、不留叶）；解包树校验后移 `{DEL}`；原件移 `{DEL}\...\originals\<code>\<family>\<leaf>\` + 台账；叶 `目录说明.md` 改为「只留说明 + 档→表映射」；`_index.csv` note。
6. **P5 收口** — `cd D:\MyProjects\_Docs && python -B test/structure_check.py` 全门 PASS；批次报告 `<batch>-REPORT.md`。

## 门禁（verify_db / 单库化 / 目录说明 QC）

**verify_db 判级**：输出 `[P<级>][FAIL|WARN|INFO][D<号>] msg`，汇总行 `== 结果 == P0=.. P1=.. P2=..`，`exit 1` 仅当 `P0 > 0`。级别映射：D1/D2/D3/D5 → P0，D4/D6/D7 → P1，D8/D9 → P2；伦理进库（D19）→ P0；D20 表头一致性、D21 fact 层明文 PHI、D22 role 为新增门。D10–D18 属语义项（entity 键是否可用、结果表是否被拆、PHI 是否真脱敏），机器门判不了，必须人工过并留证据。

**目录说明 QC 段**：每库 `_db` 根 `目录说明.md` 固定含 `## QC`：日期 / 标准 / 结论 / 未过项 / `- PHI：` / 影响 / 下次检查日期 / 明细报告路径；`- PHI：` 单独成行，便于机器扫。

**单库化切换门**：多家族库并成 1 库（core-6t）前，四处必须同一批改——① RULES「一族一库」条款；② `structure_check.py` S25–S27；③ 本技能 build-db 契约；④ `verify_db.py` D1–D22 + core-6t 布局识别。四处不同批改就切库 = 绕过门禁。方案与 7 步见 [references/single-lab-db.md](references/single-lab-db.md)。

**建库门**：写 `entity` 前做键可用性预检——键重复率 >5%，或键值只是分级标签 / 特征名 / 组号而非个体号 → 拒绝建 entity 并报 P0，避免「先建错再修」。

## 解档 → 入库 → 档移 `_share` → 解包树移 `{DEL}` → 记档 → 表映射

压缩档是**数据来源**，不是库内对象：原档只留 `_share`，档内表格才入库，解包树不留在 `_DataBase`。

1. **解档** — 归档解到 `{DEL}\_by-function\<batch>\staging\_unpack\<leaf>\`（不就地解压、不解到 `_DataBase`）。
2. **入库** — 档内表格按与散表相同的三层去重入库；`doc.rel_path` = 档在 `_DataBase` 下的相对路径 + `/<成员>`（例 `PHT/_share/lmd_PHT.7z/PHT-data.xlsx`；叶档例 `MHE_AN/_share/thesis/ly_THESIS/morris copy.7z/<成员>`）；档内**非表格**件不入库。
3. **档移 `_share`** — 原档 → `<family>\_share\<leaf>\`；`ethics` / `thesis` 类按 D1 打平 `<CODE>__<档>` / `<slug>__<档>`（`_share\<类>\<文件>`，自 `_share` 起 ≤2 层）。
4. **解包树移 `{DEL}`** — 解包树逐件 sha256 与档内成员清单核对 100% 后，整树移 `{DEL}\_by-function\<batch>\unpack\`；不得在 `_DataBase` 任何层留解包副本。
5. **记档** — 台账分行分记：`kind=archive`（档 → `_share`）、`kind=table`（档内表 → `originals\<code>\<family>\_share\<档相对路径>\`）；跳过件（库内同 sha / 两档互重）单列 skip 清单；readme 记「档 → 表」映射与跳过原因。
6. **表映射** — 用 `doc.rel_path` 反查档名 + 成员；`_share` 根 `目录说明.md` 记档清单（子层 / 件数 / MiB），叶 readme 记未入库例外。

叶内非表格 raw（图片 / 文档 / 原始记录）按**单元**压档上收：`<PREFIX>__<leaf>__<unit>-raw-<YYYY-MM-DD>.tar.zst` → `_share\<leaf>\`（不整叶 mega 档）；逐件 sha256 校验后原件移 `{DEL}`，readme 记「raw → 档」。

## Bans

- 不得跳过去重直接拼；不得以 mtime 当新旧或去重依据（迁移刷新 mtime）。
- 不得覆盖 / 删除源文件；原件只移 `{DEL}` 并留 sha256 台账。
- 不得把压缩档原档入库；归档不进 `_db`、不留叶，一律 `<family>\_share\<leaf>\`（`ethics` / `thesis` 类打平 `<CODE>__<档>` / `<slug>__<档>`）。
- 不得就地解压：解包只到 `{DEL}` staging，校验后整树移 `{DEL}`，`_DataBase` 不留解包副本。
- 叶内不得留散表 / 压缩档：入库后叶内只 `目录说明.md`；未入库例外（PHI 花名册、模板、解析失败件）留叶并在 readme 写明原因，不另存副本。
- `_share` 层级 ≤2：`_share\<类>\<文件>`；一级只 `<leaf>/`、`ethics/`、`thesis/`、`目录说明.md`（无叶家族可 `_share\<family>/`，须登记例外）；`ethics` / `thesis` 内不得建子目录。
- 不得把 `_DataBase` 的件回流项目树（用户口径：不回流）。
- 未获当轮点名不得写 `_DataBase`（写盘总闸）；不确定即停、先问。
- 不得先切库、后补门：单库化 / 6t 结构切换的四处门禁须同批改（见「单库化切换门」）。
- 不得把 `ANALYZE` 生成的 `sqlite_stat1` 留在库内（`verify_db` D2 会判 schema 额外表）；确需统计信息时用完即 `DROP` 并 `VACUUM`。
- 不得为「每行都有唯一标识」硬塞 `person_id` / `entity`：无可靠个体键时宁可不建（置 NULL + 记理由）。
- 出库归档原件须两份异盘；库内 blob 保留的明文 PHI 外发前必须再脱敏（假名 ≠ 已脱敏）。
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
| D2 报「schema 额外表」 | 手跑 `ANALYZE` 生成 `sqlite_stat1` | `DROP TABLE sqlite_stat1` 后二次 `VACUUM` |
| `cannot modify doc because it is a view` | 6t 库里 `doc` / `sheet` 是只读兼容视图 | 按 `db_core._ingest_sheet` 语义直写 `src/item/val/person/person_key` |
| `UNIQUE constraint failed`（person_key 主键） | `(id_type, id_value)` 跨 project 全局唯一，按 project 作用域查 | 缓存建成全局 `_pk_cache[(kind, kn)]` |
| 仪器表被判出库、其中含 PHI 临床表 | 仪器签名收了 `#1..#8` 占位列 | 签名只取仪器专有列；去占位列后命中 123 张 / 误判 0 |
| 仪器表行数对账对不上 | blob 前有 30–88 行元数据，`nrow + 1` 不等于 TSV 行数 | 只按 sha256 对账，不按行数反推 |
| 空目录被当库重建 | 从未有过 sqlite 的占位说明 | 不建假库；占位说明移 `{DEL}`，不搬进家族 `_db` |

## Verification checklist

- [ ] 行数守恒：源行（去重后）= 合并行；差异有逐条理由
- [ ] 键唯一 / 缺失盘点有数（姓名、性别、年龄、部位…）
- [ ] 原件 sha256 全部核验通过，台账行数 = 移动件数
- [ ] 库：`PRAGMA integrity_check` ok；表数 / fact / entity 与报告一致；抽样查询能复现已知值
- [ ] 单库化迁移四验：`src` 与 `sheet` 1:1；blob SHA1 全等；每表 `(row_ix, item, num, text)` 多重集 0 差异；兼容视图计数与旧表一致
- [ ] 修库后 6 项自检：`integrity_check` ok、`Σdoc.n_sheets == COUNT(sheet)`、dup+subset 行数 = `COUNT(sheet_dup)`、五组孤儿 = 0、`dup_groups = 0`、`fact.entity_id` 键 100% 存在
- [ ] 库内无 `sqlite_stat1`、无伦理表（D19）；`verify_db --quiet` 的 exit / P0 / P1 / P2 记进 `目录说明.md` 的 QC 段
- [ ] 叶内只留 `目录说明.md`；未入库例外在 readme 固定段写明（可机器判定）
- [ ] 归档不在叶内：家族桶 depth≥2 无压缩档，压缩档只在 `_share`
- [ ] `_share` 层级 ≤2（`_share\<类>\<文件>`；`ethics` / `thesis` 打平 `<CODE>__<文件>` / `<slug>__<文件>`），无子目录
- [ ] 台账号对齐：`doc.rel_path` ↔ 台账逐条对齐，档内表带档名 + 成员；`_share` 根 `目录说明.md` 件数 / MiB 与实盘一致
- [ ] `目录说明.md` 追加段含口径、重算文件数 / 大小、库路径、台账指针
- [ ] `_index.csv` note 追加日期 + 落点，不留悬空 `→` 路径
- [ ] `structure_check.py` 全门 PASS
