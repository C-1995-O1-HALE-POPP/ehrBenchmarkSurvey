# RADQA

- **Paper**: Clinical T5 (2024), original by Soni et al. (2022)
- **Data**: MIMIC-III radiology reports
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Task

Extractive Question Answering from radiology reports. Given a radiology report (context) and a question, extract the answer span. Unanswerable questions → empty output.

## Required MIMIC-III Tables

- `MIMIC3.NOTEEVENTS` — filter for `CATEGORY = 'Radiology'`
- Contains full radiology report text

## Construction

The original RadQA dataset (Soni et al., 2022):
1. Radiology reports from MIMIC-III
2. Manually authored questions with answer spans
3. SQuAD 2.0-style format (includes unanswerable questions)

Metrics: Exact Match, F1 score.

## Related Summary Files

- `summaries/2024_are_clinical_t5_models_better_for_clinical_text_benchmark_summary.md`
