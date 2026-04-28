# MentalHealth (Counseling Conversations)

## Overview

A dataset of mental health counseling conversations between individuals and licensed professionals, structured as question-answer pairs. Useful for evaluating empathetic response generation and clinical counseling dialogue.

- **HuggingFace**: [Amod/mental_health_counseling_conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)
- **DOI**: 10.57967/hf/1581
- **License**: Other (research use)
- **Language**: English
- **Domain**: Mental health counseling
- **Task**: Response generation / empathetic dialogue

## Dataset Structure

| Field | Description |
|-------|-------------|
| `Context` | User's question or mental health concern |
| `Response` | Counselor's professional response |

### Example

```
Context: "I'm going through some things with my feelings and myself.
I barely sleep and I do nothing but think about how I'm worthless..."

Response: "If everyone thinks you're worthless, then maybe you need to
find new people to hang out with. Seriously, the social context in which
a person lives is a big influence in self-esteem..."
```

## Access

```python
from datasets import load_dataset
ds = load_dataset("Amod/mental_health_counseling_conversations")
```

## Note

This dataset was found by searching "mental_health_counseling" on HuggingFace. If the intended benchmark was a different counselor response generation dataset, please search for the specific paper or group that created it.
