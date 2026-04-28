# MIMIC-IV Billing Code

- **Paper**: Various EHR papers
- **Data**: MIMIC-IV clinical notes + ICD codes
- **Access**: PhysioNet credentialed (user has local MIMIC-IV)
- **Priority**: P1

## Task

ICD-10 Code Extraction from Clinical Note: given a discharge summary or clinical note, predict the ICD-10 billing codes.

## Required MIMIC-IV Tables

- `mimiciv_note.discharge` — discharge summaries
- `mimiciv_hosp.diagnoses_icd` — ICD diagnoses (ground truth labels)
- `mimiciv_hosp.d_icd_diagnoses` — ICD dictionary (code → description)

## Construction

1. Join discharge notes with admission-level ICD codes via `hadm_id`
2. Create (note_text, [ICD_codes]) pairs
3. Split by patient or admission
4. Format as text: "Note: {...} → ICD codes: A41.9, I10, E11.9"

## Related Summary Files

- `summaries/2025_ehr_r1_*_benchmark_summary.md`
