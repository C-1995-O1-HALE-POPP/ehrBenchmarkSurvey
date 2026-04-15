<!-- paper_key: "2023_ehrsql_a_practical_text_to_sql_benchmark_for_electronic_health_records" -->
<!-- paper_url: "https://arxiv.org/abs/2301.07695" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *EHRSQL: A Practical Text-to-SQL Benchmark for Electronic Health Records*

Source paper: [https://arxiv.org/abs/2301.07695](https://arxiv.org/abs/2301.07695)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2023_ehrsql_a_practical_text_to_sql_benchmark_for_electronic_health_records/source.pdf`](../papers/2023_ehrsql_a_practical_text_to_sql_benchmark_for_electronic_health_records/source.pdf)
- Extracted text: [`../papers/2023_ehrsql_a_practical_text_to_sql_benchmark_for_electronic_health_records/source.txt`](../papers/2023_ehrsql_a_practical_text_to_sql_benchmark_for_electronic_health_records/source.txt)
- The paper introduces one primary benchmark (`EHRSQL`) and additionally uses one reused benchmark (`MIMICSQL`) for zero-shot cross-domain transfer evaluation.
- Task normalization assumption: the paper defines one core benchmark task ("trustworthy semantic parsing"), but reports two metric-focused evaluation aspects (`F1ans`, `F1exe`). To keep survey formatting consistent, these are represented as three task entries under `EHRSQL`.
- Scope note for reused benchmarks: `MIMICSQL` details in this summary are limited to what this paper explicitly states (mainly comparative and transfer-evaluation context), not a full reconstruction of the original MIMICSQL paper specification.
- Task example policy (updated workflow): explicit examples are taken from Figure 1, Table 1, and Appendix Table 14/15 when available; no synthetic examples are used.
- Example-search rerun (`2026-04-15`): the EHRSQL paper does not print a worked MIMICSQL transfer instance for Section 4.5, so the reused-benchmark task below now keeps a source-benchmark example from the official MIMICSQL paper instead of recording the transfer setup as example-free.
- Judge prompt policy (updated workflow): this paper uses deterministic metrics (`F1ans`, `F1exe`, execution accuracy) and does not provide an LLM-judge setup or judge prompt.
- After the summary is complete, run:
  `python3 scripts/ehr_benchmark_pipeline.py sync-registry "/Users/cometp/Documents/ehrBenchmarkSurvey/summaries/2023_ehrsql_a_practical_text_to_sql_benchmark_for_electronic_health_records_benchmark_summary.md"`

## 1. EHRSQL

EHRSQL is an English text-to-SQL benchmark designed for trustworthy question answering over structured electronic health records. It is introduced by the paper and linked to two open-source EHR databases, MIMIC-III and eICU. The dataset is constructed from a hospital poll of 222 staff members, then expanded through template and paraphrase pipelines to cover practical hospital information needs, rich time-sensitive expressions, and unanswerable questions. The benchmark includes 24,411 question-SQL pairs in total (22.5K answerable and 1.9K unanswerable), with 230 question templates (174 answerable, 56 unanswerable). For evaluation, unanswerable questions are assigned only to validation and test (33% of each split), and the released train+validation portion is about 21K samples while test is hidden.

- **Language:** English (examples and templates are in English; multilingual setting is not stated)
- **Clinical Stage:** Longitudinal inpatient and ICU hospital course, plus hospital operations and utilization analysis
- **Source Clinical Document Type:** Structured EHR relational tables converted into question-SQL pairs (not native clinical note narratives)
- **Clinical Specialty:** Multi-specialty (critical care, nursing workflows, physician workflows, insurance/administrative analytics)
- **Application Method:** Public benchmark introduced in the paper, released at `https://github.com/glee4810/EHRSQL`

---

## 1.1 Task: Trustworthy Semantic Parsing

This task is to answer natural-language healthcare questions over structured EHR databases by generating executable SQL only when the question is answerable, and refusing otherwise.

### Task type
Generation + Classification

```md
### Instruction
Given a natural-language question about structured EHR data, generate a SQL query that correctly answers the question when it is answerable under the database schema and context. If the question is unanswerable, do not send generated SQL to the database (i.e., refuse the query according to a confidence threshold policy).
### Input
[One natural-language EHR question over MIMIC-III or eICU; schema-aware setting]
### Output
[Either an executable SQL query for answerable questions or a refusal decision for unanswerable/low-confidence cases]
```

### Task example

```md
### Example
Question (Figure 1):
When was the last time that patient 1234 had a body temperature measured?

SQL Query (Figure 1):
SELECT chartevents.charttime
FROM chartevents
WHERE chartevents.icustay_id IN (
  SELECT icustays.icustay_id
  FROM icustays
  WHERE icustays.hadm_id IN (
    SELECT admissions.hadm_id
    FROM admissions
    WHERE admissions.subject_id = 1234
  )
)
AND chartevents.itemid IN (
  SELECT d_items.itemid
  FROM d_items
  WHERE d_items.label = 'temperature c (calc)'
    AND d_items.linksto = 'chartevents'
)
ORDER BY chartevents.charttime DESC
LIMIT 1
```

### Scoring standard

```md
### Scoring
This task is evaluated with a combination of answerability recognition and execution correctness:
- F1ans: combines Pans and Rans for recognizing answerable questions.
- F1exe: combines Pexe and Rexe and counts a case as correct only when the returned answer is correct after SQL execution.

### Evaluation Dimensions
- Answerability recognition quality (precision/recall/F1ans)
- Correct execution result quality under refusal policy (Pexe/Rexe/F1exe)

### Judge Prompt
The full judge prompt is not explicitly provided in the paper.
```

---

## 1.2 Task: Answerability Recognition (F1ans)

This task is to distinguish answerable from unanswerable EHR questions as a reliability gate before SQL execution.

### Task type
Classification

```md
### Instruction
Given a natural-language EHR question, determine whether the question is answerable using the target database and schema in the benchmark setting.
### Input
[One natural-language EHR question]
### Output
[Binary label: answerable / unanswerable]
```

### Task example

```md
### Example
Answerable sample question (Table 1):
Tell me the birthdate of patient 92721?

Unanswerable sample question (Table 1):
When is the next earliest hospital visit of patient 73652?
```

### Scoring standard

```md
### Scoring
Primary metric: F1ans.
- Pans: correctly recognized answerable questions / all questions predicted answerable.
- Rans: correctly recognized answerable questions / all answerable questions.
- F1ans: harmonic mean of Pans and Rans.

### Evaluation Dimensions
- Precision on answerable prediction (Pans)
- Recall on answerable prediction (Rans)
- Balanced recognition quality (F1ans)

### Judge Prompt
The full judge prompt is not explicitly provided in the paper.
```

---

## 1.3 Task: Executable SQL Retrieval Under Refusal Policy (F1exe)

This task is to maximize correct retrieved answers while penalizing wrong SQL executions and missed answerable questions.

### Task type
Generation + Execution-based Evaluation

```md
### Instruction
Given a natural-language EHR question, return SQL only if predicted answerable; then execute the SQL and retrieve the correct answer. If confidence is low or the question is predicted unanswerable, refuse instead of executing an unreliable query.
### Input
[One natural-language EHR question (+ model confidence signal / threshold policy)]
### Output
[Executable SQL and retrieved answer, or refusal]
```

### Task example

```md
### Example
Falsely executed sample (Appendix Table 14):
Question: what was the duration of the packed cell transfusion procedure for patient 9566?
Real SQL: nan
Generated SQL: (model-generated SQL shown in Table 14)
Comment: Execution error

Refused sample (Appendix Table 15):
Question: how many patients were prescribed with magnesium sulfate within the same month after the treatment of cont inv mec ven <96 hrs?
Real SQL: (gold SQL shown in Table 15)
Generated SQL: (model-generated SQL shown in Table 15)
Comment: refused result sample
```

### Scoring standard

```md
### Scoring
Primary metric: F1exe.
- Pexe: correctly answered questions / all questions predicted answerable.
- Rexe: correctly answered questions / all answerable questions.
- F1exe: harmonic mean of Pexe and Rexe.
Only cases with correct returned answers after execution are counted as correct.

### Evaluation Dimensions
- Execution correctness of predicted-answerable cases
- Coverage over all answerable questions
- Precision-recall balance under refusal policy

### Judge Prompt
The full judge prompt is not explicitly provided in the paper.
```

---

## 2. MIMICSQL

MIMICSQL is a reused healthcare text-to-SQL benchmark over MIMIC-III that the paper uses for cross-domain transfer comparison (not as the newly introduced benchmark). In the paper, MIMICSQL appears in benchmark comparisons and in zero-shot execution-accuracy experiments with the GAP model, where MIMICSQL is used as a simpler parsable healthcare SQL setting relative to EHRSQL.

- **Language:** English (inferred from benchmark usage and question examples in the paper context)
- **Clinical Stage:** Inpatient/ICU structured EHR querying
- **Source Clinical Document Type:** Structured EHR relational tables converted to text-to-SQL pairs
- **Clinical Specialty:** Critical care and general hospital structured-data QA
- **Application Method:** Reused public benchmark used for comparative and zero-shot transfer evaluation in this paper

---

## 2.1 Task: Zero-Shot Cross-Domain Transfer Execution (GAP)

This task is to test whether a general-domain text-to-SQL model can transfer to healthcare SQL generation without in-domain fine-tuning.

### Task type
Generation (Zero-shot Transfer Evaluation)

```md
### Instruction
Given a MIMICSQL validation question, generate a SQL query in a zero-shot setting using a general-domain text-to-SQL model, then evaluate by execution accuracy on answerable questions.
### Input
[Natural-language question from MIMICSQL validation split]
### Output
[Generated SQL query; scored by execution accuracy]
```

### Task example

```md
### Example
Source-benchmark example reused because the EHRSQL paper evaluates MIMICSQL in zero-shot transfer but does not print a worked MIMICSQL instance:

Question:
how many patients admitted in emergency were tested for ferritin?

Ground-truth SQL:
select count (distinct demographic."subject_id") from demographic
inner join lab on demographic.hadm_id = lab.hadm_id
where demographic."admission_type" = "emergency" and lab."label" = "ferritin"

Provenance:
MIMICSQL source paper, Table 6 Example 2.
```

### Scoring standard

```md
### Scoring
Execution accuracy on answerable questions in the validation set.
The paper reports:
- MIMICSQL: 16.4% (164/1000)
- EHRSQL parsable subset for comparison: 4.7% (5/107)

### Evaluation Dimensions
- Exact execution correctness on answerable validation queries
- Performance by SQL hardness groups (easy/medium/hard/extra) as reported in Table 6

### Judge Prompt
The full judge prompt is not explicitly provided in the paper.
```
