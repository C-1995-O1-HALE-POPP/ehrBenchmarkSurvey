# Example Search Policy

Use this policy whenever a summary needs a `Task example` block.

## Goal

Prefer a faithful worked example over a clean but empty template. Record the closest official example you can verify, and preserve the original input and output as much as possible.

## Search order

1. Paper-local evidence
   - Search the main paper, appendix, supplement, figures, tables, captions, and case studies.
   - Search for markers such as `Example`, `Case`, `Figure`, `Table`, `interaction`, `trace`, `workflow`, `sample`, `prompt`, `input`, and `output`.
2. Linked official artifacts named by the paper
   - Follow only official artifacts directly referenced by the paper or supplement, such as dataset homepages, benchmark repositories, released code, data cards, task pages, or competition pages.
   - Prefer README examples, dataset card examples, official demo traces, benchmark task descriptions with concrete I/O, and released task JSON / JSONL / YAML / XML files.
   - Inspect official preprocessing scripts, scenario files, configs, and data-building code when they exist. These are often the only public source for the exact prompt definition, input field order, gold label semantics, and task-construction transform.
3. Public companion material for gated datasets
   - If the underlying rows require credentialed access, still read the public landing page, dataset card, access notes, benchmark README, and released preprocessing code.
   - Use those public materials to recover the exact task structure even when no public patient/report/example row can be copied.
4. Closely related source benchmark material
   - If the current paper reuses a benchmark but does not show an example, use the source benchmark paper or official source benchmark artifact.
   - Mark clearly that the example comes from the reused source benchmark rather than the current paper.

## Recording rules

- Keep the full interaction when possible:
  - user question / task instruction
  - context or patient record snippet
  - tool calls or SQL if present
  - ground-truth answer, target label, or expected output
- If the only available official artifact is a prompt template, copy the full template and label it as a template rather than as a concrete dataset instance.
- If the source publishes a multi-part appendix prompt, answer format, or agent protocol, copy all relevant parts in full.
- If only part of the interaction is available, preserve the most concrete pieces and say what is missing.
- If the paper shows a benchmark-family example without mapping it to a normalized subtask, keep it as a benchmark-family exemplar with a provenance note.
- If the example is visually messy because it came from a figure or multi-column PDF, keep the important input/output content and note that formatting was compacted.
- If the only public evidence is a preprocessing script, record the script-derived task construction explicitly:
  - source columns or source sections used
  - how the prompt input is serialized
  - which field becomes the gold output
  - any label mapping such as `0/1/2` or `True/False`
- If the paper name and the official artifact name differ, keep both visible and explain the mapping.
- Do not paraphrase a sample or prompt template. Keep original wording whenever possible, allowing only line-wrap repair, whitespace cleanup, or clearly marked omission of irrelevant boilerplate.
- Never fabricate missing values, tool traces, or gold answers.

## Output expectations

Each task example block should answer:

- Where the example came from
- How deep the search went
- What source dataset / artifact and task construction produced the example
- What the concrete input was
- What the model is expected to output
- What the gold / reference answer or target is, if the source exposes it
- Whether the example is a public dataset instance, a prompt template, or a script-derived task-construction note for a gated source

Use compact language such as:

- `Paper figure example; not explicitly attributed to one normalized subtask.`
- `Source benchmark example reused because the current paper does not publish a worked instance.`
- `Official companion prompt template copied in full because no concrete instance is published.`
- `Searched paper, appendix, supplement, linked official artifact, and released preprocessing code; no public worked example found.`
- `Underlying source rows are credentialed; task structure reconstructed from the public dataset card and official preprocessing script.`

## Failure condition

Do not write `No explicit task example...` until you have checked all applicable levels above, including released preprocessing scripts when they exist.
