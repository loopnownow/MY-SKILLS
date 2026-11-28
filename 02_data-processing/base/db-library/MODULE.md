---
name: "db-library"
domain: "02_data-processing"
trigger: ["散表", "合并", "去重", "_PHI", "SQLite", "入库", "台账", "REVOKED", "压缩档", "__zip", "解档", "家族库", "叶说明", "单库", "6t", "修库", "verify_db"]
inputs: ["loose_tables", "family_tree", "share_archives"]
outputs: ["merged_workbook", "family_db", "move_ledger", "archive_map"]
quality_control: "三层去重; sha256 台账; 行数守恒; 叶内只留说明; __zip 层级 ≤2; structure_check 全门 PASS; verify_db P0=0"
owner: "02_data-processing/base/db-library/MODULE.md"
---

trigger is documentation only; not independently discoverable.

# Loose tables → merged workbook / family SQLite library

Contract only for db-library: scope, phases, bans, verification, and pointers. Recipes live in
[references/merge-tables.md](references/merge-tables.md)（散表归并）、[references/build-db.md](references/build-db.md)（建库）、
[references/single-lab-db.md](references/single-lab-db.md)（单库化与 core-6t）、[references/db-fix.md](references/db-fix.md)（库内修库）、[references/load-pipeline.md](references/load-pipeline.md)（契约驱动建库）。
Path / ledger / gate rules live in `{RULES}\zone-database.md`（「家族桶落点」「家族库 `_PHI`」「散表归并与表格入库」「台账落点」）；build contract in `{RULES}\db-build-contract.md` — do not restate them here.

## Scope

| In | Out |
|---|---|
| 家族根 / 叶根散表盘点（文件数、行、列、sha256、版本簇） | 临床底表清洗标准（表头规范、缺失值策略）→ `clean-data` |
| 三类型判定：同构纵并 / 一簿多 sheet / 单件只改名 | 统计分析、建模、图 → `stats-analysis` / `model-evaluation` / `plot-figures` |
| 去重三层（文件 sha → 整表重复/子集 → 行/实体） | 影像 DICOM / NIfTI 处理 → `preprocess-imaging` |
| 合并成 `<项目名>_merged_YYYYMMDD.xlsx`（默认入库中间件 / 点名交付，不落叶根） | 压缩档原档入库（`_PHI` 放库 + 说明 + 可重建预览；档一律 `__zip`） |
| 建 `<family>\_PHI\<family>db` + `目录说明.md`；叶内只留 `目录说明.md` | 档内**非表格**件入库（随档留 `__zip`） |
| 单库化（多家族库 → 1 库，core-6t 结构）与库内修库（entity / 结果表 / PHI 整改）；单库切换门同批改 | 先切库后补门（绕过门禁）；库内语义级判断代替人工 QC |
| 压缩档归档 `<family>\__zip\<leaf>\`；档内表格解出入库；解包树校验后移 `{DEL}` | 改 `_diseases.csv` / `_index.csv` 的**语义**（只按既有格式登记事实） |
| 叶内非表格 raw 按单元压档上收 `__zip\<leaf>\` | 删除原件（禁删；只移 `{DEL}`） |
| 原件 → `{DEL}\_by-function\<batch>\originals\<code>\<family>\<leaf>\` + `*-MOVED-*.tsv` |  |

## Phases

1. **P0 盘点** — 只读扫描目标叶 / 家族根：表格清单（xlsx/xls/csv）、字节、每 sheet 行列、sha256、名称版本簇、mtime 桶。
2. **P1 判定** — 逐项目定处理类型；三层去重预判；列出「需开表核对」清单（版本簇、可疑重复）。
3. **P2 构建（dry-run）** — 只写 `out/`，不动 `_DataBase`；先给用户看清单 / 抽样。
4. **P3 校验** — 行数守恒、键唯一、缺失盘点、sha256 100%、`PRAGMA integrity_check`、抽样查询；档内表另核「档名 + 成员」映射可回溯。
5. **P4 落盘** — 库落 `<family>\_PHI\<family>db`；压缩档移 `__zip\<leaf>\`（原档不进 `_PHI`、不留叶）；解包树校验后移 `{DEL}`；原件移 `{DEL}\...\originals\<code>\<family>\<leaf>\` + 台账；叶 `目录说明.md` 改为「只留说明 + 档→表映射」；`_index.csv` note。
6. **P5 收口** — `cd D:\MyProjects\_Docs && python -B test/structure_check.py` 全门 PASS；批次报告 `<batch>-REPORT.md`。

## 契约驱动建库（与 P0–P5 并列）

与上面「P0–P5 批量合并」并列，不合并：那是一批表进一个库，这是从零建标准库。硬约束只在 `{RULES}\db-build-contract.md`，判据见 `{RULES}\db-gates.md` D93–D99（尚未机器化 / report-only）。

| 阶段 | 产物 | 卡口 |
|---|---|---|
| 0 契约 | `map.csv`（13 列）、`qc_codes.tsv`、`schema.sql` | 三份齐了才许建表 |
| 1 空库 | `newdb.py` 由 `schema.sql` 生成，不抄现有库 | 空库 `gates` 只允许「无数据」类提示 |
| 2 源登记 | `src` 一行一源 + sha256 | Σ`src.rows` 与源文件行数一致 |
| 3 身份 | `id` / `id_number`，姓名只进 `id.name` | 9 段占位不判冲突 |
| 4 清洗 | 列名归一、表头拼接、单位外置、枚举英文化 | 全部进 `map.csv`，不改语义 |
| 5 回填 | 按列组八组顺序，每格写 `src_id` + `src_row` | dry-run 计数 → 审 → apply |
| 6 收口 | `fix_sha` + `gates` 全绿 | D96 计数守恒（尚未机器化） |

详细步骤见 `references/load-pipeline.md`。目录契约见 `{RULES}\db-build-contract.md` 契 10。

## 门禁（verify_db / 单库化 / 目录说明 QC）

**verify_db 判级**：输出 `[P<级>][FAIL|WARN|INFO][D<号>] msg`，汇总行 `== 结果 == P0=.. P1=.. P2=..`，`exit 1` 仅当 `P0 > 0`。级别映射：D1/D2/D3/D5 → P0，D4/D6/D7 → P1，D8/D9 → P2；伦理进库（D19）→ P0；D20 表头一致性、D21 fact 层明文 PHI、D22 role 为新增门。D10–D18 属语义项（entity 键是否可用、结果表是否被拆、PHI 是否真脱敏），机器门判不了，必须人工过并留证据。

**目录说明 QC 段**：每库 `_PHI` 根 `目录说明.md` 固定含 `## QC`：日期 / 标准 / 结论 / 未过项 / `- PHI：` / 影响 / 下次检查日期 / 明细报告路径；`- PHI：` 单独成行，便于机器扫。

**单库化切换门**：多家族库并成 1 库（core-6t）前，四处必须同一批改——① RULES「一族一库」条款；② `structure_check.py` S25–S27；③ 本技能 build-db 契约；④ `verify_db.py` D1–D22 + core-6t 布局识别。四处不同批改就切库 = 绕过门禁。方案与 7 步见 [references/single-lab-db.md](references/single-lab-db.md)。

**建库门**：写 `entity` 前做键可用性预检——键重复率 >5%，或键值只是分级标签 / 特征名 / 组号而非个体号 → 拒绝建 entity 并报 P0，避免「先建错再修」。

## 解档 → 入库 → 档移 `__zip` → 解包树移 `{DEL}` → 记档 → 表映射

压缩档是**数据来源**，不是库内对象：原档只留 `__zip`，档内表格才入库，解包树不留在 `_DataBase`。

1. **解档** — 归档解到 `{DEL}\_by-function\<batch>\staging\_unpack\<leaf>\`（不就地解压、不解到 `_DataBase`）。
2. **入库** — 档内表格按与散表相同的三层去重入库；`doc.rel_path` = 档在 `_DataBase` 下的相对路径 + `/<成员>`（例 `PHT/__zip/lmd_PHT.7z/PHT-data.xlsx`；论文档目标落点 `__zip/thesis/<slug>/...`（现行盘面在改挂前仍可能见 `_thesis`，实体未搬））；档内**非表格**件不入库。
3. **档移 `__zip`** — 原档 → `<family>\__zip\<leaf>\`（自 `__zip` 起普通叶 ≤2 层）；学位论文 / 博士后 / 汇报稿原档目标落点 `<family>\__zip\thesis\<slug>\<文件>`（学位支为层级例外；勿再新建 `_thesis`；实体改挂待另点名）；伦理材料不进 `_DataBase`（见禁忌）。
4. **解包树移 `{DEL}`** — 解包树逐件 sha256 与档内成员清单核对 100% 后，整树移 `{DEL}\_by-function\<batch>\unpack\`；不得在 `_DataBase` 任何层留解包副本。
5. **记档** — 台账分行分记：`kind=archive`（档 → `__zip`）、`kind=table`（档内表 → `originals\<code>\<family>\__zip\<档相对路径>\`）；跳过件（库内同 sha / 两档互重）单列 skip 清单；readme 记「档 → 表」映射与跳过原因。
6. **表映射** — 用 `doc.rel_path` 反查档名 + 成员；`__zip` 根 `目录说明.md` 记档清单（子层 / 件数 / MiB），叶 readme 记未入库例外。

叶内非表格 raw（图片 / 文档 / 原始记录）按**单元**压档上收：`<PREFIX>__<leaf>__<unit>-raw-<YYYY-MM-DD>.tar.zst` → `__zip\<leaf>\`（不整叶 mega 档）；逐件 sha256 校验后原件移 `{DEL}`，readme 记「raw → 档」。

## 5t 口径下的 skipped、归档退役与内容去重

下列做法按现行 db5t 书写（家族五表 / 子库 `clin` / `_modules_<mod>` / `qc` 等，空席不垫）。不得用精简登记册或 blob 库骨架替换现行五表；冻结旧库 core-6t 只读对账，不按旧骨架新建。

- **`skipped` 只用于体积闸或空表**：入库状态（5t 记在 `src` 或入库台账；冻结旧库若仍见 `doc.status` 同此执行）标 `skipped`，仅当该表因体积闸（例如 >2 MiB）或空表不入 blob，且必须在 note 写明判据与回溯口径。不得当作「暂不处理」的停放位（与 `{RULES}\skills.md` §6：skip 不是绕过）。
- **可追溯**：原件进归档后，路径不一定还能直接打开；要能落到「哪只档 + 档内哪个成员」。用归档旁路清单（`.files.txt`）的成员名与 `src.rel_path`（旧库兼容视图则对 `doc.rel_path`）的 basename 匹配率衡量。归档校验三态：成员逐字节与记录的 sha256 相等 / 大档不解码 / 同名歧义未指派则留空。成员名按「全名 → 后缀 → 唯一 basename」三级解析；同名多成员必判歧义并留空，不可猜。
- **归档退役顺序固定**：先标依赖 → 再搬字节 → 同批改台账。反过来会留 dangling 指针，且「sha256 ok」会变成假绿。搬档前先按 archive 分组计数谁还指着它；有引用就先改状态，再搬。退役不是删除：整档进 `{DEL}`，保相对路径 + sha256 台账；内容指纹仍可证明「曾是什么」，只是字节不在 `__zip`。
- **`archive-moved` 是状态不是新路径**：不要把 archive 字段改写成 `{DEL}` 绝对路径（违反「禁活指针指 `{DEL}`」）。体积账要写进说明与索引 note，否则下次巡检会把「缺档」当事故。退役前确认该档没有被库内 blob 依赖；清单文件必须跟档一起搬。同一批若既改索引又搬档，先把索引原件备份到批次夹并记 sha256。
- **L2 内容去重**：文件级 sha256 只能抓同一字节，抓不到「同一张表存了两个文件」。内容级必须比表头归一 + 行哈希多重集。去重标记的空串按空值处理；`status='new'` 且尚未入库，不等于重复，也不等于已入库。同名不同 sha 可能是不同版本（保留），只有整表全等或真子集才记边。先用便宜签名（维度，不读单元格）分组，只在「签名相同且 sha 不同」的组里做完整 L2。名字信号（`copy/`、`old/`、副本后缀）只作候选，不是结论。`--apply` 只写去重边 + 说明，台账只追加不覆盖。去重是否做完，看指纹分组与重算的表级签名，不看库内自述字段。
- **改库后必须重生成说明与预览**，否则页面数字是旧账。预览页口径与 `{RULES}\zone-database.md`「家族库 `_PHI`」一致。删行后必须 `VACUUM`，否则空闲页让库虚涨。空库不建假库：记一句后把空壳移 `{DEL}`，说明里留指针。
- schema 门若是子集判据：必须先加允许的 schema 集合再删表，顺序反了整批红。改 schema 必须与门同批改。

## Bans

- 不得跳过去重直接拼；不得以 mtime 当新旧或去重依据（迁移刷新 mtime）。
- 不得覆盖 / 删除源文件；原件只移 `{DEL}` 并留 sha256 台账。
- 不得把压缩档原档入库；归档不进 `_PHI`、不留叶，一律 `<family>\__zip\<leaf>\`。
- 不得就地解压：解包只到 `{DEL}` staging，校验后整树移 `{DEL}`，`_DataBase` 不留解包副本。
- 叶内不得留散表 / 压缩档：入库后叶内只 `目录说明.md`；未入库例外（PHI 花名册、模板、解析失败件）留叶并在 readme 写明原因，不另存副本。
- `__zip` 普通叶层级 ≤2：`__zip\<leaf>\<文件>`；一级只 `<leaf>/` 与 `目录说明.md`（无叶家族可 `__zip\<family>/`，须登记例外）。学位支例外为 `__zip\thesis\<slug>\<文件>`；勿再新建 `_thesis`。伦理材料不落 `_DataBase`。
- 不得把 `_DataBase` 的件回流项目树（用户口径：不回流）。
- 未获当轮点名不得写 `_DataBase`（写盘总闸）；不确定即停、先问。
- 不得先切库、后补门：单库化 / 6t 结构切换的四处门禁须同批改（见「单库化切换门」）。
- 不得把 `ANALYZE` 生成的 `sqlite_stat1` 留在库内（`verify_db` D2 会判 schema 额外表）；确需统计信息时用完即 `DROP` 并 `VACUUM`。
- 不得为「每行都有唯一标识」硬塞 `person_id` / `entity`：无可靠个体键时宁可不建（置 NULL + 记理由）。
- 出库归档原件须两份异盘；库内 blob 保留的明文 PHI 外发前必须再脱敏（假名 ≠ 已脱敏）。
- 手工发现「台账 dst 不存在」时：先取证（回收站 → `E:\Aitor` 冻结快照 → 全盘落点），问过主人再动；确认清除才写 `REVOKED-*.tsv`，不得静默恢复或删除。
- 契约未齐不得建表、dict 无行不得 ALTER：见 `{RULES}\db-build-contract.md` 契 1、律 4。
- 中文映射与换算系数不进 `dict` / `qc`：见 `{RULES}\db-build-contract.md` 律 1。

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
| 空目录被当库重建 | 从未有过 sqlite 的占位说明 | 不建假库；占位说明移 `{DEL}`，不搬进家族 `_PHI` |

## Verification checklist

- [ ] 行数守恒：源行（去重后）= 合并行；差异有逐条理由
- [ ] 键唯一 / 缺失盘点有数（姓名、性别、年龄、部位…）
- [ ] 原件 sha256 全部核验通过，台账行数 = 移动件数
- [ ] 库：`PRAGMA integrity_check` ok；表数 / fact / entity 与报告一致；抽样查询能复现已知值
- [ ] 单库化迁移四验：`src` 与 `sheet` 1:1；blob SHA1 全等；每表 `(row_ix, item, num, text)` 多重集 0 差异；兼容视图计数与旧表一致
- [ ] 修库后 6 项自检：`integrity_check` ok、`Σdoc.n_sheets == COUNT(sheet)`、dup+subset 行数 = `COUNT(sheet_dup)`、五组孤儿 = 0、`dup_groups = 0`、`fact.entity_id` 键 100% 存在
- [ ] 库内无 `sqlite_stat1`、无伦理表（D19）；`verify_db --quiet` 的 exit / P0 / P1 / P2 记进 `目录说明.md` 的 QC 段
- [ ] 叶内只留 `目录说明.md`；未入库例外在 readme 固定段写明（可机器判定）
- [ ] 归档不在叶内：家族桶 depth≥2 无压缩档，压缩档只在 `__zip`
- [ ] `__zip` 普通叶层级 ≤2（`__zip\<leaf>\<文件>`）；学位支允许 `__zip\thesis\<slug>\<文件>`；一级无 `ethics` / `raw` 子夹，勿再新建 `_thesis`
- [ ] 台账号对齐：`doc.rel_path` ↔ 台账逐条对齐，档内表带档名 + 成员；`__zip` 根 `目录说明.md` 件数 / MiB 与实盘一致
- [ ] `目录说明.md` 追加段含口径、重算文件数 / 大小、库路径、台账指针
- [ ] `_index.csv` note 追加日期 + 落点，不留悬空 `→` 路径
- [ ] `structure_check.py` 全门 PASS

