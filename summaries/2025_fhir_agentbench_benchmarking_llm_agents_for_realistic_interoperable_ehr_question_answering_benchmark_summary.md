<!-- paper_key: "2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering" -->
<!-- paper_url: "https://arxiv.org/abs/2509.19319" -->
<!-- generated_on: "2026-04-20" -->

# Benchmark Summary for *FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering*

Source paper: [https://arxiv.org/abs/2509.19319](https://arxiv.org/abs/2509.19319)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-20`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.pdf`](../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.pdf)
- Extracted text: [`../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.txt`](../papers/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering/source.txt)
- Searched the main paper, Appendix A/C/D, and the official artifact referenced by the paper: `https://github.com/glee4810/FHIR-AgentBench`.
- The paper introduces one primary benchmark, `FHIR-AgentBench`.
- For survey consistency, the benchmark is normalized into two tasks matching the paper's explicit two-stage evaluation framework in Section 4.1: retrieval and answer generation.
- Appendix C provides concrete benchmark examples for both stages. Appendix D provides full baseline-agent prompts, which are used below only to normalize the task instruction wording rather than to fabricate new examples.

## Verifier Notes

- Benchmark existence: `FHIR-AgentBench` is explicit in the title, abstract, Table 1, Section 3, and the public repo.
- Task mapping: `1.1` and `1.2` are explicit normalization of the Section 4.1 two-stage protocol.
- Instruction fidelity: instructions are normalized from Section 4.1 and Appendix D baseline prompts.
- Example fidelity: task examples use concrete Appendix C examples and Table 2 benchmark samples rather than synthesized instances.
- Scoring fidelity: retrieval uses resource-level precision / recall; answer generation uses binary answer correctness as defined in Section 4.1.
- Judge prompt fidelity: the paper reports an LLM evaluator for answer correctness but does not publish the full evaluator prompt. That absence is marked explicitly.
- Inference labeling: clinical-stage / specialty labels are inferred from the benchmark's single-patient hospital-question setting.

## 1. FHIR-AgentBench

FHIR-AgentBench is an English interoperable EHR question-answering benchmark introduced by the paper for evaluating LLM agents over real HL7 FHIR-formatted patient data derived from MIMIC-IV-FHIR. The benchmark contains 2,931 question-context-FHIR-resource-answer pairs grounded in real patient data, with questions selected from EHRSQL-style clinical queries and translated into FHIR-compatible evaluation instances. Each example includes a natural-language question, optional context, a ground-truth set of FHIR resource IDs needed to answer the question, and a final answer. The paper deliberately retains empty-answer cases (about 24%) to test whether agents can correctly recognize that no relevant result exists.

- **Language:** English
- **Clinical Stage:** Not explicitly stated; inferred as single-patient longitudinal hospital-course and point-of-care query answering
- **Source Clinical Document Type:** Structured EHR serialized as HL7 FHIR resources rather than native free-text notes
- **Clinical Specialty:** Not explicitly stated; inferred as multi-specialty inpatient clinical QA over observations, medications, encounters, conditions, and related resources
- **Application Method:** Public benchmark introduced by the paper; code and data-construction scripts are released in the official `FHIR-AgentBench` repository and use MIMIC-IV-FHIR / MIMIC-IV-FHIR-Demo resources

---

## 1.1 Task: FHIR Resource Retrieval for Question Grounding

This task is to retrieve the relevant FHIR resources needed to answer a patient-specific clinical question.

### Task type
Retrieval

```md
### Instruction
Given a single-patient clinical question and any provided context, retrieve the set of FHIR resources needed to answer the question.
### Input
[Natural-language clinical question], [optional context], [patient identifier], [available FHIR resource types / retrieval tools]
### Output
[Predicted set of relevant FHIR resources or resource IDs]
```

### Task example

```md
### Example Provenance
Table 2 prints a full benchmark row for the respiratory-rate question, and the official repo releases the same row in `final_dataset/questions_answers_sql_fhir.csv` with stable fields such as `question_id`, `patient_fhir_id`, `true_fhir_ids`, `sql_query`, `template`, and `val_dict`. Appendix C.1.1 then publishes a full retrieval-error case: "Question: What is the number of times that patient XXX had ostomy (output) since 12/03/2133?", "True answer: 68", and "Agent answer: 0", followed by the diagnosis that "Ostomy output measurements are stored in Observation resources (code 226582, category "Output"), not in Procedure."
### Search Depth
Paper + appendix + linked artifact
### Example Type
Concrete benchmark row from official dataset plus paper-local retrieval-error analysis
### Source Dataset / Artifact
Table 2 and Appendix C.1.1 of the paper; official repo `final_dataset/questions_answers_sql_fhir.csv`
### Task Construction
For each question, the benchmark stores the natural-language question, optional assumption/context, patient FHIR identifier, and the gold `true_fhir_ids` map. Retrieval is correct when the agent surfaces the resource IDs needed for the downstream answer.
### Fidelity
Question, context, patient/resource IDs, SQL, template, and answer below are copied from the official CSV row with only line wrapping; the appendix error case is copied from the paper with whitespace cleanup.
### Example
Official dataset row (`question_id = 000f58d3abb4ad76b2ebc35c`):
- `split`: `train`
- `question`: `When was the first time the respiratory rate of patient 10018081 was measured to be less than 23.0 today?`
- `assumption`: `Assume the current time is 2133-12-31 23:59:00.`
- `patient_fhir_id`: `dd2bf984-33c3-5874-8f68-84113327877e`
- `true_fhir_ids`: `{'Observation': ['b2c4828b-2de2-5116-9485-9e34d05bee40']}`
- `true_answer`: `[['2133-12-31 02:00:00']]`
- `sql_query`: `SELECT chartevents.charttime FROM chartevents WHERE chartevents.stay_id IN ( SELECT icustays.stay_id FROM icustays WHERE icustays.hadm_id IN ( SELECT admissions.hadm_id FROM admissions WHERE admissions.subject_id = 10018081 ) ) AND chartevents.itemid IN ( SELECT d_items.itemid FROM d_items WHERE d_items.label = 'Respiratory Rate' AND d_items.linksto = 'chartevents' ) AND chartevents.valuenum < 23.0 AND datetime(chartevents.charttime,'start of day') = datetime('2133-12-31 00:00:00','start of day','-0 day') ORDER BY chartevents.charttime ASC LIMIT 1`
- `template`: `When was the [time_filter_exact1] time that the {vital_name} of patient {patient_id} was [comparison] than {vital_value} [time_filter_global1]?`
- `val_dict`: `{'val_placeholder': {'patient_id': 10018081, 'vital_name': 'respiratory rate', 'vital_value': 23.0}, 'op_placeholder': {'comparison': {'nlq': 'less', 'sql': '<', 'type': 'less', 'sql_pattern': '[comparison]'}}, 'time_placeholder': {'time_filter_exact1': {'nlq': 'first', 'sql': 'ORDER BY chartevents.charttime ASC LIMIT 1', 'type': 'exact-first', 'col': ['chartevents.charttime'], 'sql_pattern': 'time_filter_exact1(chartevents.charttime)'}, 'time_filter_global1': {'nlq': 'today', 'sql': "AND datetime(chartevents.charttime,'start of day') = datetime('2133-12-31 00:00:00','start of day','-0 day')", 'type': 'rel-day-this', 'col': ['chartevents.charttime'], 'sql_pattern': 'time_filter_global1_absolute(chartevents.charttime)'}}}`

Appendix C.1.1 retrieval-error case:
- `Question`: `What is the number of times that patient XXX had ostomy (output) since 12/03/2133?`
- `True answer`: `68`
- `Agent answer`: `0`
- `Error`: `Ostomy output measurements are stored in Observation resources (code 226582, category "Output"), not in Procedure.`
### Example Input
Natural Language Question: `When was the first time the respiratory rate of patient 10018081 was measured to be less than 23.0 today?`
Context / assumption: `Assume the current time is 2133-12-31 23:59:00.`
Patient FHIR ID: `dd2bf984-33c3-5874-8f68-84113327877e`
### Example Output
`{'Observation': ['b2c4828b-2de2-5116-9485-9e34d05bee40']}`
### Gold / Reference Answer
The official dataset row exposes the gold retrieval target directly as `{'Observation': ['b2c4828b-2de2-5116-9485-9e34d05bee40']}`. The paired gold answer after reasoning over that resource is `[['2133-12-31 02:00:00']]`.
```

### Scoring standard

```md
### Scoring
Resource-level precision and recall:
- Precision = |R_hat intersect R| / |R_hat|
- Recall = |R_hat intersect R| / |R|
Edge-case handling from the paper:
- If true resources are empty but predictions exist, precision = 0 and the case is excluded from recall calculation
- If true resources exist but nothing is predicted, recall = 0 and the case is excluded from precision calculation
- If both true and predicted resource sets are empty, precision = 1 and recall = 1
### Evaluation Dimensions
- Retrieval precision
- Retrieval recall
### Judge Prompt
Not applicable. Retrieval is evaluated by deterministic set-overlap formulas.
```

---

## 1.2 Task: Answer Generation from Retrieved FHIR Resources

This task is to generate the final answer to a clinical question using the retrieved FHIR resources.

### Task type
QA

```md
### Instruction
Given a clinical question and the retrieved FHIR resources, generate the final answer in the benchmark's expected answer format. If the evidence is absent, return a no-information answer rather than guessing.
### Input
[Natural-language clinical question], [optional context], [retrieved FHIR resources]
### Output
[Final answer value or values matching the benchmark reference format]
```

### Task example

```md
### Example Provenance
Appendix C.2.2 explicitly prints the benchmark row content for the hospital-visit counting example and its failure explanation. The official repo further exposes full released rows in `questions_answers_sql_fhir.csv`, including yes/no and counting questions with their `true_answer`, `true_fhir_ids`, SQL, and template fields. Appendix D publishes the exact baseline-agent answer format: "When you have completed your analysis and are ready to provide the final answer, you MUST format your response as follows : The final answer is : [ your answer here ]".
### Search Depth
Paper + appendix + linked artifact
### Example Type
Concrete benchmark row from official dataset plus paper-local interpretation-error analysis
### Source Dataset / Artifact
Appendix C.2.2 of the paper; official repo `final_dataset/questions_answers_sql_fhir.csv`; Appendix D prompt
### Task Construction
After retrieval, the agent must interpret the returned FHIR resources, produce the benchmark answer value, and serialize it in the task's expected answer format. In the multi-turn setting, the paper requires the response suffix `The final answer is : [ your answer here ]`.
### Fidelity
Question, assumption, patient/resource IDs, SQL, template, and gold answer below are copied from the official CSV row with line wrapping only; the interpretation-error case and answer-format instruction are copied from the appendix with whitespace cleanup.
### Example
Official dataset row (`question_id = 0018b73b2eda7611f63bee38`):
- `split`: `valid`
- `question`: `Did patient 10029291 undergo a ultrasonography of superior vena cava, guidance treatment in the first hospital visit?`
- `assumption`: `When searching for values in the database, account for all variations in letter case and surrounding whitespace.`
- `patient_fhir_id`: `7ec7078a-0593-5a99-9862-ebbff47fd1c5`
- `true_fhir_ids`: `{'Procedure': ['9780364b-459b-5f63-be17-3b39de7a5632', '1b37804d-01ef-504a-9c03-29420820e2cd']}`
- `true_answer`: `[[1]]`
- `sql_query`: `SELECT COUNT(*)>0 FROM procedures_icd WHERE procedures_icd.icd_code = ( SELECT d_icd_procedures.icd_code FROM d_icd_procedures WHERE d_icd_procedures.long_title = 'Ultrasonography of Superior Vena Cava, Guidance' ) AND procedures_icd.hadm_id IN ( SELECT admissions.hadm_id FROM admissions WHERE admissions.subject_id = 10029291 AND admissions.dischtime IS NOT NULL ORDER BY admissions.admittime ASC LIMIT 1 )`
- `template`: `Has_verb patient {patient_id} received a {procedure_name} procedure [time_filter_global1]?`
- `val_dict`: `{'val_placeholder': {'procedure_name': 'ultrasonography of superior vena cava, guidance', 'patient_id': 10029291}, 'op_placeholder': {}, 'time_placeholder': {'time_filter_global1': {'nlq': 'on the first hospital visit', 'sql': 'AND admissions.dischtime IS NOT NULL ORDER BY admissions.admittime ASC LIMIT 1', 'type': 'rel-hosp-first', 'col': ['admissions.admittime', 'admissions.dischtime'], 'sql_pattern': 'time_filter_global1_event(admissions.admittime, admissions.dischtime)'}}}`

Appendix C.2.2 interpretation-error case:
- `Question`: `How many times patient XXX came to the hospital since 1 year ago?`
- `True answer`: `1`
- `Agent answer`: `2`
- `Error`: `One of the counted encounters was an ambulatory visit. Because the agent did not filter encounters for hospital/inpatient visits (e.g., via identifier.system containing "encounter-hosp" or class.code == 'IMP'), it overcounted hospital visits.`

Appendix D final-answer format:
- `The final answer is : [ your answer here ]`
### Example Input
Question: `Did patient 10029291 undergo a ultrasonography of superior vena cava, guidance treatment in the first hospital visit?`
Retrieved resources: `{'Procedure': ['9780364b-459b-5f63-be17-3b39de7a5632', '1b37804d-01ef-504a-9c03-29420820e2cd']}`
### Example Output
`The final answer is : 1`
### Gold / Reference Answer
The released row stores the gold answer as `[[1]]`, i.e. a yes/no answer with `1 = yes`. Appendix C.2.2 separately shows a counting example whose gold answer is `1`.
```

### Scoring standard

```md
### Scoring
Binary answer correctness:
AC = 1(y_hat = y)
Because model outputs are free-text, the paper uses an LLM evaluator (OpenAI o4-mini) to decide correctness against the reference answer.
Appendix A1 reports 97 percent agreement between the evaluator and human judgment on 500 manually reviewed samples.
### Evaluation Dimensions
- Binary answer correctness against the benchmark reference answer
- The paper does not provide a richer multi-axis rubric beyond correctness
### Judge Prompt
The full evaluator prompt is not explicitly provided in the paper, appendix, or linked repo materials searched for this summary.
```
