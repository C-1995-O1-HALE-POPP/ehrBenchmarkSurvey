# CMeIE: Chinese Medical Information Extraction

## Overview
CMeIE is a dataset for Chinese medical information extraction, specifically relation extraction. The task is to identify subject-predicate-object (SPO) triples from Chinese clinical texts. It covers 53 pre-defined relation schemas connecting medical entities such as diseases, symptoms, drugs, and procedures.

**Task Type**: Relation Extraction / Information Extraction (IE)
**Language**: Chinese
**Source**: `Aunderline/CMeIE` on HuggingFace
**License**: MIT

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Train | 14,339 |
| Dev   | included |
| Test  | included |

## Relation Schemas
The dataset defines 53 relation schemas spanning domains like:
- Disease-Symptom relations (临床表现, 并发症, 鉴别诊断)
- Disease-Treatment relations (药物治疗, 手术治疗, 预防)
- Disease-Examination relations (实验室检查, 影像学检查)
- Drug-Drug interactions (药物相互作用, 配伍禁忌)

Schema file available in `raw/schemas.jsonl` with fields: `subject_type`, `predicate`, `object_type`.

## Field Schema
| Field | Type | Description |
|-------|------|-------------|
| `text` | string | Clinical text passage |
| `spo_list` | list[object] | List of relation triples |
| `spo_list[].subject` | string | Subject entity text |
| `spo_list[].subject_type` | string | Entity type of subject |
| `spo_list[].predicate` | string | Relation predicate |
| `spo_list[].object.@value` | string | Object entity text |
| `spo_list[].object_type.@value` | string | Entity type of object |
| `spo_list[].Combined` | boolean | Whether this is a combined relation |

## Examples

### Example 1
```json
{
  "text": "产后抑郁症@区分产后抑郁症与轻度情绪失调（产后忧郁或"婴儿忧郁"）是重要的，因为轻度情绪失调不需要治疗。",
  "spo_list": [
    {
      "Combined": false,
      "predicate": "鉴别诊断",
      "subject": "产后抑郁症",
      "subject_type": "疾病",
      "object": {"@value": "轻度情绪失调"},
      "object_type": {"@value": "疾病"}
    }
  ]
}
```

### Example 2
```json
{
  "text": "患者确诊2型糖尿病，给予二甲双胍口服治疗。",
  "spo_list": [
    {"Combined": false, "predicate": "药物治疗", "subject": "2型糖尿病", "subject_type": "疾病", "object": {"@value": "二甲双胍"}, "object_type": {"@value": "药物"}}
  ]
}
```

## Access Instructions
```bash
# Download from HuggingFace
curl -L -s "https://huggingface.co/datasets/Aunderline/CMeIE/resolve/main/CMeIE_train.jsonl" -o train.jsonl
curl -L -s "https://huggingface.co/datasets/Aunderline/CMeIE/resolve/main/53_schemas.jsonl" -o schemas.jsonl
```

Data is in JSONL format (one JSON object per line).

## Citation
CMeIE is from the CHIP shared task series. See https://github.com/CBLUEbenchmark/CBLUE for details.
