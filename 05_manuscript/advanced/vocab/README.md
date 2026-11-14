# 05_manuscript advanced vocab (personal corpus + overrides)

Canonical L1/L2/L3 **machine lists and bans** live in `05_manuscript/base/vocab/` (`SKILL.md` + `MODULE.md` + `05_manuscript/base/vocab/L1/ban-phrases.md` + `05_manuscript/base/vocab/L1/ban-terms.yaml` + `05_manuscript/base/vocab/L2/approved-en.tsv` + `05_manuscript/base/vocab/L3/lab-ste.md`).

This folder carries the owner's **personality / voice / habits** that base must not hold:

| File | Role |
|---|---|
| `L1/sci-overrides.md` | lab-specific SCI overrides on top of the base ban lists |
| `L2/preferred-bank.md` | the frequency bank: what the owner actually writes, with counts (QCV source) |
| `L2/preferred-advanced.md` | the owner's recurring writing phrases, with bank counts |
| `L3/voice-habits.md` | house overrides that beat generic STE defaults + Chinese comment five-slot habit |
| `scripts/README.md` | pointer to the MY-CODES counters |

**Conflict rule:** base stays canonical for bans and machine lists — where an advanced row and a base row disagree, base wins; counts never lift a ban. The only ban authority is `05_manuscript/base/vocab/L1/ban-terms.yaml`. Advanced files are a QCV/voice source (S3-S4), not a first-pass rule set.

The counters live in `{code_stats}\tools\vocab-harvest\`; this pack keeps the pointer
`scripts/README.md`. They read `<GLOSSARY_ROOT>\banks\paras.jsonl` and need `SKILLS_ROOT` for the
ban list — both env vars, no lab default; a missing env exits 1.
