# db5t 建库流水线（load-pipeline）

> 适用：从零建一个标准子库（`{RAW}\Family\<FAM>\<slug>\<slug>db`），或把一批源表规整进新库。
> 硬约束在 `{RULES}\db-build-contract.md`（契 1–10、律 1–5）；判据见 `{RULES}\db-gates.md` D93–D99（尚未机器化 / report-only，不在此复述判据文字）。
> 本文件只讲**怎么做**，不重述禁令。全部实测数字来自 2026-11-28 的 `{RAW}`（28 家族 / 80 子库 / 43,290 行）。

## 0 七条铁律

1. **契约先于数据**：`map.csv` + `qc_codes.tsv` + `schema.sql` 三份没齐，不建表、不导数据。
2. **空库由 `schema.sql` 生成**，不从现有库 `COPY`。抄来的库会连旧债一起抄进来（现状：79 个库有 15 个空 `path_*` 占位列，就是「先建表后补契约」的后果）。
3. **`dict` 是真源，不是产物**：目标列先有 dict 行，再 ALTER 建列。
4. **身份先于值**：先发 `family_uid`，再填任何业务列。
5. **一个格一来源**：每个值写 `src_id` + `src_row`，指不到就不许填。
6. **不确定就停**：六类停列情形见契 2 / 律 5，写 `qc(PENDING_REVIEW)` + `REVIEW-QUEUE.csv` + 当轮问人。
7. **收口即对账**：`Σ clin.merged_n = Σ src.rows`，不等不算完成。

## 1 阶段 0：立契约（不产库，只产三份文件）

### 1.1 `map.csv`（13 列固定）

列定义见 `{RULES}\db-build-contract.md` 契 1。文件名即 `map.csv`（目录名已含 slug）；开工落 `_work\`，收口后随库（见 `{RULES}\zone-database.md` §8）。写法要点：

- `src_header` 写**源文件里的原文**（可以是中文，这是唯一允许中文的位置）；`target_column` 写英文。
- 多行表头：`src_header_row` 写起始行，`src_column` 写拼接后的子列（`行1|行2`）。
- 数值列：`dtype` 只用 `REAL` / `INTEGER`；能算的列不许写 `TEXT`（现状 1,037 列把纯数字存成 TEXT）。
- 单位：`unit` 写外置代码，**不许写进列名**（现状 194 列名内嵌单位）。
- 枚举：`enum_values` 写英文（`M|F|U`）；中文映射写在 `transform`，例如 `enum(male:男/男性/M;female:女/女性/F;unknown:其它,U,-)`。
- `expect_rows` 是收口对账用，不许估——从源文件数出来。

### 1.2 `qc_codes.tsv`（家族级 `<family>\_work\`）

| 列 | 说明 |
|---|---|
| `code` | ASCII 大写，`[A-Z][A-Z0-9_]*` |
| `level` | P0 / P1 / P2 |
| `means` | 一句话判据 |
| `auto` | `clean` / `fill` / `manual` |
| `superseded_by` | 旧码归一目标（空=保留） |

初始词表 16 码（从现有 190 个 code 里归一得来）：

```
VALUE_NORMALIZED  P2  clean  值域归一（男→M）
VALUE_DIRTY       P2  clean  单元格含占位/公式/句（0、#VALUE!、见备注）
VALUE_CONFLICT    P1  manual 同人同变量两值不等（停列）
DATE_INVALID      P1  clean  日期不可解析（停列）
DATE_CONFLICT     P1  manual 两源日期不等（停列）
UNIT_CONVERTED    P2  clean  按声明系数换算（记系数）
UNIT_UNCERTAIN    P1  manual 单位不可换算（停列）
ENUM_UNMAPPED     P1  manual 枚举无英文对应（停列）
NAME_SEMANTIC     P1  manual 列名与值语义不符（停列）
PENDING_REVIEW    P1  manual 停列待审（与 REVIEW-QUEUE 互指）
SUPERSEDED        P2  fill   人工勘误：取最后修订版
MULTI_ROW_MERGED  P2  fill   同人多行合并（记 merged_n）
NO_SOURCE         P1  manual 有值无来源（停列）
SRC_EXCLUDED      P2  fill   源已排除（只存档）
HEADER_LOST       P2  clean  表头行丢失（列名不作列）
PHI_EXCLUDED      P2  clean  列含 PHI，移入 `_PHI` 后删列
```

旧码保留但按 `superseded_by` 归一（例：`GRADE_CODE_REMAP` → `VALUE_NORMALIZED`，`SOURCE_SNAPSHOT_ONLY` → `SRC_EXCLUDED`，`CROSSWALK_CONFLICT` → `VALUE_CONFLICT`）。

### 1.3 `schema.sql`

由 `{code_root}\tools\db-library\db5t\schema-v1.md`（41,289 B）反编译生成，**不由现有库 dump**。内容：

- `meta` / `src` / `person` / `qc` / `clin` 五张核心表；
- `clin` 的 11 个骨架列 + 15 个 `path_*`（`stage` 级 dict 行对应）；
- `_modules_<mod>` 注册表 + `<mod>_val` 长表（`(exam_uid, entity, feature, value, unit)`）；
- 索引：`clin(family_uid)`、`clin(period_month)`、`clin(src_id, src_row)`、`*_val(exam_uid)`。

### 1.4 dict 行（全局 `{RAW}\Family\dict.db`）

建库前先把目标列的 dict 行写进去（`scope='proj:<slug>'`），再建表。骨架列走 `scope='stage'`，一次登记全库共用（现状 24,189 个 proj 键里有 2,463 个是该上提的骨架键）。

## 2 阶段 1：建空库

```
# 计划中（CLI 为约定，脚本落地前不存在）
python -B tools/db-library/db5t/newdb.py --family <FAM> --slug <slug> \
  --schema <schema.sql> --map map.csv --period-unit singleton --dry-run
```

建出来的目录（契 10）：

```
{RAW}\Family\<FAM>\
├─ _PHI\<FAM>db          ← 已存在则复用，不重建（身份是家族级资产）
├─ <slug>\<slug>db       ← 新建，空表
└─ <slug>\map.csv        ← 契约随库走
```

`meta` 必填项：`schema_version`（`5t/1.1`）、`kind`（`project`）、`family`、`project`=slug、`subject_type`、`built_at`、`period_unit`、`period_unit_reason`、`clin_cols_n`、`outcome_status`。

空库自检：`gates.py <FAM>` 应只有「无数据」类提示，不许出现结构类 FAIL。

## 3 阶段 2：源登记

`src` 七列：`src_id, kind, status, rel_path, sha256, rows, note`。

- `kind` ∈ `curated` / `old_db` / `old_db_blob` / `original_zip_member` / `original_7z_member`（现状 526 行里 85% 是 `old_db_blob`，属历史债，新库不许再走 blob）。
- `status` ∈ `active` / `excluded`；`excluded` 必须写 `note` 说明为什么（表头丢失 / 列名即人名 / 非患者×变量表）。
- `sha256` 记源文件字节指纹；`rows` 记源记录数（收口对账用）。
- 源文件本体放 `__zip\<leaf>\`，不复制到子工程目录。

## 4 阶段 3：身份聚类

顺序：`id` 建人 → `id_number` 挂号 → 归一 `sex` / `birth_date`。

- `kind` 白名单：`inpatient` / `outpatient` / `mrn` / `imaging` / `pathology` / `sample` / `study` / `other`。
- 段位：`0xxxxx` 人（真身份）/ `8xxxxx` 动物 / `9xxxxx` 占位（label_only）。9 段可多人共用同一号码，不判冲突。
- 姓名只进 `id.name`，不参与判重（D41）；`id.name_pinyin` 可写，但不作键。
- `sex` 归一 `M` / `F` / `U`（现状 8 种写法混装、41,060 个 NULL；NULL 允许，混写不允许）；`birth_date` 只 ISO，允许 `YYYY-MM`。
- **PHI 边界**：子库零 PHI。`clin` / `qc` 里已有的 `姓名` / `电话` / `身份证` / `地址` 列，入库时进 `id` 后删列，记 `qc(PHI_EXCLUDED)`。

## 5 阶段 4：清洗（三级阶梯，不改语义）

### L0 结构对齐
列名转 ASCII snake_case；多行表头拼成 `行1|行2` 并记 `src_header_row`；数值矩阵/非患者×变量表排除（记 `SRC_EXCLUDED`）。

### L1 命名
按 `alias-map` + 列名单位后缀归一：`cr` / `crea` / `scr` → `creatinine`；`alt` / `gpt` → `alt`。名字对上但值形态不符 → 记 `NAME_SEMANTIC` 停列（现状 14 列此情形，如 `EC/ybc_EC_clin.tp` 是病理类型文本、`LC/qrx_LUNG_his.tnm` 是分期文本）。

### L2 单位与值域
- 单位三级来源：列名后缀 → dict `unit` → 组内双峰检测（两侧各 ≥15%、断层 ≥8 倍，且两模之比等于已知因子）。
- 换算必须声明：`unit-rules.tsv` 的系数（creatinine mg/dL×88.4、tbil mg/dL×17.1、hgb/alb/tp g/dL×10、ua mg/dL×59.48 …）。
- **不可换算的停列**：DDimer `mg/L DDU`（随试剂 1:2 上下浮动）、HE4 `pmol/L`。
- 值形态六条：仅英文（原文靠 `src_row` 回指）、数值化（能算的存 REAL/INTEGER）、单一域（numeric/text/date/enum）、截尾拆三列（`x` + `x_flag`(lt/gt) + `x_raw`）、单位外置、日期 ISO。
- 每条清洗必落 `qc`：`VALUE_NORMALIZED` / `UNIT_CONVERTED` / `DATE_INVALID` / `HEADER_LOST`。

## 6 阶段 5：按列组回填

八组顺序（前一组没清完不进下一组）：

1. 键与时点（`family_uid` / `observed_on` / `period_month` / `period_source` / `visit_kind` / `visit_no`）
2. 队列与分组（`cohort` / `group_v` / `subgroup`）
3. 人口学（`age` / `sex`；`sex` 以 `_PHI` 为准，子库不重复存 PHI）
4. 诊断与分期（`diagnosis` / `stage` / `grade` / `path_*`）
5. 治疗（手术/药物/放疗列）
6. 结局（`outcome_status` 可为 `pending`，此时该组留空）
7. 病理与 ihc
8. 派生与模块（`_modules_*` + `*_val`）

规则：

- 每组先 dry-run：输出「目标列 × 源列 × 命中行数 × 失败行数」，人工看过再 `--apply`。
- 每格写 `src_id` + `src_row`；拼行写 `merged_n`。
- 多时点：只有 `period_unit` ∈ `followup_6m` / `peri_op` 才允许多行；`singleton` 库一人一行，出现第二行即停列。
- 同人同变量两值不等 → 停列（契 7），不许先到者胜。

## 7 阶段 6：收口

```
python -B tools/db-library/db5t/fix_sha.py <FAM>     # 写库后必跑，否则 P0 镜像门
DB5T_ROOT={RAW}/Family DB5T_DICT={RAW}/Family/dict.db \
  python -B tools/db-library/db5t/gates.py <FAM>
```

收口三查：`Σ merged_n = Σ src.rows`（D96）、dict 覆盖（D95）、qc 码受控（D94）。全绿才算完，不许「先把 P2 放着」。

## 8 冲突处置

| 冲突类型 | 处置 | 台账 |
|---|---|---|
| 同人同变量两值不等 | 停列 + 问人 | `qc(PENDING_REVIEW)` + REVIEW-QUEUE 一行 |
| 两源日期不等 | 停列 + 问人 | 同上 |
| 单位不可换算 | 停列 + 问人 | `qc(UNIT_UNCERTAIN)` |
| 枚举无英文对应 | 停列 + 问人 | `qc(ENUM_UNMAPPED)` |
| 列名与值语义不符 | 停列 + 问人 | `qc(NAME_SEMANTIC)` |
| 时点不明 | 停列 + 问人 | `qc(PENDING_REVIEW)` |

`REVIEW-QUEUE.csv` 列：`review_id, family, slug, uid, column, src_a_src_id, src_a_row, src_a_value, src_b_src_id, src_b_row, src_b_value, rule, raised_at, resolution`。

## 9 试点（验收用）

按本轮决策，试点两处的操作口径是**直接重建现库 + 开工前备份**（不用影子库）。此条待另点名后执行：本批未备份、未重建、未改现行家族 `.db`。

- **B：从零建 `MM/zy_MM`**（最小：185 行 / 47 列 / 1 子库 / `_modules_lesion` 370 exam + 5,832 val）。跑通全流程，验收「空库 → 契约 → 回填 → 全绿」。
- **A：重放 `EC/ybc_EC_clin`**（226 列 / 1,064 行）。与现库逐格 diff，允许差异只有两处：D92 已登记 1,291 格脏值、D93 已登记 71 个越界值。未登记差异必须为 0。

多时点白名单写死：仅 `SCH/js_SCH`、`PAH/lxf_PAH`（`period_unit=followup_6m`）允许多行随访；`zjl_RDL` 数据不动，只加 meta 例外位（只报数）。其它库不得自行写 `multi_visit_exempt=1`。

## 10 命令速查

```
# 门禁（必须传家族名，传路径 rc=2）
DB5T_ROOT={RAW}/Family python -B tools/db-library/db5t/gates.py <FAM>

# sha 回填
python -B tools/db-library/db5t/fix_sha.py <FAM|all>

# 全库概览
python -B {doc_root}/test/db_overview.py --all --meta-only

# 结构自检（37 项）
python -B {doc_root}/test/structure_check.py

# 契约：SCHEMA 副本
cp tools/db-library/db5t/schema-v1.md <批次目录>/SCHEMA-v1.md

# 代码清单（须 git add 之后）
python -B tools/sync/gen_code_manifest.py
```

## 11 踩坑（实测，别重犯）

| 坑 | 症状 | 正解 |
|---|---|---|
| 以「p50 比健康参考区间」判单位 | 59 个 `UNIT_MIXED` 全假阳性（透析病人肌酐 p50=738 μmol/L） | 用组内双峰 + 已知因子双条件；超出健康区间 ≠ 单位错 |
| 单侧区间判单位 | 任何缩小因子都能「落回」 | 单位嫌疑限双侧区间 + ≥20% 且 ≥3 值 |
| 名字对上就用 | `EC/ybc_EC_clin.tp` 被当总蛋白，实为病理类型文本 | 先看值形态（0% 数值 → 停） |
| `typeof` 四类判混合 | 误报 32 列（`INTEGER`+`REAL` 合规） | 按域判 + 排除 NULL |
| openpyxl 读数是字符串 | `TypeError: can't multiply sequence by non-int` | 算术前 `float(str(x).strip())` |
| Windows glob 反斜杠 | `p.split('/')[-3]` 得到 `D:` / `MyProjects` | 先 `p.replace('\\','/')` |
| 忘跑 `fix_sha` | P0 镜像门恒红 | 每次写库后立刻跑 |
| `gates.py` 传路径 | rc=2（不是数据错） | 只传家族名 |
| 一律 `TEXT` 存值 | 1,037 列数值存成文本 | 按值域定 dtype，能算的 REAL/INTEGER |
| 空库抄现有库 | 79 库的 15 个空 `path_*` 占位列 | 由 `schema.sql` 生成 |
| `_thesis` 新建目录 | 勿再新建 | 论文目标落点 `__zip\thesis\<slug>\`；实体改挂待另点名 |

