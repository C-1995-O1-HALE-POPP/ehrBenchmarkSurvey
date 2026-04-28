# MedicationQA — Consumer Medication Question Answering

- **Source**: HuggingFace `truehealth/medicationqa`
- **Config**: default / Split: train
- **Examples collected**: 200

## Task

Answer consumer drug questions using authoritative sources (MedlinePlus, DailyMed, Wikipedia). Questions cover drug interactions, side effects, dosing, indications, and ingredients.

## Data Format

| Field | Description |
|-------|-------------|
| `Question` | Consumer question about a medication |
| `Focus (Drug)` | The drug the question is about |
| `Question Type` | Action / Interaction / Dose / Information / Ingredient / Side Effect |
| `Answer` | Reference answer from authoritative source |
| `Section Title` | Source document section |
| `URL` | Source URL |

## Sample Examples

### Example 1 (Interaction)

> **Q**: how does rivatigmine and otc sleep medicine interact

**Drug**: rivastigmine | **Answer**: ...tell your doctor and pharmacist what prescription and nonprescription medications...you are taking or plan to take. Be sure to mention...antihistamines; aspirin and other NSAIDs...medications for Alzheimer's disease, glaucoma...

*Source: MedlinePlus*

### Example 2 (Action)

> **Q**: how does valium affect the brain

**Drug**: Valium | **Answer**: Diazepam is a benzodiazepine that exerts anxiolytic, sedative, muscle-relaxant, anticonvulsant and amnestic effects. Most of these effects are thought to result from a facilitation of the action of gamma aminobutyric acid (GABA), an inhibitory neurotransmitter in the central nervous system.

*Source: DailyMed*

### Example 3 (Information)

> **Q**: what is morphine

**Drug**: morphine | **Answer**: Morphine is a pain medication of the opiate family which is found naturally in a number of plants and animals. It acts directly on the central nervous system (CNS) to decrease the feeling of pain.

*Source: Wikipedia*

### Example 4 (Dose)

> **Q**: what are the milligrams for oxycodone e

**Drug**: oxycodone ER | **Answer**: ...10 mg ... 20 mg ... 40 mg ... 80 mg ...

*Source: DailyMed*

### Example 5 (Ingredient)

> **Q**: 81% aspirin contain resin and shellac in it?

**Drug**: aspirin 81 mg | **Answer**: Inactive Ingredients: [list of inactive ingredients]

*Source: DailyMed*

---

*5 of 200 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 200 records

## Reference

TrueHealth. "MedicationQA: Consumer Medication Question Answering Dataset." HuggingFace, 2023.
