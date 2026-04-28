# RuCCoN

## Overview
RuCCoN (Russian Clinical Concept Normalization) is a dataset for clinical concept normalization in Russian, manually annotated by medical professionals. It contains entity mentions linked to concepts from the Russian-language part of the UMLS ontology.

## Task
- **Clinical Concept Normalization** (Entity Linking)
- **NER**: Named Entity Recognition with 7 entity types
- **Language**: Russian
- **Domain**: Clinical free-text notes (pediatric, allergic and pulmonary conditions)

## Dataset Statistics
- 160 fully annotated clinical texts
- ~250,000 tokens
- 16,028 entity mentions linked to 2,409 unique UMLS concepts
- 7 entity types, 7,400 attributes, 3,500 relations

## Entity Types
| Type | Description |
|------|-------------|
| Disease | Diagnosis / disease |
| Symptom | Clinical symptom |
| Drug | Medication |
| Treatment | Treatment procedure |
| BodyLocation | Anatomical body location |
| Severity | Severity assessment |
| Course | Disease course |

## Source
- GitHub: `AIRI-Institute/RuCCoN`
- Paper: Nesterov et al., "RuCCoN: Clinical Concept Normalization in Russian" (ACL 2022 Findings)

## Download Status
Downloaded 55 annotated text files from GitHub repository.

## References
- https://github.com/AIRI-Institute/RuCCoN
- https://aclanthology.org/2022.findings-acl.21/
