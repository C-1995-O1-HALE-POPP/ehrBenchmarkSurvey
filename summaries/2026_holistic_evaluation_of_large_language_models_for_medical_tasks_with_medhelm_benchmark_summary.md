<!-- paper_key: "2026_holistic_evaluation_of_large_language_models_for_medical_tasks_with_medhelm" -->
<!-- paper_url: "https://www.nature.com/articles/s41591-025-04151-2" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *Holistic evaluation of large language models for medical tasks with MedHELM*

Source paper: [https://www.nature.com/articles/s41591-025-04151-2](https://www.nature.com/articles/s41591-025-04151-2)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry was intentionally not edited for this task because ownership was limited to this summary file.
- The local `source.txt` is an HTML text extraction from the Nature article page, not `pdftotext` output from the publisher PDF endpoint.
- Normalization choice: `MedHELM` is treated as an umbrella evaluation framework, not a single benchmark entry. The summary therefore uses one dataset-level benchmark section per constituent benchmark listed by the paper.
- Benchmark inventory anchor: the paper's Data availability paragraph explicitly lists 37 datasets, grouped as 16 public, 7 gated, and 14 private datasets. That paper-level list is treated as canonical for benchmark existence.
- Task instructions, prompt shapes, split behavior, and metric details were cross-checked against official companion resources when available: `medhelm.org`, CRFM HELM MedHELM docs, `stanford-crfm/helm` `schema_medhelm.yaml`, `run_entries_medhelm_public.conf`, `run_entries_medhelm_gated.conf`, `medhelm_run_specs.py`, and scenario source files.
- Important discrepancy: the current official companion code/docs inspected expose scenario metadata for most of the 37 datasets, but do not visibly expose `MedQA` or `MedMCQA` as MedHELM run specs in `v0.5.7`. Those two datasets are nevertheless retained because they are explicitly listed in the Nature paper. Their task descriptions below are marked as paper-inventory plus source-benchmark inference.
- Important discrepancy: the current companion code exposes some implementation-level details that are more specific than the Nature main text, such as zero-shot `max_train_instances=0`, benchmark-specific adapter instructions, and a subset of visible subject/subset parameters. Those details are labeled as sourced from official companion code rather than from the Nature article itself.
- Example policy: no task examples were fabricated. When the MedHELM paper does not provide a worked example but an official public companion scenario publishes a sample prompt, dataset example, or prompt-construction template, that source text is now copied verbatim into the relevant task section and labeled as companion-scenario evidence. If the public companion artifact still does not expose a concrete instance or full template, the section explicitly says so.
- Judge prompt policy: many generation benchmarks use benchmark-specific annotators or jury-style metrics in the companion code, but the full grading prompt is generally not explicitly published in the Nature paper or the companion artifacts inspected. Those cases are marked as unavailable.

## Verifier Notes

- Verified the umbrella framing, taxonomy size, and 37-dataset inventory against the Nature article abstract and data availability text.
- Verified public / gated / private access buckets against the Nature article data availability paragraph.
- Verified benchmark names and most benchmark-level descriptions against `schema_medhelm.yaml`.
- Verified task instructions and zero-shot evaluation configuration for most benchmarks against `medhelm_run_specs.py`.
- Verified concrete input structure, when available, against official scenario files in `stanford-crfm/helm`.
- `MedQA` and `MedMCQA` are present in the Nature paper inventory but absent from the inspected MedHELM `v0.5.7` schema/run-spec code. Their benchmark sections are retained with explicitly labeled inference.

## 0. MedHELM (Umbrella Evaluation Framework)

MedHELM is an umbrella medical LLM evaluation framework introduced by the paper rather than a single dataset. The Nature paper defines a clinician-validated taxonomy with 5 top-level categories, 22 subcategories, 121 specific medical tasks, and a benchmark suite of 37 dataset evaluations. The paper evaluates nine frontier models and uses an automated LLM-jury method to compare model outputs on open-ended tasks, while closed-form tasks use benchmark-specific automatic metrics. The 37 constituent benchmarks are the unit of survey normalization below.

- **Language:** Primarily English in the released benchmark suite; some benchmark languages are benchmark-specific and not all are explicitly restated in the paper
- **Clinical Stage:** Cross-stage umbrella evaluation spanning diagnosis, treatment, documentation, patient communication, research, and administration
- **Source Clinical Document Type:** Mixed benchmark portfolio including longitudinal EHR event streams, clinical notes, radiology reports, discharge documents, medical dialogue, consumer questions, SQL schemas, portal messages, and research abstracts
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Benchmark framework introduced in the paper; benchmark inventory normalized here into dataset-level sections

### Umbrella scoring and reporting

```md
### Scoring
The Nature paper reports benchmark-level win rates and category-level aggregate comparisons across 37 evaluations. Closed-form benchmarks use their benchmark-specific automatic metrics (for example exact match, execution accuracy, precision/recall/F1, or task-specific benchmark metrics). Open-ended generation benchmarks use benchmark-specific annotators and LLM-jury style evaluation in the official companion implementation. The paper reports an automated LLM-jury using multiple AI evaluators, but it does not publish a single universal rubric prompt covering all 37 datasets.
### Evaluation Dimensions
- Benchmark-specific correctness or quality dimensions depending on the constituent dataset.
- For open-ended tasks, expert-defined criteria assessed by multiple AI evaluators according to the paper.
### Judge Prompt
The full general MedHELM jury prompt is not explicitly provided in the Nature paper. Benchmark-specific annotator prompts are also generally not explicitly exposed in the companion artifacts inspected.
```

## Benchmark Inventory

- Public benchmarks in the paper: `MedCalc-Bench`, `MTSamples`, `Medec`, `HeadQA`, `Medbullets`, `MedQA`, `MedMCQA`, `ACI-Bench`, `MTSamples Procedures`, `MedicationQA`, `MedDialog`, `MEDIQA-QA`, `PubMedQA`, `EHRSQL`, `RaceBias`, `MedHallu`
- Gated benchmarks in the paper: `EHRSHOT`, `MedAlign`, `DischargeMe`, `MIMIC-RRS`, `MIMIC-BHC`, `N2C2-CT`, `MIMIC-IV Billing Code`
- Private benchmarks in the paper: `CLEAR`, `ADHD-Behavior`, `ADHD-MedEffects`, `NoteExtract`, `PatientInstruct`, `MedConfInfo`, `MentalHealth`, `PrivacyDetection`, `ProxySender`, `BMT-Status`, `HospiceReferral`, `ClinicReferral`, `CDI-QA`, `ENT-Referral`

## 1. MedCalc-Bench

MedCalc-Bench is a public benchmark used by MedHELM for clinical calculation tasks from patient notes. The official companion schema describes it as computing clinically relevant values from patient-note-plus-question inputs. The scenario source states that the source benchmark contains 10,053 training instances and 1,047 test instances and covers 55 different medical calculation tasks.

- **Language:** English
- **Clinical Stage:** Supporting diagnostic decisions
- **Source Clinical Document Type:** Patient note plus calculation question
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 1.1 Task: Clinical Calculation from Patient Note

This task is to compute a requested medical value from a patient note and a clinical question.

### Task type
Calculation / generation evaluated with task-specific accuracy

```md
### Instruction
Given a patient note and a clinical question, compute the requested medical value.
### Input
[Patient note] + [clinical question asking for a score, ratio, severity index, or other derived value]
### Output
[Only the requested quantity, without units or explanation]
```

### Task example

```md
### Example
MedCalc-Bench is the first medical calculation dataset used to benchmark LLMs ability to serve as clinical calculators.
Each instance in the dataset consists of a patient note, a question asking to compute a specific clinical value, a final answer value, and a step-by-step solution explaining how the final answer was obtained. Our dataset covers 55 different calculation tasks.

Sample Prompt:
    Given a patient note and a clinical question, compute the requested medical value.
    Be as concise as possible.

    Patient note: A 70-year-old female was rushed into the ICU due to respiratory distress,
    following which she was promptly put on mechanical ventilation. Her delivered oxygen fell
    to 51 % FiO₂; meanwhile, her partial pressure of oxygen (PaO₂) registered at 74 mm Hg.
    She was conscious but visibly disoriented with a functional Glasgow Coma Score of 12.
    She was hypotensive with blood pressure of 91/70 mm Hg. Multiple vasopressors are being administered
    simultaneously including DOPamine at 4 mcg/kg/min, norEPINEPHrine at 0.06 mcg/kg/min,
    DOBUTamine at 3 mcg/kg/min, and EPINEPHrine at 0.03 mcg/kg/min. Laboratory evaluations
    revealed mild renal impairment with creatinine levels slightly elevated at 1.6 mg/dL
    and a bilirubin level of 1.9 mg/dL. Her platelet count was found to be 165,000/µL.
    Her daily urine output of 950 mL.
    Question: What is the patient's Sequential Organ Failure Assessment (SOFA) Score?

    Answer:
```

### Scoring standard

```md
### Scoring
The MedHELM schema defines the main metric as `medcalc_bench_accuracy`. Official companion docs describe it as exact match for some categories and range-based correctness for others.
### Evaluation Dimensions
- Numeric correctness under the benchmark's category-specific rule.
- Exact string match metrics are also computed in the companion run spec.
### Judge Prompt
Not applicable. This benchmark uses automatic scoring rather than an LLM judge.
```

## 2. MTSamples

MTSamples is a public benchmark used in MedHELM for treatment-plan generation from medical transcription style clinical information. The companion schema places it in clinical decision support and describes it as returning a reasonable treatment plan from patient information. The official run spec uses zero-shot generation and benchmark-specific summarization-style evaluation.

- **Language:** English
- **Clinical Stage:** Treatment planning
- **Source Clinical Document Type:** Medical transcription style patient notes
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 2.1 Task: Treatment Plan Generation

This task is to generate a reasonable treatment plan from patient information.

### Task type
Generation

```md
### Instruction
Given various information about a patient, return a reasonable treatment plan for the patient.
### Input
[Patient information / clinical note]
### Output
[Free-text treatment plan]
```

### Task example

```md
### Example
Official companion synthetic prompt template from `mtsamples_replicate_scenario.py` and `medhelm_run_specs.py`:

Given various information about a patient, return a reasonable treatment plan for the patient.

The official scenario constructs each instance by:
- using the transcribed medical report with any `PLAN` section removed as model input
- extracting `PLAN` as the gold answer when available, otherwise falling back to `SUMMARY`, then `FINDINGS`
- scoring the generated treatment-plan text against that extracted reference section
```

### Scoring standard

```md
### Scoring
The companion run spec computes summarization-style metrics and a benchmark-specific `MTSamplesReplicateMetric`. The schema exposes the main displayed score as `MTSamples Replicate Jury Score`.
### Evaluation Dimensions
- Benchmark-specific generation quality according to the task metric.
- Generic summarization metrics from the companion stack.
### Judge Prompt
The full MTSamples grading prompt is not explicitly provided in the Nature paper or the companion artifacts inspected.
```

## 3. Medec

Medec is a public benchmark for medical error detection and correction in clinical narratives. The companion scenario states that the source dataset contains 3,848 clinical texts across diagnosis, management, treatment, pharmacotherapy, and causal-organism error types, with 2,189 training texts, 734 validation texts, and 925 test texts.

- **Language:** English
- **Clinical Stage:** Planning treatments / clinical note verification
- **Source Clinical Document Type:** Clinical note narratives with sentence IDs
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 3.1 Task: Medical Error Detection and Correction

This task is to determine whether a clinical text is correct or contains one medical error, and if erroneous, identify and correct the offending sentence.

### Task type
Error detection + correction generation

```md
### Instruction
The following is a medical narrative about a patient. The text is either correct or contains one error. The text has a sentence per line. If the text is correct return CORRECT. If the text has a medical error, return the sentence ID of the sentence containing the error, followed by a space, and a corrected version of the sentence.
### Input
[Clinical note with one sentence per line and sentence IDs]
### Output
[Either CORRECT] or [sentence_id + corrected sentence]
```

### Task example

```md
### Example
Official source-benchmark example from the MEDEC test CSV used by `medec_scenario.py`:

Clinical note:
0 A 29-year-old internal medicine resident presents to the emergency department with complaints of fevers, diarrhea, abdominal pain, and skin rash for 2 days.
1 He feels fatigued and has lost his appetite.
2 On further questioning, he says that he returned from his missionary trip to Brazil last week.
3 He is excited as he talks about his trip.
4 Besides a worthy clinical experience, he also enjoyed local outdoor activities, like swimming and rafting.
5 His past medical history is insignificant.
6 The blood pressure is
7 120/70 mm
8 Hg, the pulse is 100/min, and the temperature is 38.3 C (100.9 F).
9 On examination, there is a rash on the legs.
10 Patient's symptoms are suspected to be due to hepatitis A.
11 The rest of the examination is normal.

Gold output:
10 Patient's symptoms are suspected to be due to Schistosoma mansoni.

Task construction from the official scenario:
- `Error Flag = 1`, so the required output is `Error Sentence ID + space + Corrected Sentence`
- if `Error Flag = 0`, the required output would be `CORRECT`
```

### Scoring standard

```md
### Scoring
The companion schema exposes two Medec-specific metrics: medical error flag accuracy and erroneous-sentence accuracy. The run spec also computes basic string-overlap metrics.
### Evaluation Dimensions
- Correctly flag whether an error exists.
- Correctly localize the erroneous sentence.
- Correctly produce the corrected sentence when an error exists.
### Judge Prompt
Not applicable. The benchmark uses automatic task-specific scoring rather than an LLM judge.
```

## 4. HeadQA

HeadQA is a public multiple-choice biomedical reasoning benchmark used by MedHELM for clinical knowledge support. The official scenario describes it as healthcare exam questions originally sourced from Spanish healthcare exams; the MedHELM code evaluates the English text QA subset and uses exact match.

- **Language:** English in the inspected MedHELM run spec; original benchmark also has Spanish source material
- **Clinical Stage:** Clinical knowledge support
- **Source Clinical Document Type:** Biomedical multiple-choice exam questions
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 4.1 Task: Biomedical Multiple-Choice Question Answering

This task is to answer a biomedical multiple-choice question by selecting the correct option.

### Task type
Multiple-choice QA

```md
### Instruction
You are a highly knowledgeable AI assistant specializing in biomedical sciences. Select the correct answer by outputting only the letter corresponding to your choice (A, B, C, or D).
### Input
[Biomedical question with answer choices]
### Output
[Single option letter]
```

### Task example

```md
### Example
Example from the dataset:

Question:
The excitatory postsynaptic potentials:

A) They are all or nothing.
B) They are hyperpolarizing.
C) They can be added.
D) They spread long distances.

Answer:
The answer is C. Explanation: None provided in this dataset.
```

### Scoring standard

```md
### Scoring
Exact match on the selected answer option.
### Evaluation Dimensions
- Multiple-choice answer correctness.
### Judge Prompt
Not applicable.
```

## 5. Medbullets

Medbullets is a public USMLE-style clinical multiple-choice benchmark included by MedHELM as a clinical knowledge support evaluation. The companion scenario downloads the five-option test split and uses exact match.

- **Language:** English
- **Clinical Stage:** Clinical knowledge support
- **Source Clinical Document Type:** USMLE-style clinical question stems with five answer options
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 5.1 Task: USMLE-Style Clinical Multiple-Choice QA

This task is to choose the correct answer for a clinical multiple-choice question.

### Task type
Multiple-choice QA

```md
### Instruction
Select the correct answer by outputting only the letter corresponding to your choice.
### Input
[Clinical question stem with answer choices A-E]
### Output
[Single option letter]
```

### Task example

```md
### Example
Example from the dataset:

Question:
A 42-year-old woman is enrolled in a randomized controlled trial to study cardiac function in the setting of
several different drugs. She is started on verapamil and instructed to exercise at 50% of her VO2 max while
several cardiac parameters are being measured. During this experiment, which of the following represents
the relative conduction speed through the heart from fastest to slowest?

A) AV node > ventricles > atria > Purkinje fibers
B) Purkinje fibers > ventricles > atria > AV node
C) Purkinje fibers > atria > ventricles > AV node
D) Purkinje fibers > AV node > ventricles > atria

Answer:
The answer is C. Explanation: The conduction velocity of the structures of the heart is in the following order:
Purkinje fibers > atria > ventricles > AV node. A calcium channel blocker such as verapamil would only slow
conduction in the AV node.
```

### Scoring standard

```md
### Scoring
Exact match on the selected answer option.
### Evaluation Dimensions
- Multiple-choice answer correctness.
### Judge Prompt
Not applicable.
```

## 6. MedQA

MedQA is explicitly listed as a public MedHELM dataset in the Nature paper's data availability paragraph, but the inspected MedHELM `v0.5.7` schema and run-spec code do not expose a corresponding MedHELM scenario. The benchmark section below therefore records the paper-level benchmark existence and a source-benchmark task description inferred from the cited MedQA literature and repo-local mentions.

- **Language:** English (inferred from the MedQA USMLE benchmark cited by the paper)
- **Clinical Stage:** Clinical knowledge support
- **Source Clinical Document Type:** USMLE-style medical exam questions
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark listed in the Nature paper; task/instruction details inferred because the inspected companion code does not expose a MedHELM run spec for this benchmark

### 6.1 Task: Medical Board-Style Multiple-Choice QA

This task is to answer medical exam-style multiple-choice questions.

### Task type
Multiple-choice QA

```md
### Instruction
Inferred from the cited MedQA benchmark: select the correct answer to the medical question from the provided options.
### Input
[Medical multiple-choice question]
### Output
[Single correct option]
```

### Task example

```md
### Example
Official source-benchmark example from the `med_qa_scenario.py` docstring:

{
  "question": "A 23-year-old pregnant woman at 22 weeks gestation presents with burning upon urination. She states it started 1 day ago and has been worsening despite drinking more water and taking cranberry extract. She otherwise feels well and is followed by a doctor for her pregnancy. Her temperature is 97.7°F (36.5°C), blood pressure is 122/77 mmHg, pulse is 80/min, respirations are 19/min, and oxygen saturation is 98% on room air. Physical exam is notable for an absence of costovertebral angle tenderness and a gravid uterus. Which of the following is the best treatment for this patient?",
  "answer": "Nitrofurantoin",
  "options": {
    "A": "Ampicillin",
    "B": "Ceftriaxone",
    "C": "Ciprofloxacin",
    "D": "Doxycycline",
    "E": "Nitrofurantoin"
  },
  "meta_info": "step2&3",
  "answer_idx": "E"
}

The same official scenario notes that the MedHELM subset uses the 4-option US setting, so this docstring example is a source-benchmark exemplar rather than the exact preprocessed MedHELM row.
```

### Scoring standard

```md
### Scoring
Not explicitly stated in the MedHELM paper. Inference from the source benchmark suggests multiple-choice exact-match accuracy.
### Evaluation Dimensions
- Inferred: answer-option correctness.
### Judge Prompt
Not applicable if evaluated as standard multiple-choice exact match; exact MedHELM implementation details were not exposed in the inspected companion code.
```

## 7. MedMCQA

MedMCQA is explicitly listed as a public MedHELM dataset in the Nature paper and cited in the references, but the inspected MedHELM `v0.5.7` schema and run-spec code do not visibly expose a matching scenario. The details below are therefore benchmark-presence plus source-benchmark inference.

- **Language:** English (inferred from the cited benchmark)
- **Clinical Stage:** Clinical knowledge support
- **Source Clinical Document Type:** Medical multiple-choice exam questions
- **Clinical Specialty:** Multi-subject medical exam benchmark
- **Application Method:** Public benchmark listed in the Nature paper; task/instruction details inferred because no visible MedHELM run spec was found in the inspected companion code

### 7.1 Task: Multi-Subject Medical Multiple-Choice QA

This task is to answer a medical multiple-choice question drawn from a broad set of medical subjects.

### Task type
Multiple-choice QA

```md
### Instruction
Inferred from the source benchmark: select the correct option for the provided medical multiple-choice question.
### Input
[Medical multiple-choice question]
### Output
[Single correct option]
```

### Task example

```md
### Example
Official source-benchmark example from the `med_mcqa_scenario.py` docstring:

Question: In a patient of heart disease antibiotic prophylaxis for dental extraction is:
A. Amoxicillin.
B. Imipenem.
C. Gentamicin.
D. Erythromycin.
Answer: A
```

### Scoring standard

```md
### Scoring
Not explicitly stated in the MedHELM paper. Inference from the source benchmark suggests multiple-choice exact-match accuracy.
### Evaluation Dimensions
- Inferred: answer-option correctness.
### Judge Prompt
Not applicable if evaluated as standard multiple-choice exact match; exact MedHELM implementation details were not exposed in the inspected companion code.
```

## 8. ACI-Bench

ACI-Bench is a public MedHELM benchmark for automatic visit note generation from doctor-patient dialogue. The scenario source describes three official test JSON files plus a train file and frames the task as generating structured notes with four sections.

- **Language:** English
- **Clinical Stage:** Clinical note generation during / after patient visit
- **Source Clinical Document Type:** Doctor-patient dialogue transcripts
- **Clinical Specialty:** General outpatient documentation
- **Application Method:** Reused public benchmark included in MedHELM

### 8.1 Task: Visit Note Generation from Dialogue

This task is to summarize a clinician-patient conversation into a structured clinical note.

### Task type
Generation

```md
### Instruction
Summarize the conversation to generate a clinical note with four sections: 1. HISTORY OF PRESENT ILLNESS 2. PHYSICAL EXAM 3. RESULTS 4. ASSESSMENT AND PLAN.
### Input
[Doctor-patient conversation transcript]
### Output
[Structured clinical note with the four requested sections]
```

### Task example

```md
### Example
Example from the dataset:

Dialogue:
[doctor] hi, brian. how are you?
[patient] hi, good to see you.
[doctor] it's good to see you too. so, i know the nurse told you a little bit about dax.
[patient] mm-hmm.
[doctor] i'd like to tell dax about you, okay?
[patient] sure.

Note:
CHIEF COMPLAINT

Follow-up of chronic problems.

HISTORY OF PRESENT ILLNESS
```

### Scoring standard

```md
### Scoring
The companion schema exposes `ACI-Bench Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and uses a benchmark-specific `ACIBenchMetric`.
### Evaluation Dimensions
- Benchmark-specific generation quality judged by the benchmark metric / annotator.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full ACI-Bench grading prompt is not explicitly provided in the Nature paper or the companion artifacts inspected.
```

## 9. MTSamples Procedures

MTSamples Procedures is a public MedHELM generation benchmark focused on documenting or summarizing procedural cases. The companion schema treats it as a procedure-documentation benchmark and the run spec uses generation plus benchmark-specific summarization-style evaluation.

- **Language:** English
- **Clinical Stage:** Procedure documentation
- **Source Clinical Document Type:** Procedure / operative patient notes
- **Clinical Specialty:** Procedure-heavy documentation, multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 9.1 Task: Procedure Summary or Treatment Plan Generation

This task is to produce a clinically reasonable procedural summary or treatment plan from patient notes.

### Task type
Generation

```md
### Instruction
Here are information about a patient, return a reasonable treatment plan for the patient.
### Input
[Patient notes about a procedure case]
### Output
[Free-text treatment plan or procedural summary]
```

### Task example

```md
### Example
Official source-benchmark exemplar from the procedure file `Abscess Excision.txt` used by `mtsamples_procedures_scenario.py`:

Source report:
PREOPERATIVE DIAGNOSIS:  Recurrent re-infected sebaceous cyst of abdomen.
POSTOPERATIVE DIAGNOSES:
1. Abscess secondary to retained foreign body.
2. Incisional hernia.
PROCEDURES
1. Excision of abscess, removal of foreign body.
2. Repair of incisional hernia.
ANESTHESIA:  LMA.
INDICATIONS:  Patient is a pleasant 37-year-old gentleman who has had multiple procedures including a laparotomy related to trauma. The patient has had a recurrently infected cyst of his mass at the superior aspect of his incision, which he says gets larger and then it drains internally, causing him to be quite ill. He presented to my office and I recommended that he undergo exploration of this area and removal. The procedure, purpose, risks, expected benefits, potential complications, and alternative forms of therapy were discussed with him and he was agreeable to surgery.
FINDINGS: The patient was found upon excision of the cyst that it contained a large Prolene suture, which is multiply knotted as it always is; beneath this was a very small incisional hernia, the hernia cavity, which contained omentum; the hernia was easily repaired.

Gold / extracted reference section:
The patient was found upon excision of the cyst that it contained a large Prolene suture, which is multiply knotted as it always is; beneath this was a very small incisional hernia, the hernia cavity, which contained omentum; the hernia was easily repaired.

Task construction from the official scenario:
- input = raw procedure report with any `PLAN`, `SUMMARY`, and `FINDINGS` sections removed
- gold = the first available section among `PLAN`, `SUMMARY`, or `FINDINGS`; this file uses `FINDINGS`
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MTSamples Procedures Jury Score` as the main displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MTSamplesProceduresMetric`.
### Evaluation Dimensions
- Benchmark-specific open-ended generation quality.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the companion artifacts inspected.
```

## 10. MedicationQA

MedicationQA is a public consumer-medication question answering benchmark used in MedHELM. The scenario source downloads an Excel workbook of question-answer pairs and evaluates zero-shot answer generation.

- **Language:** English
- **Clinical Stage:** Patient education / medication counseling
- **Source Clinical Document Type:** Consumer medication questions
- **Clinical Specialty:** Pharmacotherapy / general medication counseling
- **Application Method:** Reused public benchmark included in MedHELM

### 10.1 Task: Consumer Medication Question Answering

This task is to answer a consumer health question about medications.

### Task type
Generation / QA

```md
### Instruction
Please answer the following consumer health question.
### Input
[Medication-related consumer question]
### Output
[Free-text medically grounded answer]
```

### Task example

```md
### Example
Official source-benchmark example from the `MedInfo2019-QA-Medications.xlsx` workbook used by `medication_qa_scenario.py`:

Question:
how does rivatigmine and otc sleep medicine interact

Gold answer:
tell your doctor and pharmacist what prescription and nonprescription medications, vitamins, nutritional supplements, and herbal products you are taking or plan to take. Be sure to mention any of the following: antihistamines; aspirin and other nonsteroidal anti-inflammatory medications (NSAIDs) such as ibuprofen (Advil, Motrin) and naproxen (Aleve, Naprosyn); bethanechol (Duvoid, Urecholine); ipratropium (Atrovent, in Combivent, DuoNeb); and medications for Alzheimer's disease, glaucoma, irritable bowel disease, motion sickness, ulcers, or urinary problems. Your doctor may need to change the doses of your medications or monitor you carefully for side effects.
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MedicationQA Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MedicationQAMetric`.
### Evaluation Dimensions
- Benchmark-specific open-ended answer quality.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the MedHELM paper or the inspected companion artifacts.
```

## 11. MedDialog

MedDialog is a public dialogue summarization benchmark in MedHELM. The official scenario uses the `healthcaremagic` and `icliniq` English subsets, both evaluated in zero-shot mode on their test splits.

- **Language:** English
- **Clinical Stage:** Patient-provider messaging / conversation summarization
- **Source Clinical Document Type:** Doctor-patient dialogues from `healthcaremagic` and `icliniq`
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 11.1 Task: One-Sentence Medical Dialogue Summarization

This task is to summarize a patient-doctor conversation into one sentence.

### Task type
Generation / summarization

```md
### Instruction
Generate a one sentence summary of this patient-doctor conversation.
### Input
[Doctor-patient conversation]
### Output
[One-sentence summary]
```

### Task example

```md
### Example
The following is an example from the healthcaremagic.com subset:

Patient: I get cramps on top of my left forearm and hand and it causes my hand and fingers to draw up and it
hurts. It mainly does this when I bend my arm. I ve been told that I have a slight pinch in a nerve in my neck.
Could this be a cause? I don t think so. Doctor: Hi there. It may sound difficult to believe it ,but the nerves
which supply your forearms and hand, start at the level of spinal cord and on their way towards the forearm and
hand regions which they supply, the course of these nerves pass through difference fascial and muscular planes
that can make them susceptible to entrapment neuropathies. Its a group of conditions where a nerve gets
compressed between a muscle and a bone, or between the fibers of a muscle that it pierces or passes through.
Also, the compression can happen when the nerves are travelling around a blood vessel which can mechanically put
pressure on them. Usually patients who would be having such a problem present with a dull aching pain over the
arm and forearm. If it is not too severe and does not cause any neurological deficits then conservative management
with Pregabalin and Vitamin B complex tablets, activity modifications and physiotherapy can be started which
will provide relief. Avoid the activities which exaggerate your problem.

Could painful forearms be related to pinched nerve in neck?

The following is an example from the icliniq.com subset:

Patient: Hello doctor,  We are looking for a second opinion on my friend's MRI scan of both the knee joints as he
is experiencing excruciating pain just above the patella. He has a sudden onset of severe pain on both the knee
joints about two weeks ago. Previously he had a similar episode about two to three months ago and it subsided
after resting and painkillers. Doctor: Hi. I viewed the right and left knee MRI images. (attachment removed to
protect patient identity).  Left knee: The MRI, left knee joint shows a complex tear in the posterior horn of the
medial meniscus area and mild left knee joint effusion. There is some fluid between the semimembranous and medial
head of gastrocnemius muscles. There is a small area of focal cartilage defect in the upper pole of the patella
with mild edematous fat. The anterior and posterior cruciate ligaments are normal. The medial and lateral
collateral ligaments are normal. Right knee: The right knee joint shows mild increased signal intensity in the
posterior horn of the medial meniscus area and minimal knee joint effusion. There is minimal fluid in the back
of the lower thigh and not significant. There is a suspicious strain in the left anterior cruciate ligament
interiorly but largely the attachments are normal. The posterior cruciate ligament is normal. There are subtle
changes in the upper pole area of the right patella and mild edema. There is mild edema around the bilateral
distal quadriceps tendons, but there is no obvious tear of the tendons.

My friend has excruciating knee pain. Please interpret his MRI report
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MedDialog Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MedDialogMetric`.
### Evaluation Dimensions
- Benchmark-specific summary quality.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the Nature paper or the inspected companion artifacts.
```

## 12. MEDIQA-QA

MEDIQA-QA is a public benchmark in MedHELM for answering consumer health questions using ranked answer candidates. The official scenario loads the `bigbio/mediqa_qa` test split and uses the highest-ranked answer as the gold response.

- **Language:** English
- **Clinical Stage:** Patient understanding and accessibility in health communication
- **Source Clinical Document Type:** Consumer health questions with answer candidates
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused public benchmark included in MedHELM

### 12.1 Task: Consumer Health Question Answering

This task is to answer a consumer health question with a medically appropriate free-text response.

### Task type
Generation / QA

```md
### Instruction
Answer the following consumer health question.
### Input
[Consumer health question]
### Output
[Free-text answer]
```

### Task example

```md
### Example
Official companion sample prompt from the `medi_qa_scenario.py` docstring:

Answer the following consumer health question.

Question: Noonan syndrome. What are the references with noonan syndrome
and polycystic renal disease?
Answer:

Task construction from the official scenario:
- input = `QuestionText`
- gold/reference answer = the highest-ranked answer in `AnswerList` where `ReferenceRank == 1`
- the docstring sample prints the prompt template and source question, but not the final answer text
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MEDIQA Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MediQAMetric`.
### Evaluation Dimensions
- Benchmark-specific answer quality.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the companion artifacts inspected.
```

## 13. PubMedQA

PubMedQA is a public biomedical research QA benchmark included by MedHELM. The companion scenario uses the labeled `PQA-L` subset and exact-match multiple-choice evaluation.

- **Language:** English
- **Clinical Stage:** Literature research
- **Source Clinical Document Type:** PubMed abstract snippets with yes/no/maybe questions
- **Clinical Specialty:** Biomedical literature
- **Application Method:** Reused public benchmark included in MedHELM

### 13.1 Task: Yes/No/Maybe Question Answering from PubMed Abstracts

This task is to answer a biomedical question using contextualized PubMed abstract snippets.

### Task type
Multiple-choice QA

```md
### Instruction
Answer A for yes, B for no or C for maybe. Do not include any explanation or additional text. Output only the letter on a single line.
### Input
[Structured PubMed abstract context] + [question]
### Output
[A / B / C]
```

### Task example

```md
### Example
The following is an example from the dataset

```
"QUESTION": "Is anorectal endosonography valuable in dyschesia?",
"CONTEXTS": [
    "Dyschesia can be provoked by inappropriate defecation movements. The aim of this prospective study was to
    demonstrate dysfunction of the anal sphincter and/or the musculus (m.) puborectalis in patients with dyschesia
    using anorectal endosonography.",
    "Twenty consecutive patients with a medical history of dyschesia and a control group of 20 healthy subjects
    underwent linear anorectal endosonography (Toshiba models IUV 5060 and PVL-625 RT). In both groups, the
    dimensions of the anal sphincter and the m. puborectalis were measured at rest, and during voluntary squeezing
    and straining. Statistical analysis was performed within and between the two groups.",
    "The anal sphincter became paradoxically shorter and/or thicker during straining (versus the resting state) in
    85% of patients but in only 35% of control subjects. Changes in sphincter length were statistically
    significantly different (p<0.01, chi(2) test) in patients compared with control subjects. The m. puborectalis
    became paradoxically shorter and/or thicker during straining in 80% of patients but in only 30% of controls.
    Both the changes in length and thickness of the m. puborectalis were significantly different (p<0.01, chi(2)
    test) in patients versus control subjects."
],
"LABELS": [
    "AIMS",
    "METHODS",
    "RESULTS"
],
"MESHES": [
    "Adolescent",
    "Adult",
    "Aged",
    "Aged, 80 and over",
    "Anal Canal",
    "Case-Control Studies",
    "Chi-Square Distribution",
    "Constipation",
    "Defecation",
    "Endosonography",
    "Female",
    "Humans",
    "Male",
    "Middle Aged",
    "Pelvic Floor",
    "Rectum"
],
"YEAR": "2002",
"reasoning_required_pred": "yes",
"reasoning_free_pred": "yes",
"final_decision": "yes"
```

The following is the template of how they constructed the prompts

```
Context: <Label>. <context>
<Label>. <context>
<Label>. <context>

Question: <Question>

A) yes
B) no
C) maybe
```

among A through C, the answer is
```

### Scoring standard

```md
### Scoring
Exact match on the three-way answer label.
### Evaluation Dimensions
- Multiple-choice correctness among yes / no / maybe.
### Judge Prompt
Not applicable.
```

## 14. EHRSQL

EHRSQL is a public text-to-SQL benchmark used by MedHELM for clinical research data analysis. The official scenario downloads the `eicu` benchmark files, injects the database schema into the prompt, and evaluates generated SQL with task-specific metrics plus exact match.

- **Language:** English
- **Clinical Stage:** Clinical research data analysis
- **Source Clinical Document Type:** Natural-language clinical research questions plus relational schema
- **Clinical Specialty:** Clinical informatics / multi-specialty research
- **Application Method:** Reused public benchmark included in MedHELM

### 14.1 Task: Clinical Text-to-SQL

This task is to generate a valid SQL query that answers a clinical research question over the provided EHR database schema.

### Task type
Code generation / semantic parsing

```md
### Instruction
You are a highly skilled AI specializing in medical SQL queries. Given a database schema and a medical question, generate a valid SQL query that retrieves the required information. If the question is unanswerable, return an empty string.
### Input
[Database schema] + [natural-language medical question]
### Output
[SQL query ending with ;] or [empty string for unanswerable question]
```

### Task example

```md
### Example
Official source-benchmark example from the `eicu/test.json` file used by `ehr_sql_scenario.py`:

Question:
tell me the method of dextrose 5% in water (d5w) iv : 1000 ml bag intake?

Gold SQL:
select distinct medication.routeadmin from medication where medication.drugname = 'dextrose 5% in water (d5w) iv : 1000 ml bag'

Task construction from the official scenario:
- the model input is `-- Database Schema:` followed by the extracted `CREATE TABLE` schema and then `-- Question:` followed by the natural-language question
- the gold/reference answer is the SQL in the JSON field `query`
- the scenario also records `is_impossible` and `value` metadata for evaluation
```

### Scoring standard

```md
### Scoring
The companion schema exposes execution accuracy as the main metric and also lists answerable-question precision, answerable-question recall, query validity, and exact-match style metrics.
### Evaluation Dimensions
- SQL execution accuracy.
- Query validity.
- Correct handling of answerable vs unanswerable questions.
### Judge Prompt
Not applicable.
```

## 15. RaceBias

RaceBias is a public MedHELM benchmark for detecting harmful race-based content in medical QA responses. The companion scenario converts the source paper's supplementary document into yes/no classification examples.

- **Language:** English
- **Clinical Stage:** Clinical research quality / fairness auditing
- **Source Clinical Document Type:** Medical question-answer pairs with bias labels
- **Clinical Specialty:** Cross-specialty fairness and safety evaluation
- **Application Method:** Reused public benchmark included in MedHELM

### 15.1 Task: Detect Race-Based Harmful Content

This task is to determine whether a question-answer pair contains harmful, inaccurate, or race-based content.

### Task type
Binary classification

```md
### Instruction
For the following question-answer pair, respond A for yes if the answer involves harmful, inaccurate, and/or race-based content and respond B for no otherwise.
### Input
[Question] + [model response]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `race_based_med_scenario.py`, which converts the source benchmark paper's supplementary DOCX into MedHELM instances:

For the following question-answer pair, respond 'A' for yes if the answer involves harmful, innacurate,and/or race-based content and respond 'B' for no otherwise.

Question: {question}
Response: {response}

Task construction from the official scenario:
- `question` is extracted from the supplementary DOCX run header
- `response` is the associated answer text collected from the same supplementary file
- red-highlighted text in the DOCX is mapped to the gold label `yes`; non-highlighted text is mapped to `no`
```

### Scoring standard

```md
### Scoring
Exact match on the binary yes/no label.
### Evaluation Dimensions
- Correct detection of harmful or race-based content.
### Judge Prompt
Not applicable.
```

## 16. MedHallu

MedHallu is a public MedHELM benchmark for hallucination detection in biomedical answers. The official scenario constructs paired factual and hallucinated instances from the `UTAustin-AIHealth/MedHallu` dataset and labels them with `0` or `1`.

- **Language:** English
- **Clinical Stage:** Clinical research quality / factuality evaluation
- **Source Clinical Document Type:** PubMed-derived knowledge snippet, question, and answer
- **Clinical Specialty:** Biomedical QA factuality
- **Application Method:** Reused public benchmark included in MedHELM

### 16.1 Task: Detect Hallucinated Medical Answers

This task is to judge whether a provided answer contains non-factual or hallucinated information.

### Task type
Binary factuality classification

```md
### Instruction
Given a question and an answer, determine whether the answer contains non-factual or hallucinated information. Return 0 if the answer is factual and 1 if the answer is hallucinated.
### Input
[World knowledge snippet] + [question] + [answer]
### Output
[0 or 1]
```

### Task example

```md
### Example
Official companion prompt template from `medhallu_scenario.py`:

World Knowledge: {knowledge}

Question: {question}

Answer: {answer}

Task construction from the official scenario:
- for each dataset row, the `Ground Truth` answer is emitted as one instance with gold label `0`
- the `Hallucinated Answer` field from the same row is emitted as a second instance with gold label `1`
- the model must output only `0` or `1`
```

### Scoring standard

```md
### Scoring
Exact match between the model's `0/1` judgment and the gold factuality label.
### Evaluation Dimensions
- Hallucination detection correctness.
### Judge Prompt
Not applicable as a separate external judge prompt. The task instruction itself is the factuality-judgment prompt.
```

## 17. EHRSHOT

EHRSHOT is a gated benchmark in MedHELM for future-event prediction from structured EHR histories serialized into long textual inputs. The Nature paper lists EHRSHOT as gated via PhysioNet; the companion gated run config visibly includes at least `guo_readmission`, `new_hypertension`, and `lab_anemia` subject settings, and the scenario source documents a larger underlying task set.

- **Language:** English
- **Clinical Stage:** Predicting patient risks and outcomes
- **Source Clinical Document Type:** Structured EHR code sequences serialized into text
- **Clinical Specialty:** Multi-specialty longitudinal EHR prediction
- **Application Method:** Reused gated benchmark included in MedHELM

### 17.1 Task: Future Clinical Event Prediction from Longitudinal EHR

This task is to predict whether a future diagnosis, abnormal lab result, or hospital event will occur based on the patient's historical EHR record.

### Task type
Binary classification

```md
### Instruction
Answer A for yes, B for no.
### Input
[Longitudinal EHR history serialized into text] + [binary prediction question]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template reconstructed directly from `ehrshot_scenario.py`:

# Instructions
You are an expert {role} at Stanford Healthcare, an academic medical center affiliated with Stanford University. You specialize in predicting {task_full_name}.

Clinical Definition: {clinical_definition}

Medical Code Definition: In an electronic health record (EHR), {task_full_name} is denoted by the occurrence of any of the following medical codes: {code_def}

Instruction: Review the patient's EHR history. Based on all available medical evidence in the provided EHR, please answer the question: {question}

# Your Task
Patient EHR:
{ehr}

Official task questions published in the same scenario include:
- If this patient is discharged from the hospital right now, is the patient likely to be readmitted to the hospital within 30 days?
- Is this patient likely to receive a first-time diagnosis of Hypertension within the next year?
- If a lab test for Anemia is ordered for this patient right now, will it come back back abnormal? (i.e. <120 g/L)

Gold label construction from the official scenario:
- each row's `boolean_value` becomes `yes` or `no`
- MedHELM presents those as `A` / `B` at inference time
```

### Scoring standard

```md
### Scoring
Exact match on the binary answer label.
### Evaluation Dimensions
- Correct yes/no prediction for the benchmark's subject-specific task.
### Judge Prompt
Not applicable.
```

## 18. MedAlign

MedAlign is a gated MedHELM benchmark for clinician-generated instruction following over longitudinal EHR. The official scenario uses clinician prompts and clinician responses as references, while the official run spec uses zero-shot generation with a blank adapter instruction because the benchmark prompt itself already contains the instruction.

- **Language:** English
- **Clinical Stage:** Clinical knowledge support over longitudinal EHR
- **Source Clinical Document Type:** Longitudinal EHR event stream plus clinician-authored instruction
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Reused gated benchmark included in MedHELM

### 18.1 Task: Clinician Instruction Following over Longitudinal EHR

This task is to produce the clinician-requested output for a given patient record and prompt.

### Task type
Generation

```md
### Instruction
No extra wrapper instruction is added in the official MedHELM run spec; the benchmark prompt itself carries the task instruction.
### Input
[Clinician-authored prompt grounded in a longitudinal EHR record]
### Output
[Clinician response / requested generated text]
```

### Task example

```md
### Example
Source-benchmark examples reused from the MedAlign paper and appendix because the MedHELM paper reuses the benchmark but does not print a worked instance:

Standard generation prompt from MedAlign Appendix Figure S9:
Instruction: Answer the following question based on the EHR:
###
Question: """{Question}"""
EHR: """{EHR}"""

Synthetic benchmark-style example from MedAlign Appendix Figure S4:
Instruction: Summarize from the EHR the strokes that the patient had and their associated neurologic deficits.
Answer: The patient had strokes in the L basal ganglia in 2018 and multiple strokes in 2022: R occipital, left temporal, L frontal. The patient had right sided weakness associated with the 2018 stroke after which she was admitted to rehab. She then had a left sided hemianopsia related to the 2022 stroke.

Concrete benchmark sample with gold references from MedAlign Appendix Table S3:
Instruction: Has she ever been on a statin before?
Gold standard reference answer 1: Yes, she has been on a statin before but she had side effects of myositis and GI issues. Had GI upset with simvastatin, nausea with crestor, vomiting wtih pravastatin, fluvastatin cannot tolerate
Gold standard reference answer 2: Patient on pravastatin and simvastatin, but these were stopped due to muscle pain and because they were ineffective.
Gold standard reference answer 3: Yes, this patient has been on pravastatin and simvastatin before.

Task construction from the official MedHELM scenario:
- model input = the benchmark field `prompt`
- gold/reference answer = the benchmark field `clinician_response`
- the MedHELM run spec adds no extra wrapper instruction because the benchmark prompt itself already contains the task instruction
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MedAlign Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MedalignMetric`.
### Evaluation Dimensions
- Benchmark-specific instruction-following / response-quality metric.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the Nature paper or the companion artifacts inspected.
```

## 19. DischargeMe

DischargeMe is a gated MedHELM benchmark for discharge-document generation from MIMIC-IV data. The scenario source states that MedHELM uses the phase I test set with 14,702 hospital admission instances and constructs two generation tasks per admission: brief hospital course and discharge instructions.

- **Language:** English
- **Clinical Stage:** Hospital discharge
- **Source Clinical Document Type:** Discharge text plus radiology report text
- **Clinical Specialty:** Inpatient care
- **Application Method:** Reused gated benchmark included in MedHELM

### 19.1 Task: Brief Hospital Course Generation

This task is to generate the brief hospital course from discharge text and radiology report context.

### Task type
Generation

```md
### Instruction
Given a discharge text, a radiology report text, and a target document of either discharge instructions or a brief hospital course, return the generated target document from the context provided.
### Input
[Discharge text] + [radiology report text]
### Output
[Brief hospital course]
```

### Task example

```md
### Example
Sample Synthetic Prompt:
    Generate the {TASK} from the following patient discharge text and radiology report text.

    Discharge Text:
    Name: {Patient Name} Unit No: {Unit Number} Date of Birth: {DOB} Date of Admission:
    {DOA} Date of Discharge: {DOD}
    Chief Complaint: {Chief Complaint} History of Present Illness: {HPI} Past Medical History: {PMH}
    Medications on Admission: {Medications} Allergies: {Allergies} Physical Exam: {Physical Exam}
    Discharge Diagnosis: {Discharge Diagnosis}

    Radiology Report:
    {Radiology Report}

    {TASK}:
```

### Scoring standard

```md
### Scoring
The companion schema exposes `DischargeMe Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `DischargeMeMetric`.
### Evaluation Dimensions
- Benchmark-specific document quality.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the inspected companion artifacts.
```

### 19.2 Task: Discharge Instructions Generation

This task is to generate patient-facing discharge instructions from discharge text and radiology report context.

### Task type
Generation

```md
### Instruction
Given a discharge text, a radiology report text, and a target document of either discharge instructions or a brief hospital course, return the generated target document from the context provided.
### Input
[Discharge text] + [radiology report text]
### Output
[Discharge instructions]
```

### Task example

```md
### Example
Sample Synthetic Prompt:
    Generate the {TASK} from the following patient discharge text and radiology report text.

    Discharge Text:
    Name: {Patient Name} Unit No: {Unit Number} Date of Birth: {DOB} Date of Admission:
    {DOA} Date of Discharge: {DOD}
    Chief Complaint: {Chief Complaint} History of Present Illness: {HPI} Past Medical History: {PMH}
    Medications on Admission: {Medications} Allergies: {Allergies} Physical Exam: {Physical Exam}
    Discharge Diagnosis: {Discharge Diagnosis}

    Radiology Report:
    {Radiology Report}

    {TASK}:
```

### Scoring standard

```md
### Scoring
Same benchmark-level scoring setup as above: benchmark-specific DischargeMe metric plus summarization metrics.
### Evaluation Dimensions
- Patient-facing instruction quality and benchmark-specific correctness.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the inspected companion artifacts.
```

## 20. MIMIC-RRS

MIMIC-RRS is a gated MedHELM benchmark for radiology report summarization. The official scenario describes it as using MIMIC-III radiology reports and states that the dataset contains 73,259 reports.

- **Language:** English
- **Clinical Stage:** Diagnostic report documentation
- **Source Clinical Document Type:** Radiology report `Findings` and `Impression` sections
- **Clinical Specialty:** Radiology
- **Application Method:** Reused gated benchmark included in MedHELM

### 20.1 Task: Impression Generation from Findings

This task is to generate the impression section of a radiology report from the findings section.

### Task type
Generation / summarization

```md
### Instruction
Generate the impression section of the radiology report based on its findings. Be as concise as possible.
### Input
[Findings section]
### Output
[Impression section]
```

### Task example

```md
### Example
Sample Synthetic Prompt:
    Generate the impressions of a radiology report based on its findings.

    Findings:
    The heart is normal in size. The lungs are clear.

    Impressions:
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MIMIC-RRS Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MIMICRRSMetric`.
### Evaluation Dimensions
- Radiology impression quality.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the inspected companion artifacts.
```

## 21. MIMIC-BHC

MIMIC-BHC is a gated MedHELM benchmark for summarizing full clinical notes into the brief hospital course section. The official scenario states that the underlying dataset contains 270,033 clinical notes and uses the test split in zero-shot mode.

- **Language:** English
- **Clinical Stage:** Hospital discharge summarization
- **Source Clinical Document Type:** Discharge notes
- **Clinical Specialty:** Inpatient care
- **Application Method:** Reused gated benchmark included in MedHELM

### 21.1 Task: Brief Hospital Course Summarization

This task is to summarize a clinical note into a brief hospital course.

### Task type
Generation / summarization

```md
### Instruction
Summarize the clinical note into a brief hospital course.
### Input
[Clinical note]
### Output
[Brief hospital course]
```

### Task example

```md
### Example
Sample Synthetic Prompt:
    Summarize the clinical note into a brief hospital course.

    Clinical Note:
    <SEX> M <SERVICE> SURGERY <ALLERGIES> No Known Allergies \/ Adverse Drug Reactions
    ...
    continue to follow-up with your health care providers as an outpatient.

    Brief Hospital Course:
    Mr. ___ was pre-admitted on ___ for liver transplantation
    ...
    discharged home to continue home medications and follow-up as an outpatient.
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MIMIC-BHC Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MIMICBHCMetric`.
### Evaluation Dimensions
- Brief hospital course summary quality.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the inspected companion artifacts.
```

## 22. N2C2-CT

N2C2-CT Matching is a gated MedHELM benchmark for clinical-trial cohort matching. The scenario source states that the source dataset contains 288 patients with 202 train and 86 test patients, and that MedHELM uses a yes/no trial-criterion classification formulation.

- **Language:** English
- **Clinical Stage:** Research enrollment / pre-trial screening
- **Source Clinical Document Type:** Deidentified clinical notes plus trial eligibility criterion
- **Clinical Specialty:** Clinical research recruitment
- **Application Method:** Reused gated benchmark included in MedHELM

### 22.1 Task: Clinical Trial Eligibility Matching

This task is to determine whether a patient meets a specified eligibility criterion for a clinical trial.

### Task type
Binary classification

```md
### Instruction
Answer A for yes, B for no.
### Input
[Clinical notes] + [eligibility criterion / matching question]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `n2c2_ct_matching_scenario.py`:

# Task
Your job is to decide whether the given patient meets the inclusion criterion for a clinical trial.

# Inclusion Criterion
The inclusion criterion being assessed is: "{subject}".
The definition of the inclusion criterion is: "{LONG_DEFINITIONS[self.subject]}".

# Patient Clinical Notes
Below is a set of {len(patient['ehr'])} clinical notes describing the patient's current health status. Each note is separated by a header with the date that the note was written, as well as a long list of asterisks.

{notes}

# Current Date
Assume that the current date is: {current_date}

# Question
Does the patient meet the inclusion criterion "{self.subject}"?

The same official scenario publishes explicit criterion definitions including:
- `ABDOMINAL`: `History of intra-abdominal surgery, small or large intestine resection, or small bowel obstruction`
- `ADVANCED-CAD`: `Advanced cardiovascular disease (CAD). For the purposes of this annotation, we define “advanced” as having 2 or more of the following: • Taking 2 or more medications to treat CAD • History of myocardial infarction (MI) • Currently experiencing angina • Ischemia, past or present`
- `CREATININE`: `Serum creatinine level above the upper normal limit`
```

### Scoring standard

```md
### Scoring
Exact match on the yes/no answer label.
### Evaluation Dimensions
- Correct patient-criterion match classification.
### Judge Prompt
Not applicable.
```

## 23. MIMIC-IV Billing Code

MIMIC-IV Billing Code is a gated MedHELM benchmark for ICD-10 coding from discharge notes. The companion scenario loads preprocessed MIMIC-IV discharge-summary text with ICD-10 targets and the schema exposes precision, recall, and F1 as the key metrics.

- **Language:** English
- **Clinical Stage:** Billing / coding near or after discharge
- **Source Clinical Document Type:** Discharge summaries
- **Clinical Specialty:** Medical coding / administration
- **Application Method:** Reused gated benchmark included in MedHELM

### 23.1 Task: ICD-10 Code Extraction from Clinical Note

This task is to identify all relevant ICD-10 codes from a clinical note.

### Task type
Multi-label generation / coding

```md
### Instruction
Given the following clinical note, identify all relevant ICD-10 codes.
### Input
[Clinical note]
### Output
[Comma-separated ICD-10 code list]
```

### Task example

```md
### Example
Official companion prompt template from `mimiciv_billing_code_scenario.py` and `medhelm_run_specs.py`:

Given the following clinical note, identify all relevant ICD-10 codes.

Task construction from the official scenario:
- input = the discharge-note text in column `text`
- gold/reference answer = the list in column `target`, converted to a comma-separated ICD-10 string
- scoring uses ICD-10 precision, recall, and F1 over that gold code set
```

### Scoring standard

```md
### Scoring
The companion schema exposes precision, recall, and F1 for predicted ICD-10 codes, with F1 as the main displayed score.
### Evaluation Dimensions
- ICD-10 code precision.
- ICD-10 code recall.
- ICD-10 code F1.
### Judge Prompt
Not applicable.
```

## 24. CLEAR

CLEAR is a private MedHELM benchmark for classifying whether a note supports a history of a target condition. The inspected companion code exposes condition-specific prompting and a three-way label space (`has history`, `does not have history`, `uncertain`), but the Nature paper is the benchmark-existence anchor.

- **Language:** English
- **Clinical Stage:** Supporting diagnostic decisions / history extraction
- **Source Clinical Document Type:** Clinical notes
- **Clinical Specialty:** Mixed condition-specific history classification
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 24.1 Task: Condition History Classification

This task is to decide whether a patient has a history of a target condition, does not have such a history, or the note is uncertain.

### Task type
Three-way classification

```md
### Instruction
Answer A for "Has a history of <condition>", B for "Does not have a history of <condition>", or C for "Uncertain".
### Input
[Clinical note] + [target condition]
### Output
[A / B / C]
```

### Task example

```md
### Example
Sample Synthetic Prompt:
    You are a helpful medical assistant. Determine whether the patient has a history of <medical condition>.

    Text: [insert text here]

    A. Has a history of alcohol dependence
    B. Does not have a history of alcohol dependence
    C. Uncertain

    Answer:
```

### Scoring standard

```md
### Scoring
Exact match on the three-way label.
### Evaluation Dimensions
- Correct affirmative / negative / uncertain classification for the target condition.
### Judge Prompt
Not applicable.
```

## 25. ADHD-Behavior

ADHD-Behavior is a private MedHELM benchmark for detecting whether pediatric ADHD notes recommend parent training in behavior management. The companion scenario builds prompts from `prompt`, `context`, and binary `label` fields.

- **Language:** English
- **Clinical Stage:** Treatment planning for pediatric ADHD
- **Source Clinical Document Type:** Pediatric primary-care visit notes
- **Clinical Specialty:** Pediatrics / ADHD care
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 25.1 Task: Detect Parent Training in Behavior Management Recommendation

This task is to classify whether a clinical note documents a recommendation for parent training in behavior management.

### Task type
Binary classification

```md
### Instruction
Answer A for yes or B for no.
### Input
[Question about PTBM recommendation] + [clinical note context]
### Output
[A / B]
```

### Task example

```md
### Example
No concrete task example is provided in the MedHELM paper. The companion scenario exposes the prompt template but not a paper-worked instance.
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct detection of PTBM recommendation.
### Judge Prompt
Not applicable.
```

## 26. ADHD-MedEffects

ADHD-MedEffects is a private MedHELM benchmark for detecting medication side-effect inquiry in pediatric ADHD documentation. The companion scenario includes a more explicit in-prompt definition of side effects inquiry versus no side effects inquiry.

- **Language:** English
- **Clinical Stage:** Treatment monitoring
- **Source Clinical Document Type:** Pediatric ADHD visit notes
- **Clinical Specialty:** Pediatrics / ADHD care
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 26.1 Task: Detect Side Effects Inquiry

This task is to classify whether the note documents actual medication side-effect monitoring.

### Task type
Binary classification

```md
### Instruction
Answer A for yes or B for no after applying the benchmark's explicit SEI vs NSEI definition.
### Input
[Question] + [clinical note context] + [inline definition of side effects inquiry]
### Output
[A / B]
```

### Task example

```md
### Example
No concrete task example is provided in the MedHELM paper. The companion scenario provides the full definitional prompt template.
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct detection of actual side-effect monitoring.
### Judge Prompt
Not applicable.
```

## 27. NoteExtract

NoteExtract is a private MedHELM benchmark for extracting a structured care-plan style format from free-form health worker notes. The companion scenario publishes the prompt template explicitly and emphasizes no hallucination or inference.

- **Language:** English
- **Clinical Stage:** Care-plan documentation
- **Source Clinical Document Type:** Free-form care plan / health worker notes
- **Clinical Specialty:** General care planning
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 27.1 Task: Structured Extraction from Care Plan Note

This task is to convert a free-form clinical note into a predefined structured output format.

### Task type
Structured extraction / generation

```md
### Instruction
Extract the required information precisely as presented in the source text. If the text does not contain specific information, clearly state "Not mentioned". Do not hallucinate or infer details that are not explicitly stated.
### Input
[Clinical note]
### Output
[Structured template including Chief Complaint and HPI fields]
```

### Task example

```md
### Example
The official companion scenario publishes the exact structured template but not a concrete worked MedHELM paper example.
```

### Scoring standard

```md
### Scoring
The companion schema exposes `NoteExtract Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `CHWCarePlanMetric`.
### Evaluation Dimensions
- Faithful extraction without hallucination.
- Output-format adherence.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the MedHELM paper or the inspected companion artifacts.
```

## 28. PatientInstruct

PatientInstruct is a private MedHELM benchmark for generating personalized post-procedure instructions. The companion scenario requires diagnosis, procedure, history and physical note, operative note, and target instruction text, and filters to `QC == TRUE`.

- **Language:** English
- **Clinical Stage:** Post-procedure patient communication
- **Source Clinical Document Type:** Diagnosis, H&P note, operative report, and post-procedure instructions
- **Clinical Specialty:** Procedure and surgery aftercare
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 28.1 Task: Post-Procedure Patient Instruction Generation

This task is to generate clear, actionable post-procedure instructions for a patient from case details.

### Task type
Generation

```md
### Instruction
Generate personalized post-procedure patient instructions from diagnosis, planned procedure, history and physical note, and operative report.
### Input
[Diagnosis] + [procedure] + [history and physical note] + [operative report]
### Output
[Patient instructions]
```

### Task example

```md
### Example
Sample Synthetic Prompt:
    Given the following case details, generate personalized after-surgery care instructions.

    Diagnosis: [diagnosis text]
    Procedure: [actual procedure text]
    History & Physical: [H&P note text]
    Operative Report: [operative note text]

    Patient Instructions:
```

### Scoring standard

```md
### Scoring
The companion schema exposes `PatientInstruct Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics, a benchmark-specific `StarrPatientInstructionsMetric`, and some basic metrics.
### Evaluation Dimensions
- Patient-instruction quality.
- Benchmark-specific task metric and generic summarization metrics.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the inspected companion artifacts.
```

## 29. MedConfInfo

MedConfInfo is a private MedHELM benchmark for identifying confidential content in adolescent notes. The benchmark is linked in the paper to the cited JAMA Pediatrics study on confidential content detection.

- **Language:** English
- **Clinical Stage:** Patient communication governance / confidentiality review
- **Source Clinical Document Type:** Adolescent encounter notes
- **Clinical Specialty:** Pediatrics / adolescent medicine
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 29.1 Task: Confidential Content Detection

This task is to determine whether a note contains confidential content that should be restricted from parental access.

### Task type
Binary classification

```md
### Instruction
Answer A or B for the confidentiality question posed over the provided note context.
### Input
[Question] + [clinical note context]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `shc_conf_scenario.py`:

Provide an answer to the following question: {question} with the following context: {context} , Answer the question with a 'A' for yes or 'B' for no. Do not provide any additional details or response, just a simple A or B response.

Task construction from the official scenario:
- `question` comes from the CSV column `prompt`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label` and is either `A` or `B`
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct detection of confidential content.
### Judge Prompt
Not applicable.
```

## 30. MentalHealth

MentalHealth is a private MedHELM benchmark for generating empathetic counselor responses. The companion scenario states that the dataset includes 7 complete dialogues and evaluates next-response generation from prior conversation context.

- **Language:** English
- **Clinical Stage:** Patient engagement and support
- **Source Clinical Document Type:** Counseling dialogue history
- **Clinical Specialty:** Mental health counseling
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 30.1 Task: Next Counselor Response Generation

This task is to generate an empathetic and appropriate counselor response given the conversation history.

### Task type
Generation

```md
### Instruction
Given a mental health conversation history, generate an empathetic and appropriate counselor response.
### Input
[Topic metadata] + [dialogue type] + [previous conversation]
### Output
[Counselor response]
```

### Task example

```md
### Example
Example dialogue structure:
```
counselor: Hi there, to start can you tell me your name and a little bit about what's been going on?
client: I sleep too much... I'm 23, female and work as IT professional. I feel like I'm not fitting in...
counselor: I can see you have been facing challenges with feeling like you don't fit in...
```
```

### Scoring standard

```md
### Scoring
The companion schema exposes `MentalHealth Jury Score` as the displayed benchmark score. The run spec also computes summarization metrics and a benchmark-specific `MentalHealthMetric`.
### Evaluation Dimensions
- Empathy and appropriateness of the next counselor response.
- Generic summarization metrics from the companion implementation.
### Judge Prompt
The full grading prompt is not explicitly provided in the paper or the inspected companion artifacts.
```

## 31. PrivacyDetection

PrivacyDetection is a private MedHELM benchmark for detecting whether generated or submitted portal messages leak confidential information.

- **Language:** English
- **Clinical Stage:** Patient-provider messaging governance
- **Source Clinical Document Type:** Patient or caregiver portal messages
- **Clinical Specialty:** General patient communication / privacy auditing
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 31.1 Task: Privacy Leak Detection

This task is to determine whether a portal message contains confidential information that should be protected.

### Task type
Binary classification

```md
### Instruction
You are reviewing clinical messages in order to determine if any confidential information was included. Answer A for yes or B for no.
### Input
[Question] + [message context]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `shc_privacy_scenario.py`:

You are reviewing clinical messages in order to determine if any confidential information was included. Please answer the following question: {question} with the following context: {context} , Answer the question with a 'A' for yes or 'B' for no. Do not provide any additional details or response, just a simple A or B response.

Task construction from the official scenario:
- `question` comes from the CSV column `prompt`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label` and is either `A` or `B`
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct privacy-leak classification.
### Judge Prompt
Not applicable.
```

## 32. ProxySender

ProxySender is a private MedHELM benchmark for determining whether a patient portal message was sent by the patient or by a proxy user.

- **Language:** English
- **Clinical Stage:** Patient-provider messaging workflow
- **Source Clinical Document Type:** Patient portal messages
- **Clinical Specialty:** General patient communication
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 32.1 Task: Proxy Message Sender Detection

This task is to classify whether a message was sent by a proxy user. The official companion implementation is internally inconsistent about whether the label space is binary or ternary.

### Task type
Classification with companion-code label-set discrepancy

```md
### Instruction
The scenario prompt string asks for `A` / `B`, but the same companion implementation sets `POSSIBLE_ANSWER_CHOICES = ["A", "B", "C"]` and the MedHELM run spec says `Answer A, B, or C.`
### Input
[Question] + [message context]
### Output
[A / B in the inline prompt string; A / B / C in the scenario/run-spec label space]
```

### Task example

```md
### Example
Official companion prompt template from `shc_proxy_scenario.py`:

You are reviewing a clinical messages in order to determine if they have been sent by a proxy user. Please determine the following: {question} with the following context: {context} , Answer the question with a 'A' for yes or 'B' for no. Do not provide any additional details or response, just a simple A or B response.

Companion-code discrepancy:
- `shc_proxy_scenario.py` sets `POSSIBLE_ANSWER_CHOICES = ["A", "B", "C"]`
- `medhelm_run_specs.py` sets the wrapper instruction to `Answer A, B, or C.`
- the inline scenario prompt text itself only explains `A` / `B`

Task construction from the official scenario:
- `question` comes from the CSV column `prompt`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label`
```

### Scoring standard

```md
### Scoring
Exact match on the companion implementation's stored label, with an explicit caveat that the inspected scenario and run spec disagree on whether the available label space is binary or ternary.
### Evaluation Dimensions
- Correct proxy-sender classification.
### Judge Prompt
Not applicable.
```

## 33. BMT-Status

BMT-Status is a private MedHELM benchmark for answering binary transplant-status questions from clinical notes.

- **Language:** English
- **Clinical Stage:** Clinical research or status verification
- **Source Clinical Document Type:** Clinical notes with associated transplant-status question
- **Clinical Specialty:** Hematology / transplant follow-up
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 33.1 Task: Bone Marrow Transplant Status Verification

This task is to determine whether the patient received a subsequent transplant based on the provided notes.

### Task type
Binary classification

```md
### Instruction
Answer A or B for the transplant-status question posed over the provided context.
### Input
[Question] + [clinical note context]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `shc_bmt_scenario.py`:

Provide an answer to the following question: {question} with the following context: {context} , Answer the question with a 'A' for yes or 'B' for no. Do not provide any additional details or response, just a simple A or B response.

Task construction from the official scenario:
- `question` comes from the CSV column `prompt`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label` and is either `A` or `B`
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct transplant-status classification.
### Judge Prompt
Not applicable.
```

## 34. HospiceReferral

HospiceReferral is a private MedHELM benchmark for hospice referral decisions from palliative-care notes.

- **Language:** English
- **Clinical Stage:** End-of-life care coordination
- **Source Clinical Document Type:** Palliative care clinical notes
- **Clinical Specialty:** Palliative care / hospice referral
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 34.1 Task: Hospice Referral Eligibility Classification

This task is to determine whether the patient is eligible for hospice referral based on the note context.

### Task type
Binary classification

```md
### Instruction
Answer A or B for the hospice referral question posed over the provided note context.
### Input
[Question] + [palliative care note context]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `shc_gip_scenario.py`:

Provide an answer to the following question: {question} with the following context: {context} , Answer the question with a 'A' for yes or 'B' for no. Do not provide any additional details or response, just a simple A or B response.

Task construction from the official scenario:
- `question` comes from the CSV column `prompt`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label` and is either `A` or `B`
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct hospice referral classification.
### Judge Prompt
Not applicable.
```

## 35. ClinicReferral

ClinicReferral is a private MedHELM benchmark for Sequoia clinic referral appropriateness based on palliative care notes.

- **Language:** English
- **Clinical Stage:** Care coordination and planning
- **Source Clinical Document Type:** Palliative care notes with referral question
- **Clinical Specialty:** Palliative care / clinic referral workflow
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 35.1 Task: Sequoia Clinic Referral Classification

This task is to determine whether a patient should be referred to the Sequoia Clinic.

### Task type
Binary classification

```md
### Instruction
Answer A or B for the referral question posed over the provided context.
### Input
[Referral question] + [note context]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `shc_sequoia_scenario.py`:

 {counter} Provide an answer to the following question: {question} with the following context: {context} , Answer the question with a 'A' for yes or 'B' for no. Do not provide any additional details or response, just a simple A or B response.

Task construction from the official scenario:
- `question` comes from the CSV column `question`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label` and is either `A` or `B`
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct clinic referral classification.
### Judge Prompt
Not applicable.
```

## 36. CDI-QA

CDI-QA is a private MedHELM benchmark for verifying clinical conditions from Clinical Documentation Integrity notes.

- **Language:** English
- **Clinical Stage:** Administration / documentation integrity verification
- **Source Clinical Document Type:** Clinical Documentation Integrity notes
- **Clinical Specialty:** Documentation integrity / coding support
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 36.1 Task: Clinical Documentation Integrity Verification QA

This task is to answer yes/no verification questions using CDI note context.

### Task type
Binary classification

```md
### Instruction
Answer the question with either A for yes or B for no.
### Input
[Verification question] + [CDI note context]
### Output
[A / B]
```

### Task example

```md
### Example
Official companion prompt template from `shc_cdi_scenario.py`:

Provide an answer to the following question: {question} with the following context: {context} , Answer the question with either 'A' for yes or 'B' for no. Do not provide any additional details or response, just a simple A or B response.

Task construction from the official scenario:
- `question` comes from the CSV column `prompt`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label` and is either `A` or `B`
```

### Scoring standard

```md
### Scoring
Exact match on the binary label.
### Evaluation Dimensions
- Correct verification answer.
### Judge Prompt
Not applicable.
```

## 37. ENT-Referral

ENT-Referral is a private MedHELM benchmark for deciding whether a note supports referral to an ENT specialist. The companion scenario uses a three-way label space: yes, no, or no mention.

- **Language:** English
- **Clinical Stage:** Referral workflow
- **Source Clinical Document Type:** Clinical notes
- **Clinical Specialty:** Otolaryngology referral triage
- **Application Method:** Private benchmark listed in the Nature paper and exposed in companion code

### 37.1 Task: ENT Referral Classification

This task is to classify whether the note supports referral to an ENT specialist, does not support referral, or makes no mention.

### Task type
Three-way classification

```md
### Instruction
Answer A for yes, B for no, or C for no mention.
### Input
[Referral question] + [clinical note context]
### Output
[A / B / C]
```

### Task example

```md
### Example
Official companion prompt template from `shc_ent_scenario.py`:

{counter} Provide an answer to the following question: {question} with the following context: {context} , Answer the question with either 'A' for yes, 'B' for no, or 'C' for no mention. Do not provide any additional details or response, just a simple A, B, or C response.

Task construction from the official scenario:
- `question` comes from the CSV column `prompt`
- `context` comes from the CSV column `context`
- gold/reference answer comes from the CSV column `label`
- rows with empty labels are skipped by the official scenario implementation
```

### Scoring standard

```md
### Scoring
Exact match on the three-way label.
### Evaluation Dimensions
- Correct yes / no / no-mention classification.
### Judge Prompt
Not applicable.
```

## Coverage and Gaps

- Dataset-level benchmark sections in this summary: 37
- Task sections in this summary: 38
- Benchmarks whose MedHELM implementation details are grounded in inspected companion code: 35
- Benchmarks retained from the Nature paper inventory but not visibly exposed in the inspected MedHELM `v0.5.7` companion code: 2 (`MedQA`, `MedMCQA`)
- Benchmarks with explicit benchmark-specific example prompts or schematic examples in inspected companion scenario files: `ACI-Bench`, `HeadQA`, `Medbullets`, `DischargeMe`, `MIMIC-RRS`, `MIMIC-BHC`, `PubMedQA`, `MentalHealth`, `PatientInstruct`
- Benchmarks where the full grading / jury prompt remains unavailable in the inspected sources despite benchmark-specific annotators or jury scores: most open-ended generation benchmarks, including `MTSamples`, `ACI-Bench`, `MedAlign`, `DischargeMe`, `MIMIC-RRS`, `MIMIC-BHC`, `NoteExtract`, `MedicationQA`, `PatientInstruct`, `MedDialog`, `MEDIQA-QA`, and `MentalHealth`
