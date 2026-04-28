# emrQA

- **Source**: GitHub `emrqa/emrQA` + i2b2/n2c2 portal
- **Paper**: [emrQA: A Large Corpus for Question Answering on Electronic Medical Records](http://aclweb.org/anthology/D18-1258) (EMNLP 2018)
- **Access**: Licensed under i2b2/n2c2 — download from portal after signing DUA
- **Priority**: P3 (gated, requires i2b2/n2c2 data use agreement)

## Dataset Stats

| Source Dataset | QA Pairs | Clinical Notes |
|---|---|---|
| i2b2 relations (concepts, relations, assertions) | 1,322,789 | 425 |
| i2b2 medications | 226,128 | 261 |
| i2b2 heart disease risk | 49,897 | 119 |
| i2b2 smoking | 4,518 | 502 |
| i2b2 obesity | 354,503 | 1,118 |
| **Total** | **1,957,835** | **2,425** |

## Data Access

1. Go to: https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/
2. Sign the data use agreement (typically approved same day)
3. Look under "Community Annotations Downloads" for emrQA
4. Download the JSON dataset (~1.96M QA pairs)

## Alternative: Build from Source

If you have the i2b2 challenge datasets:

```bash
git clone https://github.com/emrqa/emrQA.git
cd emrQA
pip install -r requirements.txt
# Download i2b2 datasets to ./i2b2/ directory
python main.py  # generates output/data.json
```

## Data Format

SQuAD-style JSON:
```json
{
  "data": [{
    "title": "i2b2 medications",
    "paragraphs": [{
      "context": "clinical note text",
      "note_id": "12345",
      "qas": [{
        "question": "What medications were prescribed?",
        "answers": [{
          "text": "metformin",
          "evidence": "Patient continued on metformin 500mg BID",
          "answer_entity_type": "single"
        }]
      }]
    }]
  }]
}
```

## Task Types

- **emrQA**: General clinical QA from i2b2 notes
- Sub-tasks: medication QA, relation QA, risk factor QA, smoking QA, obesity QA

## Related Summary Files

- `summaries/2018_emrqa_a_large_corpus_for_question_answering_on_electronic_medical_records_benchmark_summary.md`
