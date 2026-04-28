# n2c2 2014 — De-identification Challenge

## Description

The 2014 n2c2 De-identification challenge extends the earlier 2006 task to longitudinal clinical records. Participants must detect PHI across multiple clinical notes spanning longer patient timelines, reflecting real-world EHR de-identification scenarios.

## Data Source

- **Provider**: Partners HealthCare (now Mass General Brigham)
- **Portal**: DBMI Data Portal (Harvard Medical School)
- **Access URL**: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

## Access Requirements

Requires a Data Use Agreement (DUA) with Partners HealthCare / n2c2. After signing the DUA, access is granted through the DBMI Portal (same portal as 2006 challenge).

## Files to Download

After obtaining access via the DBMI portal:

1. **Training data**: Annotated longitudinal clinical records with PHI spans
2. **Test data**: Held-out longitudinal records (unannotated)
3. **Annotation guidelines**: PHI categories and annotation schema (may differ from 2006)
4. **Optional**: Gold-standard test annotations released post-evaluation

## Task Description

- **Task**: PHI detection in longitudinal clinical notes
- **Input**: Multiple clinical notes per patient across time
- **Output**: PHI spans with category labels across the patient timeline
- **Key difference from 2006**: Notes are linked to patients — de-identification must be consistent across notes for the same patient (e.g., same name appears in multiple notes)

## Expected Data Format

Based on typical n2c2 challenge structure:

- Clinical notes as `.txt` files (potentially organized by patient)
- Annotations in standoff or inline XML format:
  - Character offsets
  - PHI category label
  - Patient-level linking for longitudinal consistency
- Data split: train / test with patient-level separation

## Status

**P3 — Awaiting credentialed access**

📋 Documented; data not yet downloaded pending n2c2 DUA approval.
