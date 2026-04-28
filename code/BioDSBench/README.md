# BioDSBench

## Overview

BioDSBench evaluates whether LLMs can replace data scientists in biomedical research. It includes coding tasks in Python and R that represent real-world biomedical data analysis scenarios including gene expression analysis, genomic alteration profiling, and clinical data integration.

- **Paper**: [BioDSBench: Benchmarking LLMs for Biomedical Data Science Tasks](https://arxiv.org/abs/2410.21591)
- **HuggingFace**: [zifeng-ai/BioDSBench](https://huggingface.co/datasets/zifeng-ai/BioDSBench)
- **License**: Unknown
- **Task**: Biomedical code generation / data science
- **Languages**: Python, R
- **Domain**: Biomedical data science (cBioPortal, clinical genomics)

## Dataset Structure

| Config | Description |
|--------|-------------|
| `python` | Python coding tasks |
| `R` | R coding tasks |
| `dataset_schema` | Schema definition for dataset tables |

### Fields

| Field | Description |
|-------|-------------|
| `study_ids` | PubMed ID of the source study |
| `question_ids` | Unique question identifier |
| `analysis_types` | Types of analysis (e.g., Gene Expression & Differential Analysis) |
| `study_types` | Study category (e.g., Pan-Cancer) |
| `dataset_url` | cBioPortal dataset URL |
| `queries` | Natural language task description |
| `cot_instructions` | Chain-of-thought instructions for solving |
| `reference_answer` | Reference implementation |
| `test_cases` | Unit test assertions to verify correctness |
| `tables` | Input data files |
| `study_data_configs` | Dataset configuration metadata |

### Example

```python
# Query: "Given a gene expression dataset... transpose the DataFrame so that
# there is a column named 'sample' containing all the sample IDs..."

# Reference:
import pandas as pd
df_exp = pd.read_csv("gene_expression_rna_sub.csv")
df_exp = df_exp.set_index("sample").T
df_exp = df_exp.rename_axis("sample").reset_index()

# Test:
assert len(df_exp) == 1173
assert len(df_exp.columns) == 3002
```

## Access

```python
from datasets import load_dataset
ds_python = load_dataset("zifeng-ai/BioDSBench", "python", split="test")
ds_r = load_dataset("zifeng-ai/BioDSBench", "R", split="test")
```

## Citation

```bibtex
@article{liu2024biodsbench,
  title={BioDSBench: Benchmarking LLMs for Biomedical Data Science Tasks},
  author={Liu, Zifeng and others},
  journal={arXiv preprint arXiv:2410.21591},
  year={2024}
}
```
