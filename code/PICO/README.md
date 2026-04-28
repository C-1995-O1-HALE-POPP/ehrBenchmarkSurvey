# PICO

- **Source**: HuggingFace `bigbio/pico_extraction`
- **Config**: pico_extraction_source
- **Split**: train
- **Examples collected**: 200

## Field Schema

```json
{
  "doc_id": "str",
  "text": "str",
  "entities": "list"
}
```

## Sample Examples

### Example 1

```json
{
  "doc_id": "11317090:7",
  "text": "Outcome results applied to life expectancy tables were used to estimate QALYs .",
  "entities": [
    {
      "text": "life expectancy tables",
      "type": "outcome",
      "start": 27,
      "end": 49
    },
    {
      "text": "QALYs",
      "type": "outcome",
      "start": 72,
      "end": 77
    }
  ]
}
```

### Example 2

```json
{
  "doc_id": "12960652:2",
  "text": "These types of gastric myoelectrical activity and dysrhythmia can be measured by electrogastrography using cutaneous electrodes .",
  "entities": [
    {
      "text": "gastric myoelectrical activity and dysrhythmia",
      "type": "outcome",
      "start": 15,
      "end": 61
    },
    {
      "text": "electrogastrography",
      "type": "outcome",
      "start": 81,
      "end": 100
    }
  ]
}
```

### Example 3

```json
{
  "doc_id": "20560622:8",
  "text": "Serum and urine biochemical parameters related to calcium status and bone metabolism remained unaltered .",
  "entities": [
    {
      "text": "Serum and urine biochemical parameters related to calcium status and bone metabolism",
      "type": "outcome",
      "start": 0,
      "end": 84
    }
  ]
}
```

### Example 4

```json
{
  "doc_id": "19802506:6",
  "text": "After 24 months , women who took medications without exercising had significant improvements in BMD at the total hip ( +1.81 % ) and spine ( +2.85 % ) and significant decreases in Alkphase B ( -8.7 % ) and serum NTx ( -16.7 % ) .",
  "entities": [
    {
      "text": "medications",
      "type": "intervention",
      "start": 33,
      "end": 44
    },
    {
      "text": "exercising",
      "type": "intervention",
      "start": 53,
      "end": 63
    },
    {
      "text": "BMD",
      "type": "outcome",
      "start": 96,
      "end": 99
    }
  ]
}
```

### Example 5

```json
{
  "doc_id": "23417625:10",
  "text": "The SST-GP had higher efficacy than the LA-GP .",
  "entities": [
    {
      "text": "SST-GP",
      "type": "intervention",
      "start": 4,
      "end": 10
    },
    {
      "text": "LA-GP",
      "type": "intervention",
      "start": 40,
      "end": 45
    },
    {
      "text": "efficacy",
      "type": "outcome",
      "start": 22,
      "end": 30
    }
  ]
}
```

## Data Files

- `raw/examples.json` — 200 records

## Reference

Nye, B., et al. "A Corpus with Multi-Level Annotations of Patients, Interventions and Outcomes to Support Language Processing for Medical Literature." Proceedings of ACL, 2018.
