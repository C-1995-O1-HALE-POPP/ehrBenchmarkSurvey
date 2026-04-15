<!-- paper_key: "2025_from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for_ehr_database_agents" -->
<!-- paper_url: "https://arxiv.org/abs/2509.23415" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *From Conversation to Query Execution: Benchmarking User and Tool Interactions for EHR Database Agents*

Source paper: [https://arxiv.org/abs/2509.23415](https://arxiv.org/abs/2509.23415)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Re-processed with updated workflow requirements on `2026-04-15` (task example + scoring standard + verifier pass).
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2025_from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for_ehr_database_agents/source.pdf`](../papers/2025_from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for_ehr_database_agents/source.pdf)
- Extracted text: [`../papers/2025_from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for_ehr_database_agents/source.txt`](../papers/2025_from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for_ehr_database_agents/source.txt)
- Normalization assumption: the paper introduces one benchmark (`EHR-ChatQA`) with two interaction flows rather than a conventional fixed task list. For survey consistency, the two flows (`IncreQA`, `AdaptQA`) are represented as two task entries.
- Task-level `Instruction/Input/Output` fields are normalized from Section 3-4 task definitions and Appendix A.1 sample task instances; the paper does not provide one unified per-task template table for all 366 instances.
- After the summary is complete, run:
  `python3 scripts/ehr_benchmark_pipeline.py sync-registry "/Users/cometp/Documents/ehrBenchmarkSurvey/summaries/2025_from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for_ehr_database_agents_benchmark_summary.md"`

### Verifier Check (2026-04-15)

- Benchmark existence: `EHR-ChatQA` appears explicitly in title/abstract/main text.
- Task mapping: `IncreQA` and `AdaptQA` are explicit interaction flows (Section 4.1); represented as two survey tasks by normalization.
- Instruction fidelity: task instructions are normalized from Section 4.1 and Appendix A.1 task-instance definitions.
- Example fidelity: both tasks use explicit Appendix A.1 samples; no synthesized examples are introduced.
- Scoring fidelity: task scoring rules come from Appendix A.6 and Section 5.1 evaluation metrics; validator details come from Appendix A.4 (Tables 6-7).
- Judge prompt fidelity: full simulation-validator prompt is included from Tables 6-7; no additional hidden prompt is fabricated.
- Inference labeling: language/clinical metadata that are not formal paper metadata fields remain marked as inferred or not explicitly stated.

## 1. EHR-ChatQA

EHR-ChatQA is an English interactive EHR database question answering benchmark designed to evaluate end-to-end LLM agent performance from ambiguous user conversation to SQL execution and final answer delivery. It is introduced by the paper and grounded in real-world clinical QA scenarios over two public ICU EHR systems (MIMIC-IV and eICU), with schema-renamed variants (MIMIC-IV* and eICU*) to reduce schema memorization effects. The benchmark contains 366 task instances (286 IncreQA, 80 AdaptQA), each with user instruction, gold SQL, and gold answer, and is evaluated in a simulated user + tool environment with validator-backed trace filtering for reliability analysis.

- **Language:** English (inferred from paper language and instruction examples; not explicitly labeled in a metadata table)
- **Clinical Stage:** ICU-focused longitudinal hospital course query answering
- **Source Clinical Document Type:** Structured EHR tables (MIMIC-IV/eICU demo schemas, renamed as MIMIC-IV* and eICU*)
- **Clinical Specialty:** Multi-specialty clinical QA with ICU data focus
- **Application Method:** Public benchmark introduced in the paper; code/data release referenced at `https://github.com/glee4810/EHR-ChatQA`

---

## 1.1 Task: Incremental Query Refinement (IncreQA)

This task is to interactively refine an initially vague clinical query by incrementally adding constraints while preserving previously established context and generating executable SQL for the final information request.

### Task type
Interactive QA + Text-to-SQL Generation

```md
### Instruction
Given an EHR question-answering conversation with a vague initial request, maintain conversational context as the user incrementally adds new constraints toward a single linear goal. Clarify missing details when needed, use available schema/value exploration tools, generate and execute SQL, and return the final answer that satisfies all accumulated constraints.
### Input
[Initial vague user query], [multi-turn user clarifications], [database schema/tools over MIMIC-IV* or eICU*], [optional external clinical knowledge via web search].
### Output
[Final answer to the user query], with correct SQL execution path consistent with all incremental constraints.
```

### Task example

```md
### Example
Appendix A.1.1 explicit sample task instance (IncreQA):
- task id: 6
- task type: incre
- db id: mimic iv star
- instruction: "Your goal is to find the number of patients admitted to the hospital who meet specific criteria. Specifically, you want to know how many patients admitted in the past 90 days have a family history of breast cancer."
- gold sql: provided explicitly in Appendix A.1.1 (count distinct patients with diagnosis "family history of malignant neoplasm of breast" and admit time within last 90 days from the benchmark's reference time).
- gold answer: [[1]]
```

### Scoring standard

```md
### Scoring
Official evaluation is two-stage:
1) Simulation-validator gate (LLM-as-a-judge): a completed interaction trace is first checked by the simulation validator; traces marked with user errors are re-run.
2) IncreQA task scoring (deterministic rule-based): execute the SQL query generated by the agent (parsed from input to the sql execute tool), compare the SQL result with the ground-truth SQL result, and mark success/failure. Up to 100 returned rows are checked.

Benchmark-level aggregate metrics (Section 5.1):
- SR-k: average success rate across k i.i.d. trials.
- Pass@k: solved in at least one of k trials.
- Pass∧k: solved in all k trials.
- Gap-k: Pass@k - Pass∧k.
The paper sets k=5 for reported main results.

### Evaluation Dimensions
- Conversation-context retention under incremental constraints.
- SQL execution correctness against GT SQL outputs (all accumulated constraints must be reflected).
- Trace validity under simulation-validator rule compliance.
- Robustness across stochastic user trajectories (SR-5, Pass@5, Pass∧5, Gap-5).

### Judge Prompt
The paper provides the full prompt for the simulation validator (Appendix A.4, Tables 6-7):

System prompt (Table 6):
"Your task is to determine whether [USER] accurately followed the provided rules and user instruction during their conversation with [DB AGENT]. Errors are defined as any deviations from the rules or user instruction. You must carefully review the rules, user instruction, conversation between [USER] and [DB AGENT], and the gold SQL query to identify any errors made by [USER]."

Input prompt template (Table 7):
{user_system_prompt}
Conversation:
{conversation}
Gold SQL:
{gold_sql}
Types of common user errors:
- The user gives away their goals all at once in the same turn.
- The user acts like a DB agent or AI assistant instead of the user (e.g., writing, reviewing, or executing SQL queries, calling external APIs, or responding to the DB agent in a machine assistant way).
- The user asks for information that is slightly different from what is specified in the instruction.
- The user confirms values that differ from those in the gold SQL, unless specified otherwise in the instruction.
- The user mentions information beyond the instruction, including related or unrelated details not specified.
- The user does not provide all the detailed conditions specified in the instruction before ending the conversation.
- The user does not provide all the detailed conditions specified in the predicates of the gold SQL, either explicitly or implicitly, before ending the conversation.
- The user does not double-check with the DB agent to see if the agent's final answer satisfies all the information the user provided before ending the conversation.
- The user violates any other rules specified in the rules or the user instruction.
You must respond in JSON format with the following fields:
- explanation
- broken_rule
- evidence
- result ("user_error" or "no_error")
```

---

## 1.2 Task: Adaptive Query Refinement (AdaptQA)

This task is to handle conditional conversational branching where the query goal changes based on intermediate retrieval outcomes (for example, fallback to generic drug names if the original value is absent).

### Task type
Interactive QA + Conditional Planning + Text-to-SQL Generation

```md
### Instruction
Given an EHR question-answering conversation with ambiguous intent, adapt the query plan at runtime based on intermediate tool/SQL results. If the current path fails (e.g., no matching records), follow the user's conditional refinement flow, perform value mismatch resolution, and continue until reaching a valid final answer or an instruction-defined stopping condition.
### Input
[Initial vague user query], [multi-turn conditional user responses], [database schema/tools over MIMIC-IV* or eICU*], [optional external clinical knowledge via web search].
### Output
[Final answer based on conditionally adapted retrieval/query steps], with SQL/tool usage aligned to the branch taken in the dialogue.
```

### Task example

```md
### Example
Appendix A.1.2 explicit sample task instance (AdaptQA):
- task id: 12
- task type: adapt
- db id: mimic iv star
- instruction: user asks for prescription timing for carbamazepine after first epilepsy diagnosis; if carbamazepine is absent, fall back to other epilepsy medication classes; if none exist, end conversation.
- gold sql: provided explicitly in Appendix A.1.2 with branching CTE logic (carbamazepine-first, else alternative epilepsy medications).
- gold answer: [['2100-10-12 20:00:00']]
```

### Scoring standard

```md
### Scoring
Official evaluation is two-stage:
1) Simulation-validator gate (LLM-as-a-judge): a completed interaction trace is first checked by the simulation validator; traces marked with user errors are re-run.
2) AdaptQA task scoring (deterministic rule-based): evaluate correctness from the content inside <answer></answer> tags in the agent's user-facing response. Success requires strict match with the annotated GT answer that reflects final intent after refinements.

AdaptQA-specific notes from Appendix A.6.2:
- This answer-level evaluation is used because tasks can require clinical reasoning beyond direct SQL retrieval.
- For numerical answers, instructions require word form (e.g., "ten" instead of "10") to avoid numeral/word mismatch artifacts.

Benchmark-level aggregate metrics (Section 5.1):
- SR-k, Pass@k, Pass∧k, Gap-k (with k=5 in the paper).

### Evaluation Dimensions
- Conditional branch handling and goal adaptation after intermediate results.
- Final answer correctness in <answer> tags against deterministic GT answer.
- Value-mismatch resolution quality (including fallback strategies when initial value/path fails).
- Trace validity under simulation-validator rule compliance.
- Robustness across stochastic user trajectories (SR-5, Pass@5, Pass∧5, Gap-5).

### Judge Prompt
The paper provides the full prompt for the simulation validator (Appendix A.4, Tables 6-7):

System prompt (Table 6):
"Your task is to determine whether [USER] accurately followed the provided rules and user instruction during their conversation with [DB AGENT]. Errors are defined as any deviations from the rules or user instruction. You must carefully review the rules, user instruction, conversation between [USER] and [DB AGENT], and the gold SQL query to identify any errors made by [USER]."

Input prompt template (Table 7):
{user_system_prompt}
Conversation:
{conversation}
Gold SQL:
{gold_sql}
Types of common user errors:
- The user gives away their goals all at once in the same turn.
- The user acts like a DB agent or AI assistant instead of the user (e.g., writing, reviewing, or executing SQL queries, calling external APIs, or responding to the DB agent in a machine assistant way).
- The user asks for information that is slightly different from what is specified in the instruction.
- The user confirms values that differ from those in the gold SQL, unless specified otherwise in the instruction.
- The user mentions information beyond the instruction, including related or unrelated details not specified.
- The user does not provide all the detailed conditions specified in the instruction before ending the conversation.
- The user does not provide all the detailed conditions specified in the predicates of the gold SQL, either explicitly or implicitly, before ending the conversation.
- The user does not double-check with the DB agent to see if the agent's final answer satisfies all the information the user provided before ending the conversation.
- The user violates any other rules specified in the rules or the user instruction.
You must respond in JSON format with the following fields:
- explanation
- broken_rule
- evidence
- result ("user_error" or "no_error")
```

---
