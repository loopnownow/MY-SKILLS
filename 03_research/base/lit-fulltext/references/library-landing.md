# 入库落点与计数对账

OA 全文取回后落库的口径：一个文件一篇、文件名即键、sha256 判同一文件、三处计数必须同数。取不到不是失败，落错地方才是。

## 实体落点

- 路径：`_library\references\<L1>\<L2>\<DOI>.pdf`；DOI 里的 `/` 落盘转 `_`（如 `10.1016/j.eurrad.2020.1089` → `10.1016_j.eurrad.2020.1089.pdf`）。
- 同族同层平铺，不按期刊或年份再分子夹：层级只由 L1/L2 决定。
- 无 DOI 件：`NOID_<sha8>_<slug>.pdf`，sha8 = sha256 前 8 位；L1/L2 走兜底层 `other/theses`。
- 子工程只放指针 `ref\refer\DOI_<doi>.md`，不存第二份 PDF。

## sha256 是唯一判据

每件入库即算 sha256 并写进 index。判"是不是同一文件"只看 sha256，不看文件名、不看大小、不看下载时间：文件名可改，内容不变即同一件。

## index 九列

`doi,pmid,l1,l2,rel_path,sha256,source_project,fetched_at,notes`。九个字段是登记契约，缺字段的条目不入库（见 MODULE 入库前置检查）。

## 计数三处同步

实体文件数 = index 行数 = `_library/INDEX.md` 的计数。三处不同数即停，先对账再继续；写"行数"时必须带日期，因为下一轮会变。

## 多版本同文只留定稿

preprint、accepted manuscript、出版社定稿属同一篇的不同版本，只留定稿，其余在 notes 记「同文旧版不存」。多版本不算多件，不能作为多条 index 行。

## 过程

1. 取 DOI|PMID 清单，先查 index 的 sha256；命中即跳过（已有同文件）。
2. 走 OA 源：PMC、出版社 OA、机构/学科仓储；取不到记 `unavailable`，并写下试过的源。
3. 落到对应 `<L1>\<L2>`，DOI 转下划线；无 DOI 件按 NOID 命名进兜底层。
4. 算 sha256，写 index 九列。
5. 计数三处对账；不一致即停。
6. 入库前检查三项齐：DOI（或 NOID）、L1/L2、source_project。

## 注意事项

- 禁第二份副本：同一 sha256 在库里只出现一次，项目侧只留指针。
- 多版本同文不算多件，只留定稿。
- 文件名被改过的件，先修 DOI 再入库；修正要走实体文件名、index 的 rel_path、指针文件名三段同步（规则见 verify-refs 的指针同步条目）。
- 取不到不建 0 字节占位 PDF；记为 unavailable 并在 manual_needed 里留清单。
- 写「行数」必带日期，跨轮引用标日期。
- 本文件不抽 PDF 正文，只登记实体。
