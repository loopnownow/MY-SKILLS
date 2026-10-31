# Contract tests

One file per contract domain; shared fixtures live in `support.py`. A guard must
fail on the state it forbids before it passes on the fixed state.

Run:

```
python -B -m unittest discover -s tests -v          # whole suite
python -B -m unittest tests.test_gates_contract -v  # one domain
```

Cross-repo tests (`test_cross_repo_contract.py`) expect **MY-RULES** and **MY-CODES**
beside **MY-SKILLS** (or on lab drive aliases). On a partial checkout only, set
`MY_SKILLS_ALLOW_MISSING_SIBLINGS=1` to skip those tests; default is **fail** (no silent skip).

| File | Covers |
|---|---|
| `test_registry_contract.py` | registry mirrors, fine id paths, alias targets, ledger freshness |
| `test_gates_contract.py` | gate table / mmd parity, Mermaid node integrity, viz seat ban, state templates, verdict vocabulary |
| `test_lab_paths.py` | lab path aliases, fine-id board, raw-lab-path hygiene |
| `test_cross_repo_contract.py` | E3 cross-repo: Rules->Skills cites, {code_stats} layout, retired ids not LIVE, version markers |
| `test_paths_resolve.py` | documented paths and owners resolve; bare relative pointers resolve from the citing file (else seat-prefixed); no external renderer |
| `test_retirements.py` | retired ids, seats, packs, absorbed 03 packs and absorption residue stay dead |
| `test_doc_structure.py` | pack layout, headers, registry-state match, one H1 per file |
| `test_frontmatter.py` | YAML / frontmatter parses, cited contract files exist |
| `test_language_style.py` | language lint contract (vocabulary, sections, constructions) |
| `test_seat_packs.py` | seat packs, routing, review interaction, pack dedupe |
| `test_repo_hygiene.py` | BOM, empty stubs, retired folders, mount vocabulary, pack side docs, test index match, cleanup invariants |
| `test_qc_guards.py` | retired lab tree, anchors, flow steps, punctuation wording |
| `test_office_track_changes.py` | track-changes validator rejects a silent overwrite |
| `test_vocab_harvest_sections.py` | paragraph-layer section rebuild and phrase counter |

Conventions: `unittest` only, `from __future__ import annotations`, constants at the
top of each file, no network or LLM calls, failure lists truncated to 20-40 items.
