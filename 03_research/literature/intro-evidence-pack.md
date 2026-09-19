# Introduction evidence pack (03 side)

**Owner:** `03_research`. Serves the `05_manuscript` Introduction cards (`personal/evidence-request.md`). 03 searches and verifies; 05 decides.

## Intake

One card set per endpoint: `guideline_definition`, `missing_prior_result`, `related_work_appraisal`, `scarcity_check`. Read the endpoint name and the study method from the card. Do not read or copy unpublished results.

## Guideline lookup (latest edition)

1. Identify the issuing bodies for the endpoint. Examples: ESGO/ESTRO/ESP and FIGO for endometrial cancer staging and risk groups, WHO tumour classification, NCCN, ESUR for MRI, ACR Appropriateness Criteria.
2. Search the body's own site and PubMed for the newest edition. State the year, the citation, and the date checked. A superseded edition may be cited only as history.
3. Read the full text. Record the definition and where it sits (section, figure, or table), the recommendation and its level of evidence, and what the guideline leaves open (low evidence, postoperative-only information, insufficient data, not recommended outside trials).
4. Return the open issue as a candidate gap. 05 decides whether it is the gap.

## Prior results

One source per class: `mri_accuracy`, `radiomics_endpoint`, `habitat_or_nearest`. Prefer systematic reviews or multicenter validation. Record design, n, effect with CI, validation type, endpoint definition, and region of interest. Include one weaker or limited result if one exists.

## Appraisal fields

For each returned study: the strength, and the weakness relevant to the study (endpoint definition, validation type, region of interest, comparator, sample). These fields feed the one or two group-appraisal sentences in the Introduction.

## Scarcity check

PubMed plus one other source (Europe PMC, Scopus, or a web search). Log query strings, dates, and counts screened. Return the closest studies found. Do not state that none exist.

## Verification

L1 metadata, L2 numbers against the abstract or full text, L3 full text. Guideline definitions and appraisals need L3. Run `verify-refs` and the retraction and correction check on every returned reference.

## Boundaries

Candidates only. No manuscript wording. No invented PMID, DOI, page, or number. Only topic terms go to external services.
