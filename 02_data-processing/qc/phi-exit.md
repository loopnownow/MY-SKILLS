# G-PHI exit checklist (pointer only)

**Owner:** 00 at Gate time. Do not invent new PHI policy here.

Pass criteria are defined in `00_orchestrator/gates.md` (**G-PHI**). Before 02 tables or clinical extraction, 00 checks:

- [ ] PHI status known
- [ ] No HIS host/password in git or skill files
- [ ] Extraction uses env `HIS_USERNAME` / `HIS_PASSWORD` on the hospital machine only

On fail: stop; user. Related capability packs (e.g. `base/preprocess-imaging`) stay out of this folder.