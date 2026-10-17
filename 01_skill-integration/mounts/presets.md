# Mount presets — first-pass fine-ID lists

Session recipes. **Fine ids** are the pick unit (not “which package”).
Still ask-each-run. Chassis = `my-skills-base` only.

Presets must match `registry.yaml` source / path / MOUNTED.

## review-hybrid-default

Machine core: [`presets/review-hybrid.yaml`](presets/review-hybrid.yaml).

First-pass fine ids: `verify-refs`, `analyze-stats`; force-B also `peer-review`, `revise`, `self-review`.
A06 personal adjudicates. Attribution: `[Source:pack-skill]` per skill.

## evidence-deep-L2

Machine core: [`presets/evidence-deep-L2.yaml`](presets/evidence-deep-L2.yaml).

First-pass fine ids: `lit-search`, `verify-refs`. A03 evidence entry. Prefer verify-refs over a second search engine.

## manuscript-final-W2

Machine core: [`presets/manuscript-final-W2.yaml`](presets/manuscript-final-W2.yaml).

First-pass fine ids: `write-paper`, `verify-refs`, `check-reporting`. A/B05 personal = sentence authority. Engines are QC, not co-authors.

## external-review-R1

Machine core: [`presets/external-review-R1.yaml`](presets/external-review-R1.yaml).

First-pass fine ids: `peer-review`, `self-review`. **A06 adjudicates.** Findings only.

## A/B top-layer (00 owns flow)

Flow: B fine-ID first-pass → 00 QC → A re-loops. Response final authority is A07 (`07_response`). A top layers are **not** registered as capability mounts.
