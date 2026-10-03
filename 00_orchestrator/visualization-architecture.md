# MY-SKILLS Visualization Architecture v1.0

Approved design specification. User approved execution on 2026-10-03. This file is a source document. It is not the documentation homepage. The generated homepage is [`../docs/index.html`](../docs/index.html). Design-history pages only point here.

## Implementation record

Archify is pinned to `tt-a1i/archify` **3.0.1** (tag `v3.0.1`, commit `2ab3cae7ac2c2a55d7386ca789d03c4fcd31816c`, published 2026-09-28). Verification on 2026-10-03 used the GitHub tags list (newest tag `v3.0.1`), the [v3.0.1 release](https://github.com/tt-a1i/archify/releases/tag/v3.0.1), and the schema README plus `architecture.schema.json` and `workflow.schema.json` at that tag. The record is [`archify-version.yaml`](archify-version.yaml). `update_policy` is `check`. `auto_update` is `false`. `visualization_only` is `true`.

`schema_version` follows that pin. Architecture IR uses **1** because `architecture.schema.json` at v3.0.1 sets `schema_version` to the constant 1. Workflow IR uses **2** because the v3.0.1 schema README says new workflows use schema version 2, and this repository has no legacy workflow geometry to keep on version 1.

The mapping contract is [`visualization-source-contract.yaml`](visualization-source-contract.yaml). The generator is [`scripts/gen_visualization.py`](scripts/gen_visualization.py). It reads [`runtime-flow.mmd`](runtime-flow.mmd), [`runtime-flow.md`](runtime-flow.md), [`gates.md`](gates.md), [`../ARCHITECTURE.md`](../ARCHITECTURE.md), and [`../01_skill-discovery-integration/registry.yaml`](../01_skill-discovery-integration/registry.yaml). It does not read `mounts-cap/`.

Generated files live under `docs/` and carry a generated marker, a rebuild command, the source fingerprint, the Archify pin, and a build status. Hand-authored sources are this note, the version record, and the mapping contract. GitHub Pages settings are not changed. Archify itself is not installed in CI. The render job fails closed and leaves the last good files in place. See `.github/workflows/visualization.yml`.

Delta output lists added, removed, and changed identifiers and labels. It does not assign merge risk.

## 1. Design decision

Archify is not a new MY-SKILLS layer. It is a read-only visualization compiler. It reads defined registry and runtime metadata and emits Architecture and Workflow graphics. Skill prose and repository structure stay facts of MY-SKILLS.

| Layer | Role |
| --- | --- |
| Fact source | `SKILL.md`, registry, runtime-flow, configuration, and the real repository structure |
| Index | `01` discovers external packages, versions, and the mount index. It indexes. It does not rewrite external skill bodies |
| Schedule | `00` decides entry, Gate, QC, visualization build, and failure fallback |
| Display | Archify HTML and skill documentation are derived. They can be deleted and rebuilt. They do not become the fact source |

## 2. Boundary: 00 / 01 / Archify

| Component | Owns | Does not own |
| --- | --- | --- |
| 00 | When to generate; Architecture versus Workflow; Gate and QC; whether a failure blocks publish | Skill prose; external package bodies |
| 01 | External skill discovery; version check; mount registry; index and lifecycle | Treating a scan of external files as MY-SKILLS architecture facts |
| Archify | Render typed JSON IR to HTML diagrams | Deciding MY-SKILLS architecture; editing skills; deciding whether a PR merges |
| Human | Review Delta, architecture changes, and the final PR | Hand-editing generated HTML |

## 3. Canonical data flow

MY-SKILLS source → 01 registry / runtime metadata → 00 visualization gate → Archify JSON IR → schema validation → render → HTML QC → `/docs`.

Reverse dependency is forbidden. Generated HTML, previous generated HTML, screenshots, and an LLM guess about the repository are not the next round's architecture facts.

## 4. Visualization source contract

| View | Authoritative input | Question it answers |
| --- | --- | --- |
| Architecture | 01 registry, 00 architecture metadata, repository structure | What the system is made of, and where the boundaries are |
| Workflow | 00 runtime-flow, Gate, routing rules | How a task runs, including branches, exceptions, and loops |
| External mounts | 01 mount registry / version metadata | Which external packages are mounted, and which version is recorded |
| Skill detail | `SKILL.md` and its supporting files | Documentation pages. Prose is not forced into a diagram |

These are not fact sources:

- LLM inference
- generated HTML
- previous generated HTML
- arbitrary mounted-file crawling
- filename alone
- visual appearance
- unvalidated JSON

Machine-readable copy: [`visualization-source-contract.yaml`](visualization-source-contract.yaml).

## 5. Two primary Archify views

### 5.1 Architecture

Show stable system components, about 6–12 primary components. Use a boundary only for a real ownership, trust, process, or deployment boundary. Do not turn every fine skill into a node.

Primary chain: 00 Control / QC → 01 Discovery / Registry → 02 Data → 03 Literature → 04 Statistics → 05 Writing → 06 Review.

`skill-harvest` stays governance. External mounts stay one index node fed by the registry, not one node per fine id.

### 5.2 Workflow

Task → 00 Detect / Gate → 01 Mount / Dispatch → 02 Data → 04 Statistics → 05 Writing → 06 Review → QC / Loop.

03 literature can be an independent entry, and it can be called during design, interpretation, or discussion. The main line does not mean every task must pass every layer. Mid-entry stays: existing statistics may enter 05, an existing manuscript may enter 06. Writing and review still pass 03 citation-verify (`Lit05` before Gate · 05, `Lit06` inside 06).

The machine graph is [`runtime-flow.mmd`](runtime-flow.mmd).

## 6. Archify schema policy

This project does not copy Archify's full schema. It keeps a mapping of MY-SKILLS facts onto Archify IR. The schema is the one shipped by the pinned Archify version.

Architecture documents use `components`, `boundaries`, and `connections`, with `schema_version` 1 under the v3.0.1 pin. Workflow documents use `lanes`, `phases`, `groups`, `mainPath`, `nodes`, and `edges`. New workflow IR uses schema version 2. An existing version-1 workflow would stay on version 1 only to preserve fixed geometry. None is stored here.

## 7. External Archify version policy

| Field | Value |
| --- | --- |
| source | `tt-a1i/archify` |
| version | explicit, currently `3.0.1` |
| update_policy | `check` |
| auto_update | `false` |
| network | builds stay offline and reproducible |
| upgrade | 01 lifecycle check, then human confirmation, then update the record, then rebuild |

## 8. CI / build pipeline

On relevant path changes, regenerate IR and docs from sources. Shape or schema failure does not overwrite the last good artifact. Render with Archify only from a pinned local binary. This repository's CI does not fetch Archify. GitHub Pages is not configured here.

Gates:

| Gate | Check | On failure |
| --- | --- | --- |
| G-VIZ-01 | Source completeness and registry consistency | Block IR generation |
| G-VIZ-02 | Shape check against the mapping pin | Do not write a new artifact |
| G-VIZ-03 | Layout, route, and label diagnostics | Local repair. Do not delete a semantic edge to pass a visual check |
| G-VIZ-04 | HTML artifact check | Keep last-good |
| G-VIZ-05 | Architecture Delta review | A human confirms it on a PR |

## 9. Architecture Delta

A review compares Before, the structural diff, and After. Delta lists added, removed, and changed identifiers and labels. It does not infer risk, impact, or merge safety.

## 10. Documentation layer

| Page | Content |
| --- | --- |
| Homepage | Architecture, workflow, system status, external mounts, build metadata |
| Skill index | Indexed by 00–06, status, source, and entry |
| Skill detail | Generated from `SKILL.md` frontmatter, with a path back to the source file |
| Design history | Decisions and this specification. Not the homepage |

## 11. Suggested `/docs` layout

```text
/docs/
├── index.html
├── architecture/
│   ├── index.html
│   └── architecture.json
├── workflow/
│   ├── index.html
│   └── runtime.workflow.json
├── skills/
│   ├── index.html
│   └── <skill-id>.html
├── mounts/
│   └── index.html
├── changes/
│   └── latest-delta.html
└── design-history/
    └── index.html
```

`architecture/index.html` and `workflow/index.html` are generated status pages until a pinned Archify render writes the diagram. They are marked generated. They are not presented as Archify output.

## 12. Repository safety rules

1. The visualization build does not rewrite MY-SKILLS skill prose.
2. Fixes to a diagram go back to source, registry, or IR. Generated HTML is not hand-edited.
3. Mount contents do not redefine architecture. External packages enter through the 01 registry first.
4. HTML is not a fact source. Deleting generated `docs/` HTML and IR leaves the sources able to rebuild them.
5. Delta is evidence. A human decides merge.
6. A layout failure does not justify deleting a semantic edge.

## 13. Acceptance

Deleting generated `/docs` artifacts leaves a rebuild path from repository sources (`python3 00_orchestrator/scripts/gen_visualization.py`). Editing a skill does not require a hand edit of HTML. An external mount upgrade does not change the architecture diagram unless the 01 registry changes. A schema failure does not overwrite the last good artifact. A structural Delta can be shown beside the HTML diff. Visualization does not add a long-lived top-level skill beside 00–06. Generated artifacts can show generation time, source snapshot, Archify version, and build status.

## 14. Notes for a later pull request

No pull request is opened by the branch that introduced this file. GitHub Pages was not enabled.

What is generated: IR JSON, homepage, status pages, skill pages from frontmatter, mounts page, Delta page, design-history index, `docs/build-manifest.json`.

What stays manual: this specification, `archify-version.yaml`, `visualization-source-contract.yaml`, and the generator.

What did not run in CI: Archify render. During implementation the two IR files were checked once against the v3.0.1 `architecture.schema.json` and `workflow.schema.json` (zero schema errors). Those schema files were not copied into this repository. The generator's own shape check covers the fields it emits (required keys, `schema_version` pins, id pattern, component types, workflow column range, endpoint references). The CI render job exits non-zero when a pinned `ARCHIFY_BIN` is absent, and it does not download a release. Last-good files stay because `--check` does not write, and a shape failure returns before publish.
