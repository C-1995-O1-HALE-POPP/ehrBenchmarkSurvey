# i2b2 2009 — Medication Extraction Challenge

## Description

The 2009 i2b2 Medication Extraction challenge focuses on extracting structured medication information from clinical discharge summaries. The task involves identifying medication names, dosages, modes of administration, frequencies, durations, and reasons from narrative text.

## Data Source

- **Provider**: Partners HealthCare / i2b2 (Informatics for Integrating Biology and the Bedside)
- **Portal**: DBMI Data Portal (Harvard Medical School)
- **Access URL**: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

## Access Requirements

Requires a Data Use Agreement (DUA) with Partners HealthCare / i2b2/n2c2. After signing the DUA, access is granted through the DBMI Portal.

## Files to Download

After obtaining access via the DBMI portal:

1. **Training data**: Annotated discharge summaries with medication entities and attributes
2. **Test data**: Held-out discharge summaries (unannotated)
3. **Annotation guidelines**: Medication extraction schema and attribute definitions
4. **Optional**: Gold-standard test annotations released post-evaluation

## Task Description

- **Task**: Multi-field information extraction from clinical notes
- **Entities extracted**: Medication name (required), plus optional attributes:
  - Dosage (e.g., "500 mg")
  - Frequency (e.g., "BID", "every 6 hours")
  - Route/Mode (e.g., "oral", "IV")
  - Duration (e.g., "for 7 days")
  - Reason (e.g., "for hypertension")
- **Input**: Clinical discharge summaries (plain text)
- **Output**: Structured medication entries with linked attribute spans

## Expected Data Format

Based on typical i2b2 challenge structure:

- Clinical notes as `.txt` files
- Annotations as XML or standoff files:
  - Medication name spans with entity type
  - Linked attributes (dosage, frequency, etc.) with relationship edges to medication names
  - Character offsets and original text for each span
- Data split: train / test

## Status

**P3 — Awaiting credentialed access**

📋 Documented; data not yet downloaded pending n2c2/i2b2 DUA approval.
