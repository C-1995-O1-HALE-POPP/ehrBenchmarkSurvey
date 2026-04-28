# MIMIC-IV CDM

- **Paper**: EHR-R1 (2025) / BRIDGE (2025)
- **Data**: MIMIC-IV clinical database
- **Access**: PhysioNet credentialed (user has local MIMIC-IV)
- **Priority**: P1

## Task Description

Clinical Decision Making: predict main disease diagnosis and ICD-level diagnosis from structured MIMIC-IV records. Two subtasks:
1. **Main Disease Diagnoses** — primary diagnosis classification
2. **ICD Code Diagnoses** — ICD-10 code prediction

## Data Construction

Uses the MIMIC-IV CDM (Common Data Model) format. Needs:
- `mimiciv_hosp.patients` — patient demographics
- `mimiciv_hosp.admissions` — admission records
- `mimiciv_hosp.diagnoses_icd` — ICD diagnoses
- `mimiciv_hosp.d_icd_diagnoses` — ICD code dictionary
- `mimiciv_hosp.labevents` — lab results (optional)
- `mimiciv_hosp.procedures_icd` — ICD procedures (optional)

## Construction Steps

1. Identify index admissions (first admission per patient or specified criteria)
2. Extract diagnosis labels from `diagnoses_icd` table
3. Build feature vectors from demographics, prior diagnoses, lab values
4. Format as text prompts: "Patient: 65yo M with HTN, DM... Diagnosis:"

## Related Summary Files

- `summaries/2025_ehr_r1_a_reasoning_enhanced_foundational_language_model_for_electronic_health_record_analysis_benchmark_summary.md`
- `summaries/2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text_benchmark_summary.md`
