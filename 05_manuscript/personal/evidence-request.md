# Evidence Request protocol (thin)

**Owner:** `05_manuscript` personal. Final claim/citation QC lives here (Aitor-format / overclaim rules). **Not** a literature-research route and **not** a B05 upgrade.

**Loop (lab):**

```text
Mounted pack (this-run pick: B / ARS / MedSci / Scientific / OpenClaw)
  → Evidence Request card (gap discovery only)
  → 03_research searches
  → Candidate evidence
  → A 05 personal: Accept / Weaken / Delete
  → if still insufficient → G-LIT dual plan (00 may call 03 again)
```

Mount packs **propose**; they do **not** choose the final citation or keep an over-strong verb. 03 **searches** only. A 05 **judges** whether a candidate supports the claim. 00 owns whether to invoke 03 again (G-LIT).

Related: consume verified I/D rows via `intro-discussion-evidence.md`; quotas in `Aitor-format.md`; citation mechanics in `citation-and-language.md`.

## When to raise a card

- A mounted writing/review skill flags a claim with missing, associative-only, wrong-population, or second-hand-only support
- 05/06 literature verify fails on a factual sentence that still needs a source
- User asks to 补文献 / 核对引用 for a specific sentence (not “search the topic”)

Do **not** use this file for 选题 / 选刊 / systematic review / Embase+Cochrane default sweeps.

## Card fields (required)

Copy into a Word comment (author **A**) and/or handoff note. Prefix the discoverer when a mount raised it (`[ARS:…]` / `[MedSci:…]` / `[Scientific:…]` / `[OpenClaw:…]` / `[B:…]`); dual-tag with `[A:personal]` when A 05 also judges.

```text
Evidence Request
────────────────
Claim: <exact sentence or claim atom>
Problem: <missing | associative_only | wrong_population | second_hand | contradictory | overclaim>
Required: <what would count as adequate support>
Section: <Intro | Discussion | other>
Source: <mount id or A:personal>
Status: open
```

Optional: `PMID/DOI candidates` (only if already verified; never invent).

## Roles

| Step | Who | May | Must not |
|---|---|---|---|
| Discover gap | Mounted pack (this-run) or A 05/06 | Raise card | Pick final ref; rewrite whole paragraph; auto-mount another source |
| Search | `03_research` only | PubMed / DOI verify; return candidates | Change manuscript wording; invent PMID/DOI |
| Judge | **A 05 personal** | Accept / Weaken / Delete (below) | Treat mount suggestion as silent apply; run a second lit-research route inside 05 |
| Re-invoke 03 | `00_orchestrator` (G-LIT) | Call 03 after dual-plan comment | Skip dual plan; invent citations |

A05 stays the writing skill entry / personal upper layer. It is **not** a permanent three-pack writing sub-dispatcher. Session mount pick stays in 01.

## Three exits (A 05)

After 03 returns candidates (or when none exist):

### A. Accept
Candidate design / population / effect actually support the claim → keep claim strength; cite per `citation-and-language.md` (new `[n]` = max existing + 1, unused).

### B. Weaken
Evidence is associative or partial → lower the verb/hedge (e.g. *causes* → *has been associated with*); cite only what remains true.

### C. Delete
Cannot support even a weakened form safely → remove the claim (word/sentence unit); do not pad with a vaguely related paper.

Never keep a strong claim because a “nearby” paper looks topical.

## Hand-off to G-LIT

If verify still fails after one search pass, comment with **both**:

1. Revise/weaken/delete the sentence now  
2. Keep the sentence and ask whether 00 should call `03_research` again for substitute refs  

No invented PMID/DOI. User decides which plan when both remain open.

## Out of scope

- Upgrading B into a personal writing orchestrator or Evidence QC home  
- Hard-wiring ARS + MedSci + Scientific under A05 every run  
- New coarse ids or `ocms-*` writing mounts  
- Letting OpenClaw (or any backup) become default
