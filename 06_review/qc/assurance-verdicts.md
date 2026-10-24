# Assurance verdicts (00 qc · standards only)

**Owner:** domain seat (canonical under `06_review/qc/assurance-verdicts.md`); 00 calls only. at Gate / Integrity compositions.
**Distill of:** ARIS `skills/shared-references/assurance-contract.md` + `acceptance-gate.md` (wanshuiyin/Auto-claude-code-research-in-sleep). Lab rewrite — not a clone.
**Chain index:** `06_review/qc/assurance-audit-chain.md`.

## Two axes (do not conflate)

| Axis | Controls | Lab stages |
|---|---|---|
| **effort** | depth / cost (rounds, prose polish) | draft work vs deep rework |
| **assurance** | whether audits must emit verdicts | draft → internal QC → submit |

| Assurance level | Silent skip? | Lab map |
|---|---|---|
| `draft` | Allowed | Early draft / exploratory |
| `polished` | Discouraged | Internal polish before Lee |
| `conference-ready` | Forbidden on mandatory layers | Pre-conference / internal QC freeze |
| `submission` | **Forbidden** on mandatory layers | Submit / Bai portal |

Default mapping when only depth is stated: light/balanced work → `draft`; max/beast / “submission-ready” language → `submission`. Override is legal: shallow effort + `assurance: submission`.

## Six-state verdict (every mandatory audit)

| Verdict | Meaning | Blocks submission? |
|---|---|---|
| `PASS` | Checks ran; green | No |
| `WARN` | Issues found; none disqualifying | No (must disclose) |
| `FAIL` | Disqualifying issues | **Yes** |
| `BLOCKED` | Audit should apply; prerequisites missing | **Yes** |
| `ERROR` | Audit invoked but failed (tool/timeout/malformed) | **Yes** at submission |
| `NOT_APPLICABLE` | Detector negative; artifact still written | No |

**`NOT_APPLICABLE` ≠ silent skip.** Phase ran; detector negative; JSON/MD artifact exists. Silent skip leaves no record — forbidden at `submission` / `conference-ready`.

**`BLOCKED` > `NOT_APPLICABLE`.** Example: numeric claims present but no primary results files → `BLOCKED`, not `NOT_APPLICABLE`.

## Minimal artifact fields

Each mandatory layer writes `*.json` (+ optional `.md` sibling):

- `audit_skill`, `verdict` (one of six), `reason_code`, `summary`
- `audited_input_hashes` (paths → sha256 of inputs actually read)
- `generated_at` (ISO-8601), optional `trace_path` / reviewer identity
- `details` — skill-specific

Stale hashes after edit → re-run that layer before submit.

## Who may ACCEPT (Type-B)

One-liner: **a loop may DRIVE; it must not ACQUIT.**

| Gate type | Example | Who judges |
|---|---|---|
| **Type-A** (execution) | file exists, exit 0, checklist attempted | Executor / script OK |
| **Type-B** (merit) | integrity OK, claim supported, submission-ready | Cross-seat / independent reviewer — **not** the executor who produced the work |

- Executor collects **paths only** for integrity audits; does not self-judge Type-B.
- Same-family interim review → label `provisional`; do not present as submission-ready yes.
- Human / recorded stop remains mandatory at Integrity FAIL and before `stage: done` (see `gates.md`).

## Soft pointers (ARIS P1 · no new G-* ids)

- **Stage map W1→W3** (IDEA / EXPERIMENT / NARRATIVE / paper → seats): `research-stage-artifacts.md`.
- **Review loop + REVIEW_STATE resume**: `06_review/qc/review-loop-state.md` (Lee seat; compose `assurance-audit-chain.md`).
- **Resubmit text-only whitelist / ledger**: `resubmit-edit-whitelist.md`.

## Soft wiring (no new G-* ids)

- **G-FACT** / **Integrity · pre-06**: when numbers cited, compose layers 1–3 per `assurance-audit-chain.md`.
- **G-LIT** / **G-CIT**: compose layer 4 (`citation-audit-gate.md` + `refs-verified.md`).
- **G-06** / Lee pre-review: layer 5 (`kill-argument-preflight.md`) before external / Bai when assurance ≥ conference-ready.

*Attribution: distilled from ARIS assurance-contract + acceptance-gate (wanshuiyin/Auto-claude-code-research-in-sleep). Host-agnostic; no MCP/Codex lock-in.*
