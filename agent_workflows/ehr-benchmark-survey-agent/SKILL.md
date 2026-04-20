---
name: ehr-benchmark-survey-agent
description: Use when the task is to read an EHR paper, identify all benchmark or dataset evaluations, rewrite them into the survey Markdown format in `summaries/`, verify task-example fidelity, and update the local benchmark registry so future papers can be processed consistently.
---

# EHR Benchmark Survey Agent

This is a repo-local workflow pack for stable benchmark extraction from EHR papers.

Use it when the user gives:
- a paper URL, DOI landing page, PubMed / PMC page, publisher page, arXiv link, PDF link, or local paper file
- a request to summarize benchmark or dataset sections
- a request to extract task definitions or instructions
- a request to update the running EHR benchmark catalog

## Primary goal

Produce a survey-ready Markdown summary that is structurally consistent across papers, then update the local registry of benchmark names and sources.

## Output files

- Survey summary: usually create one paper-specific Markdown file under `summaries/`, typically `summaries/<paper_key>_benchmark_summary.md`.
- Cached paper assets: usually `papers/<paper_key>/source.pdf`, `papers/<paper_key>/source.txt`, and `papers/<paper_key>/metadata.json`.
- Example-search audit report when needed: usually a Markdown report under `reports/`.
- Registry update: edit `/Users/cometp/Documents/ehrBenchmarkSurvey/registry/ehr_benchmark_registry.yaml`.
- Optional repo-level follow-up: update reports such as `/Users/cometp/Documents/ehrBenchmarkSurvey/reports/benchmark_taxonomy.md` if a new alias, benchmark family, or organizational pattern materially changes the current taxonomy.

## Automation entrypoint

Use the script:

- `/Users/cometp/Documents/ehrBenchmarkSurvey/scripts/ehr_benchmark_pipeline.py`

Standard command flow:

1. Bootstrap a new paper workspace:
   - `python3 scripts/ehr_benchmark_pipeline.py bootstrap "<paper_url>"`
2. Fill the generated summary file with the benchmark analysis.
3. Audit example-search coverage before registry sync:
   - `python3 scripts/ehr_benchmark_pipeline.py audit-examples "<summary_path>"`
4. Sync benchmark names into the registry:
   - `python3 scripts/ehr_benchmark_pipeline.py sync-registry "<summary_path>"`

## Standard workflow

1. Run the bootstrap command to create the standard file layout.
   - The input does not need to be arXiv. Prefer the most canonical paper URL available:
     - publisher / journal page when available
     - PubMed Central (PMC) full-text page when available
     - PubMed abstract page when it provides cleaner metadata than the publisher landing page
     - DOI landing page
     - arXiv / e-print page
     - direct PDF link
   - If multiple URLs point to the same paper, keep the summary's `paper_url` aligned to the most stable canonical page rather than the transient PDF URL.
2. Inspect the existing registry before starting analysis.
   - Also search existing `summaries/*.md` and, when relevant, `reports/benchmark_taxonomy.md` for the benchmark family or obvious aliases.
   - If a benchmark already appears in the registry or taxonomy, preserve the current canonical naming unless the new paper provides stronger benchmark-level evidence.
3. Read the paper PDF, not only the abstract.
   - Also skim the cached `papers/<paper_key>/source.txt` early. It is often the fastest way to locate benchmark names, appendix sections, figures, tables, and linked official URLs before doing a slower full read.
4. Identify every benchmark used in evaluation, not just the headline benchmark.
5. Separate:
   - newly proposed benchmark(s)
   - reused public benchmark(s)
   - released variants / subsets / difficulty splits
   - in-distribution vs out-of-distribution benchmarks
6. For each benchmark, extract:
   - benchmark-level description
   - benchmark naming discrepancies between the paper and the released official artifact, if any
   - source data system
   - task families
   - task list
   - task construction details, including how the task is formed from the source data when stated
   - task instruction text if available
   - task example if available in the appendix, supplement, or linked official artifact
   - model input shape and required output schema
   - gold / target answer form when available
   - scoring criteria / evaluation metric details
   - full judge prompt if the paper uses LLM-as-a-judge and the prompt is provided
   - metric
   - any split or sample-count information
7. Re-run example search using the policy in `references/example_search_policy.md`.
   - Do not stop at the first missing-example signal.
   - Search the main paper, appendix, supplement, figures, tables, captions, supplementary PDFs, and any linked official dataset / code artifact named by the paper.
   - When the paper links to official benchmark artifacts on Hugging Face, GitHub, PhysioNet, or an official project website, inspect those artifacts as part of the default search path rather than treating them as optional follow-up.
   - Treat official task files, scenario files, preprocessing scripts, and dataset-building code as first-class evidence. They often expose the true instruction text, field order, label vocabulary, and gold-target construction even when the paper prints no example.
   - If the paper contains a benchmark-family example but does not attribute it to one normalized subtask, keep the example with an explicit provenance note instead of marking the task as example-free.
   - Focus on preserving the full interaction flow, especially the concrete input and output, even when the original format does not match the survey template cleanly.
   - If the only official evidence is a synthetic prompt template, copy the full template into the summary instead of replacing it with a one-line description.
   - If an appendix section publishes a full prompt or answer-format specification, reproduce the full appendix content in the relevant block rather than leaving only a section reference.
   - In any `Task example` or prompt block, do not paraphrase the sample itself. Keep original wording from the paper / appendix / supplement / official artifact, allowing only minimal formatting cleanup such as line-break compaction or bullet indentation.
   - If the underlying dataset is gated or credentialed, still inspect the public landing page, README, and released construction code. Use those public materials to document exact task construction and access limits instead of leaving the task structurally vague.
   - If the paper name and the official artifact name disagree, reconcile them explicitly in the benchmark description rather than silently choosing one.
8. Normalize the output into the survey format using `references/output_template.md`.
   - Keep both `Workflow Notes` and `Verifier Notes` near the top of the summary.
   - In `Workflow Notes`, record the exact search path, normalization choices, naming discrepancies, and any gated-access limitations.
   - In `Verifier Notes`, record what is directly supported, what is normalized, what is inferred, and what remains unavailable.
9. Mark inferred fields explicitly when the paper does not state them.
10. If appendix tables have line-wrap or alignment issues, use the task inventory table as the canonical list and map instructions by semantic alignment.
11. Run the verifier stage using `references/verifier_checklist.md`.
12. Run `audit-examples` before touching the registry.
   - Treat the audit report as a trigger for re-checking search depth, not as ground truth by itself.
   - If `audit-examples` still flags a missing-example count, grep the final summary for the actual placeholder phrase before assuming the count is real.
13. Update the registry:
   - append new benchmark names if unseen
   - add the paper to `source_papers` for existing benchmarks if already present
   - keep a single canonical name per benchmark
14. Run a final self-check before finishing:
   - task count in the summary matches the paper
   - benchmark count matches the paper
   - registry entries are deduplicated by canonical name
   - every task section states example provenance and search depth, or explicitly states why no example was found after re-search
   - every task section makes it obvious what source dataset the task comes from, how the task is constructed, what the model sees, what the model must output, what counts as the gold / reference answer, and how the task is evaluated
   - every evaluation section is either quoted/paraphrased from the paper or explicitly marked unavailable
   - workflow notes and verifier notes do not contain stale statements left over from an earlier weaker search pass
   - if the paper introduces a new alias or benchmark family that changes repo-level organization, update the relevant report such as `reports/benchmark_taxonomy.md`

## Normalization rules

- Do not assume the source paper is on arXiv. The workflow must handle journal articles, conference proceedings, PMC full text, DOI landing pages, and direct PDFs.
- Prefer stable bibliographic metadata from the canonical paper source. If title/year differ across mirrors, use the publisher/PMC/PubMed version unless there is a strong reason not to.
- Keep dataset names as they appear in the paper unless there is a widely accepted canonical form.
- If the paper label and the released official artifact label differ, preserve the paper label in the section heading but add an explicit discrepancy note describing the official artifact name and what evidence supports the mapping.
- If the benchmark already exists in the local registry or taxonomy under a stable canonical name, prefer preserving that canonical entry and recording the current paper's surface form as an alias or discrepancy note rather than silently splitting the benchmark into a new canonical entry.
- Use title case for benchmark headings.
- Preserve original task wording in `Instruction` when available.
- `Input` and `Output` may be normalized into survey-style placeholders if the paper only provides one-line instructions.
- When the source provides enough information, make the task block self-contained: a reader should be able to tell the source dataset, task construction, model input, required output, gold / target answer form, and evaluation rule at a glance.
- Use the example-search hierarchy in `references/example_search_policy.md`.
- If the paper provides an actual task example in the main body, appendix, supplement, figure, table, or caption, use that example in the task section.
- If the paper provides a benchmark-family example but not an exact subtask match, keep it with a provenance caveat instead of discarding it.
- If the paper itself has no worked example, continue to linked official artifacts referenced by the paper, such as dataset cards, benchmark homepages, supplemental repositories, and source code readmes.
- Treat official repositories and data hosts named by the paper as first-class evidence sources:
  - Hugging Face dataset cards, example rows, `README.md`, prompt templates, and processing scripts
  - GitHub repositories, especially `README.md`, `examples/`, `data/`, `scripts/`, benchmark configs, and scenario files
  - PhysioNet project pages, dataset cards, task pages, sample files, and released code or benchmark documentation
- If the only public evidence is a construction script, use that script to recover the exact prompt definition, source columns, section-splitting rules, field order, label semantics, and gold-target mapping.
- If one of these official artifacts is gated or requires login / credentialed access, record that fact explicitly and stop short of fabricating content from memory.
- For gated datasets with public code but non-public rows, document the exact construction logic and say that no public instance row can be reproduced without credentialed access.
- Preserve concrete example input and output as faithfully as possible. Do not over-normalize away useful interaction details.
- If a concrete sample is unavailable but a full official prompt template is available, include that full template and label it clearly as a prompt template rather than as a dataset instance.
- If an appendix publishes a multi-part prompt (for example `Part I`, `Part II`, `Answer Format`), copy the full text of each applicable part into the summary.
- If the released artifact turns one source task into several benchmark variants, explain the transformation explicitly, for example:
  - discriminative classification from `(premise, hypothesis) -> label`
  - generative reformulation from `premise -> gold hypothesis`
  - structured EHR row serialized into newline-separated `key: value` fields
- Sample blocks should be source-faithful. Do not rewrite dataset instances in your own words.
- If no explicit task example exists after the full search pass, state that explicitly in the task section and record the search depth that was attempted. Do not fabricate an example.
- After the task example, add the scoring-standard block.
- If evaluation uses an LLM judge and the paper provides the judge prompt, include the full prompt and list the evaluation dimensions.
- If the paper mentions judge-based evaluation but does not provide the full prompt, say that the full prompt is not explicitly provided and only summarize the dimensions/criteria that are actually stated.
- Do not invent sample counts, annotation details, or language if the paper does not state them. If needed, write `inferred` or `not explicitly stated`.
- When a benchmark is structured EHR converted to free text, say so explicitly instead of calling it a native clinical note dataset.
- The verifier stage is mandatory: every non-trivial claim in the summary should be traceable to the paper text, appendix, figure, table, or clearly labeled as an inference.
- Keep the final summary aligned with the current repo conventions: a top-of-file `Workflow Notes` section, a top-of-file `Verifier Notes` section, and a completed example/scoring block for every task.

## Registry rules

Read `/Users/cometp/Documents/ehrBenchmarkSurvey/agent_workflows/ehr-benchmark-survey-agent/references/registry_update_rules.md` before editing the registry.

## Verifier

Read `/Users/cometp/Documents/ehrBenchmarkSurvey/agent_workflows/ehr-benchmark-survey-agent/references/verifier_checklist.md` before finalizing a summary.

## Example Search Policy

Read `/Users/cometp/Documents/ehrBenchmarkSurvey/agent_workflows/ehr-benchmark-survey-agent/references/example_search_policy.md` before finalizing any `Task example` block.

## Template

Use `/Users/cometp/Documents/ehrBenchmarkSurvey/agent_workflows/ehr-benchmark-survey-agent/references/output_template.md` as the default formatting scaffold.
