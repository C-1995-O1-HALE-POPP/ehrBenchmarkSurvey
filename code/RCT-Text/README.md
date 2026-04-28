# RCT-Text

- **Source**: HuggingFace `pietrolesci/pubmed-20k-rct`
- **Config**: default
- **Split**: validation
- **Examples collected**: 200

## Field Schema

```json
{
  "abstract_id": "str",
  "labels": "int",
  "text": "str",
  "sentence_id": "int",
  "uid": "int",
  "embedding_all-mpnet-base-v2": "list",
  "embedding_multi-qa-mpnet-base-dot-v1": "list",
  "embedding_all-MiniLM-L12-v2": "list"
}
```

## Sample Examples

### Example 1

```json
{
  "abstract_id": "24290286",
  "labels": 0,
  "text": "IgE sensitization to Aspergillus fumigatus and a positive sputum fungal culture result are common in patients with refractory asthma .",
  "sentence_id": 0,
  "uid": 176642,
  "embedding_all-mpnet-base-v2": [
    -0.01820213533937931,
    -0.06089496985077858,
    0.05369611829519272
  ],
  "embedding_multi-qa-mpnet-base-dot-v1": [
    -0.2861972749233246,
    -0.7012609243392944,
    -0.07130526751279831
  ],
  "embedding_all-MiniLM-L12-v2": [
    0.006212283857166767,
    0.014559509232640266,
    0.037409376353025436
  ]
}
```

### Example 2

```json
{
  "abstract_id": "24290286",
  "labels": 0,
  "text": "It is not clear whether these patients would benefit from antifungal treatment .",
  "sentence_id": 1,
  "uid": 176643,
  "embedding_all-mpnet-base-v2": [
    0.04328802227973938,
    0.03104563243687153,
    0.014925499446690083
  ],
  "embedding_multi-qa-mpnet-base-dot-v1": [
    0.2105707824230194,
    -0.09401403367519379,
    -0.30395376682281494
  ],
  "embedding_all-MiniLM-L12-v2": [
    -0.02685953676700592,
    -0.006969951558858156,
    -0.00854499638080597
  ]
}
```

### Example 3

```json
{
  "abstract_id": "24290286",
  "labels": 3,
  "text": "We sought to determine whether a @-month course of voriconazole improved asthma-related outcomes in patients with asthma who are IgE sensitized to A fumigatus .",
  "sentence_id": 2,
  "uid": 176644,
  "embedding_all-mpnet-base-v2": [
    -0.020313965156674385,
    -0.02382824197411537,
    -0.0009158641332760453
  ],
  "embedding_multi-qa-mpnet-base-dot-v1": [
    -0.29805564880371094,
    -0.2518543004989624,
    -0.152854785323143
  ],
  "embedding_all-MiniLM-L12-v2": [
    0.009919253177940845,
    -0.05082356557250023,
    0.05553131550550461
  ]
}
```

### Example 4

```json
{
  "abstract_id": "24290286",
  "labels": 2,
  "text": "Asthmatic patients who were IgE sensitized to A fumigatus with a history of at least @ severe exacerbations in the previous @ months were treated for @ months with @ mg of voriconazole twice daily , followed by observation for @ months , in a double-blind , placebo-controlled , randomized design .",
  "sentence_id": 3,
  "uid": 176645,
  "embedding_all-mpnet-base-v2": [
    -0.01904868520796299,
    -0.028880994766950607,
    0.008178848773241043
  ],
  "embedding_multi-qa-mpnet-base-dot-v1": [
    -0.1888599693775177,
    -0.37657254934310913,
    -0.08850768208503723
  ],
  "embedding_all-MiniLM-L12-v2": [
    0.002077037701383233,
    -0.04036054015159607,
    0.060761865228414536
  ]
}
```

### Example 5

```json
{
  "abstract_id": "24290286",
  "labels": 2,
  "text": "Primary outcomes were improvement in quality of life at the end of the treatment period and a reduction in the number of severe exacerbations over the @ months of the study .",
  "sentence_id": 4,
  "uid": 176646,
  "embedding_all-mpnet-base-v2": [
    0.021420178934931755,
    -0.040573667734861374,
    -0.009090238250792027
  ],
  "embedding_multi-qa-mpnet-base-dot-v1": [
    0.16900880634784698,
    -0.44234025478363037,
    -0.2287217527627945
  ],
  "embedding_all-MiniLM-L12-v2": [
    0.04457692429423332,
    0.009956331923604012,
    0.018619714304804802
  ]
}
```

## Data Files

- `raw/examples.json` — 200 records

## Reference

Dernoncourt, F. & Lee, J.Y. "PubMed 200k RCT: A Dataset for Sequential Sentence Classification in Medical Abstracts." Proceedings of the Eighth International Joint Conference on Natural Language Processing (IJCNLP), 2017.
