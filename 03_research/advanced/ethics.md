# Ethics

Use this file when the user asks about ethics approval, consent waiver, retrospective
clinical imaging research, privacy, de-identification, data sharing restrictions,
multi-center data use agreements, or manuscript ethics statements.

## Core goal

Goal: help authors state existing approvals and limits accurately. This does not replace an IRB/ethics-committee opinion and must not invent approvals that do not exist.

## First questions

- Is the study retrospective, prospective, registry, or multi-center retrospective analysis?
- Is ethics approval already in place? Which body, number, date, and which centers does it cover?
- What are the approval validity start and end dates（伦理期，批件起止日期）? Does the
  data-collection window fit inside them?
- Is informed consent waived? Who approved the waiver basis?
- Does it involve imaging, clinical, pathology, genomics, transcriptomics, single-cell, or spatial-omics data?
- Does it involve cross-institution transfer, cloud training, model deployment, or public sharing?
- Are data de-identified? Which fields cannot be shared?
- Does the target journal require a specific Ethics/Consent/Data Availability format?

## Ethics statement elements

Include only true facts:

- approving ethics committee or IRB
- approval number
- study design
- consent status or waiver
- data de-identification
- compliance with institutional rules
- multi-center approval or local approvals when applicable
- controlled-access restrictions if data cannot be public

## Ethics validity period / 伦理期

「伦理期」 means the **validity period of the ethics approval**（伦理批件/审批的**有效期**）: the
start and end dates printed on the approval. It is not a loose label for "the ethics stage"
（不是笼统的「伦理阶段」）. Ask for both dates and never infer them from the study period.

| Design | Rule |
|---|---|
| Prospective（前瞻性） | The data-collection window must sit inside the approval validity period. Collection window ⊆ validity period, both ends. |
| Retrospective（回顾性） | Data-collection activities only need to finish **on or before the validity end date**. Historical cases may be retrieved and the database built while the approval is valid; the case dates themselves are not required to fall inside the validity period, but no collection action may run past the end date. |

- If the planned window would run past the end date, either narrow the window to fit or have the
  author confirm a renewal/extension — do not silently present the longer window as covered.
- State the validity range in Methods or the ethics form only when the journal or form asks for it,
  and only from the approval letter.
- If the validity start or end is missing, ask the author for the批件起止日期. Do not back-fill them
  from the study period, the submission date, or another project's approval.

## Retrospective study skeleton

```text
This retrospective study was approved by [ethics committee/institutional review board]
of [institution] (approval No. [number]), and the requirement for written informed
consent was waived due to the retrospective nature of the study. All imaging and
clinical data were de-identified before analysis.
```

Use only if the user confirms approval and waiver. If not confirmed, ask for the facts.

## Multicenter wording

```text
Each participating center obtained local ethics approval or was covered by the
central approval according to institutional requirements. Data were transferred and
analyzed under approved data-use agreements after de-identification.
```

Use only when true. If centers have different approvals, list them in supplement or
state that center-specific approvals were obtained (each with its own 伦理期).

## Consent and privacy

Check:

- direct identifiers removed
- dates shifted or generalized where needed
- DICOM metadata scrubbed
- accession numbers removed
- rare disease and small-cell privacy risk
- genetic and omics data re-identification risk
- data-use agreement restrictions
- cloud or third-party processing approval

## Data sharing ethics

Possible positions:

- public open sharing: only when allowed and de-identified
- controlled access: common for clinical imaging and omics data
- no public sharing: acceptable when justified by consent, law, or institutional policy
- derived data sharing: feature tables, aggregate statistics, trained weights, or code

Use live `clean-data` (`data.md`) and live `preprocess-imaging` (`02_data-processing/base/preprocess-imaging/references/reproducibility-qc.md`) together for availability wording.

## Output format

```text
Ethics framing
- Study type:
- Approval status:
- Approval validity (伦理期, start–end):
- Data types and privacy risks:

Needs author confirmation
- [IRB, approval number, validity start/end, consent waiver, data-use agreement, sharing limits]

Ethics / informed-consent text
[only after facts are supplied]

Data-sharing limits
- Shareable:
- Controlled access:
- Not shareable:

Pre-submission risks
- [missing approval, unclear waiver, window outside 伦理期, identifiable metadata, omics privacy]
```

## Red lines

- Do not invent ethics approval, waiver, approval numbers, committee names, or dates.
- Do not invent or infer the approval validity period (伦理期) start or end; ask for the批件起止.
- Do not describe a prospective collection window that extends past the approval end date as covered.
- Do not provide legal advice; recommend checking institutional IRB and journal requirements.
- Do not recommend sharing identifiable DICOM, genetic, or clinical data.
- Do not imply consent waiver unless confirmed.
- Do not ignore multi-center approval and data-use agreement differences.
