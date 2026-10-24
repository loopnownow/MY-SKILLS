# Public datasets

Use this file when the user asks about public datasets, TCIA, TCGA, GEO, CPTAC,
IDC, public imaging cohorts, public transcriptomics, public single-cell or spatial
transcriptomics datasets, external validation, or public-data-based mechanism analysis.

## Core goal

Goal: put public data in the right role — external validation, mechanism annotation, background support, or method comparison. Always distinguish
“paired-data validation” from “unpaired-data interpretation.”

## First questions

- What is the public data for: external validation, mechanism explanation, extra literature evidence, pretraining, or replication control?
- Target disease, modality, treatment setting, endpoint, and sample size?
- Does the public set have raw imaging, masks, clinical endpoints, pathology/molecular labels, follow-up?
- Are imaging and omics from the same patient, lesion, and timepoint?
- Can license, citation requirements, access limits, and download date be recorded?
- Need a live check of availability, version, and access policy?

## Common public resources

Use current source checking before final recommendations, because dataset availability,
versions, and access rules can change.

| Resource type | Examples | Typical use |
|---|---|---|
| public imaging | TCIA, Imaging Data Commons | imaging validation, segmentation, radiogenomics |
| cancer genomics | TCGA, CPTAC | molecular annotation, paired radiogenomics when matched |
| transcriptomics | GEO, ArrayExpress, SRA | pathway validation, expression signatures |
| single-cell | GEO, Single Cell Portal, cellxgene | cell type annotation and mechanism support |
| spatial transcriptomics | GEO, HuBMAP, institutional public data | spatial niche support |
| challenge data | BraTS, KiTS, LIDC-IDRI, LiTS, MSD | segmentation/detection benchmarking |

Do not list a public dataset as available for the user's exact task without checking its
cohort, labels, modality, and access status when the advice is submission-critical.

## Public-data use levels

### Level 1: direct external validation

Requirements:

- same disease and clinically comparable population
- same or compatible modality/protocol
- same endpoint or mappable label
- enough sample size/events
- independent from training data
- locked model applied without retuning

### Level 2: paired radiogenomics validation

Requirements:

- same patient-level imaging and omics pairing
- clear sample ID mapping
- consistent time point or treatment context
- outcome or biology endpoint available
- transparent exclusions

### Level 3: mechanism support

Use when:

- public omics data are not paired to the user's images
- data can support pathway, cell type, or immune microenvironment interpretation
- claims are phrased as external annotation/support, not direct validation

### Level 4: background evidence

Use when:

- dataset is too different for validation
- it only supports literature context or hypothesis generation

## Search and screening plan

For public datasets, return:

1. disease and modality keywords
2. candidate databases
3. inclusion criteria
4. required fields
5. exclusion reasons
6. matching strategy
7. data-use and citation requirements
8. risk of domain mismatch

## Reporting public data

Methods should state:

- database name
- dataset/accession identifier
- access date
- inclusion/exclusion criteria
- downloaded files
- preprocessing and matching rules
- endpoint mapping
- whether data were used for validation, mechanism annotation, or background only

## Output format

```text
Public-data framing
- Purpose:
- Target disease / modality:
- Need paired data?

Candidate public sets
| Dataset | Likely use | Must verify | Risks |

Use path
- External validation:
- Mechanism explanation:
- Background support:

Writing and citation
- Methods wording:
- Data availability:
- Citation / access date:
```

## Red lines

- Do not present unpaired public data as direct validation of the user's model.
- Do not invent dataset IDs, sample sizes, endpoints, access dates, or availability.
- Do not ignore data licenses, citation requirements, controlled access, or privacy rules.
- Do not mix public data into training and then call it independent external validation.
- Do not use public data with incompatible endpoints without explicitly stating limitations.
