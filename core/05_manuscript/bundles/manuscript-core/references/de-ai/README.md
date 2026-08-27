# de-ai — 去 AI 腔 索引

**Canonical entry:** `../../MODULE.md`（manuscript-core）。此文件仅做路由，不重复规则正文。

## 加载顺序（`de-ai` 模式）

1. **`forbidden-phrases.md`** — 先查这个。学科专属禁词表（delve/robust/leverage 等），任何润色/草稿都先过一遍。
2. **`ai-isms-checklist.md`** — 更细的 AI 味特征清单（句式、结构层面），forbidden-phrases 查完再查这个。
3. **`stop-slop-core.md`** — 通用 prose hygiene 规则 + **医学 SCI 场景的强制覆盖**（被动语态例外、禁 em-dash 等）。**覆盖条款优先于文件内其余通用规则。**
4. **`ai-writing-detector.md`** — 仅当用户明确要"检测报告 / 打分"时才打开，不是默认润色路径的一部分。

## 不在默认加载路径中（背景参考，非规则源）

- `phrases.md` / `structures.md` / `examples.md` — `stop-slop-core.md` 内部引用的通用博客体参考资料。其中多数条目（如 "Plot twist:"、"circle back"）不出现在医学英文论著语域中；真正适用于本实验室写作的禁词/结构规则已被 `forbidden-phrases.md` 和 `ai-isms-checklist.md` 覆盖。除非要处理非医学文本，否则不必单独查阅。

## 铁律（不因去 AI 而放弃）

- 不改数字、P 值、CI、术语、引用、伦理号
- Methods 保持被动语态（实验室体例），不因"去 AI"而强改主动语态
- Discussion 的 calibrated hedge（may/might/could/suggest）不算 AI 腔，不要删
