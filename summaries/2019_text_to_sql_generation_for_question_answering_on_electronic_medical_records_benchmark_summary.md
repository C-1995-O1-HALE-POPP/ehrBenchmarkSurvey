<!-- paper_key: "2019_text_to_sql_generation_for_question_answering_on_electronic_medical_records" -->
<!-- paper_url: "https://arxiv.org/abs/1908.01839" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *Text-to-SQL Generation for Question Answering on Electronic Medical Records*

Source paper: [https://arxiv.org/abs/1908.01839](https://arxiv.org/abs/1908.01839)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2019_text_to_sql_generation_for_question_answering_on_electronic_medical_records/source.pdf`](../papers/2019_text_to_sql_generation_for_question_answering_on_electronic_medical_records/source.pdf)
- Extracted text: [`../papers/2019_text_to_sql_generation_for_question_answering_on_electronic_medical_records/source.txt`](../papers/2019_text_to_sql_generation_for_question_answering_on_electronic_medical_records/source.txt)
- The paper introduces one healthcare benchmark dataset (`MIMICSQL`) and evaluates all models on this dataset with multiple subsets/splits.
- Assumption used for normalization: because the paper does not publish per-example prompt templates as a separate appendix instruction block, task `Instruction/Input/Output` below are normalized from Section 3 (dataset construction) and Section 5 (evaluation setup).
- Example-search rerun (`2026-04-15`): the robustness subsection does not isolate one noisy benchmark row in a table, but Sections 4.2.4-4.2.5 do provide a concrete noisy question plus the intended recovered SQL condition values. The robustness task below now keeps that partial worked example instead of treating the task as example-free.
- Verifier pass (`2026-04-15`): task examples were re-checked against Section 3.2.1 and Table 6, scoring definitions were re-checked against Section 5.1.4 and Tables 2-3, and no LLM-judge prompt was found in the paper.

## 1. MIMICSQL

MIMICSQL is an English healthcare Question-to-SQL benchmark introduced in the paper for question answering over electronic medical records stored as a multi-relational database. It is built from MIMIC-III and includes 10,000 Question-SQL pairs across five linked tables (Demographics, Diagnosis, Procedure, Prescriptions, Laboratory tests), with both machine-generated template questions and human-paraphrased natural language questions. The benchmark supports both direct retrieval and reasoning-style questions, and evaluation is reported with logic-form accuracy and execution accuracy on train/dev/test splits (0.8/0.1/0.1), including a noisy test variant for robustness to missing information and typos.

- **Language:** English (inferred from released question examples and paper descriptions; not explicitly labeled as a language field)
- **Clinical Stage:** ICU and longitudinal hospital course (derived from MIMIC-III critical care records)
- **Source Clinical Document Type:** Structured EHR serialized into relational SQL tables (not narrative clinical notes)
- **Clinical Specialty:** Critical care, multi-specialty inpatient care
- **Application Method:** Public benchmark introduced in the paper; dataset and code released via the project repository

---

## 1.1 Task: Template Question Text-to-SQL

This task is to generate executable SQL queries from machine-generated healthcare template questions over multi-table EMR data.

### Task type
Generation

```md
### Instruction
Given a healthcare question generated from predefined retrieval/reasoning templates over MIMICSQL tables, produce the corresponding SQL query that retrieves the correct answer from the relational EMR database.
### Input
[One template-style healthcare question in natural language; database schema context is implicit in question wording]
### Output
[One SQL query in the benchmark format: SELECT ... FROM ... WHERE ...]
```

### Task example

```md
### Example
Retrieval template example from Section 3.2.1:
What is the H1 and H2 of Patient Pat (or Disease D, or Procedure Pro, or Prescription Pre, or Lab test L)?

General SQL template paired with generated questions in Section 3.2.1:
SELECT $AGG_OP ($AGG_COLUMN)+ FROM $TABLE WHERE ($COND_COLUMN $COND_OP $COND_VAL)+
```

### Scoring standard

```md
### Scoring
Primary metrics from Section 5.1.4:
1) Execution accuracy (Acc_EX = N_EX / N): a prediction is counted correct if the generated SQL returns the correct answer.
2) Logic form accuracy (Acc_LF = N_LF / N): a prediction is counted correct only when the generated SQL exactly matches the ground-truth SQL string.

### Evaluation Dimensions
- SQL exact-match correctness (logic form)
- SQL execution-result correctness (answer-level)

### Judge Prompt
No LLM judge is used in this paper. The full judge prompt is not explicitly provided in the paper.
```

---

## 1.2 Task: Natural Language Question Text-to-SQL

This task is to generate SQL queries from human-paraphrased clinical questions that preserve the semantics of the original template questions.

### Task type
Generation

```md
### Instruction
Given a human-written natural language healthcare question (paraphrased from a validated template question), generate the SQL query that yields the same answer as the ground-truth query on the EMR database.
### Input
[One natural language healthcare question from the NL subset of MIMICSQL]
### Output
[One SQL query aligned with ground-truth semantics and executable on the benchmark database]
```

### Task example

```md
### Example
Explicit NL example from Table 6 (Example 2):
Question:
how many patients admitted in emergency were tested for ferritin?

Ground-truth SQL:
select count (distinct demographic."subject_id") from demographic
inner join lab on demographic.hadm_id = lab.hadm_id
where demographic."admission_type" = "emergency" and lab."label" = "ferritin"
```

### Scoring standard

```md
### Scoring
Primary metrics from Section 5.1.4, reported for NL development/testing in Table 2:
1) Execution accuracy (Acc_EX = N_EX / N)
2) Logic form accuracy (Acc_LF = N_LF / N)

### Evaluation Dimensions
- SQL exact-match correctness (logic form)
- SQL execution-result correctness (answer-level)

### Judge Prompt
No LLM judge is used in this paper. The full judge prompt is not explicitly provided in the paper.
```

---

## 1.3 Task: Noisy Template Question Text-to-SQL (Robustness)

This task is to generate SQL queries when test questions include missing information, abbreviations, or typos, emphasizing robust condition-value recovery.

### Task type
Generation

```md
### Instruction
Given a noisy template healthcare question with partial condition information and/or typos, generate the most accurate SQL query possible and recover condition values when feasible from schema/value cues.
### Input
[One noisy template question from the robustness test set]
### Output
[One SQL query that preserves intended semantics under noisy input conditions]
```

### Task example

```md
### Example
Closest worked robustness example reconstructed from Sections 4.2.4-4.2.5:

Noisy question:
How many patients who have bowel obstruct and stay in hospital for more than 10 days?

Recovered target SQL:
SELECT COUNT ( PATIENT_ID ) FROM DEMOGRAPHIC
WHERE PRIMARY_DISEASE = bowel obstruction
  AND DAYS_OF_STAY > 10

Why this counts as the robustness example:
- the paper uses `bowel obstruct` as the abbreviated / noisy condition value
- the recover module is explicitly described as correcting it to `bowel obstruction`
- the numeric condition `> 10 days` is preserved
```

### Scoring standard

```md
### Scoring
Primary metrics are unchanged from Section 5.1.4:
1) Execution accuracy (Acc_EX = N_EX / N)
2) Logic form accuracy (Acc_LF = N_LF / N)

For noisy template evaluation, Table 3 additionally reports break-down matching on:
- Aggop
- Aggcol
- Table
- Concol+op
- Conval
- Average

### Evaluation Dimensions
- SQL exact-match correctness (logic form)
- SQL execution-result correctness (answer-level)
- Component-level SQL matching under noise (Table 3 break-down fields)

### Judge Prompt
No LLM judge is used in this paper. The full judge prompt is not explicitly provided in the paper.
```
