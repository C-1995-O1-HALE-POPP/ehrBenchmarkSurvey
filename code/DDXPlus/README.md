# DDXPlus

## Overview

DDXPlus is a large-scale dataset for **Automatic Symptom Detection (ASD)** and **Automatic Diagnosis (AD)** systems. Patients are synthesized using a proprietary medical knowledge base and a commercial rule-based differential diagnosis system. Each patient is characterized by socio-demographic data, a ground-truth pathology, a set of evidence (symptoms/antecedents), and a ranked list of differential diagnoses with confidence scores.

- **Source**: HuggingFace `aai530-group6/ddxplus`
- **Paper**: [DDXPlus: A New Dataset For Automatic Medical Diagnosis](https://arxiv.org/abs/2205.09148) (NeurIPS 2022 Datasets & Benchmarks)
- **PapersWithCode**: [ddxplus](https://paperswithcode.com/dataset/ddxplus)
- **License**: CC-BY 4.0
- **Languages**: English (also available in French)
- **Task**: Tabular classification — multi-class differential diagnosis
- **Format**: CSV
- **Examples collected**: 150

## Dataset Structure

| Split     | File |
|-----------|------|
| Train     | `train.csv` |
| Test      | `test.csv` |
| Validate  | `validate.csv` |

### Fields

| Field | Description |
|-------|-------------|
| `AGE` | Patient age (2–109) |
| `SEX` | Patient sex (M/F) |
| `PATHOLOGY` | Ground-truth diagnosis |
| `INITIAL_EVIDENCE` | The initial symptom/evidence presented |
| `EVIDENCES` | Full list of symptom/evidence codes |
| `DIFFERENTIAL_DIAGNOSIS` | Ranked list of `[disease, probability]` pairs |

The evidence codes (e.g., `E_91`, `E_48`, `E_54_@_V_161`) reference a structured medical ontology. The differential diagnosis contains a ranked list of candidate diseases with predicted probabilities.

### Example (from raw/examples.json)

```json
{
  "AGE": "18",
  "SEX": "M",
  "PATHOLOGY": "URTI",
  "INITIAL_EVIDENCE": "E_91",
  "EVIDENCES": "['E_48', 'E_50', 'E_53', 'E_54_@_V_161', ...]",
  "DIFFERENTIAL_DIAGNOSIS": "[['Bronchitis', 0.192], ['Pneumonia', 0.176], ...]"
}
```

## Statistics (sampled 150 patients)

| Metric | Value |
|--------|-------|
| Unique pathologies | 45 |
| Age range | 2–109 |
| Sex distribution | M: 73, F: 77 |
| Top pathologies | Viral pharyngitis (11), URTI (10), Anaphylaxis (9) |

## Data Files

- `raw/examples.json` — 150 records

## Access

```bash
# Download via curl
curl -L "https://huggingface.co/datasets/aai530-group6/ddxplus/resolve/main/train.csv" -o train.csv

# Or via Python
from datasets import load_dataset
dataset = load_dataset("aai530-group6/ddxplus")
```

## Citation

```bibtex
@inproceedings{ddxplus2022,
  title={DDXPlus: A New Dataset For Automatic Medical Diagnosis},
  author={Tchango, Arsene Fansi and Goel, Rishab and Wen, Zhi and Martel, Julien and Ghosn, Joumana},
  booktitle={Thirty-sixth Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
  year={2022}
}
```
