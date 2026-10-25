# Evidence (request + I/D consumption)

## Part A — Evidence Request

## Evidence Request protocol (thin)

**Owner:** `05_manuscript` personal. Final claim/citation QC lives here (Aitor-format / overclaim rules). **Not** a literature-research route and **not** a B05 upgrade.

**Loop (lab):**

```text
Mounted pack (this-run pick: session mounts from 01 registry menu)
  → Evidence Request card (gap discovery only)
  → 03_research (Victor) searches
  → Candidate evidence
  → A 05 personal (Aitee): Accept / Weaken / Delete
  → if still insufficient → G-LIT dual plan (00 may call 03 again)
```

Mount packs **propose**; they do **not** choose the final citation or keep an over-strong verb. 03 **searches** only. A 05 **judges** whether a candidate supports the claim. 00 owns whether to invoke 03 again (G-LIT).

Related: consume verified I/D rows via `05_manuscript/personal/process/evidence.md` (Part B); quotas in `Aitor-format.md`; citation mechanics in `citation-and-language.md`.

### When to raise a card

- A mounted writing/review skill flags a claim with missing, associative-only, wrong-population, or second-hand-only support
- 05/06 literature verify fails on a factual sentence that still needs a source
- User asks to 补文献 / 核对引用 for a specific sentence (not “search the topic”)

Do **not** use this file for 选题 / 选刊 / systematic review / Embase+Cochrane default sweeps.

### Card fields (required)

Copy into a Word comment (author **A**) and/or handoff note. Prefix the discoverer when a mount raised it (`[Nature:…]` / `[self-review:…]` / `[peer-review:…]` / `[B:…]`); dual-tag with `[A:personal]` when A 05 also judges.

```text
Evidence Request
────────────────
Claim: <exact sentence or claim atom>
Problem: <missing | associative_only | wrong_population | second_hand | contradictory | overclaim
          | guideline_definition | missing_prior_result | related_work_appraisal | scarcity_check>
Required: <what would count as adequate support>
Section: <Intro | Discussion | other>
Source: <mount id or A:personal>
Status: open
```

Optional: `PMID/DOI candidates` (only if already verified; never invent).

#### Introduction card types

| Problem | Raise when | 03 returns |
|---|---|---|
| `guideline_definition` | Element 2 has no dated guideline, or cites an edition that may be superseded | Latest edition (body, year, date checked); where the definition sits; the recommendation and its level of evidence; one open issue the guideline states; full-text level (L3) |
| `missing_prior_result` | Element 3 or 4 states a limit or a gap with no prior quantitative finding | One source per class (`mri_accuracy`, `radiomics_endpoint`, `habitat_or_nearest`): design, n, effect with CI; at least one weaker or limited result if one exists |
| `related_work_appraisal` | Element 4 has results but no judgement | For each returned study: strength, and the weakness relevant to this study (endpoint definition, validation type, region of interest, comparator, sample), so A 05 can write one or two group-appraisal sentences |
| `scarcity_check` | A sentence says "few", "uncommon", or "limited" about published work | Search log: PubMed plus one other source, query strings, dates, counts screened; the closest studies found |

03 returns rows in the Evidence Pack format (`05_manuscript/personal/process/evidence.md` (Part B)), not prose. A 05 decides with the three exits below. Draft elements 2–5 only after every card has an exit.


### Roles

| Step | Who | May | Must not |
|---|---|---|---|
| Discover gap | Mounted pack (this-run) or A 05/06 | Raise card | Pick final ref; rewrite whole paragraph; auto-mount another source |
| Search | `03_research` (Victor) only | PubMed / DOI verify; return candidates | Change manuscript wording; invent PMID/DOI |
| Judge | **A 05 personal (Aitee)** | Accept / Weaken / Delete (below) | Treat mount suggestion as silent apply; run a second lit-research route inside 05 |
| Re-invoke 03 | `00_orchestrator` (G-LIT) | Call 03 after dual-plan comment | Skip dual plan; invent citations |

A05 stays the writing skill entry / personal upper layer. It is **not** a permanent three-pack writing sub-dispatcher. Session mount pick stays in 01.

### Three exits (A 05)

After 03 returns candidates (or when none exist):

#### A. Accept
Candidate design / population / effect actually support the claim → keep claim strength; cite per `citation-and-language.md` (new `[n]` = max existing + 1, unused).

#### B. Weaken
Evidence is associative or partial → lower the verb/hedge (e.g. *causes* → *has been associated with*); cite only what remains true.

#### C. Delete
Cannot support even a weakened form safely → remove the claim (word/sentence unit); do not pad with a vaguely related paper.

Never keep a strong claim because a “nearby” paper looks topical.

### Hand-off to G-LIT

If verify still fails after one search pass, comment with **both**:

1. Revise/weaken/delete the sentence now  
2. Keep the sentence and ask whether 00 should call `03_research` (Victor) again for substitute refs  

No invented PMID/DOI. User decides which plan when both remain open.

### Out of scope

- Upgrading base into a personal writing orchestrator or Evidence QC home  
- Hard-wiring external review packs under A05 every run  
- New coarse ids or `ocms-*` writing mounts  
- Letting any backup become default


---

### Part B — Intro/Discussion evidence

## Introduction / Discussion evidence

**Owner:** `05_manuscript` / `manuscript-core`. Purpose: consume verified evidence so this manuscript's Introduction and Discussion can be written. 05 does not run a literature-research route. Retrieval, guideline lookup, and full-text checks belong to `03_research`; 选题 / 选刊 also stay in `03_research` (选刊 is not a 05 task; `find-journal` routes to 03; journal formatting is `write-paper`; not 01).

Gap discovery from mounted packs → `05_manuscript/personal/process/evidence.md` (Part A) (A 05 judges; 03 searches).

Quotas and IMRAD locks live only in `Aitor-format.md` (do not copy): Intro 800–1000 words, 10–15 refs, last paragraph no citations; Discussion 800–1000 words, 10–15 **new** refs (no overlap with Intro), first paragraph no citations and no result numbers; Methods no citations. Scoring: `05_manuscript/qc/manuscript-local-qc.md`.

### When to load

写引言 · 写讨论 · 补文献 · 核对引用 · 这篇前言/讨论文献不够

### Introduction workflow (03 handoff)

1. **Endpoint frame (05).** Write the endpoint name once, exactly as Methods (Outcomes) will name it. Note whether it equals a guideline construct or is an operational surrogate of one.
2. **Raise cards (05 → 03)** per `05_manuscript/personal/process/evidence.md` (Part A): `guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`. One card set per endpoint.
3. **Evidence Pack (03 → 05).** 03 returns the table below plus a search log. 03 does not touch manuscript wording.
4. **Decide (A 05).** Accept / Weaken / Delete each row. Draft elements 2–5 only after every card has an exit.
5. **Budget references before drafting.** Select at most 15 rows. Rank: guideline > systematic review or meta-analysis > multicenter study > single-center study. Assign each row to Intro or Discussion, not both. If more than 15 remain, drop by rank and record why.
6. **Draft** with `Aitor-format.md` + `polisher-sections.md` §2.
7. **Verify (03).** Ledger at the level required below; retraction and correction check on every reference.
8. **Score.** `05_manuscript/qc/manuscript-local-qc.md`, by a scorer independent of the drafter.

```text
Claim | Source (PMID/DOI) | Class | Design · n · effect | Strength | Weakness relevant to this study | Level (L1-L3) | Intro or Discussion | Keep?
```

Class: `guideline`, `mri_accuracy` (or the modality's accuracy class), `radiomics_endpoint`, `habitat_or_nearest`, `background`.

### Guideline rule

The Introduction uses the latest edition of the guideline that defines the endpoint or the decision. 03 confirms in the same session that no newer edition exists and records body, year, and where the definition sits (section, figure, or table). The gap is mined from what the guideline leaves open. If the study endpoint is an operational surrogate of the guideline construct, element 2 states the construct and element 6 names the study endpoint in one clause; algorithm details stay in Methods.

### Verification levels

- **L1** metadata resolves (title, authors, journal, DOI).
- **L2** numbers checked against the abstract or the full text.
- **L3** full text read. Required for guideline definitions, for any appraisal of strength or weakness, and for comparative claims.

Numbers in the Introduction need L2 or higher. Record the level in the Word comment whenever it is below L3. A reference that fails verification, or that has no retraction check, is a G-LIT case (`05_manuscript/personal/process/evidence.md` (Part A)).

### Claim coverage (replaces a sentence-count gate)

Every literature claim is covered by a citation in its own sentence or by the same-source group it sits in. Reasoning sentences may stand uncited; word them as inference. The sentence-level uncited share is reported, not gated.

### QC (before the section is done)

- Elements 1–6 present; element 2 names guideline body, year, and the decision it supports
- One or two appraisal sentences, tied to this study's design
- Last paragraph: aim and hypothesis, **no** citations, endpoint name identical to Methods
- Reporting standards not named in the Introduction
- Intro vs Discussion reference lists do not overlap
- New writing: within 10–15 / 10–15 new. Checking an already-written manuscript: do **not** delete genuine refs to hit quota; note over-quota only
- Scarcity claims backed by a logged search
- Discussion first paragraph: **no** citations, **no** result numbers
- Methods still citation-free
- Page/year/author checked when the user asks to 核对 (verify citations)

Scarcity checks use PubMed plus one other source; they are not a systematic sweep. Do not run Embase+Cochrane by default. Do not generate PRISMA or AI schematics.
