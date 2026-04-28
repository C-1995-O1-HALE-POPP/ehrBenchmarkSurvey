# CLIP (Clinical Language Inference for Patients)

- **Paper**: Mullenbach et al. (2021), used in Clinical T5 (2024) and BRIDGE (2025)
- **Data**: MIMIC-III discharge summaries
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Task

Multi-label Clinical Action Item Classification: given a discharge summary, predict which clinical action items apply (e.g., "patient instructions", "appointment scheduling", "medication changes").

## Required MIMIC-III Tables

- `MIMIC3.NOTEEVENTS` — discharge summaries

## Construction

Mullenbach et al. (2021) annotated discharge summaries with action item labels. Due to long document length, the original paper segments records into chunks and maps labels appropriately.

## Related Summary Files

- `summaries/2024_are_clinical_t5_models_better_for_clinical_text_benchmark_summary.md`
- `summaries/2025_bridge_*_benchmark_summary.md`
