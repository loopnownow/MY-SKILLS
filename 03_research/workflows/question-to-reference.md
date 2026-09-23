---
name: question-to-reference
description: >
  03 default research spine (not a fine id; not a lit-search mega-skill).
  Stages R1–R5: Question → Evidence/Mechanism → Design → Data need → Research Brief.
  Each stage emits a card; later stages consume prior cards. Mid-chain entry allowed.
  00 chooses entry / rollback / stop; 03 owns content. lit-search is a tool under R2 only.
triggers:
  - 这个课题能不能做
  - 研究问题怎么拆
  - 证据和机制
  - 数据够不够做
  - 研究探索
  - question-to-reference
owner: 03_research
type: 03-workflow
---

# question-to-reference

## 0. Positioning

**This is 03’s default research exploration spine**, not a “literature search flow”.

```text
R1 Question → R2 Evidence & Mechanism → R3 Design → R4 Data need → R5 Research Brief
```

| Owns | Does not own |
|---|---|
| Content chain + stage cards | Session mount pick (01) |
| Mechanism labels with source class | Manuscript prose (05) |
| Data **requirements** list | Data extract / QC tables (02) |
| Hand-off asks to 02/04 | Final sample-size / model verdict (04) |
| | QC gate ids `G0` / `G-04` / … (00) |

**Hard split with 00**

- **03** = research content chain (R1–R5) and card quality.
- **00** = which stage to enter, whether to reuse completed cards, when to roll back, when to STOP, L1/L2 budgets (`00_orchestrator/workflows/research-exploration-loop.md`).

Stage ids are **R1–R5** (research). Do **not** call them G1–G5 — that collides with QC gates (`G0`, `G-PHI`, `G-04`, …).

**One workflow file only.** Do not re-implement PubMed search, MA, design engines, stats, or ETL here. Dispatch live mounts / personal supplements.

---

## 1. Cards (intermediate objects)

Every stage **must** leave a card. The next stage consumes cards, not chat memory.

| Stage | Core question | 03 does | Card |
|---|---|---|---|
| **R1** | What am I studying? | Split question; PICO/PECO; hypothesis; search keywords | **Question Card** |
| **R2** | What does existing work say? | Retrieve (via tools); screen; verify claims; mechanism map; conflicts / gaps | **Evidence & Mechanism Map** |
| **R3** | How should we test it? | Design type; exposure/intervention; outcomes; confounders; bias; reporting guideline | **Study Design Card** |
| **R4** | Can current data support it? | List variables / imaging / timepoints / follow-up / missing; ask 02/04 | **Data Requirement Card** |
| **R5** | What can we conclude *for planning*? | Synthesize evidence + design + data conditions | **Research Brief** (reference conclusion) |

Card stubs (keep short; fill only known fields; never invent PMID / *n* / ethics):

```yaml
# Question Card (R1)
question_card:
  pico_or_peco: ""
  hypothesis: ""
  keywords: []
  status: draft | locked | blocked
  stop_reason: ""   # if blocked
```

```yaml
# Evidence & Mechanism Map (R2)
evidence_map:
  claims: []        # claim → source → population → endpoint → effect → conflict
  mechanisms: []    # claim → source → class: direct | indirect | hypothesis | unknown
  gaps: []
  status: draft | locked | blocked
```

```yaml
# Study Design Card (R3)
design_card:
  design_type: ""
  population: ""
  exposure_or_intervention: ""
  outcomes: []
  confounders: []
  bias_risks: []
  reporting_guideline: ""
  status: draft | locked | blocked
```

```yaml
# Data Requirement Card (R4)
data_requirement:
  required: []      # must-have variables / series / events
  optional: []
  substitutes: []
  imaging: []
  timepoints: []
  follow_up: ""
  feasibility_ask:
    to_02: ""       # obtain / process?
    to_04: ""       # stats support?
  verdict_from_handoff: ""  # yes | partial | no | pending
  status: draft | locked | blocked
```

```yaml
# Research Brief (R5) — NOT a paper Conclusion
research_brief:
  current_evidence: ""
  evidence_gap: ""
  proposed_question: ""
  feasible_design: ""
  data_limits_or_stops: ""
  reference_conclusion: ""
  status: draft | locked | handoff
```

Prefer storing under `<project>/ref/` (e.g. extend `project-state.yaml` or sibling `research-cards.yaml`). Do not fork a second global schema without a CHG.

---

## 2. Mid-chain entry (not a forced linear run)

```text
                ┌──────────────┐
                │ R1 Question  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ R2 Evidence  │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ R3 Design    │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ R4 Data need │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ R5 Brief     │
                └──────────────┘

       ↑              ↑              ↑
   unclear Q     design hole      data short
       └──────── return to stage ──────┘
```

**00** inspects what already exists (cards, cohort description, locked hypothesis). **Do not** restart at R1 when later cards are already valid.

Examples:

- “肝硬化患者 + CT，想做侧支与并发症” → often enter **R1** (question still fuzzy) then R2→R5.
- “已定脾肾分流与曲张出血关系，看现有数据能不能做” → enter **R2/R3 as needed**, focus **R4**; skip a locked R1.

Reuse rule: completed card with intact sources → do not re-run that stage without cause (aligns with 00 exploration-loop reusable work).

---

## 3. Stage rules

### R1 — Question Card

- Output a testable question (PICO/PECO) + hypothesis + keyword set.
- **STOP** if the question cannot be made testable after one clarify round.

### R2 — Evidence & Mechanism Map (`lit-search` is a tool here only)

```text
R2
├─ literature retrieval     → mount lit-search (and session-picked helpers)
├─ evidence screening
├─ claim verification       → verify-refs when mounted / needed
├─ mechanism synthesis
├─ contradictory evidence
└─ evidence gap
```

**Mechanism lock**

```text
Mechanism claim
  → must have source
  → source must actually address that mechanism
  → class each edge: direct | indirect | hypothesis | unknown
```

03 **may** propose a mechanism hypothesis. 03 **must not** write a guess as literature fact.

**STOP / RETURN R1** if core hypothesis has no usable support and cannot be reframed.

### R3 — Study Design Card

- Design type, exposure/intervention, outcomes, confounders, bias, reporting guideline.
- Use mounted design capability + `design/radiology-design.md` when imaging-specific.
- **RETURN R1/R2** if bias or endpoint definition is unresolvable with current evidence.

### R4 — Data Requirement Card + feasibility gate

```text
R3 design needs
  → R4 lists required / optional / substitutes
  → hand off:
       03: What data are needed?
       02: Can we obtain/process them?
       04: Can they support the analysis?
  → yes | partial | no
```

03 **does not** extract HIS/PACS tables and **does not** give the final statistical go/no-go.

**STOP** if a must-have field is absent and no substitute is accepted by the user.

### R5 — Research Brief (reference conclusion)

Answer only:

1. Current evidence  
2. Evidence gap  
3. Proposed research question  
4. Feasible study design  
5. Data limitations / stopping conditions  

Then **HANDOFF** (02/04/05 as appropriate). Never emit Introduction/Discussion prose here.

---

## 4. Dispatch map (existing capabilities only)

| Stage | Call (examples) | Do not |
|---|---|---|
| R1 | `frontier-hypothesize`; `personal/intake.md` | Invent endpoints |
| R2 | `lit-search`; optional `verify-refs` / `ma-scout` / `paper-lookup` if session-picked | Treat lit-search as the whole of 03 |
| R3 | mounted design ids; `design/radiology-design.md` | Write 05 prose |
| R4 | emit Data Requirement Card → **02** / **04** | Run 02 ETL or 04 models inside 03 |
| R5 | synthesize cards → Research Brief | Paper Conclusion section |

No new fine ids for R1–R5.

---

## 5. Stop / return / handoff

| Stage | Stop or return when |
|---|---|
| R1 | Cannot form a testable question → **STOP** |
| R2 | No usable support for core claim → **STOP** or **RETURN R1** |
| R3 | Unfixable bias / endpoint hole → **RETURN R1/R2** |
| R4 | Must-have data missing → **STOP** |
| R5 | Brief locked → **HANDOFF** |

00 records stop reasons in project state / defects; do not silently continue.

---

## 6. Relation to other SOPs

| SOP | Role |
|---|---|
| This file | 03 content spine + cards |
| `00_orchestrator/workflows/research-exploration-loop.md` | Entry node, reuse, L1/L2, structural QC |
| `literature/intro-evidence-pack.md` | 05-driven Intro cards — later, narrower than this spine |
| `literature/journal-selection.md` | 选刊 — not this chain |

---

## 7. CHG note

Recorded as `CHG-20260924-002`. Expanding cards into a second global schema or new fine ids needs a new CHG + user nod.
