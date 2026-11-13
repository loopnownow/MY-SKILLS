# 库内修库（db-fix）

适用：已入库的家族库做缺陷整改——entity 键不可用、结果表被拆、PHI 明文、整表该出库。铁律与修法来自一次 21 库整改批次；单库化按 [single-lab-db.md](single-lab-db.md)。

## 1 铁律

- 只动分到的那几个库；不碰 `verify_db` / `structure_check` / DB-QC 标准 / 别的库。
- 写库前先 `copy` 备份（`backup\<FAM>db.before-fix2-<YYYYMMDD>`），记 sha256 + 字节数。
- 修库脚本默认 **dry-run**：打印每一步与前后计数；`--apply` 才写。
- 写库用 `BEGIN IMMEDIATE … COMMIT`，异常回滚；不用裸 `executescript` 一次跑完。
- 修完必过 §3 自检 + `verify_db --quiet`，结果记进 `目录说明.md` 的 QC 段。

## 2 四类修法

### A 整表出库（表不该在库里）

1. `sheet.blob` zlib 解成 TSV → `zstd -19` 压到 `_share\<叶>\<源件名>__<sheet名>.tsv.zst`（`zstd` CLI 或 python `zstandard`）。
2. 回读解压件，与原文逐字节 + sha256 比对。
3. 删 `fact` 行、`sheet_dup` 边、`sheet` 行，`doc.n_sheets` 递减。
4. `meta.external` 记一行（列见 [merge-tables.md](merge-tables.md) §6 台账三式）。

### B 结果表只删 fact、留 blob

成品表判据：表名含 `pic/tab/figure/exam/结果`，或含 `±` 的均值汇总表（实测 34 张成品表 25,642 fact + 16 张 ± 汇总 4,885 fact）。处置：`DELETE FROM fact`，保留 blob，`meta.note.sheet_role.<sid>='derived'`。

### C entity 重建或拆除

- 有可靠个体键 → 按行解析 + `emap` 重映射，脏行置 NULL。
- 无可靠键（只是分级标签 / 特征名 / 组号，且无第二列可组合）→ `DELETE FROM entity`；`UPDATE fact SET entity_id=NULL`；`meta.entity.dropped = 理由`。**宁可不建，不留错的。**

### D PHI 假名

- 只覆盖手机 / 电话 / 身份证 / 邮箱 / 地址 / 姓名；其余列不动。
- 值 = `"P" + sha256(salt + 原值)[:12]`；salt 用统一文件生成，单独保管，不进库、不进报告。
- 空值 / `无` / `-` 保持原样，不改写。
- blob 保留原始（仅本机）；外发前对 blob 再脱敏。

## 3 修后自检

1. `PRAGMA integrity_check` = ok。
2. `Σdoc.n_sheets == COUNT(sheet)`。
3. dup + subset 行数 == `COUNT(sheet_dup)`。
4. 五组孤儿 = 0。
5. `dup_groups = 0`。
6. `fact.entity_id` 键 100% 存在。

再与备份对一遍：表集合相同、逐表行内容摘要一致、`meta` 只新增预期键。最后 `verify_db --quiet`，记 exit / P0 / P1 / P2。

## 4 机器门挡不住语义

21 库跑 `verify_db` 全 `P0=0 / exit 0`，人工 QC 仍查出 26 个 P0（entity 键不可用、结果表被拆、PHI 明文）。机器门只覆盖完整性 / 孤儿 / 计数 / 伦理（D1–D9、D19），D10–D18 全靠人；修库报告须写「人工核过哪些语义项」。

## 5 假名 ≠ 已脱敏

3 个库 `meta.rule` 自称已假名，实测与宣称矛盾——比不做更危险。以实测为准，不信 `meta.rule` 自述；PHI 列关键词已提为机器门 D21（fact 层明文 PHI）。

## 6 建库门（写 entity 前）

键可用性预检：重复率 >5%，或键值非个体号 → 拒绝建 entity 并报 P0，防止「先建错再修」。
