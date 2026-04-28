# RuMedNLI

## Overview
RuMedNLI (Russian Medical Natural Language Inference) is the Russian-language counterpart of the MedNLI dataset. It consists of premise-hypothesis pairs from clinical text, where the task is to determine whether the hypothesis is entailed by, contradicted by, or neutral to the premise.

## Task
- **Natural Language Inference (NLI)**
- **Classes**: entailment, contradiction, neutral
- **Language**: Russian
- **Domain**: Clinical (translated from MIMIC-III Past Medical History)

## Dataset Statistics
- Training: 11,232 pairs
- Development: 1,395 pairs
- Test: 1,422 pairs
- Private test: available on MedBench platform

## Data Format
JSONL with fields: `ru_sentence1` (premise), `ru_sentence2` (hypothesis), `gold_label` (entailment/contradiction/neutral)

## Source
- GitHub: `sb-ai-lab/MedBench` (RuMedBench)
- Original: PhysioNet (credentialed access required)
- Paper: Blinov et al., "RuMedBench: A Russian Medical Language Understanding Benchmark" (2022)

## Download Status
Downloaded 150 examples from RuMedBench GitHub repository.

## References
- https://github.com/sb-ai-lab/MedBench
- https://physionet.org/content/rumednli-russian-inference/
- https://medbench.ru/
