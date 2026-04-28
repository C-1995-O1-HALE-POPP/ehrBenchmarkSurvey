# HealthBench

## Overview

HealthBench is a benchmark for evaluating large language models (LLMs) on health-related conversations and clinical reasoning. Developed by OpenAI, it contains approximately 5,000 healthcare conversations scored by physician evaluators. Each conversation is evaluated against multiple rubric items with detailed criteria and point allocations. The benchmark covers diverse themes including global health, communication, emergency referrals, complex responses, and health data tasks.

- **Paper**: [HealthBench: Evaluating Large Language Models Towards Improved Human Health](https://arxiv.org/abs/2405.18874)
- **HuggingFace**: [openai/healthbench](https://huggingface.co/datasets/openai/healthbench)
- **Eval Implementation**: [openai/simple-evals](https://github.com/openai/simple-evals)
- **License**: MIT
- **Task**: Health conversation QA with rubric-based evaluation
- **Size**: ~5,000 conversations with physician-scored rubrics

## Dataset Structure

### Files

| File | Description |
|------|-------------|
| `consensus_2025-05-09-20-00-46.jsonl` | Final consensus data with physician-agreed tags |
| `2025-05-07-06-14-12_oss_eval.jsonl` | Model evaluation results |
| `2025-05-07-06-14-12_oss_meta_eval.jsonl` | Meta-evaluation data |
| `hard_2025-05-08-21-00-10.jsonl` | Hard subset of cases |

### Fields

| Field | Description |
|-------|-------------|
| `prompt_id` | Unique identifier (UUID) for each prompt |
| `prompt` | List of conversation turns `[{role, content}]` ending with a user message |
| `rubrics` | List of `[{criterion, points}]` scoring items |
| `ideal_completions_data` | Reference completions (may be null) |
| `example_tags` | Thematic tags e.g. `theme:global_health`, `physician_agreed_category:enough-context` |
| `canary` | Dataset canary string for benchmark contamination detection |

### Example

```json
{
  "prompt_id": "1f548d5b-cd00-49a0-b327-283a2e00debd",
  "prompt": [
    {
      "role": "user",
      "content": "Make a 3 months plan to address my mild postpartum depression..."
    }
  ],
  "rubrics": [
    {
      "criterion": "Recognizes the need for professional mental health evaluation...",
      "points": 1
    },
    {
      "criterion": "Recommends consulting with a healthcare provider...",
      "points": 1
    }
  ],
  "example_tags": [
    "theme:context_seeking",
    "physician_agreed_category:enough-context"
  ]
}
```

## Sample Statistics (200 conversations)

| Theme | Count |
|-------|-------|
| Global health | 47 |
| Communication | 32 |
| Context seeking | 31 |
| Hedging | 28 |
| Emergency referrals | 26 |
| Complex responses | 20 |
| Health data tasks | 16 |

## Access

```bash
# Download consensus data
curl -L "https://huggingface.co/datasets/openai/healthbench/resolve/main/consensus_2025-05-09-20-00-46.jsonl" -o consensus.jsonl

# Or via Python
from datasets import load_dataset
dataset = load_dataset("openai/healthbench")
```

## Citation

```bibtex
@article{healthbench2024,
  title={HealthBench: Evaluating Large Language Models Towards Improved Human Health},
  author={OpenAI},
  journal={arXiv preprint arXiv:2405.18874},
  year={2024}
}
```
