# Keep · Merge · Delete · Archive

Decision rules after observation / measurement. Harvest **proposes** these outcomes; it does not apply them without explicit user approval.

## Keep

Keep when the change demonstrates benefit and preserves boundaries (see `benefit-metrics.md`).

A frequently used but error-prone rule is **not** a successful improvement — optimize for benefit per context cost, not usage count.

## Revise

Revise when the problem is real but the implementation has weak evidence, excess complexity, or boundary ambiguity. Prefer another Proposal cycle over silent patching.

## Rollback

If a change causes worse routing, more corrections, contradictory behavior, or unnecessary context cost:

1. Identify the exact change (Git commit / change_id).
2. **Propose** restore to the recorded rollback point.
3. Record why it failed; keep the failed lesson in INTEGRATION_MAP.
4. Do not silently delete evidence of the failed iteration.
5. Do not auto-patch a second evolution on top of a regression.

## Merge / SIMPLIFY

Prefer `MERGE` or `SIMPLIFY` when:

- two modes/rules overlap and one home can absorb both;
- context cost rises while success/correction metrics do not improve;
- a denser principle can replace several rules (evolution budget prefers no net length increase).

## Archive

Archive unused modules instead of deleting when recovery may be useful. Keep the path findable via route-map or INTEGRATION_MAP note.

## Delete

Delete only when:

- the material is confirmed duplicate of an authoritative home;
- it is unsafe (credentials, PHI, invented facts);
- the user explicitly approves deletion after a Proposal.

Never delete pack bytes under `mounts-cap/` as part of harvest evolution. Never wipe `STATE.yaml` to “clean” orphans — document the orphan instead.

## Anti-promotion

Before promoting a new mode, require either ≥3 independent positive uses, a reproducible failure prevented by the rule, or a defined workflow requirement. See `boundary-contract.md` promotion thresholds and `evolution-policy.md` E0–E5.
