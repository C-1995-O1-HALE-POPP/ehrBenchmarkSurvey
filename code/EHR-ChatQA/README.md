# EHR-ChatQA

- **Source**: GitHub `glee4810/EHR-ChatQA`
- **Paper**: [From Conversation to Query Execution](https://openreview.net/forum?id=hLweUPBz7k) (ICLR 2026)
- **Data**: MIMIC-IV Star + eICU Star SQLite databases (Google Drive)
- **Access**: Public repo + Google Drive databases

## Task Description

Multi-turn EHR database conversations with simulated users. Two task types:

1. **Incremental Query Refinement (IncreQA)**: User asks a question, agent queries DB, user follows up — agent must refine and re-query
2. **Adaptive Query Refinement (AdaptQA)**: Agent must adapt SQL queries based on conversation context

## Environments

| Environment | IncreQA Tasks | AdaptQA Tasks |
|---|---|---|
| MIMIC-IV Star | 145 | 40 |
| eICU Star | 141 | 40 |
| **Total** | **286** | **80** |

## Setup

### 1. Install

```bash
cd code/EHR-ChatQA/repo
pip install -r requirements.txt
```

### 2. Download Databases

```bash
pip install gdown
bash download_db.sh
# Downloads mimic_iv_star.sqlite + eicu_star.sqlite
```

### 3. Configure API Keys

Create `.env`:
```
OPENAI_API_KEY=...
GOOGLE_API_KEY=...
TAVILY_API_KEY=...
```

### 4. Run

```bash
python run.py --env mimic_iv_star --task_type incre \
  --model gemini/gemini-2.5-flash --agent_strategy tool-calling --num_trials 5
```

## Evaluation

- **IncreQA**: Exact set match between agent SQL result and gold answer
- **AdaptQA**: Fuzzy string matching on `<answer>` tags
- Metrics: SR-k, Pass@k, Pass^k, Gap-k

## Related Summary Files

- `summaries/2025_from_conversation_to_query_execution_benchmarking_user_and_tool_interactions_for_ehr_database_agents_benchmark_summary.md`
