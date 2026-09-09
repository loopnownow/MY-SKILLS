# Logical modules (skills-within-pack)

These are **modules inside** `medical-journal-submit`, not separate top-level skills yet. **Victor** owns Phase-1 recommend / this pack; **Bai** owns checkbox HTML → JSON handoff and portal submit **after** the user picks a journal — keep modules documented here and bump pack version when the pipeline changes.

**Naming (aligned):**

| Short | Full | Alias / note |
|---|---|---|
| **JDI** | Journal Difficulty Index | Objective journal hardness |
| **JEI** | Journal Ease Index | Same family as **JESI**; `JEI = f(JDI, Capacity, Reviewability)` — not merely `100 − JIF` |
| **JESI** | Journal Ease-of-Submission Index | Composite used in Phase-1 tables; see `jesi-model.md` |
| **MJF** | Manuscript–Journal Fit | **= MFI** (Manuscript Fit Index); prefer MJF in new prose, accept MFI |
| **PAI** | Personal Acceptance Index / Prior | From `submission-prior.jsonl` |
| **JCI-C** | Journal Capacity Index | Capacity slots; **not** Clarivate JCI |

External `journal-recommender` (and similar tools) are **data/capability providers via query mounts**, **not** the top-level decision maker. Do not install them as a seventh system or mounted skill.

## Cross-system placement (01 / 03 / 04)

| Layer | Role |
|---|---|
| **01** Discovery / integration | External skill discovery; journal-skill query interface; mount management |
| **03** External mounts / query | PubMed, OpenAlex, Crossref, Europe PMC, JCR/JIF/JCI, CAS, indexing, APC/OA, review data, candidate retrieval — **current evidence only** |
| **04** Statistics / decision | JDI, JEI/JESI, MJF, Risk, PAI, dynamic weighting, Submission Tier |
| **05** Writing | Adapt manuscript to chosen target (after selection) |
| **06** Review | Validate fit and strategy |

## Workflow order (pack modules)

```text
sci-metrics-retriever → manuscript-fit-analyzer → jesi-calculator → submission-prior-logger
(metrics / 03)           (fit / MJF)               (JEI·JESI / 04)    (PAI correction)
```

Optional front door: **external candidate pool** (query mount) → then Difficulty + Fit + Risk → **MY-SKILLS decision** → Challenge / Target / Safety / Not recommended. Mapping to Jinshan layers: `recommendation-workflow.md`.

## 1. sci-metrics-retriever

Pull annual_publications, acceptance_rate, review_rate / desk_reject_rate, jif_percentile, jci_quartile, sub_pub_ratio from **primary** OpenAlex, Crossref, Europe PMC, journal/publisher sites, and Clarivate JCR (when licensed). LetPub and GitHub helpers are **auxiliary** query sources — not fixed dependencies (`query-sources.md`). Feeds **JDI** and **JCI-C**. Runtime only for yearly metrics — do not persist IF/quartile/volume into `submission-urls.csv`.

Each pulled value should carry Evidence/Confidence: `value | source | retrieval_date | confidence`.

## 2. manuscript-fit-analyzer

Extract abstract/manuscript keywords, design, disease, modality/tech (e.g. radiomics, 4D Flow MRI). Search target-journal ~3y papers (OpenAlex / Europe PMC), compute similarity and method coverage → **MJF (=MFI)** 0–100.

Prioritize: Scope Fit, Methodological Fit, Recent-Paper Similarity (over IF). Also consider Article Type, Population/Disease, Audience, Impact/Tier Fit, Practicality Fit, and Risk.

## 3. jesi-calculator

Normalize and weight per `jesi-model.md`. Gemini three-index and A/R/P/Q/C forms are **initial defaults only** and **must be overridable**.

```text
JESI = 0.50×(100−JDI) + 0.20×JCI-C + 0.30×MJF   # default; dynamic weights OK
JEI  = f(JDI, Capacity, Reviewability)
```

**Dynamic weighting by user constraints** (no fixed weights baked in as policy):

- Speed-focused → raise review speed, acceptance difficulty, capacity  
- Q1-required → raise JCR/JIF/JCI/CAS importance  
- OA/APC limits → hard constraints, not soft score pads  

Emit confidence when approximating. Do **not** copy external Fit Score fixed weights (e.g. Scope 30% / Impact 20% / …) into this pack.

## 4. submission-prior-logger

Append `[manuscript_type, target_journal, outcome, date, notes]` to `references/submission-prior.jsonl`. Later: logistic/Bayesian correction → **PAI** and personal `P(Accept)`. No IF/quartile fields on log lines.

## Risk module (04)

Journal Risk Assessment dimensions: Indexing Risk; Publisher Risk; Predatory Risk; CAS Warning; APC Transparency; Scope Ambiguity; Metric Conflict; Indexing Conflict; Review-time Uncertainty; Data-source Uncertainty.

**Critical rule: Unknown ≠ Low Risk.** No evidence is not evidence of safety.

## Conceptual decision (04)

```text
Submission Utility ≈ Journal Ease (JEI/JESI) + MJF + PAI + Practicality + Strategic Value − Risk
```

## Strategy labels vs pack layers

See `recommendation-workflow.md` for Challenge / Target / Safety mapping onto 层2补 / 层2 / 层3.
