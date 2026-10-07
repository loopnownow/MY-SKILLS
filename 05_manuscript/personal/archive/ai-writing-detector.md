# AI writing detector (archive — not default)

**Canonical entry:** `../../SKILL.md` (manuscript-core).

This file is **not** on the default de-AI path. Do not load it for polish, draft, or house.docx.

Diagnosis of AI-tell vocabulary and constructions uses `00_orchestrator/scripts/style_lint.py` (machine source: `05_manuscript/personal/ban-terms.yaml`). Default de-AI stays `de-ai.md` → `forbidden-phrases.md` → `ai-isms-checklist.md` → `stop-slop-core.md`.

Trigger only when the user explicitly asks for a historical detector note. Do not lower a detector score. Do not bypass GPTZero / Turnitin / Copyleaks. Do not inject colloquial detail or controlled imperfection. Methods stay passive (lab house rule); there is no passive-voice percentage target.

## What this archive is not

- Not a humanizer.
- Not a score-to-10% rewrite loop.
- Not Claude Bypass / Detail Injection / Controlled Imperfection.
- Not a detector-threshold table.

## Perkins 2024 (accuracy of detectors)

Perkins M, Roe J, Vu BH, et al. Simple techniques to bypass GenAI text detectors: implications for inclusive practices in educational assessment. *Int J Educ Technol High Educ*. 2024;21:53. doi: [10.1186/s41239-024-00487-w](https://doi.org/10.1186/s41239-024-00487-w)

- 39.5% is the detectors' baseline accuracy across the tools in that study.
- After deliberate rewriting, accuracy fell to about 17.4%.
- The paper's conclusion: these detectors are not suitable for judging academic misconduct.

Lab rule follows that conclusion: do not treat a commercial AI-detector score as proof of misconduct, and do not rewrite to chase a score.

## Ethical note

Detection notes are educational. Journal policy on AI use is checked at pre-submit (`pre-submit-consistency.md`). Integrity stays with the author and the journal.
