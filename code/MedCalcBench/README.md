# MedCalcBench (from MedAgentGym)

**Category**: Clinical Formula Computation (P2 - Clinical Reasoning)

## Overview
MedCalcBench is a clinical calculation benchmark component of MedAgentGym (ICLR 2026), the first publicly available training environment for coding-based medical reasoning in LLM agents. MedCalcBench tests LLM ability to perform clinical formula computations (55 task types, text-based). No standalone repo exists - it is part of the MedAgentGym framework.

- **Paper**: [arXiv:2506.02911](https://arxiv.org/abs/2506.02911) / [OpenReview](https://openreview.net/forum?id=jHDZEUgS4r)
- **Repo**: https://github.com/wshi83/MedAgentGym (this benchmark is a subset)
- **Documentation**: https://wshi83.github.io/MedAgentGym-Page/
- **HuggingFace**: https://huggingface.co/MedAgentGym

## Dataset
MedCalcBench is one of 12 datasets in MedAgentGym:
- **Data Type**: Text
- **Task Types**: 55 clinical formula computation tasks
- **Role**: Internal validation (in-distribution) dataset

The public repo contains task definitions (`train_tasks.jsonl`, `test_tasks.jsonl`) with task ID, description, question, and ground truth answer. Full preprocessed data requires approval.

## Data Access

**Step 1**: Obtain PhysioNet credentials for MIMIC-related data:
- Complete CITI Data or Specimens Only Research training
- Sign PhysioNet Credentialed Health Data Use Agreement 1.5.0

**Step 2**: Email `medagentgym@gmail.com` with subject "MedAgentGym Preprocessed Data Access" to request the `download_data.py` script.

**Step 3**: Run the download script to get preprocessed datasets into `./data/`.

## Setup

```bash
# Build Docker container for isolated code execution
docker buildx build -t ehr_gym:latest .

# Or use the prepared script
bash build_docker.sh
```

## Running Experiments

```bash
# Single-task evaluation (e.g., Biocoder with GPT-4.1-mini)
python3 /home/main.py \
  --config /home/configs/gpt_4_1_mini/exp-gpt_4_1_mini-biocoder.yaml \
  --async_run --parallel_backend joblib --n_jobs 5
```

Modify `entrypoint.sh` with desired experiment commands. Configs are in `configs/` directory.

## Dependencies
- Docker
- Python 3.x
- PhysioNet credentialed access (for MIMIC-III, eICU, TREQS, EHRSHOT subsets)
- Preprocessed data from `download_data.py`

## Relationship to MedCalc-Bench (ncbi-nlp)
MedCalcBench is a different benchmark from ncbi-nlp/MedCalc-Bench. Both involve clinical calculations, but MedCalcBench is embedded within the MedAgentGym agent training environment.
