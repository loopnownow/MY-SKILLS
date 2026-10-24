# Mount → review / polish recipe (lab)

**Owner:** `00_orchestrator` (session mount pick). Word delivery rules SSOT:  
Standing policy: `00_orchestrator/references/ownership-contract.md` + `06_review/personal/review.md` §0.  
Review voice / prefixes: `06_review/personal/review.md` §0.

## Trigger patterns (user)

Typical one-liner (Chinese):

```text
Use my skills, mount <pack>, review/polish <path>.docx
```

Pack aliases seen in lab traffic: resolve user synonyms to registry fine ids via `01_skill-integration/registry.yaml`. Do not invent ids. Historical pack nicknames are not live menus.

## Default chain

1. **00** — intent: review and/or polish on a `.docx`.
2. **01** — session mount pick: attach **only** the named pack fine ids; record `session_picked_fine_ids`. Do not auto-load all `MOUNTED`.
3. **06** — review / pre-review annotations (Lee). Comment author field **A**. Source tags per `06_review/personal/review.md` §0 — **no default-only `[A:personal]` when a mount supplied the finding**.
4. **05** — polish / Track Changes (Aitee) after user agrees on undecidable items.
5. Deliver: Track Changes on the original docx + comments; intermediate QC → project `ref\`.

## Plan-first

If the user asks for plan / proposal / do after agree: stop after the plan card; wait for explicit agree (e.g. `agree` / `1-4agree` / `agree-all`).

## Isolation

When the user asks for multiple independent reviewers (e.g. Nature Reviewer 1/2/3): run each in an **isolated** context; do not leak wording across reviewers.
