# DischargeMe

- **Paper**: Discharge summary generation
- **Data**: MIMIC-III / MIMIC-IV discharge summaries
- **Repo**: `teanalab/DischargeMe` (GitHub, may be private)
- **Priority**: P1

## Tasks

1. **Brief Hospital Course Generation** — generate BHC section of discharge summary
2. **Discharge Instructions Generation** — generate patient-facing instructions

## Data Source

- `mimiciv_note.discharge` — discharge summaries
- Relevant sections: Brief Hospital Course, Discharge Instructions

## Construction

1. Extract BHC sections from discharge summaries
2. Task input: preceding clinical notes + structured data
3. Task output: BHC or discharge instructions text

## Access

If the teanalab/DischargeMe repo is private:
- Request access from authors
- Alternatively: construct from scratch using MIMIC-IV discharge summaries
- Extract BHC section splits using regex on discharge notes

## Related Summary Files

- `summaries/2025_bridge_*_benchmark_summary.md`
