# MIMIC-IV Report

- **Paper**: EHR-R1 (2025)
- **Data**: MIMIC-IV radiology reports
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Tasks

Three radiology report summarization tasks:
1. **Ultrasound Summarization** — generate findings summary
2. **CT Summarization** — generate impression from CT report
3. **MRI Summarization** — generate impression from MRI report

## Required MIMIC-IV Tables

- `mimiciv_note.radiology` — radiology reports (filter by `note_type`)
- `mimiciv_hosp.admissions` — link to admissions

## Construction

1. Filter radiology reports by modality (US/CT/MRI)
2. Extract "Findings" and "Impression" sections
3. Task: given Findings, generate Impression

## Related Summary Files

- `summaries/2025_ehr_r1_*_benchmark_summary.md`
