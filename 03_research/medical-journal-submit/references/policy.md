# Stable policy (edit only when the user changes rules)

Data year changes every year. These rules do not, unless the user says so.

- Medical or medically eligible journals only.
- **BMC / Medicine 白名单优先**：`references/whitelist-bmc-medicine.csv`（刊名或 ISO 含 BMC，或含 Medicine；约 486 本）。层内在稿件匹配度相近时**优先推荐**白名单刊；勾选表**不要**标「可疑」、**不要**红标。已黑名单的 MEDICINE（LWW Baltimore）永不进白名单、永不荐。本条取代原「刊名含 Medicine 降权」。
- **投过/选刊白名单优先**：`references/whitelist-submitted.csv`（种子：`submission-urls.csv` 已写回投稿网址的刊；约实验室实际用过的刊）。层内在稿件匹配度相近时**优先于** BMC/Medicine 模式白名单。新写回投稿网址时同步追加（去重）；勿把黑名单/灰名单刊写入。
- **灰名单（不推荐）**：`references/graylist.csv`（含 **Frontiers 系列** pattern：Frontiers Media / 刊名 Frontiers…）。介于白名单与黑名单之间。**有更好的非灰名单匹配时不使用灰名单刊**；仅层额不足且 scope 仍合适、或用户点名时才列入，并标「灰名单/不推荐」。永不 boost。与黑名单冲突时以黑名单为准。
- Phase-1 HTML：**仅投稿易投指数 ≥80 黄底高亮**。
- Mounted blacklist on every run: PLoS One, Scientific Reports, MEDICINE (LWW Baltimore). Not NEJM, not Nature Medicine.
- Default layers and order: 层2 (Q1 IF<5) **10本** → 层3 (Q2) **10本** → 层4 (Q3) **10本**. 层2补 (Q1 5≤IF≤10) ask-before-use, **default OFF**.
- Rank inside a layer by **MJF/MFI match** (highest) → **投过/选刊 whitelist boost** (`whitelist-submitted.csv`) → **BMC/Medicine pattern boost** → **JESI/JEI ease** → capacity signal; omit graylist unless asked (log volume as weak tie-breaker). See `jesi-model.md`. Do not bake concrete IF numbers into this policy file.
- **No fixed scoring weights** as durable policy — Gemini/JESI numeric weights are initial defaults only and must be overridable by user constraints (speed vs Q1 vs APC).
- Layer 1 (Q1 IF>10) only if asked. Layer 4 (Q3) is **default on**. Comprehensive/general medical journals may be recommended when fit is reasonable.
- Two phases: no AIM / author instructions / APC until the user confirms 备选杂志.
- Best quartile = best among that journal's medical-related categories.
- External journal-recommender tools are **query/candidate providers only**, not the top-level decision maker; do not mount them as skills.
- **Risk:** Unknown ≠ Low Risk; do not invent missing metrics.
- **Persistence / absorb·query·delete:** save submission URLs, blacklist names, policy/workflow/approach, query-source *capability*, personal prior outcomes, and rewritten Fit/Risk/Evidence methods. Do **not** persist JIF, JCR/JCI/CAS values, APC, review-time, annual volume, self-citation, or author-experience **values** into `submission-urls.csv` or other DB-like files — retain **query capability** only. Delete abstract→CAS prediction, fixed weights, fixed LetPub dependency, fixed external output template, monolithic external SKILL.md (`persistence.md`).
- Phase-1 display (v1.9+): Chinese score headers **稿件匹配度** / **投稿易投指数**; always show **接收率 / 初筛拒稿率 / 送审率** (blank if unknown); curated **易投指数** display column removed from Phase-1 tables/HTML/JSON and from JDI/JESI approximations (`jesi-model.md`). Rates are query/display-only — never invent; never persist into `submission-urls.csv`.
