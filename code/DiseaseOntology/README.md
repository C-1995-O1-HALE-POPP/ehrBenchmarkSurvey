# DiseaseOntology — Disease Ontology (DO) Reasoning

- **Source**: HuggingFace `Hierarchy-Transformers/DOID`
- **Config**: MixedHop-HardNegatives-Pairs / Split: train
- **Examples collected**: 200

## Task

Predict parent-child relationships in the Human Disease Ontology (DOID). Given a child disease concept and a candidate parent concept, determine whether the parent relationship is valid. This is a binary classification task testing biomedical ontology reasoning.

## Data Format

| Field | Description |
|-------|-------------|
| `child` | Child disease concept name |
| `parent` | Candidate parent disease concept name |
| `label` | 1 = valid parent-child relationship, 0 = negative/hard negative |

## Sample Examples

### Example 1 (Positive)

> **Child**: Froelich syndrome
> **Parent**: hypothalamic disease
> **Label**: `1` ✓

### Example 2 (Negative)

> **Child**: Froelich syndrome
> **Parent**: androgenic alopecia
> **Label**: `0` ✗

### Example 3 (Negative)

> **Child**: Froelich syndrome
> **Parent**: pleomorphic lipoma
> **Label**: `0` ✗

### Example 4 (Negative)

> **Child**: Froelich syndrome
> **Parent**: intracranial structure hemangioma
> **Label**: `0` ✗

### Example 5 (Negative)

> **Child**: Froelich syndrome
> **Parent**: pontocerebellar hypoplasia type 1
> **Label**: `0` ✗

---

*5 of 200 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 200 records

## Reference

Schriml, L.M., et al. "Human Disease Ontology 2022 update." *Nucleic Acids Research*, 2022.

Huang et al. "Hierarchy Transformers for Biomedical Ontology Reasoning." 2024.
