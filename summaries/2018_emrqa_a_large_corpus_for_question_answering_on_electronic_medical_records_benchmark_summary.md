<!-- paper_key: "2018_emrqa_a_large_corpus_for_question_answering_on_electronic_medical_records" -->
<!-- paper_url: "https://arxiv.org/abs/1809.00732" -->
<!-- generated_on: "2026-04-20" -->

# Benchmark Summary for *emrQA: A Large Corpus for Question Answering on Electronic Medical Records*

Source paper: [https://arxiv.org/abs/1809.00732](https://arxiv.org/abs/1809.00732)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-20`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2018_emrqa_a_large_corpus_for_question_answering_on_electronic_medical_records/source.pdf`](../papers/2018_emrqa_a_large_corpus_for_question_answering_on_electronic_medical_records/source.pdf)
- Extracted text: [`../papers/2018_emrqa_a_large_corpus_for_question_answering_on_electronic_medical_records/source.txt`](../papers/2018_emrqa_a_large_corpus_for_question_answering_on_electronic_medical_records/source.txt)
- Searched the main paper plus the official artifact named by the paper: `https://github.com/panushri25/emrQA`.
- The paper introduces one benchmark, `emrQA`, and evaluates it through three benchmarkable task views: question-to-logical-form mapping, question-to-answer evidence mapping, and answer-class prediction.
- The public repo README describes a later refactored / extended release with larger counts than the EMNLP 2018 paper. The benchmark statistics and task framing below follow the paper unless explicitly marked as a post-paper artifact note.
- Concrete benchmark-family examples are available for the logical-form and answer-evidence tasks from Figure 2 plus the official `templates-all.csv` and README materials in the linked repo. No concrete public class-prediction note-level instance was found, so that task block records the recoverable template row and licensing-constrained access path instead.

## Verifier Notes

- Benchmark existence: `emrQA` is explicit in the title, abstract, contribution bullets, Table 1, and official repo.
- Task mapping: the three task sections below are grounded in Sections 6.1 and 6.2; `Question-to-Logical-Form Mapping` is the paper's `emrQL`, while the QA benchmark is split into machine comprehension and class prediction exactly as the paper does.
- Instruction fidelity: instructions are normalized from Sections 4, 6.1, and 6.2.
- Example fidelity: Figure 2 plus the official template / README artifacts are used directly for the first two tasks; the class-prediction task explicitly records the public template row and the reason no note-level worked example is openly available.
- Scoring fidelity: logical-form prediction uses accuracy; machine comprehension uses modified EM/F1; class prediction uses subset accuracy.
- Judge prompt fidelity: no LLM judge is used in this benchmark.
- Inference labeling: specialty and clinical stage are marked as inferred because the paper draws from multiple i2b2 clinical-note challenges rather than one care setting.

## 1. emrQA

emrQA is an English benchmark introduced by the paper for patient-specific question answering on electronic medical records derived from i2b2 challenge annotations and clinical notes. In the paper's release, the benchmark contains 455,837 question-answer pairs, 1,295,814 question-logical-form pairs, and 2,425 clinical notes collected across medications, relations, heart-disease-risk, obesity, and smoking challenge data. The benchmark also exposes 680 question templates mapped to 94 unique logical-form templates, making it useful both for interpretable semantic parsing and for downstream answer extraction from longitudinal clinical text. The linked public repo later documents an expanded refactored release, but the paper-introduced benchmark definition remains the canonical source for the summary below.

- **Language:** English
- **Clinical Stage:** Not explicitly stated; inferred as mixed longitudinal clinical-note QA over patient histories
- **Source Clinical Document Type:** General clinical notes and longitudinal note bundles from i2b2 challenge datasets
- **Clinical Specialty:** Not explicitly stated; inferred as multi-specialty clinical QA over heterogeneous EMR note collections
- **Application Method:** Public benchmark introduced by the paper; distribution and later updates are tied to i2b2 / n2c2 licensing and the official `emrQA` repository

---

## 1.1 Task: Question-to-Logical-Form Mapping

This task is to map a natural-language clinical question to the benchmark's human-readable symbolic logical form.

### Task type
Semantic Parsing

```md
### Instruction
Given a clinical question, predict the emrQA logical form template / instance that captures the medical events, attributes, relations, and answer slot implied by the question.
### Input
[Natural-language clinical question]
### Output
[Logical form string over the emrQA ontology]
```

### Task example

```md
### Example Provenance
Figure 2 prints the full worked example used by the paper. The official repo then releases the corresponding template row in `templates/templates-all.csv` with the exact paraphrase bundle and logical-form template. Together these two sources expose both the instantiated question and the reusable template form.
### Search Depth
Paper + linked artifact
### Example Type
Concrete paper example plus official template row
### Source Dataset / Artifact
Figure 2 in the paper; official repo template schema for question and logical-form pairs
### Task Construction
The benchmark first normalizes clinician questions into templates with entity placeholders, then links those templates to expert-authored logical-form templates. Filled question / logical-form pairs are produced by instantiating placeholders from i2b2 annotations.
### Fidelity
Figure 2 content and the `templates-all.csv` row below are copied source-faithfully with only whitespace cleanup and line wrapping.
### Example
Figure 2 instantiated example:
- `Question`: `What is the dosage of Nitroglycerin ?`
- `Logical form`: `MedicationEvent (Nitroglycerin) [dosage=x]`
- `Answer = 40mg, Evidence = Nitroglycerin 40 mg daily, evening`

Official template row from `templates-all.csv`:
- `dataset`: `risk`
- `Input`: `medication`
- `Question`: `How much |medication| does the patient take per day##What is her current dose of |medication|##What is the current dose of |medication|##What is the current dose of the patient's |medication|##What is the dosage of |medication|##What is the patient's current dose does the patient take of her |medication|##What was the dosage prescribed of |medication|`
- `Logical Forms`: `MedicationEvent (|medication|) [dosage=x]`
- `Answer Concepts`: `none`
### Example Input
What is the dosage of Nitroglycerin ?
### Example Output
MedicationEvent (Nitroglycerin) [dosage=x]
### Gold / Reference Answer
The instantiated gold logical form in Figure 2 is `MedicationEvent (Nitroglycerin) [dosage=x]`; the corresponding official template is `MedicationEvent (|medication|) [dosage=x]`.
```

### Scoring standard

```md
### Scoring
Accuracy, defined as the number of logical forms predicted correctly.
### Evaluation Dimensions
- Exact logical-form prediction accuracy
- The paper evaluates two splits: `emrQL-1` (harder paraphrase split) and `emrQL-2` (instance split)
### Judge Prompt
Not applicable. This benchmark uses deterministic matching rather than an LLM judge.
```

---

## 1.2 Task: Question-to-Answer Evidence Mapping

This task is to answer a clinical question by extracting the supporting answer evidence from the clinical note, optionally together with the answer entity.

### Task type
QA

```md
### Instruction
Given a clinical question and the associated clinical note context, find the answer evidence in the note and recover the answer entity when it is explicitly represented.
### Input
[Natural-language clinical question], [clinical note context]
### Output
[Answer evidence line or span], [answer entity when available]
```

### Task example

```md
### Example Provenance
Figure 2 prints the concrete answer-evidence pair: `Answer = 40mg, Evidence = Nitroglycerin 40 mg daily, evening`. Section 4.3 then explains the release rule in direct wording: `instead of a single word or phrase we provide the entire i2b2 annotation line from the clinical note as the answer` and `we call them answer evidence instead of just answers`. The official repo README makes the evidence extraction rule concrete: `Our evidence line is simply the line in the clinical note corresponding to a particular i2b2 annotation's line number.`
### Search Depth
Paper + linked artifact
### Example Type
Concrete paper example plus repo-level answer-line construction rule
### Source Dataset / Artifact
Figure 2 in the paper; official repo README answer-evidence description
### Task Construction
After a question / logical-form template is filled with i2b2 annotations, emrQA extracts answer evidence from the note. For specific-answer questions it records both the answer entity and the supporting evidence line.
### Fidelity
The answer/evidence pair below is copied from Figure 2, and the evidence-line rule is copied from the official README.
### Example
Figure 2 answer-evidence example:
- `Question`: `What is the dosage of Nitroglycerin ?`
- `Answer`: `40mg`
- `Evidence`: `Nitroglycerin 40 mg daily, evening`

Official repo evidence-line rule:
- `Our evidence line is simply the line in the clinical note corresponding to a particular i2b2 annotation's line number.`
### Example Input
Question: What is the dosage of Nitroglycerin ?
Clinical note context: ... Nitroglycerin 40 mg daily, evening ...
### Example Output
Answer entity: 40mg
Answer evidence: Nitroglycerin 40 mg daily, evening
### Gold / Reference Answer
The answer entity is `40mg`, and the gold supporting evidence is the medication line `Nitroglycerin 40 mg daily, evening`.
```

### Scoring standard

```md
### Scoring
Modified Exact Match (EM) and F1 for machine comprehension.
### Evaluation Dimensions
- If the answer entity in the evidence is explicitly known, EM checks whether the predicted evidence contains that answer entity
- Otherwise EM checks whether the predicted evidence span lies within +/-20 characters of the ground-truth evidence
- F1 is computed from token-overlap bags built from evidence strings
- Because a question may have multiple evidence lines, the paper considers the top 10 predictions and averages EM / F1 over the ground-truth number of answers
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```

---

## 1.3 Task: Answer Class Prediction

This task is to predict a categorical answer directly from the full clinical note when the source challenge provides a document-level class label rather than span-level evidence.

### Task type
Classification

```md
### Instruction
Given a clinical question and the full clinical note, predict the answer class when the benchmark source data provide class labels rather than entity-level answer spans.
### Input
[Natural-language clinical question], [full clinical note]
### Output
[Categorical class label]
```

### Task example

```md
### Example Provenance
Section 4.3 gives the original construction rule in direct form: `The patient records in the smoking and obesity challenge datasets are categorized into classes with no entity annotations. Thus, for questions generated on these datasets, the entire document acts as evidence and the annotated class information (7 classes) needs to be predicted as the answer.` Section 6.2 then makes the benchmark split explicit: `(1) extraction of answer line from the clinical note` and `(2) prediction of answer class based on the entire clinical note`. The official repo releases the smoking template row in `templates-all.csv`, but its README states that the actual dataset must be downloaded from the i2b2 / n2c2 portal after signing the agreement, so the public repo does not expose a note-level smoking-class instance.
### Search Depth
Paper + linked artifact + public download instructions
### Example Type
Official template row plus public access-limit note
### Source Dataset / Artifact
Smoking and obesity source subsets in emrQA; official repo `templates/templates-all.csv`; official repo README download instructions
### Task Construction
For the smoking and obesity source datasets, the benchmark does not have entity annotations. The entire document serves as evidence, and the annotated class information from the source challenge becomes the answer to predict.
### Fidelity
The smoking template row below is copied verbatim from `templates-all.csv`. No public note-plus-class row was found after checking the paper, the official GitHub repo, and public download instructions.
### Example
Official smoking template row:
- `dataset`: `smoking`
- `Input`: `None`
- `Question`: `Does the patient currently smoke##Does the patient smoke##is the patient currently a smoker`
- `Logical Forms`: `SmokingUseEvent (x) [IsTobaccoUser=x]`
- `Answer Concepts`: `smoke_class`

Paper construction rule:
- `the entire document acts as evidence and the annotated class information (7 classes) needs to be predicted as the answer`

Public access note from the official repo:
- `emrQA is available for download here: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/ (you'll need to sign the agreement and request for the data, it comes through the same day).`
### Example Input
One of the smoking / obesity question templates together with the full clinical note.
### Example Output
One source-task class label, for example the smoking-status label hidden inside the licensed i2b2 / n2c2 release.
### Gold / Reference Answer
The gold answer is the document-level class annotation from the underlying smoking / obesity challenge data. The public repo exposes the template and answer concept type (`smoke_class`), but not a public note-level row with its class label.
```

### Scoring standard

```md
### Scoring
Subset accuracy.
### Evaluation Dimensions
- Exact class prediction against the document-level label
- This task is evaluated separately from extractive machine comprehension
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```
