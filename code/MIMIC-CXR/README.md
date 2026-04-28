# MIMIC-CXR

- **Paper**: EHR-R1 (2025)
- **Data**: MIMIC-CXR (chest X-ray reports)
- **Access**: PhysioNet (separate module from MIMIC-III/IV)
- **Priority**: P1

## Task

X-ray Report Summarization: generate findings/impression from chest X-ray report text.

## Required Data

MIMIC-CXR module (separate PhysioNet dataset):
- Contains chest X-ray images + radiology reports
- `mimic_cxr_reports` — de-identified report text
- https://physionet.org/content/mimic-cxr/

## Construction

1. Extract report text from MIMIC-CXR
2. Parse "Findings" and "Impression" sections
3. Task: Findings → Impression

## Note

MIMIC-CXR is a separate PhysioNet download (~470 GB with images, much smaller for text only).

## Related Summary Files

- `summaries/2025_ehr_r1_*_benchmark_summary.md`
