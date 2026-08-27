# Guardrails — overclaiming, causation, hedging

Flag (don't silently rewrite away) claims that exceed the evidence; propose calibrated
wording.

## Overclaim patterns to flag
- **Absolutes**: "accurate," "proves," "eliminates," "always/never" → soften to the measured
  performance with its CI.
- **Unverified novelty**: "first to," "unprecedented" → remove unless verifiable;
  replace with the concrete contribution. **"Novel" itself is not banned** — it's
  corpus-verified (59 occurrences in the deduplicated manuscript corpus) as a normal,
  sparingly-used word when the novelty claim is actually verifiable (e.g. describing a
  genuinely new procedure). Flag "novel" only when the claim behind it is *unverified*,
  not on sight. See `../../corpus/corpus-phrase-bank.md` §8.
- **Scope creep**: single-center retrospective result → "clinically ready," "should be
  adopted." Bound to the evidence and call for validation.
- **Reader/▢ comparison without statistic**: "outperformed radiologists" → give the
  difference + CI + test.

## Causation vs association (critical for radiogenomics)
- Observational/correlational designs support **association**, not causation. Flag
  "causes/drives/leads to/because" when the design can't support it.
- Calibrate: `is associated with` / `correlated with` / `reflects` (associative) vs
  `causes` / `results in` (causal — needs intervention/mechanism).

## Hedging calibration (verb ladder)
`demonstrate / show` (direct evidence) → `indicate / suggest` (associative) →
`may / might / could reflect` (speculative). Over-hedging a solid result is also a flaw —
match the verb to the evidence, both directions.

## Forbidden / discouraged
- "P = NS," "trend toward significance" (report the exact P and CI; let the reader judge).
- "Significant" used colloquially (reserve for statistical significance, with the test).
- Implying clinical deployment from a non-prospective, non-externally-validated study.
- Mechanism asserted from a correlation.

## Output
List each flag as: `Claim (quoted) | Why it exceeds evidence | Calibrated alternative`. The
author decides; the skill never invents the supporting evidence.
