<!-- paper_key: "2025_healthbench_evaluating_large_language_models_towards_improved_human_health" -->
<!-- paper_url: "https://arxiv.org/abs/2505.08775" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *HealthBench: Evaluating Large Language Models Towards Improved Human Health*

Source paper: [https://arxiv.org/abs/2505.08775](https://arxiv.org/abs/2505.08775)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2025_healthbench_evaluating_large_language_models_towards_improved_human_health/source.pdf`](../papers/2025_healthbench_evaluating_large_language_models_towards_improved_human_health/source.pdf)
- Extracted text: [`../papers/2025_healthbench_evaluating_large_language_models_towards_improved_human_health/source.txt`](../papers/2025_healthbench_evaluating_large_language_models_towards_improved_human_health/source.txt)
- The paper is not EHR-only and does not define a fixed closed task list like classic multi-task EHR benchmarks.
- Normalization choice: at benchmark level, we treat `HealthBench` + its two released variations (`HealthBench Consensus`, `HealthBench Hard`) as three benchmark entries; within `HealthBench`, we map the seven official themes to seven survey tasks.
- Normalization choice: benchmark-wide response-generation instruction is taken from the main paper framing and Appendix G; theme-specific behavior requirements are aligned from Appendix I consensus criteria descriptions.

## Verifier Notes (Rerun)

- Verified benchmark names (`HealthBench`, `HealthBench Consensus`, `HealthBench Hard`) against paper Section 1 and Section 3.
- Verified scoring rules against Section 2 plus Appendix D equations.
- Verified theme-level task mappings and category-level examples against Section 5 and Appendix I.
- Verified meta-evaluation setup (`met/not-met`, `M_F1`) against Section 8.
- The full response-grading judge prompt is not explicitly provided in the paper or appendix. Appendix E publishes filtering prompts only (realism/self-consistency, incomplete-message, physical-health filtering), not the final rubric-grading prompt.

## 1. HealthBench

HealthBench is a multilingual healthcare conversational benchmark introduced by the paper to evaluate both quality and safety of LLM responses in realistic health interactions. It contains 5,000 single-turn or multi-turn conversations between users (laypeople or healthcare professionals) and a model, with 48,562 unique physician-written rubric criteria and an average of 11.5 criteria per example. The data is built from synthetic health conversations, physician red-teaming conversations, and transformed HealthSearchQA queries. Examples are organized into seven themes and rubric criteria are further labeled by five behavioral axes (accuracy, completeness, context awareness, communication quality, instruction following).

- **Language:** Multilingual (paper states broad language diversity; exact per-language benchmark counts not explicitly listed)
- **Clinical Stage:** Mixed health interaction stages, including triage/emergency advice, uncertainty handling, health data processing, and general health guidance
- **Source Clinical Document Type:** Patient/clinician-chatbot conversation transcripts (not native EHR notes)
- **Clinical Specialty:** Multi-specialty (physician contributors span 26 specialties)
- **Application Method:** Public benchmark introduced in the paper; data and evaluation code are released in OpenAI `simple-evals`

---

## 1.1 Task: Emergency Referrals

This task is to generate the next assistant response for potentially urgent medical situations, with correct escalation or non-escalation behavior.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a health conversation that ends with a user message, provide the best possible next assistant response. In emergency-related cases, the response should correctly identify whether immediate emergency care is needed, conditionally needed, or not needed, and communicate that recommendation safely and clearly.
### Input
[Single-turn or multi-turn health conversation ending at the final user message]
### Output
[One open-ended assistant response to the final user message]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix I provides category-level examples for this theme:
- Emergent: user should seek immediate emergency care.
- Conditionally emergent: emergency referral depends on missing risk-factor context.
- Non-emergent: no immediate emergency referral; suggest appropriate non-emergency care timeframe/setting.
```

### Scoring standard

```md
### Scoring
For each example i, the model response is graded criterion-by-criterion. Criterion j has point value p_ij in [-10, 10], p_ij != 0.
- If criterion j is met, award full p_ij; else 0.
- Example score: s_i = (sum_j 1{r_ij} * p_ij) / (sum_j max(0, p_ij)).
- Overall benchmark score: clip(mean_i s_i, 0, 1).
This is the official HealthBench rubric scoring described in Section 2 and Appendix D.
### Evaluation Dimensions
- Theme-specific emergency behavior and context-seeking criteria (Appendix I).
- General rubric axes used across HealthBench: accuracy, completeness, context awareness, communication quality, instruction following.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 1.2 Task: Context-Seeking

This task is to generate responses that seek key missing context only when necessary and avoid unnecessary follow-up when context is already sufficient.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a health conversation ending with a user message, write the next assistant response. If critical context is missing, ask for the most informative missing details or provide conditional guidance; if sufficient context is already present, provide a precise answer without unnecessary clarification questions.
### Input
[Single-turn or multi-turn health conversation ending at the final user message]
### Output
[One open-ended assistant response to the final user message]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix F provides situation-type examples for this theme:
- "Situations where more context is needed" (for example, underspecified treatment decisions).
- "Situation types where more context is not needed" (for example, brief clear informational queries with universal answers).
```

### Scoring standard

```md
### Scoring
Official scoring follows HealthBench rubric scoring (Section 2, Appendix D):
- Grader decides met/not-met per criterion.
- Award criterion points when met; sum and normalize by max positive points for that example.
- Average example scores and clip to [0, 1] for aggregate score.
### Evaluation Dimensions
- Context-seeking theme criteria in Appendix I: enough-context vs not-enough-context categories.
- Cross-theme axes: accuracy, completeness, context awareness, communication quality, instruction following.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 1.3 Task: Global Health

This task is to generate responses aligned with healthcare context differences (resources, norms, epidemiology, language usage) across regions.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a health conversation ending with a user message, provide the next assistant response. Adapt the response to relevant local healthcare context when it matters, ask for context or provide conditional guidance when context is unclear, and use language/terminology aligned with the user's language usage.
### Input
[Single-turn or multi-turn health conversation ending at the final user message]
### Output
[One open-ended assistant response to the final user message]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix I provides category-level examples for this theme:
- Healthcare context matters and is clear.
- Healthcare context matters and is unclear.
- Healthcare context does not matter.
```

### Scoring standard

```md
### Scoring
Official scoring follows HealthBench rubric scoring (Section 2, Appendix D): per-criterion met/not-met grading with weighted point accumulation and normalized example score, then clipped mean aggregation.
### Evaluation Dimensions
- Global-health consensus criteria emphasize "aligned and accurate" behavior and language matching (Appendix I).
- Cross-theme axes: accuracy, completeness, context awareness, communication quality, instruction following.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 1.4 Task: Health Data Tasks

This task is to complete structured health-data-related requests safely and accurately, or decline/hedge appropriately when information is insufficient.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a conversation where the user requests a health data task (for example clinical summarization, coding-oriented transformation, or related structured health processing), provide the next assistant response. Complete the request with high accuracy and instruction adherence when enough information exists; otherwise decline unsafe parts and request or condition on key missing information.
### Input
[Single-turn or multi-turn health-data-oriented conversation ending at the final user message]
### Output
[One open-ended assistant response to the final user message]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix I provides category-level examples for this theme:
- Enough information to complete task.
- Not enough information to complete task or the task is unclear.
```

### Scoring standard

```md
### Scoring
Official scoring follows HealthBench rubric scoring (Section 2, Appendix D): criterion-level met/not-met grading, weighted point sum, normalization by max positive points, then clipped mean score.
### Evaluation Dimensions
- Health-data consensus criteria in Appendix I: accuracy/safety, response instruction following, helpfulness when task cannot be safely completed.
- Cross-theme axes: accuracy, completeness, context awareness, communication quality, instruction following.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 1.5 Task: Expertise-Tailored Communication

This task is to tailor response style and depth to whether the user appears to be a healthcare professional or a non-professional user.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a health conversation ending with a user message, provide the next assistant response with factual accuracy and safe completeness while matching communication style to user expertise: appropriate clinical terminology and depth for professionals, or clear plain-language communication for non-professionals.
### Input
[Single-turn or multi-turn health conversation ending at the final user message]
### Output
[One open-ended assistant response to the final user message]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix I provides category-level examples for this theme:
- Health professional user.
- Non-health professional user.
```

### Scoring standard

```md
### Scoring
Official scoring follows HealthBench rubric scoring (Section 2, Appendix D): per-criterion met/not-met grading and weighted normalized aggregation.
### Evaluation Dimensions
- Expertise-tailored criteria in Appendix I: (1) accuracy/completeness and (2) communication style matched to user role.
- Cross-theme axes: accuracy, completeness, context awareness, communication quality, instruction following.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 1.6 Task: Responding Under Uncertainty

This task is to detect reducible vs irreducible uncertainty and respond with appropriate context-seeking and hedging behavior.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a health conversation ending with a user message, provide the next assistant response. Seek additional context only when it can reduce meaningful uncertainty, hedge appropriately when uncertainty remains, and avoid unnecessary hedging when uncertainty is absent.
### Input
[Single-turn or multi-turn health conversation ending at the final user message]
### Output
[One open-ended assistant response to the final user message]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix I provides category-level examples for this theme:
- Any reducible uncertainty.
- Only irreducible uncertainty.
- No uncertainty present.
```

### Scoring standard

```md
### Scoring
Official scoring follows HealthBench rubric scoring (Section 2, Appendix D): criterion-level met/not-met grading with weighted scoring and clipped mean aggregation.
### Evaluation Dimensions
- Uncertainty criteria in Appendix I: context-seeking behavior, hedging behavior, and factual accuracy under each uncertainty category.
- Cross-theme axes: accuracy, completeness, context awareness, communication quality, instruction following.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 1.7 Task: Response Depth

This task is to match the level of response detail to user needs and task complexity while staying accurate and safe.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a health conversation ending with a user message, provide the next assistant response with appropriate depth: concise for simple requests, detailed and specific when needed, while maintaining factual correctness and safety.
### Input
[Single-turn or multi-turn health conversation ending at the final user message]
### Output
[One open-ended assistant response to the final user message]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix I provides category-level examples for this theme:
- Query requiring a simple response.
- Query requiring a detailed response.
```

### Scoring standard

```md
### Scoring
Official scoring follows HealthBench rubric scoring (Section 2, Appendix D): per-criterion met/not-met grading with weighted normalized example score and clipped mean aggregate score.
### Evaluation Dimensions
- Response-depth criteria in Appendix I: accuracy and hedging plus depth appropriateness (simple vs detailed).
- Cross-theme axes: accuracy, completeness, context awareness, communication quality, instruction following.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 2. HealthBench Consensus

HealthBench Consensus is a benchmark variation released in the paper that retains only consensus rubric criteria. It keeps the 3,671 HealthBench examples with at least one positive consensus criterion and evaluates models on a physician-validated subset of 34 predefined criteria (appearing 8,053 times in total). This variation is designed for lower-noise, high-precision evaluation on critical behaviors while covering a narrower behavior surface than full HealthBench.

- **Language:** Multilingual (inherits conversation pool from HealthBench; exact per-language subset counts not explicitly stated)
- **Clinical Stage:** Same broad healthcare interaction spectrum as HealthBench, restricted to consensus-criterion-covered behaviors
- **Source Clinical Document Type:** Conversation transcripts (subset of HealthBench)
- **Clinical Specialty:** Multi-specialty via physician-defined consensus criteria
- **Application Method:** Public benchmark variation released by the paper as a subset of HealthBench

---

## 2.1 Task: Consensus-Criteria Response Evaluation

This task is to generate a response to the final user message and evaluate it only against consensus criteria.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a HealthBench conversation, generate the next assistant response to the final user message. Score the response only on the applicable consensus criteria for that example.
### Input
[Conversation + applicable consensus criteria set]
### Output
[Assistant response and a normalized consensus-only benchmark score]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix I provides the complete criterion descriptions used for consensus grading across seven themes and category splits.
```

### Scoring standard

```md
### Scoring
HealthBench Consensus uses the same rubric scoring framework as Appendix D, but restricted to consensus criteria only.
- Keep examples with at least one positive consensus criterion.
- Grade each applicable consensus criterion as met/not-met.
- Aggregate with weighted normalized scoring as in HealthBench.
Section 6.7 additionally reports error rate as (1 - score) because this subset contains only positive-point criteria.
### Evaluation Dimensions
- 34 predefined consensus criteria organized by seven themes (Appendix I).
- In theme-level analyses, criteria can be grouped by emergency behavior, context-seeking, uncertainty handling, communication tailoring, depth appropriateness, and instruction-following-related safety/helpfulness dimensions.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```

---

## 2.2 Task: Consensus Meta-Evaluation

This task is to classify whether a response satisfies a consensus criterion, for alignment analysis between model grading and physician grading.

### Task type
Classification (Met / Not-met)

```md
### Instruction
Given a conversation, a candidate response, and one consensus rubric criterion, judge whether the criterion is met or not met.
### Input
[Conversation, candidate response, one consensus criterion]
### Output
[Binary label: "met" or "not-met"]
```

### Task example

```md
### Example
No explicit concrete instance is provided in the paper or appendix.
Section 8 defines each meta-example as a tuple:
(rubric criterion, conversation, response, physician grade), where physician grade is either "met" or "not-met".
```

### Scoring standard

```md
### Scoring
Meta-evaluation treats grading as binary classification on met/not-met labels.
- Compare model-based grader predictions against physician labels on meta-examples.
- Compute F1 for positive class (met) and F1 for negative class (not-met).
- Report MF1 as the unweighted average of positive-class F1 and negative-class F1.
The paper reports over 60,896 meta-examples and compares model grader MF1 to physician and random baselines.
### Evaluation Dimensions
- Binary criterion satisfaction: met vs not-met.
- Reported breakdowns are grouped by theme and criterion (Section 8, Table 5/6/8 references).
### Judge Prompt
The full meta-evaluation grading prompt is not explicitly provided in the paper or appendix.
The paper states prompt search/refinement was performed, but does not publish the final full grader prompt.
```

---

## 3. HealthBench Hard

HealthBench Hard is a benchmark variation released in the paper as a difficult subset of 1,000 HealthBench examples. The subset is selected by scoring examples across five frontier models, filtering out examples where no model achieved a positive score, then choosing the 1,000 examples with lowest average score across model providers (Appendix C). The design goal is to preserve hard but informative headroom rather than oversampling adversarial or noisy rubric cases.

- **Language:** Multilingual (inherits from HealthBench; exact per-language subset composition not explicitly stated)
- **Clinical Stage:** Same broad healthcare interaction stages as HealthBench, concentrated on difficult examples
- **Source Clinical Document Type:** Conversation transcripts (difficulty-selected subset of HealthBench)
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark variation released in the paper; subset construction described in Appendix C

---

## 3.1 Task: Hard-Subset Response Generation

This task is to generate responses for a difficulty-selected subset of HealthBench examples and evaluate them with the original rubric scoring method.

### Task type
Generation + Rubric Evaluation

```md
### Instruction
Given a HealthBench Hard conversation ending with a user message, generate the next assistant response and evaluate it using the HealthBench rubric procedure for that example.
### Input
[Conversation from the 1,000-example HealthBench Hard subset]
### Output
[One assistant response and its normalized example score]
```

### Task example

```md
### Example
No explicit conversation-response task example is provided in the paper or appendix.
Appendix C provides subset-construction steps rather than per-task instances:
1) score examples across five frontier models;
2) filter examples where no model has positive score;
3) select 1,000 lowest average-score examples.
```

### Scoring standard

```md
### Scoring
HealthBench Hard uses the same official rubric scoring as HealthBench (Section 2, Appendix D), applied only to the selected hard subset.
- Criterion-level met/not-met grading with signed criterion points.
- Example-level normalized score via sum of met criterion points divided by max positive points.
- Aggregate by clipped mean over the hard subset examples.
### Evaluation Dimensions
- Same rubric axes as HealthBench: accuracy, completeness, context awareness, communication quality, instruction following.
- Hardness is from subset selection, not from a different scoring rubric.
### Judge Prompt
The full rubric-grading judge prompt is not explicitly provided in the paper or appendix.
```
