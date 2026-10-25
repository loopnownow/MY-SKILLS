# G-STATS HTML results checklist (00 only)

**Owner:** `00_orchestrator` at Gate time.
Pass criteria extracted from `00_orchestrator/gates.md` (**G-STATS**) — no new rules.

After each `*-results.html`, 00 checks:

- [ ] HTML exists and is non-empty
- [ ] n and AUC taken from HTML (not invented)
- [ ] Split is training vs test (never Development set)
- [ ] `VAL_MODE` and columns only from `settings.ini`
- [ ] DeLong is a paired comparison, not a CI

On fail: 02 Loopnow (local rework; max 3 recoveries). Stats definitions / reported-consistency detail: `report-checks.md` in this folder.