# PatientInstruct (Patient Instructions)

**Category**: Post-Procedure Patient Instruction Generation (P2 - Clinical Reasoning)

## Overview
Patient Instructions (PI) is a benchmark for generating accurate and faithful discharge/patient instructions from clinical health records. Published at NeurIPS 2022. The Re3Writer model uses Retrieval, Reasoning, and Refinement to generate patient instructions. Dataset built from MIMIC-III (~35k pairs of health records and output instructions).

- **Paper**: [arXiv:2210.12777](https://arxiv.org/abs/2210.12777) - "Retrieve, Reason, and Refine: Generating Accurate and Faithful Patient Instructions"
- **Repo**: https://github.com/AI-in-Hospitals/Patient-Instructions
- **License**: MIT (code)

## Dataset
Built from MIMIC-III v1.4:
- **Size**: ~35,881 pairs (28,021 unique patients) of input health records + output patient instructions
- **Input**: Patient health records (diagnoses, medications, procedures)
- **Output**: Discharge/patient instruction text
- **Pre-processed data**: Available on [Google Drive](https://drive.google.com/file/d/1z1SvPDZ_yixuWuzQr9aK7bNPJUq2tEhY/view?usp=sharing) (data.zip, 132MB)

## Setup

```bash
# Clone the repo (already done)
# Clone coco-caption for metrics
cd repo && git clone https://github.com/ruotianluo/coco-caption.git

# Conda environment
conda create -n pi python==3.9
conda activate pi
pip install torch==1.7.1+cu101 torchvision==0.8.2+cu101 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
pip install transformers==4.10.0
pip install pytorch-lightning==1.5.1
pip install pandas rouge scipy

# For data preparation: pip install scikit-learn plotly
```

## Data Download

Download pre-processed data from Google Drive and extract to `repo/data/`:
```
Patient-Instructions/
  data/
    splits/         # train.csv, val.csv, test.csv
    vocab/          # tokenizer files
    diagnose-procedure-medication/   # ICD mappings
```

Raw MIMIC-III data must be acquired from [PhysioNet](https://physionet.org/content/mimiciii/1.4/) with credentialed access.

## Training

```bash
cd repo
python pretreatments/prepare_codes_adjacent_matrix.py
python pretreatments/prepare_relevant_info.py
python pretreatments/extract_instruction_embs.py

# Train with Transformer (base architecture)
python train.py --gpus 8 --batch_size 8 --arch base --setup transformer

# Train with LSTM (small architecture)
python train.py --gpus 8 --batch_size 8 --arch small --setup lstm
```

Key args: `--gpus`, `--batch_size`, `--accumulate_grad_batches`, `--arch` (small/base), `--setup` (transformer/transformer_Full/lstm/lstm_Full).

## Evaluation

```bash
# Automatic metrics (BLEU, METEOR, ROUGE)
python translate.py $path_to_model

# Save generated instructions
python translate.py $path_to_model --save_json --save_base_path ./inference_results

# Evaluate on subtasks
python translate.py $path_to_model --subtask_type age|sex|disease
```

Results written to `csv_results/overall.csv`.

## Dependencies
- MIMIC-III v1.4 (PhysioNet credentialed access for raw data)
- Google Drive download for pre-processed data
- 8 GPUs recommended for training (configurable via `--gpus`)
- coco-caption (for evaluation metrics)
