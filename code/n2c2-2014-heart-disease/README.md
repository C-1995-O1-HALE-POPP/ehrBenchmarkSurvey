# n2c2 2014 — Heart Disease Risk Factor Challenge

## Description

The 2014 n2c2 Heart Disease Risk Factor challenge involves classifying coronary artery disease (CAD) risk factors from narrative clinical records of 296 diabetic patients. It consists of 5 classification subtasks.

## Data Source

- **Provider**: Partners HealthCare (now Mass General Brigham)
- **Cohort**: 296 diabetic patients
- **Portal**: DBMI Data Portal (Harvard Medical School)
- **Access URL**: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

## Access Requirements

Requires a Data Use Agreement (DUA) with Partners HealthCare / n2c2. After signing the DUA, access is granted through the DBMI Portal.

## Files to Download

After obtaining access via the DBMI portal:

1. **Training data**: Clinical records (~296 patients) with risk factor annotations
2. **Test data**: Held-out patient records (unannotated)
3. **Annotation guidelines**: Risk factor definitions and annotation schema
4. **Optional**: Gold-standard test annotations released post-evaluation

## Task Description

Five risk factor classification subtasks for coronary artery disease:

| Subtask | Target | Type |
|---------|--------|------|
| 1 | Coronary Artery Disease (CAD) | Binary |
| 2 | Hypertension | Binary |
| 3 | Hyperlipidemia | Binary |
| 4 | Diabetes | Binary |
| 5 | Smoking Status | Classification |

- **Input**: Clinical narratives (history & physical notes, discharge summaries)
- **Output**: One label per subtask per patient
- **Evaluation**: Micro-averaged F1 over all 5 subtasks

## Expected Data Format

Based on typical n2c2 challenge structure:

- Clinical notes as `.txt` files (one or more per patient)
- Annotations as tabular/XML files mapping patient IDs to 5 risk factor labels:
  - CAD: present / absent
  - Hypertension: present / absent
  - Hyperlipidemia: present / absent
  - Diabetes: present / absent
  - Smoking: current / past / never / unknown
- Data split: train / test with patient-level separation

## Status

**P3 — Awaiting credentialed access**

📋 Documented; data not yet downloaded pending n2c2 DUA approval.
