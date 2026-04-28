# n2c2 2006 — De-identification Challenge

## Description

The 2006 n2c2 (formerly i2b2) De-identification challenge focuses on detecting Protected Health Information (PHI) in clinical narrative text. The task is to identify and classify PHI spans (names, dates, locations, phone numbers, etc.) in discharge summaries.

## Data Source

- **Provider**: Partners HealthCare (now Mass General Brigham)
- **Portal**: DBMI Data Portal (Harvard Medical School)
- **Access URL**: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

## Access Requirements

Requires a Data Use Agreement (DUA) with Partners HealthCare / n2c2. After signing the DUA, access is granted through the DBMI Portal.

## Files to Download

After obtaining access via the DBMI portal:

1. **Training data**: Annotated discharge summaries with PHI spans (likely XML or standoff format)
2. **Test data**: Held-out discharge summaries (unannotated)
3. **Annotation guidelines**: Documentation of PHI categories and annotation schema

## Task Description

- **Task**: Named entity recognition (NER) for 7+ PHI categories
- **Input**: Clinical discharge summaries (plain text)
- **Output**: PHI spans with category labels
- **Categories typically include**: Patient names, doctor names, hospital names, dates, locations, phone numbers, IDs, ages

## Expected Data Format

Based on typical n2c2 challenge structure:

- Clinical notes provided as `.txt` files or within XML
- Annotations as standoff files (e.g., `.txt.knowtator.xml` or `.xml`) with:
  - Character offsets for each PHI span
  - PHI category label
  - Original text of the span
- Data split: train / test (gold labels held by organizers)

## Status

**P3 — Awaiting credentialed access**

📋 Documented; data not yet downloaded pending n2c2 DUA approval.
