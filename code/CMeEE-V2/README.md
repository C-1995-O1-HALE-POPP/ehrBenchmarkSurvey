# CMeEE-V2: Chinese Medical Named Entity Recognition V2

## Overview
CMeEE-V2 is a dataset for Chinese medical named entity recognition (NER). It is part of the CBLUE benchmark and was originally from the CHIP 2021 shared task. The dataset contains clinical text annotated with medical entities such as diseases, symptoms, drugs, procedures, and body parts.

**Task Type**: Named Entity Recognition (NER)
**Language**: Chinese
**Source**: `Aunderline/CMeEE-V2` on HuggingFace
**License**: MIT

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Train | 15,000 |
| Dev   | 5,000  |
| Test  | test.json (held-out) |

## Field Schema
| Field | Type | Description |
|-------|------|-------------|
| `text` | string | Clinical text passage |
| `entities` | list[object] | List of entity annotations |
| `entities[].start_idx` | int | Character start index of the entity |
| `entities[].end_idx` | int | Character end index of the entity |
| `entities[].type` | string | Entity type label |
| `entities[].entity` | string | The entity text string |

## Entity Types
The dataset includes 11 entity types:
- `dis` (disease/疾病)
- `sym` (symptom/症状)
- `pro` (procedure/手术)
- `bod` (body part/身体部位)
- `dru` (drug/药物)
- `ite` (item examination/检查)
- `mic` (microorganism/微生物)
- `equ` (equipment/医疗设备)
- `dep` (department/科室)
- `lab` (laboratory test/检验指标)
- `sub` (substance/物质)

## Examples

### Example 1
```json
{
  "text": "（5）房室结消融和起搏器植入作为反复发作或难治性心房内折返性心动过速的替代疗法。",
  "entities": [
    {"start_idx": 3, "end_idx": 7, "type": "pro", "entity": "房室结消融"},
    {"start_idx": 9, "end_idx": 13, "type": "pro", "entity": "起搏器植入"},
    {"start_idx": 25, "end_idx": 33, "type": "dis", "entity": "心房内折返性心动过速"}
  ]
}
```

### Example 2
```json
{
  "text": "患者女，54岁，因“发现阴道口肿物1年”入院。",
  "entities": [
    {"start_idx": 12, "end_idx": 16, "type": "bod", "entity": "阴道口"},
    {"start_idx": 16, "end_idx": 18, "type": "sym", "entity": "肿物"}
  ]
}
```

### Example 3
```json
{
  "text": "实验室检查：白细胞计数升高，C反应蛋白增高。",
  "entities": [
    {"start_idx": 6, "end_idx": 10, "type": "lab", "entity": "白细胞计数"},
    {"start_idx": 15, "end_idx": 20, "type": "lab", "entity": "C反应蛋白"}
  ]
}
```

## Access Instructions
```bash
# Download from HuggingFace
curl -L -s "https://huggingface.co/datasets/Aunderline/CMeEE-V2/resolve/main/CMeEE-V2_train.json" -o train.json
curl -L -s "https://huggingface.co/datasets/Aunderline/CMeEE-V2/resolve/main/CMeEE-V2_dev.json" -o dev.json
```

Alternative: `xusenlin/cmeee` on HuggingFace (parquet format with same schema).

## Citation
CMeEE-V2 is part of the CBLUE benchmark. See https://github.com/CBLUEbenchmark/CBLUE for details.
