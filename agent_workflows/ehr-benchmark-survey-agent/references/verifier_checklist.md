# Verifier Checklist

This verifier stage is required before finalizing any summary.

## Goal

Reject unsupported claims early. The summary should be defensible against the paper text.

## What to verify

For every benchmark summary:

1. Benchmark existence
   - The benchmark name appears in the paper, or the summary explicitly says it is a normalization choice.
2. Task mapping
   - Each task name is either directly stated in the paper or explicitly marked as a normalization.
3. Instruction fidelity
   - `Instruction` is either copied/paraphrased from the paper or clearly labeled as normalized.
   - The task block makes the model input shape and required output schema explicit when the source provides them.
4. Example fidelity
   - If the paper, appendix, supplement, figure, or table contains a concrete task example, the summary uses that example.
   - If the paper contains only a benchmark-family example, the summary may keep it only with an explicit provenance caveat.
   - If the current paper reuses an older benchmark and does not publish a task instance, the summary should check linked official artifacts or the source benchmark material before concluding no example exists.
   - If linked official artifacts include preprocessing scripts, task JSON / JSONL files, scenario files, or benchmark configs, the summary should use those materials to recover exact task structure before concluding no example exists.
   - If the only official evidence is a prompt template, the summary should copy the full prompt template rather than summarizing it in one sentence.
   - If an appendix publishes a multi-part prompt or answer-format specification, the summary should reproduce all relevant parts in full instead of leaving only an appendix reference.
   - Sample text itself should not be paraphrased. Only minimal formatting cleanup is allowed.
   - If no example exists after the full search pass, the summary explicitly says so and records the search depth.
   - The example block makes clear what source dataset / artifact the example comes from, how the task is constructed, and what the gold / reference answer form is when the source exposes it.
   - If the underlying source rows are gated, the summary should say so explicitly and use public landing pages plus released scripts to document the exact task-construction logic.
   - If the paper name and the official artifact name differ, the summary should keep the discrepancy visible instead of silently flattening it.
5. Scoring fidelity
   - Metrics, rubric criteria, judge dimensions, and evaluation rules come from the paper.
   - Missing scoring details are explicitly marked unavailable.
6. Judge prompt fidelity
   - Include the full prompt only if the full prompt is actually present in the paper, appendix, supplement, or linked official artifact referenced by the paper.
   - Otherwise state that the full prompt is not explicitly provided.
7. Inference labeling
   - Any inferred field such as language, clinical stage, or document type is labeled `inferred` or `not explicitly stated`.
8. Internal consistency
   - `Workflow Notes`, `Verifier Notes`, and task sections agree with the final evidence state.
   - No stale note should still claim that examples were not found after the example blocks have been upgraded.

## Minimum verification pass

Before finishing:

- Re-open the relevant appendix or table for every task example included.
- Re-open any linked official artifact or source benchmark page used for an example block.
- Re-open any preprocessing script or scenario file used to reconstruct task structure.
- Re-open the section or appendix that defines metrics or rubric criteria.
- Re-check every `Judge Prompt` block against the source text.
- Re-check that each task section explains the source dataset, task construction, model input, required output, and gold / reference answer form as far as the source allows.
- Re-check every normalization assumption in `Workflow Notes`.

## Failure rules

If any of the following are true, revise the summary before syncing the registry:

- A task example is synthesized even though the paper provides none.
- A source-provided sample or prompt template is paraphrased instead of being copied faithfully.
- A task is marked as having no example before the linked official artifact or reused source benchmark has been checked when those sources are applicable.
- A task is marked as example-free even though released preprocessing code makes the task construction recoverable.
- A full appendix prompt exists but the summary leaves only a section reference or short paraphrase.
- A judge prompt is presented as complete but the paper only describes it partially.
- A benchmark variant is written as canonical without noting that it is a subset or normalization.
- A paper/artifact naming mismatch is silently ignored even though it materially affects how the task should be interpreted.
- A metric, split size, or evaluation dimension cannot be traced back to the paper.
- `Workflow Notes` or `Verifier Notes` still describe an earlier weaker search state after the summary has been upgraded.

## Output expectation

A valid summary should make it easy to answer:

- What is directly from the paper?
- What is inferred?
- What is normalized for survey consistency?
- What is unavailable in the original source?
