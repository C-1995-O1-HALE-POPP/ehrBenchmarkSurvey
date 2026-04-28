# Species-800 (S800)

## Overview
Species-800 is a corpus of PubMed abstracts annotated for organism/species mentions. It is used for evaluating biomedical Named Entity Recognition (NER) systems for species recognition.

## Task
- **Named Entity Recognition**: Organism/Species detection
- **Language**: English
- **Domain**: Biomedical literature (PubMed abstracts)

## Dataset Statistics
- Training: 4,576 documents / 147,291 tokens
- Development: 749 documents / 22,217 tokens
- Test: 1,356 documents / 42,298 tokens
- Total entity mentions: ~3,708

## Data Format
TSV format: `token	label` per line (BIO tagging scheme)

## Source
- HuggingFace: `spyysalo/species_800`
- Repository contains `data/s800.zip` with train/devel/test TSV files
- Original: JNLPBA 2004 shared task corpus extension

## Download Status
Downloaded 200 examples from `spyysalo/species_800` on HuggingFace.

## References
- https://huggingface.co/datasets/spyysalo/species_800
- Pafilis et al., "The SPECIES and ORGANISMS Resources for Fast and Accurate Identification of Taxonomic Names in Text" (2013)
