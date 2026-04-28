# KUAKE-IR: Knowledge-based Unsupervised Anomaly detection and Knowledge Extraction - Information Retrieval

## Overview
KUAKE-IR is a dataset for medical information retrieval. Given a medical query, the task is to retrieve relevant documents from a corpus of medical articles. It is part of the KUAKE benchmark series from Alibaba, focusing on evaluating retrieval models in the Chinese medical domain.

**Task Type**: Information Retrieval / Document Retrieval
**Language**: Chinese
**Source**: CBLUE benchmark (released August 1, 2022); provided by Alibaba OpenSearch and Alibaba KUAKE
**License**: Not specified

## Current Status
**NOT FOUND on HuggingFace.** KUAKE-IR was released later than the other KUAKE datasets (August 2022 vs. earlier releases) and does not appear to have been uploaded to HuggingFace by community members at the time of this survey.

## Access Instructions

### Option 1: Official CBLUE Distribution
The dataset is distributed through the official CBLUE benchmark channel:
- GitHub: https://github.com/CBLUEbenchmark/CBLUE
- Follow the download instructions at https://github.com/CBLUEbenchmark/CBLUE#download-dataset
- The data requires registration/application through the CBLUE platform

### Option 2: Alibaba Tianchi
The dataset was announced on the Alibaba Tianchi platform:
- Tianchi CBLUE page: https://tianchi.aliyun.com/specials/promotion/cblue-news
- Released: August 1, 2022

### Option 3: Modelscope (potential)
The dataset may be available on Alibaba Modelscope (modelscope.cn), but was not found during search.
```bash
# To check Modelscope:
# Visit: https://modelscope.cn/datasets
# Search: "KUAKE-IR"
```

## Expected Data Format (from CBLUE specification)
Based on the other KUAKE datasets and the CBLUE benchmark structure, KUAKE-IR likely contains:
- Medical search queries paired with candidate documents
- Relevance labels indicating document-query relevance
- A document corpus of Chinese medical articles

The data is expected to follow a format similar to other CBLUE retrieval tasks with fields like:
| Field | Type | Description |
|-------|------|-------------|
| `query` | string | Medical search query |
| `doc_id` | string | Document identifier |
| `doc_text` | string | Document text |
| `label` | int/string | Relevance label |

## Related Datasets
- **KUAKE-QIC**: Query Intent Classification (available on HF)
- **KUAKE-QTR**: Query-Title Relevance (available on HF)
- **KUAKE-QQR**: Query-Query Relevance (available on HF)
- **KUAKE-IR**: Information Retrieval (this dataset, not on HF)

## Citation
From the CBLUE benchmark paper. If using this dataset, please cite:
- The CBLUE benchmark paper
- The KUAKE (Alibaba) medical AI initiative

Reference: https://github.com/CBLUEbenchmark/CBLUE
