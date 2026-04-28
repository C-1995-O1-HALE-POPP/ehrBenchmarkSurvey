# MedAgentBench

**Category**: FHIR-based Clinical Workflow Agent (P2 - Clinical Reasoning)

## Overview
MedAgentBench (NEJM AI, 2025) is a comprehensive evaluation suite for benchmarking LLM agents in medical records settings. Unlike traditional QA benchmarks, MedAgentBench challenges AI agents with 300 clinically relevant tasks requiring interactive FHIR API operations. Built on a FHIR-compliant environment with 100 de-identified realistic patient profiles and 700,000+ medical data points.

- **Paper**: [NEJM AI (2025)](https://ai.nejm.org/doi/full/10.1056/AIdbp2500144)
- **Repo**: https://github.com/stanfordmlgroup/MedAgentBench
- **Docker Image**: `jyxsu6/medagentbench:latest`
- **Reference Solutions**: [Stanford Box](https://stanfordmedicine.box.com/s/fizv0unyjgkb1r3a83rfn5p3dc673uho)

## Dataset
- **300 clinically-derived tasks** across 10 medical categories
- **100 de-identified realistic patient profiles** with 700k+ FHIR records
- **10 task categories** covering essential clinical workflows
- **9 FHIR API functions**: condition.search, lab.search, vital.search, vital.create, medicationrequest.search, medicationrequest.create, procedure.search, observation.search, patient.search

## Setup

### Prerequisites
```bash
# Install dependencies
conda create -n medagentbench python=3.9
conda activate medagentbench
pip install -r repo/requirements.txt

# Verify Docker
docker ps
```

### Step 1: Start FHIR Server
```bash
docker pull jyxsu6/medagentbench:latest
docker tag jyxsu6/medagentbench:latest medagentbench
docker run -p 8080:8080 medagentbench
```
Verify: `http://localhost:8080/` should show the FHIR server console.

### Step 2: Download Reference Solutions
Download `refsol.py` from [Stanford Box](https://stanfordmedicine.box.com/s/fizv0unyjgkb1r3a83rfn5p3dc673uho) and place as `src/server/tasks/medagentbench/refsol.py`.

### Step 3: Configure Agent
```bash
# Set OpenAI API key in configs/agents/openai-chat.yaml
# Test configuration
python -m src.client.agent_test --config configs/agents/api_agents.yaml --agent gpt-4o-mini
```

### Step 4: Run Evaluation
```bash
# Terminal 1: Start task server (wait ~1 min for "200 OK")
python -m src.start_task -a

# Terminal 2: Start tasks
python -m src.assigner
```

### Step 5: View Results
Results at `outputs/MedAgentBenchv1/gpt-4o-mini/medagentbench-std/overall.json`.

## Architecture
MedAgentBench is built on top of **AgentBench** and uses:
- **FHIR Server**: HAPI FHIR JPA (H2 persistent storage)
- **Task Controller**: Manages 20 task workers on ports 5000-5015
- **Agent Orchestrator**: Inspired by BFCL, exposes 9 FHIR functions to the agent
- **Docker-based**: Entire environment runs in Docker containers

## Task Categories (10)
Tasks span essential clinical workflows covering condition management, lab orders, vital signs, medication management, procedures, and observations.

## Evaluation
- Agents are evaluated on task completion accuracy
- Requires correct FHIR API calls, parameter passing, and result interpretation
- Evaluates decision-making, planning, and execution within EHRs

## Dependencies
- Docker (for FHIR server)
- Python 3.9
- Conda environment with `requirements.txt`
- OpenAI API key (for default agent; supports Gemini, Claude via Vertex AI)
- `refsol.py` reference solutions (Stanford Box download)

## Citation
```bibtex
@article{jiang2025medagentbench,
  title={MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents},
  author={Jiang, Yixing and Black, Kameron C and Geng, Gloria and Park, Danny and Zou, James and Ng, Andrew Y and Chen, Jonathan H},
  journal={NEJM AI},
  pages={AIdbp2500144},
  year={2025},
  publisher={Massachusetts Medical Society}
}
```
