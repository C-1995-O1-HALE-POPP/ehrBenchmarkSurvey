# MedQSum (Medical Question Summarization)

- **Source**: Not available on HuggingFace
- **Original source**: NLM/MeQSum dataset
- **Examples collected**: 0

## Overview

MedQSum (also known as MeQSum) is a dataset for medical question summarization. The task is to generate concise summary questions from verbose consumer health questions (CHQs). This helps in improving question-answering systems by reformulating long, noisy consumer queries into clear, focused medical questions.

## Task Description

Given a verbose consumer health question (CHQ), the system must:
- Identify the core medical intent
- Remove extraneous personal details and narrative elements
- Produce a concise, well-formed medical question suitable for QA systems

## Related Datasets on HuggingFace

Search for related consumer health question datasets:
- `bigbio/meddialog` — Medical dialogues
- `wangrongsheng/icliniq-10k-en` — Online medical consultations

## Search Status

Searched HuggingFace for: `medqsum`, `meqsum`, `medical question summarization`, `CHQ`, `consumer health question` — no matching dataset found.

The original MeQSum dataset is distributed by the U.S. National Library of Medicine (NLM).

## Data Files

- `raw/examples.json` — 0 records (not yet downloaded)

## Reference

Ben Abacha, A. & Demner-Fushman, D. "On the Summarization of Consumer Health Questions." Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics (ACL), 2019.

MeQSum dataset: https://github.com/abachaa/MeQSum
