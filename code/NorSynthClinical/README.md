# NorSynthClinical

## Overview
NorSynthClinical is a synthetic corpus of Norwegian clinical text describing patients' family history relating to cases of cardiac disease. It is the first publicly available resource of Norwegian clinical text, with annotations for Named Entity Recognition (NER) of family history information and Protected Health Information (PHI).

## Task
- **NER**: Family history entity recognition
- **De-identification**: PHI detection
- **RE**: Relation extraction between family members and diseases
- **Language**: Norwegian (Bokmål)
- **Domain**: Clinical (cardiac disease, family history)

## Dataset Statistics (Original)
- 477 sentences
- 6,030 tokens

## Dataset Statistics (PHI Extension - NorSynthClinical-PHI)
- 8,270 tokens
- 409 PHI instances

## Annotation Types
- Family history entities (family members, diseases, relationships)
- PHI types (names, dates, identifiers, etc.)

## Data Format
CoNLL-U format with dependency parsing, lemmatization, and morphological features (Universal Dependencies style)

## Source
- GitHub: `ltgoslo/NorSynthClinical`
- PHI Extension: `synnobra/NorSynthClinical-PHI`
- Paper: Rama et al., "Iterative development of family history annotation guidelines using a synthetic corpus of clinical text" (LOUHI 2018)

## Download Status
Downloaded 150 examples from GitHub repository (CoNLL-U parsed format).

## References
- https://github.com/ltgoslo/NorSynthClinical
- https://github.com/synnobra/NorSynthClinical-PHI
- https://aclanthology.org/W18-5613/
