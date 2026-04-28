# MIMIC-IV DiReCT

- **Paper**: BRIDGE (2025)
- **Data**: MIMIC-IV
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Tasks

Two diagnostic reasoning tasks:
1. **DiReCT.Dis** — Disease diagnosis from clinical text
2. **DiReCT.PDD** — Principal diagnosis differentiation

## Required MIMIC-IV Tables

- `mimiciv_hosp.admissions` — admission data
- `mimiciv_hosp.diagnoses_icd` — ICD codes
- `mimiciv_note.discharge` — discharge summaries
- `mimiciv_hosp.patients` — patient demographics

## Construction

The DiReCT (Diagnostic Reasoning for Clinical Text) benchmark frames diagnosis as a multi-step reasoning task. Each instance provides partial clinical context and asks the model to determine the most likely diagnosis from a differential.

## Related Summary Files

- `summaries/2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text_benchmark_summary.md`
