"""Retired fine ids and non-routable bodies.

Formerly `00_orchestrator/legacy_aliases.yaml`. Not a runtime alias table.
Internal runtime uses only canonical short ids. Human-facing entry text may
still keep 激发词, including old names; those are not ids.
"""
from __future__ import annotations

RETIRED_FINE_IDS: dict[str, str] = {
    "analyze-stats": "stats-analysis",
    "imaging-io": "preprocess-imaging",
    "meta-analysis": "stats-analysis",
    "02-tables": "clean-data",
    "02-imaging-qc": "preprocess-imaging",
    "02-radiomics-habitat": "stats-analysis",
    "04-fig-flow": "draw-flowchart",
    "04-fig-plot": "plot-figures",
    "02-imaging-io": "preprocess-imaging",
    "04-stats-models": "stats-analysis",
    "04-model-eval": "model-evaluation",
    "nature-academic-search": "verify-refs",
    "nature-reviewer": "simulate-reviewers",
    "nature-response": "tighten-response",
    "response-tone-polisher": "tighten-response",
    "nature-figure": "plot-figures",
    "scikit-survival": "stats-analysis",
    "make-figures": "draw-flowchart",
    "fig-plot": "plot-figures",
    "ma-scout": "stats-analysis",
    "pydicom": "preprocess-imaging",
    "cross-pack/aipoch/retraction-watcher": "verify-refs",
    "cross-pack/aipoch/response-tone-polisher": "tighten-response",
    "audit-figure-risk": "plot-figures",
    "scientific-visualization": "plot-figures",
    "manage-refs": "verify-refs",
    "peer-review-pdf-scan": "peer-review",
    "radiomics-ml": "stats-analysis",
    "architecture-zoo": "design-study",
    "design-ai-benchmarking": "design-study",
    "frontier-hypothesize": "design-study",
    "find-cohort-gap": "design-study",
    "intake-project": "design-study",
    "scout-meta-analysis": "stats-analysis",
    "batch-cohort": "clean-data",
    "04-stats-power": "calc-sample-size",
    "03-lit-cite": "verify-refs",
    "scientific-critical-thinking": "self-review",
    "model-validation": "model-evaluation",
    "audit-citations": "verify-refs",
    "analyze-survival": "stats-analysis",
    "audit-dicom": "preprocess-imaging",
    "write-venue": "write-paper",
}

RETIRED_BODIES: dict[str, str] = {
    "check-reporting": "05_manuscript/qc/check-reporting/",
}

# Never an alias; must not return as a live fine id either.
BANNED_UNALIASED_IDS: frozenset[str] = frozenset({"03-lit-fulltext"})
