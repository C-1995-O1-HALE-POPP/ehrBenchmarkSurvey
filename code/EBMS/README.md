# EBMS (Evidence-Based Medicine Summarization)

- **Source**: Not available on HuggingFace
- **Examples collected**: 0

## Overview

EBMS (Evidence-Based Medicine Summarization) is a dataset focused on generating evidence-based justifications from biomedical literature. Given a clinical question and a set of PubMed abstracts, the task is to produce a concise justification citing relevant evidence.

## Task Description

The EBMS task involves:
- Reading PubMed abstracts related to a clinical question
- Identifying sentences that provide evidence for or against a clinical intervention
- Generating a summarized justification with citations

## Related Datasets on HuggingFace

While the specific EBMS corpus is not on HuggingFace, related resources include:
- `bigbio/pico_extraction` — PICO element extraction from RCT abstracts
- `pietrolesci/pubmed-20k-rct` — PubMed 200k RCT sentence classification
- EBM-NLP corpus: http://ebm-nlp.herokuapp.com

## Search Status

Searched HuggingFace for: `ebms`, `evidence_based_medicine`, `ebm`, `evidence based` — no matching standalone EBMS dataset found.

## Data Files

- `raw/examples.json` — 0 records (not yet downloaded)

## Reference

Mollá, D., et al. "Overview of the 2019 ALTA Shared Task: Evidence-Based Medicine." Proceedings of the Australasian Language Technology Association Workshop, 2019.

The EBM-NLP corpus is available at: http://ebm-nlp.herokuapp.com
