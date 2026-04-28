# EHRSQL 2024 Shared Task

- **Source**: GitHub `glee4810/ehrsql-2024`
- **Paper**: [Overview of the EHRSQL 2024 Shared Task](https://arxiv.org/abs/2405.06673)
- **Data**: MIMIC-IV Clinical Demo Database (open access, no PhysioNet credential needed!)
- **Access**: Public GitHub + PhysioNet demo (ODC Open Database License)

## Task Description

Reliable Text-to-SQL on EHR with abstention. Models must:
1. Generate correct SQL for answerable questions
2. Abstain (return null) for unanswerable questions
3. Maximize F1exe (execution accuracy with refusal penalty)

## Dataset

| Split | Count |
|---|---|
| train | 5,124 |
| valid | 1,163 |
| test | 1,167 |

Total: 7,454 questions over MIMIC-IV demo schema.

### Compared to EHRSQL (MIMIC-III)

- Uses MIMIC-IV schema (more modern, more tables)
- Demo dataset is **publicly accessible** (no PhysioNet credential required!)
- Focus on reliability evaluation (abstention policy)

## Setup

### 1. Download MIMIC-IV Demo Database

```bash
wget https://physionet.org/static/published-projects/mimic-iv-demo/mimic-iv-clinical-database-demo-2.2.zip
unzip mimic-iv-clinical-database-demo-2.2
gunzip -r mimic-iv-clinical-database-demo-2.2
```

### 2. Preprocess

```bash
cd code/EHRSQL-2024/repo/preprocess
bash preprocess.sh
cd ../..
```

### 3. Data Format

```
train_data.json: {"version": "...", "data": [{"id": "...", "question": "..."}, ...]}
train_label.json: {"id1": "SELECT ...", "id2": null, ...}
```

## Related Summary Files

- `summaries/2024_overview_of_the_ehrsql_2024_shared_task_on_reliable_text_to_sql_modeling_on_electronic_health_records_benchmark_summary.md`
