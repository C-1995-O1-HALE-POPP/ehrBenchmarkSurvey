<!-- paper_key: "2024_overview_of_the_ehrsql_2024_shared_task_on_reliable_text_to_sql_modeling_on_electronic_health_records" -->
<!-- paper_url: "https://arxiv.org/abs/2405.06673" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *Overview of the EHRSQL 2024 Shared Task on Reliable Text-to-SQL Modeling on Electronic Health Records*

Source paper: [https://arxiv.org/abs/2405.06673](https://arxiv.org/abs/2405.06673)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2024_overview_of_the_ehrsql_2024_shared_task_on_reliable_text_to_sql_modeling_on_electronic_health_records/source.pdf`](../papers/2024_overview_of_the_ehrsql_2024_shared_task_on_reliable_text_to_sql_modeling_on_electronic_health_records/source.pdf)
- Extracted text: [`../papers/2024_overview_of_the_ehrsql_2024_shared_task_on_reliable_text_to_sql_modeling_on_electronic_health_records/source.txt`](../papers/2024_overview_of_the_ehrsql_2024_shared_task_on_reliable_text_to_sql_modeling_on_electronic_health_records/source.txt)
- Normalization assumption: the paper presents one shared task with a unified reliability objective (correct SQL generation + abstention). For survey consistency, it is represented as one benchmark with one core task.
- Normalization assumption: the paper does not provide a unified per-instance task template (`Instruction/Input/Output`), so the task block below is normalized from Section 2 and Section 4.1.
- Example availability statement: no explicit single worked task instance is provided in the main paper or Appendix A. Following the deeper example-search policy, the task section therefore reuses one source-benchmark answerable example from the earlier EHRSQL benchmark with explicit provenance instead of leaving the example block empty.

## Verifier Notes

- Benchmark existence verified: `EHRSQL 2024 Shared Task` is explicitly described in Section 2 and throughout the paper.
- Task mapping verified: one core shared-task objective (reliable text-to-SQL with abstention) is explicit; representing it as one survey task is a normalization choice.
- Instruction fidelity verified: the instruction block is normalized from Section 2 task definition and Section 4.1 metric behavior.
- Example fidelity verified: no explicit task instance is provided in the paper/appendix. The task example below is intentionally inherited from the source EHRSQL benchmark and labeled as such rather than synthesized.
- Scoring fidelity verified: `RS(c)` definition, five scoring cases, `Acc(x)` execution-accuracy definition, and main metric `RS(10)` are taken from Section 4.1.
- Judge prompt fidelity verified: official scoring is deterministic (`RS` + execution accuracy); no LLM-judge prompt is provided.
- Inference labeling verified: fields such as language and clinical stage are marked as inferred or not explicitly stated.

## 1. EHRSQL 2024 Shared Task

EHRSQL 2024 Shared Task is an English clinical text-to-SQL benchmark designed for reliable question answering over structured EHR databases. It is derived from the earlier EHRSQL question template pool and augmented with MIMIC-IV Demo-linked SQL pairs, new LLM-generated paraphrases, adversarial unanswerable questions (partly from the EHRSQL portion of TrustSQL), and a harder split containing seen and unseen answerable templates. The benchmark evaluates whether systems can both generate correct SQL for answerable questions and abstain on likely incorrect or intrinsically unanswerable questions under the Reliability Score (RS) metric family.

The shared-task data is reported as follows: train/valid/test total samples of 5124/1163/1167, with unanswerable samples 450/232/233 (20% per split), and answerable question templates distributed as 100 (train) and 134 (valid/test; 100 seen + 34 unseen).

- **Language:** English (inferred; source poll utterances were collected in South Korea and translated, while the shared-task release/paper uses English question forms)
- **Clinical Stage:** Not explicitly stated (benchmark targets longitudinal EHR database QA rather than a single stage-specific workflow)
- **Source Clinical Document Type:** Structured EHR tables (MIMIC-IV Demo relational schema) queried via SQL
- **Clinical Specialty:** Multi-specialty hospital workflows (physicians, nurses, and administrative staff use cases)
- **Application Method:** Public shared-task benchmark introduced by the paper; dataset released at `https://github.com/glee4810/ehrsql-2024` and hosted on Codabench

---

## 1.1 Task: Reliable Text-to-SQL Modeling with Abstention

This task is to answer clinical natural-language questions over EHR tables by generating executable SQL for answerable questions while abstaining for unanswerable questions or cases likely to be answered incorrectly.

### Task type
Text-to-SQL Generation + Selective Prediction (Abstention) / QA

```md
### Instruction
Given a clinical question about an EHR database:
1. Determine whether the question is answerable from the provided EHR schema/database content.
2. If answerable, generate a SQL query that returns the correct answer.
3. If unanswerable (or if reliable SQL generation is not possible), abstain instead of outputting an incorrect SQL query.
4. Optimize for reliability under RS(c), which rewards:
   - correct SQL on answerable questions,
   - abstention on unanswerable questions,
   and penalizes incorrect SQL and false answering of unanswerable questions.
### Input
Natural-language clinical question + EHR database schema/content context (MIMIC-IV Demo setting).
### Output
Either:
- a SQL query (for answerable questions), or
- an abstain decision (no SQL), for unanswerable or unreliable cases.
```

### Task example

```md
### Example
Inherited answerable example from the source EHRSQL benchmark, used here because the 2024 shared-task paper does not print a full worked instance:

Question:
how many patients admitted in emergency were tested for ferritin?

Ground-truth SQL:
select count (distinct demographic."subject_id") from demographic
inner join lab on demographic.hadm_id = lab.hadm_id
where demographic."admission_type" = "emergency" and lab."label" = "ferritin"

Provenance:
EHRSQL source benchmark summary, which cites the MIMICSQL source paper Table 6 Example 2.

Coverage note:
This captures the answerable half of the shared-task format. The shared-task paper does not print a matched abstention / unanswerable example with a gold abstain output.
```

### Scoring standard

```md
### Scoring
Official metric: Reliability Score RS(c), computed per sample and averaged across the evaluation set.

Per-sample cases (Section 4.1):
1) score = 1, if question is answerable, model answers (g(x)=1), and SQL execution is correct (Acc(x)=1)
2) score = 0, if question is answerable and model abstains (g(x)=0)
3) score = -c, if question is answerable, model answers, but SQL execution is incorrect (Acc(x)=0)
4) score = -c, if question is unanswerable but model still outputs SQL (g(x)=1)
5) score = 1, if question is unanswerable and model abstains (g(x)=0)

Acc(x) is execution accuracy: 1 when predicted SQL and gold SQL return matching answers, else 0.
Main leaderboard metric: RS(10). The paper also reports RS(0) and RS(N).

### Evaluation Dimensions
- Answerability handling (answer vs abstain via g(x))
- SQL correctness on answerable questions (execution accuracy Acc(x))
- Penalty-aware reliability under different c (RS(0), RS(10), RS(N))
- Safety behavior on unanswerable questions (abstain vs harmful SQL output)

### Judge Prompt
Not applicable for the official metric. The paper uses a deterministic metric (RS + execution accuracy) and does not provide an LLM-judge prompt.
```
