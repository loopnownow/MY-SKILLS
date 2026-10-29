---
name: "radiology-frontier"
description: "Turn imaging-AI frontier topics (选题 / 前沿 / frontier) into a publishable question with evidence gaps and journal-fit notes. Never invent PMID/DOI."
domain: "03_research"
trigger: ["frontier", "选题", "前沿", "立项方法", "超极化"]
inputs: ["topic", "year_window"]
outputs: ["evidence_gaps", "journal_fit_notes"]
tools: ["pubmed_pages"]
quality_control: "do not invent PMID/DOI"
owner: "03_research/advanced/radiology-frontier.md"
---

trigger is documentation only; not independently discoverable.

# Frontier Directions & Evidence Layer

Use this skill to turn "what's hot in imaging AI" into **a publishable question matched to the
user's data** — and to expose the **publication-pattern evidence** behind each recommendation.
It is the strategic front of the chain: before designing (→ radiology-design), decide *what is
worth doing and likely to be accepted at a high-impact venue*.

## Core stance

- **Frontier ≠ feasible for you.** A direction is only useful if the user's data can actually
  carry it. Always test a trend against their disease, modality, n, centers, labels, and omics.
- **Evidence over vibes.** Recommendations are grounded in *how top journals actually publish*
  — design patterns, validation expectations, and what each venue rewards — not in slogans.
- **Patterns are durable; specific papers are not.** This skill encodes **publication-pattern
  heuristics** (the kinds of studies that get into each journal and the methodological bar
  they meet). It does **not** ship a fixed citation list. Concrete recent papers must be
  retrieved and verified **live** (→ live `lit-search`); never cite a PMID/DOI from memory.
- **Separate hot from suitable.** Name directions that are trendy but a poor fit for the data,
  and say why — steering away from a wrong direction is as valuable as suggesting a right one.
- **Bound novelty claims.** "First/novel" is a liability without a literature check. Frame
  innovation as a specific, defensible gap, not a superlative.
- **Integrity.** Never fabricate references, effect sizes, or "recent studies show…" claims.
  Mark anything that needs same-day verification.

## When to use

- "Give me frontier directions for [disease/modality] I can publish in the next 1–2 years."
- "找近三年的前沿方向和创新点" / "结合我的数据找创新点。"
- "Is [foundation models / self-supervised / VLM / multimodal / federated] right for my data?"
- "What's the evidence/publication-pattern basis for this recommendation?" / "有什么文献依据？"
- "Which top journals publish this kind of study, and what do they demand?"

## When to open extra files

| File | Open when |
|---|---|
| live `design-study` | Feasibility / study-design conversion for a candidate frontier direction |
| live `lit-search` | Retrieve and verify seed papers (PMID/DOI); confirm the gap is still open |
| `03_research/advanced/radiology-design.md` | Inventory already exists, or hand off to full design after a direction is chosen |
| [method-upgrade-into-grant.md](method-upgrade-into-grant.md) | **Voice B**: write method upgrade into justification (MRS → hyperpolarized 13C / metabolic flux → multimodal+ML); sentence placement only |

## Workflow

1. **Read the data** — disease, modality, n, centers, labels, follow-up, omics availability
   (reuse the inventory from `radiology-design` if present).
2. **Scan themes and filter by fit** — candidate directions include foundation models, SSL, VLM,
   multimodal fusion, longitudinal, weak/semi-supervision, domain adaptation, federated,
   generative, radiogenomics. For each, state data prerequisites and whether the user meets
   them. Reject poor fits explicitly.
3. **For AI/radiogenomics strategy**, judge each idea against generalisability, supervision cost,
   multimodal fusion, trustworthy inference, external validation, and clinical-value evidence
   (keep the criteria in this step; no separate theme-map file).
4. **Ground in evidence** — for each surviving direction, state the publication pattern (study
   kind, validation, venues) and the methodological bar. Flag every concrete claim that needs
   **live verification**.
5. **Convert to questions** — with live `design-study` (and `radiology-design` when imaging-
   specific), turn the best 2–4 directions into specific research questions with endpoint,
   comparator, and the minimum evidence to be competitive.
6. **Trigger live search** — hand the chosen direction to live `lit-search` to retrieve and
   verify current seed papers (PMID/DOI) and confirm the gap is still open.
7. **Return** a ranked shortlist: direction → fit → evidence pattern → executable question →
   target-venue tier → what to verify now.

## Output contract

1. **`Data-fit summary`** — the inventory and the binding constraint, reused or restated.
2. **`Frontier shortlist`** — ranked directions, each with: fit (yes/conditional/no + reason),
   the publication-pattern evidence, and the methodological bar.
3. **`Executable questions`** — 2–4 concrete questions (endpoint, comparator, minimum evidence),
   each mapped to a candidate venue tier (→ `03_research/advanced/journal-selection.md`).
4. **`Hot-but-unsuitable`** — trendy directions to avoid for this data, with the reason.
5. **`Verify now`** — the explicit list of claims/papers to confirm via live search today
   (handed to live `lit-search`); nothing here is presented as already-verified.


## Method upgrades into justification (立项) (Voice B only)

When the user is writing **their own** justification and the method is moving along
**MRS → hyperpolarized 13C / metabolic flux → multimodal + interpretable ML**,
open `method-upgrade-into-grant.md`. Put the technical gap **in the justification**, not only in the innovation box.

- Justification subsection titles are mechanism nodes; methods are evidence.
- Name the gap (1H-MRS cannot quantify [molecule]; subjective scales) → this study uses the upgraded technique.
- Do not write unfinished techniques as completed basis. Do not put Voice A critique into the justification.
- Chapter skeleton / 确定·阐明·探讨 → `radiology-design`. CN/EN abstract sentence bank → `grant-writing.md`.

## Quality bar

A good frontier read sounds like a mentor who reviews for these journals: it knows what each
venue keeps publishing and why, matches the trend to the user's real data, names the directions
that are fashionable but wrong for them, and never invents a citation to sound current.

## Handoffs

- Turn the chosen direction into a full design → `radiology-design`.
- Retrieve & verify current seed literature / confirm the gap → live `lit-search`.
- Which journal tier the question targets → `03_research/advanced/journal-selection.md`.
- Method-specific feasibility → live `stats-analysis` / live `design-study`.
- Citation export of verified seeds → live `manage-refs` (check with `verify-refs`).
- The direction fits **own** funding proposal (Voice B) → `method-upgrade-into-grant.md` then
  `radiology-design` `grant-own-skeleton.md` + `grant-writing.md` phrase bank.
- Reviewing **other people's** NSFC (Voice A) → `../advanced/grant-review.md`.
  Never mix review tics (评议口癖) into the justification.
- This skill advises on research strategy; specific recent claims must be verified live.
