# Review Resolution protocol (thin)

**Owner:** `06_review` personal. Final judgment on whether a review issue is truly fixed lives here (eight-section review / response voice). **Not** a B06 upgrade and **not** an A06 permanent three-engine dispatcher.

**Loop (lab):**

```text
Mounted review source (this-run pick: B / ARS / MedSci / Scientific / OpenClaw)
  → findings (optional status draft)
  → A 06 personal: integrate / eight-section or response letter / resolution status
  → conflicts stay in comments; user decides
  → wording → 05; stats/figures → 04; evidence gap → Evidence Request → 03
  → 00 G-06 / G-LIT
```

Mount packs **propose** findings. They do **not** free-collaborate with each other, do not own Ying Li review voice, and do not silently close an issue. A 06 **judges** Resolved / Partially resolved / Unresolved / New issue. 00 owns cross-skill QC and whether to re-invoke siblings.

Related: English peer-review envelope `personal-review-style.md`; response letter voice `personal-response-style.md`; claim gaps while writing `05_manuscript/personal/evidence-request.md`.

## When to use

- `response` mode: after author revisions, verify each reviewer point was actually addressed  
- `pre-review` / re-audit: reopen prior Major/Minor items and set status  
- Mounted `06-review-*` (or backup source) returns findings that need consolidation under A 06  

Do **not** use this file to invent rescue experiments, missing AUCs, or unrun analyses. Undecidable items → ask the user (reference-only sentence drafts OK; no silent manuscript edit).

## Issue card (required)

One card per atomic reviewer/pre-review point. Word comment author field stays **A**. Prefix the discoverer when a mount raised it; dual-tag with `[A:personal]` when A 06 also judges.

```text
Review Issue
────────────
issue_id: <R-001>
severity: <blocking | major | minor>
original_problem: <short>
domain: <stats | design | imaging | writing | refs | other>
source: <mount id or A:personal>
claimed_fix: <what the author/revision says was done>
checks:
  - methods_text: <yes|no|na>
  - results_numbers: <yes|no|na>
  - tables_figures: <yes|no|na>
  - conclusions_aligned: <yes|no|na>
status: <resolved | partially_resolved | unresolved | new_issue>
next: <close | weaken_claim | ask_user | call_04 | call_05 | evidence_request | reschedule_mount>
```

`status` is set only by **A 06 personal** after the checks. Mount drafts are suggestions.

## Roles

| Step | Who | May | Must not |
|---|---|---|---|
| Discover finding | Mounted pack (this-run) or A 06 | Raise/fill draft card | Cross-talk with other mounts; apply lab-rule conflicts silently |
| Route siblings | `00_orchestrator` | Call 02/03/04/05 when handoff says so | Treat 06 as manuscript writer |
| Judge resolution | **A 06 personal** | Set status; draft response / re-review text | Put “personal review intelligence” into B; auto-mount backup sources |
| Session mounts | 01 pick | Attach B / ARS / MedSci / Scientific / OpenClaw for this run | Permanent A06 three-pack sub-dispatcher; fixed Reviewer A/B/C pipeline |

A06 stays the review/response **entry** and personal upper layer. Capability labels for mounts stay on `01_skill-discovery-integration/mounts/*.md` — do not fork a second A06-only registry of full skill texts.

## Resolution checklist (A 06)

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

## Three exits when not resolved

### A. Ask user / keep open
Need data, ethics, or unrun analysis → question the user; optional reference-only sentence; no silent edit.

### B. Call sibling
Wording → 05 (word/sentence). Numbers/figures → 04. Prep/imaging verify → 02. Literature fact → Evidence Request → 03 (not a second lit route inside 06).

### C. Reschedule mount (rare)
Only if this-run pick left a needed pack unloaded — go through **01 session-mount pick** again; never auto-mount a non-B source.

## Out of scope

- B06 as “Review Intelligence Core” or resolution home  
- A06 as always-on ARS+MedSci+Scientific dispatcher  
- Fixed Reviewer A→B→C personas  
- Mount packs writing free-form Word comments without status cards when this protocol is in use  
- OpenClaw (or any backup) becoming a standing fourth reviewer
