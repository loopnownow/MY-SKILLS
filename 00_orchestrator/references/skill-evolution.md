# Skill evolution (propose only)

Applies to skills 00–07. Never edit live skill bodies directly; post-merge deploy sync is the only write path (Rules `skills.md` §1b).

**Harvest task flow** (section «Harvest task flow» below) is owned by **00_orchestrator**; collection-standard SSOT is `{doc_skill_harvest}\HARVEST-STANDARD.md`. Do **not** add a top-level evolution skill / evolution agent / 5th knowledge base. Do not vendor `_code` / `0doc` trees.

## Evidence

- Default evidence level **E4** = the same class of user correction repeated. A single event never evolves a skill.
- Priority: user edits the deliverable > explicit correction > named issue > observation > self-review.

## Keep or skip

- Keep only if ALL: repeated or locked; used in a future project; methodology / naming / layout / validation / hygiene (not n / AUC / ethics IDs); no other SSOT.
- Skip: one-off path; SSOT duplicate; vendor production script; long human profile (pointer only); taste; single-project numbers or IDs.
- Absorb external packs into an existing layer. Do not open a new top level for a disease, organ, package, section, statistical test, metric, or modality. One authority home per topic.

## Budget and outcome

- Budget: at most 1 core behaviour change, at most 3 new rules, no duplicates, no unapproved boundary expansion.
- Each proposal answers: what recurrence it prevents; how effectiveness will be known.
- Outcome: keep / revise / rollback / merge·simplify / delete (delete needs explicit approval). **Do not leave `archived` labels in live prose** — Rules `skills.md` §6: at QC, delete archived shells/refs (or move bytes to `{DEL}`); retired names stay only as `legacy_aliases.yaml` redirects.
- Rollback restores a recorded git point; do not stack a second evolution on a regression.

---

## Harvest task flow (owned by 00)

Owner (2026-10-24): harvest also updates the task flow; skill-00 owns it and turns it into a collection standard.

**Layers (keep; do not open a parallel tree)**

| Layer | Meaning | Physical home |
|---|---|---|
| Rules (R) | Cross-skill hard contracts | MY-RULES |
| Skills (S) | 00–07 skill bodies / personal | MY-SKILLS |
| Registry (Reg) | fine-ID / fine-id registry | `00_orchestrator/registry.yaml` etc. |
| Capabilities (Cap) | Live capability packs | MY-SKILLS `NN_slug/base/` + registry (**no** separate capabilities clone) |
| Corpus | Corpus / harvest drafts | `{doc_root}\skill-harvest\` (SSOT); `{DEL}` = working copy |

**Hard gates**

- **Extract ≠ promote**: extraction writes only corpus / candidates; only **「进skills」 (promote into live skills)** may change runtime.
- Corpus update ≠ runtime update; runtime changes only via MY-SKILLS PR → merge → `git pull` on the live clone (Rules `skills.md` §1b).
- **No scoring system**; candidates record minimal fields only.

### Steps

```text
1 Evidence intake
      │  Format = collection standard HARVEST-STANDARD (fine-ID three buckets + candidate fields)
      ▼
2 Evidence type
      │  user correction | failure rework | success case | AI hypothesis
      ▼
3 Ownership
      │  R / S / Reg / Cap / Corpus
      ▼
4 Candidate record
      │  Minimal fields; land in corpus; do not change live
      ▼
5 Human gate
      │  城城 says 「进skills」 (or equivalent explicit approval)
      ▼
6 Scoped change
      │  Change one place by ownership; respect budget; risk-tiered
      ▼
7 Regression four questions
      │  All yes before merge
      ▼
8 Promote or rollback
```

### 1–2 Evidence intake and types

| Evidence type | Default disposition | Auto-change runtime? |
|---|---|---|
| User correction | Candidate → await 「进skills」 | No |
| Failure rework | Candidate → await 「进skills」 | No |
| Success case | **Default into Corpus** (may later candidate for promote) | No |
| AI hypothesis | Record candidate / note only; **never** auto-change runtime | No |

Intake format pointer: collection standard `HARVEST-STANDARD.md` (fine-ID: **corpus elements / process / cautions**; candidate fields attached, do not replace the three buckets).

### 3–4 Ownership and minimal candidate fields

Candidate records (corpus side) at least include:

| Field | Notes |
|---|---|
| Evidence type | user correction / failure rework / success case / AI hypothesis |
| Ownership | R / S / Reg / Cap / Corpus |
| Strength | low / mid / high (qualitative; not a score) |
| Disposition | corpus-only / awaiting approval / promoted / rejected / rolled back |
| Summary | one sentence; may attach fine-ID / path pointer |

Optional: `source`, `date`, `fine_id`, `risk_tier`. No scores, no leaderboards.

### 5–6 Approval and scoped change · risk tiers

| Risk tier | Examples | Gate |
|---|---|---|
| content | corpus draft, personal `corpus-*.md` addenda | 「进skills」 + budget |
| merge | edit existing skill body / merge PR | checklist + user agree to merge |
| registry/ID | registry, fine-ID, fine-id map | explicit approval; never silently change IDs |
| Rules | MY-RULES | highest gate; propose-only; explicit approval |

Cap changes = edit `base/` and/or registry; do **not** create a capabilities repo.

### 7 Regression four questions

Before merge, answer in writing (PR description is fine):

1. **Recurrence prevented**: which class of repeated failure / correction does this block?
2. **Observable**: after merge, how will we know it works (one failure replay or checkpoint is enough)?
3. **SSOT**: does it duplicate or steal another layer’s authority? Is the authority home unique?
4. **Budget and boundary**: ≤1 core behaviour change, ≤3 new rules, no unapproved boundary expansion?

Any “no” → do not promote; fall back to corpus-only or revise the candidate.

### 8 Promote / rollback

- Promote: open/update PR by ownership → full change list → merge → live clone `git pull`.
- Rollback: restore a recorded git point; **do not** stack a second evolution on a regression.
- delete: needs explicit approval (see «Budget and outcome» above).

### Pointers

- Collection standard (SSOT): `{doc_skill_harvest}\HARVEST-STANDARD.md`
- Fine-ID thin pointer: `00_orchestrator/references/text-harvest-by-fine-id.md`
- Rules gate: `{RULES}\skills.md` §3 (propose-only; task-flow body lives in this file)
