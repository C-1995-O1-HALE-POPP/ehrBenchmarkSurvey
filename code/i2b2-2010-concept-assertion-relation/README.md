# i2b2 2010 — Concept, Assertion, and Relation Extraction Challenge

## Description

The 2010 i2b2/VA challenge consists of three subtasks on clinical discharge summaries: (1) medical concept extraction (NER), (2) assertion classification (present, absent, possible, etc.), and (3) relation extraction between medical concepts.

## Data Source

- **Provider**: Partners HealthCare / i2b2 / VA
- **Portal**: DBMI Data Portal (Harvard Medical School)
- **Access URL**: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/

## Access Requirements

Requires a Data Use Agreement (DUA) with Partners HealthCare / i2b2/n2c2. After signing the DUA, access is granted through the DBMI Portal.

## Files to Download

After obtaining access via the DBMI portal:

1. **Training data**: Annotated discharge summaries with concept, assertion, and relation labels
2. **Test data**: Held-out discharge summaries (unannotated)
3. **Annotation guidelines**: Concept types, assertion categories, and relation schema
4. **Optional**: Gold-standard test annotations released post-evaluation

## Task Description

Three subtasks on the same corpus of discharge summaries:

### Subtask 1 — Medical Concept Extraction
- **Type**: Named entity recognition (NER)
- **Target**: Identify spans for medical problems, treatments, and tests
- **Categories**: problem, treatment, test

### Subtask 2 — Assertion Classification
- **Type**: Sequence classification on extracted concepts
- **Target**: Classify each concept as present, absent, possible, hypothetical, conditional, or not associated with the patient
- **Input**: Concept spans (from Subtask 1) + surrounding clinical text

### Subtask 3 — Relation Extraction
- **Type**: Relation classification between concept pairs
- **Target**: Identify whether two medical concepts have a clinical relationship
- **Relation types**: Treatment improves/worsens problem, Test reveals problem, Problem indicates problem, etc.
- **Input**: Concept pairs (from Subtask 1) + surrounding text

## Expected Data Format

Based on typical i2b2 challenge structure:

- Clinical notes as `.txt` files
- Concept annotations (Subtask 1):
  - XML or standoff format with character offsets, concept type (problem/treatment/test)
- Assertion annotations (Subtask 2):
  - Linked to concept IDs with assertion label (present/absent/possible/hypothetical/conditional/other)
- Relation annotations (Subtask 3):
  - Pairs of concept IDs with relation type label
- Data split: train / test with same documents shared across all 3 subtasks

## Status

**P3 — Awaiting credentialed access**

📋 Documented; data not yet downloaded pending n2c2/i2b2 DUA approval.
