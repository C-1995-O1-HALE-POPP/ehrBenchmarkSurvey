# MMedBench

## Overview

MMedBench is a **multilingual medical MCQA (Multiple Choice Question Answering)** benchmark for evaluating large language models in clinical medicine. It contains 45,048 QA pairs for training and 8,518 QA pairs for testing across 6 languages. Each sample includes a medical question, multiple-choice options, the correct answer with index, and a rationale (reference explanation).

- **Source**: HuggingFace `Henrychur/MMedBench`
- **Paper**: [Towards Building Multilingual Language Model for Medicine](https://arxiv.org/abs/2402.13963)
- **GitHub**: [Magic-AI4Med/MMedLM](https://github.com/Magic-AI4Med/MMedLM)
- **License**: CC-BY-NC 4.0
- **Task**: Question answering (multiple choice with rationale)
- **Format**: JSONL (one JSON object per line)
- **Examples collected**: 270 (45 per language)

## Languages & Splits

| Language  | Train   | Test  | Total   |
|-----------|---------|-------|---------|
| Chinese   | 27,400  | 3,426 | 30,826  |
| English   | 10,178  | 1,273 | 11,451  |
| Spanish   | 2,657   | 2,742 | 5,399   |
| French    | 2,171   | 622   | 2,793   |
| Japanese  | 1,590   | 199   | 1,789   |
| Russian   | 1,052   | 256   | 1,308   |
| **Total** | **45,048** | **8,518** | **53,566** |

## Dataset Structure

```
MMedBench/
├── Train/
│   ├── Chinese.jsonl
│   ├── English.jsonl
│   ├── French.jsonl
│   ├── Japanese.jsonl
│   ├── Russian.jsonl
│   └── Spanish.jsonl
└── Test/
    ├── Chinese.jsonl
    ├── English.jsonl
    ├── French.jsonl
    ├── Japanese.jsonl
    ├── Russian.jsonl
    └── Spanish.jsonl
```

### Fields

| Field | Description |
|-------|-------------|
| `question` | Clinical multiple-choice question |
| `options` | Dict of `{label: text}` answer choices (A/B/C/D) |
| `answer` | The correct answer text |
| `answer_idx` | Index of correct answer (A/B/C/D) |
| `meta_info` | Topic/metadata (e.g., "step1", medical specialty) |
| `rationale` | Explanation for the correct answer |
| `human_checked` | Whether human-verified (0/1) |
| `human_check_passed` | Whether human check passed (0/1) |

### English Example

```
Question: A 39-year-old woman presents to her primary care physician
because she has been experiencing intermittent abdominal pain for the
last 2 weeks. She says that the pain is squeezing in nature, is located
in the right upper quadrant, and is particularly severe after eating...

Options:
  A: Connective tissue that envelops the other layers
  B: Contains cells that primarily absorb nutrients
  C: Contains large blood vessels and large lymphatic vessels
  D: Contracts to generate peristaltic waves

Answer: C
Topic: step1
```

### Chinese Example

```
Question: 卧位腰椎穿刺，脑脊液压力正常值是（　　）。
Options:
  A: 80～180mmH2O（0.78～1.76kPa）
  B: 50～70mmH2O（0.49～0.69kPa）
  C: 230～250mmH2O（2.25～2.45kPa）
  D: 260～280mmH2O（2.55～2.74kPa）

Answer: A
Topic: 第三部分　精神神经系统疾病
```

## Data Files

- `raw/examples.json` — 270 records (45 per language, mixed Train/Test)

## Access

```bash
# Download full zip (20.7 MB)
curl -L "https://huggingface.co/datasets/Henrychur/MMedBench/resolve/main/MMedBench.zip" -o MMedBench.zip
unzip MMedBench.zip
```

## Citation

```bibtex
@article{qiu2024towards,
  title={Towards Building Multilingual Language Model for Medicine},
  author={Qiu, Pengcheng and Wu, Chaoyi and Zhang, Xiaoman and Lin, Weixiong and
          Wang, Haicheng and Zhang, Ya and Wang, Yanfeng and Xie, Weidi},
  journal={arXiv preprint arXiv:2402.13963},
  year={2024}
}
```
