# 单库化与 core-6t 结构（single-lab-db）

适用：家族库从「一族一库」并成 1 个实验室库（core-6t）。前置门（四处同批改 + owner 点头）见 [MODULE.md](../MODULE.md)「单库化切换门」；本文件只讲结构、判据与实施。

## 1 决策与基线

- 21 个家族库 schema 完全一致，只是 21 次分批入库的产物 → 可以并，且应该并成 1 库。
- 实测基线（只读 `COUNT(*)`）：21 库 / 60 project / 342 doc / 1257 sheet / fact 4,837,262 / entity 53,099 / blob 103.4 MiB，盘上 528 MiB。
- 去重已做过一轮：145 张（65,830 行）已标 `dup` / `subset`，省 blob 264 MiB——不要重复做。
- 两方案：A 保留现有多库作入库层，另建分析库（改动小、双份盘）；B 直接并 1 库（须四处门禁同批改 + owner 点头）。按 §6 实施。

## 2 core-6t 结构

7 张实表：

| 表 | 内容 |
|---|---|
| `meta` | 键值：口径、`rule`、leaf 实盘位置、external 出库内账 |
| `project` | project / family / slug / leaf / short_code |
| `src` | 来源（doc 或 sheet 级）：`kind` 四类、`header` 归一表头、`role`（如 `merged`） |
| `item` | 列词典：标准列名、单位、`alias_of` |
| `val` | 值：主键 `(src_id, row_ix, item_id)`，`WITHOUT ROWID`；`num` / `text` 双列 |
| `person` | 个体（属性组合） |
| `person_key` | 个体键：主键 `(id_type, id_value)`（全局唯一）+ `PRIO` |

5 个只读兼容视图（列名与旧 schema 一致）：`doc` / `sheet` / `sheet_dup` / `entity` / `fact`。视图只读——按旧 `doc` / `sheet` 写会报 `cannot modify doc because it is a view`，写入须直写实表。

## 3 身份键：PRIO 与认领

PRIO（`person_key`，数字越小越强）：全院号 10 > 影像号 20 > 门诊号 30 > 住院号 40 > 病理号 50 > 医技号 60 > Patient_ID 65 > ID 70 > 样本编号 80 > 编号 85。

认领 5 级：

| 级 | 键 | 实测 |
|---|---|---|
| 1 | 全院号 | 4 表 / 602 行 |
| 2 | 影像号 | 12 表 / 14,130 行（全在 EC） |
| 3 | 医技号 / 门诊号 / 住院号 / 病理号 | 按 PRIO 依次 |
| 4 | 姓名 + 性别 + 年龄（±1） | 仅候选确认；自动建键须属性同时相等 |
| 5 | 姓名 单独 | 禁止做键（同名无法排除） |

- 同 `id_type + id_value` 但姓名 / 性别冲突 → 不覆盖，写 `conflicts.tsv` 人工裁决。
- `val.person_id` 必须允许 NULL：1063 张有表头的表里，姓名 + 性别 + 年龄三列齐全的只有约 50 张。
- 编号类各是独立 `id_type`，不互相合并。

## 4 分流与覆盖序

`src.kind` 四类：`clinical` / `derived` / `instrument` / `public`；判不出为 `unmapped`（不删、不改名）。

覆盖序（同名冲突时谁的值进 `val`）：curated（项目工程）> `_his`（HIS 导出）> 原始工作单（`SheetN`）> `derived`（结果表不覆盖原始值）。

- `_his` 是**来源**不是旧版：13 项目 / 212 表 / 116,513 行，抽样 5 组与 curated 行集交集 = 0；按「只留最新」删会丢互补数据。
- `SheetN` 274 张（21.8%）：按内容重命名，判不出进 `_unmapped`。
- 仪器原始导出 2,334,641 行（48.3%）+ 公开数据集 334,110 行（6.9%）= 55.2% 的 fact 行不该进窄表。
- 宽表 / 仪器 / 结果表：`ncol > 80` 或 `kind ≠ clinical` → 不参与拼接，只留 blob（实测宽表 173 张）。

## 5 拼接四档

1. 表头归一后集合相同 → 直接 union（534 张 / 132 组）。
2. Jaccard ≥ 0.8 且同短码可映射 → union（587 对）。
3. Jaccard 0.6–0.8 → 只出候选（841 对），不自动拼。
4. 跨短码 → 禁止自动拼。

产物：`<leaf>_<主题>_merged`；`src.header` 记归一后表头；`src.role='merged'`；来源用多行 `src` + 一条 union 视图，不新存一份宽 blob。

## 6 实施 7 步

1. **冻结** 21 库（只读 + 备份 sha256）。
2. **建库** 按 §2 建空库。
3. **重灌** 按 §4 分流；`instrument` / `public` 只登记 `src`（blob 或出库），不进 `val`。
4. **认人** 按 §3 填 `person` + `person_key`；缓存建全局 `_pk_cache[(kind, kn)]`，不按 project 作用域查。
5. **拼接** 按 §5 四档。
6. **门禁** 四验（§7）+ `verify_db`。
7. **切换** 旧库转归档；验收断言写死可复算值：SCH 部位 Top3 = 头颅 19,320 / 腰椎 5,149 / 上腹部 MRI 4,264；`001643` → 17 条。

## 7 迁移等价性四验

- `src` 与 `sheet` 1:1（21/21 OK）。
- 每张表 blob SHA1 全等。
- 每表 `(row_ix, item, num, text)` 多重集 0 差异。
- 兼容视图计数与旧表一致；`D2` 增加 core-6t 布局识别。

## 8 已知坑

- entity 孤儿 44,897 条（SCH 41,979 + SCC 2,918）：迁移时按新键重建，不要原样搬；删前整表归档 `tsv.zst`。
- 表头只用 blob 首行，`sheet.header` 不可靠（不一致 228/344）；行哈希用 blake2b 逐行。
- `ANALYZE` 生成的 `sqlite_stat1` 会被 `D2` 判为 schema 额外表。
- 修库（entity 重建 / 结果表降级 / PHI）见 [db-fix.md](db-fix.md)。
