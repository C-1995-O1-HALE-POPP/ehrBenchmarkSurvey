# Registry Update Rules

The registry file is:

- `/Users/cometp/Documents/ehrBenchmarkSurvey/registry/ehr_benchmark_registry.yaml`

## One benchmark, one canonical entry

Each benchmark should appear once under a canonical name.

Good examples:
- `EHR-Bench`
- `MIMIC-IV-CDM`
- `EHRSHOT`

## Update policy

When processing a new paper:

1. Search the registry for the benchmark name and obvious aliases.
2. If the benchmark already exists:
   - keep the existing `canonical_name`
   - append the current paper under `source_papers` if not already listed
   - update `notes` only if the new paper adds stable benchmark facts
3. If the benchmark is new:
   - create a new entry
   - include `canonical_name`, `aliases`, `benchmark_type`, `source_system`, `task_families`, and `source_papers`

## Naming guidance

- Prefer the paper's official benchmark name.
- Keep aliases minimal and useful.
- Do not create separate entries for formatting variants such as "Markdown-formatted EHRSHOT" if it is still the same benchmark.

## Provenance guidance

For each benchmark entry, store:
- where the benchmark originally comes from, if known
- which papers in this repo have already used or discussed it

## Minimal schema

```yaml
benchmarks:
  - canonical_name: "Example-Benchmark"
    aliases:
      - "Example Benchmark"
    benchmark_type: "risk prediction"
    source_system: "MIMIC-IV"
    task_families:
      - "risk prediction"
    source_papers:
      - title: "Paper title"
        year: 2026
        url: "https://..."
        role_in_paper: "primary benchmark"
    notes: "Optional stable notes."
```

