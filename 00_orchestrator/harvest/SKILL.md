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
| Source in scope | `.Del` move-outs, `_library` (schema and how-to only), `_DataBase` (`_PHI` / `__zip` / leaf readme), project or archived tree, downloads folder; each named |
| Not closeout | no byte move, rename, delete, or warehouse ingest in this run |
| No PHI / PII | no patient identifiers, identifiable images, ethics annexes, or unpublished grant / manuscript bodies. Author **Adm** comments and tracked changes may be harvested (marks only) |

`archived` is read-only by default: extracting from the cold store also needs the same-turn name. A lifecycle
stage never triggers harvest by itself. Source and stage authority: `{RULES}\zone-projects.md`
「工作区关系：阶段 · 分流 · harvest · 冷库」.

## 2 Triage before extracting (H1-H4)

Owner rule: `{RULES}\zone-docs.md` §1（H1–H4）. Classify the batch first; only H1 reaches extraction.

| Class | Test | Action |
|---|---|---|
| H1 reusable how-to | procedure, criterion, decision reason, trap, verification method, checklist or report shape | harvest (three buckets) |
| H2 no harvest | data tables, raw files, PHI-adjacent files, third-party source trees, build output, browser or probe profiles, single-use one-off patches, logs | never queued; move to `harvested` after the three checks |
| H3 live dependency | an active script or doc depends on the path | fix code or pointer first, then move |
| H4 project leftovers | one project's in-progress or closeout files | `_by-project/<slug>/` |

Repeatedly used, functionally similar one-off scripts are harvest objects (H1): extract the reusable procedure, interface and traps, and propose them to MY-CODES. Do not class them as H2 just because they were written or filed as one-offs. A truly single-use patch remains H2.

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
- Word comments and Track Changes by author **Adm** are the owner's marks and first-class harvest sources (用户纠正 / 成功案例). Extract the marks only, never the full manuscript body. Helper author **A** is not the owner.
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
| a library-shape or database criterion | `{doc_root}\STRUCTURE.md`, `{doc_root}\test`, or `_DataBase` (root note, `_PHI` readme) | separate write authorization |
| a data body | its own SSOT | never into harvest, skills, or rules |
| nothing reusable | discard; remaining bytes go to `harvested` | three checks, then `MOVED.tsv` |

`by-fine-id` notes belong only under `{DEL}` (`{RULES}\zone-docs.md` §3). Do not treat
`harvest\rounds` + `by-fine-id` as a live SSOT under `{doc_root}`.

Deposit by type (still propose-only; live `{SKILLS}` needs 「进skills」, live `{RULES}` needs a PR):

- Runnable, reusable scripts → `{code_root}\tools\<fine-id>\` (script plus that group's README). A one-off
  script stays out of the code repo: record its SHA and move it to `{DEL}` unless it has already been reused
  and is functionally similar (then it is H1, same as `{RULES}\zone-docs.md` §1).
- Cross-skill hard contracts, gates, aliases, or disk policy → `{RULES}`.
- Process how-to, criteria, and traps → `{SKILLS}`.

Decision order: if it can run, it goes to the code repo; if not, and it is a cross-skill hard constraint, it
goes to rules; otherwise it goes to skills. Do not copy tool variants: differences go through a CLI or the
`[tools]` section of `settings.ini`; keep one implementation per function.

## 8 Round shape, and leaving the floor

Round working directories live under `{DEL}`, not under `{doc_root}\harvest\`:

```text
{DEL}\harvest-park\rounds\<YYYYMMDD><letter>-<slug>\
  HARVEST-*.md      three-bucket body
  INDEX.md          source, coverage, routing, authorization
  MANIFEST.tsv      per-item sha256 and decision
  evidence\         recomputable proof and gate logs
  tools\            optional reusable scan and triage scripts
```

The collection standard stays at `{doc_root}\harvest\HARVEST-STANDARD.md`. The durable ledger is
`{doc_root}\harvest\LEDGER.tsv` (one row per round). Do not create `{doc_root}\harvest\rounds\` or
`{doc_root}\harvest\<lane>\` as a live working layer.

No mirrored source tree and no snapshot: the body points at the source with `MANIFEST.tsv` relative paths.
An H3 batch that a live report, handoff, or rule still cites by literal path is not moved; `MANIFEST.tsv`
records `keep_due_to`. A batch already promoted is not harvested again: add a ledger row and an
「已 promote」destination only.

Once a round is promoted, or judged H2, the whole folder moves to `{DEL}\harvested\rounds\<round>\` and
`{doc_root}\harvest\LEDGER.tsv` keeps one row (round / date / source / lanes / promote PR / left date /
`{DEL}` path / owner wording / retro). Put the recomputable evidence summary in the PR description before
the folder leaves. After the content has entered rules or skills, the owner may delete these round
directories. Only the owner clears `{DEL}`; the executor must not empty it. PHI / PII, name lists, image
binaries, HIS scrape scripts, and unpublished full texts are H2: leave a decision row in `MANIFEST.tsv`,
do not extract them.

The previous machine half of the old live-floor shape is `{doc_root}\test\structure_check.py` S29
(`harvest-rounds`). That gate still has to be realigned to this `{DEL}` working-directory policy; until then
do not treat S29 as proof that a `{doc_root}\harvest\rounds\` live floor is required.

## 9 Self-evolution (owner habits and round QC)

- **Owner wording**: one ledger row per owner correction that changes harvest behaviour (date, owner wording,
  affected rule, round). Repeated wording becomes a proposal; a single event does not.
- **Round retro**: the `retro` column of the round's `rounds\LEDGER.tsv` row is filled before the folder leaves
  the floor (gap, over-abstraction, wrong lane, QC miss, candidate for a machine check). A retro is written for
  the next owner reading the ledger, not for the current round.
- **QC feeding back**: a miss that a script can decide becomes a gate in `{doc_root}\test\structure_check.py` plus a
  `**SNN**` row in `{doc_root}\test\QC-REQUIREMENTS.md` with the incident it prevents; a miss that needs judgement stays a manual
  gate. First instance: S29 `harvest-rounds`, 2026-11-14, prevents promoted rounds and dead round pointers from
  coming back into the live floor.
- Propose at most one core behaviour change per PR; answer the four regression questions from `skills.md` §3 and
  record the change in the version row below.

## 10 Anti-regression (learned failures)

1. `sources\` is a durable park, not an empty folder: `{doc_lab_ste}`, `{doc_grants}`, `{doc_fill_protocol}` still
   point into it. Never delete the folder; re-point the aliases before any move.
2. Round directories are not a live SSOT under `{doc_root}\harvest`; see §8.
3. Never invent a lane or a fine id.
4. Never harvest a data body, full manuscript or grant text, or PHI. Author **Adm** comments and tracked changes are marks, not the body.
5. Never present an LLM hypothesis as lab practice.
6. No mirror snapshots, no second evolution log, no fifth knowledge base.
7. A round with no `evidence/` is not a finished round.

## 11 Pointers

- Collection standard (disk SSOT): `HARVEST-STANDARD.md` under `{doc_skill_harvest}`.
- Thin lane card: `00_orchestrator/references/text-harvest-by-fine-id.md` (notes only; the files themselves land in `{DEL}`).
- Rules gate: `{RULES}\skills.md` §3 and `{RULES}\zone-docs.md` §3; source and stage authority: `{RULES}\zone-projects.md` 「工作区关系：阶段 · 分流 · harvest · 冷库」.
- Library-shape gates: `{doc_root}\test\structure_check.py` with `{doc_root}\test\QC-REQUIREMENTS.md`; database
  criteria: `{doc_root}\test\DB-QC-STANDARD.md`. Durable ledger: `{doc_root}\harvest\LEDGER.tsv`. S29 still
  describes an older live-floor layout and needs a follow-up in `_Docs`.
- Task flow scheduling and the round review: 00 (`00_orchestrator/SKILL.md` §3). This body does not schedule.

## Version

- 1.0 (2026-11-14, t20261114a): first body, split out of the «Harvest task flow» section of
  `00_orchestrator/references/skill-evolution.md`; 00 keeps scheduling, gates and the round review and points here.
- 1.1 (2026-11-14, t20261114c): round shape and exit consistency become the machine gate S29 in
  `_Docs\test\structure_check.py`; the round retro is the `rounds\LEDGER.tsv` retro column; QC misses that a
  script can decide become gates, judgement misses stay manual.
- 1.2 (2026-11-15, t2073u): author **A** Word comments and tracked changes are the owner's marks and first-class harvest sources; extract marks only, never the full body.
- 1.3 (2026-11-19, t155u): the owner's Word author mark is **Adm**, not **A** (corrects 1.2 / t2073u); harvest Adm revisions and comments (marks only). Helper comments/TC remain author **A**.
- 1.4 (2026-11-19, t2154u): repeatedly used, functionally similar one-off scripts are harvest objects (H1); single-use patches remain H2.
- 1.5: round working directories move to `{DEL}`; `harvest\rounds` + `by-fine-id` is not a live SSOT under `{doc_root}`; three-way deposit to skills / rules / code; after promote, the owner may delete the round folder.
