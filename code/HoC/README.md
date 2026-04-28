# Hallmarks of Cancer (HoC) Dataset

**Sentence-level multi-label classification of PubMed abstracts for cancer hallmarks.**

## Overview

The Hallmarks of Cancer (HoC) Corpus consists of 1,852 PubMed abstracts (12,119 sentences in the training set) manually annotated by domain experts. Each sentence is classified with zero or more labels from a taxonomy of 11 cancer hallmark classes, as defined by [Hanahan & Weinberg](https://doi.org/10.1016/j.cell.2011.02.013).

- **Paper**: [Baker et al. (2016) *Bioinformatics*](https://doi.org/10.1093/bioinformatics/btv585)
- **Dataset**: [`bigbio/hallmarks_of_cancer` on HuggingFace](https://huggingface.co/datasets/bigbio/hallmarks_of_cancer)
- **License**: GPL 3.0
- **Task**: Multi-label sentence classification
- **Splits**: Train (1,219 abstracts / 12,119 sentences), Validation, Test

## Label Taxonomy (11 classes)

| # | Hallmark Label | Train Sentences |
|---|---------------|----------------:|
| 0 | evading growth suppressors | 268 |
| 1 | tumor promoting inflammation | 375 |
| 2 | enabling replicative immortality | 219 |
| 3 | cellular energetics | 136 |
| 4 | resisting cell death | 602 |
| 5 | activating invasion and metastasis | 448 |
| 6 | genomic instability and mutation | 523 |
| 7 | **none** (no hallmark) | 9,027 |
| 8 | inducing angiogenesis | 238 |
| 9 | sustaining proliferative signaling | 674 |
| 10 | avoiding immune destruction | 185 |

**Note**: "none" is the majority class (~74% of sentences convey no cancer hallmark). The dataset is multi-label — a single sentence can express multiple hallmarks.

## Examples

Each row in `raw/examples.json` has:
- `document_id`: sentence-unique ID (`<pmid>_<sentence_index>`)
- `pmid`: source PubMed ID
- `text`: the sentence string
- `labels`: resolved human-readable hallmark labels
- `bigbio_labels`: labels from the BigBio standardised format

### "none" (no hallmark expressed)

| PMID | Sentence |
|------|----------|
| 22239943 | Hypoxic events frequently occur in the aquatic environment in association with micro pollutants, including heavy metals. |
| 22239943 | Only a few studies are however available on the uptake and biological responses of heavy metals under hypoxic conditions. |
| 14627703 | It is also proposed that the differences observed in these two types of cancers can be attributed to specific patterns of histological differentiation. |

### Single-label examples

**evading growth suppressors**
| PMID | Sentence |
|------|----------|
| 12659514 | It is demonstrated that the mei-41 gene is a homologue of the human atm gene which is responsible for a cell cycle checkpoint. |
| 21195136 | The established cell lines stably express either SV40 LTAg alone, or SV40 LTAg and hTERT, and demonstrate high proliferative rate, contact inhibition at confluence, and stable expression of protein markers of differentiation. |

**tumor promoting inflammation**
| PMID | Sentence |
|------|----------|
| 22753494 | This mechanism of action of miRNAs is implicated in tumor-immune system communication and is important in tumor growth and spread, thus representing a possible target for cancer treatment. |
| 24025408 | Thus, we assert that the existence of miR-504 mediated degradative-regulatory pathway is novel in the regulation of PTEN expression in CRC and might serve as a new viable target for CRC therapy. |

**enabling replicative immortality**
| PMID | Sentence |
|------|----------|
| 20237138 | Despite continuous telomere erosion of individual tumour cells, colon tumours maintained stable expression levels of TERC (the RNA component) and of telomerase activity during disease progression. |
| 20442238 | Telomerase therapy is a promising approach to blunt telomere attrition and thereby prevent senescence in cells derived from patients with dyskeratosis congenita and related telomerase syndromes. |

**cellular energetics**
| PMID | Sentence |
|------|----------|
| 22819516 | A number of clinical trials for glutamine metabolic pathway inhibitors and glutamine analogues have also been undertaken. |
| 23165003 | By comparing a control with a CQ treatment, elevation of fumarate, malate, citrate, and succinate was observed together with the suppression of isocitrate. |

**resisting cell death**
| PMID | Sentence |
|------|----------|
| 23001828 | A search for apoptosis inhibitors identified NS1 protein and dsRNA-binding domain was found sufficient for this activity. |
| 18952644 | A number of targets such as tumor necrosis factor-related apoptosis-inducing ligand (TRAIL) receptors, Bcl-2 family proteins, caspases, and XIAP are the major sites of drug action. |

**activating invasion and metastasis**
| PMID | Sentence |
|------|----------|
| 24885485 | A small set of miRNAs that promotes migration and invasion was found to be overexpressed in collective cell migration. |
| 22835863 | Blocking of MMP-14 catalytic activity revealed a key function of the enzyme in the regulation of ECM degradation, invasion, and angiogenesis by endothelial cells. |

**genomic instability and mutation**
| PMID | Sentence |
|------|----------|
| 22683702 | The interaction of environmental factors with inherent genetic instability of the tumor cell results in clonal heterogeneity and selection of aggressive tumor cells with acquisition of resistance. |
| 24383795 | Patients with Lynch syndrome inherit a germline mutation in one of the mismatch repair (MMR) genes associated with a high risk of several cancers. |

**inducing angiogenesis**
| PMID | Sentence |
|------|----------|
| 21118913 | VEGF-A is perhaps the most well-characterized angiogenic growth factor and is crucially involved in tumor-associated angiogenesis. |
| 23345228 | We constructed a MLT of high intensity with endothelial-like differentiation by taking advantage of the hypoxia microenvironment, using NPC cell lines. |

**sustaining proliferative signaling**
| PMID | Sentence |
|------|----------|
| 22525479 | Thus, miR-29a is a highly valuable biomarker for CRC, with great potential as a diagnostic tool and therapeutic target for CRC therapy. |
| 18838276 | Activation of growth factor receptors activates multiple intracellular signaling pathways. |

**avoiding immune destruction**
| PMID | Sentence |
|------|----------|
| 24743214 | Loss of TIPE2 expression is considered a mechanism for immune evasion in human HCC, and therapies designed to restore TIPE2 expression may therefore be useful in HCC treatment. |
| 27010849 | The immune system plays an important role in the development, monitoring and treatment of cancer. |

### Multi-label examples

| PMID | Labels | Sentence |
|------|--------|----------|
| 22967914 | activating invasion and metastasis, tumor promoting inflammation | Besides their direct effects on tumor cells, NSAIDs can inhibit cell migration and invasion, induce apoptosis, but also act as potent anti-inflammatory agents in the tumor microenvironment. |
| 23907170 | genomic instability and mutation, resisting cell death | Persistent DNA damage of the genome induces premature senescence, which is accompanied by secretion of inflammatory cytokines and matrix metalloproteinases. |
| 23208801 | evading growth suppressors, tumor promoting inflammation, activating invasion and metastasis | As EC is considered a hormone-related cancer, the present study aimed to investigate the effect of steroid hormones on the expression of NDRG1 in EC cell lines. |

## Data Format

Two configurations are available on HuggingFace:

### `hallmarks_of_cancer_source` (original format)

```python
{
  "document_id": "22239943_0",  # PMID_sentenceIndex
  "text": "Hypoxic events ...", # sentence text
  "label": [7]                  # list of int class indices (0-10)
}
```

### `hallmarks_of_cancer_bigbio_text` (BigBio standardised)

```python
{
  "id": "1",
  "document_id": "22239943_0",
  "text": "Hypoxic events ...",
  "labels": ["none"]            # list of string class names
}
```

## Loading the Dataset

```bash
# Using HuggingFace datasets
python -c "
from datasets import load_dataset
ds = load_dataset('bigbio/hallmarks_of_cancer', name='hallmarks_of_cancer_source', split='train')
print(ds[0])
"
```

Or via parquet directly:

```bash
curl -L -o train.parquet \
  "https://huggingface.co/datasets/bigbio/hallmarks_of_cancer/resolve/refs%2Fconvert%2Fparquet/hallmarks_of_cancer_source/train/0000.parquet"
```

## Citation

```bibtex
@article{DBLP:journals/bioinformatics/BakerSGAHSK16,
  author    = {Simon Baker and
               Ilona Silins and
               Yufan Guo and
               Imran Ali and
               Johan H{\"o}gberg and
               Ulla Stenius and
               Anna Korhonen},
  title     = {Automatic semantic classification of scientific literature
               according to the hallmarks of cancer},
  journal   = {Bioinform.},
  volume    = {32},
  number    = {3},
  pages     = {432--440},
  year      = {2016},
  doi       = {10.1093/bioinformatics/btv585},
}
```

## Files

| File | Description |
|------|-------------|
| `README.md` | This file |
| `raw/examples.json` | 28 annotated examples with label distribution |
| `raw/train_source.parquet` | Train split (source format, 12,119 sentences) |
| `raw/train_bigbio.parquet` | Train split (BigBio format) |
