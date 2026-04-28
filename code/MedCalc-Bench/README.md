# MedCalc-Bench

**Category**: Clinical Calculation from Patient Notes (P2 - Clinical Reasoning)

## Overview
MedCalc-Bench (NeurIPS 2024 Datasets and Benchmarks Track Oral) is the first medical calculation dataset designed to benchmark LLM ability to serve as clinical calculators. Each instance contains a patient note, a question asking to compute a specific clinical value, a ground truth answer, and a step-by-step solution. Covers 55 different calculation tasks across equation-based and rule-based categories.

- **Paper**: [arXiv:2406.12036](https://arxiv.org/abs/2406.12036)
- **Repo**: https://github.com/ncbi-nlp/MedCalc-Bench
- **Verified Version**: https://github.com/nikhilk7153/MedCalc-Bench-Verified
- **HuggingFace**: https://huggingface.co/datasets/nsk7153/MedCalc-Bench-Verified
- **License**: CC-BY-SA 4.0

## Dataset
- **Training set**: 10,543 instances (`datasets/train_data.csv.zip`)
- **Test set**: 1,100 manually reviewed instances (`datasets/test_set.csv`)
- **Task types**: 55 clinical calculators (equation-based: lab test, dosage, date, physical; rule-based: risk, severity, diagnosis)
- **Output types**: decimal, integer, date (MM/DD/YY), time (weeks + days)
- **Note sources**: PMC-Patients extracts, clinician-generated, template-synthesized

Each instance includes: Row Number, Calculator ID, Calculator Name, Category, Output Type, Note ID, Note Type, Patient Note, Question, Relevant Entities, Ground Truth Answer, Lower/Upper Limits, Ground Truth Explanation.

## Setup

```bash
# Create conda environment
conda env create -f repo/environment.yml
conda activate medcalc-bench

# Set API keys
export OPENAI_API_KEY=your_key
export HUGGINGFACE_TOKEN=your_token
```

## Evaluation

```bash
cd repo/evaluation

# Run evaluation on a model
python run.py --model <model_name> --prompt <prompt_style>

# Available models: mistralai/Mistral-7B-Instruct-v0.2, mistralai/Mixtral-8x7B-Instruct-v0.1,
#   meta-llama/Meta-Llama-3-8B-Instruct, meta-llama/Meta-Llama-3-70B-Instruct,
#   epfl-llm/meditron-70b, OpenAI/gpt-3.5-turbo, OpenAI/gpt-4, axiong/PMC_LLaMA_13B

# Available prompts: direct_answer, zero_shot, one_shot_cot

# Code interpreter evaluation (GPT-3.5/4 only)
python generate_code_prompt.py --gpt 4
```

Results output to `outputs/<model>_<prompt>.jsonl` and summarized in `results/results_<model>_<prompt_style>.json`.

## Dependencies
- Conda environment (environment.yml)
- OpenAI API key (for GPT models)
- HuggingFace token (for Llama/Mistral/Meditron models)
- No additional data download needed (dataset included in repo)
