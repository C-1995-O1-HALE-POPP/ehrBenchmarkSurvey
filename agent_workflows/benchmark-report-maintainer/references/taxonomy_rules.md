# Taxonomy Labeling Rules

## Dimensions

### `task` — primary evaluation task type

| Label | Description | Typical examples |
|---|---|---|
| `MCQ` | Multiple-choice question answering | USMLE-style exam QA, medical board questions |
| `CLS` | Classification / labeling / verification | Binary/multi-class/multi-label classification, assertion detection |
| `REG` | Regression / continuous-value prediction | Length of stay prediction, lab value forecasting |
| `SIM` | Semantic similarity / NLI / relevance | MedNLI, STS, query-document relevance |
| `EXT` | Extraction / sequence labeling / slot filling | NER, relation extraction, structured data extraction |
| `COD` | Normalization / coding / canonical mapping | ICD coding, UMLS concept normalization |
| `SUM` | Summarization / note construction | Discharge summary generation, radiology report summarization |
| `GEN` | Free-form answer / explanation generation | Open-ended QA, treatment plan generation, response writing |
| `RET` | Retrieval / grounding | Patient record lookups, FHIR resource retrieval |
| `SQL` | Text-to-SQL / database semantic parsing | EHRSQL, MIMICSQL |
| `CODE` | Code generation / executable problem solving | Bioinformatics scripts, clinical data analysis code |
| `CALC` | Numeric clinical calculation | Dosage calculation, risk score computation |
| `ACT` | Action execution / workflow operation | Clinical order placement, FHIR API mutations |
| `MIX` | Benchmark mixes multiple task forms | Suite benchmarks with diverse tasks |

### `interaction` — input/output interaction regime

| Label | Description |
|---|---|
| `ST-S` | Single-turn, short/closed-form input (sentence, paragraph, structured row) |
| `ST-L` | Single-turn, long-context input (full clinical note, entire discharge summary) |
| `MT-X` | Multi-utterance transcript as static input, one final output (e.g., doctor-patient dialogue) |
| `INT` | Genuinely interactive multi-turn dialogue (model responds turn-by-turn) |
| `AGT` | Tool-using / API-using / executable agent loop (model calls tools over multiple steps) |
| `MIX` | Benchmark intentionally mixes several interaction regimes |

### `source` — origin of the benchmark data

| Label | Description |
|---|---|
| `EXAM` | Exam questions / expert-authored QA items |
| `LIT` | Biomedical literature, ontology, or abstract-derived text (PubMed, ontologies) |
| `SEHR` | Structured EHR tables, coded event streams, SQL schemas, or FHIR resources |
| `NOTE` | Free-text clinical notes, discharge summaries, case reports, chief complaints |
| `RAD` | Radiology / imaging reports |
| `DIAL` | Patient-doctor dialogue, consultation record, portal/chat transcript |
| `WEB` | Consumer medical questions, search queries, web/forum QA |
| `MIX` | Multi-source benchmark suite or mixed record types |

### `role` — benchmark's role in the ecosystem

| Label | Description |
|---|---|
| `CORE` | Standalone benchmark / dataset |
| `VAR` | Released variant or difficulty split of a core benchmark |
| `SUITE` | Umbrella benchmark family / benchmark suite |

## Placement rules

### Section assignment priority

When a benchmark spans multiple families, assign to the section that best matches its **primary evaluation goal**:

1. If it requires tool use, API calls, or code execution → §1 Executable EHR Querying
2. If it predicts clinical outcomes from structured data or notes → §2 Clinical Prediction
3. If the output is a span, entity, code, or structured slot → §3 Extraction & Coding
4. If it asks the model to judge the relationship between two texts → §4 Semantic Matching
5. If it asks the model to produce narrative text (summary, response) → §5 Summarization
6. If it asks the model to select from options (exam-style) → §6 Knowledge QA
7. If it evaluates safety, bias, privacy, or compliance → §7 Safety
8. If it's a benchmark family/suite → §8 Suites

### Within-section ordering

Within each section, order lines alphabetically by benchmark name, grouped by source type when the section is large enough to warrant grouping.

### Multi-task benchmarks

When a single benchmark has sub-tasks of different types (e.g., `CAS-label` is CLS, `CAS-evidence` is SUM), label the benchmark with the dominant task type. In ambiguous cases, use `MIX`.

## Quick reference: common benchmark patterns

| Benchmark type | Typical `task` | Typical `source` | Typical `interaction` | Typical section |
|---|---|---|---|---|
| Clinical NER/de-identification | `EXT` | `NOTE` | `ST-S` or `ST-L` | §3 |
| ICD/code prediction | `COD` or `CLS` | `NOTE` | `ST-L` | §3 |
| MedNLI/STS | `SIM` | `NOTE` or `LIT` | `ST-S` | §4 |
| EHR outcome prediction | `CLS` or `REG` | `SEHR` | `ST-L` | §2 |
| Radiology report QA | `EXT` or `SUM` | `RAD` | `ST-L` | §3 or §5 |
| Text-to-SQL | `SQL` | `SEHR` | `ST-S` | §1 |
| Agent tool-use | `ACT` or `CODE` | `MIX` | `AGT` | §1 |
| USMLE/board exam | `MCQ` | `EXAM` | `ST-S` | §6 |
| Dialogue summarization | `SUM` | `DIAL` | `MT-X` | §5 |
| Literature NER | `EXT` | `LIT` | `ST-S` | §3 |
| Stigmatizing language detection | `CLS` | `NOTE` | `ST-S` | §7 |
| Bias/hallucination detection | `CLS` | `LIT` or `NOTE` | `ST-S` | §7 |
