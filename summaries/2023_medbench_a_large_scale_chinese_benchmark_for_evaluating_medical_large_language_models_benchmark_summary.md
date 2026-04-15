<!-- paper_key: "2023_medbench_a_large_scale_chinese_benchmark_for_evaluating_medical_large_language_models" -->
<!-- paper_url: "https://arxiv.org/abs/2312.12806" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *MedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models*

Source paper: [https://arxiv.org/abs/2312.12806](https://arxiv.org/abs/2312.12806)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2023_medbench_a_large_scale_chinese_benchmark_for_evaluating_medical_large_language_models/source.pdf`](../papers/2023_medbench_a_large_scale_chinese_benchmark_for_evaluating_medical_large_language_models/source.pdf)
- Extracted text: [`../papers/2023_medbench_a_large_scale_chinese_benchmark_for_evaluating_medical_large_language_models/source.txt`](../papers/2023_medbench_a_large_scale_chinese_benchmark_for_evaluating_medical_large_language_models/source.txt)
- Ownership for this pass is limited to this summary file. The registry was intentionally not edited.
- Normalization choice: this summary treats `MedBench` as a paper-level umbrella benchmark with four constituent benchmark sections: `Chinese Medical Licensing Examination (CNMLE)`, `Resident Standardization Training Examination`, `Doctor In-Charge Qualification Examination`, and `Real-World Clinical Cases`.
- Normalization choice: `A1/A2/B`, `A3/A4`, and `Case Analysis` are treated as task formats within the examination benchmarks rather than standalone benchmarks.
- Normalization choice: the paper's `Item Response Theory` difficulty-stratified analysis over 7,335 questions and the prompt-variation experiments are treated as evaluation slices, not as separate benchmarks.
- Example handling rerun (`2026-04-15`): Figure 2 contains one generic exam multiple-choice example and one explicit real-world examinations example. The exam example is still not attributed to a named constituent exam or normalized subtask, but it is now retained below as the closest official MedBench exam-family exemplar instead of being treated as missing.
- Prompt availability: the paper states that multiple-choice evaluations are performed in a five-shot setting and reports a Chain-of-Thought comparison for one Resident subset, but the full few-shot prompt text and the full Chain-of-Thought prompt are not explicitly provided.
- Judge availability: the paper reports expert human evaluation for real-world cases, but the full human-evaluation rubric/prompt is not explicitly provided.

## Benchmark Inventory

- `MedBench` umbrella benchmark: 40,041 total exercises spanning three examination sources plus real-world EHR-derived clinical cases.
- `Chinese Medical Licensing Examination (CNMLE)`: 27,248 questions; tasks normalized as `A1/A2/B` and `A3/A4`.
- `Resident Standardization Training Examination`: 2,841 questions; tasks normalized as `A1/A2/B`, `A3/A4`, and `Case Analysis`.
- `Doctor In-Charge Qualification Examination`: 8,927 questions; tasks normalized as `A1/A2/B`, `A3/A4`, and `Case Analysis`.
- `Real-World Clinical Cases`: 701 annotated reports converted into 1,025 question-answer pairs; tasks normalized as `Examinations`, `Diagnoses`, and `Treatments`.

## 1. MedBench

MedBench is a Chinese medical benchmark introduced in the paper to evaluate medical large language models against the education-to-practice trajectory of doctors in mainland China. It combines three authentic examination sources with expert-annotated real-world EHR cases, for a total of 40,041 exercises. The benchmark is explicitly positioned as a contamination-resistant and practice-aligned alternative to earlier Chinese or international medical QA benchmarks.

- **Language:** Chinese
- **Clinical Stage:** medical education, residency training, doctor-in-charge qualification, and real-world clinical practice
- **Source Clinical Document Type:** mixed benchmark composed of authentic examination questions plus expert-annotated EHR reports
- **Clinical Specialty:** multi-specialty, including traditional Chinese medicine and Chinese-western medicine content; internal medicine and surgery are shown as representative examples for later-stage exams
- **Application Method:** benchmark introduced in the paper; access/release method is not explicitly stated in the paper

---

## 2. Chinese Medical Licensing Examination (CNMLE)

The Chinese Medical Licensing Examination component is the first MedBench constituent benchmark and covers 27,248 multiple-choice questions collected from recent years of the licensing exam. It is used to evaluate foundational and early-practice medical knowledge in a mainland-China clinical context. The paper reports overall and question-type accuracy for this benchmark, but it does not provide question-type counts or split counts within CNMLE.

- **Language:** Chinese
- **Clinical Stage:** medical licensing / end-of-medical-school transition
- **Source Clinical Document Type:** authentic medical examination questions
- **Clinical Specialty:** multi-specialty
- **Application Method:** constituent benchmark within MedBench; exact public access path not explicitly stated

---

## 2.1 Task: A1/A2/B Single-Statement Multiple Choice

This task is to answer a Chinese medical exam question that has one correct option among five candidates.

### Task type
Multiple-choice QA / Classification

```md
### Instruction
Normalized from the paper: given a Chinese medical examination question with five answer options, select the single correct option.
### Input
A standalone medical question in Chinese plus five candidate options (A-E).
### Output
One selected answer option.
```

### Task example

Paper-level MedBench exam-family example from Figure 2. The paper does not attribute this item to CNMLE rather than another exam component, so it is recorded as the closest official exam exemplar instead of a CNMLE-specific sample:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options:
  - A. 门管区胆管和胆小管 (Bile ducts in portal tracts)
  - B. 肝胆管 (Hepatic ducts)
  - C. 毛细胆管 (Bile canaliculi)
  - D. 肝细胞 (Hepatocytes)
  - E. 胆总管 (Common bile duct)
- Accepted answer shown in Figure 2 responses: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy. The paper states that three-stage multiple-choice examinations are evaluated with accuracy.
### Evaluation Dimensions
Correctness of the selected option. Any finer-grained matching rule is not explicitly provided in the paper.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The paper mentions five-shot evaluation but does not provide the full few-shot prompt.
```

---

## 2.2 Task: A3/A4 Case-Linked Multiple Choice

This task is to answer a series of exam questions attached to a short clinical case, where each question still has one correct option among five candidates.

### Task type
Case-based QA / Classification

```md
### Instruction
Original task definition paraphrased from the paper: answer a series of questions accompanied by a clinical case, with one correct answer out of five options for each question.
### Input
A clinical case stem in Chinese followed by one or more multiple-choice questions with five options each.
### Output
One selected answer option per question.
```

### Task example

Closest official MedBench exam-family exemplar from Figure 2. The paper does not map it to CNMLE A3/A4 specifically, but it still preserves the benchmark's concrete exam-style input/output:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options A-E are shown in Figure 2.
- Accepted answer shown by the figure: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Correctness of the selected option for each question. Aggregation details beyond reported accuracy are not explicitly provided in the paper.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The full five-shot prompt is not explicitly provided.
```

---

## 3. Resident Standardization Training Examination

The Resident Standardization Training Examination component is the second MedBench constituent benchmark and covers 2,841 questions collected across recent years. It is intended to reflect the residency-stage assessment process in mainland China. The paper reports overall accuracy plus per-question-type results, and it uses this benchmark for a prompt-sensitivity comparison between vanilla prompting and Chain-of-Thought prompting on an A1/A2 subset.

- **Language:** Chinese
- **Clinical Stage:** residency training
- **Source Clinical Document Type:** authentic medical examination questions
- **Clinical Specialty:** multi-specialty; Figure 3 shows internal medicine and surgery as representative examples while noting many subcategories exist
- **Application Method:** constituent benchmark within MedBench; exact public access path not explicitly stated

---

## 3.1 Task: A1/A2/B Single-Statement Multiple Choice

This task is to answer a residency-stage medical exam question that has one correct option among five candidates.

### Task type
Multiple-choice QA / Classification

```md
### Instruction
Normalized from the paper: given a Chinese resident-training examination question with five answer options, select the single correct option.
### Input
A standalone residency exam question in Chinese plus five candidate options (A-E).
### Output
One selected answer option.
```

### Task example

Closest official MedBench exam-family exemplar from Figure 2. The paper does not identify whether the item belongs to the Resident component, so this remains a benchmark-family rather than subset-specific sample:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options A-E are shown in Figure 2.
- Accepted answer shown by the figure: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy. Table 3 also reports accuracy for a Resident A1/A2 subset under vanilla prompting versus Chain-of-Thought prompting.
### Evaluation Dimensions
Correctness of the selected option. The paper does not provide additional grading details or the exact prompt templates used in Table 3.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The full vanilla and Chain-of-Thought prompts are not explicitly provided in the paper.
```

---

## 3.2 Task: A3/A4 Case-Linked Multiple Choice

This task is to answer a series of residency exam questions attached to a clinical case, with one correct answer out of five options for each question.

### Task type
Case-based QA / Classification

```md
### Instruction
Original task definition paraphrased from the paper: answer a series of questions accompanied by a clinical case, with one correct answer out of five options for each question.
### Input
A clinical case stem in Chinese followed by one or more multiple-choice questions with five options each.
### Output
One selected answer option per question.
```

### Task example

Closest official MedBench exam-family exemplar from Figure 2. The paper does not identify whether the item belongs to the Resident A3/A4 subset, but it still supplies concrete exam input and output:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options A-E are shown in Figure 2.
- Accepted answer shown by the figure: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Correctness of the selected option for each question. The paper notes that A3/A4 questions are multi-question and more demanding on conversational and reasoning ability, but it does not define a separate rubric.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The full five-shot prompt is not explicitly provided.
```

---

## 3.3 Task: Case Analysis

This task is to answer a series of more complex clinical case-analysis questions, where each question has 6-12 options and some questions may have more than one correct answer.

### Task type
Clinical reasoning / Multi-answer multiple-choice QA

```md
### Instruction
Original task definition paraphrased from the paper: given a clinical case, answer a series of questions with 6-12 options per question; some questions may have more than one correct answer.
### Input
A residency-stage clinical case in Chinese followed by one or more case-analysis questions and 6-12 options per question.
### Output
The selected correct option or option set for each question.
```

### Task example

Closest official MedBench exam-family exemplar from Figure 2. This is not explicitly labeled as a Resident case-analysis item, but it is the nearest official examination example the paper publishes:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options A-E are shown in Figure 2.
- Accepted answer shown by the figure: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Correctness of the selected answer or answer set. The paper does not explain whether partially correct multi-answer responses receive partial credit, so the exact matching rule is unavailable.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The full few-shot prompt is not explicitly provided.
```

---

## 4. Doctor In-Charge Qualification Examination

The Doctor In-Charge Qualification Examination component is the third MedBench constituent benchmark and covers 8,927 questions from recent years. It is intended to reflect a later-career clinical qualification stage beyond residency. The paper reports overall accuracy and per-question-type accuracy, but it does not provide question-type counts or specialty-specific sample counts.

- **Language:** Chinese
- **Clinical Stage:** doctor-in-charge qualification / later-career physician certification
- **Source Clinical Document Type:** authentic medical examination questions
- **Clinical Specialty:** multi-specialty; Figure 3 shows internal medicine and surgery as representative examples while noting many subcategories exist
- **Application Method:** constituent benchmark within MedBench; exact public access path not explicitly stated

---

## 4.1 Task: A1/A2/B Single-Statement Multiple Choice

This task is to answer a doctor-in-charge qualification exam question that has one correct option among five candidates.

### Task type
Multiple-choice QA / Classification

```md
### Instruction
Normalized from the paper: given a Chinese doctor-in-charge examination question with five answer options, select the single correct option.
### Input
A standalone medical exam question in Chinese plus five candidate options (A-E).
### Output
One selected answer option.
```

### Task example

Closest official MedBench exam-family exemplar from Figure 2. The paper does not identify whether the item belongs to the Doctor In-Charge component, so it is preserved as a benchmark-family sample:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options A-E are shown in Figure 2.
- Accepted answer shown by the figure: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Correctness of the selected option. Any additional grading details are not explicitly provided in the paper.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The full few-shot prompt is not explicitly provided.
```

---

## 4.2 Task: A3/A4 Case-Linked Multiple Choice

This task is to answer a series of qualification-exam questions attached to a clinical case, with one correct answer out of five options for each question.

### Task type
Case-based QA / Classification

```md
### Instruction
Original task definition paraphrased from the paper: answer a series of questions accompanied by a clinical case, with one correct answer out of five options for each question.
### Input
A clinical case stem in Chinese followed by one or more multiple-choice questions with five options each.
### Output
One selected answer option per question.
```

### Task example

Closest official MedBench exam-family exemplar from Figure 2. The paper does not identify whether the item belongs to Doctor In-Charge A3/A4 specifically, but it still provides concrete exam I/O:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options A-E are shown in Figure 2.
- Accepted answer shown by the figure: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Correctness of the selected option for each question. The paper does not define a separate scoring rubric beyond reported accuracy.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The full few-shot prompt is not explicitly provided.
```

---

## 4.3 Task: Case Analysis

This task is to answer a series of more complex clinical case-analysis questions, where each question has 6-12 options and some questions may have more than one correct answer.

### Task type
Clinical reasoning / Multi-answer multiple-choice QA

```md
### Instruction
Original task definition paraphrased from the paper: given a clinical case, answer a series of questions with 6-12 options per question; some questions may have more than one correct answer.
### Input
A doctor-in-charge qualification case in Chinese followed by one or more case-analysis questions and 6-12 options per question.
### Output
The selected correct option or option set for each question.
```

### Task example

Closest official MedBench exam-family exemplar from Figure 2. This is not explicitly labeled as a Doctor In-Charge case-analysis item, but it is the nearest official exam example released in the paper:

- Question stem: Considered to be primary biliary cirrhosis. The main lesions of primary biliary cirrhosis are located in the ( ).
- Options A-E are shown in Figure 2.
- Accepted answer shown by the figure: `A. 门管区胆管和胆小管`

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Correctness of the selected answer or answer set. The exact handling of partially correct multi-answer responses is not explicitly provided in the paper.
### Judge Prompt
Not applicable. This task is scored with accuracy, not an LLM judge. The full few-shot prompt is not explicitly provided.
```

---

## 5. Real-World Clinical Cases

The real-world clinical case component is the fourth MedBench constituent benchmark and is derived from over 2,000 real-world electronic health records. Experts annotated symptoms, diagnoses, treatments, and examinations from these reports, yielding 701 high-quality reports with an average report length of 60-100 words and 1,025 final question-answer pairs. The paper evaluates this constituent benchmark with automatic overlap metrics and benchmark-level human evaluation performed by a postgraduate medical scholar.

- **Language:** Chinese
- **Clinical Stage:** real-world clinical practice
- **Source Clinical Document Type:** expert-annotated electronic health record reports
- **Clinical Specialty:** multi-specialty; exact specialty distribution is not explicitly stated
- **Application Method:** constituent benchmark within MedBench; created from annotated EHR reports, with release/access status not explicitly stated

---

## 5.1 Task: Examinations

This task is to predict the examination plan that should follow from a patient's symptoms in an EHR-derived clinical case.

### Task type
Clinical planning / Generation

```md
### Instruction
Normalized from Figure 2 and the benchmark description: given patient symptoms from a real-world case, provide the examination(s) that should be ordered or identified.
### Input
A symptom-focused case description derived from an annotated EHR report.
### Output
One or more examination names in Chinese.
```

### Task example

The paper provides an explicit example in Figure 2:

```md
### Example
Symptoms:
检查中发现右甲状腺甲状腺包块，遂于2018-08-14我院甲状腺外科就诊
(Examination revealed a nodule in the right lobe of the thyroid gland, so the patient visited the thyroid surgery department of our hospital on August 14, 2018.)

Target task:
检查 (Examinations)

Ground truth:
甲状腺彩超
(Thyroid ultrasound)
```

### Scoring standard

```md
### Scoring
Automatic metrics reported for this subtask are BLEU-1, BLEU-4, and ROUGE-L. The paper also reports benchmark-level human evaluation on real-world cases.
### Evaluation Dimensions
Automatic overlap scoring with BLEU-1 / BLEU-4 / ROUGE-L for Examinations. Human evaluation across real-world cases overall is reported as being performed by a postgraduate medical scholar on correctness, completeness, fluency, and friendliness, but the paper does not provide Examinations-only human scores or rubric details.
### Judge Prompt
The full human-evaluation prompt/rubric is not explicitly provided in the paper.
```

---

## 5.2 Task: Diagnoses

This task is to infer the likely diagnosis from a patient's symptom description in an EHR-derived clinical case.

### Task type
Clinical diagnosis / Generation

```md
### Instruction
Normalized from the benchmark description: given patient symptoms from a real-world case, provide the diagnosis.
### Input
A symptom-focused case description derived from an annotated EHR report.
### Output
A diagnosis or diagnosis list in Chinese.
```

### Task example

`No explicit diagnosis-task example is provided in the paper or appendix.`

### Scoring standard

```md
### Scoring
Automatic metrics reported for this subtask are BLEU-1, BLEU-4, and ROUGE-L. The paper also reports benchmark-level human evaluation on real-world cases.
### Evaluation Dimensions
Automatic overlap scoring with BLEU-1 / BLEU-4 / ROUGE-L for Diagnoses. Human evaluation across real-world cases overall is reported as being performed by a postgraduate medical scholar on correctness, completeness, fluency, and friendliness, but the paper does not provide Diagnoses-only human scores or rubric details.
### Judge Prompt
The full human-evaluation prompt/rubric is not explicitly provided in the paper.
```

---

## 5.3 Task: Treatments

This task is to infer the treatment plan from a patient's symptom description in an EHR-derived clinical case.

### Task type
Treatment recommendation / Generation

```md
### Instruction
Normalized from the benchmark description: given patient symptoms from a real-world case, provide the treatment(s).
### Input
A symptom-focused case description derived from an annotated EHR report.
### Output
A treatment plan or treatment list in Chinese.
```

### Task example

`No explicit treatment-task example is provided in the paper or appendix.`

### Scoring standard

```md
### Scoring
Automatic metrics reported for this subtask are BLEU-1, BLEU-4, and ROUGE-L. The paper also reports benchmark-level human evaluation on real-world cases.
### Evaluation Dimensions
Automatic overlap scoring with BLEU-1 / BLEU-4 / ROUGE-L for Treatments. Human evaluation across real-world cases overall is reported as being performed by a postgraduate medical scholar on correctness, completeness, fluency, and friendliness, but the paper does not provide Treatments-only human scores or rubric details.
### Judge Prompt
The full human-evaluation prompt/rubric is not explicitly provided in the paper.
```
