# MY-SKILLS Visualization Architecture v1.1

Approved design specification. User approved execution on 2026-10-03. Revision 1.1 (2026-10-20) removed the external renderer: the IR is rendered to HTML by the in-repo generator only. This file is a source document. It is not the documentation homepage. The generated homepage is written under the lab output dir given by `--out` / `MY_SKILLS_VIZ_OUT` (no default); not in-repo. Design-history pages only point here.

## Implementation record

The renderer is the in-repo generator [`scripts/gen_visualization.py`](scripts/gen_visualization.py). It renders the typed IR to HTML locally. No external renderer package is fetched, unpacked, verified, or executed, and no pin record is kept: the former `archify-version.yaml` was deleted on 2026-10-20 together with its G-VIZ-01 field checks.

`schema_version` is fixed by this specification: Architecture IR uses **1**; Workflow IR uses **2**. Both constants live in the generator and are asserted by `tests/test_frontmatter.py`.

The mapping contract is [`visualization-source-contract.yaml`](visualization-source-contract.yaml). The generator is [`scripts/gen_visualization.py`](scripts/gen_visualization.py). It reads [`runtime-flow.mmd`](../../../00_orchestrator/runtime-flow.mmd), [`runtime-flow.md`](../../../00_orchestrator/runtime-flow.md), [`gates.md`](../../../00_orchestrator/gates.md), [`ARCHITECTURE.md`](../../../ARCHITECTURE.md), and [`registry.yaml`](../../../00_orchestrator/registry.yaml). It reads only the in-repo files named above.

Generated files live under the dir given by `--out` / `MY_SKILLS_VIZ_OUT` (required; no default; former `my-skills-viz` retired 2026-10-20) and carry a generated marker, a rebuild command, the source fingerprint, the IR schema versions, and a build status. Every page is rendered from the IR by the in-repo generator; no page comes from an external renderer. `architecture/status.html` and `workflow/status.html` are the architecture and workflow pages. Hand-authored sources are this note, the mapping contract, and the generator. MY-SKILLS must **not** keep a committed `docs/` tree. GitHub Pages settings are not changed. **No in-repo GitHub Actions CI** (the former `.github/workflows/visualization.yml` is a `{DEL}` park, not a repo path). Local rebuild uses `gen_visualization.py --check` only (no write / no commit). A shape failure exits before replacing lab OUT files, so the last good files stay.

Delta output lists added, removed, and changed identifiers and labels. It does not assign merge risk.

## 1. Design decision

Rendering is not a new MY-SKILLS layer. The generator is a read-only consumer of registry and runtime metadata; it emits the typed IR, the Architecture page, and the Workflow page. Skill prose and repository structure stay facts of MY-SKILLS.

| Layer | Role |
| --- | --- |
| Fact source | `SKILL.md`, registry, runtime-flow, configuration, and the real repository structure |
| Index | `00` indexes the in-repo fine-id registry and session-pick. It indexes. It does not rewrite skill bodies |
| Schedule | `00` decides entry, Gate, QC, visualization build, and failure fallback |
| Display | Generated HTML and skill documentation are derived from the IR. They can be deleted and rebuilt. They do not become the fact source |

## 2. Boundary: 00 index / generator

| Component | Owns | Does not own |
| --- | --- | --- |
| 00 | When to generate; Architecture versus Workflow; Gate and QC; whether a failure blocks publish | Skill prose |
| 00 | orchestrator index: registry / session-pick / fine-id index and lifecycle | Treating a scan of files outside the registry as MY-SKILLS architecture facts |
| Generator (`scripts/gen_visualization.py`) | Render typed JSON IR to HTML pages | Deciding MY-SKILLS architecture; editing skills; deciding whether a PR merges |
| Human | Review Delta, architecture changes, and the final PR | Hand-editing generated HTML |

## 3. Canonical data flow

MY-SKILLS source → 00 registry / runtime metadata → 00 visualization gate → typed JSON IR → IR shape validation → local HTML render → HTML QC → lab `my-skills-viz` OUT.

Reverse dependency is forbidden. Generated HTML, previous generated HTML, screenshots, and an LLM guess about the repository are not the next round's architecture facts.

## 4. Visualization source contract

| View | Authoritative input | Question it answers |
| --- | --- | --- |
| Architecture | 00 registry, 00 architecture metadata, repository structure | What the system is made of, and where the boundaries are |
| Workflow | 00 runtime-flow, Gate, routing rules | How a task runs, including branches, exceptions, and loops |
| Fine ids | 00 fine-id registry (`registry.yaml`) | Which in-repo fine ids are LIVE / PROPOSED, and the status recorded there |
| Skill detail | `SKILL.md` and its supporting files | Documentation pages. Prose is not forced into a diagram |

These are not fact sources:

- LLM inference
- generated HTML
- previous generated HTML
- arbitrary external-file crawling
- filename alone
- visual appearance
- unvalidated JSON

Machine-readable copy: [`visualization-source-contract.yaml`](visualization-source-contract.yaml).

## 5. Two primary views

### 5.1 Architecture

Show stable system components, about 6-12 primary components. Use a boundary only for a real ownership, trust, process, or deployment boundary. Do not turn every fine skill into a node.

Primary chain: 00 Control / QC / Registry → 02 Data / Stats → 03 Literature → 05 Writing → 06 Review → 07 Response.

Skill evolution stays MY-RULES `{RULES}\skills.md` (skill-evolution; governance; propose only). Fine ids stay one index node fed by the in-repo registry, not one node per fine id.

### 5.2 Workflow

Task → 00 Detect / Gate → 00 Fine id pick / Dispatch → 02 data processing + statistics → 05 Writing → 06 Review → QC / Loop.

03 literature can be an independent entry, and it can be called during design, interpretation, or discussion. The main line does not mean every task must pass every layer. Mid-entry stays: existing statistics may enter 05, an existing manuscript may enter 06. Writing and review still pass 03 citation-verify (`Lit05` before Gate · 05, `Lit06` inside 06).

The machine graph is [`runtime-flow.mmd`](../../../00_orchestrator/runtime-flow.mmd).

## 6. IR schema policy

This project keeps its own small typed IR mapping of MY-SKILLS facts; it does not vendor an external schema. The shape is defined by [`visualization-source-contract.yaml`](visualization-source-contract.yaml) and enforced by `validate_ir()` in the generator.

Architecture documents use `components`, `boundaries`, and `connections` with `schema_version` 1. Workflow documents use `lanes`, `phases`, `groups`, `mainPath`, `nodes`, and `edges` with `schema_version` 2. Changing either version is a specification change: update this file, the contract, and the shape test together.

## 7. External renderer policy

| Field | Value |
| --- | --- |
| external renderer | none (removed 2026-10-20) |
| render | in-repo generator, offline, read-only |
| network | builds stay offline and reproducible |
| upgrade | none; adding a renderer requires a new approved revision of this file |

There is no version record and no update policy, because nothing outside the repository is consumed. If a renderer is ever reintroduced, it must arrive with a pinned version, an offline build path, and a gate that fails closed.

## 8. Local check / build (no in-repo CI)

There is **no** committed `.github/workflows` CI in this repository (retired workflow parked under `{DEL}`). On relevant path changes, regenerate IR and docs locally from sources with `gen_visualization.py`. Shape or schema failure does not overwrite the last good artifact. Rendering is local: no download, unzip, or external process runs at build time. GitHub Pages is not configured here.

Gates:

| Gate | Check | On failure |
| --- | --- | --- |
| G-VIZ-01 | Source completeness and registry consistency | Block IR generation |
| G-VIZ-02 | IR shape check against the fixed schema versions | Do not write a new artifact |
| G-VIZ-03 | Layout, route, and label diagnostics | Local repair. Do not delete a semantic edge to pass a visual check |
| G-VIZ-04 | HTML artifact check | Keep last-good |
| G-VIZ-05 | Architecture Delta review | A human confirms it on a PR |

G-VIZ-01 and G-VIZ-02 are **domain-held**: the generator raises them, and `00_orchestrator` does not route them. `00_orchestrator/gates.md` records only that fact.

## 9. Architecture Delta

A review compares Before, the structural diff, and After. Delta lists added, removed, and changed identifiers and labels. It does not infer risk, impact, or merge safety.

## 10. Documentation layer

| Page | Content |
| --- | --- |
| Homepage | Architecture, workflow, system status, fine-id registry index, build metadata |
| Skill index | Indexed by 00-07, status, source, and entry |
| Skill detail | Generated from `SKILL.md` frontmatter, with a path back to the source file |
| Design history | Decisions and this specification. Not the homepage |

## 11. Suggested lab OUT layout (`my-skills-viz`, retired 2026-10-20)

```text
<OUT>/
├── index.html
├── architecture/
│   ├── status.html
│   └── architecture.json
├── workflow/
│   ├── status.html
│   └── runtime.workflow.json
├── skills/
│   ├── index.html
│   └── <skill-id>.html
├── fine ids/
│   └── index.html
├── changes/
│   └── latest-delta.html
├── design-history/
│   └── index.html
└── build-manifest.json
```

`architecture/status.html` and `workflow/status.html` list the IR ids and link to the IR JSON. The homepage links to both pages. There is no externally rendered diagram page to link to.

## 12. Repository safety rules

1. The visualization build does not rewrite MY-SKILLS skill prose.
2. Fixes to a diagram go back to source, registry, or IR. Generated HTML is not hand-edited.
3. Fine-id bodies outside the 00 registry do not redefine architecture. New fine ids enter through the 00 registry first.
4. HTML is not a fact source. Deleting generated HTML and IR leaves the sources able to rebuild them (pass `--out DIR`; no default dir).
5. Delta is evidence. A human decides merge.
6. A layout failure does not justify deleting a semantic edge.

## 13. Acceptance

Deleting generated artifacts leaves a rebuild path from repository sources (`python3 02_data-processing/advanced/visualization/scripts/gen_visualization.py --out DIR`; no default dir). Editing a skill does not require a hand edit of HTML. A fine-id registry change does not alter the architecture diagram unless the 00 seat map changes. A shape failure does not overwrite the last good artifact. A structural Delta can be shown beside the HTML diff. Visualization does not add a long-lived top-level skill beside 00-06. Generated artifacts can show generation time, source snapshot, IR schema versions, and build status.

## 14. Notes for a later pull request

No pull request is opened by the branch that introduced this file. GitHub Pages was not enabled.

What is generated: IR JSON, homepage, status pages, skill pages from frontmatter, fine ids page, Delta page, design-history index, `build-manifest.json` under lab OUT.

What stays manual: this specification, `visualization-source-contract.yaml`, and the generator.

Local check/rebuild: `python 02_data-processing/advanced/visualization/scripts/gen_visualization.py` (`--check` = in-memory gates, no write). Rendering is local; nothing is downloaded, unpacked, or executed from outside the repository. Lab OUT defaults to `D:/0Grok/0doc/_library/my-skills-viz`. A failed shape check returns before replacing last-good lab files. **No in-repo `.github` CI** (retired workflow archived under `{DEL}` / `D:/0del`).

**Size note:** scripts/gen_visualization.py is ~55 KB (single generator). Prefer edits in place; split only if edit friction rises.
