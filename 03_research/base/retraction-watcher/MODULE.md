---
name: "retraction-watcher"
domain: "03_research"
trigger: ["撤稿", "retraction", "Retraction Watch", "citation integrity"]
outputs: ["retraction_report"]
owner: "03_research/base/retraction-watcher/MODULE.md"
---

Pre-submission / evidence citation integrity check against retraction databases.
Lit-related sibling of `lit-cite` / `lit-search`. Absorbed from AIPOCH on 2026-10-17 (MIT).

> **Source**: [https://github.com/aipoch/medical-research-skills](https://github.com/aipoch/medical-research-skills)

# Retraction Watcher

A specialized skill for identifying retracted, corrected, or questionable papers in academic reference lists before they compromise research integrity.

## Quick Check

Use this command to verify that the packaged script entry point can be parsed before deeper execution.

```bash
python -m py_compile scripts/main.py
```

## Audit-Ready Commands

Use these concrete commands for validation. They are intentionally self-contained and avoid placeholder paths.

```bash
python -m py_compile scripts/main.py
python scripts/main.py --help
```

## When to Use

- Use this skill when the task needs Automatically scan document reference lists and check against Retraction.
- Use this skill for evidence insight tasks that require explicit assumptions, bounded scope, and a reproducible output format.
- Use this skill when you need a documented fallback path for missing inputs, execution errors, or partial evidence.

## Workflow

Generic five-step workflow: see `00_orchestrator/references/pack-execution-contract.md` (fill `{pack_id}`). Pack-specific steps, if any, follow below.

## Purpose

Academic misconduct and errors can lead to paper retractions. Citing retracted work undermines research credibility. This skill:
- Scans reference lists from manuscripts, papers, or bibliographies
- Cross-checks citations against Retraction Watch and other retraction databases
- Identifies papers with retraction notices, expressions of concern, or corrections
- Provides detailed reports with retraction reasons and dates

## Trigger Conditions

Activate this skill when:
1. User provides a document with references and asks to check for retractions
2. User explicitly requests "check my references" or "scan for retracted papers"
3. User submits a bibliography or reference list for verification
4. Pre-submission manuscript review is requested
5. User wants to verify citation integrity

## Input Format

Accepted inputs:
- PDF files (manuscripts, papers, theses)
- Plain text files (.txt,.bib,.ris)
- Raw text containing reference lists
- URLs to papers or reference lists
- Clipboard content with citations

## Output Format

### Report Header
```
🔍 RETRACTION WATCH REPORT
Documents Scanned: [N]
References Found: [N]
Check Date: [YYYY-MM-DD]
```

### Status Categories

**🔴 RETRACTED** - Paper has been officially retracted
- Reason for retraction
- Retraction date
- Original DOI/PMID
- Recommended action: Remove citation

**🟡 EXPRESSION OF CONCERN** - Journal has raised concerns
- Nature of concern
- Date issued
- Recommended action: Verify current status, consider alternative sources

**🟠 CORRECTED** - Paper has published corrections/errata
- Correction details
- Date of correction
- Recommended action: Check if correction affects cited claims

**🟢 CLEAR** - No retraction issues found

## Technical Approach

### Citation Parsing Strategy
1. **Format Detection**: Identify citation style (APA, MLA, Vancouver, Chicago, etc.)
2. **Field Extraction**: Parse DOI, PMID, title, authors, journal, year
3. **Identifier Resolution**: Normalize DOIs (remove prefixes, validate format)
4. **Title Matching**: Extract article titles for fuzzy matching

### Database Checking
1. **Retraction Watch Database** - Primary source for retraction data
2. **Crossref API** - Retraction metadata via "update-type: retraction"
3. **PubMed API** - Retraction notices via publication type filters
4. **Open Retractions** - Aggregated retraction data

### Matching Algorithm
- **Exact Match**: DOI/PMID exact match (highest confidence)
- **Title Match**: Normalized title comparison (90%+ similarity threshold)
- **Author + Year**: Secondary verification for ambiguous matches
- **Fuzzy Matching**: Handle minor title variations and typos

## Difficulty Level

**Medium-High** - Requires:
- Robust citation parsing across multiple formats
- API integration with retraction databases
- Handling of partial/incomplete citation data
- Fuzzy matching for title-based lookups
- Rate limiting and caching for API calls

## Quality Criteria

A successful scan must:
- [ ] Parse >90% of citations correctly from standard formats
- [ ] Achieve <1% false positive rate on retraction detection
- [ ] Provide actionable recommendations for each flagged citation
- [ ] Handle missing DOIs/PMIDs via title matching fallback
- [ ] Complete checks within reasonable time (<30s for 50 references)
- [ ] Preserve reference numbering for easy identification

## Limitations

- Requires internet connection for database lookups
- Rate limits may apply to free API tiers
- Very recent retractions (<48 hours) may not be indexed
- Title-only matching may produce false positives with similar titles
- Non-English papers may have limited coverage
- Preprint citations (arXiv, bioRxiv) typically not tracked for retractions

## Example Usage

```python
# Check a PDF manuscript
python scripts/main.py --input manuscript.pdf --format detailed

# Check a BibTeX file
python scripts/main.py --input references.bib --output report.txt

# Check raw text
python scripts/main.py --text "[paste references here]"

# Quick check with summary only
python scripts/main.py --input paper.pdf --format summary
```

## Data Sources

- **Retraction Watch Database**: https://retractionwatch.com/
- **Crossref API**: https://api.crossref.org/
- **PubMed E-utilities**: https://www.ncbi.nlm.nih.gov/home/develop/api/
- **Open Retractions**: https://openretractions.com/

## References

See `references/audit-reference.md` for the audit criteria. Upstream format specs and API
notes were not vendored (upstream pack text stays upstream).

---

**Author**: AI Assistant 
**Version**: 1.0 
**Last Updated**: 2026-02-06 
**Status**: Ready for use 
**Requires**: Internet connection for database lookups

## Risk Assessment

| Risk Indicator | Assessment | Level |
|----------------|------------|-------|
| Code Execution | Python scripts with tools | High |
| Network Access | External API calls | High |
| File System Access | Read/write data | Medium |
| Instruction Tampering | Standard prompt guidelines | Low |
| Data Exposure | Data handled securely | Medium |

## Security Checklist

- [ ] No hardcoded credentials or API keys
- [ ] No unauthorized file system access (../)
- [ ] Output does not expose sensitive information
- [ ] Prompt injection protections in place
- [ ] API requests use HTTPS only
- [ ] Input validated against allowed patterns
- [ ] API timeout and retry mechanisms implemented
- [ ] Output directory restricted to workspace
- [ ] Script execution in sandboxed environment
- [ ] Error messages sanitized (no internal paths exposed)
- [ ] Dependencies audited
- [ ] No exposure of internal service architecture

## Prerequisites

```text
# Python dependencies
pip install -r requirements.txt
```

## Evaluation Criteria

### Success Metrics
- [ ] Successfully executes main functionality
- [ ] Output meets quality standards
- [ ] Handles edge cases gracefully
- [ ] Performance is acceptable

### Test Cases
1. **Basic Functionality**: Standard input → Expected output
2. **Edge Case**: Invalid input → Graceful error handling
3. **Performance**: Large dataset → Acceptable processing time

## Lifecycle Status

- **Current Stage**: Draft
- **Next Review Date**: 2026-03-06
- **Known Issues**: None
- **Planned Improvements**: 
 - Performance optimization
 - Additional feature support

## Execution contract

`retraction-watcher` uses the shared pack execution contract (output requirements, error handling, input validation, response template, when not to use, required inputs, output contract, failure handling, user checkpoints, quick validation): `00_orchestrator/references/pack-execution-contract.md`.
