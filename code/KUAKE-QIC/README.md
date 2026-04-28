# KUAKE-QIC: Query Intent Classification

## Overview
KUAKE-QIC (KUAKE Query Intent Classification) is a dataset for classifying medical search queries into predefined intent categories. Given a user's medical search query, the task is to classify it into one of 11 categories such as "疾病表述" (disease description), "治疗方案" (treatment plan), "病因分析" (etiology analysis), "诊断", and "就医建议" (medical advice).

**Task Type**: Text Classification (multi-class, single-label, 11 classes)
**Language**: Chinese
**Source**: `wyp/CBlue-KUAKE-QIC`, `CHIHCI/CBlue-KUAKE-QIC` on HuggingFace
**License**: Not specified

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Dev   | 1,955    |

Note: Full train/dev/test splits are available through the official CBLUE distribution at https://github.com/CBLUEbenchmark/CBLUE.

## Field Schema
| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique example identifier |
| `query` | string | Medical search query text |
| `label` | string | Intent category label |

## Label Categories (11 classes)
- `疾病表述` (disease description)
- `治疗方案` (treatment plan)
- `病因分析` (etiology analysis)
- `诊断` (diagnosis)
- `就医建议` (medical advice)
- `指标解读` (indicator interpretation)
- `医疗费用` (medical expenses)
- `疾病预防` (disease prevention)
- `定义` (definition)
- `其他` (other)
- `后果表述` (consequence description)

## Examples

### Example 1
```json
{"id": "s1", "query": "心肌缺血如何治疗与调养呢？", "label": "治疗方案"}
```

### Example 2
```json
{"id": "s2", "query": "19号来的月经，25号服用了紧急避孕药本月5号，怎么办？", "label": "治疗方案"}
```

### Example 3
```json
{"id": "s3", "query": "什么叫痔核脱出？什么叫外痔？", "label": "疾病表述"}
```

### Example 4
```json
{"id": "s4", "query": "您好，请问一岁三个月的孩子可以服用复方锌布颗粒吗？", "label": "治疗方案"}
```

## Access Instructions
```bash
# Download from HuggingFace
curl -L -s "https://huggingface.co/datasets/wyp/cblue-qic/resolve/main/KUAKE-QIC_dev.json" -o dev.json
```

Alternative source: `CHIHCI/CBlue-KUAKE-QIC` (dataset viewer available, auto-converted to parquet).

For the full dataset with all splits, please refer to:
- Official CBLUE: https://github.com/CBLUEbenchmark/CBLUE

## Citation
Part of the KUAKE (Alibaba) medical benchmark and CBLUE suite.
