# 检索结果入库闸

检索结果不直接进库：先过三件套闸，再登记。列在这里的规则控制"什么能进 `_library`、进哪一层、进哪本账"。

## 入库三件套

进库必齐三项，缺一项留在项目侧：

1. DOI（真核过的；核不到不算）。
2. L1/L2 层级。
3. `source_project` 登记（这条文献是为哪个项目收的）。

三件齐才写 `references\index.csv` 并同步 `_library/INDEX.md` 计数（+N 后核对总数）。

## L1/L2 取家族口径

层级沿用家族口径（妇科肿瘤 → `obgyn`），不按个人偏好另立。新增 L2 前停下、由城城点名；检索 agent 不得自建层级，也不许把 `radiology` 当自造的 L1。

## 无 DOI 件

走兜底层 `other/theses` + `NOID_<sha8>_<slug>.pdf`（sha8 = sha256 前 8 位），仍照常登记 index，不能因为没 DOI 就留在项目侧。

## 项目侧只留指针

子工程只放 `ref\refer\DOI_<doi>.md` 指针，不存 PDF 副本、不存检索快照。index 只存书目字段，库里实体才是文件本体。

## 两本账不混填

| 账本 | 存什么 |
|---|---|
| `lit-bank\index.csv` | 书目池：题录、结论、主题词，含 layer/kind/edition |
| `references\index.csv` | 实体件：rel_path、sha256、L1/L2、source_project |

同一篇可以两本都有，但字段各填各的；把实体字段填进书目池（或反之）会让计数与去重同时失效。

## 路由

文献检索与文献替换归检索席，写作席只做路由、不自己检索。检索结果交给 `lit-fulltext` 取全文，交 `verify-refs` 核引用。

## 过程

1. 先查重：DOI、PMID、题名三项比对已有两本账。
2. 结果先落候选清单，再逐条核 DOI 真实性；核不到的不写进正式结果。
3. 定 layer（personal / base / 其他）与 L1/L2；新 L2 前停下点名。
4. 去重后一行一条：citation_nlm、result_conclusion（一句）、themes，留 verified_at。
5. 需要全文转 `lit-fulltext`；需要核对引用转 `verify-refs`。
6. 入库前查三件套，缺项退回，不带着缺口登记。

## 注意事项

- 不存 PDF 副本、不存检索快照；项目侧只留指针。
- l1/l2 不许自造一级（如把 `radiology` 当 L1）。
- 不编 DOI、题名；抓不到写「未找到」，不写推测值。
- 同文多来源只留一行，其余记 notes。
- 行数跨轮会变，引用具体数字时标日期。
