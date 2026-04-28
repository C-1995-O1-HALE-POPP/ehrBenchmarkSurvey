# CHIP-CTC: Clinical Trial Criteria Classification

## Overview
CHIP-CTC is a dataset for classifying clinical trial eligibility criteria into predefined categories. Given a clinical trial screening criterion sentence, the task is to classify it into one of 44+ categories such as "疾病" (disease), "治疗或手术" (treatment/surgery), "药物" (drug), "年龄" (age), "实验室检查" (lab test), etc. This task is formulated as a multi-class single-label classification problem with varying answer choices per example.

**Task Type**: Text Classification (multi-class, single-label, with per-example candidate labels)
**Language**: Chinese
**Source**: `AIBoy1993/Prompt-CHIP-CTC` on HuggingFace (prompt-formatted version)
**License**: Not specified

## Dataset Statistics
| Split | Examples |
|-------|----------|
| Train | 6,000    |
| Dev   | included  |
| Test  | included  |

## Field Schema
| Field | Type | Description |
|-------|------|-------------|
| `input` | string | Prompt-formatted input with the criterion text and candidate labels |
| `target` | string | Correct classification label |
| `answer_choices` | list[string] | Candidate label options for this example |
| `task_type` | string | Always "cls" (classification) |
| `task_dataset` | string | Always "CHIP-CTC" |
| `sample_id` | string | Unique sample identifier |

## Label Categories (44 total)
The dataset uses up to 44 categories per example, including but not limited to:
`器官组织状态`, `设备`, `药物`, `睡眠`, `症状(患者感受)`, `伦理审查`, `病例来源`, `成瘾行为`, `治疗或手术`, `酒精使用`, `种族`, `风险评估`, `疾病`, `残疾群体`, `锻炼`, `读写能力`, `居住情况`, `教育情况`, `受体状态`, `数据可及性`, `肿瘤进展`, `年龄`, `性别`, `实验室检查`, `诊断`, `知情同意`, `预期寿命`, etc.

## Examples

### Example 1
```json
{
  "input": "⑨需进行西医系统治疗的患者。\n这句话是什么临床试验筛选标准类型？\n类型选项：器官组织状态，设备，药物，睡眠，症状(患者感受)，伦理审查，病例来源，成瘾行为，治疗或手术，酒精使用，种族，风险评估，疾病，残疾群体，锻炼，读写能力，居住情况，教育情况，受体状态，数据可及性，肿瘤进展\n答：",
  "target": "治疗或手术",
  "answer_choices": ["器官组织状态", "设备", "药物", "睡眠", "症状(患者感受)", "伦理审查", "病例来源", "成瘾行为", "治疗或手术", "酒精使用", "种族", "风险评估", "疾病", "残疾群体", "锻炼", "读写能力", "居住情况", "教育情况", "受体状态", "数据可及性", "肿瘤进展"]
}
```

### Example 2
```json
{
  "input": "判断临床试验筛选标准的类型：\n3. 阿片类药物滥用成瘾或有吸毒病史患者；\n选项：依存性，体征(医生检测），献血，睡眠，病例来源，成瘾行为，怀孕相关，治疗或手术，设备，知情同意\n答：",
  "target": "成瘾行为",
  "answer_choices": ["依存性", "体征(医生检测）", "献血", "睡眠", "病例来源", "成瘾行为", "怀孕相关", "治疗或手术", "设备", "知情同意"]
}
```

### Example 3
```json
{
  "input": "1、符合中华人民共和国医政司编写的《常见恶性肿瘤诊治规范》中的诊断标准。估计生存期超过3个月；\n这句话是什么临床试验筛选标准类型？\n类型选项：...[44 options]...\n答：",
  "target": "诊断"
}
```

## Access Instructions
```bash
# Download prompt-formatted version from HuggingFace (JSONL format)
curl -L -s "https://huggingface.co/datasets/AIBoy1993/Prompt-CHIP-CTC/resolve/main/train_CHIP-CTC.json" -o train.jsonl
```

For the original (non-prompt) format, please refer to the official CBLUE benchmark:
- GitHub: https://github.com/CBLUEbenchmark/CBLUE

## Citation
CHIP-CTC is part of the CHIP conference shared tasks and CBLUE benchmark.
