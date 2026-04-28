# KUAKE-QTR: Query-Title Relevance

## Overview
KUAKE-QTR is a dataset for determining the relevance between a medical search query and a document title. Given a user query and a candidate article title, the task is to classify whether the title is relevant to the query. This is a binary classification task with three label values (0, 1, 2, 3) representing different relevance levels where higher values indicate greater relevance.

**Task Type**: Relevance Classification (multi-class, 4 levels)
**Language**: Chinese
**Source**: `dirtycomputer/CBLUE-KUAKE-QTR`, `wyp/cblue-qtr` on HuggingFace
**License**: Not specified

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Train | 24,174   |

## Field Schema

### dirtycomputer/CBLUE-KUAKE-QTR format:
| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique example identifier |
| `query` | string | Medical search query |
| `title` | string | Candidate document title |
| `label` | string | Relevance label (0, 1, 2, or 3) |

## Examples

### Example 1 (label=3, highly relevant)
```json
{
  "id": "s1",
  "query": "10个月宝宝一般睡多少个小时",
  "title": "10个月的宝宝一天应该睡多少小时？我",
  "label": "3"
}
```

### Example 2 (label=3)
```json
{
  "id": "s2",
  "query": "10个月宝宝没长牙怎么办",
  "title": "宝宝快十个月了，还没有长牙怎么办？",
  "label": "3"
}
```

### Example 3 (label=1, relevant)
```json
{
  "id": "s3",
  "query": "儿童远视眼怎么恢复视力",
  "title": "远视眼该如何保养才能恢复一些视力",
  "label": "1"
}
```

## Access Instructions
```bash
# Download from HuggingFace (dirtycomputer mirror)
curl -L -s "https://huggingface.co/datasets/dirtycomputer/CBLUE-KUAKE-QTR/resolve/main/KUAKE-QTR_train.json" -o train.json

# Alternative source (wyp mirror, dev set only)
curl -L -s "https://huggingface.co/datasets/wyp/cblue-qtr/resolve/main/KUAKE-QTR_dev.json" -o dev.json
```

Also available via datasets-server API:
```bash
curl -s "https://datasets-server.huggingface.co/rows?dataset=dirtycomputer/CBLUE-KUAKE-QTR&config=default&split=train&offset=0&length=100"
```

For the full official dataset with all splits:
- Official CBLUE: https://github.com/CBLUEbenchmark/CBLUE

## Citation
Part of the KUAKE (Alibaba) medical benchmark and CBLUE suite.
