# Survey Output Template

Use this template for each benchmark extracted from a paper.

```md
## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` or equivalent local workflow.
- Record the exact search path used for this paper: paper body, appendix, supplement, cached source text, and every official artifact named by the paper that was inspected.
- Record normalization choices, paper/artifact naming discrepancies, and any gated-access limitations.
- Before syncing the registry, run:
  - `python3 scripts/ehr_benchmark_pipeline.py audit-examples "<summary_path>"`
  - `python3 scripts/ehr_benchmark_pipeline.py sync-registry "<summary_path>"`

## Verifier Notes

- Benchmark existence: [directly stated / normalized / mixed]
- Task mapping: [directly stated / normalized / mixed]
- Instruction fidelity: [verbatim / normalized / mixed]
- Example fidelity: [paper example / official artifact / source benchmark / no public example after full search]
- Scoring fidelity: [paper-local metric / rubric / unavailable]
- Judge prompt fidelity: [full prompt available / partially described / unavailable]
- Inference labeling: [what was inferred or marked not explicitly stated]

## [section_id] [Benchmark Name]

[Benchmark Name] is a [language if known] benchmark designed for [main purpose / evaluation setting]. It is derived from [source system / institution / paper]. The benchmark covers [task families / scope]. [Add split, sample count, or construction notes if stated in the paper.]

- **Language:** [English / Chinese / Multilingual / inferred / not explicitly stated]
- **Clinical Stage:** [diagnosis / treatment / ICU / longitudinal hospital course / etc.]
- **Source Clinical Document Type:** [general EHR note / structured EHR serialized into free text / discharge summary / radiology report / etc.]
- **Clinical Specialty:** [specialty or multi-specialty]
- **Application Method:** [public benchmark / benchmark introduced in the paper / access method if stated]

---

## [section_id].[task_id] Task: [Task Name]

This task is to [plain-language task description].

### Task type
[Decision Making / Risk Prediction / Classification / Extraction / Generation / QA / etc.]

```md
### Instruction
[Original task instruction from the paper if available]
### Input
[Survey-normalized input description]
### Output
[Survey-normalized output description]
```

### Task example

- If the paper provides an explicit worked example, appendix sample, figure, table, interaction trace, or exact task instance, include it here in compact form.
- If the paper provides only a benchmark-family example, keep it and explain the provenance caveat.
- If the paper itself has no example, continue to linked official artifacts and source benchmark materials before declaring failure.
- Preserve concrete input and output even if the original formatting is messy.
- Do not paraphrase a sample or prompt template. Copy the original wording from the paper / appendix / supplement / official artifact, allowing only minimal formatting cleanup such as line-wrap repair or indentation.
- If no dataset instance is available but a full official prompt template is available, include the full template here and label it explicitly as a prompt template.
- If an appendix prompt is split into multiple parts (for example `Part I`, `Part II`, `Answer Format`), include every applicable part in full instead of leaving only a section reference.
- Use the surrounding prose plus the fields below to make the task legible at a glance: source dataset / artifact, task construction, concrete model input, required output, gold / target answer form if available, and evaluation rule.

```md
### Example Provenance
[Paper / appendix / supplement / official dataset card / official repo / source benchmark paper]
### Search Depth
[Paper only / paper + supplement / paper + supplement + linked artifact / paper + linked artifact + source benchmark]
### Example Type
[Concrete dataset instance / prompt template / benchmark-family exemplar]
### Source Dataset / Artifact
[Exact dataset split, scenario file, appendix section, or official artifact that produced this example]
### Task Construction
[How the task is built from the source data, if stated]
### Fidelity
[Verbatim except line-wrap cleanup / lightly reformatted for readability / exact copy]
### Example
[Quoted task example or prompt template from the source]
### Example Input
[Concrete input / context / interaction trace]
### Example Output
[Concrete answer / label / SQL / action / target output]
### Gold / Reference Answer
[Gold label, target text, reference SQL, expected tool action, or "Not explicitly provided in the source."]
```

### Scoring standard

- Describe the official scoring rule used for this task.
- If the paper uses a deterministic metric, describe the metric and what counts as correct.
- If the paper uses an LLM judge, include the full judge prompt when it is explicitly available.
- If the full judge prompt is not available, state that explicitly and only summarize the stated dimensions or rubric.

```md
### Scoring
[Metric / rubric / exact-match / AUROC / F1 / human evaluation rule / etc.]
### Evaluation Dimensions
[List the dimensions, criteria, rubric axes, or write "Not explicitly provided in the paper."]
### Judge Prompt
[Full judge prompt if explicitly provided; otherwise write "The full judge prompt is not explicitly provided in the paper."]
```
```

## Required checks

- The file includes both `Workflow Notes` and `Verifier Notes` near the top.
- Benchmark-level paragraph is specific to the paper, not generic.
- If task instructions come from appendix tables with broken line wrapping, mention the mapping assumption in a note near the top of the output file.
- If the paper contains multiple benchmarks, keep them all in one paper summary file unless the user asks otherwise.
- For reused benchmarks, distinguish between the benchmark itself and the way the current paper reformats or evaluates it.
- If the paper provides an appendix example, prefer that example over an invented normalization.
- If the paper provides only a figure/table/case example, keep it instead of discarding it for formatting reasons.
- If the current paper omits examples for a reused benchmark, check linked official artifacts or the source benchmark before concluding that no example exists.
- If the source only provides a full prompt template, keep that template in full rather than reducing it to a one-line description.
- If the paper or appendix publishes a full judge / agent / answer-format prompt, include the full prompt text rather than only citing the appendix section.
- If no task example exists after the full search pass, say so explicitly instead of synthesizing one.
- If the evaluation is judge-based, include the full prompt only when it is actually present in the paper or appendix.
- If the evaluation prompt is missing, explicitly record that absence.
- Run `audit-examples` before registry sync and reconcile any stale `No explicit task example` placeholders.
