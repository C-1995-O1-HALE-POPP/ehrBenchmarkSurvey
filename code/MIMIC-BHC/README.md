# MIMIC-BHC

- **Paper**: BRIDGE (2025)
- **Data**: MIMIC-III discharge summaries
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Task

Brief Hospital Course Summarization: generate a concise BHC section summarizing the patient's hospital stay.

## Required MIMIC-III Tables

- `MIMIC3.NOTEEVENTS` — discharge summaries (CATEGORY = 'Discharge summary')
- Extract "Brief Hospital Course" section

## Construction

1. Filter MIMIC-III for discharge summaries
2. Parse sections to extract BHC text (gold summary)
3. Use preceding history/physical/exam notes as input context
4. Task: given clinical notes → generate BHC

## Related Summary Files

- `summaries/2025_bridge_*_benchmark_summary.md`
