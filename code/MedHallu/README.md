# MedHallu — Medical Hallucination Detection

- **Source**: HuggingFace `UTAustin-AIHealth/MedHallu`
- **Config**: pqa_labeled / Split: train
- **Examples collected**: 200

## Task

Detect hallucinated (factually incorrect) statements in LLM-generated answers to medical questions. Each example pairs a medical question with supporting knowledge, a ground truth answer, and a hallucinated answer. The task is to identify that the hallucinated answer is incorrect.

## Data Format

| Field | Description |
|-------|-------------|
| `Question` | Medical/clinical question |
| `Knowledge` | List of reference passages for grounding |
| `Ground Truth` | Factually correct answer |
| `Difficulty Level` | easy / medium / hard |
| `Hallucinated Answer` | LLM-generated answer containing hallucination |
| `Category of Hallucination` | Type of error (e.g., Mechanism/Pathway Misattribution, Incomplete Information) |

## Sample Examples

### Example 1 (medium)

> **Q**: Do mitochondria play a role in remodelling lace plant leaves during programmed cell death?

**Ground Truth**: Results depicted mitochondrial dynamics in vivo as PCD progresses within the lace plant...

**Hallucinated Answer**: Mitochondria regulate the formation of perforations in lace plant leaves through the modulation of calcium channels and by activating specific proteases...

*Category: Mechanism and Pathway Misattribution*

### Example 2 (hard)

> **Q**: Landolt C and Snellen E acuity: differences in strabismus amblyopia?

**Ground Truth**: There was only a slight overestimation of visual acuity by the Snellen E compared to the Landolt C, even in strabismus amblyopia.

**Hallucinated Answer**: Patients with strabismus amblyopia showed a significant underestimation of visual acuity when assessed with the Landolt C chart compared to the Snellen E chart.

*Category: Incomplete Information*

### Example 3 (easy)

> **Q**: Are the long-term results of the transanal pull-through equal to those of the transabdominal pull-through?

**Ground Truth**: Significantly better (2-fold) results regarding the continence score for the abdominal approach compared with transanal.

**Hallucinated Answer**: Both transanal and transabdominal pull-through procedures yield comparable long-term outcomes.

*Category: Misinterpretation of #Question#*

---

*3 of 200 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 200 records

## Reference

UT Austin AI Health. "MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations." 2024.
