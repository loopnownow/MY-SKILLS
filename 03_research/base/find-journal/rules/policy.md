# Stable policy (edit only when the user changes rules)

Data year changes every year. These rules do not, unless the user says so.

- Medical or medically eligible journals only.
- **BMC / Medicine whitelist first**: `data/2026/whitelist-bmc-medicine.csv` (name or ISO contains BMC, or contains Medicine; ~486 titles). Within a layer, when 稿件匹配度 is similar, **prefer** whitelist titles; checkbox table must **not** mark「可疑」and must **not** red-flag. Blacklisted MEDICINE (LWW Baltimore) never enters whitelist and is never recommended. Replaces the old “down-rank name contains Medicine” rule.
- **Submitted / 选刊 whitelist first**: `{find_journal_submission}\whitelist-submitted.csv` (seed: journals with submission URLs written back in `data/2026/submission-urls.csv`; roughly lab-used titles). Within a layer, when 稿件匹配度 is similar, prefer this over the BMC/Medicine pattern whitelist. Append on new URL write-backs (dedupe); never write blacklist/graylist titles here.
- **Graylist (not recommended)**: `data/2026/graylist.csv` (includes **Frontiers family** pattern: Frontiers Media / name Frontiers…). Between whitelist and blacklist. **Do not use a graylist title when a better non-gray match exists**; only include when the layer quota is short and scope still fits, or the user names it — mark「灰名单/不推荐」. Never boost. Blacklist wins on conflict.
- Phase-1 HTML: **yellow highlight only when 投稿易投指数 ≥80**.
- Live blacklist on every run: PLoS One, Scientific Reports, MEDICINE (LWW Baltimore). Not NEJM, not Nature Medicine.
- Default layers and order: 层2 (Q1 IF<5) **10 titles** → 层3 (Q2) **10 titles** → 层4 (Q3) **10 titles**. 层2补 (Q1 5≤IF≤10) ask-before-use, **default OFF**.
- Rank inside a layer by **MJF/MFI match** (highest) → **submitted/选刊 whitelist boost** (`whitelist-submitted.csv`) → **BMC/Medicine pattern boost** → **JESI/JEI ease** → capacity signal; omit graylist unless asked (log volume as weak tie-breaker). See `jesi-model.md`. Do not bake concrete IF numbers into this policy file.
- **Similar-article check (user rule 2026-10-08), round 2:** round 1 ranks by the existing criteria and does not search. Round 2 searches each candidate journal for similar articles from the last 3–5 years. No similar article → lower it inside its layer. Cite found articles (title, year, DOI/link); never invent them. Full rule: `SKILL.md` § Similar-article check.
- **No fixed scoring weights** as durable policy — Gemini/JESI numeric weights are initial defaults only and must be overridable by user constraints (speed vs Q1 vs APC).
- Layer 1 (Q1 IF>10) only if asked. Layer 4 (Q3) is **default on**. Comprehensive/general medical journals may be recommended when fit is reasonable.
- Two phases: no AIM / author instructions / APC until the user confirms shortlist (备选杂志).
- Best quartile = best among that journal's medical-related categories.
- External journal-recommender tools are **query/candidate providers only**, not the top-level decision maker; do not adopt them as skills.
- **Risk:** Unknown ≠ Low Risk; do not invent missing metrics.
- **Persistence / absorb·query·delete:** save submission URLs, blacklist names, policy/workflow/approach, query-source *capability*, personal prior outcomes, and rewritten Fit/Risk/Evidence methods. Do **not** persist JIF, JCR/JCI/CAS values, APC, review-time, annual volume, self-citation, or author-experience **values** into `data/2026/submission-urls.csv` or other DB-like files — retain **query capability** only. Delete abstract→CAS prediction, fixed weights, fixed LetPub dependency, fixed external output template, monolithic external SKILL.md (`persistence.md`).
- Phase-1 display (v1.9+): Chinese score headers **稿件匹配度** / **投稿易投指数**; always show **接收率 / 初筛拒稿率 / 送审率** (blank if unknown); curated **易投指数** display column removed from Phase-1 tables/HTML/JSON and from JDI/JESI approximations (`jesi-model.md`). Rates are query/display-only — never invent; never persist into `data/2026/submission-urls.csv`.
