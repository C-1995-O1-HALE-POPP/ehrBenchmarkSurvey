# MIMIC-III Outcome

- **Paper**: BRIDGE (2025)
- **Data**: MIMIC-III
- **Access**: PhysioNet credentialed (user has local MIMIC-III)
- **Priority**: P1

## Tasks

1. **Length of Stay (LoS)** — predict hospital stay duration category
2. **Mortality** — predict in-hospital mortality

## Required MIMIC-III Tables

- `MIMIC3.PATIENTS` — patient demographics
- `MIMIC3.ADMISSIONS` — admissions (contains `HOSPITAL_EXPIRE_FLAG`, `LOS`)
- `MIMIC3.ICUSTAYS` — ICU stays
- `MIMIC3.DIAGNOSES_ICD` — diagnoses
- `MIMIC3.LABEVENTS` — lab results
- `MIMIC3.CHARTEVENTS` — charted vitals

## Construction

Follow the standard MIMIC-III benchmark preprocessing:
1. Select first ICU stay per patient
2. Extract demographics, lab values (first 24h), vitals
3. Label: LoS > 3 days or > 7 days; mortality = in-hospital death

## Related Summary Files

- `summaries/2025_bridge_*_benchmark_summary.md`
