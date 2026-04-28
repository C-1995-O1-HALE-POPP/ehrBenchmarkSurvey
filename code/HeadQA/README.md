# HeadQA — HEAlthcare Dataset for Question Answering

- **Source**: HuggingFace `EleutherAI/headqa`
- **Config**: en / Split: train
- **Examples collected**: 200

## Task

Multiple-choice question answering from biomedical specialization exams. Questions come from Spanish healthcare training exams (MIR, EIR, etc.) and have been machine-translated to English. Each question has 3–5 answer choices with one correct answer (`ra` field).

## Data Format

| Field | Description |
|-------|-------------|
| `name` | Exam booklet identifier |
| `year` | Exam year |
| `category` | Subject category (biology, pharmacology, medicine, etc.) |
| `qid` | Question ID within booklet |
| `qtext` | Question text |
| `ra` | Correct answer ID (index into answers) |
| `answers[].aid` | Answer choice ID |
| `answers[].atext` | Answer choice text |

## Sample Examples

### Example 1 (Biology, 2013)

> **Q**: The excitatory postsynaptic potentials:

- **A1.** They are all or nothing.
- **A2.** They are hyperpolarizing.
- **A3.** They can be added. **✓**

### Example 2 (Biology, 2013)

> **Q**: Motor plate is the union between the motor neuron and the:

- **A1.** Smooth muscle.
- **A2.** Skeletal muscle **✓**
- **A3.** Cardiac muscle

### Example 3 (Biology, 2013)

> **Q**: DO NOT generate action potentials:

- **A1.** Smooth muscle fibers.
- **A2.** Bipolar neurons of the retina. **✓**
- **A3.** Skeletal striated muscle fibers.

### Example 4 (Biology, 2013)

> **Q**: In the initiation of voluntary movements the first area that is activated is:

- **A1.** Premotor cortex. **✓**
- **A2.** Primary motor cortex.
- **A3.** Brain stem

### Example 5 (Biology, 2013)

> **Q**: The corpuscles of Pacini:

- **A1.** They are innervated by unmyelinated fibers.
- **A2.** They are mechanoreceptors of slow adaptation.
- **A3.** They have small receptor fields.
- **A4.** [correct answer — ra=4]

---

*5 of 200 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 200 records

## Reference

Vilares, D. & Gomez-Rodriguez, C. "HEAD-QA: A Healthcare Dataset for Complex Reasoning." *ACL*, 2019.
