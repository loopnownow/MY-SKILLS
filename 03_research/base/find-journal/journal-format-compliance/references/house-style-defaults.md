# House 版式默认与套刊对照

本组稿件的版式基线，用作「期刊值 vs house 默认」两列对照的左列。套刊时期刊明写的覆盖 house，未写的保留 house，冲突交作者裁决。

## 页面与段落默认

- 页面：A4 `21.00×29.70cm`，四边 `2.54cm`。
- 每一段（不只正文）：`style='Normal'`、`align=JUSTIFY (3)`、`before=0 after=0 line=360 rule=auto jc=both`、`12.0pt Times New Roman #000000`。line=360 即 1.5 倍行距。

## 样式表（粗/斜）

| 位置 | 形态 |
|---|---|
| Title | 粗 + 斜 |
| Authors / Affiliation | 斜 |
| `Corresponding author:`、`Funding:`、`Ethics:`、`Acknowledgments:`、`Author contributions:`、`Data availability:` | 粗体标签 + 斜体占位（如 `[name, email, address]`、`[IRB Date/NO / empty]`） |
| `Highlights`、`Abbreviations`、`Abstract` | 粗标签，其下内容斜 |
| Abstract 内 `Objective:` 等标签 | 标签 run 粗、正文斜，只加粗到冒号 |
| `Table 1.`、`Figure 1.` | 标签粗 + caption/legend 斜 |

## 结构默认值

| 项 | house 默认 |
|---|---|
| Running title | ≤50 字符、无缩写、无冒号 |
| Title | 无冒号、无缩写 |
| Keywords | 5–8 个，非专有名词小写 |
| Abbreviations | 字母序，只收正文出现 ≥2 次的词 |
| Highlights | 3 条，各一句；分别为主发现、增量价值、更远终点；可含终点名，禁数字 |
| Abstract | 六个标签；其 Methods 句须镜像正文 Methods 小节名（单向可追） |
| Methods | 14 节固定顺序，不带引用 |
| Results | 小节名与顺序同 Methods，一一对应 |
| References | Vancouver，按首现编号，每条带 DOI；flush left 无悬挂缩进，不聚簇引用（不写 range） |

## 冲突处置枚举

三选一，不静默改内容：

1. 替换为期刊值（instructions 明写时）。
2. 保留 house 默认并标注未覆盖项。
3. 交作者裁决（涉及内容取舍时；不自行删句、不改结论数字）。

## 版式改动的验收形态

- 修订计数：`w:ins` / `w:del` 数量与段落、表格数一起记（实测样例：`w:ins=11`、`w:del=12`、194 段、2 表）。
- 逐段读回 `accepted` 全文抽查，确认无残留占位。
- 再渲染一次比对版式；纯文本观感不能当证据。

## 过程

1. 取目标刊 author instructions，建「期刊值 vs house 默认」两列差异表：字数、摘要结构、关键词数、图表数、参考文献风格、字体/行距、盲审要求。
2. 逐项裁决（替换 / 保留 / 交裁决）。
3. 套版：按上表改段落样式、字体、行距、标签粗斜；不改结论与数字。
4. 全部改动走 Word Track Changes，每处可在修订层定位。
5. 验收：读回段落/表格数 + 修订计数 + 逐段 `accepted` 抽查 + 再渲染比对。
6. 交付三件：tracked 版 + clean 版 + 变更清单（改哪项、依据哪条 instructions）。

## 注意事项

- house 默认不等于期刊值：本组 Keywords 默认 5–8，既有记录里 Acta Radiologica 要求 ≤6；套该刊须按期刊覆盖，不能拿 house 值当合规标准。
- `[PLACEHOLDER]` 与方括号写作指令是排版期脚手架，投稿前必须删净。
- 版式只能在 docx 的 paragraph / section 层验证：before/after 成对 dump 才可复算 line=360 与四边 2.54cm。
- 格式与内容分开改：格式修订批不夹带数字或结论改动。
- 中英图题、关键词分隔符、摘要字数属期刊特例，不能由 house 默认外推。

## 已知边界

- house 默认由本组 5 篇稿件提炼，未与任何特定期刊的 instructions 逐条映射。
- 「Methods 14 节顺序」是否被目标刊接受，尚未验证；套刊时以期刊要求为准，必要时重排并记入变更清单。
