# BioLORD — Biomedical Ontology Concept Explanation

- **Source**: HuggingFace `UMCU/biolord_dutch_marianmt` (Dutch translation of `FremyCompany/BioLORD-Dataset`)
- **Original**: `FremyCompany/BioLORD-Dataset` (gated — requires authentication)
- **Config**: default / Split: train
- **Examples collected**: 200

## Task

Explain biomedical ontology concepts. BioLORD was constructed for training text embedding models that produce similar representations for biomedical concept names and their definitions. Each entry pairs a concept name with its definitional description.

**Note**: This dataset is a machine-translated (Dutch) version via MarianMT. The original English dataset (`FremyCompany/BioLORD-Dataset`) is gated on HuggingFace and requires access approval.

## Data Format

| Field | Description |
|-------|-------------|
| `id` | Example ID |
| `text` | Biomedical concept definition (Dutch) |
| `approx_token_counts` | Approximate token count |

## Sample Examples

### Example 1

> **Text**: "regulatie van CD4 positieve, alfa-beta-T celproliferatie (regulering van CD4 positieve, alfa-beta-T cel activatie) regeling van CD4 positieve, alfa-beta-T cel activatie beschreven als elk proces dat de frequentie, snelheid of omvang van CD4 positieve, alfa-beta-T celproliferatie moduleert."

*Translation: regulation of CD4-positive, alpha-beta T cell proliferation — described as any process that modulates the frequency, rate or extent of CD4-positive, alpha-beta T cell proliferation.*

### Example 2

> **Text**: "positieve regulering van de dendrite extension (positieve regulering van de celgroei) iets wat wordt omschreven als elk proces dat de frequentie, snelheid of omvang van de dendrite extension activeert of verhoogt."

*Translation: positive regulation of dendrite extension — described as any process that activates or increases the frequency, rate or extent of dendrite extension.*

### Example 3

> **Text**: "positieve regulering van de koude-induceerde thermogenese (positieve regulering van het metabole proces)..."

*Translation: positive regulation of cold-induced thermogenesis — described as any process that activates or increases cold-induced thermogenesis.*

---

*3 of 200 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 200 records

## Reference

Remy, F., et al. "BioLORD: Learning Ontological Representations from Biomedical Definitions." *arXiv*, 2023.

Kusa, W., et al. "BioLORD-2023: Semantic Textual Representations Fusing Large Language Models and Clinical Knowledge Graph Insights." *arXiv*, 2024.
