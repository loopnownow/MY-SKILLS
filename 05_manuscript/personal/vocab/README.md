# 05_manuscript personal vocab (overrides + personal L2)

Canonical L1/L2/L3 bodies live in **A** `05_manuscript/base/vocab/` (`SKILL.md` + `MODULE.md` + `05_manuscript/base/vocab/L1/ban-phrases.md` + `L1/ban-terms.yaml` + `05_manuscript/base/vocab/L3/lab-ste.md`).

This A folder carries what base cannot hold:

| File | Role |
|---|---|
| `L1/sci-overrides.md` | lab-specific SCI overrides on top of the base ban lists |
| `L2/preferred-personal.md` | the owner's recurring writing phrases, with bank counts |
| `scripts/harvest_write_phrases.py` | offline counter that fills the `次数` / `篇数` columns |
| `scripts/harvest_sections.py` | rebuilds IMRAD sections from heading paragraphs (the `section_idx` field is unset in the paragraph layer) and counts sentence-head / sentence-tail phrases per section |

Base stays canonical: where a personal row and a base row disagree, base wins. Banned words are never restated in L2; the only authority is `05_manuscript/base/vocab/L1/ban-terms.yaml`.
