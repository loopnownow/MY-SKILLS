# A top layer vs B capability loops (2026-10-17)

Short pointer. Full flow: `../runtime-flow.md` A/B layering. Gates: `../gates.md` A/B top-layer QC checks.

| | **B** | **A** |
|---|---|---|
| Role | Fine-ID **first-pass** capability bodies | Personal **top-layer** route/handoff/authority |
| When | Before 00 QC | After 00 QC (re-loops) |
| Examples | write-paper, peer-review, verify-refs, polish-language, humanize, revise | A03/A05/A06/A07 personal SKILL + route + handoff |

**Flow:** B fine-ID loops -> **00 QC** -> A top-layer re-loops.

- A does not host long procedure bodies that live in B.
- Fine IDs for stats-analysis / figures / data-processing / study-design unchanged.
- Registry source stays B; A documents trigger/authority only.

**QC standards:** live in each domain `NN_slug/qc/`; `00_orchestrator/gates.md` decides WHEN / PASS-FAIL. Specialists and B first-pass do not self-invoke `qc/`.
