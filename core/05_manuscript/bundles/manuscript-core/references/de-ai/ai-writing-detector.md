# AI writing detection / humanization (optional deep mode)

**Canonical entry:** `../../MODULE.md` (manuscript-core).
Trigger only when user asks to detect AI probability, humanize for detectors, or lower AI score.

## Lab academic protocol (overrides casual humanization)

- Preserve all statistics and citations exactly.
- No colloquial injection in manuscripts.
- Structural variation only (clause split/merge, rhythm).
- After rewrite, re-apply manuscript-core house style (forbidden fluff, hedging calibration).
- Ethical disclaimer remains mandatory on detection/humanization outputs.

---

# AI Writing Detection & Humanization Expert Skill

## Overview

This skill performs multi-dimensional AI writing fingerprint analysis and, optionally, structured
humanization rewriting. It combines syntactic, lexical, semantic, and model-specific signature
detection to produce a standardized detection report, then offers an optional rewrite pipeline
that drops detection scores below 10% across common detectors (GPTZero, Turnitin, Copyleaks, etc.).

---

## Execution Pipeline

### Step 1 — Fingerprint Scanning (Multi-dimensional Scoring 0–100%)

Analyze the input text across the following five dimensions. Assign a weighted sub-score to each,
then compute an aggregate AI Probability Score.

#### 1.1 Syntax / Sentence Structure
- Overuse of em-dashes (—) → strong Claude signature
- Passive voice density above ~35%
- Overly complex compound sentences with balanced clausal symmetry
- Repetitive transitional phrases: "furthermore", "notably", "it is worth noting", "importantly"
- Low sentence-length variance (burstiness < 6 on standard 0–15 scale)

#### 1.2 Vocabulary & Lexical Patterns
- High-frequency academic jargon stacked within single sentences
- Repetitive sentence-opening structures across consecutive paragraphs
- Absence of burstiness: sentence length variance significantly below human baseline (target > 8)
- Synonymic variety is present but feels mechanically rotated

#### 1.3 Semantics & Discourse
- Overly perfect logical flow with no tangential asides or self-corrections
- Absence of personal perspective, hedging, or authorial stance
- Flat emotional tone; no rhythm variation between argumentative and descriptive passages
- Conclusions restate introductions too precisely

#### 1.4 Model-Specific Signatures

| Model   | Characteristic Patterns |
|---------|--------------------------|
| Claude  | Elegant extended long sentences; heavy em-dash use; polished hedging |
| GPT-4/o | Listicle tendency; "It is evident that…"; "Certainly,"; numbered sub-points in prose |
| Gemini  | Neutral highly templated responses; factual density without narrative flow |
| Llama   | Slightly uneven transitions; occasional abrupt topic shifts |

#### 1.5 Statistical / Perplexity Indicators (if tooling available)
- Low perplexity (< 20 on GPT-2 scale) flags high AI likelihood
- Low burstiness score (< 6) combined with low perplexity = high-confidence AI
- Invoke `scripts/perplexity.py` if available in the environment

---

### Step 2 — Standardized Report Output

Always produce the following structured report:

```
╔══════════════════════════════════════════════════╗
║          AI WRITING DETECTION REPORT             ║
╚══════════════════════════════════════════════════╝

[AGGREGATE AI PROBABILITY SCORE]  XX%
[ESTIMATED BURSTINESS SCORE]       X.X / 15
[MOST LIKELY SOURCE MODEL]         [Claude / GPT / Gemini / Mixed / Uncertain]
[HUMAN SIMILARITY SCORE]           X / 10

──────────────────────────────────────────────────
EVIDENCE FLAGS (Quote → Issue → Recommended Fix)
──────────────────────────────────────────────────
Evidence 1: "[original sentence]"
  └─ Issue: [fingerprint explanation]
  └─ Fix:   [brief suggestion]

Evidence 2: "[original sentence]"
  └─ Issue: [fingerprint explanation]
  └─ Fix:   [brief suggestion]

[Continue for all flagged items]

──────────────────────────────────────────────────
RECOMMENDED ACTION
──────────────────────────────────────────────────
[ ] No action needed (score < 25%)
[ ] Minor revisions suggested (score 25–60%)
[ ] Full humanization recommended (score > 60%)

Would you like me to proceed with humanization? (yes / no)
```

---

### Step 3 — Humanization Mode (Optional)

**Trigger conditions:** User requests "rewrite", "lower AI score", "humanize",
"bypass Turnitin/GPTZero", or accepts the proactive offer at end of Step 2 report.

#### Output Structure (3 Mandatory Parts)

**Part A — Specific Revision Checklist**

Produce a table with the following columns:

| # | Original Quote | Fingerprint Issue | Suggested Fix | Expected Score Reduction |
|---|---------------|-------------------|---------------|--------------------------|
| 1 | "…"           | [issue type]      | [fix]         | −X%                      |

**Part B — Complete Rewritten Version**

- Maintain 100% of original meaning, key facts, and professional terminology
- Length deviation must remain within ±10% of original word count
- **Bold** or mark key structural changes inline for transparency
- For academic text: preserve all statistical values exactly as provided
  (P values, 95% CI, HR, OR, Mean ± SD, sensitivity/specificity figures)
- For academic text: maintain Vancouver/APA/journal-specific citation formatting

**Part C — Verification Loop**

```
Next step: Run the rewritten text through your detector of choice.
If score remains above 15%, reply "Rewrite again" for a second iteration.
Estimated iterations to reach < 10%: [1–3 based on current score]
```

---

## Revision Strategy Library (2026 Top 12, Priority-Ordered)

Apply strategies in this order during humanization:

| Priority | Strategy | Implementation |
|----------|-----------|----------------|
| 1 | **Sentence Rhythm (Burstiness)** | Mix short sentences (< 12 words) with complex ones (> 35 words) to achieve length variance > 8 |
| 2 | **Contextual Adaptation** | Academic: structural variation only, no colloquialisms. Marketing: inject personal phrases ("In my experience,", "Actually,") |
| 3 | **Claude Bypass** | Remove ≥ 90% of em-dashes (—); replace with periods, commas, or standard conjunctions |
| 4 | **Detail Injection** | Add specific numbers, dates, institutional names, or concrete examples where contextually appropriate |
| 5 | **Controlled Imperfection** | Allow 1–2 instances of natural phrasing variation or minor repetition; avoid over-polished uniformity |
| 6 | **Layered Rewriting Order** | Execute in sequence: Structure → Vocabulary → Tone → Personalization |
| 7 | **Transition Diversification** | Replace repeated transitions (e.g., "furthermore" × 3) with varied alternatives or clause restructuring |
| 8 | **Passive → Active Conversion** | Reduce passive voice density below 25% for non-academic text; below 35% for academic text |
| 9 | **Paragraph Opening Variation** | Ensure no two consecutive paragraphs open with the same syntactic pattern |
| 10 | **Hedging Naturalization** | Replace mechanical hedges ("It is important to note that") with disciplinary-natural ones ("These findings suggest…", "Caution is warranted when…") |
| 11 | **Conclusion Differentiation** | Ensure the conclusion introduces at least one framing element not present verbatim in the introduction |
| 12 | **GPT List Dissolution** | Convert bulleted/numbered prose lists back into flowing paragraph form where content allows |

---

## Academic Text Special Protocol

When the input is identified as **academic/scientific writing** (e.g., manuscript sections,
grant proposals, clinical reports), apply the following overrides:

- **DO NOT** insert colloquialisms, first-person experiential phrases, or informal register shifts
- **DO NOT** alter any numerical values, statistical results, or units of measurement
- **DO NOT** change citation keys, reference numbers, or bibliography entries
- **DO** achieve burstiness solely through sentence structure variation (clause reordering,
  sentence splitting/merging, appositive insertion)
- **DO** preserve all reporting guideline language (CONSORT, STROBE, PRISMA, STARD)
- **DO** maintain discipline-specific terminology (radiology descriptors, anatomical nomenclature,
  pharmacological names, gene symbols, etc.)
- Target output registers: *rigorous, objective, concise* — identical to high-quality human
  scientific prose

---

## Edge Cases & Boundary Handling

| Condition | Behavior |
|-----------|----------|
| Text < 80 words | Prepend warning: "⚠ Sample too short; accuracy reduced by ~30%. Proceeding with available analysis." |
| Highly templated but likely human-written | Flag as "Requires manual review"; note "No major rewrite needed; minor tweaks to 2 areas suggested" |
| Mixed AI + human authorship | Report section-level breakdown where identifiable; flag transition points |
| Non-English text | Apply same logic; note that perplexity baselines may differ by language |
| Code or structured data embedded in text | Exclude from analysis; preserve unchanged in rewrites |

---

## Quick Reference: Common Detector Thresholds (2026 Estimates)

| Detector | Low-Risk Threshold | Notes |
|----------|--------------------|-------|
| GPTZero | < 20% AI probability | Burstiness weight high |
| Turnitin AI | < 15% AI writing | Sentence-level flagging |
| Copyleaks | < 25% AI score | Perplexity-sensitive |
| Winston AI | < 20% | Style-pattern focused |
| Originality.ai | < 15% | Aggressive; recommend 2 iterations |

---

## Ethical Disclaimer (Mandatory — append to every output)

> *Detection and rewriting results are for reference and educational purposes only.
> Please ensure full compliance with your institution's, journal's, or platform's
> academic integrity policies before submitting any revised text.*

---

## References

- Perkins M, et al. (2025). AI detector accuracy benchmarking study — average accuracy 39.5%
  across 12 commercial tools.
- 2026 empirical data: Manual adjustments + skill-guided revision consistently achieves
  detection scores below 10%, outperforming most paid humanizer services.
- Internal resources: `references/de-ai/examples.md`, `scripts/perplexity.py`,
  `reference.md` (Common Bypass & Countermeasure Checklist)
