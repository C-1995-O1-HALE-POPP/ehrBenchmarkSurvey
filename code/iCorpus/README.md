# iCorpus (Japanese Clinical NER / Case Report Corpus)

## Overview
iCorpus is a Japanese clinical case report corpus developed by the University of Tokyo, Department of AI and Digital Twin Development in Healthcare. It contains case reports from J-Stage publications with manual annotations for Named Entity Recognition (NER) and Relation Extraction (RE) of medical entities.

## Task
- **NER**: Named Entity Recognition (56 entity types)
- **RE**: Relation Extraction (35 relationship types)
- **Language**: Japanese
- **Domain**: Clinical case reports (rare and intractable diseases)

## Dataset Statistics
- 183 documents (179 case reports covering 102 rare diseases)
- Average: 1,692 characters/document
- 113 NER labels (B- + I- + O for 56 entity types)
- 36 relation labels (35 types + None)

## NER Baseline Performance
- Clinical-BERT (UTH-BERT): Micro-F1 0.912, Macro-F1 0.601
- NICT-BERT: Micro-F1 0.892

## Source
- Official website: https://ai-health.m.u-tokyo.ac.jp/home/research/corpus
- GitHub (code): https://github.com/aih-uth/joint-entity-and-relation-extraction-from-Japanese-case-report-corpus
- NOT available on HuggingFace (requires separate access from UTokyo)

## Download Status
The dataset on HuggingFace (`Bohanlu/iCorpus-100`) is Taiwanese Hokkien medical translations, NOT the actual Japanese iCorpus. The real iCorpus requires contacting the University of Tokyo for access. Downloaded 100 examples from the available HF dataset as placeholder.

## References
- https://ai-health.m.u-tokyo.ac.jp/home/research/corpus
- Shibata et al., "Towards Structuring Clinical Texts: Joint Entity and Relation Extraction from Japanese Case Report Corpus"
- MedTxt-CR: https://sociocom.naist.jp/medtxt-en/cr/
