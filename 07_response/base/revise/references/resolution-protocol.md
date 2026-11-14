# Review resolution protocol (thin)

Issue status and ownership for a review round. Moved out of `07_response/advanced/response.md` on 2026-11-14: the letter voice, opener templates and phrase banks stay in the advanced file; this base file states the bot map, issue card, roles, resolution checklist, three exits and out-of-scope list. Gate ids G-P1..G-P3 stay in the revise contract.

## Review Resolution protocol (thin)

**Bot map:** response upper layer (07) → **Lee** (`07_response`); re-review Lee (`06_review`); literature substitute search if needed → **Victor** (`03`); manuscript Track Changes → **Aitee** (`05`). Ownership: see `00_orchestrator/references/ownership-contract.md`.

**Owner:** the response upper layer (07); letter voice stays in `07_response/advanced/response.md`. Final judgment on whether a review issue is truly fixed lives here (eight-section review / response voice). **Not** a B06 upgrade and **not** an 06 permanent three-engine dispatcher.

**Loop (lab):**

```text
Live review source (this-run pick: session fine ids from the 00 registry menu)
  → findings (optional status draft)
  → A 06 advanced: post-QC re-review integrate / eight-section
  → A 07 advanced: response letter / resolution status (final authority)
  → conflicts stay in comments; user decides
  → wording → 05; stats/figures → 02; evidence gap → Evidence Request → 03
  → 00 G-06 / G-LIT
```

Specialist packs **propose** findings. They do **not** free-collaborate with each other, do not own Aitor review voice, and do not silently close an issue. A **07** **judges** Resolved / Partially resolved / Unresolved / New issue. 00 owns cross-skill QC and whether to re-invoke siblings.

Related: English peer-review envelope `06_review/advanced/review.md`; response letter voice this file; claim gaps while writing `05_manuscript/advanced/process/evidence.md`.

Disk bank (external reviewer comments and revise replies; pointer only): `{doc_glossary}\banks\` (`flattened.jsonl`, `FLATTENED.tsv`, `review-text.jsonl`).

### When to use

- `response` mode: after author revisions, verify each reviewer point was actually addressed
- `pre-review` / re-audit: reopen prior Major/Minor items and set status
- Live `peer-review` / `self-review` / `revise` (or backup source) returns findings that need consolidation under A 06

Do **not** use this file to invent rescue experiments, missing AUCs, or unrun analyses. Ownership: see `00_orchestrator/references/ownership-contract.md`. Ask the user on undecidable items; do not edit the manuscript until the user picks, and then Aitee applies Track Changes.

### Issue card (required)

One card per atomic reviewer/pre-review point. Word comment author field stays **A**. Prefix the discoverer when a fine id raised it; dual-tag with `[advanced]` when 06 also judges.

```text
Review Issue
────────────
issue_id: <R-001>
severity: <blocking | major | minor>
original_problem: <short>
domain: <stats | design | imaging | writing | refs | other>
source: <fine id or A:advanced>
claimed_fix: <what the author/revision says was done>
checks:
  - methods_text: <yes|no|na>
  - results_numbers: <yes|no|na>
  - tables_figures: <yes|no|na>
  - conclusions_aligned: <yes|no|na>
status: <resolved | partially_resolved | unresolved | new_issue>
next: <close | weaken_claim | ask_user | call_04 | call_05 | evidence_request | reschedule_fine_id>
```

`status` is set only by **A 06 advanced** after the checks. Live drafts are suggestions.

### Roles

| Step | Who | May | Must not |
|---|---|---|---|
| Discover finding | Live pack (this-run) or A 06 | Raise/fill draft card | Cross-talk with other fine ids; apply lab-rule conflicts silently |
| Route siblings | `00_orchestrator` | Call 02/03/05 when handoff says so | Treat 06 as manuscript writer |
| Judge resolution | **A 06 advanced** | Set status; draft response / re-review text | Put “advanced review intelligence” into B; auto-add backup sources |
| Session fine ids | 00 pick | Attach this-run registry fine ids for review sources | Fixed Reviewer A/B/C pipeline via 06 fine ids |

06 stays the review/response **entry** and advanced upper layer. Capability labels / fine ids stay on `00_orchestrator/registry.yaml` — do not fork a second 06-only registry of full skill texts.

### Resolution checklist (A 06)

For each issue, do not stop at “author added a sentence.” Prefer:

1. Was the **method** actually changed (or a justified refusal documented)?
2. Do **Results / Tables / Figures** match the claimed fix (e.g. adjusted *P*, new CI)?
3. Does the **conclusion / abstract** still depend on the pre-fix claim?
4. Did the fix create a **new_issue**?

Then set one status:

| Status | Meaning |
|---|---|
| `resolved` | Checks pass; safe to close in the response letter |
| `partially_resolved` | Something fixed, residual risk remains → keep open + `next` |
| `unresolved` | Claimed fix missing or cosmetic only |
| `new_issue` | Revision introduced a new defect |

### Three exits when not resolved

#### A. Ask user / keep open
Need data, ethics, or unrun analysis → question the user; optional reference-only sentence; no silent edit.

#### B. Call sibling
Wording → 05 (word/sentence). Even a decidable wording fix stays a comment for Aitee to TC-fix. Lee does not edit the body by default. Numbers/figures → 02. Prep/imaging verify → 02. Literature fact → Evidence Request → 03 (not a second lit route inside 06). Victor supplies suggested literature for comments when needed.

#### C. Reschedule fine id (rare)
Only if this-run pick left a needed pack unloaded — go through the **00 session-fine-id pick** again; never auto-add a non-base source.

### Out of scope

- B06 as “Review Intelligence Core” or resolution home
- 06 as always-on multi-source review dispatcher
- Fixed Reviewer A→B→C personas
- Specialist packs writing free-form Word comments without status cards when this protocol is in use
- Any backup becoming a standing fourth reviewer

### Bank reply skeletons (2026-10-23)

Frequency evidence + per-point skeleton: `07_response/advanced/references/bank-reply-skeletons.md`.
Standing letter opener remains authoritative in `07_response/advanced/response.md`: **Thank you for your comments** | **suggestions** | **inquiry**.

