# FHIR-AgentBench

- **Source**: GitHub `glee4810/FHIR-AgentBench`
- **Paper**: [FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering](https://arxiv.org/abs/2509.19319)
- **Data**: MIMIC-IV Clinical Database Demo on FHIR (PhysioNet)
- **Access**: PhysioNet credential + GCP account required

## Task Description

FHIR-AgentBench evaluates LLM agents on two core clinical tasks:

1. **FHIR Resource Retrieval for Question Grounding**: Given a clinical question, identify which FHIR resources (Patient, Observation, MedicationRequest, etc.) are needed
2. **Answer Generation from Retrieved FHIR Resources**: Generate correct answers using retrieved FHIR data

Agents must interact with a real FHIR API (Google Cloud Healthcare API) populated with MIMIC-IV FHIR data.

## Setup Instructions

### 1. Download MIMIC-IV FHIR Demo

```
PhysioNet: https://physionet.org/content/mimic-iv-fhir-demo/2.1.0/
Download: mimic-iv-fhir-demo-2.1.0.tar.gz (~500 MB)
Extract: *.ndjson files (FHIR resources)
```

### 2. Set up Google Cloud FHIR Store

1. Create GCP account
2. Upload extracted ndjson files to Cloud Storage bucket
3. Create FHIR store in Healthcare API (R4 version)
4. Import data from bucket → FHIR store

### 3. Configure Authentication

```bash
gcloud auth login
gcloud auth application-default login --no-launch-browser
```

### 4. Create config.yml

```yaml
OPENAI_API_KEY: "your-key"
GEMINI_API_KEY: "your-key"
FHIR_CONFIG:
  PROJECT_ID: "your-gcp-project-id"
  LOCATION: "us-central1"
  DATASET_ID: "your-dataset-id"
  STORE_ID: "your-fhir-store-id"
```

### 5. Run Dataset Preparation

```bash
bash scripts/setup_data.sh
python create_question_answer_dataset.py
python create_question_fhir_dataset.py
```

### 6. Run Agents

```bash
# Single-turn FHIR RESTful agent
bash scripts/run_single_turn_request_agent.sh

# Multi-turn iterative agent
bash scripts/run_multi_turn_resource_agent.sh
```

## Key Dependencies

- Google Cloud Healthcare API
- FHIR R4 standard
- OpenAI / Gemini API for agent LLM
- Python 3.11, conda environment

## Example Task

**Question**: "What was the patient's most recent hemoglobin level?"

Agent must:
1. Identify needed FHIR resource: `Observation` (LOINC code 718-7)
2. Query FHIR API with patient ID and LOINC code
3. Parse JSON response to extract value
4. Return: "The patient's hemoglobin was 12.3 g/dL on 2024-01-15"

## Related Summary Files

- `summaries/2025_fhir_agentbench_benchmarking_llm_agents_for_realistic_interoperable_ehr_question_answering_benchmark_summary.md`
