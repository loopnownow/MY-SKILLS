# Mount presets（v4）

Session recipes. **Fine ids** are the pick unit. Still ask-each-run.

## review-hybrid-default

Machine core: [`presets/review-hybrid.yaml`](presets/review-hybrid.yaml) (`2026-09-13.1`).

- B chassis required
- Optional Nature overlays on `verify-refs` / `analyze-stats` (license 需核实 — confirm before load)
- Scientific overlay on `scientific-critical-thinking`
- Force B: `peer-review`, `peer-review-pdf-scan`, `revise`, `self-review`
- Excluded: ARS, OpenClaw

Attribution: `[Source:pack-skill]` per skill, not whole source.


<!-- legacy notes may follow in git history -->

## evidence-deep-L2

Machine core: [`presets/evidence-deep-L2.yaml`](presets/evidence-deep-L2.yaml).

- B chassis + A03 evidence entry
- Scientific `paper-lookup` (discovery) + `verify-refs` / citation-management
- Optional full-text path when user asks (do not auto-revive archived `03-lit-fulltext` without ask)
- Still ask-each-run. Prefer verify-refs over a second search engine.

## manuscript-final-W2

Default writing recipe (pre-check on 写稿/润色/修订论著; still ask-each-run). B chassis.

Machine core: [`presets/manuscript-final-W2.yaml`](presets/manuscript-final-W2.yaml).

- Evidence already in A03 cards; 04 results fixed
- `write-paper` (structure) + A/B05 personal (sentence authority / Intro v3 / de-AI)
- `verify-refs` + `check-reporting` as QC — not second authors
- Nature venue overlays only when target journal needs them

## external-review-R1

Machine core: [`presets/external-review-R1.yaml`](presets/external-review-R1.yaml).

- Scientific critical-thinking overlay + MedSci/B `peer-review` / `self-review` → **A06 adjudicates**
- Findings only; no direct manuscript edits by engines
- Closely related to `review-hybrid-default`; R1 emphasizes dual finding sets before personal envelope

