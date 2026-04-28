# PMC-Patients

**Category**: Patient Information Extraction from PMC (P2 - Clinical Reasoning)

## Overview
PMC-Patients is a large-scale dataset of 167k patient summaries extracted from case reports in PubMed Central (PMC), annotated with 3.1M patient-article relevance and 293k patient-patient similarity annotations via the PubMed citation graph. Defines two Retrieval-based Clinical Decision Support (ReCDS) tasks: Patient-to-Article Retrieval (PAR) and Patient-to-Patient Retrieval (PPR).

- **Paper**: [Scientific Data 10, 909 (2023)](https://www.nature.com/articles/s41597-023-02814-8)
- **Repo**: https://github.com/pmc-patients/pmc-patients
- **Data**: [Figshare](https://figshare.com/collections/PMC-Patients/6723465) or [HuggingFace](https://huggingface.co/zhengyun21)
- **Leaderboard**: https://pmc-patients.github.io/
- **License**: CC BY-NC-SA

## Dataset

### PMC-Patients.json
Core dataset with patient summaries and relational annotations:
- 167k patient summaries extracted from PMC case reports
- Each entry: `patient_id`, `patient_uid` (PMID-x format), `PMID`, `title`, `patient` note, `age`, `gender`, `relevant_articles`, `similar_patients`

### ReCDS Benchmark (BEIR format)
- **PAR (Patient-to-Article Retrieval)**: Query patients → 11.7M PubMed article corpus
- **PPR (Patient-to-Patient Retrieval)**: Query patients → 155.2k patient corpus
- Split: train/dev/test with queries in `.jsonl`, qrels in `.tsv` (TREC format)

## Setup

```bash
# Download data from Figshare or HuggingFace (no DUA required)
# https://figshare.com/collections/PMC-Patients/6723465
# https://huggingface.co/zhengyun21

# Unzip and place datasets/ folder in repo root
cd repo

# Install dependencies
pip install -r requirements.txt
```

## Evaluation

```bash
# Run evaluation for PPR (Patient-to-Patient Retrieval)
python evaluation.py --task PPR --split test --result_path YOUR_RESULT_PATH

# Run evaluation for PAR (Patient-to-Article Retrieval)
python evaluation.py --task PAR --split test --result_path YOUR_RESULT_PATH
```

Results format (JSON):
```json
{
    "query_id": {
        "doc_id": relevance_score,
        ...
    }
}
```

## Data Format Details

### Query files (JSONL)
```json
{"_id": "patient_uid", "text": "patient summary text"}
```

### Corpus files (JSONL)
- PAR: `{"_id": "PMID", "title": "...", "text": "abstract"}`
- PPR: `{"_id": "patient_uid", "title": "", "text": "patient summary"}`

### Qrels (TSV)
```
query_id\tcorpus_id\tscore
```

Scores: 2 (high relevance/similarity) or 1 (low relevance/similarity).

## Dataset Collection Code
Full collection pipeline and baseline retrievers available at https://github.com/zhao-zy15/PMC-Patients.

## Dependencies
- Data download from Figshare or HuggingFace (no DUA/credentials needed)
- `requirements.txt` (evaluation code dependencies)
- BEIR evaluation framework (integrated in `evaluation.py`)
