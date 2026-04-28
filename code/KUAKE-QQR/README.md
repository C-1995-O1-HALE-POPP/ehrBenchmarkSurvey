# KUAKE-QQR: Query-Query Relevance

## Overview
KUAKE-QQR is a dataset for measuring the relevance between two medical search queries. Given two user queries, the task is to determine whether they express the same information need. This is a binary classification task where 1 indicates the queries are relevant/similar, and 0 indicates they are not.

**Task Type**: Query-Query Relevance / Binary Classification
**Language**: Chinese
**Source**: `dirtycomputer/CBLUE-KUAKE-QQR`, `wyp/cblue-qqr2` on HuggingFace
**License**: Not specified

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Train | 15,000   |

## Field Schema

### dirtycomputer/CBLUE-KUAKE-QQR format:
| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique example identifier |
| `query1` | string | First medical search query |
| `query2` | string | Second medical search query |
| `label` | string | "0" (not similar) or "1" (similar) |

## Examples

### Example 1 (Not Relevant, label=0)
```json
{
  "id": "s1",
  "query1": "天价输液费",
  "query2": "输液价格",
  "label": "0"
}
```

### Example 2 (Not Relevant, label=0)
```json
{
  "id": "s2",
  "query1": "天价输液费",
  "query2": "输液港费用",
  "label": "0"
}
```

### Example 3 (Relevant, label=1)
```json
{
  "id": "s3",
  "query1": "茴香是发物吗",
  "query2": "茴香怎么吃？",
  "label": "0"
}
```

## Access Instructions
```bash
# Download from HuggingFace (dirtycomputer mirror)
curl -L -s "https://huggingface.co/datasets/dirtycomputer/CBLUE-KUAKE-QQR/resolve/main/KUAKE-QQR_train.json" -o train.json

# Alternative source (wyp mirror, dev set only)
curl -L -s "https://huggingface.co/datasets/wyp/cblue-qqr2/resolve/main/KUAKE-QQR_dev.json" -o dev.json
```

Also available via datasets-server API:
```bash
curl -s "https://datasets-server.huggingface.co/rows?dataset=dirtycomputer/CBLUE-KUAKE-QQR&config=default&split=train&offset=0&length=100"
```

For the full official dataset with all splits:
- Official CBLUE: https://github.com/CBLUEbenchmark/CBLUE

## Citation
Part of the KUAKE (Alibaba) medical benchmark and CBLUE suite.
