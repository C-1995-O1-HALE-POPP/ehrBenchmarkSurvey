<!-- paper_key: "2025_er_reason_a_benchmark_dataset_for_llm_based_clinical_reasoning_in_the_emergency_room" -->
<!-- paper_url: "https://arxiv.org/abs/2505.22919" -->
<!-- generated_on: "2026-05-11" -->

# Benchmark Summary for *ER-REASON: A Benchmark Dataset for LLM-Based Clinical Reasoning in the Emergency Room*

Source paper: [arXiv:2505.22919](https://arxiv.org/abs/2505.22919)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-05-11`.
- Registry file: [`registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`papers/2025_er_reason_a_benchmark_dataset_for_llm_based_clinical_reasoning_in_the_emergency_room/source.pdf`](../papers/2025_er_reason_a_benchmark_dataset_for_llm_based_clinical_reasoning_in_the_emergency_room/source.pdf)
- Extracted text: [`papers/2025_er_reason_a_benchmark_dataset_for_llm_based_clinical_reasoning_in_the_emergency_room/source.txt`](../papers/2025_er_reason_a_benchmark_dataset_for_llm_based_clinical_reasoning_in_the_emergency_room/source.txt)
- Record the exact search path used for this paper: paper body, appendix (prompt tables), and GitHub repo at https://github.com/AlaaLab/ER-Reason.
- The paper body contains full task descriptions, evaluation metrics, and experimental results. The appendix (Tables 8–16) contains all LLM input prompts with variable placeholders. No explicit dataset examples (full patient cases) are included in the paper — only prompt templates.
- Normalization notes: The paper uses "ER-REASON" (with a space) in text but "ER-R EASON" in the title (a typographic artifact). We normalize to "ER-REASON" throughout.
- Before syncing the registry, run:
  `python3 scripts/ehr_benchmark_pipeline.py audit-examples "summaries/2025_er_reason_a_benchmark_dataset_for_llm_based_clinical_reasoning_in_the_emergency_room_benchmark_summary.md"`
- After the summary passes verification, run:
  `python3 scripts/ehr_benchmark_pipeline.py sync-registry "summaries/2025_er_reason_a_benchmark_dataset_for_llm_based_clinical_reasoning_in_the_emergency_room_benchmark_summary.md"`

## Verifier Notes

- Benchmark existence: ER-REASON is the sole benchmark introduced and used in this paper.
- Task mapping: 5 tasks aligned with ER workflow stages: triage (acuity), EHR review (summarization), assessment+treatment (treatment planning with 3 reasoning dimensions), disposition (final diagnosis + disposition decision).
- Instruction fidelity: Prompt templates are verbatim from Appendix Tables 8–16.
- Example fidelity: No concrete patient-level dataset examples in the paper. Prompt templates are verbatim. Figure 3 shows a partial differential diagnosis example from GPT-4o vs physician (syncope case) but is not a full task example.
- Scoring fidelity: Evaluation metrics described in Section 3.3 — accuracy for acuity, ROUGE/F1 for summarization, cTAKES CUI overlap ratio for treatment planning, ICD-10 exact match + HCC match for diagnosis, accuracy for disposition.
- Judge prompt fidelity: No automated judge prompt. Physician evaluation rubric for hallucination severity and clinical utility (1–5 scales) described in Section 4 but full rubric not provided.
- Inference labeling: Models evaluated: LLaMA 3.2-3B Instruct, GPT-3.5, GPT-4o, o3-mini. Temperature settings: 0.1 (OpenAI models), 0.5 (LLaMA). HIPAA-compliant API for closed-weight models.

## 1. ER-REASON

ER-REASON is a benchmark introduced by this paper for evaluating LLM-based clinical reasoning and decision-making in the emergency room. The dataset comprises 3,984 ER patients (3,437 unique patients across 3,984 encounters) from a large academic medical center (UCSF), spanning March 2022 to March 2024. It includes 25,174 de-identified longitudinal clinical notes across multiple note types: discharge summaries, progress notes, history and physical exams (H&P), consult notes, echocardiogram reports, ECG reports, imaging notes, and ED provider notes. On average, there are 7 notes per encounter. The dataset covers 395 unique chief complaints, with the most frequent being abdominal pain, shortness of breath, and chest pain. The benchmark is designed to mirror five stages of the real-world ER workflow: triage intake, EHR review, initial assessment and treatment choice, and disposition planning with final diagnosis. A distinctive feature is the inclusion of 72 physician-authored clinical reasoning rationales (written by ER attending and resident physicians) that capture rule-out reasoning, medical decision factors, and treatment planning — elements typically absent from routine EHR documentation. The paper uses ER-REASON as its sole evaluation benchmark (primary, in-distribution).

- **Language:** English (U.S. academic medical center, UCSF)
- **Clinical Stage:** Emergency department — triage → EHR review → assessment → treatment → disposition (full ER workflow)
- **Source Clinical Document Type:** De-identified longitudinal clinical notes: discharge summaries, progress notes, H&P, consults, echocardiogram reports, ECG reports, imaging notes, and ED provider notes
- **Clinical Specialty:** Emergency medicine, multi-specialty acute care
- **Application Method:** Primary benchmark introduced in the paper; derived from UCSF EHR data with HIPAA-compliant de-identification. Data split and construction described in Section 3.1.

---

## 1.1 Task: ER Acuity Assessment

This task evaluates an LLM's ability to predict Emergency Severity Index (ESI) scores from sparse initial triage information, simulating the triage intake stage of the ER workflow.

### Task type
Classification

```md
### Instruction
Predict the emergency department acuity level for this patient.
Chief Complaint: {primarychiefcomplaintname}
Age: {age}
Sex: {sex}
Race: {firstrace}
Vital Signs: {vital_signs}
Select the most appropriate acuity level from the following options ONLY:
'Immediate', 'Emergent', 'Urgent', 'Less Urgent', 'Non-Urgent'
Respond with ONLY ONE of these five options.
### Input
Sparse initial patient intake: chief complaint, age, sex, race, and vital signs.
### Output
One of five ESI acuity levels: Immediate (1), Emergent (2), Urgent (3), Less Urgent (4), Non-Urgent (5).
```

### Task example

```md
### Example Provenance
Paper appendix (Table 8) — prompt template with variable placeholders. No concrete patient-level example provided in the paper.
### Search Depth
Paper + appendix
### Example Type
Prompt template
### Source Dataset / Artifact
ER-REASON dataset (UCSF EHR). Appendix Table 8.
### Task Construction
Inputs are extracted from structured patient intake data: chief complaint, demographics, and vital signs. The target is the ESI score assigned by the triage nurse or ER physician during the actual patient admission.
### Fidelity
Verbatim prompt template from appendix.
### Example
Predict the emergency department acuity level for this patient.
Chief Complaint: {primarychiefcomplaintname}
Age: {age}
Sex: {sex}
Race: {firstrace}
Vital Signs: {vital_signs}
Select the most appropriate acuity level from the following options ONLY:
'Immediate', 'Emergent', 'Urgent', 'Less Urgent', 'Non-Urgent'
Respond with ONLY ONE of these five options.
### Example Input
Not explicitly provided in the paper — variable placeholders only.
### Example Output
Not explicitly provided in the paper — variable placeholders only.
### Gold / Reference Answer
ESI score (1–5) assigned by ER physicians during actual patient admissions.
```

### Scoring standard

```md
### Scoring
Accuracy of ESI score prediction against ground-truth physician-assigned ESI scores.
### Evaluation Dimensions
Exact match accuracy across five ESI levels (Immediate, Emergent, Urgent, Less Urgent, Non-Urgent).
### Judge Prompt
Not applicable — automated accuracy metric against ground-truth labels.
```

---

## 1.2 Task: Patient Case Summarization

This task evaluates an LLM's ability to extract and summarize key details from a patient's most recent discharge summary, generating a concise "one-liner" summary tailored to the patient's current chief complaint. This mirrors the EHR review stage of the ER workflow.

### Task type
Generation / Summarization

```md
### Instruction
[System] You are an experienced emergency department (ED) physician creating a one-liner for a NEW patient who has just arrived at the ED. The patient's past medical records are available to you. Your task is to summarize the patient's relevant PAST medical history and end with their CURRENT chief complaint that is given with no adjectives about the chief complaint as you can NOT assume anything about their current condition. All notes and medical records provided are from PAST encounters, not the current visit.

[User] Create a concise one-liner summary for a patient who has just arrived at the Emergency Department. The one-liner must:
1. Start with demographic information (age, sex). Example of a one liner: 80 y.o. old male, with h/o of HFpEF (EF 55-60% 05/20/22), HTN, HLD, and bipolar disorder presenting with shortness of breath.
2. Include a concise summary of relevant PAST medical history from previous visits/notes
3. End with just CURRENT presenting chief complaint that is not capitalized in the summary and does have additional information regarding the chief complaint: '{chief_complaint}'
IMPORTANT: Everything in the notes is from PAST encounters. The patient is NOW presenting with a NEW complaint: '{chief_complaint}'.
Age: {age}
Sex: {sex}
PAST Medical Records: {discharge_summary}
### Input
Discharge summary text and current chief complaint.
### Output
Concise one-line patient summary starting with demographics, summarizing past medical history, and ending with the current chief complaint.
```

### Task example

```md
### Example Provenance
Paper appendix (Table 9) — full system and user prompt templates with variable placeholders. Example format "80 y.o. old male, with h/o of HFpEF..." is provided as an illustrative template rather than a concrete dataset instance.
### Search Depth
Paper + appendix
### Example Type
Prompt template with illustrative format example
### Source Dataset / Artifact
ER-REASON dataset (UCSF EHR). Appendix Table 9.
### Task Construction
Inputs are the patient's most recent discharge summary and current chief complaint. The target one-liner is generated by ER physicians. Evaluation uses ROUGE and F1 against physician-authored summaries.
### Fidelity
Verbatim prompt template from appendix.
### Example
Create a concise one-liner summary for a patient who has just arrived at the Emergency Department. The one-liner must:
1. Start with demographic information (age, sex). Example of a one liner: 80 y.o. old male, with h/o of HFpEF (EF 55-60% 05/20/22), HTN, HLD, and bipolar disorder presenting with shortness of breath.
2. Include a concise summary of relevant PAST medical history from previous visits/notes
3. End with just CURRENT presenting chief complaint that is not capitalized in the summary and does have additional information regarding the chief complaint: '{chief_complaint}'
### Example Input
Age, sex, discharge summary text, chief complaint — variable placeholders only.
### Example Output
Physician-authored one-liner summary — not explicitly provided for a concrete patient.
### Gold / Reference Answer
Physician-authored one-line patient summaries created for evaluation purposes.
```

### Scoring standard

```md
### Scoring
ROUGE-1-F1, ROUGE-2-F1, ROUGE-L-F1 against physician-authored one-liner summaries.
### Evaluation Dimensions
N-gram overlap and longest common subsequence between LLM-generated and physician-authored summaries.
### Judge Prompt
Not applicable — automated ROUGE metric computation.
```

---

## 1.3 Task: Treatment Planning — Rule-Out Reasoning

This task evaluates the model's ability to formulate a differential diagnosis list by applying rule-out reasoning based on the patient's past medical history and current chief complaint. This is one of three dimensions of the treatment planning task (Stage 3 of the ER workflow).

### Task type
Generation / Clinical Reasoning

```md
### Instruction
[System] You are an experienced Emergency Department (ED) physician tasked with creating a comprehensive assessment and plan for patients. Based on the available clinical information, you will provide: 1) A differential diagnosis list, 2) Medical decision factors including necessary exams/imaging to rule out diagnoses, and 3) A treatment plan including disposition and recommendations.

DIFFERENTIAL QUESTION: What are your initial differential diagnoses based on the past medical history (PREVIOUS HOSPITAL ENCOUNTER) and the chief complaint (CURRENT CHIEF COMPLAINT – THIS IS THE TREATMENT FOCUS), and why? Please also address which diagnoses are lowest on your differential and why.

[User] Based on the patient's chief complaint, age, sex, and available clinical information, provide:
DIFFERENTIAL DIAGNOSIS: List of differential diagnoses to consider for the CURRENT chief complaint given clinically relevant information such as the PAST medical notes.
IMPORTANT: Everything in the notes is from PAST encounters. The patient is NOW presenting with a NEW complaint: Chief Complaint: {chief_complaint}
Age: {age}
Sex: {sex}
Patient One-liner Summary: {one_liner}
REMINDER: All of these notes are from the PREVIOUS hospital encounter for this patient. This should only give you context for their current complaint: {notes_content}
### Input
All available EHR notes (past medical history), current chief complaint, ER clinical presentation, patient one-liner summary, age, and sex.
### Output
Differential diagnosis list with reasoning, including lowest-priority diagnoses and rationale.
```

### Task example

```md
### Example Provenance
Paper appendix (Tables 10, 11) — common system message and differential diagnosis prompt. Figure 3 in the paper body provides a partial qualitative example comparing GPT-4o vs. physician reasoning for a syncope case with color-coded concept overlap, but this is not a complete task input-output pair.
### Search Depth
Paper + appendix
### Example Type
Prompt template; partial qualitative comparison in Figure 3
### Source Dataset / Artifact
ER-REASON dataset, physician-authored rationales (72 cases). Appendix Tables 10–11.
### Task Construction
Inputs combine longitudinal EHR notes with chief complaint and demographics. The 72 gold-standard physician-authored rationales serve as reference outputs. Evaluation uses cTAKES to extract UMLS Concept Unique Identifiers (CUIs) and computes Clinical Concept Recall.
### Fidelity
Verbatim prompt template from appendix.
### Example
[Prompt template as shown in Instruction above; full concrete example not provided in the paper.]
### Example Input
EHR notes, chief complaint, demographics — variable placeholders only.
### Example Output
A differential diagnosis list with rule-out reasoning — qualitative partial example for syncope case shown in Figure 3.
### Gold / Reference Answer
72 physician-authored clinical reasoning rationales with rule-out reasoning, medical decision factors, and treatment plans.
```

### Scoring standard

```md
### Scoring
Clinical Concept Recall = |CUIs_LLM ∩ CUIs_Physician| / |CUIs_Physician|, where CUIs are UMLS Concept Unique Identifiers extracted via the cTAKES toolkit. CUIs map to a formal medical ontology (UMLS) spanning ICD, SNOMED-CT, CMS, RxNorm, and LOINC, maintaining semantic equivalence despite lexical variation.
### Evaluation Dimensions
Rule-out reasoning: proportion of physician-identified differential diagnoses and rule-out concepts matched by the model at the UMLS concept level.
### Judge Prompt
Not applicable — automated cTAKES CUI extraction and overlap computation.
```

---

## 1.4 Task: Treatment Planning — Medical Decision Factors

This task evaluates the model's ability to identify appropriate additional information, exams, imaging, laboratory tests, and specialist consultations needed to narrow the differential diagnosis. This is the second dimension of the treatment planning task.

### Task type
Generation / Clinical Reasoning

```md
### Instruction
[System - Common System Message from Table 10]
DECISION FACTORS: What additional information or studies would you want in order to help narrow your differential diagnoses? How would you weigh their relative importance?

[User] Based on the patient's chief complaint, age, sex, and available clinical information, provide:
MEDICAL DECISION FACTORS: List what important additional information you'd like to know on history, what important exam findings you'd assess for, and what imaging/tests you would do, in addition to any formal consultations you'd made with specialists – this should be items that would be necessary to rule out diagnoses on the differential list for the CURRENT chief complaint. NOTE: NOTHING has currently been performed.
IMPORTANT: Everything in the notes is from PAST encounters. The patient is NOW presenting with a NEW complaint: Chief Complaint: {chief_complaint}
Age: {age}
Sex: {sex}
Patient One-liner Summary: {one_liner}
REMINDER: All of these notes are from the PREVIOUS hospital encounter for this patient. This should only give you context for their current complaint: {notes_content}
### Input
All available EHR notes, current chief complaint, ER clinical presentation, patient one-liner summary, age, and sex.
### Output
List of medical decision factors: additional history questions, exam findings to assess, imaging/tests to order, and specialist consultations needed.
```

### Task example

```md
### Example Provenance
Paper appendix (Tables 10, 12) — common system message and medical decision factors prompt. No concrete patient-level example provided.
### Search Depth
Paper + appendix
### Example Type
Prompt template
### Source Dataset / Artifact
ER-REASON dataset, 72 physician-authored rationales. Appendix Tables 10, 12.
### Task Construction
Same as rule-out reasoning task. Physician-authored rationales include explicitly labeled medical decision factors.
### Fidelity
Verbatim prompt template from appendix.
### Example
[Prompt template as shown in Instruction above; full concrete example not provided.]
### Example Input
EHR notes, chief complaint, demographics — variable placeholders only.
### Example Output
List of recommended labs, imaging, exams, and consultations — not explicitly provided for a concrete patient.
### Gold / Reference Answer
Physician-authored medical decision factors within the 72 expert rationales.
```

### Scoring standard

```md
### Scoring
Clinical Concept Recall = |CUIs_LLM ∩ CUIs_Physician| / |CUIs_Physician|, using cTAKES UMLS CUI extraction.
### Evaluation Dimensions
Medical decision factors: proportion of physician-identified labs, imaging, exams, and consultations matched by the model at the UMLS concept level.
### Judge Prompt
Not applicable — automated cTAKES CUI extraction and overlap computation.
```

---

## 1.5 Task: Treatment Planning — Treatment Plan

This task evaluates the model's ability to propose a clinically sound management plan including immediate interventions and preliminary treatment, given the history and physical exam from the ED provider note. This is the third dimension of the treatment planning task (Stage 4 of the ER workflow).

### Task type
Generation / Clinical Reasoning

```md
### Instruction
[System - Common System Message from Table 10]
TREATMENT PLAN: Given the additional history and physical exam provided in the ED provider note, which additional diagnostic tests would you like to order and what is your recommended initial treatment plan?

[User] Based on the patient's chief complaint, age, sex, and available clinical information, provide:
TREATMENT PLAN: Given the current history and physical provided in the ED note, what do you think is the most likely diagnosis and what is your recommended treatment plan? If you do not have enough information to conclude a final diagnosis, describe what information you still need. Include disposition (discharge, admit, ICU, etc.) and treatment recommendations for the patient given the history and physical exam in the current ER visit.
IMPORTANT: Everything in the notes is from PAST encounters. The patient is NOW presenting with a NEW complaint: Chief Complaint: {chief_complaint}
Age: {age}
Sex: {sex}
Patient One-liner Summary: {one_liner}
REMINDER: All of these notes are from the PREVIOUS hospital encounter for this patient. This should only give you context for their current complaint: {notes_content}
### Input
All available EHR notes, current chief complaint, ER clinical presentation with history and physical exam, patient one-liner summary, age, and sex.
### Output
Most likely diagnosis, recommended treatment plan, additional information needed if uncertain, and disposition recommendation.
```

### Task example

```md
### Example Provenance
Paper appendix (Tables 10, 13) — common system message and treatment plan prompt. No concrete patient-level example provided.
### Search Depth
Paper + appendix
### Example Type
Prompt template
### Source Dataset / Artifact
ER-REASON dataset, 72 physician-authored rationales. Appendix Tables 10, 13.
### Task Construction
Same as above treatment planning dimensions. Physician-authored rationales include explicitly labeled treatment plans.
### Fidelity
Verbatim prompt template from appendix.
### Example
[Prompt template as shown in Instruction above; full concrete example not provided.]
### Example Input
EHR notes, chief complaint, demographics — variable placeholders only.
### Example Output
Treatment plan with disposition and recommendations — not explicitly provided for a concrete patient.
### Gold / Reference Answer
Physician-authored treatment plans within the 72 expert rationales.
```

### Scoring standard

```md
### Scoring
Clinical Concept Recall using cTAKES UMLS CUI extraction. Additionally, physician-rated hallucination severity (1–5) and clinical utility (1–5) evaluated on 20 GPT-4o rationales by a single board-certified ER physician.
### Evaluation Dimensions
Treatment planning: proportion of physician-identified treatment concepts matched; hallucination severity (degree of factually incorrect or fabricated content); clinical utility (extent to which outputs contribute meaningfully to clinical decisions).
### Judge Prompt
Physician evaluation rubric described in Section 4. Hallucination severity scale: 1 (no hallucinations) to 5 (most severe hallucinations). Clinical utility scale: 1 (not useful) to 5 (most clinically useful). Full rubric not explicitly provided in the paper.
```

---

## 1.6 Task: Final Diagnosis

This task evaluates the model's ability to predict the final ED diagnosis as a CMS standardized code in textual form, given the patient's chief complaint, demographics, and clinical presentation. This corresponds to the first part of Stage 5 (Disposition Plan) in the ER workflow.

### Task type
Classification / Generation

```md
### Instruction
[System] You are an experienced Emergency Department (ED) physician tasked with predicting the most likely diagnosis for a patient based on their presentation, chief complaint, and available medical information.

[User] Based on the patient's chief complaint, age, sex, and available clinical information, predict the most likely ED diagnosis. Provide a single diagnosis for the CURRENT ED Visit from the standardized CMS codes without explanation but with the word, not the code.
Chief Complaint: {chief_complaint}
Age: {age}
Sex: {sex}
Current ED Presentation: {presentation}
{notes_content}
### Input
Age, sex, chief complaint, past medical history, ED clinical presentation, and available clinical notes (selected by the model via a note selection subprompt, Table 16).
### Output
A single CMS diagnosis in textual form (not ICD code number).
```

### Task example

```md
### Example Provenance
Paper appendix (Table 14) — verbatim diagnosis prediction prompt. Note selection subprompt in Table 16 used upstream to select which clinical notes to include.
### Search Depth
Paper + appendix
### Example Type
Prompt template
### Source Dataset / Artifact
ER-REASON dataset (UCSF EHR). Appendix Tables 14, 16.
### Task Construction
Model first selects relevant note types via the note selection subprompt (Table 16), then predicts the diagnosis. Ground truth is the CMS diagnosis code assigned to the patient. Evaluation at two levels: ICD-10 exact match and HCC category match.
### Fidelity
Verbatim prompt template from appendix.
### Example
Based on the patient's chief complaint, age, sex, and available clinical information, predict the most likely ED diagnosis. Provide a single diagnosis for the CURRENT ED Visit from the standardized CMS codes without explanation but with the word, not the code.
Chief Complaint: {chief_complaint}
Age: {age}
Sex: {sex}
Current ED Presentation: {presentation}
{notes_content}
### Example Input
Chief complaint, demographics, presentation, selected notes — variable placeholders only.
### Example Output
A single CMS diagnosis word — not explicitly provided for a concrete patient.
### Gold / Reference Answer
CMS diagnosis code assigned to the patient during the actual ER visit.
```

### Scoring standard

```md
### Scoring
(1) ICD-10 Exact Match accuracy: model-predicted diagnosis must match the true ICD-10 code. (2) HCC Category Match accuracy: diagnosis grouped into broader Hierarchical Condition Categories as defined by CMS.
### Evaluation Dimensions
Exact ICD-10 code-level match; CMS HCC category-level match (broader, clinically meaningful groupings).
### Judge Prompt
Not applicable — automated matching against ground-truth CMS diagnosis codes.
```

---

## 1.7 Task: Final Disposition Decision

This task evaluates the model's ability to predict the appropriate patient disposition (discharge, admit, transfer, etc.) given the patient's full clinical context. This is the second part of Stage 5 (Disposition Plan) in the ER workflow.

### Task type
Classification

```md
### Instruction
[System] You are an experienced Emergency Department (ED) physician tasked with predicting the most likely disposition for a patient based on their presentation and physical, chief complaint, and available past medical information.

[User] Based on the patient's chief complaint, age, sex, and available clinical information, predict the most likely ED disposition from the following choices: 'Discharge', 'Admit', 'Eloped', 'Transfer to Another Facility', 'AMA', 'OR Admit', 'LWBS after Triage', 'Send to L&D', 'Expired', 'Dismissed - Never Arrived', 'Observation', 'None' – ONLY RESPOND WITH THESE OPTIONS, no explanations.
Chief Complaint: {chief_complaint}
Age: {age}
Sex: {sex}
Current ED Presentation: {presentation}
{notes_content}
### Input
Age, sex, chief complaint, past medical history, ED clinical presentation, and available clinical notes (selected by the model via a note selection subprompt, Table 16).
### Output
One of 12 disposition options: Discharge, Admit, Eloped, Transfer to Another Facility, AMA, OR Admit, LWBS after Triage, Send to L&D, Expired, Dismissed - Never Arrived, Observation, None.
```

### Task example

```md
### Example Provenance
Paper appendix (Table 15) — verbatim disposition prediction prompt. Note selection subprompt in Table 16 used upstream.
### Search Depth
Paper + appendix
### Example Type
Prompt template
### Source Dataset / Artifact
ER-REASON dataset (UCSF EHR). Appendix Tables 15, 16.
### Task Construction
Model first selects relevant note types via the note selection subprompt (Table 16), then predicts disposition. Ground truth is the physician-documented disposition from the structured tabular data of the corresponding ER visit. The paper notes that the true discharge rate is ~37% while o3-mini predicts discharge in only ~15% of cases.
### Fidelity
Verbatim prompt template from appendix.
### Example
Based on the patient's chief complaint, age, sex, and available clinical information, predict the most likely ED disposition from the following choices: 'Discharge', 'Admit', 'Eloped', 'Transfer to Another Facility', 'AMA', 'OR Admit', 'LWBS after Triage', 'Send to L&D', 'Expired', 'Dismissed - Never Arrived', 'Observation', 'None' – ONLY RESPOND WITH THESE OPTIONS, no explanations.
Chief Complaint: {chief_complaint}
Age: {age}
Sex: {sex}
Current ED Presentation: {presentation}
{notes_content}
### Example Input
Chief complaint, demographics, presentation, selected notes — variable placeholders only.
### Example Output
One of 12 disposition options — not explicitly provided for a concrete patient.
### Gold / Reference Answer
Physician-documented disposition from the ER visit structured tabular data.
```

### Scoring standard

```md
### Scoring
Accuracy of disposition prediction against physician-documented dispositions.
### Evaluation Dimensions
Exact match across 12 disposition categories.
### Judge Prompt
Not applicable — automated accuracy metric against ground-truth labels.
```

---

## 1.8 ER-REASON Notes

- The dataset is from a single academic medical center (UCSF), with 3,984 ER encounters across 3,437 patients, spanning March 2022 to March 2024.
- 25,174 de-identified clinical notes across 8+ note types. All notes are de-identified per HIPAA Safe Harbor standards.
- The benchmark covers the full ER workflow across 5 stages, with 7 tasks (5 main tasks; treatment planning split into 3 separately evaluated reasoning dimensions).
- 72 physician-authored clinical reasoning rationales provide gold-standard references for the treatment planning tasks (rule-out reasoning, medical factors, treatment plan).
- Clinical Concept Recall (cTAKES CUI overlap) is the primary metric for treatment planning tasks. The cTAKES toolkit maps free-text outputs to UMLS CUIs, enabling semantic equivalence matching across lexical variation (e.g., "Coronary Artery Disease" and "CAD" map to the same CUI: C1956346).
- Models evaluated: LLaMA 3.2-3B Instruct, GPT-3.5, GPT-4o, o3-mini. Temperature: 0.1 (OpenAI), 0.5 (LLaMA).
- Best performing model: o3-mini achieved highest accuracy on acuity (62.70%), ICD-10 match (34.40%), HCC match (81.08%), and disposition (63.08%). GPT-4o achieved best ROUGE-1-F1 on summarization (0.347).
- Key finding: Despite state-of-the-art reasoning models, there is still a gap between LLM-generated and clinician-authored clinical reasoning. Models show systematic biases: o3-mini over-classifies as "Urgent" and over-admits, suggesting risk-averse behavior that could lead to resource misallocation.
- Note selection subprompt (Table 16): Models autonomously select which note types to review before Tasks 3–5, simulating real-world clinical information triage.
- Limitations: Single-institution data; does not account for hospital-level contextual factors (bed availability, staffing, institutional protocols); only 72 cases have physician-authored rationales.
- Code and data: https://github.com/AlaaLab/ER-Reason
