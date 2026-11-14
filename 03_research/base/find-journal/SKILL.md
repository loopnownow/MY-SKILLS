---
name: find-journal
description: Recommend medical journals from the user's JCR2026 curated pool and format manuscripts to target-journal author instructions. Use when the user asks to 推荐杂志, 投稿, 选刊, JCR/JCI分区, 影响因子, 版面费, AIM, author instructions, or to tidy a medical paper for submission.
metadata:
  type: workflow
  version: "1.20"
  source_table: {jcr2026_xlsx}
  owner: "03_research/base/find-journal/MODULE.md"
  seat_route: A 03_research/find-journal (Victor)
  home: 03_research/base/find-journal (A 03_research/find-journal is Victor seat pointer only)
  advice_merged: Gemini+ChatGPT 2026-09
---

# Medical Journal Submit

Thin contract for find-journal (list gates, layer policy, output shape): scope, bans, phase names, and pointers. The house working method and the revision authority live in `03_research/advanced/`; this file does not restate a procedure. Pack data (`rules/`, `data/`, `references/`) stays beside it as data.

## Mission

Recommend journals from the lab's curated JCR pool with an auditable fit/ease rationale, then hand the chosen journal to formatting. It decides; external recommenders are data providers only. It does not write the manuscript (`05_manuscript/base/write-paper/`) or format it (`journal-format-compliance/`).

## Scope / Out of scope

In: 推荐杂志 / 选刊, layer and list gates, similar-article check, Phase-2 short table, portal-URL write-back.
Out: journal formatting to author guidelines (nested `journal-format-compliance/`, a registered fine id since 2026-11-13); manuscript prose; APC/AIM lookups before the user confirms a shortlist.

Routing: lives in `03_research/base/find-journal/`; the former advanced `find-journal/` stub was removed 2026-10-17 — do not recreate it. Called from `03_research/advanced/journal-selection.md`. Bai handles Phase-1 checkbox HTML → export JSON; Aitee only for formatting.

## Input

Minimum: the manuscript (or its abstract + design), and the target layer order defaults. Ask the user **before each run** whether to include 层2补 (default OFF). If a rate/metric is unknown, leave it blank and mark it; never invent it.

## Workflow (decision nodes)

1. **Load gates first**, in this order: `data/2026/blacklist.csv` (never list), `data/2026/graylist.csv`, `{find_journal_submission}\whitelist-submitted.csv` (submitted/选刊/审稿; stronger boost), `data/2026/whitelist-bmc-medicine.csv` (BMC/Medicine/MDPI pattern; secondary boost).
2. **Build Phase-1 tables**: three default tables of 10, in layer order 层2 (Q1, IF<5) → 层3 (Q2) → 层4 (Q3, default on); 层2补 (Q1, 5≤IF≤10) only on opt-in; layer 1 (IF>10) only when asked. Default total 30. Layers come from the `layer` column of the single pool table `{find_journal_pools}\index.csv`. General/comprehensive titles are allowed when fit is reasonable.
3. **Rank inside each layer**: 稿件匹配度 (MJF = MFI) highest; then submitted/选刊/审稿 whitelist; then BMC/Medicine/MDPI pattern whitelist; then 投稿易投指数 computed from **available** inputs only (formula in `rules/jesi-model.md`, never copied into prose; partial values marked e.g. `62.4*` + `缺:…`); annual volume only as a weak capacity tie-breaker.
4. **Similar-article round** (round 2 of this check only): query the candidate journal for similar work from the last 3-5 years with a real tool (PubMed/OpenAlex/Europe PMC/Crossref/journal site); if found, cite 1-3 titles with year and DOI/link in 匹配理由; if none, lower that journal below same-layer journals with matches and write 「近年未见类似文章，已降级」. A failed search is not "no hits": retry, then say the search failed.
5. **Phase-1 columns** (exact): 勾选 | 期刊全称 | 2025 JIF | 年发文量 | 接收率 | 初筛拒稿率 | 送审率 | 匹配理由 | 稿件匹配度 | 投稿易投指数(可带缺标). Chinese headers only for MJF/MFI→稿件匹配度 and JESI→投稿易投指数; no 分层/策略 column (keep `data-layer`/`data-tier` on checkboxes); always show the three rates (— if unknown); no AIM/instructions/APC in Phase 1. Then ask the user to circle 备选杂志.
6. **Phase 2 short table** after confirmation: 期刊全称｜JCR分区｜影响因子｜年发文量｜投稿网址/作者须知 — full URLs visible, author-instruction URLs allowed, no ISO/OA/置信/APC/分刊详情. Lookups follow `rules/aim-author-checklist.md`.
7. **Persist and deliver**: only portal submission URLs go to `data/2026/submission-urls.csv`; JIF/quartile/volume/APC/review time are query-only and never persisted as durable lists; advanced outcomes append `{find_journal_submission}\submission-prior.jsonl` (no IF/quartile fields). Prefer HTML; generic HTML craft in `00_orchestrator/references/html-visual-design.md`.
8. **Format the chosen journal** via nested [`journal-format-compliance/`](journal-format-compliance/): plan first, Track Changes author A, never silently fix identity/funding/ethics conflicts; publisher quirks in `rules/journal-format-publisher-notes.md`; house baseline `journal-format-compliance/references/house-style-defaults.md`.

## Constraints (never)

- **Never list blacklist titles** (also `data/2026/blacklist-names.csv`); the list body is data, not prose.
- Never boost a graylisted title; use gray only when non-gray cannot fill the layer or the user asks, and label 「灰名单/不推荐」. Never move gray → submitted whitelist without approval (the review-invite/reviewed + JCR-quartile standing rule is the only exception).
- Never treat **Unknown risk as Low Risk**.
- Never invent rates, articles, titles, years, DOIs, or links; blank rate cells stay blank.
- Never persist yearly metrics into `data/2026/submission-urls.csv` or skill text; never hand-edit the pool `index.csv` (tag at the July rebuild).
- Never collapse the three layers into one top-N list; never recommend layer 1 by default; never offer 层2补 without asking.
- Never install external journal-recommender skills or copy their fixed Fit-Score weights.
- Never query AIM/instructions/APC before the shortlist is confirmed.
- Wording: when pointing at journal-selection rules, say **this repo**; do not say 「空挂」.

## Output and handoff

- Phase 1: three (optionally four) tables of 10 + shortlist request; Phase 2: per-paper short table + portal URL write-back.
- Handoff: to `journal-format-compliance` after the journal is chosen; to 00 at G-06/G-05; to `write-paper` only for house style, not journal rules.

## Files

| File | Use |
|---|---|
| `data/2026/blacklist.csv`, `blacklist-names.csv` | hard exclusion |
| `data/2026/graylist.csv` | not recommended when better exists |
| `data/2026/whitelist-bmc-medicine.csv` | pattern boost (LWW MEDICINE excluded) |
| `{find_journal_submission}\whitelist-submitted.csv` | submitted / review-invite boost |
| `data/2026/submission-urls.csv` | portal URLs only |
| `{find_journal_pools}\index.csv` (+ `l1-l2-map.csv`) | single pool table in _Docs; select by `layer` |
| `{doc_library_jcr}\<year>\` | per-year submission priors |
| `rules/recommendation-workflow.md`, `rules/jesi-model.md` | workflow; JESI/JEI/JDI/JCI-C/MJF |
| `rules/policy.md`, `rules/persistence.md`, `rules/modules.md` | stable rules; absorb/query/delete; four logical modules |
| `rules/query-sources.md`, `rules/aim-author-checklist.md` | query sources; Phase-2 checklist |
| `rules/annual-update.md`, `rules/graylist.fine-id.md` | July refresh; gray definition |
| `journal-format-compliance/` | chosen-journal formatting (nested fine id) |

## Annual refresh and provenance

New JCR workbook → follow `rules/annual-update.md` (July, after the JCR release); keep `rules/policy.md` unless blacklist/layers/10-per-layer rules also change. Advice provenance: merged Gemini + ChatGPT private advice (2026-09); absorb/query/delete table in `rules/persistence.md`.
