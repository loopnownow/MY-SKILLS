# Lit pipeline router (03 capability · thin)

**Owner:** Victor / `03_research`. Not a cron product; thin pointer only.
**Inspired by:** Yuan1z `nature-literature-pipeline` / `nature-academic-search` / `nature-paper-card` (Apache-2.0 / MIT frontmatter where noted). Short original router; no Feishu/Telegram delivery layer.

## Pattern

```text
multi-source search  →  score / filter  →  card / deep-read  →  archive note
```

| Stage | Lab home | Notes |
|---|---|---|
| Search | `lit-search/` (+ optional live academic-search) | Prefer ≥2 sources; OpenAlex/PubMed before Scholar scrape |
| Score / filter | personal intake / intro-evidence-pack | Topic × methods × venue quality — lab weights; not a fixed 6-dim product |
| Card / deep-read | personal / project notes | One-paper card: claim, methods, n, limits — not full 01–16 dump |
| Verify | `verify-refs/` + `personal/citation-verify.md` | DOI-first field audit + claim→ref |
| Retraction | `retraction-watcher/` | After ref set changes |

## Explicit skip

- Full cron / messaging delivery product
- AutoResearchClaw pipeline orchestration
- PRISMA-trAIce full engine (systematic review only as a **router row** via reporting-guideline router)

*Attribution: pattern distilled from Yuan1z0825/nature-skills literature skills (Apache-2.0; lit-pipeline MIT in upstream frontmatter).*
