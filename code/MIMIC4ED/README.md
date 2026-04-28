# MIMIC4ED Benchmark

- **Paper**: EHR-R1 (2025)
- **Data**: MIMIC-IV-ED (Emergency Department)
- **Access**: PhysioNet credentialed (separate MIMIC-IV-ED module)
- **Priority**: P1

## Tasks

Three ED prediction tasks:
1. **Hospitalization Prediction** — predict whether ED visit leads to admission
2. **72-hour ED Revisit Prediction** — predict return within 72h
3. **Critical Triage Prediction** — predict critical outcomes from triage

## Required Data

MIMIC-IV-ED module (separate from main MIMIC-IV):
- `mimiciv_ed.edstays` — ED visits
- `mimiciv_ed.triage` — triage assessments
- `mimiciv_ed.vitalsign` — vital signs
- `mimiciv_ed.medrecon` — medication reconciliation

## Note

MIMIC-IV-ED is a separate PhysioNet module. If you don't have it, request access at:
https://physionet.org/content/mimic-iv-ed/

## Related Summary Files

- `summaries/2025_ehr_r1_*_benchmark_summary.md`
