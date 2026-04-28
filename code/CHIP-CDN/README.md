# CHIP-CDN: Clinical Diagnosis Normalization

## Overview
CHIP-CDN (Clinical Diagnosis Normalization) is a dataset for standardizing Chinese clinical diagnosis terms. Given a raw diagnosis text from electronic health records, the task is to map it to a standardized diagnosis name. This is essentially a text normalization / entity linking task in the medical domain.

**Task Type**: Text Normalization / Entity Linking
**Language**: Chinese
**Source**: `wyp/cblue-cdn` on HuggingFace (dev set); also available through CBLUE official distribution
**License**: Not specified

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Dev   | 1,007    |

Note: The full dataset (train/dev/test splits) is available through the official CBLUE benchmark distribution at https://github.com/CBLUEbenchmark/CBLUE.

## Field Schema
| Field | Type | Description |
|-------|------|-------------|
| `text` | string | Raw diagnosis text from EHR |
| `normalized_result` | string | Standardized/normalized diagnosis name |

## Examples

### Example 1
```json
{"text": "1型糖尿病性植物神经病变", "normalized_result": "1型糖尿病性自主神经病"}
```

### Example 2
```json
{"text": "2型糖尿病性周围神经病变", "normalized_result": "2型糖尿病性周围神经病"}
```

### Example 3
```json
{"text": "高血压病3级（极高危）", "normalized_result": "高血压病3级"}
```

### Example 4
```json
{"text": "冠状动脉粥样硬化性心脏病", "normalized_result": "冠状动脉粥样硬化性心脏病"}
```

### Example 5
```json
{"text": "脑梗死（急性期）", "normalized_result": "脑梗死"}
```

## Access Instructions
```bash
# Download from HuggingFace (dev set only)
curl -L -s "https://huggingface.co/datasets/wyp/cblue-cdn/resolve/main/CHIP-CDN_dev_1007.json" -o dev.json
```

For full dataset including train/test splits, please refer to the official CBLUE benchmark:
- GitHub: https://github.com/CBLUEbenchmark/CBLUE
- Download instructions: https://github.com/CBLUEbenchmark/CBLUE#download-dataset

## Citation
CHIP-CDN is part of the CHIP 2021 shared tasks and CBLUE benchmark.
