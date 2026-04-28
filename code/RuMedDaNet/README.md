# RuMedDaNet

## Overview
RuMedDaNet is a yes/no medical question answering dataset in Russian. It consists of medical context passages with associated binary questions, testing whether a model can correctly answer medical domain questions.

## Task
- **Binary Question Answering** (Yes/No)
- **Language**: Russian
- **Domain**: Medical (pharmacology, anatomy, therapeutic medicine, biochemistry, etc.)

## Dataset Statistics
- Training: 1,052 examples
- Development: 256 examples
- Test: 256 examples
- Private test: available on MedBench platform

## Data Format
JSONL with fields: `context` (medical text passage), `question`, `answer` (yes/no)

## Source
- GitHub: `sb-ai-lab/MedBench` (RuMedBench)
- Paper: Blinov et al., "RuMedBench: A Russian Medical Language Understanding Benchmark" (2022)

## Download Status
Downloaded 200 examples from RuMedBench GitHub repository.

## References
- https://github.com/sb-ai-lab/MedBench
- https://medbench.ru/
