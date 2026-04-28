# MEDIQA 2019 Task 2 — Recognizing Question Entailment (RQE)

- **Source**: HuggingFace `bigbio/mediqa_rqe`
- **Config**: mediqa_rqe_source / Split: train
- **Examples collected**: 200

## Task

Recognizing Question Entailment: determine whether a frequently asked question (FAQ) is a relevant answer to a consumer health question (CHQ). Binary classification task — `value: true` means the FAQ answers the CHQ; `value: false` means it does not.

## Data Format

| Field | Description |
|-------|-------------|
| `pid` | Pair ID |
| `value` | `true` if FAQ entails/relevant to CHQ, `false` otherwise |
| `chq` | Consumer health question |
| `faq` | Frequently asked question candidate |

## Sample Examples

### Example 1 (True — exact match)

> **CHQ**: How should I treat polymenorrhea in a 14-year-old girl?
>
> **FAQ**: How should I treat polymenorrhea in a 14-year-old girl?

**Label**: `true`

### Example 2 (True — paraphrase)

> **CHQ**: Have there been any studies with low molecular weight heparin in pregnancy because I have an obstetric patient who had a deep vein thrombosis with her last pregnancy and I'm wondering if I can use it?
>
> **FAQ**: Can I use low molecular weight heparin in pregnancy (patient with deep vein thrombosis last pregnancy)?

**Label**: `true`

### Example 3 (False — different topics)

> **CHQ**: Have there been any studies with low molecular weight heparin in pregnancy...
>
> **FAQ**: What are the side effects of Florinef? Could it cause headaches?

**Label**: `false`

### Example 4 (True — identical)

> **CHQ**: Let's give these immunizations. That's right isn't it?
>
> **FAQ**: Let's give these immunizations. That's right isn't it?

**Label**: `true`

### Example 5 (False — unrelated)

> **CHQ**: Let's give these immunizations. That's right isn't it?
>
> **FAQ**: Is there more support we can provide patients with macular degeneration?

**Label**: `false`

---

*5 of 200 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 200 records

## Reference

Ben Abacha, A., et al. "Overview of the MEDIQA 2019 Shared Task on Consumer Health Question Summarization and Question Answering." *ACL-BioNLP Workshop*, 2019.
