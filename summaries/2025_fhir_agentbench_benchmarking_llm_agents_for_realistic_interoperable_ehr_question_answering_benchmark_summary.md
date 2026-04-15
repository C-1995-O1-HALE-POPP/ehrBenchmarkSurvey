<!-- paper_key: "2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering" -->
<!-- paper_url: "https://arxiv.org/abs/2509.19319" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering*

Source paper: [https://arxiv.org/abs/2509.19319](https://arxiv.org/abs/2509.19319)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.pdf`](../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.pdf)
- Extracted text: [`../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.txt`](../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.txt)
- The paper introduces one primary benchmark (`FHIR-AgentBench`). Other names in Table 1 are comparison baselines in related work discussion and are not newly constructed or re-evaluated benchmark tracks in this paper's main experiment section.
- Assumption used for normalization: the paper defines one benchmark with a two-stage protocol (resource retrieval + answer generation), but not a multi-task list. For survey consistency, we represent these two protocol stages as two tasks.
- Task instruction text is normalized from Section 4.1 task definition and Appendix D baseline prompts.

### Verifier Check (2026-04-15 rerun)

- Benchmark existence: `FHIR-AgentBench` is explicitly introduced in the title/abstract/main text.
- Task mapping: `1.1/1.2` are explicit normalization of the Section 4.1 two-stage protocol (retrieval + answer generation).
- Instruction fidelity: task instructions are normalized from Section 4.1 and Appendix D baseline prompts.
- Example fidelity: task examples use explicit Appendix C examples (C.1.1, C.2.2), not synthesized data.
- Scoring fidelity: retrieval metrics and answer-correctness rule follow Section 4.1 and Appendix A1.
- Judge prompt fidelity: paper uses an LLM evaluator for answer correctness, but does not provide the full evaluator prompt; this is explicitly marked as unavailable.
- Inference labeling: language/clinical stage/specialty fields are explicitly marked as inferred or not explicitly stated where needed.

## 1. FHIR-AgentBench

FHIR-AgentBench is an English interoperable EHR question answering benchmark introduced by the paper for evaluating LLM agents on realistic HL7 FHIR-based clinical data access and reasoning. The benchmark grounds 2,931 clinician-sourced single-patient questions in de-identified MIMIC-IV-FHIR data and provides, per example, a question, optional context, ground-truth FHIR resource IDs, and a final answer. Questions are sourced from EHRSQL-2024 and mapped to MIMIC-IV-FHIR-Demo/FHIR-compatible resources, including cases with empty answers (about 24%) to explicitly test no-result handling. The paper evaluates both retrieval quality and final answer correctness under single-turn and multi-turn agent settings.

- **Language:** English (inferred from paper language and question examples; not explicitly labeled as a metadata field)
- **Clinical Stage:** Not explicitly stated; inferred as longitudinal hospital course and point-of-care single-patient query answering
- **Source Clinical Document Type:** Structured EHR serialized as HL7 FHIR resources (not native free-text clinical notes)
- **Clinical Specialty:** Not explicitly stated; inferred as multi-specialty clinical QA over general inpatient data (observations, medications, encounters, conditions, procedures, etc.)
- **Application Method:** Public benchmark introduced in the paper; data/code and benchmark resources are released via the FHIR-AgentBench repository and based on MIMIC-IV-FHIR

---

## 1.1 Task: FHIR Resource Retrieval for Question Grounding

This task is to retrieve the relevant FHIR resources required to answer a patient-specific clinical question.

### Task type
Retrieval + QA Grounding

```md
### Instruction
Given a single-patient clinical question (and optional context), retrieve the set of FHIR resources needed to answer it. Resource retrieval should use FHIR-compatible queries/tools and return the relevant resource IDs/types for downstream reasoning.
### Input
[Natural language clinical question], [optional context], [patient identifier], [available FHIR resource types/tools]
### Output
[Predicted set of relevant FHIR resources/resource IDs]
```

### Task example

```md
### Example
Appendix C.1.1 (Retrieval Error Example):
Question: "What is the number of times that patient XXX had ostomy (output) since 12/03/2133?"
True answer: 68
Observed retrieval behavior: the agent queried Procedure resources and returned 0.
Ground-truth retrieval implication in the paper: relevant evidence should come from Observation resources (code 226582, category "Output"), not Procedure.
```

### Scoring standard

```md
### Scoring
Resource-level Retrieval Precision and Recall (Section 4.1):
- Precision P = |R_hat ∩ R| / |R_hat|
- Recall R = |R_hat ∩ R| / |R|
Edge-case handling in the paper:
- If true resources are empty but predictions exist: precision = 0; case excluded from recall calculation.
- If true resources exist but no predictions: recall = 0; case excluded from precision calculation.
- If both true and predicted resources are empty: precision = 1 and recall = 1.
### Evaluation Dimensions
- Retrieval precision (resource-level)
- Retrieval recall (resource-level)
### Judge Prompt
Not applicable for this task's core metric. Retrieval is evaluated by deterministic set-overlap formulas; no LLM judge prompt is used.
```

---

## 1.2 Task: Answer Generation from Retrieved FHIR Resources

This task is to generate the final answer to a clinical question using the retrieved FHIR resources.

### Task type
QA + Generation

```md
### Instruction
Given a clinical question and retrieved FHIR resources, generate the final answer in the expected answer format. If the relevant information is absent, return a no-information answer rather than guessing. In the paper's multi-turn baselines, the final response is constrained to the format "The final answer is: [answer]".
### Input
[Natural language clinical question], [optional context], [retrieved FHIR resources]
### Output
[Final answer value(s) matching benchmark ground-truth format; may be empty/no-result cases]
```

### Task example

```md
### Example
Appendix C.2.2 (Interpretation Error Example):
Question: "How many times patient XXX came to the hospital since 1 year ago?"
True answer: 1
Agent answer: 2
Paper's error analysis: the agent counted all Encounter resources and failed to filter for hospital/inpatient visits, causing overcounting.
```

### Scoring standard

```md
### Scoring
Answer Correctness (Section 4.1):
AC = 1(y_hat = y)
Because agent outputs are free-text, the paper uses an LLM evaluator (OpenAI o4-mini) to determine correctness against ground truth.
Appendix A1 reports 97% agreement with human judgment over 500 manually reviewed samples.
### Evaluation Dimensions
- Binary answer correctness against ground truth (correct/incorrect)
- The paper does not provide a multi-axis rubric beyond correctness alignment to reference answer.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper or appendix.
```

---
