# MEDIQA-QA — Consumer Health Question Answering

- **Source**: HuggingFace `bigbio/mediqa_qa` (MEDIQA 2019 Shared Task — QA)
- **Config**: mediqa_qa_bigbio_qa / Split: train_alexa
- **Examples collected**: 104

## Task

Answer consumer health questions by retrieving relevant information from medical knowledge sources. Part of the MEDIQA 2019 shared task (ACL-BioNLP workshop). Questions are factoid-style ("What is Flu?", "What causes Flu?") and answers are extracted from consumer health documents.

## Data Format

| Field | Description |
|-------|-------------|
| `id` | Example ID |
| `question` | Consumer health question |
| `type` | Question type (factoid) |
| `context` | Document context |
| `answer` | List of relevant answer passages from knowledge sources |

## Sample Examples

### Example 1

> **Q**: What is Flu?

**Answer** (from 3 sources): *"The flu is an infection of the nose, throat, and lungs. It spreads easily. This article discusses influenza types A and B."* ...

### Example 2

> **Q**: What causes Flu?

**Answer**: *"The flu is caused by an influenza virus. Most people get the flu when they breathe in tiny airborne droplets from the coughs or sneezes of someone who has the flu."* ...

### Example 3

> **Q**: What are the symptoms of Flu?

**Answer** (from 3 sources): *"Flu symptoms will often start quickly...The first symptom is a fever between 102F and 106F...Other common symptoms include: Body aches, Chills, Dizziness, Flushed face, Headache..."*

### Example 4

> **Q**: What are the treatments for Flu?

**Answer** (from 3 sources): *"HOME CARE: Acetaminophen (Tylenol) and ibuprofen (Advil, Motrin) help lower fever...DO NOT use aspirin..."*

### Example 5

> **Q**: How to diagnose Flu?

**Answer** (from 3 sources): *"Your doctor will conduct a physical exam...and possibly order a test that detects influenza viruses...a rapid influenza diagnostics test...can provide results in 30 minutes or less."*

---

*5 of 104 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 104 records

## Reference

Ben Abacha, A., et al. "Overview of the MEDIQA 2019 Shared Task on Consumer Health Question Summarization and Question Answering." *ACL-BioNLP Workshop*, 2019.
