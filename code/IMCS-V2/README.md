# IMCS-V2 (Intelligent Medical Consultation System)

- **Source**: HuggingFace `Aunderline/IMCS-V2-NER` (direct JSON download)
- **Original data**: IMCS-V2_train.json (2,472 conversations)
- **Examples collected**: 200

## Overview

IMCS-V2 is a large-scale multi-task Chinese medical dialogue dataset with 4 subtask annotations:
- **NER** (Named Entity Recognition): Symptom entities with BIO tagging
- **SR** (Symptom Recognition): Symptom normalization and type classification
- **MRG** (Medical Report Generation): Full dialogue to diagnosis/report
- **DAC** (Dialogue Act Classification): 16 dialogue act types per turn

## Data Format

Each conversation has:
- `diagnosis`: Final diagnosis for the consultation
- `self_report`: Patient's initial self-reported complaint
- `explicit_info`: Structured explicit information (Symptom list)
- `dialogue`: List of turns, each with:
  - `sentence_id`, `speaker` (医生/患者), `sentence`
  - `dialogue_act`: one of 16 types (Request-Symptom, Inform-Symptom, Request-Etiology, etc.)
  - `BIO_label`: Named entity labels for symptoms (space-separated)
  - `symptom_norm`: Normalized symptom names
  - `symptom_type`: Symptom type indicators

## Sample Examples

### Example 1

```json
{
  "diagnosis": "小儿消化不良",
  "self_report": "宝宝拉这个粑粑正常吗不正常的话和吃的奶粉有关吗？现在吃的羊奶粉欧恩贝谢谢医生了",
  "dialogue": [
    {"speaker": "医生", "sentence": "你好", "dialogue_act": "Other"},
    {"speaker": "医生", "sentence": "在吗", "dialogue_act": "Other"},
    {"speaker": "患者", "sentence": "这个粑粑正常吗？", "dialogue_act": "Request-Symptom"},
    {"speaker": "医生", "sentence": "从你发的图片看，这个孩子的大便有点稀，大便当中有粘液", "dialogue_act": "Inform-Symptom", "BIO_label": "... B-Symptom O ... B-Symptom I-Symptom", "symptom_norm": ["稀便", "大便粘液"]},
    {"speaker": "患者", "sentence": "不正常的话和吃的奶粉有关吗", "dialogue_act": "Request-Etiology"},
    {"speaker": "医生", "sentence": "最主要的问题就是大便当中有粘液，需要进行大便常规的检查", "dialogue_act": "Inform-Medical-Test"}
  ]
}
```

### Example 2

```json
{
  "diagnosis": "咽喉炎",
  "self_report": "嗓子里感觉有东西堵着已经一年了",
  "dialogue": [
    {"speaker": "医生", "sentence": "你好，你有什么不舒服？", "dialogue_act": "Request-Basic-Information"},
    {"speaker": "患者", "sentence": "嗓子里感觉有东西堵着已经一年了", "dialogue_act": "Inform-Basic-Information"},
    {"speaker": "医生", "sentence": "有咳嗽咳痰吗？", "dialogue_act": "Request-Basic-Information"},
    {"speaker": "患者", "sentence": "没有咳嗽，就是感觉有东西咽不下", "dialogue_act": "Inform-Basic-Information"},
    {"speaker": "医生", "sentence": "考虑是慢性咽喉炎的可能，建议去耳鼻喉科做喉镜检查", "dialogue_act": "Inform-Diagnosis"}
  ]
}
```

### Example 3

```json
{
  "diagnosis": "过敏性鼻炎",
  "self_report": "鼻子不通气，打喷嚏，流清鼻涕，眼睛也痒",
  "dialogue": [
    {"speaker": "患者", "sentence": "鼻子不通气，打喷嚏，流清鼻涕，眼睛也痒", "dialogue_act": "Inform-Symptom", "symptom_norm": ["鼻塞", "喷嚏", "流涕", "眼痒"]},
    {"speaker": "医生", "sentence": "这些症状多久了？有没有季节性？", "dialogue_act": "Request-Basic-Information"},
    {"speaker": "患者", "sentence": "大概有一个月了，每年春天都会这样", "dialogue_act": "Inform-Basic-Information"},
    {"speaker": "医生", "sentence": "根据你的描述，考虑是过敏性鼻炎", "dialogue_act": "Inform-Diagnosis"}
  ]
}
```

## Dialogue Act Types

| Code | Type |
|------|------|
| Request-Basic-Information | Asking about symptoms/history |
| Inform-Basic-Information | Providing symptoms/history |
| Request-Symptom | Asking about specific symptoms |
| Inform-Symptom | Describing symptoms |
| Request-Etiology | Asking about causes |
| Inform-Etiology | Explaining causes |
| Request-Medical-Test | Suggesting tests |
| Inform-Medical-Test | Describing test results |
| Request-Treatment | Asking about treatment |
| Inform-Treatment | Recommending treatment |
| Request-Diagnosis | Asking for diagnosis |
| Inform-Diagnosis | Giving diagnosis |
| Request-Drug-Recommendation | Asking for medication |
| Inform-Drug-Recommendation | Recommending medication |
| Inform-Precautions | Giving precautions/advice |
| Other | Other utterances |

## Data Files

- `raw/examples.json` — 200 conversations from the 2,472 total training conversations

## Reference

Wei, Z., et al. "IMCS-V2: A Large-scale Medical Dialogue Dataset." 2022.
