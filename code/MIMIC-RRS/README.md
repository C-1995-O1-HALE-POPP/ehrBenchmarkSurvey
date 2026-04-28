# MIMIC-RRS

- **Paper**: Various
- **Data**: MIMIC radiology reports
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Task

Impression Generation from Findings: given the "Findings" section of a radiology report, generate the "Impression" section.

## Required Data

- `MIMIC3.NOTEEVENTS` — radiology reports (CATEGORY = 'Radiology')
- Or `mimiciv_note.radiology`

## Construction

1. Filter radiology reports
2. Parse "Findings" and "Impression" sections via regex
3. Task: Findings → Impression (abstractive summarization)

## Related Summary Files

- `summaries/2025_ehr_r1_*_benchmark_summary.md`
