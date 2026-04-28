# MTSamples

**Category**: Treatment Plan Generation from Medical Transcriptions (P2 - Clinical Reasoning)

## Overview
MTSamples is a dataset of transcribed medical transcription sample reports and examples, originally scraped from mtsamples.com. Contains 4,999 medical transcriptions across multiple specialties. Used for text generation, classification, and treatment plan extraction tasks.

- **Original Source**: https://www.mtsamples.com/
- **HuggingFace Dataset**: https://huggingface.co/datasets/harishnair04/mtsamples (4,999 rows)
- **HuggingFace (Alternative)**: https://huggingface.co/datasets/tchebonenko/MedicalTranscriptions
- **Kaggle**: https://www.kaggle.com/tboyle10/medicaltranscriptions/data
- **No standalone GitHub repo exists** - dataset is distributed via HuggingFace/Kaggle

## Dataset
- **Size**: 4,999 rows, ~17MB
- **Format**: Data frame with columns: `note_id`, `description`, `medical_specialty`, `sample_name`, `transcription`, `keywords`
- **Specialties**: Urology, Obstetrics/Gynecology, Neurology, Gastroenterology, General Medicine, Radiology, Orthopedic, Cardiovascular/Pulmonary, Surgery, and more
- **Sample types**: SOAP/Chart/Progress Notes (167+), consult notes, operative reports, discharge summaries, etc.

## Setup

```bash
# Load via HuggingFace datasets
pip install datasets
```

```python
from datasets import load_dataset

dataset = load_dataset("harishnair04/mtsamples")
# dataset['train'] contains all 4,999 rows
```

Or via Kaggle:
```bash
kaggle datasets download tboyle10/medicaltranscriptions
```

## Dataset Features
| Column | Description |
|--------|-------------|
| `note_id` | Unique identifier for each note |
| `description` | Description or chief concern |
| `medical_specialty` | Medical specialty of the note |
| `sample_name` | mtsamples.com note name |
| `transcription` | Full transcription text |
| `keywords` | Associated keywords |

## Usage Examples

### Treatment Plan Extraction
Use the transcription text as input for LLM-based treatment plan generation. Filter by specialty (e.g., Surgery, Orthopedic) to focus on procedure-heavy specialties.

### Text Classification
Fine-tune models to classify medical specialty from transcription text:
```python
# Example: HuggingFace model
# mnaylor/base-bert-finetuned-mtsamples
```

### Clinical NLP
- Entity extraction from transcription text
- ICD code assignment
- Procedure identification
- Treatment plan summarization

## Alternative: MedicalTranscriptions (tchebonenko)
https://huggingface.co/datasets/tchebonenko/MedicalTranscriptions
- Same source data (mtsamples.com)
- Selection for specific specialties
- Used for medical NLP training

## Dependencies
- `datasets` library (HuggingFace)
- Python 3.x
- Optional: Kaggle API for Kaggle download

## Notes
- Data is user-contributed reference examples; may not be complete or error-free
- All reports are for educational reference purposes
- Licenses: Original mtsamples.com data is for educational use; check HuggingFace dataset licenses
- This is a general medical transcription corpus, not a pre-structured treatment planning benchmark. Benchmark construction requires defining treatment plan generation/extraction tasks on this data.
