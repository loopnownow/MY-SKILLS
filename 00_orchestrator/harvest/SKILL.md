---
name: "harvest"
routable: false
status: internal-harvest-body
domain: "00_orchestrator"
description: "Harvest how-to extraction: authorization gate, H1-H4 triage, three buckets, evidence, intake QC, destination routing. Not closeout."
owner: "00_orchestrator/harvest/SKILL.md"
---

# harvest

Turn an authorized source into **how-to drafts**, route each draft to its one authority home, and stop there.
This body owns the harvest procedure only. Rules, the skill tree, `_Docs` and `_DataBase` each keep their own
SSOT (`{RULES}`, `{SKILLS}`, `_Docs`, `_DataBase`); harvest is not their steward.

- `extract ≠ promote`: extraction writes drafts only. Only the owner saying 「进skills」 may change live skills.
- `harvest ≠ closeout`: harvest never moves, renames, deletes, or ingests bytes. Closeout does that, separately.
- 00 keeps scheduling, routing, gates and the round review; this body holds the extraction how-to and the
  intake gates.

## 1 Run gate (before opening any source)

| Gate | Pass condition |
|---|---|
| Same-turn authorization | the owner named this round, this source, and this lane set in the current turn |
| Source in scope | `.Del` move-outs, `_library` (schema and how-to only), `_DataBase` (`_db` / `_share` / leaf readme), project or archived tree, downloads folder; each named |
| Not closeout | no byte move, rename, delete, or warehouse ingest in this run |
| No PHI / PII | no patient identifiers, identifiable images, ethics annexes, or unpublished grant / manuscript bodies |

`archived` is read-only by default: extracting from the cold store also needs the same-turn name. A lifecycle
stage never triggers harvest by itself. Source and stage authority: `{RULES}\workspace-layout.md`
「工作区关系：阶段 · 分流 · harvest · 冷库」.

## 2 Triage before extracting (H1-H4)

Owner rule: `{RULES}\My rule.md` §5.3.1. Classify the batch first; only H1 reaches extraction.

| Class | Test | Action |
|---|---|---|
| H1 reusable how-to | procedure, criterion, decision reason, trap, verification method, checklist or report shape | harvest (three buckets) |
| H2 no harvest | data tables, raw files, PHI-adjacent files, third-party source trees, build output, browser or probe profiles, one-off ledger patches, logs | never queued; move to `harvested` after the three checks |
| H3 live dependency | an active script or doc depends on the path | fix code or pointer first, then move |
| H4 project leftovers | one project's in-progress or closeout files | `_by-project/<slug>/` |

## 3 Lanes

A lane is an **existing fine id** (today 22; `{SKILLS}\00_orchestrator\registry.yaml`). Never invent a lane: one
2026-11-10 round used non-existent lanes in five of six sections and was fully reworked. One source may feed many
lanes: split by lane, never paste the whole text into every lane. Cross-cutting house rules go to that seat's
`advanced/`; pure policy goes to `{RULES}`.

## 4 Three buckets

Per lane, extract exactly three buckets (definitions: `HARVEST-STANDARD.md` §7.1):

| Bucket | What goes in |
|---|---|
| 语料库要素 (bank elements) | reusable facts, schemas, field lists, enums, named constraints, short quotable patterns |
| 过程 (process) | ordered how-to: gates, checklists, rebuild order, inputs to outputs, path pointers |
| 注意事项 (cautions) | hard bans, failure modes, PHI and ethics walls, look-alike traps |

A sentence that fits no bucket for a concrete fine id is dropped, or parked as owner-triage notes. Do not open a
fourth bucket.

## 5 Evidence

- Every round carries `evidence/` next to the body. A number or claim in a draft must be recomputable from that
  round's evidence (aggregate, delta, moves plan, gate log).
- Evidence types: 用户纠正 / 失败返工 / 成功案例 / AI假设. Success cases default into the bank; corrections and
  rework become candidates; AI hypotheses are recorded and never auto-promote.
- LLM-sourced lanes mark `evidence_type: AI假设` and `归属: Cap`, keep only what the rule is and when it breaks,
  and never invent numbers, cutoffs, citations or DOIs. Figure-derived lanes record layout parameters and criteria
  only, never the image, and cite the source DOI.
- Minimal candidate fields: evidence type / ownership (R, S, Reg, Cap, Bank) / strength (qualitative, not a score) /
  disposition / one-sentence summary. No scoring system, no leaderboard.

## 6 Intake gates (round QC)

Run these before handing the round to 00 for review:

1. Authorization recorded in the round index (who, when, source, lanes).
2. Not closeout: the round moved no bytes.
3. PHI / PII free: drafts and round files carry no patient identifiers, ethics material, or unpublished bodies.
4. Three buckets present for every lane the round claims.
5. Evidence recomputable from `evidence/`.
6. Destination assigned for every draft: rules / skills / library-level criterion / discard. Unknown stays `待定`
   and the round keeps it.

Fail any gate: return the round to extraction. 00 reviews only rounds that pass all six, and 00 still decides the
route and the close. Nothing is absorbed before that review.

## 7 Destinations

| Draft is | Destination | Gate |
|---|---|---|
| a cross-skill rule, a gate, or a hard contract | `{RULES}`, by PR | owner approves the PR; this skill only proposes |
| a reusable method for one fine id | `{SKILLS}`, as a thin digest or `bank-*.md` | owner says 「进skills」, then a PR |
| a library-shape or database criterion | `{doc_root}\STRUCTURE.md`, `{doc_root}\test`, or `_DataBase` (root note, `_db` readme) | separate write authorization |
| a data body | its own SSOT | never into harvest, skills, or rules |
| nothing reusable | discard; remaining bytes go to `harvested` | three checks, then `MOVED.tsv` |

`by-fine-id/<fine-id>.md` is the cumulative draft layer: append after a promotion, never clear it.

## 8 Round shape, and leaving the floor

```text
_Docs\skill-harvest\rounds\<YYYYMMDD><letter>-<slug>\
  HARVEST-*.md      three-bucket body
  INDEX.md          source, coverage, routing, authorization
  MANIFEST.tsv      per-item sha256 and decision
  evidence\         recomputable proof and gate logs
  tools\            reusable scan and triage scripts
```

No mirrored source tree and no snapshot: the body points at the source with `MANIFEST.tsv` relative paths.

Once a round is promoted, or judged H2, the round leaves the floor: the whole folder moves to
`{DEL}\harvested\rounds\<round>\` and `rounds\LEDGER.tsv` keeps one row (round / date / source / lanes / promote
PR / left date / `{DEL}` path / owner wording / retro). Put the recomputable evidence summary in the PR
description before the folder leaves. Only the owner clears `harvested`. `rounds\LEDGER.tsv` is created by the
first round that leaves under this body.

## 9 Self-evolution (owner habits and round QC)

- **Owner wording**: one ledger row per owner correction that changes harvest behaviour (date, owner wording,
  affected rule, round). Repeated wording becomes a proposal; a single event does not.
- **Round retro**: one ledger row per round (gap, over-abstraction, wrong lane, QC miss, candidate for a machine
  check).
- Propose at most one core behaviour change per PR; answer the four regression questions from `skills.md` §3 and
  record the change in the version row below.

## 10 Anti-regression (learned failures)

1. `sources\` is a durable park, not an empty folder: `{doc_lab_ste}`, `{doc_grants}`, `{doc_fill_protocol}` still
   point into it. Never delete the folder; re-point the aliases before any move.
2. `rounds\` is not a warehouse for promoted content; see §8.
3. Never invent a lane or a fine id.
4. Never harvest a data body, full manuscript or grant text, or PHI.
5. Never present an LLM hypothesis as lab practice.
6. No mirror snapshots, no second evolution log, no fifth knowledge base.
7. A round with no `evidence/` is not a finished round.

## 11 Pointers

- Collection standard (disk SSOT): `HARVEST-STANDARD.md` under `{doc_skill_harvest}`.
- Thin lane card: `00_orchestrator/references/text-harvest-by-fine-id.md`.
- Rules gate: `{RULES}\skills.md` §3; source and stage authority: `{RULES}\workspace-layout.md`.
- Library-shape gates: `{doc_root}\test\structure_check.py` with `{doc_root}\test\QC-REQUIREMENTS.md`; database
  criteria: `{doc_root}\test\DB-QC-STANDARD.md`.
- Task flow scheduling and the round review: 00 (`00_orchestrator/SKILL.md` §3). This body does not schedule.

## Version

- 1.0 (2026-11-14, t20261114a): first body, split out of the «Harvest task flow» section of
  `00_orchestrator/references/skill-evolution.md`; 00 keeps scheduling, gates and the round review and points here.
