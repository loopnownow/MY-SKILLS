# G-LIT verify gate checklist (00 only)

**Owner:** `00_orchestrator` at Gate time.
**Execution body:** `03_research/advanced/citation-verify.md` (Victor). Do not move that file into `qc/`.
Specialists and 05/06 must not self-certify lit via this folder.

What 00 checks for **G-LIT** (also required before G-05 done and inside G-06):

- [ ] Citation-verify pass was run (not skipped)
- [ ] Claim→ref table exists (`claim_ref_table`)
- [ ] Strong-claim spot-check recorded when required
- [ ] No invented PMID/DOI
- [ ] 05/06 did not self-certify lit

On fail: 03 Victor (verify) / 05 Aitee (wording); user decides revise/weaken/delete vs further 03 substitute-ref search.