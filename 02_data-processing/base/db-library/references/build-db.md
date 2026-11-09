# 家族库 SOP（build-db）

适用：把一个 / 多个短码的表格数据收进家族 SQLite 库。**位置 `<family>\_db\<family>db`、一族一库、原件进 `{DEL}`** 是 RULES 契约（`workspace-layout.md`「家族库 `_db`」），本文件只讲 schema / 算法 / QA。

## 1 硬约束

- 只收表格（xlsx / xls / csv）；压缩档（`*.tar.zst` / `7z` / `zip`）**不入库、不移动**，原地留叶。
- 值保真即可：不存公式 / 样式 / 列宽 / 合并单元格；原貌靠 `{DEL}` 原件回溯。
- 库与 `目录说明.md` 同目录；`_db` 是 `_` 前缀桶，不参与 S23，但改完仍跑 `structure_check.py` 24/24。
- 同家族多短码共用一个库；不要按短码拆库或拆子目录。

## 2 Schema（与现役 `build_code_db.py` 一致，逐字）

```sql
CREATE TABLE meta(k TEXT PRIMARY KEY, v TEXT);
CREATE TABLE project(id INTEGER PRIMARY KEY, family TEXT, slug TEXT, leaf TEXT, short_code TEXT);
CREATE TABLE doc(id INTEGER PRIMARY KEY, project_id INTEGER, rel_path TEXT, size INTEGER,
                 sha256 TEXT, mtime TEXT, n_sheets INTEGER, status TEXT, dup_of INTEGER);
CREATE TABLE sheet(id INTEGER PRIMARY KEY, doc_id INTEGER, name TEXT, nrow INTEGER, ncol INTEGER,
                   header TEXT, blob BLOB, is_wide INTEGER, status TEXT, dup_of INTEGER);
CREATE TABLE fact(id INTEGER PRIMARY KEY, sheet_id INTEGER, entity_id INTEGER, row_ix INTEGER,
                  item TEXT, value_num REAL, value_text TEXT);
CREATE TABLE entity(id INTEGER PRIMARY KEY, project_id INTEGER, key_kind TEXT, key_norm TEXT,
                    key_raw TEXT);
CREATE TABLE sheet_dup(id INTEGER PRIMARY KEY, sheet_id INTEGER, dup_sheet_id INTEGER,
                       reason TEXT, kept_bytes INTEGER);
CREATE INDEX ix_fact_sheet ON fact(sheet_id);
CREATE INDEX ix_fact_item ON fact(item, value_num);
CREATE INDEX ix_entity ON entity(project_id, key_norm);
```

- `sheet.blob` = 整表 `zlib` 压缩的 TSV（含表头）；宽表也存，保证「有多少数据可查」。
- `sheet.status`：`ingested` / `dup` / `subset`；`sheet_dup.reason` 记重复或子集、`kept_bytes` 记省下字节。
- `doc.rel_path` 保留 叶 slug 前缀（如 `MHE/ly_RI/IR-14-9-29.xlsx` 形式的相对 `_DataBase` 路径），便于回溯原文。

## 3 去重三层

1. **L1 文件级**：`sha256(file)` 相同 → `doc.status=dup`，不再解析（本轮 ly 内 0 组）。
2. **L2 整表级**：签名 = `(表头规范化串, 行哈希集合)`。集合全等 → 重复表（`sheet_dup.reason=dup`）；真子集 → `subset`。重复 / 子集表**不存 blob**，只记边。
3. **L3 行 / 实体级**：仅当表头可识别且 `ncol ≤ 40` 才展开 fact；entity 键用白名单：

```python
IDCOL = re.compile(r"^(医技号|样本编号|样本号|编号|case\s*no\.?|mid|谱图编号|patient(?:_?id)?|id)$", re.I)
```

- 未命中白名单的表只存 blob（仍可整表查，只是不做行级检索）。
- 跨项目 / 跨叶实体映射**只人工建**，不自动 join；短码是归属人，不是患者主索引。

## 4 读表细节（踩过的坑）

- `.xlsx` → `openpyxl` read_only；`.xls` → `xlrd`；`.csv` → `utf-8-sig` 再退 `gbk`。
- 伪装 `.xls` 的 TSV（几十字节，`xlrd` 抛 `XLRDError`）→ 按文本 / tab 回退解析，记为表。
- GBK 编码 `.XLS`（如 2011 汇总）→ 显式编码回退。
- 文件名含 U+00A0 → `norm()` 归一化后再匹配（否则整份文件漏读）。
- 宽表判定：表头单元格数字占比 > 0.6（谱图 / 积分矩阵）→ `is_wide=1`，只存 blob，不展开 fact。
- 全空表 / 单行说明表：照存 blob，`status=ingested`。

## 5 构建命令（草案接口，CODES 提炼后生效）

```bash
python tools/db-library/build_code_db.py --family MHE --code ly            # dry：只建 out/，不动盘
python tools/db-library/build_code_db.py --family MHE --code ly --move     # + 移原件到 {DEL}、写台账
python tools/db-library/build_code_db.py --family MHE --code ly --from-originals  # 从 {DEL}\originals 重建
python tools/db-library/verify_db.py --db "D:/MyProjects/_DataBase/MHE/_db/MHEdb"
```

现役脚本（本轮实例）：`.Del\_by-function\2026-11-db-sqlite\build_code_db.py`（`FAMILY` / `CODE` 常量写死 `MHE` / `ly`，`--from-originals` 从 `originals\ly\` 重建）。搬进 MY-CODES 时：常量改 `argparse`，`TAB` 扩展名与 `IDCOL` 提到模块级常量。

## 6 QA（全部过才报完成）

- [ ] 文件 / 表计数：`doc`、`sheet`（ingested / dup / subset）、`sheet_dup` 与报告一致
- [ ] `PRAGMA integrity_check` = ok；`PRAGMA journal_mode` 记录在 meta
- [ ] fact / entity / blob 字节数与报告一致；entity 键分布可解释（医技号 41,979 / 样本编号 1,060 / …）
- [ ] 行数守恒：入库存的表，`sheet.nrow` 之和 - 去重边 = 源表行数之和
- [ ] 抽样查询能复现已知值（例：`001643` → 17 条部位记录；SCH 部位 Top3 = 头颅 19,320 / 腰椎 5,149 / 上腹部 MRI 4,264）
- [ ] 原件 sha256 台账 100%；原件目录在 `{DEL}\_by-function\<batch>\originals\<family>\`
- [ ] `_db\目录说明.md`：口径 / 表结构 / 查询示例 / 重建 / 限制
- [ ] 相关叶 / 家族 `目录说明.md` 追加「表格数据入库」段；`_index.csv` note 追加
- [ ] `structure_check.py` 24/24

## 7 查询示例

```sql
-- 某检查号的全部部位
SELECT s.name, f.value_text FROM fact f JOIN sheet s ON s.id=f.sheet_id
WHERE f.item='部位' AND f.entity_id IN
      (SELECT id FROM entity WHERE key_kind='医技号' AND key_raw='001643');

-- 项目内样本数
SELECT p.slug, COUNT(*) FROM entity e JOIN project p ON p.id=e.project_id GROUP BY p.slug;

-- 表级总览
SELECT status, COUNT(*) FROM sheet GROUP BY status;
```

## 8 限制（写进 `目录说明.md`）

- 不保公式 / 样式 / 列宽；宽表只能整表取 blob。
- entity 仅白名单表头 + `ncol ≤ 40` 的表；未命中表的行级检索不可用。
- PHI 留本地库内，不外发；库不设加密（按本机规则）。
- 同名表可能来自不同文件（`sheet_dup` 有边）；溯源看 `doc.rel_path`。
