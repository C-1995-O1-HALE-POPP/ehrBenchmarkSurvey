# NoteExtract

- **Data**: MIMIC care plan notes
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Task

Structured Extraction from Care Plan Note: extract structured clinical information (diagnoses, medications, procedures, follow-up plans) from care plan notes.

## Required Data

- `mimiciv_note.discharge` or care plan notes
- Parse care plan sections

## Construction

Extract structured fields from semi-structured care plan text using:
1. Section header parsing
2. Entity extraction from each section
3. Output as structured JSON

## Related Summary Files

- `summaries/2025_ehr_r1_*_benchmark_summary.md`
