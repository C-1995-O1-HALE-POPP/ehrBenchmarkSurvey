<!-- paper_key: "2025_medagentbench_a_realistic_virtual_ehr_environment_to_benchmark_medical_llm_agents" -->
<!-- paper_url: "https://arxiv.org/abs/2501.14654" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents*

Source paper: [https://arxiv.org/abs/2501.14654](https://arxiv.org/abs/2501.14654)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2025_medagentbench_a_realistic_virtual_ehr_environment_to_benchmark_medical_llm_agents/source.pdf`](../papers/2025_medagentbench_a_realistic_virtual_ehr_environment_to_benchmark_medical_llm_agents/source.pdf)
- Extracted text: [`../papers/2025_medagentbench_a_realistic_virtual_ehr_environment_to_benchmark_medical_llm_agents/source.txt`](../papers/2025_medagentbench_a_realistic_virtual_ehr_environment_to_benchmark_medical_llm_agents/source.txt)
- The paper defines one primary benchmark (`MedAgentBench`) with 300 clinically derived tasks.
- Mapping assumption used for survey normalization: task sections below follow the 7 broad categories explicitly listed in Table 1.
- Uncertainty note: the paper states 10 specific task categories grouped into these 7 broad categories, but the full 10-item list is not clearly enumerated in main text/appendix text extraction.
- Instruction mapping note: paper provides benchmark-wide execution prompt in Appendix A.2; per-task instructions below are normalized from Table 1 example instructions and benchmark constraints.
- Verifier pass (`2026-04-15`): benchmark existence, task mapping, instruction normalization labels, task examples, scoring rules, and judge-prompt availability were re-checked against Table 1, Section 2.4.1, Section 2.4.3, and Appendix A.2.
- Evaluation note: the benchmark uses deterministic/reference-plus-rule-based grading, not LLM-as-a-judge.

## 1. MedAgentBench

MedAgentBench is an English medical agent benchmark introduced by the paper to evaluate LLM agents in a realistic virtual EHR environment. It contains 300 clinician-written, patient-specific, clinically derived tasks across inpatient and outpatient scenarios, with cases built from de-identified and jittered STARR data. Tasks are executed in a FHIR-compliant environment, and performance is measured primarily by pass@1 task success rate with manually curated reference solutions and rule-based graders.

- **Language:** English (inferred from paper examples/prompts; not explicitly stated as multilingual)
- **Clinical Stage:** Longitudinal hospital course and ambulatory workflow operations
- **Source Clinical Document Type:** Structured EHR data exposed through FHIR APIs (not native free-text clinical notes)
- **Clinical Specialty:** General internal medicine-oriented workflow with multi-domain clinical operations
- **Application Method:** Public benchmark introduced in the paper; code and environment released at the project GitHub/Docker resources

---

## 1.1 Task: Patient Information Retrieval

This task is to retrieve core patient identity or demographic information from the EHR system.

### Task type
Retrieval

```md
### Instruction
Given a clinician request and available EHR context, retrieve the requested patient identity/demographic field (for example MRN) by issuing valid FHIR API calls, then return the final answer in the requested format.
### Input
[High-level clinician request, patient-identifying fields such as name/DOB, environment context, and available FHIR functions]
### Output
[Single requested patient information value]
```

### Task example

- Explicit task example is provided in Table 1.

```md
### Example
User instruction: "What is the MRN of the patient with name {name} and DOB of {DOB}?"
Context: N/A
```

### Scoring standard

- This paper does not provide a task-specific separate rubric for this category; benchmark-wide rules apply.

```md
### Scoring
Primary metric: task success rate under pass@1.
For query-based tasks, the agent final response is compared with the answer produced by the manually curated reference solution.
Failure conditions include invalid actions and exceeding the maximum interaction rounds.
### Evaluation Dimensions
- Correctness of final returned value versus reference solution output.
- Validity of tool invocation format if tools are invoked.
- Completion within the benchmark interaction budget (maximum 8 rounds).
### Judge Prompt
No explicit LLM-judge prompt is provided. The paper reports deterministic/reference-solution grading rather than LLM-as-a-judge.
```

---

## 1.2 Task: Lab Result Retrieval

This task is to query recent laboratory observations under time and unit constraints.

### Task type
Retrieval

```md
### Instruction
Given a clinician query about a lab result (for example latest magnesium within 24 hours), use valid GET requests to retrieve the needed observation, apply any specified time window/unit conversion rules, and return the requested numeric result or fallback value if unavailable.
### Input
[Clinician query, patient MRN, time window rules, lab code context (e.g., LOINC/local code), and available FHIR functions]
### Output
[Requested lab value in the specified unit/format, or defined fallback output]
```

### Task example

- Explicit task example is provided in Table 1.

```md
### Example
User instruction: "What's the most recent magnesium level of the patient {MRN} within last 24 hours?"
Context: "It's 2023-11-13T10:15:00+00:00 now. The code for magnesium is MG. The answer should be a single number converted to mg/dL, and it should be -1 if a measurement within last 24 hours is not available."
```

### Scoring standard

- This paper does not provide a task-specific separate rubric for this category; benchmark-wide rules apply.

```md
### Scoring
Primary metric: task success rate under pass@1.
For query-based tasks, responses are compared against reference answers generated by manually curated reference solutions.
Failure conditions include invalid actions and exceeding the maximum interaction rounds.
### Evaluation Dimensions
- Correctness of returned lab value against the reference answer.
- Compliance with required answer format/unit constraints when specified by task context.
- Completion within the benchmark interaction budget (maximum 8 rounds).
### Judge Prompt
No explicit LLM-judge prompt is provided. The paper reports deterministic/reference-solution grading rather than LLM-as-a-judge.
```

---

## 1.3 Task: Patient Data Aggregation

This task is to compute aggregated statistics from patient time-series data.

### Task type
Retrieval + Calculation

```md
### Instruction
Given a request for an aggregated clinical measure (for example average glucose over last 24 hours), retrieve the relevant observations from EHR via valid API calls, compute the required aggregate correctly, and provide the final value in the requested format.
### Input
[Clinician aggregation request, patient MRN, aggregation rule and time window, mapping context such as base names/codes]
### Output
[Computed aggregate value]
```

### Task example

- Explicit task example is provided in Table 1.

```md
### Example
User instruction: "What is the average [blood glucose level] of the patient {MRN} over the last 24 hours?"
Context: "It's 2023-11-13T10:15:00+00:00 now. The base name for CBG is GLU."
```

### Scoring standard

- This paper does not provide a task-specific separate rubric for this category; benchmark-wide rules apply.

```md
### Scoring
Primary metric: task success rate under pass@1.
For query-based tasks, responses are compared against reference answers generated by manually curated reference solutions.
Failure conditions include invalid actions and exceeding the maximum interaction rounds.
### Evaluation Dimensions
- Correctness of computed aggregate result versus reference output.
- Correct use of relevant retrieval signals from provided system context.
- Completion within the benchmark interaction budget (maximum 8 rounds).
### Judge Prompt
No explicit LLM-judge prompt is provided. The paper reports deterministic/reference-solution grading rather than LLM-as-a-judge.
```

---

## 1.4 Task: Recording Patient Data

This task is to document newly observed clinical data into the EHR system.

### Task type
Action Execution

```md
### Instruction
Given newly measured patient data (for example blood pressure), construct and send a valid POST payload to create the corresponding clinical record in the EHR using the provided system identifiers and context.
### Input
[Clinician instruction containing patient MRN and measurement values, relevant flowsheet/field identifiers, and available FHIR functions]
### Output
[Valid POST action sequence and completion response indicating documentation is performed]
```

### Task example

- Explicit task example is provided in Table 1.

```md
### Example
User instruction: "I just measured the blood pressure for patient with MRN of {MRN}, and it was 118/77 mmHg. Help me document this."
Context: "It's 2023-11-13T10:15:00+00:00 now. The flowsheet ID for blood pressure is BP."
```

### Scoring standard

- This paper does not provide a task-specific separate rubric for this category; benchmark-wide rules apply.

```md
### Scoring
Primary metric: task success rate under pass@1.
For action-based tasks, graders apply manually written rule-based sanity checks to verify POST payload correctness.
Failure conditions include invalid actions and exceeding the maximum interaction rounds.
### Evaluation Dimensions
- Validity and parseability of action payload structure.
- Correctness of key action fields according to task/context constraints.
- Completion within the benchmark interaction budget (maximum 8 rounds).
### Judge Prompt
No explicit LLM-judge prompt is provided. The paper reports deterministic rule-based grading rather than LLM-as-a-judge.
```

---

## 1.5 Task: Test Ordering

This task is to conditionally place laboratory test orders based on prior chart review.

### Task type
Retrieval + Conditional Action

```md
### Instruction
Given a conditional order request, first retrieve the required historical lab information, then decide whether ordering criteria are met (for example recency threshold), and if needed issue a valid POST order request with appropriate coding context.
### Input
[Clinician conditional order instruction, patient MRN, threshold/time criteria, lab coding context, available FHIR functions]
### Output
[Decision result and, when criteria are met, valid POST order action]
```

### Task example

- Explicit task example is provided in Table 1.

```md
### Example
User instruction: "What is the last hemoglobin A1C value in the chart for patient {MRN} and when was it recorded? If the lab value result date is greater than 1 year old, order a new hemoglobin A1C lab test."
Context: "It's 2023-11-13T10:15:00+00:00 now. The LOINC code for HbA1C lab is 4548-4."
```

### Scoring standard

- This paper does not provide a task-specific separate rubric for this category; benchmark-wide rules apply.

```md
### Scoring
Primary metric: task success rate under pass@1.
For action-based tasks (including conditional actions), graders apply manually written rule-based sanity checks to verify POST payload correctness and action validity.
Failure conditions include invalid actions and exceeding the maximum interaction rounds.
### Evaluation Dimensions
- Correct conditional decision behavior based on retrieved evidence.
- Correctness/validity of resulting order action and payload fields when action is required.
- Completion within the benchmark interaction budget (maximum 8 rounds).
### Judge Prompt
No explicit LLM-judge prompt is provided. The paper reports deterministic rule-based grading rather than LLM-as-a-judge.
```

---

## 1.6 Task: Referral Ordering

This task is to create specialist referral orders with specified free-text and coded details.

### Task type
Action Execution

```md
### Instruction
Given a referral instruction, generate and submit a valid referral POST payload including required specialty coding and user-requested free-text details.
### Input
[Referral request with patient MRN and referral text requirements, specialty code context (e.g., SNOMED), available FHIR functions]
### Output
[Valid referral order POST action and completion response]
```

### Task example

- Explicit task example is provided in Table 1.

```md
### Example
User instruction: "Order orthopedic surgery referral for patient {MRN}. Specify within the free text of the referral..."
Context: "It's 2023-11-13T10:15:00+00:00 now. The SNOMED code for orthopedic surgery referral is 306181000000106."
```

### Scoring standard

- This paper does not provide a task-specific separate rubric for this category; benchmark-wide rules apply.

```md
### Scoring
Primary metric: task success rate under pass@1.
For action-based tasks, graders apply manually written rule-based sanity checks to verify POST payload correctness.
Failure conditions include invalid actions and exceeding the maximum interaction rounds.
### Evaluation Dimensions
- Correct use of required referral coding and fields.
- Correct inclusion of required free-text referral content constraints.
- Completion within the benchmark interaction budget (maximum 8 rounds).
### Judge Prompt
No explicit LLM-judge prompt is provided. The paper reports deterministic rule-based grading rather than LLM-as-a-judge.
```

---

## 1.7 Task: Medication Ordering

This task is to execute medication ordering logic conditioned on recent lab values and dosing rules.

### Task type
Retrieval + Conditional Action

```md
### Instruction
Given medication replacement instructions, retrieve the relevant recent lab result, evaluate the threshold rule, calculate required dose according to provided dosing instructions, and issue a valid medication POST order when indicated.
### Input
[Medication instruction with patient MRN, threshold and dosing protocol, drug code context (e.g., NDC), related lab code context, available FHIR functions]
### Output
[Ordering decision and, if criteria met, valid medication order POST action]
```

### Task example

- Explicit task example is provided in Table 1.

```md
### Example
User instruction: "Check patient {MRN}'s most recent potassium level. If [below threshold provided], then order replacement potassium according to dosing instructions."
Context: "It's 2023-11-13T10:15:00+00:00 now. The NDC for replacement potassium is 40032-917-01. Dosing instructions: for every 0.1 mEq/L (or mmol/L) below threshold, order 10 mEq potassium oral repletion to reach a goal of 3.5 serum level. The LOINC code for serum potassium level is 2823-3."
```

### Scoring standard

- This paper does not provide a task-specific separate rubric for this category; benchmark-wide rules apply.

```md
### Scoring
Primary metric: task success rate under pass@1.
For action-based tasks (including conditional actions), graders apply manually written rule-based sanity checks to verify POST payload correctness and action validity.
Failure conditions include invalid actions and exceeding the maximum interaction rounds.
### Evaluation Dimensions
- Correct threshold-based decision making from retrieved lab value.
- Correct dose computation and payload content against provided dosing rules.
- Completion within the benchmark interaction budget (maximum 8 rounds).
### Judge Prompt
No explicit LLM-judge prompt is provided. The paper reports deterministic rule-based grading rather than LLM-as-a-judge.
```
