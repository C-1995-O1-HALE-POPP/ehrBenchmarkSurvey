# Medec — Medical Error Detection and Correction

- **Source**: HuggingFace `expx/MEDEC-MS` (Medical Error Detection and Correction — Medical Summaries)
- **Config**: default / Split: train
- **Examples collected**: 100

## Task

Detect and correct medical errors in clinical text summaries. Each example is a clinical vignette that may contain an introduced factual error (e.g., wrong causal organism). The task is to identify the erroneous sentence and provide the corrected version.

## Data Format

| Field | Description |
|-------|-------------|
| `Text ID` | Example identifier (ms-train-N) |
| `Text` | Full clinical vignette (may contain error) |
| `Sentences` | Sentence-segmented version |
| `Error Flag` | 1 = contains error, 0 = error-free |
| `Error Type` | Type of introduced error (e.g., causalOrganism) |
| `Error Sentence ID` | Index of the erroneous sentence (0-based) |
| `Error Sentence` | The sentence containing the error |
| `Corrected Sentence` | The corrected version of the sentence |
| `Corrected Text` | Full text with the correction applied |

## Sample Examples

### Example 1 (Error: causalOrganism)

> A 53-year-old man comes to the physician because of a 1-day history of fever and chills, severe malaise, and cough with yellow-green sputum...

- **Error**: "After reviewing imaging, the causal pathogen was determined to be **Haemophilus influenzae**."
- **Corrected**: "After reviewing imaging, the causal pathogen was determined to be **Streptococcus pneumoniae**."

### Example 2 (No Error)

> Same vignette as Example 1 but without introduced error. All sentences are factually correct.

*Error Flag: 0*

### Example 3 (Error: causalOrganism)

> A 9-year-old girl...scratching her buttocks and anus...genital itching...worse at night...

- **Error**: "Suspected of infection with **Giardia lamblia**."
- **Corrected**: "Suspected of infection with **Enterobius vermicularis**."

### Example 4 (No Error)

> Same vignette as Example 3 but without error.

*Error Flag: 0*

### Example 5 (Error: causalOrganism)

> Blood cultures...echocardiography shows a large vegetation on tricuspid valve...

- **Error**: "Causal organism is **Staphylococcus epidermidis**."
- **Corrected**: "Causal organism is **Staphylococcus aureus**."

---

*5 of 100 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 100 records

## Reference

Manes, I., et al. "MEDEC: A Benchmark for Medical Error Detection and Correction in Clinical Notes." *arXiv*, 2024.
