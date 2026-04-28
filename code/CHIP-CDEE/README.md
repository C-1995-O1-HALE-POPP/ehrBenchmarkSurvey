# CHIP-CDEE: Clinical Diagnosis Etiology Extraction

## Overview
CHIP-CDEE (Clinical Diagnosis Etiology Extraction) is a dataset for extracting clinical events and their attributes from Chinese medical records. Each event has attributes including a core clinical finding name, its tendency (trend/result), characteristic description, and related anatomical locations.

**Task Type**: Event Extraction / Named Entity Recognition
**Language**: Chinese
**Source**: `Aunderline/CHIP-CDEE` on HuggingFace
**License**: MIT

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Train | 1,587 |
| Test  | 514    |

## Field Schema
| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Unique example identifier |
| `text` | string | Clinical text passage |
| `event` | list[object] | List of annotated events |
| `event[].core_name` | string | Core clinical finding name |
| `event[].tendency` | string | Tendency/trend of the finding |
| `event[].character` | list[string] | Characteristic descriptions |
| `event[].anatomy_list` | list[string] | Related anatomical locations |

## Examples

### Example 1
```json
{
  "id": 268,
  "text": "患者本次发病以来，食欲正常，神志清醒，精神尚可，睡眠欠佳，大便正常，小便正常，体重无明显变化。",
  "event": [
    {"core_name": "食欲", "tendency": "", "character": ["正常"], "anatomy_list": []},
    {"core_name": "神志", "tendency": "", "character": ["清醒"], "anatomy_list": []},
    {"core_name": "精神", "tendency": "", "character": ["尚可"], "anatomy_list": []},
    {"core_name": "睡眠", "tendency": "", "character": ["欠佳"], "anatomy_list": []},
    {"core_name": "大便", "tendency": "", "character": ["正常"], "anatomy_list": []},
    {"core_name": "小便", "tendency": "", "character": ["正常"], "anatomy_list": []},
    {"core_name": "体重", "tendency": "", "character": ["无明显变化"], "anatomy_list": []}
  ]
}
```

### Example 2
```json
{
  "id": 149,
  "text": "肝功仍轻度异常，乙肝标志物示hbsag、hbeab、hbcab阳性。",
  "event": [
    {"core_name": "肝功能异常", "tendency": "", "character": ["轻度"], "anatomy_list": ["肝"]},
    {"core_name": "hbsag", "tendency": "", "character": ["阳性"], "anatomy_list": []},
    {"core_name": "hbeab", "tendency": "", "character": ["阳性"], "anatomy_list": []},
    {"core_name": "hbcab", "tendency": "", "character": ["阳性"], "anatomy_list": []}
  ]
}
```

## Access Instructions
```bash
# Download from HuggingFace
curl -L -s "https://huggingface.co/datasets/Aunderline/CHIP-CDEE/resolve/main/CHIP-CDEE_train.json" -o train.json
curl -L -s "https://huggingface.co/datasets/Aunderline/CHIP-CDEE/resolve/main/CHIP-CDEE_test.json" -o test.json
```

Also available via datasets-server API:
```bash
curl -s "https://datasets-server.huggingface.co/rows?dataset=Aunderline/CHIP-CDEE&config=default&split=train&offset=0&length=100"
```

## Citation
Part of the CHIP (China Health Information Processing) conference shared tasks and CBLUE benchmark.
