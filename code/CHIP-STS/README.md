# CHIP-STS: Chinese Healthcare Information Processing - Sentence Text Similarity

## Overview
CHIP-STS is a dataset for medical sentence semantic similarity. Given two Chinese medical sentences, the task is to determine whether they are semantically equivalent (1) or not (0). The sentences are drawn from several medical domains including AIDS, diabetes, hypertension, hepatitis B, breast cancer, etc.

**Task Type**: Sentence Semantic Similarity / Binary Classification
**Language**: Chinese
**Source**: `dirtycomputer/CBLUE-CHIP-STS` on HuggingFace
**License**: Not specified

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Train | 16,000   |

## Field Schema
| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique example identifier |
| `text1` | string | First sentence |
| `text2` | string | Second sentence |
| `label` | string | "0" (not similar) or "1" (similar) |
| `category` | string | Medical domain category |

## Categories
Common categories include: `aids`, `diabetes`, `hypertension`, `hepatitis_b`, `breast_cancer`, `lung_cancer`, etc.

## Examples

### Example 1 (Not Similar)
```json
{
  "id": "1",
  "text1": "艾滋病窗口期会出现腹泻症状吗",
  "text2": "头疼腹泻四肢无力是不是艾滋病",
  "label": "0",
  "category": "aids"
}
```

### Example 2 (Similar)
```json
{
  "id": "2",
  "text1": "由于糖尿病引起末梢神经炎，怎么根治？",
  "text2": "糖尿病末梢神经炎的治疗方法",
  "label": "1",
  "category": "diabetes"
}
```

### Example 3 (Not Similar)
```json
{
  "id": "3",
  "text1": "H型高血压，是通所说的高血脂？",
  "text2": "高血压引起脑出血怎么抢救治疗",
  "label": "0",
  "category": "hypertension"
}
```

## Access Instructions
```bash
# Download from HuggingFace
curl -L -s "https://huggingface.co/datasets/dirtycomputer/CBLUE-CHIP-STS/resolve/main/CHIP-STS_train.json" -o train.json
```

Also available via datasets-server API:
```bash
curl -s "https://datasets-server.huggingface.co/rows?dataset=dirtycomputer/CBLUE-CHIP-STS&config=default&split=train&offset=0&length=100"
```

Alternative sources:
- `wyp/cblue-sts` on HuggingFace  
- Official CBLUE: https://github.com/CBLUEbenchmark/CBLUE

## Citation
Part of the CHIP 2021 shared tasks and CBLUE benchmark.
