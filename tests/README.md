# Contract tests

One file per contract domain; shared fixtures live in `support.py`. A guard must
fail on the state it forbids before it passes on the fixed state.

Run:

```
python -B -m unittest discover -s tests -v          # whole suite
python -B -m unittest tests.test_gates_contract -v  # one domain
```

| File | Covers |
|---|---|
| `test_registry_contract.py` | registry mirrors, fine id paths, alias targets, ledger freshness |
| `test_gates_contract.py` | gate table ↔ mmd map parity, gate metadata, verdict vocabulary |
| `test_lab_paths.py` | lab path aliases, fine-id board, raw-lab-path hygiene |
| `test_paths_resolve.py` | documented paths and owners resolve; bare relative pointers resolve from the citing file (else seat-prefixed); no external renderer |
| `test_retirements.py` | retired ids, seats, packs and absorption residue stay dead |
| `test_doc_structure.py` | pack layout, headers, registry-state match, one H1 per file |
| `test_frontmatter.py` | YAML / frontmatter parses, cited contract files exist |
| `test_ledger_assurance.py` | registry `change_id` reaches both ledgers; assurance terms |
| `test_language_style.py` | language lint contract (vocabulary, sections, constructions) |
| `test_seat_packs.py` | seat packs, routing, review interaction, pack dedupe |
| `test_state_template.py` | project-state and handoff templates cover hard gates + citation |
| `test_repo_hygiene.py` | BOM, empty stubs, retired folders, cleanup invariants |

Conventions: `unittest` only, `from __future__ import annotations`, constants at the
top of each file, no network or LLM calls, failure lists truncated to 20–40 items.
