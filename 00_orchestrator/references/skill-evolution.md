# Skill evolution (propose only)

Authoring punctuation (owner t1683u / t1761u): en dash (U+2013) is **allowed** in skill prose, typically for numeric ranges, CIs and page spans (`0.80–0.93`, `5–10 mm`); Unicode minus (U+2212, `−`) is **allowed** for signed numbers / difference spans (`−0.32`, `Q3−Q1`); ASCII hyphen `-` remains fine, so none of these forms is required. Em-dash (U+2014 / spaced `--`) stays banned (prefer parentheses); `≈` stays banned. En-dash ban reverse: 2026-10-30 → t1683u 2026-11-06; minus allow: t1761u 2026-11-07.

Applies to skills 00-07. Never edit live skill bodies directly; post-merge deploy sync is the only write path (Rules `{RULES}\skills.md` §1b).

**Harvest task flow** is owned by the **harvest** pack (`00_orchestrator/harvest/SKILL.md`); the collection-standard SSOT is `{doc_skill_harvest}\HARVEST-STANDARD.md`. Do **not** add a top-level evolution skill / evolution agent / 5th knowledge base. Do not vendor `_code` / `_Docs` trees.

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
- Outcome: keep / revise / rollback / merge·simplify / delete (delete needs explicit approval). **Do not leave `archived` labels in live prose** — Rules `{RULES}\skills.md` §6: at QC, merge what can merge, delete what can delete (bytes to `{DEL}`), dedupe, drop stale, keep lean; delete archived shells/refs; retired names stay only as `legacy_aliases.yaml` redirects.
- Rollback restores a recorded git point; do not stack a second evolution on a regression.

---

## Harvest task flow

Procedure body and intake gates: `00_orchestrator/harvest/SKILL.md`. This file keeps only the evolution contract;
do not restate the harvest steps here.

## Pointers

- Harvest task flow: `00_orchestrator/harvest/SKILL.md` (extract ≠ promote; harvest ≠ closeout)
- Collection standard: `{doc_skill_harvest}\HARVEST-STANDARD.md`
- Rules gate: `{RULES}\skills.md` §3
- Fine-id lane card: `00_orchestrator/references/text-harvest-by-fine-id.md`
