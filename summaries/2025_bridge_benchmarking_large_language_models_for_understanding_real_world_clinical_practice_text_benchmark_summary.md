<!-- paper_key: "2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text" -->
<!-- paper_url: "https://arxiv.org/abs/2504.19467" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *BRIDGE: Benchmarking Large Language Models for Understanding Real-world Clinical Practice Text*

Source paper: [https://arxiv.org/abs/2504.19467](https://arxiv.org/abs/2504.19467)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text/source.pdf`](../papers/2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text/source.pdf)
- Extracted text: [`../papers/2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text/source.txt`](../papers/2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text/source.txt)
- Normalization choice: `BRIDGE` is treated as a paper-level umbrella evaluation rather than a single monolithic benchmark entry in this summary. Each named source dataset/sub-benchmark evaluated by the paper gets its own benchmark section below, and multiple tasks from the same source dataset stay grouped under that dataset.
- Normalization choice: task reformulations created by BRIDGE stay under the original source dataset section rather than being promoted into separate benchmark names. This means a dataset like `EHRQA` remains one constituent benchmark section even when BRIDGE adds several newly designed tasks on top of it.
- Example-search rerun (`2026-04-15`): Section 6 of the paper appendix does provide task-specific prompt templates, including the task description, instruction wording, output schema, and placeholder `Input` / `Output` slots used during model inference. What the paper still does not print is a concrete patient-level or document-level benchmark row with verbatim source text and gold output. The paper also names official artifact endpoints including `YLabOpen/BRIDGE`, the BRIDGE leaderboard, and `YLabOpen/BRIDGE-Open`. A deeper artifact pass confirmed that the official Hugging Face dataset tree exposes a task-level `Example/` directory with files such as `ADE-Drug dosage.example.json`, `cMedQA.example.json`, `MTS.example.json`, and `MEDIQA 2023-chat-A.example.json`, even though raw file contents are access-controlled in the current environment. Those artifact leads are now recorded in the audit report at `reports/example_search_audit_2026-04-15.md`.
- Verification note: BRIDGE uses deterministic reference-based metrics; no LLM-as-a-judge prompt is provided because judge prompting is not part of the evaluation design.

## Verifier Notes

- Verified the umbrella benchmark facts (59 source datasets, 87 tasks, 9 languages, 8 task families, 138,472 test samples) against the abstract, Results, Methods, and Supplementary Table S9.
- Verified per-dataset benchmark identities and task prompt templates against Section 6 of the supplement (`BRIDGE Dataset and Task Information`).
- Verified benchmark-wide split rules, invalid-output handling, and task-family metrics against Methods Section 4.
- Verified that official BRIDGE-Open artifact metadata exposes a populated `Example/` directory, but raw example payloads were not retrievable from this environment because the dataset requires access-controlled downloads.
- No full judge prompt is available because the paper does not use LLM-as-a-judge evaluation for these tasks.

## Paper-Level Umbrella Evaluation

BRIDGE is a multilingual umbrella evaluation introduced by the paper, aggregating **59 constituent source datasets / sub-benchmarks** into **87 tasks** across **9 languages** and **8 task families**. The umbrella benchmark spans **1,418,042 total samples** with **138,472 reserved for testing**, and evaluates **95 LLMs** under zero-shot, chain-of-thought, and five-shot prompting. I treat BRIDGE itself as the evaluation wrapper and leaderboard, while the actual benchmark sections below are split by the underlying named source datasets that BRIDGE evaluates.

- **Languages covered:** English, Chinese, Spanish, Japanese, German, Russian, French, Norwegian, Portuguese.
- **Task families covered:** text classification, semantic similarity, natural language inference, normalization and coding, named entity recognition, event extraction, question answering, summarization.
- **Source data mix:** 68/87 tasks are sourced from real-world EHR notes or clinical case reports, and 19/87 are derived from online patient-doctor consultation records.
- **New-vs-reused normalization:** the paper states that BRIDGE newly designed **13 tasks** on top of existing source datasets. In the per-dataset sections below, those new task constructions are recorded inside the relevant source dataset section instead of being treated as independent benchmarks.
- **Benchmark-wide split rule:** official dataset splits were used when available; otherwise BRIDGE used the fallback heuristic described in Methods (>2000 samples: 10% test, 1000-2000: 20% test, <1000: all but 20 cases used for testing, with 5 non-test examples sampled for few-shot prompting).
- **Benchmark-wide scoring rule:** text classification / semantic similarity / NLI / document-level normalization use Accuracy as the primary metric; NER / event extraction / entity-level normalization use event-level micro-F1 as the primary metric; QA and summarization use ROUGE-average as the primary metric.

## Benchmark Inventory

| Dataset / Sub-benchmark | BRIDGE Tasks | Language | BRIDGE Role | Notes |
| --- | --- | --- | --- | --- |
| MIMIC-IV CDM | MIMIC-IV CDM | English | Reused source dataset | 1 task(s) in BRIDGE |
| MIMIC-III Outcome | MIMIC-III Outcome.LoS; MIMIC-III Outcome.Mortality | English | Reused source dataset | 2 task(s) in BRIDGE |
| MIMIC-IV BHC | MIMIC-IV BHC | English | Reused source dataset | 1 task(s) in BRIDGE |
| MIMIC-IV DiReCT | MIMIC-IV DiReCT.Dis; MIMIC-IV DiReCT.PDD | English | Reused source dataset | 2 task(s) in BRIDGE |
| ADE | ADE-Identification; ADE-Extraction; ADE-Drug dosage | English | Reused source dataset | 3 task(s) in BRIDGE |
| BARR2 | BARR2 | Spanish | Reused source dataset | 1 task(s) in BRIDGE |
| BrainMRI-AIS | BrainMRI-AIS | English | Reused source dataset | 1 task(s) in BRIDGE |
| Brateca | Brateca-Hospitalization; Brateca-Mortality | Portuguese (Brazilian) | Reused source dataset with 2 BRIDGE-new task(s) | 2 task(s) in BRIDGE |
| Cantemist | Cantemist-Coding; Cantemis-NER; Cantemis-Norm | Spanish | Reused source dataset | 3 task(s) in BRIDGE |
| CARES | CARES-Area; CARES-ICD10 Chapter; CARES ICD10 Block; CARES-ICD10 Sub-Block | Spanish | Reused source dataset with 3 BRIDGE-new task(s) | 4 task(s) in BRIDGE |
| CHIP-CDEE | CHIP-CDEE | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| C-EMRS | C-EMRS | Chinese | Reused source dataset with 1 BRIDGE-new task(s) | 1 task(s) in BRIDGE |
| CLEF eHealth 2020 - CodiEsp | CodiEsp-ICD-10-CM; CodiEsp-ICD-10-PCS | Spanish | Reused source dataset | 2 task(s) in BRIDGE |
| ClinicalNotes-UPMC | ClinicalNotes-UPMC | English | Reused source dataset | 1 task(s) in BRIDGE |
| Mexican Clinical Records | PPTS | Spanish | Reused source dataset | 1 task(s) in BRIDGE |
| CLINpt | CLINpt-NER | Portuguese | Reused source dataset | 1 task(s) in BRIDGE |
| CLIP | CLIP | English | Reused source dataset | 1 task(s) in BRIDGE |
| cMedQA | cMedQA | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| DialMed | DialMed | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| DiSMed | DiSMed-NER | Spanish | Reused source dataset | 1 task(s) in BRIDGE |
| MIE | Medical entity type extraction | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| EHRQA | EHRQA-Primary department; EHRQA-Sub department; EHRQA-QA | Chinese | Reused source dataset with 3 BRIDGE-new task(s) | 3 task(s) in BRIDGE |
| Ex4CDS | Ex4CDS | German | Reused source dataset with 1 BRIDGE-new task(s) | 1 task(s) in BRIDGE |
| GOUT-CC | GOUT-CC-Consensus | English | Reused source dataset with 1 BRIDGE-new task(s) | 1 task(s) in BRIDGE |
| n2c2 2006 | n2c2 2006-De-identification | English | Reused source dataset | 1 task(s) in BRIDGE |
| i2b2 2009 | Medication extraction | English | Reused source dataset | 1 task(s) in BRIDGE |
| i2b2 2010 | n2c2 2010-Concept; n2c2 2010-Assertion; n2c2 2010-Relation | English | Reused source dataset | 3 task(s) in BRIDGE |
| n2c2 2014 - De-identification | n2c2 2014-De-identification | English | Reused source dataset | 1 task(s) in BRIDGE |
| IMCS-V2 | IMCS-V2-NER; IMCS-V2-SR; IMCS-V2-MRG; IMCS-V2-DAC | Chinese | Reused source dataset | 4 task(s) in BRIDGE |
| Japanese Case Reports | JP-STS | Japanese | Reused source dataset | 1 task(s) in BRIDGE |
| meddocan | meddocan | Spanish | Reused source dataset | 1 task(s) in BRIDGE |
| MEDIQA_2019_Task2_RQE | MEDIQA 2019-RQE | English | Reused source dataset | 1 task(s) in BRIDGE |
| MedNLI | MedNLI | English | Reused source dataset | 1 task(s) in BRIDGE |
| MedSTS | MedSTS | English | Reused source dataset | 1 task(s) in BRIDGE |
| mtsamples | MTS | English | Reused source dataset | 1 task(s) in BRIDGE |
| mtsamples-temporal | MTS-Temporal | English | Reused source dataset | 1 task(s) in BRIDGE |
| n2c2 2018 Track2 | n2c2 2018-ADE&medication | English | Reused source dataset | 1 task(s) in BRIDGE |
| NorSynthClinical | NorSynthClinical-NER; NorSynthClinical-RE | Norwegian | Reused source dataset | 2 task(s) in BRIDGE |
| NUBES | NUBES | Spanish | Reused source dataset with 1 BRIDGE-new task(s) | 1 task(s) in BRIDGE |
| MTS-Dialog-MEDIQA-2023 | MEDIQA 2023-chat-A; MEDIQA 2023-sum-A; MEDIQA 2023-sum-B | English | Reused source dataset | 3 task(s) in BRIDGE |
| RuMedDaNet | RuMedDaNet | Russian | Reused source dataset | 1 task(s) in BRIDGE |
| CHIP-CDN | CBLUE-CDN | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| CHIP-CTC | CHIP-CTC | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| CHIP-MDCFNPC | CHIP-MDCFNPC | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| MedDG | MedDG | Chinese | Reused source dataset | 1 task(s) in BRIDGE |
| n2c2 2014 - Heart Disease Challenge | n2c2 2014-Diabetes; n2c2 2014-CAD; n2c2 2014-Hyperlipidemia; n2c2 2014-Hypertension; n2c2 2014-Medication | English | Reused source dataset | 5 task(s) in BRIDGE |
| CAS | CAS-label; CAS-evidence | French | Reused source dataset | 2 task(s) in BRIDGE |
| RuMedNLI | RuMedNLI-NLI | Russian | Reused source dataset | 1 task(s) in BRIDGE |
| RuDReC | RuDReC-NER | Russian | Reused source dataset | 1 task(s) in BRIDGE |
| NorSynthClinical-PHI | NorSynthClinical-PHI | Norwegian | Reused source dataset | 1 task(s) in BRIDGE |
| RuCCoN | RuCCoN | Russian | Reused source dataset | 1 task(s) in BRIDGE |
| CLISTER | CLISTER | French | Reused source dataset | 1 task(s) in BRIDGE |
| BRONCO150 | BRONCO150-NER&Status | German | Reused source dataset | 1 task(s) in BRIDGE |
| CARDIO:DE | CARDIO-DE | German | Reused source dataset | 1 task(s) in BRIDGE |
| GraSSCo_PHI | GraSSCo PHI | German | Reused source dataset with 1 BRIDGE-new task(s) | 1 task(s) in BRIDGE |
| IFMIR | IFMIR-Incident type; IFMIR-NER; IFMIR - NER&factuality | Japanese | Reused source dataset | 3 task(s) in BRIDGE |
| iCorpus | iCorpus | Japanese | Reused source dataset | 1 task(s) in BRIDGE |
| icliniq-10k | icliniq-10k | English | Reused source dataset | 1 task(s) in BRIDGE |
| HealthCareMagic-100k | HealthCareMagic-100k | English | Reused source dataset | 1 task(s) in BRIDGE |

## 1. MIMIC-IV CDM

MIMIC-IV CDM is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MIMIC-IV CDM (Clinical Decision Making) dataset 19 is sourced from the MIMIC-IV database and focuses on patients presenting with acute abdominal pain. It includes 2,400 real patient cases covering four common abdominal pathologies and incorporates multiple types of clinical notes to simulate a realistic clinical setting, such as the history of present illness, physical examination findings, and radiology reports. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Gastroenterology
- **Application Method:** Link of MIMIC-IV CDM Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 1.1 Task: MIMIC-IV CDM

This task is to determine the most likely diagnosis based on the clinical notes of a patient with acute abdominal pain.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the history of present illness, physical examination, and radiology reports of a patient with acute abdominal pain, determine the most likely diagnosis from the following pathologies: Appendicitis, Cholecystitis, Diverticulitis, Pancreatitis. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Diagnosis: disease The optional list for "disease" is ["Appendicitis", "Cholecystitis", "Diverticulitis", "Pancreatitis"].
### Input
[Clinical note of a patient]
### Output
Diagnosis: [Appendicitis / Cholecystitis / Diverticulitis / Pancreatitis]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 2. MIMIC-III Outcome

MIMIC-III Outcome is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MIMIC-III Outcome dataset 20 contains data from 42,808 patients sourced from the MIMIC-III database and combines patients’ clinical notes with their clinical outcomes. Admission-related information, such as chief complaint and medical history, was extracted from discharge summaries to simulate a realistic scenario for prognosis prediction at the time of hospital admission. This dataset supports research on clinical outcome prediction and risk stratification. We followed the official data split (29,839 for training, 4,300 for validation, and 8,669 for testing), and further selected 1,000 cases from the test set for evaluation in our benchmark. In BRIDGE, this source dataset contributes 2 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** Discharge Summary
- **Clinical Specialty:** Critical Care
- **Application Method:** Link of Code MIMIC-III Outcome
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** We followed the official data split (29,839 for training, 4,300 for validation, and 8,669 for testing), and further selected 1,000 cases from the test set for evaluation in our benchmark.

### 2.1 Task: MIMIC-III Outcome.LoS

This task is to predict the patient’s length of stay during the current hospital admission based on information from the admission note.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given a patient’s basic information and admission notes, predict the patient’s length of stay (LOS) in the hospital, which is the hospitalization duration required by the patient’s condition. The LoS is grouped into four categories: - "A": Under 3 days - "B": 3 to 7 days - "C": 1 week to 2 weeks - "D": more than 2 weeks Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Length of Stay: label The optional list for "label" is ["A", "B", "C", "D"].
### Input
[Clinical note of a patient]
### Output
Length of Stay: [A / B / C / D]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 2.2 Task: MIMIC-III Outcome.Mortality

This task is to predict the in-hospital mortality for the current admission based on the patient’s admission note.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given a patient’s basic information and admission notes, predict the patient’s in-hospital mortality, which means whether the patient will die during the current admission. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: In-Hospital Mortality: label The optional list for "label" is ["Yes", "No"].
### Input
[Clinical note of a patient]
### Output
In-Hospital Mortality: [Yes/No]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 3. MIMIC-IV BHC

MIMIC-IV BHC is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MIMIC-IV BHC (Brief Hospital Course) dataset 21 focuses on generating brief hospital course summaries from patients’ clinical notes. It is derived from the MIMIC-IV-Note dataset and includes 270,033 clinical notes. The dataset was constructed through data translation to transforms raw, unstructured clinical text into a standardized format suitable for brief hospital course generation. This process involves steps such as whitespace removal, section identification, tokenization, and other structural transformations, ultimately producing aligned pairs of clinical notes and corresponding brief hospital course summaries. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Discharge and Administration
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Critical Care
- **Application Method:** Link of MIMIC-IV BHC Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 3.1 Task: MIMIC-IV BHC

The objective of this task is to generate the brief hospital course based on the provided clinical notes of a patient.

### Task type
Summarization

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the patient’s clinical notes from electronic health records, summarize the patient’s clinical notes into a brief hospital course (BHC) summary, which is a concise summary of the patient’s hospital stay. The BHC summary commonly is a paragraph that includes key information such as the patient’s diagnosis, treatment, and any significant events that occurred during their hospital stay. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: BHC:...
### Input
[Progress note of a patient]
### Output
BHC: [brief hospital course for the patient]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 4. MIMIC-IV DiReCT

MIMIC-IV DiReCT is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MIMIC-IV DiReCT (Diagnostic Reasoning dataset for Clinical noTes) dataset 22 focuses on disease diagnosis through diagnostic reasoning based on clinical notes. It is derived from the MIMIC-IV database and contains 511 clinical notes, each meticulously annotated by physicians to document the step-by-step diagnostic reasoning process—from clinical observations to final diagnosis. It covers 25 diseases across five clinical specialties: Cardiology, Gastroenterology, Neurology, Pulmonology, and Endocrinology. In BRIDGE, this source dataset contributes 2 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Cardiology, Gastroenterology, Neurology, Pulmonology, Endocrinology
- **Application Method:** Link of MIMIC-IV DiReCT Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 4.1 Task: MIMIC-IV DiReCT.Dis

This task is to determine which disease the patient has based on their current clinical condition.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given a patient’s clinical notes from electronic health records (EHR), determine which disease the patient has. Specifically, the clinical notes include 6 parts: CHIEF COMPLAINT, HISTORY OF PRESENT ILLNESS, PAST MEDICAL HISTORY, FAMILY HISTORY, PHYSICAL EXAM, and PERTINENT RESULTS. The possible disease is one of the following list. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Diagnosis: disease The optional list for "disease" is ["Acute Coronary Syndrome", "Heart Failure", "Gastro-oesophageal Reflux Disease", "Pulmonary Embolism", "Hypertension", "Peptic Ulcer Disease", "Stroke", "Gastritis", "Multiple Sclerosis", "Adrenal Insufficiency", "Pneumonia", "Chronic Obstructive Pulmonary Disease", "Aortic Dissection", "Asthma", "Diabetes", "Pituitary Disease", "Alzheimer", "Atrial Fibrillation", "Thyroid Disease", "Cardiomyopathy", "Epilepsy", "Upper Gastrointestinal Bleeding", "Tuberculosis", "Migraine", "Hyperlipidemia"].
### Input
[Clinical note of a patient]
### Output
Diagnosis: [valid disease name]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 4.2 Task: MIMIC-IV DiReCT.PDD

This task is to determine the patient’s primary discharge diagnosis (PDD) based on their current clinical condition.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given a patient’s clinical notes from electronic health records (EHR), determine which disease the patient has. Specifically, the clinical notes include 6 parts: CHIEF COMPLAINT, HISTORY OF PRESENT ILLNESS, PAST MEDICAL HISTORY, FAMILY HISTORY, PHYSICAL EXAM, and PERTINENT RESULTS. The possible disease is one of the following list. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Diagnosis: disease The optional list for "disease" is ["Heart Failure", "Gastro-oesophageal Reflux Disease", "Hypertension", "Non-ST-Elevation Myocardial Infarction", "Relapsing-Remitting Multiple Sclerosis", "Unstable Angin", "Low-risk Pulmonary Embolism", "Gastric Ulcers", "Chronic Obstructive Pulmonary Disease", "Bacterial Pneumonia", "ST-Elevation Myocardial Infarction", "Hemorrhagic Stroke", "Acute Gastritis", "Ischemic Stroke", "Submassive Pulmonary Embolism", "Pituitary Macroadenoma", "Secondary Adrenal Insufficiency", "Alzheimer", "Type B Aortic Dissection", "Duodenal Ulcers", "Chronic Atrophic Gastritis", "Paroxysmal Atrial Fibrillation", "Primary Adrenal Insufficiency", "Upper Gastrointestinal Bleeding", "Type I Diabetes", "Type II Diabetes", "Chronic Non-atrophic Gastritis", "Type A Aortic Dissection", "Non-epileptic Seizure", "Tuberculosis", "Viral Pneumonia", "Severe Asthma Exacerbation", "Hyperthyroidism", "Dilated Cardiomyopathy", "Congenital Adrenal Hyperplasia", "Epilepsy", "Non-Allergic Asthma", "Migraine With Aura", "Secondary Progressive Multiple Sclerosis", "Hypothyroidism", "Massive Pulmonary Embolism", "Hyperlipidemia", "Restrictive Cardiomyopathy", "Asthma", "COPD Asthma", "Hypertrophic Cardiomyopathy", "Persistent Atrial Fibrillation", "Thyroid Nodules", "Primary Progressive Multiple Sclerosis", "Allergic Asthma", "Cough-Variant Asthma", "Arrhythmogenic Right Ventricular Cardiomyopathy", "Migraine Without Aura", "Thyroiditis", "Pituitary Microadenoma"].
### Input
[Clinical note of a patient]
### Output
[Diagnosis: [valid disease name]]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 5. ADE

ADE is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The ADE dataset 23 was constructed from 3,000 English clinical case reports focused on adverse drug effects. Through multi-round systematic annotation, the dataset captures mentions of drugs, adverse effects, dosages, and the relationships among them. All entities and relations were annotated with rigorous quality control to ensure the dataset’s reliability for medication information extraction research. This dataset supports three distinct tasks. In BRIDGE, this source dataset contributes 3 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** Pharmacology
- **Application Method:** Link of ADE Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 5.1 Task: ADE-Identification

This task is to determine whether a sentence contains information about ADEs.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text, determine whether the text mentions adverse drug effects. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: adverse drug effect: label The optional list for "label" is ["Yes", "No"].
### Input
[A snippet from a case report]
### Output
adverse drug effect: [Yes / No]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 5.2 Task: ADE-Extraction

This task is to extract all potential drugs and their associated adverse effects mentioned in the sentence.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text, identify all the drugs and their corresponding adverse effect mentioned in the text. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: drug:..., adverse effect:...;... drug:..., adverse effect:...;
### Input
[A snippet from a case report. ]
### Output
drug: [drug name], adverse effect: [text of ADE information];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 5.3 Task: ADE-Drug dosage

This task is to extract all potential drugs and their associated adverse effects mentioned in the sentence.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text, identify all the drugs and their corresponding dosage information mentioned in the text. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: drug:..., dosage:...;... drug:..., dosage:...;
### Input
[A snippet from a case report]
### Output
drug: [drug name], dosage: [text of dosage information];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 6. BARR2

BARR2 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The BARR2 (Biomedical Abbreviation Recognition and Resolution, 2nd Edition) dataset 24 is a Spanish dataset designed for the recognition and resolution of biomedical abbreviations. It includes 24.5 million tokens of Spanish clinical case study sections compiled from various clinical disciplines, and forms part of a larger 1.1 billion-token biomedical corpus created by the Barcelona Supercomputing Center (BSC). The dataset comprises clinical case reports extracted from Spanish medical literature, annotated and structured for training and evaluation of biomedical language models. The annotations in derived tasks like PharmaCoNER and CANTEMIST were conducted using curated guidelines for biomedical and oncological entities. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of BARR2 Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The dataset comprises clinical case reports extracted from Spanish medical literature, annotated and structured for training and evaluation of biomedical language models.

### 6.1 Task: BARR2

This task is to extract the clinical abbreviations from the text and resolve each of them with their definitions.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Spanish, extract the clinical abbreviations from the text and resolve each of them with their definitions. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: abbreviation:..., definition:...;... abbreviation:..., definition:...;
### Input
[A snippet from a case report]
### Output
abbreviation: [clinical abbreviation], definition: [resolved clinical abbreviation];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 7. BrainMRI-AIS

BrainMRI-AIS is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. BrainMRI-AIS 25 dataset comprises 3,024 brain MRI radiology reports, focusing on the identification of acute ischemic stroke (AIS). It consists of free-text radiology reports collected between January 2015 and December 2016 from Hallym University Sacred Heart Hospital in Korea. Reports were manually annotated with AIS or non-AIS labels by medical experts to ensure high-quality labeling. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** Radiology Report
- **Clinical Specialty:** Neurology, Radiology
- **Application Method:** Link of BrainMRI-AIS Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 7.1 Task: BrainMRI-AIS

This task is to determine if the patient has an acute ischemic stroke.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given a brain Magnetic Resonance Imaging (MRI) radiology report, determine whether the patient has acute ischemic stroke (AIS). Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: AIS: label The optional list for "label" is ["Yes", "No"].
### Input
[A brain magnetic resonance imaging (MRI) radiology report of a patient]
### Output
AIS: [Yes / No]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 8. Brateca

Brateca is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. Brateca 26 is a Portuguese-language dataset consisting of over 70,000 admissions and 2.5 million clinical notes and structured documents, including health records, prescription data, and exam results. The dataset was collected from 10 hospitals across two Brazilian states. Documents were annotated and deidentified with BiLSTM-CRF models and manually reviewed by clinical researchers, following HIPAA guidelines. The following tasks were newly constructed based on this dataset as part of our BRIDGE benchmark. In BRIDGE, this source dataset contributes 2 task(s) and is normalized as a reused source dataset / sub-benchmark with 2 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** Portuguese (Brazilian)
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Link of Brateca Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 2 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 8.1 Task: Brateca-Hospitalization

This task is to predict whether the patient will require more than seven days of hospitalization.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. For each patient, we extracted all clinical notes recorded during hospital visits and selected the admission-day notes, including both examination results and admission summaries. The input features include age, skin color, sex, weight, and height, while the output label indicates whether the patient’s length of stay during the current hospitalization exceeded seven days.

```md
### Instruction
Given a patient’s basic information and clinical notes in Portuguese, predict whether the patient will require more than seven days of hospitalization. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Hospitalization > 7 days: label The optional list for "label" is ["Yes", "No"].
### Input
[Clinical notes of a patient]
### Output
Hospitalization > 7 days: [Yes / No]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 8.2 Task: Brateca-Mortality

This task is to predict whether the clinical outcome for the patient is survival or death.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. For every patient, we collected all notes corresponding to the day of admission (including examination results and admission notes), together with basic demographic variables including age, skin color, sex, weight, and height. The target variable represents the clinical outcome, categorized as either survival or death during hospitalization.

```md
### Instruction
Given a patient’s basic information and clinical notes in Portuguese, predict whether the clinical outcome for this patient is survival or death. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Survival: status The optional list for "status" is ["Yes", "No"].
### Input
[Clinical notes of a patient]
### Output
Survival: [Yes / No]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 9. Cantemist

Cantemist is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The Cantemist corpus 27 comprises 3,000 clinical cases centered on cancer-related data in Spanish. This corpus was curated by human clinical coding experts, who manually annotated tumor morphology entities and mapped them to the Spanish version of the International Classification of Diseases for Oncology (ICD-O). The annotation process was conducted using the BRAT annotation tool, adhering to well-defined annotation guidelines established by the Spanish Ministry of Health. In BRIDGE, this source dataset contributes 3 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Discharge and Administration
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** Oncology
- **Application Method:** Link of Cantemist Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 9.1 Task: Cantemist-Coding

This task is to generate a ranked list of all morphology codes for tumor morphologies mentioned in the text according to CIE-O (Clasificación Internacional de Enfermedades para Oncología), the Spanish adaptation of the International Classification of Diseases for Oncology (ICD-O).

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical document in Spanish, identify the entities of tumor morphology and determine the corresponding morphology codes. Specifically, the entities of tumor morphology can be linked to a morphology code from CIE-O (Clasificación Internacional de Enfermedades para Oncología, i.e., the Spanish equivalent of ICD-O, version 3.1). - "Tumor morphology": Una neoplasia es un crecimiento o formación de tejido nuevo, anormal, especialmente de carácter tumoral, benigno o maligno. La clasificación de las neoplasias según su morfología o características histológicas hace referencia a la forma y estructura de las células tumorales que se estudian para clasificar las neoplasias según su tejido de origen. El tejido de origen y el tipo de células que componen una morfología determinan a menudo la tasa de crecimiento esperada, la gravedad de la enfermedad y el tipo de tratamiento recomendado. - "Morphology code": The morphology code is a code from CIE-O that represents the morphology of the tumor. This code is used to classify the tumor morphology in a standardized way. A code consists of a four-digit morphology code indicating the tumor’s histological type, followed by a slash and a single digit indicating the tumor’s behavior. Assuming the number of normalized morphology codes is N, return the N normalized codes in the output. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Morphology code: code 1, code 2,..., code N The optional list for "code" is the normalized code from CIE-O.
### Input
[Clinical case of cancer patient in Spanish]
### Output
Morphology code: [N normalized codes]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as document-level normalization/coding because the output is a normalized label/code list rather than entity spans. BRIDGE evaluates document-level normalization/coding with Accuracy as the primary metric, plus micro F1 and macro F1. Invalid outputs are replaced with random valid labels.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 9.2 Task: Cantemis-NER

This task is to extract all entities of tumor morphology mentioned in the text.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text related to cancer in Spanish, extract all entities about tumor morphology mentioned in the text. - "Tumor morphology": Una neoplasia es un crecimiento o formación de tejido nuevo, anormal, especialmente de carácter tumoral, benigno o maligno. La clasificación de las neoplasias según su morfología o características histológicas hace referencia a la forma y estructura de las células tumorales que se estudian para clasificar las neoplasias según su tejido de origen. El tejido de origen y el tipo de células que componen una morfología determinan a menudo la tasa de crecimiento esperada, la gravedad de la enfermedad y el tipo de tratamiento recomendado. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type: tumor morphology;... entity:..., type: tumor morphology;
### Input
[Clinical case of cancer patient in Spanish]
### Output
entity: [tumor morphology mention], type: tumor morphology;
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 9.3 Task: Cantemis-Norm

This task is to extract all entities about tumor morphology mentioned in the text and identify their corresponding morphology codes according to CIE-O (Clasificación Internacional de Enfermedades para Oncología), the Spanish adaptation of the International Classification of Diseases for Oncology (ICD-O).

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text related to cancer in Spanish, extract all entities about tumor morphology and identify their corresponding morphology codes. Specifically, every entity of tumor morphology is linked to a morphology code from CIE-O (Clasificación Internacional de Enfermedades para Oncología, i.e., the Spanish equivalent of ICD-O, version 3.1). - "Tumor morphology": Una neoplasia es un crecimiento o formación de tejido nuevo, anormal, especialmente de carácter tumoral, benigno o maligno. La clasificación de las neoplasias según su morfología o características histológicas hace referencia a la forma y estructura de las células tumorales que se estudian para clasificar las neoplasias según su tejido de origen. El tejido de origen y el tipo de células que componen una morfología determinan a menudo la tasa de crecimiento esperada, la gravedad de la enfermedad y el tipo de tratamiento recomendado. - "Morphology code": The morphology code is a code from CIE-O that represents the morphology of the tumor. This code is used to classify the tumor morphology in a standardized way. A code consists of a four-digit morphology code indicating the tumor’s histological type, followed by a slash and a single digit indicating the tumor’s behavior. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., code:...;... entity:..., code:...; The optional list for "code" is the normalized code from CIE-O.
### Input
[Clinical case of cancer patient in Spanish]
### Output
entity: [tumor morphology mention], code: [CIE-O code];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as entity-level normalization/coding because the output requires entity-to-code pairs. BRIDGE evaluates entity-level normalization/coding with event-level micro F1 as the primary metric and subject-level micro F1 as a secondary metric. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 10. CARES

CARES is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CARES 28 is a Spanish-language dataset including 3,219 anonymized radiological reports and 6,907 sub-code annotations. It was designed for the ICD-10 classification of free-text radiological reports. Each report was labeled with one or more ICD-10 sub-codes from a total of 223 unique sub-codes, which correspond to 156 distinct ICD-10 codes and 16 different chapters of the ontology. Annotations were carried out by a team of four expert radiologists with over 10 years of experience, following the official ICD-10 coding standards. In BRIDGE, this source dataset contributes 4 task(s) and is normalized as a reused source dataset / sub-benchmark with 3 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Discharge and Administration
- **Source Clinical Document Type:** Radiology Report
- **Clinical Specialty:** Radiology
- **Application Method:** Link of CARES Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 3 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 10.1 Task: CARES-Area

This task is to determine which anatomical area of the body that a radiographic report refers to.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. Based on the report source and type information, we link the raw report to its corresponding anatomical region as described in the report, which demonstrates the clinical focus of each report.

```md
### Instruction
Given a radiology report in Spanish, determine which anatomical area of the body the report refers to. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: anatomical area: label The optional list for "label" is [’Columna’, ’Neuro’, ’Musculoskeletal’, ’Body’].
### Input
[A radiology report in Spanish]
### Output
anatomical area: [Columna / Neuro / Musculoskeletal / Body]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 10.2 Task: CARES-ICD10 Chapter

This task is to identify the appropriate chapters of ICD-10 that correspond to the condition mentioned in the radiology report.

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given a radiology report in Spanish, determine the appropriate chapters of ICD-10 corresponding to the conditions mentioned in the report. Specifically, the chapter is the highest level of the ICD-10 classification and each chapter represents a group of related diseases. Each chapter is identified by a Roman numeral from I to XXII, including the following chapters: - "I": Certain infectious and parasitic diseases (A00–B99) - "II": Neoplasms (C00–D49) - "III": Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism (D50–D89) - "IV": Endocrine, nutritional, and metabolic diseases (E00–E89) - "V": Mental, Behavioral and Neurodevelopmental disorders (F01–F99) - "VI": Diseases of the nervous system (G00–G99) - "VII": Diseases of the eye and adnexa (H00–H59) - "VIII": Diseases of the ear and mastoid process (H60–H95) - "IX": Diseases of the circulatory system (I00–I99) - "X": Diseases of the respiratory system (J00–J99) - "XI": Diseases of the digestive system (K00–K95) - "XII": Diseases of the skin and subcutaneous tissue (L00–L99) - "XIII": Diseases of the musculoskeletal system and connective tissue (M00–M99) - "XIV": Diseases of the genitourinary system (N00–N99) - "XV": Pregnancy, childbirth, and the puerperium (O00–O9A) - "XVI": Certain conditions originating in the perinatal period (P00–P96) - "XVII": Congenital malformations, deformations, and chromosomal abnormalities (Q00–Q99) - "XVIII": Symptoms, signs, and abnormal clinical and laboratory findings, not elsewhere classified (R00–R99) - "XIX": Injury, poisoning, and certain other consequences of external causes (S00–T88) - "XX": External causes of morbidity (V00–Y99) - "XXI": Factors influencing health status and contact with health services (Z00–Z99) - "XXII": Codes for special purposes (U00–U85) This report may contain multiple conditions and is related to multiple chapters. Assuming the number of appropriate chapters is N, return the codes of N appropriate chapters in the output. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: ICD-10 chapter: code 1, code 2,..., code N The optional list for "code" is ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX", "XXI", "XXII"].
### Input
[A radiology report in Spanish]
### Output
ICD-10 chapter: chapter 1, chapter 2,..., chapter N (with each code is from ICDO-10 sub block code)
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as document-level normalization/coding because the output is a normalized label/code list rather than entity spans. BRIDGE evaluates document-level normalization/coding with Accuracy as the primary metric, plus micro F1 and macro F1. Invalid outputs are replaced with random valid labels.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 10.3 Task: CARES ICD10 Block

This task is to identify the appropriate block code of ICD-10 that corresponds to the condition mentioned in the radiology report.

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. Each report was linked to one or more ICD-10 block codes, capturing the best matched to the diagnostic descriptions contained in each report.

```md
### Instruction
Given a radiology report in Spanish, determine the appropriate ICD-10 block codes corresponding to the conditions mentioned in the report. Specifically, the block code is the second level of the ICD-10 classification and represents a group of related diseases. Each block code is identified by a code containing a character and two digits, which indicates its chapter and detailed block. This report may contain multiple conditions and is related to multiple block codes. Assuming the number of appropriate block codes is N, return the codes for the N appropriate blocks in the output. Notably, the required block code is a combination of the chapter and the block, such as "I00", "I01", rather than the coarse range of the block, such as "I00-I99". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: ICD-10 block: code 1, code 2,..., code N
### Input
[A radiology report in Spanish]
### Output
[ICD-10 block: code 1, code 2,..., code N (each code is from ICDO-10 block code)]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as document-level normalization/coding because the output is a normalized label/code list rather than entity spans. BRIDGE evaluates document-level normalization/coding with Accuracy as the primary metric, plus micro F1 and macro F1. Invalid outputs are replaced with random valid labels.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 10.4 Task: CARES-ICD10 Sub-Block

This task is to identify the appropriate subblock code of ICD-10 that corresponds to the condition mentioned in the radiology report.

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. Each report was linked to one or more ICD-10 sub-block codes, capturing finergrained diagnostic distinctions within the broader ICD-10 block categories.

```md
### Instruction
Given a radiology report in Spanish, determine the appropriate ICD-10 sub-block codes corresponding to the conditions mentioned in the report. Specifically, the sub-block code is the third level of the ICD-10 classification and represents several related diseases. Each sub-block code is identified by a code containing a character, two digits, and a decimal, which indicates its chapter, block, and detailed sub-block. This report may contain multiple conditions and is related to multiple sub-block codes. Assuming the number of appropriate sub-blocks is N, return the codes for N appropriate sub-blocks in the output. Notably, the required sub-block code is a combination of the chapter, the block, and the sub-block, such as "I00.0", "I01.0", rather than the coarse range of the sub-block, such as "I00.0-I99.9". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: ICD-10 sub-block: code 1, code_2,..., code N.
### Input
[A radiology report in Spanish]
### Output
ICD-10 sub-block: code 1, code 2,..., code N. (with each code is from ICDO-10 chapter code)
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as document-level normalization/coding because the output is a normalized label/code list rather than entity spans. BRIDGE evaluates document-level normalization/coding with Accuracy as the primary metric, plus micro F1 and macro F1. Invalid outputs are replaced with random valid labels.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 11. CHIP-CDEE

CHIP-CDEE is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CHIP-CDEE (CHIP- Clinical Discovery Event Extraction dataset) dataset 29 consists of 1,971 clinical text sourced from disease history and imaging reports in Chinese EHRs. It focuses on the extraction of clinical findings, referring broadly to patient-reported symptoms and examination-derived abnormalities, including signs and manifestations. The dataset requires identifying four attributes for each clinical finding: the subject term, descriptive term, anatomical location, and occurrence status. It was one of the shared tasks in the CHIP-2021 challenge and is included in the CBLUE benchmark 30. We adapted the CBLUE version for downstream task construction. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Initial Assessment
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Link of CHIP-CDEE Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 11.1 Task: CHIP-CDEE

This task is to extract clinical findings and their associated attributes: description, location, and status.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text from electronic healthcare records in Chinese, extract all the clinical findings and their attributes. 具体而言，给定一段现病史或者医学影像所见报告，要求从中抽取临床 发现事件的四个属性: 解剖部位、主体词、描述词，以及发生状态: 1. 主体词(subject)：指患者的电子病历中的疾病名称或者由疾病引发的症状，也包括患者的一般 情况如饮食，二便，睡眠等。主体词尽可能完整并是专有名词，比如“麻木， 疼痛，发烧，囊 肿”等；专有名词，如“头晕”，晕只能发生在头部，“胸闷”，闷只能发生在胸部，所以不进行拆 分，保留完整的专有名词。涉及泛化的症状不做标注，如“无其他不适”，句子中的“不适”不需 要标注，只针对具体的进行标注。注意：有较小比例的主体词会映射到ICD标准术语，所使用 的ICD的版本为“国际疾病分类 ICD-10北京临床版v601.xIsx” 2. 描述词(description)：对主体词的发生时序特征、轻重程度、形态颜色等多个维度的刻画，也包 括疾病的起病缓急、突发 3. 解剖部位(location)：指主体词发生在患者的身体部位，也包括组织， 细胞，系统等，也包括部位的方向和数量 4. 发生状态(status)：“肯定”，“否定”或“不确定”，表示该主体词在患者的电子病历中的存在状态 Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: subject:..., description: [...,...], location: [...,...], status:...;... subject:..., description: [...,...], location: [...,...], status:...; The optional list for "status" is ["肯定", "否定", "不确定"]; If there is not a description or location, they should be "[]"; if there are multiple descriptions or locations, they should be separated by commas in the list, like [...,...].
### Input
[Clinical text from EHRs]
### Output
subject: [subject terms], description: [descriptive words], location: [location mention], status: [肯 定/否定/不确定];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 12. C-EMRS

C-EMRS is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. C-EMRs 31 is a collection of 18,590 Chinese electronic medical records, designed for automated clinical diagnosis. It was collected from Huangshi Central Hospital, consisting of a variety of medical cases such as hypertension, diabetes, COPD, etc. across departments. Records in the dataset include fields such as chief complaint, physical examination, and labels such as diseases. Annotations were obtained through expert diagnosis and manually aligned for classification tasks. - Language: Chinese - Clinical Stage: Diagnosis and Prognosis - Sourced Clinical Document Type: General EHR Note - Clinical Specialty: Radiology, Endocrinology, Pulmonology, Cardiology, Gastroenterology - Application Method: Link of C-EMRS Dataset In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Radiology, Endocrinology, Pulmonology, Cardiology, Gastroenterology
- **Application Method:** Link of C-EMRS Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 12.1 Task: C-EMRS

This task is to diagnose the disease this patient has.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. Based on the structured EHRs provided in the dataset, we constructed a comprehensive input by aggregating multiple categories of medical information, including the chief complaint, surgical history, vital signs, specialty findings, general condition, allergy history, nutritional status, suicidal tendency, specialty examinations, surgical or trauma history, comorbidities, present illness, obstetric history, auxiliary examinations, personal history, past medical history, and family history. These elements were integrated and reformulated into a standardized clinical case report. The output label represents the physician-diagnosed disease.

```md
### Instruction
Given a clinical electronic health record in Chinese, diagnose the disease this patient has. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: diagnosis: disease The optional list for "disease" is ["胃息肉", "泌尿道感染", "慢性阻塞性肺病", "痛风", "胃溃疡", "高血 压", "哮喘", "胃炎", "心律失常", "糖尿病"].
### Input
[Clinical electronic health record in Chinese]
### Output
diagnosis: [胃息肉 / 泌尿道感染 / 慢性阻塞性肺病 / 痛风 / 胃溃疡 / 高血压 / 哮喘 / 胃炎 / 心 律失常 / 糖尿病];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 13. CLEF eHealth 2020 - CodiEsp

CLEF eHealth 2020 - CodiEsp is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CodiEsp dataset 32 is a Spanish dataset designed for automatic clinical coding, particularly the assignment of ICD-10-CM (diagnoses) and ICD-10-PCS (procedures) codes to medical documents. It includes 1,000 manually annotated clinical case reports comprising over 18435 annotations and 3427 unique ICD-10 codes, curated by professional clinical coders from the Barcelona Supercomputing Center. These documents span diverse medical specialties and contain both diagnostic and procedural information. The dataset consists of plain text clinical narratives, with annotations including ICD-10 codes and the corresponding textual evidence justifying each code. Annotations were conducted in accordance with the 2018 Spanish ICD-10 coding manuals, using an iterative validation process to ensure annotation quality. In BRIDGE, this source dataset contributes 2 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Discharge and Administration
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of CLEF eHealth 2020 - CodiEsp Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** Annotations were conducted in accordance with the 2018 Spanish ICD-10 coding manuals, using an iterative validation process to ensure annotation quality.

### 13.1 Task: CodiEsp-ICD-10-CM

Task description not cleanly recoverable from source text.

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Spanish, extract the clinical diagnosis from the clinical records and convert each of them into ICD-10-CM codes. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: diagnosis:..., ICD-10-CM:...;... diagnosis:..., ICD-10-CM:...;
### Input
[Clinical text of a patient]
### Output
diagnosis: [clinical diagnosis], ICD-10-CM: [ICD-10-CM code];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as entity-level normalization/coding because the output requires entity-to-code pairs. BRIDGE evaluates entity-level normalization/coding with event-level micro F1 as the primary metric and subject-level micro F1 as a secondary metric. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 13.2 Task: CodiEsp-ICD-10-PCS

This task is to extract clinical procedures from the clinical records and convert each of them into ICD-10-PCS codes.

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Spanish, extract clinical procedures from the clinical records and convert each of them into ICD-10-PCS codes. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: procedure:..., ICD-10-PCS:...;... procedure:..., ICD-10-PCS:...;
### Input
[Clinical text of a patient]
### Output
procedure: [clinical procedure], ICD-10-PCS: [ICD-10-PCS code];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as entity-level normalization/coding because the output requires entity-to-code pairs. BRIDGE evaluates entity-level normalization/coding with event-level micro F1 as the primary metric and subject-level micro F1 as a secondary metric. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 14. ClinicalNotes-UPMC

ClinicalNotes-UPMC is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. ClinicalNotes-UPMC 33 is a dataset comprising 2376 clinical phrases and sentences, collected from the University of Pittsburgh Medical Center. It was extracted from 120 reports of 6 types (emergency department, discharge summaries, surgical pathology, radiology, operative notes, echocardiograms). Each sentence was labeled by physicians, indicating whether the context is negated or affirmed. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Link of ClinicalNotes-UPMC Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 14.1 Task: ClinicalNotes-UPMC

This task is to determine whether the provided concept is Affirmed or Negated.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given a sentence from clinical notes, determine whether the provided concept is Affirmed or Negated. Specifically, if the concept is mentioned in the sentence and it is negated, then the label is "No". If the concept is mentioned in the sentence and it is affirmed, then the label is "Yes". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: affirmed: label The optional list for "label" is ["Yes", "No"].
### Input
[Sentence in clinical notes]
### Output
affirmed: [Yes / No]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 15. Mexican Clinical Records

Mexican Clinical Records is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The Mexican Clinical Records dataset 34 is a Spanish dataset designed for automatic classification of pneumonia and pulmonary thromboembolism (PTE). It includes 173 clinical records compiled from the Mexican Social Security Institute (IMSS). The dataset contains electronic health records, including structured data (e.g., laboratory studies, vital signs) and unstructured data (e.g., clinical notes and discharge summaries), covering diagnostic challenges in respiratory conditions. Annotations were based on ICD-10 classifications, and data preprocessing included regular expression extraction and relational database modeling. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Pulmonology
- **Application Method:** Link of Mexican Clinical Records Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 15.1 Task: PPTS

This task is to determine if the patient has pneumonia or pulmonary thromboembolism.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Spanish, label the patient into one of the following: - "pneumonia": The patient has pneumonia. - "thromboembolism": The patient has pulmonary thromboembolism. - "control": The patient has neither pneumonia nor pulmonary thromboembolism. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: answer: label The optional list for "label" is ["pneumonia", "thromboembolism", "control"].
### Input
[Clinical text of a patient]
### Output
answer: [pneumonia / thromboembolism / control]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 16. CLINpt

CLINpt is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CLINpt dataset 35 is a Portuguese dataset designed for named entity recognition in clinical text. The dataset is collected from the Sinapse journal and the Neurology service of the Coimbra University Hospital Centre. The dataset contains clinical narratives such as admission notes, diagnostic test reports, and discharge letters, focusing on neurology. Annotations were performed manually using the IOB format and revised by biomedical and data science experts, adhering to guidelines developed with physicians and linguists. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Portuguese
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Case Report, Admission Note, Discharge Summary
- **Clinical Specialty:** Neurology
- **Application Method:** Link of CLINpt Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 16.1 Task: CLINpt-NER

Task description not cleanly recoverable from source text.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Portuguese, extract the following types of entities from the clinical text: "characterization", "test", "evolution", "genetics", "anatomical Site", "negation", "additional observations", "condition", "results", "dateTime", "therapeutics", "value", "route of administration". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["characterization", "test", "evolution", "genetics", "anatomical Site", "negation", "additional observations", "condition", "results", "dateTime", "therapeutics", "value", "route of administration"].
### Input
[Clinical text of a patient]
### Output
entity: [clinical entity], type: [characterization / test / evolution / genetics / anatomical Site / negation / additional observations / condition / results / dateTime / therapeutics / value / route of administration];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 17. CLIP

CLIP is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. CLIP 36 is an English dataset focused on extracting actionable clinical items from hospital discharge summaries. It comprises 718 discharge notes with more than 107, 000 sentences, collected from the popular clinical dataset MIMIC-III. The notes were annotated with seven types of follow-up action items such as label tests, procedures, etc. Annotations were performed by five medical professionals with custom-built annotation tools. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Discharge and Administration
- **Source Clinical Document Type:** Discharge Summary
- **Clinical Specialty:** Critical Care
- **Application Method:** Link of CLIP Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 17.1 Task: CLIP

This task is to identify the clinical action items for physicians from hospital discharge notes.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the discharge summary of a patient, identify the clinical action items for physicians from hospital discharge notes. Specifically, the clinical action items include the following types: - "Patient Instructions": Post-discharge instructions that are directed to the patient, so the PCP (primary care provider) can ensure the patient understands and performs them, such as: ’No driving until post-op visit and you are no longer taking pain medications.’ - "Appointment": Appointments to be made by the PCPs, or monitored to ensure the patient attends them, such as: ’The patient requires a neurology consult at XYZ for evaluation.’ - "Medications": Medications that the PCP either needs to ensure that the patient is taking correctly (e.g., time-limited medications) or new medications that may need dose adjustment, such as: ’The patient was instructed to hold ASA and refrain from NSAIDs for 2 weeks.’ - "Lab": Laboratory tests that either have results pending or need to be ordered by the PCP, such as: ’We ask that the patients’ family physician repeat these tests in 2 weeks to ensure resolution.’ - "Procedure": Procedures that the PCP needs to either order, ensure another caregiver orders, or ensure the patient undergoes, such as: ’Please follow-up for EGD with GI.’ - "Imaging": Imaging studies that either have results pending or need to be ordered by the PCP, such as: ’Superior segment of the left lower lobe: rounded density which could have been related to infection, but follow-up for resolution recommended to exclude possible malignancy.’ - "Other": Other actionable information that is important to relay to the PCP but does not fall under existing aspects (e.g., the need to closely observe the patient’s diet, or fax results to another provider), such as: ’Since the patient has been struggling to gain weight this past year, we will monitor his nutritional status and trend weights closely.’ Assuming the number of action items is N, return the N recognized action items in the output. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: action items: item 1, item 2,..., item N The optional list for "item" is ["Patient Instructions", "Appointment", "Medications", "Lab", "Procedure", "Imaging", "Other"].
### Input
[Discharge summary of a patient]
### Output
action items: one or more of the above labels
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 18. cMedQA

cMedQA is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The cMedQA datasets contain two versions called cMedQA v1.0 37 and cMedQA v2.0 38. cMedQA v1.0 is a Chinese-language dataset comprising medical question answer (QA) from an online Chinese healthcare forum (http://www.xywy.com). In the corpus of the dataset, questions contain symptoms, diagnosis, treatment, drug usage, etc., and corresponding answers are written by certified doctors. This dataset consists of 54,000 questions and over 101,000 answers. cMedQA v2.0 is an expanded and refined version of cMedQA v1.0. The cMedQA v2.0 dataset contains double the amount of data compared to v1.0 and refined the data processing steps such as standardization and noise reduction. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Triage and Referral
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** General
- **Application Method:** Link of cMedQA Dataset1, Link of cMedQA Dataset2
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 18.1 Task: cMedQA

This task is to generate answers from a doctor’s perspective in Chinese for a medical consultation.

### Task type
Question Answering

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical consultation in Chinese, generate the anser from a doctor’s perspective in Chinese. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION:
### Input
[Medical consultation]
### Output
[responses for the medical consultation]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 19. DialMed

DialMed is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. DialMed 39 is a collection of 11,996 annotated medical dialogues in Chinese language, designed for medication recommendation in telemedicine consultations. Records in this dataset are collected from the Chunyu-Doctor platform and consist of high-quality interactions between doctors and patients. This dataset covers 16 common diseases from three departments and 70 standardized medications. The annotations of the dataset were performed by three annotators with relevant medical backgrounds and under the guidance of a doctor, and the consistency was checked with Cohen’s kappa coefficient. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** Pulmonology, Gastroenterology, Dermatology, Pharmacology
- **Application Method:** Link of DialMed Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 19.1 Task: DialMed

This task is to recommended medications for a medical consultation record in Chinese.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical consultation record in Chinese, where the recommended medications from the doctor are masked as "[MASK]", predict those recommended medications. Note that the number of medications is equal to the number of "[MASK]", assumed to be N. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: medication: label 1, label 2,..., label N The optional list for "label" is: ["酮康唑", "板蓝根", "右美沙芬", "莫沙必利", "风寒感冒颗粒", "双黄 连口服液", "蒲地蓝消炎口服液", "水飞蓟素", "米诺环素", "氯雷他定", "布地奈德", "苏黄止咳胶囊", "胶体果胶铋", "哈西奈德", "谷胱甘肽", "二硫化硒", "泰诺", "硫磺皂", "对乙酰氨基酚", "奥司他韦", "甘草酸苷", "红霉素", "西替利嗪", "克拉霉素", "氢化可的松", "复方甲氧那明胶囊", "三九胃泰", "替 诺福韦", "健胃消食片", "炉甘石洗剂", "蒙脱石", "曲美布汀", "阿奇霉素", "扶正化瘀胶囊", "依巴斯 汀", "感冒灵", "他克莫司", "氨溴索", "康复新液", "多烯磷脂酰胆碱", "恩替卡韦", "桉柠蒎肠溶软胶 囊", "曲安奈德", "甘草片", "左氧氟沙星", "奥美拉唑", "铝镁化合物", "复方消化酶", "头孢类", "甲氧 氯普胺", "地塞米松", "美沙拉秦", "双环醇", "肠炎宁", "抗病毒颗粒", "阿莫西林", "川贝枇杷露", "谷 氨酰胺", "山莨菪碱", "阿达帕林", "孟鲁司特", "糠酸莫米松", "快克", "布洛芬", "益生菌", "通窍鼻炎 颗粒", "阿昔洛韦", "生理氯化钠溶液", "连花清瘟胶囊", "黄连素"].
### Input
[Medical consultation record]
### Output
medication: [one or more of the above labels];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 20. DiSMed

DiSMed is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The DiSMed dataset 40 is a Spanish dataset designed for named entity recognition applied to the de-identification of medical texts. It includes 692 manually annotated radiology reports, compiled from the Medical Imaging Databank of the Valencian Region (BIMCV). The dataset contains brain imaging radiology reports, covering a range of patient-related data that may include identifying information. Annotations were performed manually by three annotators, using a set of six named entity categories derived from the HIPAA-defined Protected Health Information (PHI) and additional relevant entities. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Radiology Report
- **Clinical Specialty:** Radiology
- **Application Method:** Link of DiSMed Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 20.1 Task: DiSMed-NER

Task description not cleanly recoverable from source text.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Spanish, extract the following types of entities from the clinical text: - "NAME": Names and surnames (patient and others) - "DIR": Full addresses, including streets, numbers and zip codes. - "LOC": Cities, inside and outside addresses. - "NUM": Numbers or alphanumeric strings that might identify someone, including digital signatures, patient numbers, medical numbers, medical license numbers, and others. - "FECHA": Dates. - "INST": Hospitals, healthcare centers, or other institutions that might point to someone’s location. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["NAME", "DIR", "LOC", "NUM", "FECHA", "INST"].
### Input
[Clinical text of a patient]
### Output
entity: [clinical entity], type: [NAME / DIR / LOC / NUM / FECHA / INST];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 21. MIE

MIE is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. MIE 41 is a Chinese language dataset designed for extracting medical information from online consultations. It comprises 1,120 medical dialogues segmented in over 18,000 windows and 46,000 labels. The corpus originates from the Chunyu Doctor online platform, focusing on cardiology-related cases. Data was annotated with four categories (symptoms, tests, surgeries, and other lifestyle information) with five statuses (patient-positive, patientnegative, doctor-positive, doctor-negative, unknown). The labeling was conducted by three trained annotators with the supervision of physicians. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Initial Assessment
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** Cardiology
- **Application Method:** Link of MIE Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 21.1 Task: Medical entity type extraction

This task is to extract types of medical entities.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical consultation in Chinese, extract the following types of medical entities: 1. "symptom": This type of entity refers to the symptoms mentioned by the patient and the doctor. - The optional list of "entity" for "symptom" is ["行动不便", "战栗抽搐", "心慌", "背痛", "头晕", "呃逆", "腹部不适", "高血压", "高血糖", "呼吸困难", "胸闷", "高血脂", "恶心", "呕吐", "胸痛", "乏力", "出 汗", "发热", "休克", "晕厥", "感冒","咳嗽", "流涕", "头痛", "胃部不适", "僵硬", "发绀", "糖尿病", "贫 血", "水肿", "心绞痛", "甲亢", "早搏", "心律不齐", "房间隔缺损", "房颤", "心衰", "心肌梗死", "先天 性心脏病", "心肌缺血", "室间隔缺损", "心肌炎", "冠心病", "心肌病", "心脏肥大"]. - The optional list of "status" for "symptom" is ["病人-阳性", "病人-阴性", "医生-阳性", "医生-阴性", "未 知"], which means the symptom appeared in the patient, the symptom was not presented in the patient, the symptom was diagnosed by the doctor, the symptom was excluded by the doctor, and the status is unknown, respectively. 2. "surgery": This type of entity refers to the surgery operations mentioned by the patient and the doctor. - The optional list of "entity" for "surgery" is ["介入", "射频消融", "搭桥", "支架"]. - The optional list of "status" for "surgery" is ["病人-阳性", "病人-阴性", "医生-阳性", "医生-阴性", "未 知"], which means the surgery was done on the patient, the surgery was not done on the patient, the surgery was recommended by the doctor, the surgery was deprecated by the doctor, and the status is unknown, respectively. 3. "examination": This type of entity refers to the medical tests mentioned by the patient and the doctor. - The optional list of "entity" for "examination" is ["心电图", "彩超", "心肌酶", "体检", "造影", "超声", "ct", "血常规", "甲状腺功能", "胸片", "b超", "肾功能", "平板", "cta", "测血压", "核磁共振"]. - The optional list of "status" for "examination" is ["病人-阳性", "病人-阴性", "医生-阳性", "医生-阴性", "未知"], which means the examination was done on the patient, the examination was not done on the patient, the examination was recommended by the doctor, the examination was deprecated by the doctor, and the status is unknown, respectively. 4. "general information": This type of entity refers to some general information that is relevant to the patient: - The optional list of "entity" for "general information" is ["睡眠", "饮食", "精神状态", "大小便", "吸烟", "饮酒"]. - The optional list of "status" for "general information" is ["病人-阳性", "病人-阴性", "未知"], which means the status of this entity was normal, the status of this entity was abnormal, and the status is unknown, respectively. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:..., status:...;... entity:..., type:..., status:...;
### Input
[Medical consultation in Chinese]
### Output
entity:..., type:..., status:...;... entity:..., type:..., status:...;
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 22. EHRQA

EHRQA is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. EHRQA 42 is a Chinese medical QA dataset comprising over 210,175 electronic health records (EHR) from a hospital in Zhejiang Province and 3.02 million question-answer pairs from 39 Health Networks. The EHR data contains patient disease histories in free text labeled with concepts such as diseases, symptoms, etc. The QA data includes questions from users and answers from doctors organized by medical departments. Annotations were conducted via a bootstrapping method and human review. The EHRQA-QA task was constructed following the original dataset specifications, while the EHRQA-Primary department and EHRQA-Sub department tasks were newly designed and derived from this dataset as part of our BRIDGE benchmark. In BRIDGE, this source dataset contributes 3 task(s) and is normalized as a reused source dataset / sub-benchmark with 3 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Triage and Referral
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** General
- **Application Method:** Link of EHRQA Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 3 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 22.1 Task: EHRQA-Primary department

This task is to determine the hospital department the patient should visit based on the patient’s medical consultation record.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. We used the patient’s basic information and chief complaint as the model input and assigned the primary department of the hospital as the triage label.

```md
### Instruction
Given the medical consultation record in Chinese, determine the hospital department the patient should visit. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: department: label The optional list for "label" is ["儿科", "妇产科", "传染病科", "皮肤性病科", "外科", "内科", "五官科"].
### Input
[Medical consultation record in Chinese]
### Output
department: [儿科 / 妇产科 / 传染病科 / 皮肤性病科 / 外科 / 内科 / 五官科]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 22.2 Task: EHRQA-Sub department

This task is to determine the detailed hospital department the patient should visit based on the patient’s medical consultation record.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. The patient’s information and chief complaint were used as input, and the detailed sub-department of the subsequent assigned physician was designated as the triage label.

```md
### Instruction
Given the medical consultation record in Chinese, determine the detailed hospital department the patient should visit. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: department: label The optional list for "label" is ["泌尿外科", "性病科", "胃肠外科", "肝胆外科", "骨科", "小儿内科", "妇 科", "小儿精神科", "普外科", "其他传染病", "皮肤病", "消化内科", "风湿免疫科", "口腔科", "产科", "肝病科", "肛肠外科", "肾内科", "眼科", "血管外科", "小儿外科", "乳腺外科", "心胸外科", "烧伤科", "血液科", "内分泌科", "新生儿科", "神经外科", "呼吸内科"].
### Input
[Medical consultation record in Chinese]
### Output
department: [泌尿外科 / 性病科 / 胃肠外科 / 肝胆外科 / 骨科 / 小儿内科 / 妇科 / 小儿精神科 / 普外科 / 其他传染病 / 皮肤病 / 消化内科 / 风湿免疫科 / 口腔科 / 产科 / 肝病科 / 肛肠外科 / 肾内科 / 眼科 / 血管外科 / 小儿外科 / 乳腺外科 / 心胸外科 / 烧伤科 / 血液科 / 内分泌科 / 新生儿科 / 神经外科 / 呼吸内科].
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 22.3 Task: EHRQA-QA

This task is to provide the answer from the doctor’s perspective in Chinese for a patient’s information and consultation record.

### Task type
Question Answering

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. Based on each patient’s EHR, we extracted relevant medical information, including department information, patient demographics, problem summary, and specific query, and used the physician’s actual answer as the expected output.

```md
### Instruction
Given the patient’s information and consultation record in Chinese, provide the answer from the doctor’s perspective in Chinese. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: 医生:...
### Input
[patient’s information and consultation record in Chinese]
### Output
[doctor’s response]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 23. Ex4CDS

Ex4CDS is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. Ex4CDS 43 is a German-language dataset focusing on kidney disease. It was designed to generate explainable clinical decision support. The dataset includes 720 annotated textual justifications written by four junior and four senior physicians, involving 120 kidney transplant patients in three medical endpoints (rejection, infection, and graft loss). Annotations of this dataset cover multiple semantic layers including medical entities, relations, temporal markers, etc. They were labeled by automatic annotation tools and finalized by physician review. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** German
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Nephrology
- **Application Method:** Link of Ex4CDS Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 23.1 Task: Ex4CDS

This task is to extract the medical entities with their corresponding types, factuality, and progression from the physician’s explanations.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. We selected clinically relevant entities from patients’ clinical notes and linked each entity with its corresponding factuality and progression attributes. The task is formulated as an event extraction task, requiring the model to identify entities and simultaneously determine their associated status information within the same inference process.

```md
### Instruction
Given the following physician’s explanation, extract the medical entities with their corresponding types, factuality, and progression. Specifically, this explanation was generated by a physician to predict negative outcomes in kidney disease patients within the next 90 days, including rejection, death-censored graft loss, and infection. We need to extract all the following information for each entity: 1. Entity types: - "Condition": A pathological medical condition of a patient, can describe for instance a symptom or a disease. - "DiagLab": Particular diagnostic procedures which have been carried out. - "LabValues": Mentions of lab values. - "HealthState": A positive condition of the patient. - "Measure": Mostly numeric values, often in the context of medications or lab values, but can also be a description if a value changes, e.g., raises. - "Medication": A medication. - "Process": Describes a particular process, such as blood pressure or heart rate, often related to vital parameters. - "TimeInfo": Describes temporal information, such as 2 weeks ago or January. - "Other": Additional relevant information which influences the health condition and the risk. 2. Factuality: - "positive": indicates that something is present. - "negative": indicates that something is not present. - "speculated": indicates that something is not present, but might occur in the future. - "unlikely": defines a kind of speculation, but expresses a tendency towards negation. - "minor": expresses that something is present, but to a lower extent or in a lower amount. - "possible_future": expresses that something is not there, but might occur in the future. - "None": if no factuality is given. 3. Progression: - "increase_risk_factor": A state/process that causes the respective endpoint (upstream in a causal chain). Increases the risk that endpoint occurs causally and probabilistically. - "decrease_risk_factor": A state/process that prevents the respective endpoint (upstream in a causal chain). Decreases the risk that endpoint occurs causally and probabilistically. - "increase_symptom": A state/process whose absence is a consequence of the respective endpoint (downstream in a causal chain). Increases risk probabilistically, but not causally. - "decrease_symptom": A state/process whose occurrence is a consequence of the respective endpoint (downstream in a causal chain). Decreases risk probabilistically, but not causally. - "Conclusion": The physician makes a concluding statement. - "None": if no progression is given. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:..., factuality:..., progression:...;... entity:..., type:..., factuality:..., progression:...; The optional list for "type" is ["Condition", "DiagLab", "LabValues", "HealthState", "Measure", "Medication", "Process", "TimeInfo", "Other"]. The optional list for "factuality" is ["positive", "negative", "speculated", "unlikely", "minor", "possible_future", "None"]. The optional list for "progression" is ["increase_risk_factor", "decrease_risk_factor", "increase_symptom", "decrease_symptom", "Conclusion", "None"].
### Input
[Discharge summary of a patient]
### Output
entity:..., type: [Condition / DiagLab / LabValues / HealthState / Measure / Medication / Process / TimeInfo / Other], factuality: [positive / negative / speculated / unlikely / minor / possible_future / None], progression: [increase_risk_factor / decrease_risk_factor / increase_symptom / decrease_symptom / Conclusion / None];... entity:..., type: [Condition / DiagLab / LabValues / HealthState / Measure / Medication / Process / TimeInfo / Other], factuality: [positive / negative / speculated / unlikely / minor / possible_future / None], progression: [increase_risk_factor / decrease_risk_factor / increase_symptom / decrease_symptom / Conclusion / None];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 24. GOUT-CC

GOUT-CC is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. Gout-CC dataset 44 is an English dataset focused on GOUT detection. It consists of two splits: GOUT-CC-2019CORPUS which includes 300 chief complaints collected in 2019 and GOUT-CC-2020-CORPUS which includes 8037 chief complaints collected in one month period of 2020. The dataset originates from records of an academic medical center in the southern United States. Each complaint includes two kinds of annotations: A predicted gout flare annotation labeled by a practicing rheumatologist (MD) and a PhD informatician (JDO) and a reviewed consensus labeled by a rheumatologist (MD) and a post-doctoral fellow (GR). Cohen’s Kappa coefficient was applied to calculate the consistency of the annotations. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Diagnosis and Prognosis
- **Source Clinical Document Type:** Admission Note
- **Clinical Specialty:** Endocrinology
- **Application Method:** Link of GOUT-CC Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** It consists of two splits: GOUT-CC-2019CORPUS which includes 300 chief complaints collected in 2019 and GOUT-CC-2020-CORPUS which includes 8037 chief complaints collected in one month period of 2020.

### 24.1 Task: GOUT-CC-Consensus

This task is to determine whether a patient was experiencing a gout flare at the time of the Emergency Department visit.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. We used the annotations from the “consensus” column as the ground-truth labels. Because instances labeled as “unknown” typically corresponded to notes lacking meaningful clinical information (e.g., note titles or administrative text) and "Unknown" may lead to label misinterpretation, we simplified the task into a binary classification problem, requiring the model to determine whether a gout flare was present (yes or no).

```md
### Instruction
Given the patient’s chief complaint, determine whether the patient was experiencing a gout flare at the time of the Emergency Department visit. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Gout flare: label The optional list for "label" is ["Yes", "No"]
### Input
Chief complaint of a patient]
### Output
Gout flare: [Yes / No]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 25. n2c2 2006

n2c2 2006 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The n2c2 2006 45 dataset is an English dataset designed for Protected Health Information (PHI) de-identification. It includes discharge summaries from Partners HealthCare, compiled to support the de-identification of PHI. The dataset contains clinical narratives centered on patient discharge, covering a broad spectrum of medical treatments and prescriptions. Annotations were performed using a custom annotation schema by domain experts, adhering to guidelines developed for the 2006 i2b2 NLP challenge. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Discharge Summary
- **Clinical Specialty:** Pulmonology
- **Application Method:** Link of n2c2 2006 Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 25.1 Task: n2c2 2006-De-identification

This task is to identify the PHI context and their associated type within the clinical document.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical document of a patient, identify the Personal Health Information (PHI) context and their associated type within the document. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: PHI context:..., type:...;... PHI context:..., type:...; The optional list for "type" is ["PATIENT", "ID", "LOCATION", "AGE", "DOCTOR", "PHONE", "HOSPITAL", "DATE"].
### Input
[Clinical text of a patient]
### Output
PHI context: [PHI context], type: [PATIENT / ID / LOCATION / AGE / DOCTOR / PHONE / HOSPITAL / DATE];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 26. i2b2 2009

i2b2 2009 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The i2b2 2009 dataset 46 is an English dataset designed for medication information extraction. It includes 1,249 patient discharge summaries, compiled from Partners Healthcare. The dataset contains clinical narratives and was developed as part of the i2b2 medication extraction challenge. Annotations were performed by a team consisting of a physician and a researcher, adhering to a sequential annotation strategy. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Discharge Summary
- **Clinical Specialty:** Pharmacology
- **Application Method:** Link of i2b2 2009 Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 26.1 Task: Medication extraction

This task is to extract the medications from the discharge summary. Then, for each extracted medication, further extract the following entities: "dosage", "mode", "frequency", "duration", "reason", "list/narrative".

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the discharge summary of a patient, extract the medications from the discharge summary. Then, for each extracted medication, further extract the following entities: - "dosage": Indicating the amount of a medication used in each administration. - "mode": Indicating the route for administering the medication. - "frequency": Indicating how often each dose of the medication should be taken. - "duration": Indicating how long the medication is to be administered. - "reason": Stating the medical reason for which the medication is given. - "list/narrative": Indicating whether the medication information appears in a list structure or in narrative running text in the discharge summary. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: medication:..., dosage:..., mode:..., frequency:..., duration:..., reason:..., list/narrative:...;... medication:..., dosage:..., mode:..., frequency:..., duration:..., reason:..., list/narrative:...; The optional list for "list/narrative" is ["list", "narrative"]. For each extracted medication, if any of the above entity ("dosage", "mode", "frequency", "duration", "reason", "list/narrative") is not mentioned in the discharge summary, then please label this entity as "not mentioned".
### Input
[Discharge summary of a patient]
### Output
medication: [name of the medication], dosage: [medication dosage], mode: [medication route], frequency: [dose frequency], duration: [medication administration time length], reason: [reason for giving the medication], list/narrative: [list / narrative];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 27. i2b2 2010

i2b2 2010 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The i2b2 2010 dataset 47 is an English dataset designed for named entity recognition. It was compiled from Partners Healthcare, Beth Israel Deaconess Medical Center, and the University of Pittsburgh Medical Center. The dataset contains discharge summaries and progress reports, covering a wide range of clinical concepts such as medical problems, treatments, and tests. Annotations were performed using a manually annotated reference standard corpus by the i2b2 team in collaboration with the VA Salt Lake City Health Care System, adhering to task-specific guidelines for concepts, assertions, and fine-grained relations. In BRIDGE, this source dataset contributes 3 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Treatment and Intervention (Task "n2c2 2010-Assertion" has clinical stage "Discharge and
- **Source Clinical Document Type:** Discharge Summary, Progress Note
- **Clinical Specialty:** Critical Care
- **Application Method:** Link of i2b2 2010 Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 27.1 Task: n2c2 2010-Concept

This task is to identify and extract the text corresponding to patient medical problems, treatments, and tests.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the discharge summary of a patient, extract the following types of entities from the discharge summary: - "problem": Phrases that contain observations made by patients or clinicians about the patient’s body or mind that are thought to be abnormal or caused by a disease. - "treatment": Phrases that describe procedures, interventions, and substances given to a patient in an effort to resolve a medical problem. - "test": Phrases that describe procedures, panels, and measures that are done to a patient or a body fluid or sample in order to discover, rule out, or find more information about a medical problem. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["problem", "treatment", "test"].
### Input
[Discharge summary of a patient]
### Output
entity: [clinical entity], type: [problem / treatment / test];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 27.2 Task: n2c2 2010-Assertion

This task is to extract the medical problems and classify the corresponding assertions made on given medical concepts as being present, absent, or possible in the patient, conditionally present in the patient under certain circumstances, hypothetically present in the patient at some future point, and mentioned in the patient report but associated with someone other than the patient.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the discharge summary of a patient, extract the medical problems from the discharge summary, and for each medical problem, classify it into one of the following categories: - "present": Problems associated with the patient can be present. - "absent: The discharge summary asserts that the problem does not exist in the patient. - "possible": The discharge summary asserts that the patient may have a problem, but there is uncertainty expressed in the discharge summary. - "conditional": The mention of the medical problem asserts that the patient experiences the problem only under certain conditions. - "hypothetical": Medical problems that the note asserts the patient may develop. - "not associated with patient": The mention of the medical problem is associated with someone who is not the patient. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: problem:..., type:...;... problem:..., type:...; The optional list for "type" is ["present", "absent", "possible", "conditional", "hypothetical", "not associated with patient"].
### Input
[Discharge summary of a patient]
### Output
problem: [medical problem], type: [present / absent / possible / conditional / hypothetical / not associated with patient];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 27.3 Task: n2c2 2010-Relation

This task is to extract relations of pairs of given reference standard concepts from a sentence.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the discharge summary of a patient, extract the following types of entities from the discharge summary: - "problem": Phrases that contain observations made by patients or clinicians about the patient’s body or mind that are thought to be abnormal or caused by a disease. - "treatment": Phrases that describe procedures, interventions, and substances given to a patient in an effort to resolve a medical problem. - "test": Phrases that describe procedures, panels, and measures that are done to a patient or a body fluid or sample in order to discover, rule out, or find more information about a medical problem. Then, extract the following three types of relations if applicable: 1. relations between "treatment" and "problem": - "TrIP": This includes mentions where the treatment improves or cures the problem. - "TrWP": This includes mentions where the treatment is administered for the problem but does not cure the problem, does not improve the problem, or makes the problem worse. - "TrCP": The implied context is that the treatment was not administered for the medical problem that it ended up causing. - "TrAP": This includes mentions where a treatment is given for a problem, but the outcome is not mentioned in the sentence. - "TrNAP": This includes mentions where treatment was not given or discontinued because of a medical problem that the treatment did not cause. 2. relations between "test" and "problem": - "TeRP": This includes mentions where a test is conducted and the outcome is known. - "TeCP": This includes mentions where a test is conducted and the outcome is not known. 3. relations between "problem" and "problem": - "PIP": This includes medical problems that describe or reveal aspects of the same medical problem and those that cause other medical problems. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity_1:..., entity_2:..., relation:...;... entity_1:..., entity_2:..., relation:...; The optional list for "relation" is ["TrIP", "TrWP", "TrCP", "TrAP", "TrNAP", "TeRP", "TeCP", "PIP"].
### Input
[Discharge summary of a patient]
### Output
entity_1: [a problem/treatment/test entity], entity_2: [a problem/treatment/test entity], relation: [TrIP / TrWP / TrCP / TrAP / TrNAP / TeRP / TeCP / PIP];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 28. n2c2 2014 - De-identification

n2c2 2014 - De-identification is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The n2c2 2014 - De-identification dataset 48 is an English dataset designed for de-identification of clinical narratives. It includes 1,304 medical records from 296 diabetic patients, compiled from the Research Patient Data Repository of Partners Healthcare. The dataset contains longitudinal clinical notes, reflecting the progression of heart disease in diabetic patients over time. Annotations were performed using a comprehensive set of i2b2-PHI categories, extending beyond HIPAA definitions, and were conducted with both automatic and manual checks to ensure accuracy. Authentic Protected Health Information (PHI) was replaced with realistic surrogates, and the annotated corpus was used as a gold standard for system evaluations in the 2014 i2b2/UTHealth NLP shared task. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Endocrinology
- **Application Method:** Link of n2c2 2014 - De-identification Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 28.1 Task: n2c2 2014-De-identification

This task is to identify all the following type of PHI information within the document: ’STATE’, ’LOCATIONOTHER’, ’STREET’, ’PHONE’, ’FAX’, ’ZIP’, ’DOCTOR’, ’DATE’, ’EMAIL’, ’DEVICE’, ’COUNTRY’, ’HOSPITAL’, ’HEALTHPLAN’, ’ORGANIZATION’, ’USERNAME’, ’BIOID’, ’CITY’, ’PROFESSION’, ’PATIENT’, ’URL’, ’AGE’, ’IDNUM’, ’MEDICALRECORD’.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical document of a patient, identify the Personal Health Information (PHI) context and their associated type within the document. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: PHI context:..., type:...;... PHI context:..., type:...; The optional list of PHI types is ["STATE", "LOCATION-OTHER", "STREET", "PHONE", "FAX", "ZIP", "DOCTOR", "DATE", "EMAIL", "DEVICE", "COUNTRY", "HOSPITAL", "HEALTHPLAN", "ORGANIZATION", "USERNAME", "BIOID", "CITY", "PROFESSION", "PATIENT", "URL", "AGE", "IDNUM", "MEDICALRECORD"].
### Input
[Clinical document of a patient]
### Output
PHI context: [PHI context], type: [STATE / LOCATION-OTHER / STREET / PHONE / FAX / ZIP / DOCTOR / DATE / EMAIL / DEVICE / COUNTRY / HOSPITAL / HEALTHPLAN / ORGANIZATION / USERNAME / BIOID / CITY / PROFESSION / PATIENT / URL / AGE / IDNUM / MEDICALRECORD];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 29. IMCS-V2

IMCS-V2 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The IMCS-V2 (Intelligent Medical Consultation System - Version 2) dataset 49 comprises real-world doctor–patient dialogues collected from an online medical consultation platform. This dataset covers 10 common pediatric diseases, including pediatric bronchitis, fever, and diarrhea. Each dialogue includes interactions between patients (or their guardians) and physicians. Through systematic annotation, the dataset labels various medical information, such as medical entities and dialogue acts. It supports four tasks: named entity recognition (NER), dialogue act classification (DAC), symptom recognition (SR), and medical report generation (MRG). IMCS-V2 is included in the CBLUE benchmark 30. We adapted the CBLUE version for downstream task construction. In BRIDGE, this source dataset contributes 4 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Triage and Referral (IMCS-V2-DAC), Inital Assessment (IMCS-V2-NER, SR, MRG)
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** Pediatrics
- **Application Method:** Link of IMCS-V2-NER Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 29.1 Task: IMCS-V2-NER

This task is to identify five categories of medical entities from doctor–patient dialogue texts.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the text from medical consultation in Chinese, extract the medical entities mentioned by the patient and doctors, including the following types: - "symptom"(症状)：病人因患病而表现出来的异 常状况，如"发热"、"呼吸困难"、"鼻塞"等。 - "drug"(药品名)：具体的药物名称，如"妈咪爱"、"蒙脱石散"、"蒲地蓝"等。 - "drug category"(药物类别)：根据药物功能进行划分的药物种类，如"消炎药"、"感冒药"、"益生 菌"等。 - "examination"(检查)：医学检验，如"血常规"、"x光片"、"CRP分析"等。 - “operation”(操作)：相关的医疗操作，如"输液"、"雾化"、"接种疫苗"等。 Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["symptom", "drug", "drug category", "examination", "operation"].
### Input
[Medical dialogue between doctor and patient]
### Output
entity: [entity span], type: [symptom / drug / drug category / examination / operation];... entity: [entity span], type: [symptom / drug / drug category / examination / operation];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 29.2 Task: IMCS-V2-SR

This task is to recognize patient symptom information, including both normalized labels and status, from the conversation.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical consultation in Chinese, recognize the normalized symptoms mentioned by the patient and doctors and identify the global status of symptoms based on the dialogue, including: - "positive": 代表确定病人患有该症状 - "negative": 代表确定病人没有患有该症状 - "uncertain": 代表无法根据上下文确定病人是否患有该症状 Specifically, the status of the symptom is based on the entire dialogue, not just the current sentence. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: symptom:..., status:...;... symptom:..., status:...; The optional list for "status" is ["positive", "negative", "uncertain"].
### Input
[Medical dialogue between doctor and patient]
### Output
symptom: [entity span], status: [ positive / negative / uncertain];... symptom: [entity span], status: [ positive / negative / uncertain];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 29.3 Task: IMCS-V2-MRG

This task is to generate a structured summarization based on the patient’s chief complaint and the full doctor–patient dialogue.

### Task type
Summarization

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical consultation in Chinese, generate the brief report based on the dialogue between the patient and doctor. The report should include the following sections: 1. 主诉(Chief complaint): 病人自诉（Self-report）的总结，包括主要症状或体征； 2. 现病史(Present illness history): 对话中病人涉及到的现病史的总结，如主要症状的描述（发病情 况，发病时间）； 3. 辅助检查(Auxiliary examination): 对话中病人涉及过的医疗检查的总结，如病人已有的检查项 目、检查结果、会诊记录等； 4. 既往史(Past history): 对话中医生对病人的过去病史的总结，如既往的健康状况、过去曾经患过 的疾病等； 5. 诊断(Diagnosis): 对话中医生对病人的诊断结果的总结，如对疾病的诊断； 6. 建议(Suggestion): 对话中医生对病人的建议的总结，如检查建议、药物治疗、注意事项。 Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: 主诉:... 现病史:... 辅助检查:... 既往史:... 诊断:... 建议:...
### Input
[A whole medical dialogue between doctor and patient]
### Output
主诉: [summarized chief complaint] 现病史: [summarized illness history] 辅助检查: [summarized auxiliary examination ] 既往史: [summarized past history] 诊断: [summarized diagnosis] 建议: [summarized suggestion from physician]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 29.4 Task: IMCS-V2-DAC

This task is to classify the intent of each utterance in the dialogue into one of 16 predefined categories.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
[ Given the utterance from a medical consultation in Chinese, identify the act the speaker is performing. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: dialogue act: label The optional list for "label" is ["提问-症状", "提问-病因", "提问-基本信息", "提问-已有检查和治疗", "告知-用药建议", "告知-就医建议", "告知-注意事项", "诊断", "告知-症状", "告知-病因", "告知-基本 信息", "告知-已有检查和治疗", "提问-用药建议", "提问-就医建议", "提问-注意事项"].
### Input
[A utterance from medical dialogue]
### Output
dialogue act: [提问-症状/ 提问-病因/ 提问-基本信息/ 提问-已有检查和治疗/ 告知-用药建议/ 告知-就医建议/ 告知-注意事项/ 诊断/ 告知-症状/ 告知-病因/ 告知-基本信息/ 告知-已有检查和治疗/ 提问-用药建议/ 提问-就医建议/ 提问-注意事项]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 30. Japanese Case Reports

Japanese Case Reports is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The Japanese Case Reports dataset is a Japanese dataset 50 designed for semantic textual similarity tasks. It includes approximately 4,000 annotated sentence pairs, compiled from case reports extracted from the CiNii database. The dataset contains clinical case report texts, covering a wide range of medical scenarios. Annotations were performed by staff with medical backgrounds, using a 6-point scale (0 to 5) to rate semantic similarity, and following guidelines from previous STS tasks. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Japanese
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of Japanese Case Reports Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 30.1 Task: JP-STS

This task is to capture semantic textual similarity (STS) between Japanese clinical texts.

### Task type
Semantic Similarity

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following two clinical sentences that are labeled as "Sentence A" and "Sentence B" in Japanese, decide the similarity of the two sentences according to the following rubric: - "0": The two sentences are completely dissimilar. - "1": The two sentences are not equivalent, but are on the same topic. - "2": The two sentences are not equivalent, but share some details. - "3": The two sentences are roughly equivalent, but some important information differs/missing. - "4": The two sentences are mostly equivalent, but some unimportant details differ. - "5": The two sentences are completely equivalent. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: similarity score: score The optional list for "score" is ["0", "1", "2", "3", "4", "5"].
### Input
Sentence A: [Clinical sentence A] Sentence B: [Clinical sentence B]
### Output
similarity score: [0 / 1 / 2 / 3 / 4 / 5]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 31. meddocan

meddocan is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The meddocan dataset 51 is a Spanish dataset designed for de-identification of sensitive information in clinical texts. It includes 1,000 manually selected and synthetically enriched clinical case studies, compiled under the Spanish National Plan for the Advancement of Language Technology (Plan TL) by the Barcelona Supercomputing Center and the Centro Nacional de Investigaciones Oncológicas. The dataset contains clinical case reports enriched with Protected Health Information (PHI), covering a broad range of sensitive data types including names, dates, locations, and identifiers. Annotations were performed using a customized version of AnnotateIt and corrected using the BRAT annotation tool by a hybrid team of healthcare and NLP experts, adhering to guidelines based on the EU GDPR and the US HIPAA standards. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of meddocan Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 31.1 Task: meddocan

This task is to extract specific clinical entities from the clinical text.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Spanish, extract the following types of entities from the clinical text: "TERRITORIO", "FECHAS", "EDAD SUJETO ASISTENCIA", "NOMBRE SUJETO ASISTENCIA", "NOMBRE PERSONAL SANITARIO", "SEXO SUJETO ASISTENCIA", "CALLE", "PAIS", "ID SUJETO ASISTENCIA", "CORREO ELECTRONICO", "ID TITULACION PERSONAL SANITARIO", "ID ASEGURAMIENTO", "HOSPITAL", "FAMILIARES SUJETO ASISTENCIA", "INSTITUCION", "ID CONTACTO ASISTENCIAL", "NUMERO TELEFONO", "PROFESION", "NUMERO FAX", "OTROS SUJETO ASISTENCIA", "CENTRO SALUD", "ID EMPLEO PERSONAL SANITARIO", "IDENTIF VEHICULOS NRSERIE PLACAS", "IDENTIF DISPOSITIVOS NRSERIE", "NUMERO BENEF PLAN SALUD", "URL WEB", "DIREC PROT INTERNET", "IDENTF BIOMETRICOS", "OTRO NUMERO IDENTIF". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["TERRITORIO", "FECHAS", "EDAD SUJETO ASISTENCIA", "NOMBRE SUJETO ASISTENCIA", "NOMBRE PERSONAL SANITARIO", "SEXO SUJETO ASISTENCIA", "CALLE", "PAIS", "ID SUJETO ASISTENCIA", "CORREO ELECTRONICO", "ID TITULACION PERSONAL SANITARIO", "ID ASEGURAMIENTO", "HOSPITAL", "FAMILIARES SUJETO ASISTENCIA", "INSTITUCION", "ID CONTACTO ASISTENCIAL", "NUMERO TELEFONO", "PROFESION", "NUMERO FAX", "OTROS SUJETO ASISTENCIA", "CENTRO SALUD", "ID EMPLEO PERSONAL SANITARIO", "IDENTIF VEHICULOS NRSERIE PLACAS", "IDENTIF DISPOSITIVOS NRSERIE", "NUMERO BENEF PLAN SALUD", "URL WEB", "DIREC PROT INTERNET", "IDENTF BIOMETRICOS", "OTRO NUMERO IDENTIF"].
### Input
[Discharge summary of a patient]
### Output
entity: [clinical entity], type: [TERRITORIO / FECHAS / EDAD SUJETO ASISTENCIA / NOMBRE SUJETO ASISTENCIA / NOMBRE PERSONAL SANITARIO / SEXO SUJETO ASISTENCIA / CALLE / PAIS / ID SUJETO ASISTENCIA / CORREO ELECTRONICO / ID TITULACION PERSONAL SANITARIO / ID ASEGURAMIENTO / HOSPITAL / FAMILIARES SUJETO ASISTENCIA / INSTITUCION / ID CONTACTO ASISTENCIAL / NUMERO TELEFONO / PROFESION / NUMERO FAX / OTROS SUJETO ASISTENCIA / CENTRO SALUD / ID EMPLEO PERSONAL SANITARIO / IDENTIF VEHICULOS NRSERIE PLACAS / IDENTIF DISPOSITIVOS NRSERIE / NUMERO BENEF PLAN SALUD / URL WEB / DIREC PROT INTERNET / IDENTF BIOMETRICOS / OTRO NUMERO IDENTIF];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 32. MEDIQA_2019_Task2_RQE

MEDIQA_2019_Task2_RQE is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MEDIQA_2019_Task2_RQE dataset 52 is an English dataset designed for recognizing question entailment in the medical domain. It includes 230 test pairs of consumer health questions and frequently asked questions (FAQs), as well as 8,890 training and 302 validation medical question pairs. The dataset was compiled by the U.S. National Library of Medicine (NLM) using a collection of clinical and consumer health questions. The dataset contains medical question pairs and covers a variety of health-related topics. Annotations were manually validated by medical experts, adhering to the definition that a question A entails question B if every answer to B is also a complete or partial answer to A. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Triage and Referral
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** General
- **Application Method:** Link of MEDIQA_2019_Task2_RQE Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** It includes 230 test pairs of consumer health questions and frequently asked questions (FAQs), as well as 8,890 training and 302 validation medical question pairs.

### 32.1 Task: MEDIQA 2019-RQE

This task is to identify entailment between two questions in the context of QA.

### Task type
Natural Language Inference

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following two clinical questions labeled as "Question A" and "Question B", determine if the answer to "Question B" is also the answer to "Question A", either exactly or partially. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: answer: label The optional list for "label" is ["true", "false"].
### Input
Question A: [Question A context] Question B: [Question B context]
### Output
answer: [true / false]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 33. MedNLI

MedNLI is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MedNLI dataset 53 is an English dataset designed for natural language inference (NLI) in the clinical domain. It includes 14,049 unique sentence pairs, compiled from the MIMIC-III v1.3 database of de-identified clinical records. The dataset contains premise-hypothesis pairs derived from clinical notes, particularly the Past Medical History section, covering a wide range of medical conditions and concepts such as diseases, symptoms, and medications. Annotations were performed by board-certified clinicians, adhering to custom-developed guidelines to ensure consistency and quality. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Critical Care
- **Application Method:** Link of MedNLI Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 33.1 Task: MedNLI

This task is to classify the inference relation between the premise-hypothesis statements pair into one of the three classes: "entailment", "contradiction", or "neutral".

### Task type
Natural Language Inference

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the premise-hypothesis statements pair labeled as "Premise statement" and "Hypothesis statement", classify the inference relation between two statements into one of the three classes: "entailment", "contradiction", or "neutral". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: relation: label The optional list for "label" is ["entailment", "contradiction", "neutral"].
### Input
Premise statement: [Premise statement context] Hypothesis statement: [Hypothesis statement context]
### Output
relation: [entailment / contradiction / neutral]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 34. MedSTS

MedSTS is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MedSTS dataset 54 is an English dataset designed for semantic textual similarity tasks. It includes 174,629 sentence pairs compiled from de-identified clinical notes at the Mayo Clinic. The dataset contains clinical sentences reflecting a wide range of medical concepts, including signs and symptoms, disorders, procedures, and medications. A subset of 1,250 sentence pairs, called MedSTS_ann, was annotated with semantic similarity scores ranging from 0 to 5 by two experienced clinical experts. Annotations were performed using manual scoring guidelines adapted from SemEval shared tasks. The dataset was developed to support NLP research aimed at reducing redundancy in electronic health records and improving clinical decision-making. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Email the corresponding author for access
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 34.1 Task: MedSTS

This task is to determine the similarity of the two sentences in a score from 0 to 5, with 0 indicating that the medical semantics of the sentences are completely independent and 5 signifying semantic equivalence.

### Task type
Semantic Similarity

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given two clinical sentences labeled as "Sentence A" and "Sentence B", determine the similarity of the two sentences in a score from 0 to 5, with 0 indicating that the medical semantics of the sentences are completely independent and 5 indicating significant semantic equivalence. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: similarity score: score The optional list for "score" is ["0", "1", "2", "3", "4", "5"].
### Input
Sentence A: [Clinical sentence A] Sentence B: [Clinical sentence B]
### Output
similarity score: [0 / 1 / 2 / 3 / 4 / 5]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 35. mtsamples

mtsamples is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The mtsamples dataset 55 is an English dataset designed for clinical outcome prediction and self-supervised language model pre-training. It includes a large collection of publicly available medical transcriptions of medical dictations, covering a wide range of medical specialties and conditions. Annotations were used as part of the self-supervised pre-training process to integrate practical medical knowledge into clinical outcome models. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of mtsamples Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The mtsamples dataset 55 is an English dataset designed for clinical outcome prediction and self-supervised language model pre-training. Annotations were used as part of the self-supervised pre-training process to integrate practical medical knowledge into clinical outcome models.

### 35.1 Task: MTS

This task is to classify the clinical text into specific categories.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the transcribed clinical text, classify the clinical text into its corresponding clinical specialty or document type (can be more than one). Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: answer: label_1, label_2,..., label_n The optional list for "label" is [’Allergy / Immunology’, ’Autopsy’, ’Bariatrics’, ’Cardiovascular / Pulmonary’, ’Chiropractic’, ’Consult - History and Phy.’, ’Cosmetic / Plastic Surgery’, ’Dentistry’, ’Dermatology’, ’Diets and Nutritions’, ’Discharge Summary’, ’ENT - Otolaryngology’, ’Emergency Room Reports’, ’Endocrinology’, ’Gastroenterology’, ’General Medicine’, ’Hematology - Oncology’, ’Hospice - Palliative Care’, ’IMEQME-Work Comp etc.’, ’Lab Medicine - Pathology’, ’Letters’, ’Nephrology’, ’Neurology’, ’Neurosurgery’, ’Obstetrics / Gynecology’, ’Office Notes’, ’Ophthalmology’, ’Orthopedic’, ’Pain Management’, ’Pediatrics Neonatal’, ’Physical Medicine - Rehab’, ’Podiatry’, ’Psychiatry / Psychology’, ’Radiology’, ’Rheumatology’, ’SOAP / Chart / Progress Notes’, ’Sleep Medicine’, ’Speech - Language’, ’Surgery’, ’Urology’].
### Input
[Clinical text of a patient]
### Output
answer: [one or more of the above labels]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 36. mtsamples-temporal

mtsamples-temporal is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The mtsamples-temporal dataset 56 is an English dataset designed for temporal information extraction and timeline reconstruction. It includes 286 medical transcription documents covering four clinical specialties: discharge summaries, psychiatry-psychology, paediatrics, and emergency, compiled from MTSamples, a public repository of clinical text. The dataset contains annotated time expressions (TIMEXes) such as dates, times, durations, frequencies, and age-related expressions, capturing how temporal information is expressed in clinical narratives. Annotations were performed manually by two annotators, following custom annotation guidelines based on the TimeML schema, with extensions for domain-specific temporal constructs. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Initial Assessment
- **Source Clinical Document Type:** Discharge Summary
- **Clinical Specialty:** Pediatrics, Psychology
- **Application Method:** Link of mtsamples-temporal Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 36.1 Task: MTS-Temporal

This task is to extract the following types of time expression from the clinical text: ’time’, ’frequency’, ’age_related’, ’date’, ’duration’, ’other’.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text, extract the time expressions from the clinical text, and categorize each of them into one of the following categories: "time", "frequency", "age_related", "date", "duration", "other". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: time expression:..., category:...;... time expression:..., category:...; The optional list for "category" is ["time", "frequency", "age_related", "date", "duration", "other"].
### Input
[Clinical text of a patient]
### Output
time expression: [time expression within the clinical text], category: [time / frequency / age_related / date / duration / other];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 37. n2c2 2018 Track2

n2c2 2018 Track2 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The n2c2 2018 Track2 dataset 57 is an English dataset designed for adverse drug event (ADE) and medication information extraction. It includes 505 discharge summaries drawn from the MIMIC-III clinical care database. The dataset contains narrative clinical records annotated for medication-related concepts (e.g., drug name, strength, dosage, frequency, route, duration, reason, and ADE) and their relations. Annotations were performed by two independent annotators with conflict resolution by a third annotator. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Discharge Summary
- **Clinical Specialty:** Pharmacology
- **Application Method:** Link of n2c2 2018 Track2 Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 37.1 Task: n2c2 2018-ADE&medication

This task is to identify the drugs and extract the following attributes from the clinical text: "adverse drug event", "dosage", "duration", "form", "frequency", "reason", "route", "strength".

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the longitudinal medical records of a patient, identify the drugs and extract the following attributes from the clinical text: "adverse drug event", "dosage", "duration", "form", "frequency", "reason", "route", "strength". Please note that a drug may have none or some of these attributes. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: drug:..., attribute:...,..., attribute:...;... drug:..., attribute:...,..., attribute:...; The optional list for "attribute" is ["adverse drug event", "dosage", "duration", "form", "frequency", "reason", "route", "strength"].
### Input
[longitudinal medical records of a patient]
### Output
drug: [name of the drug], adverse drug event / dosage / duration / form / frequency / reason / route / strength: [drug attribute],..., adverse drug event / dosage / duration / form / frequency / reason / route / strength: [drug attribute];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 38. NorSynthClinical

NorSynthClinical is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The NorSynthClinical dataset 58 is a Norwegian dataset designed for family history information extraction. It includes 477 sentences and 6,030 tokens, compiled from synthetically produced clinical statements by a domain expert in genetic cardiology. The dataset contains synthetic descriptions of patients’ family histories, focusing primarily on cardiac conditions. Annotations were performed using the Brat annotation tool by a clinician and independent annotators, adhering to iteratively developed guidelines informed by inter-annotator agreement evaluations and clinical domain knowledge. In BRIDGE, this source dataset contributes 2 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Norwegian
- **Clinical Stage:** Initial Assessment
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Cardiology
- **Application Method:** Link of NorSynthClinical Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 38.1 Task: NorSynthClinical-NER

This task is to extract the following types of entities from the clinical records:"FAMILY", "SELF", INDEX", "CONDITION", "EVENT", "SIDE", "AGE", "NEG", "AMOUNT", "TEMPORAL".

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Norwegian, extract the following types of entities from the clinical records: - "FAMILY": Used to describes various family members. - "SELF": Used to refer to the patient. - "INDEX": Used to designate the property of being the index patient or proband. - "CONDITION": Used to describe a range of clinical conditions such as diseases, diagnoses, various types of mutations, test results, treatments, and vital state. - "EVENT": Used to describe clinical events. - "SIDE": Used to describe the side of the family and thus modify "FAMILY" entities. - "AGE": Used to describe the age of a family member. - "NEG": Used to mark lexical items that signal negation. - "AMOUNT": Used to describe quantifiers that describe numerical properties of clinical entities. - "EMPORAL": Used to modify typically position "CONDITION" or "EVENT" entities in time. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["FAMILY", "SELF", "INDEX", "CONDITION", "EVENT", "SIDE", "AGE", "NEG", "AMOUNT", "EMPORAL"].
### Input
[Clinical text of a patient]
### Output
entity: [clinical entity], type: [FAMILY / SELF / INDEX / CONDITION / EVENT / SIDE / AGE / NEG / AMOUNT / EMPORAL];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 38.2 Task: NorSynthClinical-RE

This task is to extract the following types of relations from the clinical records:"Holder", "Modifier", "Related_to", "Subset", "Partner".

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Norwegian, extract the following types of relations from the clinical records: - "Holder": Relations between a "CONDITION" or "EVENT" entity and its holder, a "FAMILY" or "SELF" or "INDEX" entity. - "Modifier": Relations hold between modifier entities and clinical entities. - "Related_to": Relations specify relations between family members and always hold between "FAMILY" entities. - "Subset": Relations specify relations between family members, where one is a subset of the other. - "Partner": Relations specify relations between entities of the "FAMILY" type, used to identify couples that are able to provide offspring. Below are the definitions of the entity types mentioned above: - "FAMILY": Used to describes various family members. - "SELF": Used to refer to the patient. - "INDEX": Used to designate the property of being the index patient or proband. - "CONDITION": Used to describe a range of clinical conditions such as diseases, diagnoses, various types of mutations, test results, treatments, and vital state. - "EVENT": Used to describe clinical events. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity_1:..., entity_2:..., relation:...;... entity_1:..., entity_2:..., relation:...; The optional list for "relation" is ["Holder", "Modifier", "Related_to", "Subset", "Partner"].
### Input
[Clinical text of a patient]
### Output
entity_1: [clinical entity 1], entity_2: [clinical entity 2], relation: [Holder / Modifier / Related_to / Subset / Partner];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 39. NUBES

NUBES is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The NUBES dataset 59 is a Spanish dataset designed for negation and uncertainty detection in clinical texts. It includes 29,682 sentences and 518,068 tokens, compiled from anonymized health records provided by a Spanish private hospital. The dataset contains excerpts from various clinical sections, such as Chief Complaint, Present Illness, and Diagnostic Tests, covering a wide range of medical contexts. Annotations were performed using the BRAT tool by a team of linguists and a medical expert, following guidelines adapted from the IULA-SCRC corpus. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** Spanish
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Link of NUBES Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 39.1 Task: NUBES

This task is to extract the negation and uncertainty cues and scope.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. We constructed the task by combining the extraction of entity text, determining its marker type, and analyzing its scope into a event extraction task.

```md
### Instruction
Given the clinical text of a patient in Spanish, extract the following types of entities from the clinical text: - "NegSynMarker": Syntactic negation cue. - "NegLexMarker": Lexical negation cue. - "NegMorMarker": Morphological negation cue. - "UncertSynMarker": Syntactic uncertainty cue. - "UncertLexMarker": Lexical uncertainty cue. Then, for each extracted entity, extract the scope that the entity affects. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:..., scope:...;... entity:..., type:..., scope:...; The optional list for "type" is ["NegSynMarker", "NegLexMarker", "NegMorMarker", "UncertSynMarker", "UncertLexMarker"].
### Input
[Clinical text of a patient]
### Output
entity: [clinical entity], type: [NegSynMarker / NegLexMarker / NegMorMarker / UncertSynMarker / UncertLexMarker], scope: [scope of the negation cue];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 40. MTS-Dialog-MEDIQA-2023

MTS-Dialog-MEDIQA-2023 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MTS-Dialog-MEDIQA-2023 dataset 60 is an English dataset designed for automatic summarization of doctorpatient conversations into clinical notes. It includes 1,701 simulated dialogue-note pairs, comprising 15,969 dialogue turns and 5,870 summary sentences, created from de-identified clinical notes sourced from the public MTSamples collection. The dataset contains synthetic medical dialogues reflecting six specialties, generated by trained annotators with medical backgrounds using detailed annotation guidelines. Annotations were validated through a rigorous quality control process involving rubric-based manual review and corrections. In BRIDGE, this source dataset contributes 3 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Initial Assessment
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** General
- **Application Method:** Link of MTS-Dialog-MEDIQA-2023 Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 40.1 Task: MEDIQA 2023-chat-A

This task involves summarizing various clinical sections based on the dialogue between a doctor and a patient. The clinical sections to be summarized include: fam/sochx [FAMILY HISTORY/SOCIAL HISTORY], genhx [HISTORY OF PRESENT ILLNESS], pastmedicalhx [PAST MEDICAL HISTORY], cc [CHIEF COMPLAINT], pastsurgical [PAST SURGICAL HISTORY], allergy, ros [REVIEW OF SYSTEMS], medications, assessment, exam, diagnosis, disposition, plan, edcourse [EMERGENCY DEPARTMENT COURSE], immunizations, imaging, gynhx [GYNECOLOGIC HISTORY], procedures, other_history, and labs.

### Task type
Summarization

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical conversation between a doctor and a patient, summarize the clinical section based on the conversation. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: summary:...
### Input
[Clinical conversation between a doctor and a patient]
### Output
summary: [summary of the specific clinical section]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 40.2 Task: MEDIQA 2023-sum-A

This task is to classify the topic of the conversation between a doctor and a patient into one of the following categories: "family history/social history", "history of patient illness", "past medical history", "chief complaint", "past surgical history", "allergy", "review of systems", "medications", "assessment", "exam", "diagnosis", "disposition", "plan", "emergency department course", "immunizations", "imaging", "gynecologic history", "procedures", "other history", "labs".

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical conversation between a doctor and a patient, determine the topic of the conversation. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: topic: label The optional list for "label" is ["family history/social history", "history of patient illness", "past medical history", "chief complaint", "past surgical history", "allergy", "review of systems", "medications", "assessment", "exam", "diagnosis", "disposition", "plan", "emergency department course", "immunizations", "imaging", "gynecologic history", "procedures", "other history", "labs"].
### Input
[Clinical conversation between a doctor and a patient]
### Output
topic: [family history/social history / history of patient illness / past medical history / chief complaint / past surgical history / allergy / review of systems / medications / assessment / exam / diagnosis / disposition / plan / emergency department course / immunizations / imaging / gynecologic history / procedures / other history / labs]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 40.3 Task: MEDIQA 2023-sum-B

This task has the same description as "MTS-Dialog-MEDIQA-2023-chat-task-A". The only difference between the two tasks is the test set. This task involves summarizing various clinical sections based on the dialogue between a doctor and a patient. The clinical sections to be summarized include: fam/sochx [FAMILY HISTORY/SOCIAL HISTORY], genhx [HISTORY OF PRESENT ILLNESS], pastmedicalhx [PAST MEDICAL HISTORY], cc [CHIEF COMPLAINT], pastsurgical [PAST SURGICAL HISTORY], allergy, ros [REVIEW OF SYSTEMS], medications, assessment, exam, diagnosis, disposition, plan, edcourse [EMERGENCY DEPARTMENT COURSE], immunizations, imaging, gynhx [GYNECOLOGIC HISTORY], procedures, other_history, and labs.

### Task type
Summarization

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical conversation between a doctor and a patient, summarize the clinical section based on the conversation. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: summary:...
### Input
[Clinical conversation between a doctor and a patient]
### Output
summary: [summary of the specific clinical section]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 41. RuMedDaNet

RuMedDaNet is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The RuMedDaNet dataset 61 is a Russian language dataset designed for medical question answering. It includes 1,564 records compiled from diverse medical domains such as therapeutic medicine, physiology, anatomy, pharmacology, and biochemistry. The dataset contains medical-related context passages paired with yes/no questions, aiming to assess a model’s understanding of domain-specific knowledge. Questions were manually created by assessors based on open-source medical texts to avoid template-like structures. Annotations were performed by human assessors to ensure balanced positive and negative responses, adhering to ethical standards of medical data handling. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Russian
- **Clinical Stage:** Triage and Referral
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Link of RuMedDaNet Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 41.1 Task: RuMedDaNet

Task description not cleanly recoverable from source text.

### Task type
Natural Language Inference

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text labeled as "Context" and the clinical question labeled as "Question" in Russian, answer the clinical question with either "yes" or "no". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: answer: label The optional list for "label" is ["yes", "no"].
### Input
Context: [Clinical context] Question: [Clinical question]
### Output
answer: [yes / no]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 42. CHIP-CDN

CHIP-CDN is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CHIP-CDN dataset 29 is sourced from diagnostic text of Chinese EHRs. It focuses on clinical terminology normalization by mapping original diagnostic expressions to standardized ICD codes through manual annotation. CHIP-CDN was one of the shared tasks in the CHIP-2021 challenges and is included in the CBLUE benchmark 30. We adapted the CBLUE version for downstream task construction. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Discharge and Administration
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Link of CHIP-CDN Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 42.1 Task: CBLUE-CDN

This task is to normalize diagnostic terms in Chinese EHRs by mapping them to standard ICD codes (text).

### Task type
Normalization and Coding

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the original diagnostic text from electronic healthcare records in Chinese, normalize them to the corresponding standard diagnostic terms. Specifically, use the names of standardized terms from the 《国际疾病分类 ICD-10 北京临床版v601》, covering diagnosis, surgery, medication, examination, laboratory testing, and symptoms. There may be multiple appropriate normalized terms for the original diagnostic text. Assuming the number of normalized terms is N, return the names of N normalized terms in the output. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: Normalized terms: label 1, label 2,..., label N The optional list for "label" is the names of normalized terms (not code) from the 《国际疾病分类 ICD-10 北 京临床版v601》, covering diagnosis, surgery, medication, examination, laboratory testing, and symptoms.
### Input
[Diagnostic terms from EHRs]
### Output
Normalized terms: [normalized ICD code]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Inferred as document-level normalization/coding because the output is a normalized label/code list rather than entity spans. BRIDGE evaluates document-level normalization/coding with Accuracy as the primary metric, plus micro F1 and macro F1. Invalid outputs are replaced with random valid labels.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 43. CHIP-CTC

CHIP-CTC is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CHIP-CTC dataset 62 is derived from clinical trial documents and aims to identify matching clinical trial eligibility criteria. Clinical trials require screening appropriate participants, which involves retrieving and matching patient cases against predefined inclusion and exclusion criteria. CHIP-CTC was one of the shared tasks in the CHIP-2019 challenges and is included in the CBLUE benchmark 30. We adapted the CBLUE version for downstream task construction. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** General
- **Application Method:** Link of CHIP-CTC Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 43.1 Task: CHIP-CTC

This task is to determine whether a given clinical case matches specific inclusion or exclusion criteria from a clinical trial.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text in Chinese, identify the clinical trial criterion that this text meets. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: clinical trial criterion: label The optional list for "label" is ["疾病", "症状-患者感受", "体征-医生检测", "怀孕相关", "肿瘤进展", "疾 病分期", "过敏耐受", "器官组织状态", "预期寿命", "口腔相关", "药物", "治疗或手术", "设备", "护 理", "诊断", "实验室检查", "风险评估", "受体状态", "年龄", "特殊病人特征", "读写能力", "性别", "教 育情况", "居住情况", "种族", "知情同意", "参与其它试验", "研究者决定", "能力", "伦理审查", "依存 性", "成瘾行为", "睡眠", "锻炼", "饮食", "酒精使用", "性取向", "吸烟状况", "献血", "病例来源", "残 疾群体", "健康群体", "数据可及性"].
### Input
[Clinical text]
### Output
clinical trial criterion: [疾病 / 症状-患者感受 / 体征-医生检测 / 怀孕相关 / 肿瘤进展 / 疾病分 期 / 过敏耐受 / 器官组织状态 / 预期寿命 / 口腔相关 / 药物 / 治疗或手术 / 设备 / 护理 / 诊断 / 实验室 检查 / 风险评估 / 受体状态 / 年龄 / 特殊病人特征 / 读写能力 / 性别 / 教育情况 / 居住情况 / 种族 / 知 情同意 / 参与其它试验 / 研究者决定 / 能力 / 伦理审查 / 依存性 / 成瘾行为 / 睡眠 / 锻炼 / 饮食 / 酒精 使用 / 性取向 / 吸烟状况 / 献血 / 病例来源 / 残疾群体 / 健康群体 / 数据可及性]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 44. CHIP-MDCFNPC

CHIP-MDCFNPC is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CHIP-MDCFNPC (Medical Dialog Clinical Findings Negative and Positive Classification) dataset 29 is sourced from Chinese doctor–patient dialogues of online medical consultations. To objectively and comprehensively describe a patient’s condition, this dataset uses the concept of clinical findings—specifically focusing on the classification of these findings as positive or negative, indicating the presence or absence of a specific condition. The definitions of positivity and negativity are generally derived from the patient’s subjective complaint and the physician’s diagnostic assessment. The annotation process follows the SOAP (Subjective, Objective, Assessment, Plan) framework, a widely adopted problem-oriented medical documentation method. The positive/negative classification is primarily applied to entities identified in the Subjective (S) and Assessment (A) sections. The preprocessing pipeline includes SOAP section alignment, named entity recognition in the S and A sections, and subsequent polarity labeling. This task was part of the CHIP-2021 shared tasks and is included in the CBLUE benchmark 30. We adapted the CBLUE version for downstream task construction. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Initial Assessment
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** General
- **Application Method:** Link of CHIP-MDCFNPC Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 44.1 Task: CHIP-MDCFNPC

Task description not cleanly recoverable from source text.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical consultation in Chinese, extract the clinical findings mentioned by the patient and doctors and identify their status based on the dialogue, including: - "阳性": 已有症状疾/病等相关，医生诊断（包含多个诊断结论），以及假设未来可能发生的疾病 等，如：“如果不治疗的话，大概率会引起A疾病”，“A疾病”标注为阳性； - "阴性": 未患有的疾病症状相关； - "其他": 未知的标注其他，一般指用户没有回答、不知道或者回答不明确/模棱两可不好推断的情 况。 - "不标注": 无实际意义的不标注，一般是医生的解释说的是一般知识，和病人当前的状态条件独立 不具有标注意义，及有些检查项带疾病名称的，识别的疾病（乙肝五项/乙肝抗体），药品名中出 现的“疾病”不标注。 Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: findings:..., status:...;... findings:..., status:...; The optional list for "status" is ["阳性", "阴性", "其他", "不标注"].
### Input
[A utterance from medical consultation]
### Output
findings: [findings mention], status: [阳性 / 阴性 / 其他 / 不标注];... findings: [findings mention], status: [阳性 / 阴性 / 其他 / 不标注];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 45. MedDG

MedDG is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The MedDG dataset 63 contains doctor–patient dialogues collected from Chinese online medical consultation platforms. It covers 12 gastrointestinal diseases and includes over 17,000 dialogues and 380,000 utterances. As an entity-centric dataset, the physicians identified and formalized 160 types medical entities through a systematic annotation. Each dialogue is annotated with entities across five major categories—diseases, symptoms, severity, examinations, and medications. This dataset is included in the CBLUE benchmark 30, and we adapted the CBLUE version for downstream task construction. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Chinese
- **Clinical Stage:** Triage and Referral
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** Gastroenterology
- **Application Method:** Link of MedDG Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 45.1 Task: MedDG

This task is to generate the doctor’s response based on the provided dialogue history of a medical consultation.

### Task type
Question Answering

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical consultation in Chinese, generate the next response of the doctor based on the dialogue context. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: 医生:...
### Input
[Dialogue history of medical consultation]
### Output
医生: [generated response from doctor’s perspective]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 46. n2c2 2014 - Heart Disease Challenge

n2c2 2014 - Heart Disease Challenge is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The n2c2 2014 - Heart Disease Challenge dataset 64 is an English dataset designed for risk factor identification and temporal classification. It includes 1304 longitudinal medical records from 296 diabetic patients, compiled and de-identified for the 2014 i2b2/UTHealth NLP shared task. The dataset contains narrative clinical records, covering a wide range of heart disease risk factors such as hypertension, hyperlipidemia, obesity, smoking, family history of CAD, diabetes, and coronary artery disease (CAD). Annotations were performed using the Multi-purpose Annotation Environment (MAE) by a group of seven medical professionals, adhering to light annotation guidelines developed specifically for this task. In BRIDGE, this source dataset contributes 5 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Initial Assessment (Task "n2c2 2014-Medication" has clinical stage "Treatment and Intervention")
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Cardiology, Endocrinology
- **Application Method:** Link of n2c2 2014 - Heart Disease Challenge Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 46.1 Task: n2c2 2014-Diabetes

This task is to extract the indicators that are related to Diabetes based on the clinical document of a patient and classify each extracted indicator into two types of categories.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical document of a patient. Firstly, extract the indicators that are related to Diabetes. Secondly, classify each extracted indicator into one of the following categories (denoted as category 1): - "mention": A diagnosis of Type 1 or Type 2 diabetes, or a mention of a preexisting diagnosis. - "high A1c": An A1c test value of over 6.5. - "high glucose": 2 fasting blood glucose measurements of over 126. Finally, for each extracted indicator, classify it into one of the following categories (denoted as category 2): - "before DCT": This attribute value is used to indicate that the indicator can only be stated to be present prior to the date of the record. - "during DCT": This attribute value is used to indicate that a risk factor indicator occurred the day of the date on the record. - "after DCT": This attribute value is used to indicate that the risk factor indicator applies to the days after the date of the record. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: indicator:..., category_1:..., category_2:...;... indicator:..., category_1:..., category_2:...; The optional list for "category_1" is ["mention", "high A1c", "high glucose"]. The optional list for "category_2" is ["before DCT", "during DCT", "after DCT"].
### Input
[Clinical document of a patient]
### Output
indicator: [indicators related to Diabetes], category_1: [mention / high A1c / high glucose], category_2: [before DCT / during DCT / after DCT];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 46.2 Task: n2c2 2014-CAD

This task is to extract the indicators that are related to Coronary Artery Disease (CAD) based on the clinical document of a patient and classify each extracted indicator into two types of categories.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical document of a patient. Firstly, extract the indicators that are related to Coronary Artery Disease (CAD). Secondly, classify each extracted indicator into one of the following categories (denoted as category 1): - "mention": A diagnosis of CAD, or a mention of a history of CAD. - "event": MI, STEMI, NSTEMI OR revascularization procedures (bypass surgery, CABG, percutaneous) OR cardiac arrest OR ischemic cardiomyopathy. - "test": Exercise or pharmacologic stress test showing ischemia OR abnormal cardiac catheterization showing coronary stenoses (narrowing). - "symptom": Chest pain consistent with angina. Finally, for each extracted indicator, classify it into one of the following categories (denoted as category 2): - "before DCT": This attribute value is used to indicate that the indicator can only be stated to be present prior to the date of the record. - "during DCT": This attribute value is used to indicate that a risk factor indicator occurred the day of the date on the record. - "after DCT": This attribute value is used to indicate that the risk factor indicator applies to the days after the date of the record. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: indicator:..., category_1:..., category_2:...;... indicator:..., category_1:..., category_2:...; The optional list for "category_1" is ["mention", "event", "test", "symptom"]. The optional list for "category_2" is ["before DCT", "during DCT", "after DCT"].
### Input
[Clinical document of a patient]
### Output
indicator: [indicators related to Diabetes], category_1: [mention / event / test / symptom], category_2: [before DCT / during DCT / after DCT];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 46.3 Task: n2c2 2014-Hyperlipidemia

This task is to extract the indicators that are related to Hyperlipidemia/Hypercholesterolemia based on the clinical document of a patient and classify each extracted indicator into two types of categories.

### Task type
Event Extractionn

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Instruction text not cleanly recoverable from source text.
### Input
[Clinical document of a patient]
### Output
indicator: [indicators related to Diabetes], category_1: [mention / high cholesterol / high LDL], category_2: [before DCT / during DCT / after DCT];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 46.4 Task: n2c2 2014-Hypertension

This task is to extract the indicators that are related to Hypertension based on the clinical document of a patient and classify each extracted indicator into two types of categories.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical document of a patient. Firstly, extract the indicators that are related to Hypertension. Secondly, classify each extracted indicator into one of the following categories (denoted as category 1): - "mention": A diagnosis of Hypertension or a mention of a pre-existing condition. - "high blood pressure": Blood pressure measurement of over 140/90 mm/hg (if either value is high, the patient has hypertension). Finally, for each extracted indicator, classify it into one of the following categories (denoted as category 2): - "before DCT": This attribute value is used to indicate that the indicator can only be stated to be present prior to the date of the record. - "during DCT": This attribute value is used to indicate that a risk factor indicator occurred the day of the date on the record. - "after DCT": This attribute value is used to indicate that the risk factor indicator applies to the days after the date of the record. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: indicator:..., category_1:..., category_2:...;... indicator:..., category_1:..., category_2:...; The optional list for "category_1" is ["mention", "high blood pressure"]. The optional list for "category_2" is ["before DCT", "during DCT", "after DCT"].
### Input
[Clinical document of a patient]
### Output
indicator: [indicators related to Diabetes], category_1: [mention / high blood pressure], category_2: [before DCT / during DCT / after DCT];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 46.5 Task: n2c2 2014-Medication

This task is to extract the indicators that are related to Medication based on the clinical document of a patient and classify each extracted indicator into one of the three categories.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical document of a patient, extract the indicators that are related to Medication. Then, for each extracted indicator, classify it into one of the following categories: - "before DCT": This attribute value is used to indicate that the indicator can only be stated to be present prior to the date of the record. - "during DCT": This attribute value is used to indicate that a risk factor indicator occurred the day of the date on the record. - "after DCT": This attribute value is used to indicate that the risk factor indicator applies to the days after the date of the record. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: indicator:..., category:...;... indicator:..., category:...; The optional list for "category" is ["before DCT", "during DCT", "after DCT"].
### Input
[Clinical document of a patient]
### Output
indicator: [indicators related to Diabetes], category: [before DCT / during DCT / after DCT];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 47. CAS

CAS is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CAS dataset 65 was derived from French clinical case reports and contains 20,363 sentences and over 397,000 word occurrences. Each sentence is annotated with Concept Unique Identifiers (CUIs) corresponding to French terms in the UMLS, along with negation and uncertainty markers. The annotated corpus was used in the DEFT shared tasks in 2019 and 2020. Based on its annotations, we constructed two downstream tasks. In BRIDGE, this source dataset contributes 2 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** French
- **Clinical Stage:** Discharge and Administration
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of CAS Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 47.1 Task: CAS-label

This task is to extract patient age, gender, and clinical outcome from French clinical case reports.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical case report in French, extract the following medical information: - "age": l’âge de la personne dont le cas est décrit, au moment du dernier élément clinique rapporté dans le cas clinique, normalisé sous la forme d’un entier (soit 0 pour un nourrisson de moins d’un an, 1 pour un enfant de moins de deux ans, y compris un an et demi, 20 pour un patient d’une vingtaine d’années, etc.). - "genre": le genre de la personne dont le cas est décrit, parmi deux valeurs normalisées: féminin, masculin (il n’existe aucun cas de dysgénésie ou d’hermaphrodisme dans le corpus). si le genre n’est pas mentionné, retournez "None". - "issue": l’issue parmi cinq valeurs possibles: (1) guérison (le problème clinique décrit dans le cas a été traité et la personne est guérie), (2) amélioration (l’état clinique est amélioré sans qu’on ne puisse conclure à une guérison), (3) stable (soit l’état clinique reste stationnaire, soit il est impossible de déterminer entre amélioration et détérioration), (4) détérioration (l’état clinique se dégrade), ou (5) décès (lorsque le décès concerne directement le cas clinique décrit). si le problème n’est pas mentionné, retournez "None". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: age:..., genre:..., issue:... The optional list for "genre" is ["féminin", "masculin", "None"]. The optional list for "issue" is ["guérison", "amélioration", "stable", "détérioration", "décès", "None"].
### Input
[A clinical case report]
### Output
age: [age mention], genre: [féminin / masculin / None], issue: [guérison / amélioration / stable / détérioration / décès / None]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 47.2 Task: CAS-evidence

Task description not cleanly recoverable from source text.

### Task type
Summarization

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical care report in French, extract the evidence of the following medical information from the original text: - "genre": le genre de la personne dont le cas est décrit, parmi deux valeurs normalisées: féminin, masculin (il n’existe aucun cas de dysgénésie ou d’hermaphrodisme dans le corpus). - "origine": l’origine (motif de la consultation ou de l’hospitalisation) pour le dernier événement clinique ayant motivé la consultation. Cette catégorie intègre généralement les pathologies, signes et symptômes (par exemple, "une tuméfaction lombaire droite, fébrile avec frissons" ou "un contexte d’asthénie et d’altération de l’état général"), plus rarement les circonstances d’un accident ("une chute de 12 mètres, par défénestration, avec réception ventrale", "un AVP moto" ou "pense avoir été violée"). Le suivi clinique se trouve dans la continuité d’événements précédents. Il ne constitue pas un motif de consultation. - "issue": l’issue parmi cinq valeurs possibles: (1) guérison (le problème clinique décrit dans le cas a été traité et la personne est guérie), (2) amélioration (l’état clinique est amélioré sans qu’on ne puisse conclure à une guérison), (3) stable (soit l’état clinique reste stationnaire, soit il est impossible de déterminer entre amélioration et détérioration), (4) détérioration (l’état clinique se dégrade), ou (5) décès (lorsque le décès concerne directement le cas clinique décrit). Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: evidence of genre:...; evidence of origine:...; evidence of issue:...; The optional evidence of "genre" is the word or shot phrase that indicates the genre of the person; The optional evidence of "origine" and "issue" is the sentence or shot paragraph that indicates the origine and issue of the person, respectively. If the evidence is not mentioned, return "None".
### Input
[A clinical case report]
### Output
evidence of genre: patient; evidence of origine: None; evidence of issue: None;
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 48. RuMedNLI

RuMedNLI is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The RuMedNLI dataset 61 is a Russian language dataset designed for natural language inference in the clinical domain. It includes 14,049 records compiled through translation and manual correction of the English MedNLI dataset. The dataset contains pairs of clinical sentences—premise and hypothesis—annotated with one of three labels: entailment, contradiction, or neutral. Annotations were generated by clinicians and translated into Russian using two automatic translation systems, followed by human post-editing to ensure domain accuracy, including adaptation of medical abbreviations and measurement units. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Russian
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Critical Care
- **Application Method:** Link of RuMedNLI Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 48.1 Task: RuMedNLI-NLI

Task description not cleanly recoverable from source text.

### Task type
Natural Language Inference

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the premise-hypothesis statements pair labeled as "Premise statement" and "Hypothesis statement" in Russian, classify the inference relation between two statements into one of the three classes: "entailment", "contradiction", or "neutral". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: relation: label The optional list for "label" is ["entailment", "contradiction", "neutral"].
### Input
Premise statement: [Premise statement context] Hypothesis statement: [Hypothesis statement context]
### Output
relation: [entailment / contradiction / neutral]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 49. RuDReC

RuDReC is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The RuDReC dataset 61 is a Russian language dataset designed for named entity recognition tasks in the pharmaceutical domain. It includes 2,587 annotated reviews compiled from the Russian drug review platform Otzovik. The dataset contains user-generated reviews about pharmaceutical products, covering aspects such as drug effectiveness, adverse drug reactions, and indications. Annotations were performed using a rule-based system and verified by domain experts, adhering to a scheme that identifies drug-related entities. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Russian
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** Pharmacology
- **Application Method:** Link of RuDReC Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 49.1 Task: RuDReC-NER

This task is to extract the following types of entities from the clinical text: "Adverse Drug Reaction", "Drugclass", "Finding", "Drugform", "Drugname", "Drug Interaction".

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Russian, extract the following types of entities from the clinical text: "Adverse Drug Reaction", "Drugclass", "Finding", "Drugform", "Drugname", "Drug Interaction". Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["Adverse Drug Reaction", "Drugclass", "Finding", "Drugform", "Drugname", "Drug Interaction"].
### Input
[Clinical text of a patient]
### Output
entity: [clinical entity], type: [Adverse Drug Reaction / Drugclass / Finding / Drugform / Drugname / Drug Interaction];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 50. NorSynthClinical-PHI

NorSynthClinical-PHI is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The NorSynthClinical-PHI dataset 66 is a Norwegian dataset designed for Protected Health Information (PHI) deidentification. It includes 8,270 tokens and 409 annotated PHI instances, compiled by extending the NorSynthClinical synthetic clinical corpus. The dataset contains synthetic clinical text focusing on family history related to cardiac disease. Annotations were performed using Named Entity Tagging by two native Norwegian speakers, following guidelines adapted from previous de-identification research. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Norwegian
- **Clinical Stage:** Research
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Cardiology
- **Application Method:** Link of NorSynthClinical-PHI Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 50.1 Task: NorSynthClinical-PHI

This task is to extract the following types of entities from the clinical records:"First_Name", "Last_Name", Age", "Health_Care_Unit", "Phone_Number", "Social_Security_Number", "Date_Full", "Date_Part", "Location".

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Norwegian, extract the following types of entities from the clinical records: - "First_Name": An individual’s first name. - "Last_Name": An individual’s last name, including double last names and middle names that could be considered a last name. Any academic title (such as Dr.) should not be included. - "Age": Any age written with numbers, letters, or a mixture of both. - "Health_Care_Unit": All healthcare institutions where health care is provided (hospitals, healthcare centers, nursing homes, etc.) and their clinical units (emergency department, neuroclinic, department of medical genetics, etc.). Even abbreviations and other unofficial institution names should be included. - "Social_Security_Number ": A person’s social security number. - "Phone_Number": A phone number. Any mentioned country codes should also be included. - "Date_Full": Including the combination of date, month, and year, written with numbers, letters, or a mixture of both. - "Date_Part": Including one or two of the instances date, month, and year, written with numbers, letters, or a mixture of both. Does not include weekdays, week numbers, or seasons. - "Location": Any geographical location, including countries, cities, towns, post codes, addresses, etc. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["First_Name", "Last_Name", "Age", "Health_Care_Unit", "Social_Security_Number", "Phone_Number", "Date_Full", "Date_Part", "Location"].
### Input
[Clinical text of a patient]
### Output
entity: [clinical entity], type: [First_Name / Last_Name / Age / Health_Care_Unit / Social_Security_Number / Phone_Number / Date_Full / Date_Part / Location];
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 51. RuCCoN

RuCCoN is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. RuCCoN 67 is a Russian-language dataset designed for clinical concept normalization. It comprises medical histories from more than 60 patients at the Scientific Center of Children’s Health, focusing on allergic and pulmonary disorders. The dataset includes deidentified discharge summaries, radiology, echocardiography, and ultrasound diagnostic reports, as well as recommendations and other physician records. RuCCoN contains more than 16,028 entity mentions, manually mapped to 2,409 unique concepts from the Russian-language section of UMLS. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Russian
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Pulmonology
- **Application Method:** Link of RuCCoN Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 51.1 Task: RuCCoN

The objective of this task is to extract all clinical entities from the text and identify their corresponding type as one of the following categories: Disease, Symptom, Drug, Treatment, Body location, Severity, or Course.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical text of a patient in Russian, extract the following types of entities from the clinical text: - "Disease": A definite pathologic process with a characteristic set of signs and symptoms. - "Symptom": Subjective evidence of disease perceived by the patient. - "Drug": A drug product that contains one or more active and/or inactive ingredients; it is intended to treat, prevent or alleviate the symptoms of disease. - "Treatment": Procedures concerned with the remedial treatment or prevention of diseases. - "Body location": Named locations of or within the body. - "Severity": The intensity of a specific adverse event evaluated based on the magnitude of clinical signs, symptoms and findings. - "Course": The course a disease typically takes from its onset, progression in time, and eventual resolution or death of the affected individual. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["Disease", "Symptom", "Drug", "Treatment", "Body location", "Severity", "Course"].
### Input
[Clinical text of a patient Russian]
### Output
entity: [clinical entity], type: [Disease / Symptom / Drug / Treatment / Body location / Severity / Course
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 52. CLISTER

CLISTER is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CLISTER corpus 68 is a French Semantic Textual Similarity (STS) dataset comprising 1,000 sentence pairs from the clinical domain, each manually annotated with similarity scores. The clinical cases were sourced from CAS 69, a French corpus containing clinical case descriptions that encompass a variety of clinical information, including medical history, treatments, and follow-ups. Each pair of sentences was given a similarity score between 0 and 5, with 0 indicating no similarity and 5 indicating the highest level of similarity. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** French
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of CLISTER Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 52.1 Task: CLISTER

Task description not cleanly recoverable from source text.

### Task type
Semantic Similarity

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following two clinical sentences that are labeled as "Sentence A" and "Sentence B" in French, decide the similarity of the two sentences. Specifically, analyze the potential similarity, including: Surface similarity: concerns the structural similarity. This similarity is based on grammatical words or words that are not related to the domain. Two sentences that have a surface similarity can be syntactically close but semantically distant. Semantic similarity: concerns medical concepts. The closer the concepts are to one another, the higher the similarity. These concepts can refer to medications, diseases, procedures, and others. Clinical compatibility: going further into the semantics, clinical compatibility is an assessment of whether sentences in a pair can refer to the same clinical case. Then, assign a similarity score to the sentence pair based on the following scale: - "0": For sentence pairs with only surface similarity, such as words non-specific to the medical domain or stop-words. - "1": For sentence pairs with only surface similarity, concerning at most one medical entity. - "2": For sentence pairs containing medical concepts with low semantic similarity, but no clinical compatibility. Typically, sentences in a pair can concern a disease, a procedure, or a drug. - "3": For sentence pairs with semantic similarity on several medical concepts making them partially clinically compatible. - "4": For sentence pairs with high semantic similarity and clinical compatibility. One sentence may contain more information than the other may, and vice-versa. - "5": For sentence pairs with high semantic similarity and full clinical compatibility. The sentences have globally the same meaning, while one may be more specific than the other. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: similarity score: score The optional list for "score" is ["0", "1", "2", "3", "4", "5"].
### Input
[Clinical sentence pair in French]
### Output
similarity score: [0 / 1 / 2 / 3 / 4 / 5]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 53. BRONCO150

BRONCO150 is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. BRONCO150 70 is a corpus containing 150 German discharge summaries from cancer patients diagnosed with hepatocellular carcinoma or melanoma, treated at Charite Universitaetsmedizin Berlin or Universitaetsklinikum Tuebingen. The corpus consists of 11,434 sentences and 89,942 tokens, with 11,124 annotations for medical entities and 3,118 annotations for related attributes. It is annotated with labels for diagnosis (ICD10), treatment (OPS), and medication (ATC), and the data is normalized to these terminologies. The corpus is provided in five splits (randomSentSet1-5) in both XML and CONLL formats. Annotation followed a structured, quality-controlled process involving two groups of medical experts to ensure consistency and high-quality annotations. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** German
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Discharge Summary
- **Clinical Specialty:** Oncology
- **Application Method:** Link of BRONCO150 Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The corpus is provided in five splits (randomSentSet1-5) in both XML and CONLL formats.

### 53.1 Task: BRONCO150-NER&Status

Task description not cleanly recoverable from source text.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following sentences from a discharge summary of a cancer patient (hepatocellular carcinoma or melanoma) in German, extract the medical entities with their types and identify their corresponding normalized terms. - "diagnosis": A diagnosis is a disease, a symptom, or a medical observation that can be matched with the German Modification of the International Classification of Diseases-10 (ICD-10-GM: https://www. bfarm.de/DE/Kodiersysteme/Klassifikationen/ICD/ICD-10-GM/_node.html). - "treatment": A treatment is a diagnostic procedure, an operation, or a systemic cancer treatment that can be found in the Operationen und Prozedurenschlu¨ssel (OPS: https://www.bfarm.de/DE/ Kodiersysteme/Klassifikationen/OPS-ICHI/OPS/_node.html). - "medication": A medication names a pharmaceutical substance or a drug that can be related to the Anatomical Therapeutic Chemical Classification System (ATC: https://www.bfarm.de/DE/ Kodiersysteme/Klassifikationen/ATC/_node.html). Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:..., normalized terms:...;... entity:..., type:..., normalized terms:...; The optional list for "type" is ["diagnosis", "treatment", "medication"]. The normalized terms should be the corresponding text of normalized terms from the ICD-10-GM, OPS, or ATC classification systems.
### Input
[Discharge summary of cancer patient in German]
### Output
entity: [clinical entity], type: [diagnosis / treatment / medication], normalized terms: [ICD-10-GM / OPS / ATC normalized term]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 54. CARDIO:DE

CARDIO:DE is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The CARDIO:DE 71 dataset is a German clinical corpus containing 500 routine doctor’s letters from Heidelberg University, representing a diverse range of cases from a tertiary care cardiovascular center during 2020 and 2021. The corpus includes 311 in-patient, 172 out-patient, and 17 cardiac emergency room letters, offering a comprehensive collection of clinical documentation. The dataset comprises a total of 993,143 tokens, with approximately 31,952 unique tokens. It is randomly divided into two subsets: CARDIO:DE400, which contains 400 documents with 805,617 tokens and 114,348 annotations, and CARDIO:DE100, which includes 100 documents, 187,526 tokens, and 26,784 annotations. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** German
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** General EHR Note
- **Clinical Specialty:** Cardiology
- **Application Method:** Link of CARDIO:DE Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 54.1 Task: CARDIO-DE

The objective of this task is to extract the following types of entities from clinical documents related to the cardiovascular domain: "ACTIVEING", "DRUG", "DURATION", "FORM", "FREQUENCY", and "STRENGTH".

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following clinical document related to the cardiovascular domain in German, extract the following types of entities from the clinical text: - "ACTIVEING": The primary ingredient in the medication responsible for its therapeutic effect. - "DRUG": The name of the medication, including brand or generic name. - "DURATION": The length of time the medication is to be taken. - "FORM": The physical form of the medication, such as tablet, capsule, or liquid. - "FREQUENCY": How often the medication should be taken within a specific time period. - "STRENGTH": The concentration or dosage of the active ingredient in the medication. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["ACTIVEING", "DRUG", "DURATION", "FORM", "FREQUENCY", "STRENGTH"].
### Input
[Doctor’s letter from the cardiology department in German]
### Output
entity: [clinical entity], type: [ACTIVEING / DRUG / DURATION / FORM / FREQUENCY / STRENGTH]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 55. GraSSCo_PHI

GraSSCo_PHI is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. GraSSCo_PHI 72 is a synthetic clinical dataset made up of carefully designed fictional discharge summaries. It comprises 63 clinical documents, containing approximately 5,000 sentences and over 43,000 tokens. The dataset features a nearly equal gender distribution, with about two-thirds of the cases involving hospitalized in-patients, and it covers a broad spectrum of medical specialties, including ophthalmology, oncology, and orthopedics. More than 1,400 instances of Protected Health Information (PHI) were automatically annotated using the Averbis Health Discovery (AHD) pipeline 73. These annotations were then reviewed and refined by two trained annotators via the INCEpTION platform, who corrected any missed or misidentified PHI to improve annotation accuracy. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s), not as a standalone newly named benchmark created by this survey.

- **Language:** German
- **Clinical Stage:** Research
- **Source Clinical Document Type:** Discharge Summary, Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of GraSSCo_PHI Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark with 1 BRIDGE-new task reformulation(s)
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 55.1 Task: GraSSCo PHI

The objective of this task is to extract all instances of Protected Health Information (PHI) from the synthetic patient discharge summaries and identify their corresponding PHI type.

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Newly constructed task reformulation on this source dataset. Based on the annotated PHI information, we formulated this task as an NER task, requiring the model to identify text spans corresponding to PHI entities and classify them into their respective types.

```md
### Instruction
Given the clinical summaries of a patient in German, extract the following types of entities from the clinical text: - "LOCATION_COUNTRY": Country name or reference - "NAME_DOCTOR": Name of a medical professional - "AGE": Numeric representation of a person’s age - "CONTACT_FAX": Fax number for communication - "LOCATION_ZIP": Postal or ZIP code - "LOCATION_ORGANIZATION": Name of an organization or institution - "CONTACT_PHONE": Phone number for communication - "DATE": Calendar date - "LOCATION_CITY": Name of a city - "CONTACT_EMAIL": Email address - "NAME_PATIENT": Name of a patient - "LOCATION_HOSPITAL": Name of a hospital or medical facility - "PROFESSION": Job title or occupation - "NAME_TITLE": Honorific or title before a name - "NAME_USERNAME": Username for online identification - "ID": Identification number or code - "NAME_RELATIVE": Name of a family member - "NAME_EXT": Name suffix, extension, or additional identifier - "LOCATION_STREET": Street address or name Return your answer in the following format. Do not output entities whose types do not exist in the clinical text. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["LOCATION_COUNTRY", "NAME_DOCTOR", "AGE", "CONTACT_FAX", "LOCATION_ZIP", "LOCATION_ORGANIZATION", "CONTACT_PHONE", "DATE", "LOCATION_CITY", "CONTACT_EMAIL", "NAME_PATIENT", "LOCATION_HOSPITAL", "PROFESSION", "NAME_TITLE", "NAME_USERNAME", "ID", "NAME_RELATIVE", "NAME_EXT", "LOCATION_STREET"]
### Input
[Synthetic discharge summary of a patient in German]
### Output
entity: [clinical entity], type: [LOCATION_COUNTRY / NAME_DOCTOR / AGE / CONTACT_FAX / LOCATION_ZIP / LOCATION_ORGANIZATION / CONTACT_PHONE / DATE / LOCATION_CITY / CONTACT_EMAIL / NAME_PATIENT / LOCATION_HOSPITAL / PROFESSION / NAME_TITLE / NAME_USERNAME / ID / NAME_RELATIVE / NAME_EXT / LOCATION_STREET]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 56. IFMIR

IFMIR is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The IFMIR corpus 74 comprises 58,658 machine-annotated Japanese incident reports sourced from the Japan Council for Quality Health (JQ). These reports capture a range of medication-related incidents, such as incorrect administration, missed doses, and overdoses (https://www.med-safe.jp/index.html). The dataset includes 478,175 named entities and features three annotation types: medication entities, entity relations, and intention/factuality 75. To validate the annotations, a random sample of 40 incident reports was manually reviewed. In BRIDGE, this source dataset contributes 3 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Japanese
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** Pharmacology
- **Application Method:** Link of IFMIR Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 56.1 Task: IFMIR-Incident type

Task description not cleanly recoverable from source text.

### Task type
Text Classification

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the medical incident report in Japanese, determine what type of incident occurred. One report might contain more than one incident type. The incident types and their definitions are as follows: - "Wrong Drug": Wrong drug occurs when inappropriate medication or IV fluid is prescribed, dispensed, prepared or administered. Wrong drug applies when the intended drug and the actual drug are different. A generic substitution is not considered as a wrong drug. - "Wrong Form": Wrong form occurs when the wrong form of drug is ordered, dispensed or administered. - "Wrong Mode": Wrong mode occurs when the wrong mode of a medication is ordered, dispensed or administered. - "Wrong Strength amount": Wrong amount is defined as a dose of medication or volume of IV fluid over or under the intended amount, taking into account the patient’s age, weight, renal and liver function. - "Wrong Strength rate": Wrong rate is defined as a rate, e.g., IV rate, being slower or faster than intended. - "Wrong Strength concentration": Wrong concentration is defined as the concentration of a medication being higher or lower than intended. Concentration is also closely related to amount and rate; most cases of ’Wrong Strength concentration’ co-occur with ’Wrong Strength rate’ or ’Wrong Strength amount’. A wrong concentration might be reported as a wrong amount. - "Wrong Timing": Timing-related errors are defined as administration too early or too late, relative to the time designated by the healthcare facility. There are three scenarios associated with wrong timing: No ’omission’ or ’extra drug’ results from wrong timing, ’omission’ results from wrong timing, or ’extra drug’ results from wrong timing. - "Wrong Date": Wrong date refers to the medication being administered for a different date compared to the intended date. - "Wrong Duration": Wrong duration refers to the medication being administered for a longer or shorter period than intended. - "Wrong Frequency": A wrong frequency occurs when the prescribed or administered frequency of delivery for a drug or an IV rate falls outside of the recommended range or planned number. If the frequency is larger, it is often also labeled as an extra drug. If the frequency is smaller, then ’omission’ is applicable. Wrong timing is also relevant is such cases. - "Wrong Dosage": Patients may be subject to excessive or insufficient amounts of a drug. - "Wrong Route": Wrong route occurs when a medication is prescribed or administered via an incorrect route of administration, e.g., a drug that creates strong vascular irritation and should be given via the central line is administered via the peripheral line. - "Others": Other errors that are not covered by the current scope of the previous annotations, e.g., procedural errors such as forgetting to fill out a questionnaire before administrating a vaccine to a patient. For errors that are out of the scope of the above or the free text inputs does not present any error, the incident type is registered as ’Others’. Assuming the number of incident types is N, return the N recognized incident types in the output. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: incident type: type 1, type 2,..., type N The optional list for "type" is ["Wrong Drug", "Wrong Form", "Wrong Mode", "Wrong Strength amount", "Wrong Strength rate", "Wrong Strength concentration", "Wrong Timing", "Wrong Date", "Wrong Duration", "Wrong Frequency", "Wrong Dosage", "Wrong Route", "Others"].
### Input
[Incident report in Japanese]
### Output
incident type: [Wrong Drug / Wrong Form / Wrong Mode / Wrong Strength amount / Wrong Strength rate / Wrong Strength concentration / Wrong Timing / Wrong Date / Wrong Duration / Wrong Frequency / Wrong Dosage / Wrong Route / Others]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Accuracy is the primary metric; micro F1 and macro F1 are also reported. Invalid outputs are replaced with random valid labels under the BRIDGE evaluation pipeline.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 56.2 Task: IFMIR-NER

The objective of this task is to extract the following entity types from the Japanese incident reports: "Strength concentration", "Frequency", "Date", "Drug", "Dosage", "Strength rate", "Drug form", "Duration", "Strength amount", "Drug mode", "Route", "Timing".

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following medical incident report in Japanese, extract the following types of entities from the medical text. - "Strength concentration": Concentration is defined as diluted medication concentration with nominator and denominator or presented as percentage or IV fluid concentration. - "Frequency": Frequency is defined as how many times a drug is given per unit of time. - "Date": Date is defined as a time unit including a date and time unit longer than one day. - "Drug": The intended to deliver or actual delivered drug name, or entities described as drugs. - "Dosage": Dosage is defined as the number of units (e.g., tables, bottles, ampules) given to the patient as a single dose. - "Strength rate": Rate typically represents one measure against another quantity or measure. - "Drug form": The form of a drug (e.g., tablet, subcutaneous injection). - "Duration": Duration is defined as the period during which a drug is administered to the patient. - "Strength amount": The amount is defined as medication dose or IV fluid volume. - "Drug mode": The mode is a drug mode of action that is associated with pharmacologic action. - "Route": Route is defined as the route of drug administration to the patient, which may include the infusion sites, routes and pumps. - "Timing": Timing is defined as a scheduled administration time that is predefined as time interval. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["Strength concentration", "Frequency", "Date", "Drug", "Dosage", "Strength rate", "Drug form", "Duration", "Strength amount", "Drug mode", "Route", "Timing"].
### Input
[Incident report in Japanese]
### Output
entity: [clinical entity], type: [Strength concentration / Frequency / Date / Drug / Dosage / Strength rate / Drug form / Duration / Strength amount / Drug mode / Route / Timing]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```

### 56.3 Task: IFMIR - NER&factuality

The objective of this task is to extract the following entity types from Japanese incident reports: "Strength Concentration," "Frequency," "Date," "Drug," "Dosage," "Strength Rate," "Drug Form," "Duration," "Strength Amount," "Drug Mode," "Route," and "Timing." Additionally, this task requires determining the intention and factuality of the incident. Intention refers to whether the medication was intended to be administered, while factuality indicates whether the medication was actually administered.

### Task type
Event Extraction

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following medical incident report in Japanese, extract the medical entities with their corresponding types and intention and factuality information. Specifically, need to extract all the following information for each entity: 1. Entity types: - "Strength concentration": Concentration is defined as diluted medication concentration with nominator and denominator or presented as percentage or IV fluid concentration. - "Frequency": Frequency is defined as how many times a drug is given per unit of time. - "Date": Date is defined as a time unit including a date and time unit longer than one day. - "Drug": The intended to deliver or actual delivered drug name, or entities described as drugs. - "Dosage": Dosage is defined as the number of units (e.g., tables, bottles, ampules) given to the patient as a single dose. - "Strength rate": Rate typically represents one measure against another quantity or measure. - "Drug form": The form of a drug (e.g., tablet, subcutaneous injection). - "Duration": Duration is defined as the period during which a drug is administered to the patient. - "Strength amount": The amount is defined as medication dose or IV fluid volume. - "Drug mode": The mode is a drug mode of action that is associated with pharmacodynamic action. - "Route": Route is defined as the route of drug administration to the patient, which may include the infusion sites, routes and pumps. - "Timing": Timing is defined as a scheduled administration time that is predefined as time interval. 2. Intention / factuality information: - "IA": Intended & Actual. The entity was intended to be given and was actually given. This indicates no error has occurred as to this entity. - "IN": Intended & Not-actual. The entity was intended to be given but actually was not given. This indicates the intended medication was not delivered. - "NA": Not-intended & Actual. The entity was not intended to be given but actually was. This indicates the not intended medication was mistakenly delivered. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:..., intention:...;... entity:..., type:..., intention:...; The optional list for "type" is ["Strength concentration", "Frequency", "Date", "Drug", "Dosage", "Strength rate", "Drug form", "Duration", "Strength amount", "Drug mode", "Route", "Timing"]. The optional list for "intention" is ["IA", "IN", "NA"].
### Input
[Incident report in Japanese]
### Output
entity: [clinical entity], type: [Strength concentration / Frequency / Date / Drug / Dosage / Strength rate / Drug form / Duration / Strength amount / Drug mode / Route / Timing], intention: [IA / IN / NA]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 57. iCorpus

iCorpus is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. iCorpus 76 is a Japanese-language dataset created from publicly accessible case reports sourced via J-STAGE, a Japanese platform for academic publications. The dataset contains text extracted from the case sections of reports that mention intractable diseases recognized by the Japanese Ministry of Health, Labor, and Welfare. iCorpus includes 179 case reports (across 183 files), representing 102 out of the 333 officially designated intractable diseases. Annotations were carried out using Brat (https://github.com/aih-uth/brat_entity_linking), an open-source annotation tool 77. The annotation guidelines were developed, refined, and validated by experts in medical informatics. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** Japanese
- **Clinical Stage:** Treatment and Intervention
- **Source Clinical Document Type:** Case Report
- **Clinical Specialty:** General
- **Application Method:** Link of iCorpus Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 57.1 Task: iCorpus

The objective of this task is to extract the following types of entities from the case reports: "age", "sex", "smoking", "drinking", "state", "body", "tissue", "item", "clinical test", "PN", "judge", "quantity evaluation", "quantity progress", "quality evaluation", "quality progress", "value", "unit", "time", or "time span".

### Task type
Named Entity Recognition

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the clinical report of a patient in Japanese, extract the following types of entities from the clinical text: - "age": 年齢を示す表現, 例: 63歳, 56歳, 1歳6か月, 高校生. - "sex": 性別を示す表現, 例: 男性, 女性, 男児, 女児. - "smoking": 喫煙に関する表現, 例: 喫煙, タバコ, 喫煙歴, 禁煙. - "drinking": 飲酒に関する表現, 例: 飲酒, アルコール, 飲酒歴, 禁酒. - "state": 患者の状態全般を示す表現. いわゆる, 病名, 症状 (患者の訴え), 所見(観察結果) などを含 む, 例: 吐き気, 萎縮症, 糖尿病, 口渇. - "body": 人体部位. 特定の部位を示す表現, 例: 頭,胃,肝,手足, 眼瞼結膜. - "tissue": 人体組織.人体各所で繰り返し出現するもの, 例: 筋,筋肉,粘膜, 細胞, 繊維. - "item": 患者の状態を表すために参照される項目, 例: 血糖,血糖値, HbA1c, 食欲. - "clinical test": 臨床検査に関する表現. item との違いは計測法を含むか否か, 例: 神経学的検査, 徒 手筋力検査. - "PN": 患者の状態が, ある (Positive), ない (Negative), わからない (None) ことを示す表現, 例: で、 認め, 示す, 認めるなし, 認めず, ではなく, なく不明であった、詳細不明. - "judge": 医療者により, 患者の状態がある (Positive), あることが疑われ る (Suspicious), 将来あるも しれない (Future), ない (Negative), 不明 (None)であることが判断されたことを示す表現, 例: 診断さ れた, 考えられた, 疑われた, 可能性も考え否定的, 明らかではなかった確定診断に至らなかった. - "quantity evaluation": 数値への評価。 高い (High), 正常 (Normal) 低い (Low), 例: 上昇, 異常高値, 増 加, 正常, 基準値, 保たれて低下, 減少, 減弱. - "quantity progress": 数値の変化。 上昇 (Increase) 変化なし (NoChange)低下 (Decrease). - "quality evaluation": 数値以外の状態の程度を質的に示す表現. 主に疾患の重症度を示 す 軽度 (Mild) 中等度 (Moderate) 重度・高度 (Severe), 例: 軽度, 軽い, わずか, やや中等度, 中度, 中等症強い, 著名, 著しい, 重度. - "quality progress": 数値以外の状態の時間的な変化を質的に示す表現. 出現 (Start) 悪化 (Worsen), 持続 (NoChange), 改善 (Improve), 軽快 (Recover), 例: 出現した, なった, きたした悪化, 増悪, 進行, 顕 在化持続, 保たれて, 変わらず改善, 軽快, 回復落ち着き, 復帰, 軽快, 回復. - "value": 検査値など、 身体や検体を測定し得られる数値, 例: 7.5, 20, 1, 5, 165.0. - "unit": 数値との組で表される単位, 例: mg/日, 行, cm, kg/m2. - "time": 時間軸上における特定位置の時点や区間を示す表現, 例: 約10年前, その後直後. - "time span": 時間軸上の位置を問わず時間幅を示す表現, 例: 1日, 長時間, 2カ月間. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: entity:..., type:...;... entity:..., type:...; The optional list for "type" is ["age", "sex", "smoking", "drinking", "state", "body", "tissue", "item", "clinical test", "PN", "judge", "quantity evaluation", "quantity progress", "quality evaluation", "quality progress", "value", "unit", "time", "time span"].
### Input
[Clinical report of patient in Japanese]
### Output
entity: [clinical entity], type: [age / sex / smoking / drinking / state / body / tissue / item / clinical test / PN / judge / quantity evaluation / quantity progress / quality evaluation / quality progress / value / unit / time / time span]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
Event-level micro F1 is the primary metric and subject-level micro F1 is also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 58. icliniq-10k

icliniq-10k is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The icliniq-10k dataset 78 contains real English conversations between patients and doctors collected from online medical consultation platforms. It includes 7,231 records, each consisting of a patient’s healthcare inquiry and the corresponding doctor’s response. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Triage and Referral
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** General
- **Application Method:** Link of icliniq-10k Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 58.1 Task: icliniq-10k

This task is to generate the doctor’s response based on the provided dialogue history of a medical consultation.

### Task type
Question Answering

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following question from a patient, generate the doctor’s response based on the dialogue context. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: doctor:...
### Input
[Clinical query from patient ]
### Output
doctor: [generated response from doctor’s perspective]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```


## 59. HealthCareMagic-100k

HealthCareMagic-100k is treated here as a constituent benchmark section under the BRIDGE umbrella evaluation. The HealthCareMagic-100k dataset 78 consists of real English conversations between patients and doctors collected from an online medical consultation platform. It contains 111,996 records, each comprising a healthcare inquiry from the patient and the doctor’s corresponding reply. In BRIDGE, this source dataset contributes 1 task(s) and is normalized as a reused source dataset / sub-benchmark, not as a standalone newly named benchmark created by this survey.

- **Language:** English
- **Clinical Stage:** Triage and Referral
- **Source Clinical Document Type:** Consultation Record
- **Clinical Specialty:** General
- **Application Method:** Link of HealthCareMagic-100k Dataset
- **BRIDGE Role:** Reused source dataset / sub-benchmark
- **Split / Sample Info:** The per-dataset subsection does not restate an exact split. BRIDGE methods say official splits were used when available; otherwise datasets with >2000 samples used a 10% test split, datasets with 1000-2000 used a 20% test split, and datasets with <1000 used all samples for testing except 20 cases reserved for few-shot example selection. Exact task-level testing counts are listed in Supplementary Table S9.

### 59.1 Task: HealthCareMagic-100k

This task is to generate the doctor’s response based on the provided dialogue history of a medical consultation.

### Task type
Question Answering

- **Task provenance in BRIDGE:** Reused task from the named source dataset; BRIDGE standardizes prompt/input/output formatting for benchmarking.

```md
### Instruction
Given the following question from a patient, generate the doctor’s response based on the dialogue context. Return your answer in the following format. DO NOT GIVE ANY EXPLANATION: doctor:...
### Input
[Clinical query from patient ]
### Output
doctor: [generated response from doctor’s perspective]
```

### Task example

```md
### Example
The paper appendix provides a task-specific prompt template rather than a concrete dataset instance with verbatim input text and gold output.
The appendix-native template is reflected in the `Instruction`, `Input`, and `Output` fields above for this task.
A concrete patient-level or document-level benchmark row with gold answer is not printed in the paper itself.
```

### Scoring standard

```md
### Scoring
ROUGE-average is the primary metric; BLEU-4 and BERTScore are also reported. Invalid outputs are retained as empty responses.
### Evaluation Dimensions
Deterministic comparison against the original dataset reference standard released with the source dataset. BRIDGE does not describe extra rubric dimensions beyond the task-family metrics for this task.
### Judge Prompt
Not applicable. The paper uses deterministic task metrics rather than an LLM judge for this task.
```
