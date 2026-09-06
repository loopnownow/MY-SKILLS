# Repository-wide Harvest-QC

`repo_qc.py` is the deterministic, read-only repository scanner for MY-SKILLS.
It is maintenance QC, not a new top-level skill and not an evolution engine.

## Scope

The scanner checks:

1. Required 00–06 + `skill-harvest` top-level Skill files.
2. Forbidden/retired top-level directories (`core/`, `archive/`, `bundles/`, `merged/`).
3. Skill frontmatter (`name`, `description`).
4. A-skill path depth (maximum four path components).
5. Relative Markdown links.
6. Active references to retired directory names; historical/negative documentation is excluded from this check.
7. `01_skill-discovery-integration/registry.yaml` mount-menu count and, when supplied, the B capabilities package path mapping.
8. `VERSION.txt` ↔ `INTEGRATION_MAP.md` consistency and fenced-block integrity.
9. Harvest-QC governance scaffold and anti-auto-modification guard.
10. Existing deterministic unit tests unless `--no-tests` is supplied.

## Usage

From the repository root:

```text
python skill-harvest/scripts/repo_qc.py
```

With the companion B package:

```text
python skill-harvest/scripts/repo_qc.py --capabilities ../MY-SKILLS-capabilities
```

Reports can be written without changing any Skill behavior. **Do not commit** generated `data/repo-qc.json` / `data/repo-qc.md` — regenerate locally when needed:


```text
python skill-harvest/scripts/repo_qc.py --json skill-harvest/data/repo-qc.json --report skill-harvest/data/repo-qc.md
```

## Governance

The scanner is **read-only**. A FAIL is evidence for diagnosis; it does not authorize an edit.
A QC event may be recorded under `skill-harvest/data/qc-events/`. Evolution proposals remain on-demand and require explicit user approval.

A repository-wide QC failure is not automatically a manuscript execution failure. Runtime gates remain owned by `00_orchestrator/gates.md`.
