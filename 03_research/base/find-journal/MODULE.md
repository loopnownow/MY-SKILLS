---
name: find-journal
label_cn: 选刊推荐
mount_status: absorbed_from_A
description: Recommend medical journals from curated JCR pools; format to target AIM after user confirms.
owner: 03_research/base/find-journal/MODULE.md
---

# find-journal

Capability body: [SKILL.md](SKILL.md). Rules under `rules/`; list gates under `data/2026/`; post-choice format under `journal-format-compliance/`.

Victor seat routing and personal submission priors live in A (`MY-SKILLS/03_research/find-journal/` pointer + `{find_journal_submission}`). Do not vendor PHI / 投过 priors here.

Companion house-style templates: `05_manuscript/base/write-paper/` (not the 选刊 engine).

## Venue compliance (P1 absorb)

Pre-submit pass/fail: `05_manuscript/qc/venue-compliance-minima.md` + currency `05_manuscript/qc/venue-currency.md`. Do not bundle LaTeX/BST here.
