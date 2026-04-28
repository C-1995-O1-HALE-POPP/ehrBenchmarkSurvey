# EHRSQL

- **Source**: GitHub `glee4810/EHRSQL`
- **Paper**: [EHRSQL: A Practical Text-to-SQL Benchmark for Electronic Health Records](https://arxiv.org/abs/2301.07695) (NeurIPS 2022)
- **Data**: MIMIC-III + eICU clinical databases
- **Examples collected**: 100 (50 train + 50 valid)
- **Access**: Public repo + Google Drive (preprocessed DB) or build from MIMIC-III

## Task Description

EHRSQL is a text-to-SQL benchmark where models must generate executable SQL queries from natural language questions about Electronic Health Records. Three task variants:

1. **Answerable SQL Generation**: answerable question → correct SQL
2. **Answerability Recognition (F1ans)**: classify whether a question is answerable
3. **Executable SQL with Refusal Policy (F1exe)**: generate SQL only for answerable questions, abstain otherwise

## Data Collection

The dataset (questions + SQL queries) is public in the EHRSQL GitHub repo:

```bash
git clone https://github.com/glee4810/EHRSQL.git code/EHRSQL/repo
ls code/EHRSQL/repo/dataset/ehrsql/mimic_iii/
# train.json (9318 questions)
# valid.json (1522 questions)
# test.json (1992 questions)
```

### Database Setup

**Option 1: Preprocessed SQLite** (recommended):
- [MIMIC-III SQLite](https://drive.google.com/file/d/17FkHhaQrmSz5-W2b7WEy90duKfvjBn5x/view) (95 MB)
- [eICU SQLite](https://drive.google.com/file/d/1JG9DUdeJeuIXShK6dDdEJ61NEyPiaGEKZ/view) (102 MB)

**Option 2: Build from MIMIC-III** (you have this locally):
```bash
cd code/EHRSQL/repo/preprocess
python3 preprocess_db.py --data_dir <path_to_mimic_iii_csv> \
  --db_name mimic_iii --deid --timeshift \
  --current_time "2105-12-31 23:59:00" --start_year 2100 \
  --time_span 5 --cur_patient_ratio 0.1
```

## Field Schema

| Field | Type | Description |
|---|---|---|
| `question` | string | Natural language question |
| `query` | string | SQL query (NaN if unanswerable) |
| `db_id` | string | Target database (mimic_iii or eicu) |
| `is_impossible` | bool | Whether the question is unanswerable |
| `department` | list | Hospital department tags |
| `importance` | string | Question importance (high/medium/low) |
| `para_type` | string | Paraphrase source (machine/human) |
| `template` | string | Original template question |

## Sample Examples

### Example 1 (Answerable)
- **Question**: What is the method of intake for clobetasol propionate 0.05% ointment?
- **SQL**: `select distinct prescriptions.route from prescriptions where prescriptions.drug = 'clobetasol propionate 0.05% ointment'`
- **DB**: mimic_iii

### Example 2 (Answerable)
- **Question**: What are the methods of consumption for the send 500mg vial?
- **SQL**: `select distinct prescriptions.route from prescriptions where prescriptions.drug = 'send 500mg vial'`
- **DB**: mimic_iii

### Example 3 (Answerable)
- **Question**: What is the ingesting method for methimazole?
- **SQL**: `select distinct prescriptions.route from prescriptions where prescriptions.drug = 'methimazole'`
- **DB**: mimic_iii

### Example 4
- **Question**: How many patients have been diagnosed with essential hypertension this month?
- **SQL**: `select count(distinct diagnoses_icd.subject_id) from diagnoses_icd join admissions on diagnoses_icd.hadm_id = admissions.hadm_id where diagnoses_icd.icd9_code = '4019' and admissions.admittime >= datetime('now', 'localtime', '-1 month') and admissions.admittime <= datetime('now', 'localtime')`
- **DB**: mimic_iii

### Example 5 (Unanswerable)
- **Question**: tell me what medicine to use to relieve a headache in hypertensive patients.
- **SQL**: (unanswerable — no exact match)
- **DB**: mimic_iii

## Dataset Stats

| Split | Count | Answerable | Unanswerable |
|---|---|---|---|
| train | 9,318 | ~7,974 | ~1,344 |
| valid | 1,522 | ~1,303 | ~219 |
| test | 1,992 | ~1,706 | ~286 |

Questions collected from **222 hospital staff** (physicians, nurses, insurance reviewers, health records teams).

## Related Summary Files

- `summaries/2023_ehrsql_a_practical_text_to_sql_benchmark_for_electronic_health_records_benchmark_summary.md`
- `summaries/2025_medagentgym_a_scalable_agentic_training_environment_for_code_centric_reasoning_in_biomedical_data_science_benchmark_summary.md`
