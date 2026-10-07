# JESI / JEI 1.0 — Journal Ease-of-Submission Index (transparent)

Do **not** treat JIF / quartile / JCI alone as “how easy to get in.” JIF and JCI are citation performance; they are not acceptance probability.

**Naming:** **JESI** (composite used in Phase-1) and **JEI** (Journal Ease Index) are the same family. Prefer:

```text
JEI = f(JDI, Capacity, Reviewability)
```

JEI is **not** merely `100 − JIF`. **MJF** = **MFI** (Manuscript–Journal Fit).

## Weight policy (ChatGPT + Gemini)

All numeric weights below are **initial defaults only**. They **must be overridable** by user constraints (speed vs Q1 vs APC/OA vs specialty influence). Do **not** bake fixed Fit Score weights from external tools into this pack. Prefer dynamic weighting at run time; document which weights were used and why.

Primary composite (three-index form — default):

```text
JESI = 0.50 × (100 − JDI) + 0.20 × JCI-C + 0.30 × MJF
```

(`MJF` interchangeable with `MFI`.) All component scores on a 0–100 scale unless noted. When rates are missing, Phase-1 still approximates from available metrics and **marks** incompleteness in-cell (no separate 置信度 column). Attach Evidence/Confidence (`value | source | date | confidence`) to inputs when available.

## Three indices

### JDI — Journal Difficulty Index

“How hard is the journal itself?” Prefer, in order:

1. Acceptance rate  
2. Desk-reject rate / Review rate (`Review Rate ≈ 1 − Desk Rejection Rate`)  
3. Submission/publication ratio when available  
4. JIF percentile / JCI / quartile (weaker proxies only)

Higher JDI ⇒ harder. In the composite, ease contribution is `(100 − JDI)`.

### JCI-C — Journal Capacity Index (capacity; not Clarivate JCI)

“Are there enough slots?” Prefer annual publications (research-article count if available), annual submissions, growth. Use **log capacity**:

```text
Publication Capacity P_raw = log(1 + Annual Publications)
P = 100 × log(1+N) / log(1+Nmax)   # normalize within the comparison pool
```

**Warning:** annual publications ≠ accepts. A mega-journal with huge N can still be hard if submissions dwarf accepts. Prefer acceptance / review rates over raw volume. Volume values are **query-only** — never durable skill/DB data.

### MJF (= MFI) — Manuscript–Journal Fit

“Does *this* manuscript belong here?” Scope similarity; similar papers in ~3 years (topic / disease / modality / design / methods / endpoints); article-type fit; clinical vs basic; audience. Output 0–100. Match outweighs ease when ranking inside a layer (see `SKILL.md`).

Rough relation:

```text
P(Acceptance) ≈ f(Journal Difficulty, Manuscript Fit, Manuscript Quality)
Journal Ease ≠ Manuscript Acceptance Probability
```

## Component scores A / R / P / Q / C (when rates available)

Alternate transparent form used to build or explain JDI / capacity / citation burden. Weights are **defaults**, overridable:

```text
JESI_components = 35A + 20R + 20P + 15Q + 10C   # default sum 100 when all present
```

| Symbol | Meaning | Scoring (0–100) |
|---|---|---|
| A | Acceptance | `A = min(100, Acceptance_Rate / 0.30 × 100)` (e.g. 5%→16.7, 10%→33.3, 15%→50, 20%→66.7, 30%→100) |
| R | Review (survives desk) | `R = Review_Rate × 100` |
| P | Publication capacity | log-normalized as above |
| Q | Quartile *ease* (not quality) | Q1=25, Q2=50, Q3=75, Q4=100 — name this `Quartile_Ease` |
| C | Citation burden ease | Prefer `C = JCI_Ease`; avoid double-counting JIF+JCI |

Priority when gathering inputs:

**Acceptance rate > Desk reject / Review rate > annual volume > quartile / JIF / JCI**

Rough acceptance bands (context only; cohort bias possible): ~5% very hard; ~10% hard; ~15–20% mid; ~20–30% relatively easier; ≥30% comparatively easy. Prefer 3-year averages when available.

## Phase-1 approximation (rates often missing)

**Removed:** do **not** use curated **易投指数**, and do **not** use `JDI ≈ 100 − 易投指数×20`.

When acceptance/review rates exist, prefer the **A / R / P** path (build JDI from acceptance and desk/review rates; capacity from log volume) then:

```text
JESI = 0.50 × (100 − JDI) + 0.20 × JCI-C + 0.30 × 稿件匹配度
```

(or the transparent `35A + 20R + 20P + 15Q + 10C` components form when enough inputs are present).

When some rate inputs are missing (**v1.11 display policy**): **still compute** 投稿易投指数 from available components (skip missing A/R and renormalize; if both A and R absent, use **capacity P + 稿件匹配度** fallback). **Mark** incompleteness in the JESI cell itself (e.g. `62.4*` plus short `缺:接收率,初筛拒稿率`, or a title tooltip listing missing inputs). Persist `jesi_missing: [...]` alongside `投稿易投指数` in Phase-1 JSON. Do **not** invent rates; rate columns stay blank/`—` when unknown. Do not use quartile-only / curated 易投指数 as the primary displayed JESI.

**Formulas (persist here; HTML 显示规则 mirrors in Chinese):**
- Full (A and R available): `JESI = 0.50×(100−JDI) + 0.20×JCI-C + 0.30×稿件匹配度` with A←接收率, R←送审率 or (1−初筛拒稿率), P/JCI-C←log(年发文量) normalized.
- Partial: same family with missing A/R skipped; or capacity+MJF fallback when no rates.

Display Chinese labels: **稿件匹配度** (MJF/MFI), **投稿易投指数** (JESI). Always show 接收率 / 初筛拒稿率 / 送审率 columns (blank/`—` if unknown). Phase-1 tables do **not** show 分层/策略 / 置信度 / ISO / JIF分区 / JCI分区. Never write approximated JIF/quartile/volume/rates into durable CSV/DB files — show them only in HTML/Markdown at generation time (see `persistence.md`). Do not estimate missing risk as “low.”

## Personal prior / PAI (later)

With enough real outcomes, correct generic JESI with **PAI** (`submission-prior.jsonl` / `submission-prior-logger`):

```text
Journal Difficulty + Capacity + Manuscript Fit + Personal Prior → Predicted P(Accept)
Submission Utility ≈ JEI + MJF + PAI + Practicality + Strategic Value − Risk
```

First phase stays on transparent JESI 1.0; do not jump to ML until dozens–hundreds of journal-level datapoints exist.

## Explicitly deleted from external tools

- Abstract → CAS 1/2/3/4 prediction  
- Fixed Fit Score weight tables copied as policy  
- Fixed LetPub-only pipelines  
- Fixed monolithic external output templates as the pack’s only format  
