# BC4Chem (BC4CHEMD / CHEMDNER)

## Overview
BC4Chem (also known as CHEMDNER / BC4CHEMD) is a dataset for chemical Named Entity Recognition (NER). It contains PubMed abstracts annotated with chemical entity mentions, from the BioCreative IV CHEMDNER task.

## Task
- **Named Entity Recognition**: Chemical compound mentions
- **Language**: English
- **Domain**: Chemistry / Biomedical literature (PubMed abstracts)

## Dataset Statistics
- Training: 3,500 abstracts / ~890,000 tokens
- Development: 3,500 abstracts / ~886,000 tokens
- Test: 3,000 abstracts / ~766,000 tokens
- Total chemical mentions: 84,355

## Entity Classes (SACEM)
| Code | Description |
|------|-------------|
| ABBREVIATION | Abbreviated form |
| FAMILY | Chemical family/class |
| FORMULA | Molecular formula |
| IDENTIFIER | Chemical identifier (e.g., CAS) |
| MULTIPLE | Multiple chemicals listed |
| SYSTEMATIC | IUPAC/systematic name |
| TRIVIAL | Common/trivial name |

## Data Format
TSV format: `token	label` (BIO tagging with SACEM subtypes)

## Source
- HuggingFace: `chintagunta85/bc4chemd`
- Original data: https://github.com/cambridgeltl/MTL-Bioinformatics-2016/
- Paper: Krallinger et al., "The CHEMDNER corpus of chemicals and drugs and its annotation principles" (2015)

## Download Status
Downloaded 200 examples from GitHub (MTL-Bioinformatics-2016 repository).

## References
- http://www.biocreative.org/resources/biocreative-iv/chemdner-corpus/
- https://github.com/cambridgeltl/MTL-Bioinformatics-2016/
