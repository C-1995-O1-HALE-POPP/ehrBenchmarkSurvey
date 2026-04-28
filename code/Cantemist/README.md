# Cantemist

## Overview
Cantemist (CANcer TExt MIning Shared Task) is a Spanish oncology Named Entity Recognition (NER) and concept coding benchmark. It focuses on extracting tumor morphology entities from Spanish clinical case reports and mapping them to the eCIE-O-3.1 classification.

## Task
- **NER**: Named Entity Recognition of tumor morphology mentions
- **Coding**: Concept normalization to eCIE-O-3.1 codes
- **Language**: Spanish
- **Domain**: Oncology (clinical case reports)

## Dataset Statistics
- Training: 501 documents / 19,397 sentences
- Development: 500 documents / 18,165 sentences
- Test: 300 documents / 11,168 sentences
- Entity types: Tumor morphology (MORFOLOGIA_NEOPLASIA)

## Data Format
CoNLL-2002 format (token	label per line, blank line between sentences). BIO tagging scheme.

## Source
- HuggingFace: `PlanTL-GOB-ES/cantemist-ner`
- Alternative: `bigbio/cantemist`
- Paper: Miró-Nicolau et al., "CANTEMIST: CANcer TExt MIning Shared Task"

## Download Status
Downloaded 200 examples from `PlanTL-GOB-ES/cantemist-ner` (CONLL format files).

## References
- https://temu.bsc.es/cantemist/
- https://huggingface.co/datasets/PlanTL-GOB-ES/cantemist-ner
