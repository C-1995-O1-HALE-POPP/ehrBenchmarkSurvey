# ADE (Adverse Drug Event Corpus)

## Overview

The ADE corpus (v2) is a benchmark for adverse drug reaction detection from biomedical text. It includes three tasks: sentence-level classification (ADE-related or not), drug-AE relation extraction, and drug-dosage relation extraction.

- **Paper**: Gurulingappa et al., "Development of a benchmark corpus to support the automatic extraction of drug-related adverse effects from medical case reports" (J Biomed Inform, 2012)
- **HuggingFace**: [ade-benchmark-corpus/ade_corpus_v2](https://huggingface.co/datasets/ade-benchmark-corpus/ade_corpus_v2)
- **License**: Unknown
- **Language**: English
- **Domain**: Medical case reports (PubMed abstracts)

## Tasks

| Config | Task | Description |
|--------|------|-------------|
| `Ade_corpus_v2_classification` | Classification | Binary: is sentence ADE-related? |
| `Ade_corpus_v2_drug_ade_relation` | Relation Extraction | Drug ↔ Adverse Effect relations |
| `Ade_corpus_v2_drug_dosage_relation` | Relation Extraction | Drug ↔ Dosage relations |

## Dataset Statistics

- ~23,500 sentences for classification (17,637 train / 5,879 test)
- ~23,500 sentences with drug-AE relation annotations
- ~23,500 sentences with drug-dosage relation annotations

Files: `ADE-NEG.txt` (negative examples), `DRUG-AE.rel` (drug-adverse effect relations), `DRUG-DOSE.rel` (drug-dosage relations)

## Data Format

**Classification**: `{text: str, label: int}` (1 = ADE-related, 0 = not)

**Relation Extraction**: Sorted sentence pairs with drug and effect/dosage annotations.

## Access

```bash
from datasets import load_dataset
ds = load_dataset("ade-benchmark-corpus/ade_corpus_v2", "Ade_corpus_v2_classification")

# Also available via:
# curl -L https://huggingface.co/datasets/ade-benchmark-corpus/ade_corpus_v2/resolve/main/...
```

## Citation

```bibtex
@article{gurulingappa2012development,
  title={Development of a benchmark corpus to support the automatic extraction
         of drug-related adverse effects from medical case reports},
  author={Gurulingappa, Harsha and Rajput, Abdul Mateen and Roberts, Angus and
          Fluck, Juliane and Hofmann-Apitius, Martin and Solano, Luca},
  journal={Journal of biomedical informatics},
  volume={45},
  number={5},
  pages={885--892},
  year={2012},
  publisher={Elsevier}
}
```
