# BC5CDR

## Overview
BC5CDR (BioCreative V Chemical-Disease Relation) is a benchmark for joint Named Entity Recognition (NER) of chemicals and diseases, and Relation Extraction (RE) of chemical-induced disease relationships from PubMed abstracts.

## Task
- **NER**: Chemical and Disease entity recognition
- **RE**: Chemical-Disease Relation extraction
- **Language**: English
- **Domain**: Biomedical literature (PubMed abstracts)

## Dataset Statistics
- Training: 500 PubMed abstracts
- Development: 500 PubMed abstracts
- Test: 500 PubMed abstracts
- Entity types: Chemical, Disease
- Relation type: Chemical-Disease Relation (CID)

## Data Format
PubTator format with PMID, entity spans, and entity types (Chemical/Disease). File extensions: `.PubTator.txt`, `.BioC.xml`

## Source
- HuggingFace: `bigbio/bc5cdr`
- Repository contains `CDR_Data.zip` with training, development, and test sets
- Original: BioCreative V CDR task

## Download Status
Downloaded 200 examples from `bigbio/bc5cdr` on HuggingFace (PubTator format).

## References
- https://huggingface.co/datasets/bigbio/bc5cdr
- Li et al., "BioCreative V CDR task corpus: a resource for chemical disease relation extraction" (2016)
- http://www.biocreative.org/tasks/biocreative-v/track-3-cdr/
