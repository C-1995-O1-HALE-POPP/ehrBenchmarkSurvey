# BioCoder

## Overview

BioCoder is a benchmark for evaluating LLMs on bioinformatics code generation tasks. It includes function-level code completion challenges extracted from real bioinformatics repositories, covering Python and R.

- **Paper**: Tang et al., "BioCoder: A Benchmark for Bioinformatics Code Generation with Contextual Pragmatic Knowledge" (ACL 2024)
- **HuggingFace (public)**: [lilbillbiscuit/biocoder_public](https://huggingface.co/datasets/lilbillbiscuit/biocoder_public)
- **HuggingFace (hidden)**: [lilbillbiscuit/biocoder_hidden](https://huggingface.co/datasets/lilbillbiscuit/biocoder_hidden)
- **License**: CC-BY-4.0
- **Task**: Code generation / function completion
- **Languages**: Python, R
- **Domain**: Bioinformatics

## Dataset Structure

The public dataset includes:
- `promptSummaryOnly`: Task description in natural language
- `repository`: Source repository name
- `content`: Surrounding code context with a hole
- `contextCode`: Full file context
- `language`: Python or R
- `goldenCode`: Reference (correct) implementation
- `signature`: Function signature
- `filePath`: Source file path

The hidden dataset has only `input` (prompt) and `output` (reference code) fields.

### Example

```python
# promptSummaryOnly: "write a function that takes in a string and returns
# a sanitized version suitable for LaTeX formatting..."

# goldenCode:
def sanitize_tex(original_text):
    sanitized_tex = original_text.replace('\\\\', '\\\\textbackslash ')
    ...
    return sanitized_tex
```

## Access

```python
from datasets import load_dataset
# Public split
ds = load_dataset("lilbillbiscuit/biocoder_public")
# Hidden split (for evaluation)
ds = load_dataset("lilbillbiscuit/biocoder_hidden")
```

## Citation

```bibtex
@article{tang2024biocoder,
  title={BioCoder: A Benchmark for Bioinformatics Code Generation with
         Contextual Pragmatic Knowledge},
  author={Tang, Xiangru and others},
  journal={ACL},
  year={2024}
}
```
