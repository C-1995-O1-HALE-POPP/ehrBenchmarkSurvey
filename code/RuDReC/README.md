# RuDReC

## Overview
RuDReC (Russian Drug Reaction Corpus) is a partially annotated corpus of Russian consumer reviews about pharmaceutical products. It supports Named Entity Recognition (NER) for health-related entities including drug names, adverse drug reactions (ADRs), drug indications, and disease symptoms.

## Task
- **Named Entity Recognition (NER)**
- **Multi-label sentence classification** (health-related issues presence)
- **Language**: Russian
- **Domain**: Pharmacology / Drug reviews

## Dataset Statistics
- Raw corpus: 1.4M+ health-related reviews
- Labeled corpus: 500 reviews (4,809 sentences)
- Entity types: 6 (DrugName, DrugClass, DrugForm, ADR, DrugIndication, Finding)

## Entity Types
| Type | Description |
|------|-------------|
| DrugName | Name of the drug |
| DrugClass | Class of the drug |
| DrugForm | Form of the drug |
| ADR | Adverse Drug Reaction |
| DrugIndication | Indication for drug use |
| Finding | Miscellaneous finding |

## Data Format
JSON with fields: `file_name`, `text`, `entities` (list of entity spans), `sentence_id`

## Source
- GitHub: `cimm-kzn/RuDReC`
- Paper: Tutubalina et al., "The Russian Drug Reaction Corpus and Neural Models for Drug Reactions and Effectiveness Detection in User Reviews" (2020)

## Download Status
Downloaded 200 examples from GitHub repository.

## References
- https://github.com/cimm-kzn/RuDReC
- https://arxiv.org/abs/2004.03659
