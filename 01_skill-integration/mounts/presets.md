# Mount presets（v4）

Session recipes. **Fine ids** are the pick unit. Still ask-each-run.
Presets must match `registry.yaml` source / path / MOUNTED|PROPOSED.

## review-hybrid-default

Machine core: [`presets/review-hybrid.yaml`](presets/review-hybrid.yaml) (`2026-10-17.3`).

- B chassis required
- `verify-refs` → B `03-research/verify-refs/` (MOUNTED; absorbed round 3)
- `analyze-stats` → B `04-analysis/stats-guide/` (MOUNTED)
- Force B: `peer-review` (covers former peer-review-pdf-scan), `revise`, `self-review` (covers former scientific-critical-thinking)
- Catalog backups offered: MedSci / Scientific / AIPOCH / Nature only (no other packs in session pick)

Attribution: `[Source:pack-skill]` per skill, not whole source.


<!-- legacy notes may follow in git history -->

## evidence-deep-L2

Machine core: [`presets/evidence-deep-L2.yaml`](presets/evidence-deep-L2.yaml).

- B chassis + A03 evidence entry
- B/MOUNTED `lit-search` (discovery) + `verify-refs`（`paper-lookup` archived 2026-10-17 round 1）
- Optional full-text path when user asks (bulk full-text is archived; do not revive without ask)
- Still ask-each-run. Prefer verify-refs over a second search engine.

## manuscript-final-W2

Default writing recipe (pre-check on 写稿/润色/修订论著; still ask-each-run). B chassis.

Machine core: [`presets/manuscript-final-W2.yaml`](presets/manuscript-final-W2.yaml).

- Evidence already in A03 cards; 04 results fixed
- `write-paper` (structure) + A/B05 personal (sentence authority / Intro v3 / de-AI)
- `verify-refs` + `check-reporting` as QC — not second authors
- Nature venue overlays only when target journal needs them

## external-review-R1

Machine core: [`presets/external-review-R1.yaml`](presets/external-review-R1.yaml) (`2026-10-17.3`).

- B/MedSci `peer-review` + `self-review` (covers former scientific-critical-thinking) — **A06 adjudicates**
- Findings only; no direct manuscript edits by engines
- Closely related to `review-hybrid-default`; R1 emphasizes dual finding sets before personal envelope

## A/B top-layer (2026-10-17)

Flow: B fine-ID first-pass -> 00 QC -> A re-loops. Response final authority is A07 (`07_response`); revise/tighten-response/response-tone-polisher stay source=B. verify-refs / retraction-watcher may be A03-triggered post-QC (bodies in B).
