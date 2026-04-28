---
name: benchmark-report-maintainer
description: Periodic maintenance workflow: read all benchmark summaries, rebuild the deduped task list and taxonomy reports. Use when adding a new summary or after batch-processing several papers.
---

# Benchmark Report Maintainer

This skill covers the periodic task of syncing `reports/deduped_benchmark_tasks_list.md` and `reports/benchmark_taxonomy.md` from the latest `summaries/*.md` content.

Use it when:
- A new benchmark summary has been added to `summaries/`
- Several papers have been processed and repo-level reports are stale
- The user asks to "update the benchmark list" or "refresh the taxonomy"

## Primary goal

Keep the two repo-level reports consistent with the full benchmark inventory across all summaries, so downstream consumers (literature review, survey tables, gap analysis) always see the current state.

## Output files

- `reports/deduped_benchmark_tasks_list.md` — flat list of every benchmark and its tasks
- `reports/benchmark_taxonomy.md` — multi-dimensional taxonomy organizing all benchmarks

## Standard workflow

### Step 1: Identify the delta

Before touching either report, determine what is new:

1. Scan all `summaries/*.md` files (skip placeholders).
2. For each summary, extract every top-level `## N. BenchmarkName` heading and its `### N.x Task: TaskName` sub-headings.
3. Cross-reference each benchmark name against the current `reports/deduped_benchmark_tasks_list.md`.
4. Build two lists:
   - **New benchmarks**: benchmark names not present in the deduped task list at all.
   - **New tasks for existing benchmarks**: benchmarks already listed but with additional tasks discovered in the new summary.

If there is no delta (the summaries and reports are already consistent), report that and stop.

### Step 2: Update `deduped_benchmark_tasks_list.md`

For each new benchmark, append a block at the end of the file:

```
## BenchmarkName

- TaskName1
- TaskName2
```

For each existing benchmark with new tasks, append the new task lines under its existing block. The task names must match the summary's `### N.x Task:` heading exactly.

Do NOT remove or rename existing entries unless the user explicitly asks for dedup reorganization.

### Step 3: Update `benchmark_taxonomy.md`

For each new benchmark (and any existing benchmark that has gained new task types), assign taxonomy labels.

Read `references/taxonomy_rules.md` for the full labeling guide. The core taxonomy dimensions are:

- `task` — `MCQ`, `CLS`, `REG`, `SIM`, `EXT`, `COD`, `SUM`, `GEN`, `RET`, `SQL`, `CODE`, `CALC`, `ACT`, `MIX`
- `interaction` — `ST-S`, `ST-L`, `MT-X`, `INT`, `AGT`, `MIX`
- `source` — `EXAM`, `LIT`, `SEHR`, `NOTE`, `RAD`, `DIAL`, `WEB`, `MIX`
- `role` — `CORE`, `VAR`, `SUITE`

**Placement rule**: find the most appropriate family section (Sections 1–8) based on the benchmark's primary evaluation goal, then insert a new line in the correct alphabetical or logical position.

**Section selection guide**:
| Benchmark's primary nature | Place in section |
|---|---|
| Text-to-SQL, executable querying, agent/tool-use | §1 Executable EHR Querying |
| Clinical prediction, diagnosis, risk scores | §2 Clinical Prediction & Decision Support |
| NER, entity extraction, de-identification, coding | §3 Extraction, Coding, Normalization |
| NLI, semantic similarity, relevance | §4 Semantic Matching & NLI |
| Summarization, response generation, dialogue | §5 Summarization & Generation |
| Exam QA, MCQA, literature reasoning | §6 Knowledge QA & Exam QA |
| Safety, bias, privacy, compliance | §7 Safety, Privacy, Bias |
| Benchmark family/suite umbrella | §8 Benchmark Suites |

### Step 4: Verify

After edits, run a quick sanity check:
- Every benchmark in the new summary appears in `deduped_benchmark_tasks_list.md`
- Every new benchmark appears in `benchmark_taxonomy.md`
- No duplicate benchmark names across sections
- Task counts match expectations

## Concrete example

Given a summary that introduces `RadQA` (extractive QA from radiology reports) and `Clinical Stigmatizing Language` (multi-class classification from clinical notes):

1. **Delta check**: Neither exists in `deduped_benchmark_tasks_list.md` → both are new.
2. **Task list**: Append:
   ```
   ## RadQA
   - Extractive Question Answering

   ## Clinical Stigmatizing Language
   - Credibility & Obstinacy Classification
   - Compliance Classification
   - Descriptors Classification
   ```
3. **Taxonomy**: 
   - `RadQA`: extractive task, radiology source → §3 Extraction. Line: `task=EXT; interaction=ST-L; source=RAD; role=CORE`
   - `Clinical Stigmatizing Language`: classification, clinical notes source → §7 Safety/Compliance. Line: `task=CLS; interaction=ST-S; source=NOTE; role=CORE`
4. **Verify**: grep both reports for the new names.

## Edge cases

- **Benchmark alias collision**: if a new summary uses a different name for an already-registered benchmark (e.g., "BC5CDR-disease" vs existing "BC5CDR"), do NOT create a new entry in `deduped_benchmark_tasks_list.md`. Instead, merge tasks under the existing canonical name. Add the alias as a taxonomy line in the Comment/Known Alias format if needed.
- **Biomedical vs clinical**: benchmarks derived from PubMed/literature (not clinical notes or EHR) should still be tracked. Use `source=LIT` and place in the appropriate section.
- **Gated datasets**: the taxonomy does not encode access restrictions. Label based on the benchmark's intrinsic properties regardless of whether it requires PhysioNet/IRB access.
- **Multi-task benchmarks**: if a single benchmark header has multiple sub-tasks of different types, list all tasks under the benchmark name in `deduped_benchmark_tasks_list.md`. In taxonomy, assign the dominant `task` label that best captures the benchmark's primary evaluation goal, or use `MIX` if no single type dominates.
