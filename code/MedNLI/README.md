# MedNLI - A Natural Language Inference Dataset for the Clinical Domain

> Source: [PhysioNet](https://physionet.org/content/mednli/1.0.0/) · [HuggingFace](https://huggingface.co/datasets/presencesw/mednli) · [Paper (arXiv)](https://arxiv.org/abs/1808.06752)

## Overview

MedNLI is a Natural Language Inference (NLI) dataset annotated by doctors, grounded in the medical history of patients. Premise sentences are drawn from the **Past Medical History** section of clinical notes in MIMIC-III (deceased patients only). The goal is to classify a given premise-hypothesis pair into one of three classes:

| Label | Meaning |
|-------|---------|
| `entailment` | The hypothesis can be inferred from the premise |
| `contradiction` | The hypothesis contradicts the premise |
| `neutral` | Neither entailment nor contradiction holds |

## Dataset Statistics

| Split | Examples | Entailment | Contradiction | Neutral |
|-------|----------|------------|---------------|---------|
| Train | 11,232 | 34% | 33% | 33% |
| Validation | 1,395 | 34% | 33% | 33% |
| Test | 1,422 | 34% | 33% | 33% |

Class distribution is balanced (~1/3 each) across all splits.

## Field Schema

Each example in the source JSONL format contains:

| Field | Type | Description |
|-------|------|-------------|
| `pairID` | string | Unique identifier for the premise-hypothesis pair |
| `gold_label` | string | `entailment`, `contradiction`, or `neutral` |
| `sentence1` | string | The premise (clinical text from a patient note) |
| `sentence2` | string | The hypothesis (statement to classify) |
| `sentence1_parse` | string | Constituency parse tree of the premise (Stanford parser) |
| `sentence2_parse` | string | Constituency parse tree of the hypothesis (Stanford parser) |
| `sentence1_binary_parse` | string | Binary parse tree of the premise |
| `sentence2_binary_parse` | string | Binary parse tree of the hypothesis |

The simplified schema (as in `raw/examples.json`) contains:
- `gold_label` — the label
- `sentence1` — the premise
- `sentence2` — the hypothesis
- `split` — which split the example belongs to (`train`, `validation`, `test`)

## Sample Premise-Hypothesis Pairs

### Example 1 — Entailment
```
Premise:    Labs were notable for Cr 1.7 (baseline 0.5 per old records) and lactate 2.4.
Hypothesis: Patient has elevated Cr.
Label:      entailment
```
*The premise states Cr is 1.7 vs baseline 0.5, so elevated Cr is entailed.*

### Example 2 — Contradiction (same premise)
```
Premise:    Labs were notable for Cr 1.7 (baseline 0.5 per old records) and lactate 2.4.
Hypothesis: Patient has normal Cr.
Label:      contradiction
```
*The premise indicates elevated Cr (1.7 > 0.5 baseline), so "normal Cr" contradicts it.*

### Example 3 — Neutral (same premise)
```
Premise:    Labs were notable for Cr 1.7 (baseline 0.5 per old records) and lactate 2.4.
Hypothesis: Patient has elevated BUN.
Label:      neutral
```
*The premise mentions Cr and lactate, not BUN, so the hypothesis is neutral.*

### Example 4 — Entailment (neurological)
```
Premise:    Nystagmus and twiching of R arm was noted.
Hypothesis: The patient had abnormal neuro exam.
Label:      entailment
```
*Nystagmus and arm twitching are abnormal neurological findings.*

### Example 5 — Entailment (cardiac)
```
Premise:    The patient was seen by his primary care physician after he had complained of a one-week history of dyspnea on exertion and jaw tightness.
Hypothesis: The patient has symptoms of a CHF exacerbation.
Label:      entailment
```
*Dyspnea on exertion and jaw tightness are classic CHF exacerbation symptoms.*

## Quick Start

```python
from datasets import load_dataset

# Load from HuggingFace (presencesw/mednli — parquet-backed, no auth required)
ds = load_dataset("presencesw/mednli", trust_remote_code=True)

print(ds["train"][0])
# {'gold_label': 'entailment',
#  'sentence1': 'Labs were notable for Cr 1.7 (baseline 0.5 per old records) and lactate 2.4.',
#  'sentence2': ' Patient has elevated Cr'}

# Or load from the raw examples in this repo
import json
with open("raw/examples.json") as f:
    examples = json.load(f)
```

## Citation

```
@misc{https://doi.org/10.13026/c2rs98,
    title     = {MedNLI — A Natural Language Inference Dataset For The Clinical Domain},
    author    = {Shivade, Chaitanya},
    year      = 2017,
    publisher = {physionet.org},
    doi       = {10.13026/C2RS98},
    url       = {https://physionet.org/content/mednli/}
}
```

## License

PhysioNet Credentialed Health Data License 1.5.0. Access to the full dataset requires PhysioNet credentialing.
