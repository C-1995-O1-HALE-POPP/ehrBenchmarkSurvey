# CLISTER

## Overview

CLISTER (Corpus for LIterary Semantic TExtual similaRity) is a French clinical narrative corpus for semantic textual similarity (STS). It contains sentence pairs from French clinical documents with human-annotated similarity scores on a 0-4 scale.

- **Paper**: Hiebel et al., "CLISTER: A Corpus for Semantic Textual Similarity in French Clinical Narratives" (LREC 2022)
- **HuggingFace**: [DrBenchmark/CLISTER](https://huggingface.co/datasets/DrBenchmark/CLISTER)
- **License**: Unknown
- **Language**: French
- **Domain**: Clinical narratives
- **Task**: Semantic textual similarity (regression)

## Dataset Structure

| Split | Pairs | Description |
|-------|-------|-------------|
| train | ~8 | Training pairs (small) |
| validation | ~8 | Validation pairs |
| test | ~8 | Test pairs |

Note: The dataset has a small number of examples by design for few-shot evaluation.

### Fields

| Field | Description |
|-------|-------------|
| `id` | Unique pair identifier |
| `document_1_id` | Source document ID for first sentence |
| `document_2_id` | Source document ID for second sentence |
| `text_1` | First clinical sentence (French) |
| `text_2` | Second clinical sentence (French) |
| `label` | Similarity score (0-4, float) |

### Example

```json
{
  "id": "0",
  "document_1_id": "filepdf-250-1_838_187",
  "document_2_id": "filepdf-250-2_454_161",
  "text_1": "L'UIV a objectivé un retard de sécrétion avec importante dilatation...",
  "text_2": "L'UIV a montré une importante dilatation urétéro-pyélo-calicielle...",
  "label": 3.0
}
```

## Access

```python
from datasets import load_dataset
ds = load_dataset("DrBenchmark/CLISTER")
# Splits: train, validation, test
```

## Citation

```bibtex
@inproceedings{hiebel2022clister,
  title={CLISTER: A corpus for semantic textual similarity in French clinical narratives},
  author={Hiebel, Nicolas and Ferret, Olivier and Fort, Karën and Névéol, Aurélie},
  booktitle={LREC 2022},
  year={2022},
  url={https://hal-cea.archives-ouvertes.fr/cea-03740484}
}
```
