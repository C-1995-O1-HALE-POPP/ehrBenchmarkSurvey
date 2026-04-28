<!-- paper_key: "2024_are_clinical_t5_models_better_for_clinical_text" -->
<!-- paper_url: "https://arxiv.org/abs/2412.05845" -->
<!-- generated_on: "2026-04-27" -->

# Benchmark Summary for *Are Clinical T5 Models Better for Clinical Text?*

Source paper: [https://arxiv.org/abs/2412.05845](https://arxiv.org/abs/2412.05845)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-27`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2024_are_clinical_t5_models_better_for_clinical_text/source.pdf`](../papers/2024_are_clinical_t5_models_better_for_clinical_text/source.pdf)
- Extracted text: [`../papers/2024_are_clinical_t5_models_better_for_clinical_text/source.txt`](../papers/2024_are_clinical_t5_models_better_for_clinical_text/source.txt)
- **Search path for this paper:** Paper body (Sections 1–8), Appendix A (Dataset Details), Appendix B (Prefix and Instructions), Appendix D (Training Details), Appendix E (Evaluation Details), Appendix F (Reproducibility Experiments), Appendix G (Cross-Validation Experiments), cached source text.
- **Linked artifacts named by the paper:** GitHub code repository: `https://github.com/yli-z/ml4h_are_clinical_t5_models_better_for_clinical_text`. The HOC dataset is noted as accessible on Huggingface. BC5CDR-disease and NCBI-disease are noted as preprocessed by SciFive and available in the SciFive repository. All MIMIC-derived datasets are credentialed on PhysioNet.
- **Normalization choices:** This paper does not introduce new benchmarks; it reuses 7 existing benchmark datasets from prior work. For benchmarks already registered in the local registry (MedNLI, CLIP), the canonical registry names are preserved. For benchmarks not yet in the registry (RadQA, HOC, BC5CDR-disease, NCBI-disease, Clinical Stigmatizing Language), canonical names align with the published source paper names. The paper uses two instruction formats per task — a T5-prefix format (from prior work) and a FLAN-T5 instruction format (written by the authors) — both are documented.
- **Paper/artifact naming discrepancies:** The paper uses "BC5CDR-disease" to refer to the disease NER subset of BC5CDR, and "NCBI-disease" for NCBI Disease Corpus. The two clinical T5 models are named "Clinical-T5" in both source papers (Lehman et al. 2023 and Lu et al. 2022); this paper disambiguates them as "MIMIC-T5" and "SciFive+MIMIC-T5" respectively.
- **Gated-access limitations:** All MIMIC-III and MIMIC-IV datasets require PhysioNet Credentialed Health Data Use Agreement. The Hospital System (anonymized) dataset requires IRB approval. No public instance-level examples are available for any MIMIC-derived dataset without credentialed access. HOC is the only dataset described as publicly accessible (via Huggingface). BC5CDR-disease and NCBI-disease data are available through the SciFive repository.
- **Example search summary:** Searched the paper body, all appendix sections, and cached source text. The paper provides instruction/prompt templates for every task in Appendix B (both T5-prefix and FLAN-T5 instruction formats). The paper does not provide any concrete dataset-instance examples with verbatim clinical text — no patient records, radiology reports, discharge summaries, or hospital notes are quoted. This is expected given MIMIC data access restrictions. The paper does not directly quote examples from the public HOC, BC5CDR, or NCBI datasets either; it references external artifacts (Huggingface for HOC, SciFive repo for BC5CDR/NCBI) where such examples may be found but does not reproduce them. No linked artifact inspection was performed for this summary beyond the paper text.
- Before syncing the registry, run:
  `python3 scripts/ehr_benchmark_pipeline.py audit-examples "/home/cometp/ehrBenchmarkSurvey/summaries/2024_are_clinical_t5_models_better_for_clinical_text_benchmark_summary.md"`
- After the summary passes verification, run:
  `python3 scripts/ehr_benchmark_pipeline.py sync-registry "/home/cometp/ehrBenchmarkSurvey/summaries/2024_are_clinical_t5_models_better_for_clinical_text_benchmark_summary.md"`

## Verifier Notes

- Benchmark existence: All 7 benchmark names appear directly in the paper text or Appendix A. Five of seven also appear by name in Table 8. The Clinical Stigmatizing Language benchmark is not named as a single benchmark in the paper; the three sub-tasks (Credibility & Obstinacy, Compliance, Descriptors) are named explicitly in Appendix A and evaluated under the umbrella of "stigmatizing language datasets."
- Task mapping: Every task name and instruction template is directly stated in Appendix A and Appendix B of the paper.
- Instruction fidelity: All FLAN-T5 instruction texts are copied verbatim from Appendix B (lines ~1287–1269 of source.txt). T5-prefix texts are also copied verbatim from Appendix B (lines ~1209–1269). The paper states the authors did not exhaustively experiment with different FLAN-T5 instructions and used straightforward formulations.
- Example fidelity: The paper provides no concrete dataset-instance examples in its body, appendix, or supplementary material. No patient records, radiology report excerpts, discharge summary text, clinical note paragraphs, or hospital documents are quoted. This is expected for MIMIC-based datasets due to PHI restrictions. The HOC, BC5CDR, and NCBI datasets are public but the paper does not reproduce example rows. Example provenance is marked accordingly per task.
- Scoring fidelity: All metrics are stated in Table 8 and Appendix E, matching the original source paper evaluation methodologies. No rubric-based or LLM-judge evaluation is used.
- Judge prompt fidelity: Not applicable. All tasks use deterministic automated metrics (accuracy, exact match, F1 scores, precision, recall) computed via sklearn or seqeval. No LLM-judge evaluation is employed.
- Inference labeling: Language is marked "inferred — not explicitly stated" where applicable. Clinical stage, document type, and specialty are inferred from dataset construction when not explicit. Split/sample counts are not stated in this paper; the paper cites original source papers for dataset statistics.

## 1. MedNLI

MedNLI (Romanov and Shivade, 2018) is an English natural language inference benchmark derived from MIMIC-III (Johnson et al., 2016). It consists of premise-hypothesis sentence pairs annotated with one of three relations: entailment, contradiction, or neutral. In this paper, MedNLI serves as one of the three MIMIC-III clinical tasks used to evaluate in-domain performance of clinical vs. general T5 models (Section 4). The paper also uses MedNLI in a low-resource experiment with 1% training data (~99 examples on average per cross-validation fold; Section 6).

- **Language:** English (inferred from the U.S. source EHR; not explicitly stated in this paper)
- **Clinical Stage:** Inpatient hospital course (inferred — MIMIC-III includes ICU and general inpatient notes)
- **Source Clinical Document Type:** Clinical notes from MIMIC-III transformed into sentence pairs
- **Clinical Specialty:** Multi-specialty (inferred from MIMIC-III breadth)
- **Application Method:** Reused public benchmark; originally introduced by Romanov and Shivade (2018). Requires PhysioNet credentialed access.
- **Role in this paper:** In-distribution clinical benchmark for MIMIC-pre-trained models; also used in low-resource downsampling experiments.

---

### 1.1 Task: Natural Language Inference

This task is to determine the logical relationship between a premise sentence and a hypothesis sentence drawn from MIMIC-III clinical notes, classifying each pair as entailment, contradiction, or neutral.

#### Task type
Natural Language Inference / Text Classification

```md
### Instruction (FLAN-T5 format, Appendix B)
Answer entailment, contradiction or neutral. Premise: {premise} Hypothesis: {hypothesis}
### Instruction (T5-prefix format, from MIMIC-T5 paper, Appendix B)
[The paper states they used the same prefix as MIMIC-T5 for MedNLI; the exact prefix text is not reproduced in this paper.]
### Input
A premise sentence and a hypothesis sentence, both derived from MIMIC-III clinical notes, formatted as text.
### Output
One of three class labels: entailment / contradiction / neutral
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material. The paper provides only the instruction/prompt template above.
### Search Depth
Paper body + appendix + cached source text. Linked source artifacts (MIMIC-III credentialed data, original MedNLI paper) not inspected for this summary.
### Example Type
No example available from the current paper. The instruction template is provided but no verbatim patient-level input text or gold label is quoted.
### Source Dataset / Artifact
MIMIC-III (Johnson et al., 2016) clinical notes, specifically the MedNLI subset curated by Romanov and Shivade (2018). Original train/dev/test split from the source paper used; this paper merged train+dev for 5-fold cross-validation.
### Task Construction
Premise-hypothesis pairs were constructed from MIMIC-III clinical text by Romanov and Shivade (2018). This paper uses the pre-constructed dataset without modification.
### Fidelity
The instruction template is copied verbatim from Appendix B. No concrete input/output instance is available from this paper.
### Example
No explicit task example is provided in this paper. The instruction/prompt template from Appendix B is the only task-level evidence. No patient text is quoted.
### Example Input
Not available from this paper. The source dataset requires PhysioNet credentialed access; no public instance-level input can be reproduced without that access.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper. The MedNLI labels (entailment, contradiction, neutral) are described but no specific gold-labeled pair is quoted.
```

#### Scoring standard

```md
### Scoring
Accuracy (primary metric). The paper also reports F1 score in Appendix G (Table 11). Evaluation is performed by direct comparison of model-predicted labels against ground-truth labels without additional post-processing.
### Evaluation Dimensions
Deterministic label-match comparison between prediction and gold label.
### Judge Prompt
Not applicable. The evaluation uses deterministic accuracy/F1 computation; no LLM judge is employed.
```

## 2. RadQA

RadQA (Soni et al., 2022) is an English extractive question-answering benchmark derived from radiology reports in MIMIC-III (Johnson et al., 2016). Given a clinical context (radiology report text) and a question, the task is to extract the answer span from the context. If the question is unanswerable from the given context, the answer is empty. In this paper, RadQA serves as one of the three MIMIC-III clinical tasks used to evaluate in-domain performance (Section 4). The SQuAD 2.0-style evaluation methodology (Rajpurkar et al., 2018) is used, matching the original MIMIC-T5 paper (Lehman et al., 2023).

- **Language:** English (inferred from U.S. source EHR radiology reports; not explicitly stated in this paper)
- **Clinical Stage:** Inpatient/outpatient radiology encounters (inferred from radiology report source)
- **Source Clinical Document Type:** Radiology reports from MIMIC-III
- **Clinical Specialty:** Radiology
- **Application Method:** Reused public benchmark; originally introduced by Soni et al. (2022). Requires PhysioNet credentialed access.
- **Role in this paper:** In-distribution clinical benchmark for MIMIC-pre-trained models.

---

### 2.1 Task: Extractive Question Answering

This task is to read a radiology report context and answer a natural language question by extracting the exact answer span from the text. If the answer is not present in the context, the model must output an empty string (unanswerable detection).

#### Task type
Extractive Question Answering

```md
### Instruction (FLAN-T5 format, Appendix B)
[The paper does not provide a separate FLAN-T5 instruction for RadQA beyond the T5-prefix format below. The prefix is used in the same way as MIMIC-T5.]
### Instruction (T5-prefix format, Appendix B)
Context: {context} Question: {question} If no answer is found in the context, do not reply; otherwise, give an answer from the context:
### Input
A radiology report text (context) paired with a natural language question about the report content.
### Output
An answer span extracted from the context text. Empty string if the question is unanswerable from the context (SQuAD 2.0-style).
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material. The paper provides only the instruction/prompt template above.
### Search Depth
Paper body + appendix + cached source text. Linked source artifacts (MIMIC-III credentialed data, original RadQA paper) not inspected for this summary.
### Example Type
No example available from the current paper. The instruction template is provided but no verbatim radiology report text, question, or answer span is quoted.
### Source Dataset / Artifact
MIMIC-III radiology reports (Johnson et al., 2016), annotated with questions and answer spans by Soni et al. (2022). Original train/dev/test split from the source paper used; this paper merged train+dev for 5-fold cross-validation.
### Task Construction
Radiology reports from MIMIC-III were paired with manually authored questions by Soni et al. (2022). Each instance has a context (report), question, and answer span (or empty for unanswerable questions). This paper uses the pre-constructed dataset without modification.
### Fidelity
The instruction template is copied verbatim from Appendix B. No concrete input/output instance is available from this paper.
### Example
No explicit task example is provided in this paper. The instruction/prompt template from Appendix B is the only task-level evidence. No radiology report text is quoted.
### Example Input
Not available from this paper. The source dataset requires PhysioNet credentialed access; no public instance-level input can be reproduced without that access.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper. Gold answer spans are part of the RadQA dataset but no specific gold-labeled instance is quoted.
```

#### Scoring standard

```md
### Scoring
Exact Match (EM) — the predicted answer span must exactly match the ground-truth answer span character-for-character. F1 score — token-level overlap between predicted and ground-truth answer spans. Evaluation uses the SQuAD 2.0 evaluation script (Rajpurkar et al., 2018), as adopted by MIMIC-T5 (Lehman et al., 2023).
### Evaluation Dimensions
Exact string match between predicted span and gold answer span. For unanswerable questions, the prediction must be empty to count as correct under exact match.
### Judge Prompt
Not applicable. The evaluation uses deterministic EM/F1 computation; no LLM judge is employed.
```

## 3. CLIP

CLIP (Mullenbach et al., 2021) is an English multi-label classification benchmark derived from hospital discharge summaries in MIMIC-III (Johnson et al., 2016). Each clinical record is labeled with one or more clinical action items such as "patient instructions" and "appointment." Due to long clinical record contexts, this paper follows the MIMIC-T5 methodology (Lehman et al., 2023) of segmenting long records and appropriately mapping labels to the segmented sequences. In this paper, CLIP serves as one of the three MIMIC-III clinical tasks (Section 4).

- **Language:** English (inferred from U.S. source EHR discharge summaries; not explicitly stated in this paper)
- **Clinical Stage:** Discharge / post-discharge planning (inferred from "clinical action items" task framing)
- **Source Clinical Document Type:** Hospital discharge summaries from MIMIC-III
- **Clinical Specialty:** Multi-specialty inpatient care (inferred from discharge summary source)
- **Application Method:** Reused public benchmark; originally introduced by Mullenbach et al. (2021). Requires PhysioNet credentialed access.
- **Role in this paper:** In-distribution clinical benchmark for MIMIC-pre-trained models.

---

### 3.1 Task: Multi-label Clinical Action Item Classification

This task is to read a discharge summary and classify it with zero or more clinical action item labels (e.g., "patient instructions," "appointment") from a predefined set.

#### Task type
Multi-label Text Classification

```md
### Instruction (FLAN-T5 format, Appendix B)
[The paper does not provide a separate FLAN-T5 instruction for CLIP beyond the T5-prefix format below.]
### Instruction (T5-prefix format, Appendix B)
Context: {context}. Label the above sentence as an empty string or as one or more of the following options, delimited by comma: Options: {labels}
### Input
A hospital discharge summary text (context), potentially exceeding the model's maximum sequence length and requiring segmentation. A set of candidate action item labels is provided in the prompt.
### Output
Zero or more action-item class labels, comma-delimited. The paper uses binary matrix transformation for evaluation: predicted labels are converted to a multi-hot binary vector indicating presence/absence of each class.
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material. The paper provides only the instruction/prompt template above.
### Search Depth
Paper body + appendix + cached source text. Linked source artifacts (MIMIC-III credentialed data, original CLIP paper) not inspected for this summary.
### Example Type
No example available from the current paper. The instruction template is provided but no verbatim discharge summary text or gold label set is quoted.
### Source Dataset / Artifact
MIMIC-III discharge summaries (Johnson et al., 2016), annotated with clinical action-item labels by Mullenbach et al. (2021). Original train/dev/test split from the source paper used; this paper merged train+dev for 5-fold cross-validation.
### Task Construction
Discharge summaries from MIMIC-III were annotated with action-item labels. Due to the long length of clinical records, the paper follows MIMIC-T5's approach: records are segmented into chunks, and labels are appropriately mapped to each segment. The exact label vocabulary is not listed in this paper but is described by Mullenbach et al. (2021).
### Fidelity
The instruction template is copied verbatim from Appendix B. No concrete input/output instance is available from this paper.
### Example
No explicit task example is provided in this paper. The instruction/prompt template from Appendix B is the only task-level evidence. No discharge summary text is quoted.
### Example Input
Not available from this paper. The source dataset requires PhysioNet credentialed access; no public instance-level input can be reproduced without that access.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper. Gold action-item labels are part of the CLIP dataset but no specific gold-labeled instance is quoted.
```

#### Scoring standard

```md
### Scoring
Macro-F1 and Micro-F1 scores. Following Lehman et al. (2023), predicted outputs are transformed into binary matrices whose dimensions encode presence/absence of each class label. sklearn.metrics is used for F1 calculation.
### Evaluation Dimensions
Label-level precision, recall, and F1. Macro-F1 averages F1 equally across all classes; Micro-F1 aggregates contributions from all classes globally.
### Judge Prompt
Not applicable. The evaluation uses deterministic F1 computation via sklearn; no LLM judge is employed.
```

## 4. Hallmarks of Cancer (HOC)

HOC (Baker et al., 2015) is an English multi-label classification benchmark derived from PubMed publication abstracts. Each sentence is annotated for the presence of zero or more hallmarks of cancer (e.g., "sustaining proliferative signaling," "activating invasion and metastasis"). This paper uses the sentence-level dataset available on Huggingface (Section 3.2, Appendix A). In this paper, HOC serves as one of three biomedical benchmarks used to evaluate the effect of biomedical-domain pre-training in SciFive+MIMIC-T5 versus MIMIC-T5 (Section 4).

- **Language:** English (inferred from PubMed source; not explicitly stated in this paper)
- **Clinical Stage:** Not applicable — the task operates on biomedical research literature rather than clinical care documents.
- **Source Clinical Document Type:** PubMed publication abstracts (biomedical literature, not clinical EHR text)
- **Clinical Specialty:** Oncology / cancer biology (inferred from "hallmarks of cancer" annotation schema)
- **Application Method:** Reused public benchmark; originally introduced by Baker et al. (2015). The paper states the dataset is accessible on Huggingface. Not subject to clinical data access restrictions.
- **Role in this paper:** Biomedical (non-clinical) benchmark used to evaluate domain generalization across pre-training strategies.

---

### 4.1 Task: Multi-label Hallmark of Cancer Classification

This task is to assign zero or more cancer hallmark labels to a sentence from a PubMed abstract.

#### Task type
Multi-label Text Classification

```md
### Instruction (FLAN-T5 format, Appendix B)
[The paper does not provide a separate FLAN-T5 instruction for HOC beyond the T5-prefix format below.]
### Instruction (T5-prefix format, Appendix B)
Sentence: {input} Assign the above sentence as zero or more of the following class labels: {labels}
### Input
A single sentence from a PubMed publication abstract. A set of cancer hallmark class labels is provided in the prompt.
### Output
Zero or more hallmark-of-cancer class labels, indicating which hallmarks are discussed in the sentence.
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material. The paper notes the dataset is available on Huggingface but does not reproduce example rows from it. The instruction template is the only task-level evidence in this paper.
### Search Depth
Paper body + appendix + cached source text. The Huggingface dataset page for HOC was not inspected for this summary.
### Example Type
No example available from the current paper. The instruction template is provided but no verbatim PubMed sentence or gold hallmark label set is quoted.
### Source Dataset / Artifact
HOC sentence-level dataset (Baker et al., 2015), derived from PubMed abstracts and available on Huggingface. Original train/dev/test split from the source paper used; this paper merged train+dev for 5-fold cross-validation.
### Task Construction
PubMed abstracts were segmented into sentences and each sentence was manually annotated for the presence of hallmarks of cancer by Baker et al. (2015). The sentence-level HOC dataset is available on Huggingface.
### Fidelity
The instruction template is copied verbatim from Appendix B. No concrete input/output instance is available from this paper.
### Example
No explicit task example is provided in this paper. The instruction/prompt template from Appendix B is the only task-level evidence.
### Example Input
Not available from this paper. The HOC dataset is public on Huggingface and contains sentence-level instances, but none are reproduced in this paper.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper. Gold hallmark labels are part of the HOC dataset but no specific gold-labeled instance is quoted.
```

#### Scoring standard

```md
### Scoring
F1 score, Precision, and Recall. Following Phan et al. (2021) and Yasunaga et al. (2022), evaluation is performed on the generated output text matched against gold labels.
### Evaluation Dimensions
Label-level precision, recall, and F1 for multi-label classification.
### Judge Prompt
Not applicable. The evaluation uses deterministic F1 computation; no LLM judge is employed.
```

## 5. BC5CDR-disease

BC5CDR-disease (Li et al., 2016b) is an English disease named entity recognition benchmark that annotates 1,500 PubMed articles with disease entity labels. In the T5 text-to-text format, the model input is a sentence and the model output is the same sentence with disease entities enclosed by "disease*" and "*disease" markers — a text generation approach to NER. This paper uses the version preprocessed by SciFive (Phan et al., 2021), available in the SciFive repository. In this paper, BC5CDR-disease serves as one of three biomedical benchmarks (Section 4).

- **Language:** English (inferred from PubMed source; not explicitly stated in this paper)
- **Clinical Stage:** Not applicable — the task operates on biomedical research literature rather than clinical care documents.
- **Source Clinical Document Type:** Full-text PubMed articles (biomedical literature, not clinical EHR text)
- **Clinical Specialty:** Multi-disease (covers disease entities across biomedical literature)
- **Application Method:** Reused public benchmark; originally introduced by Li et al. (2016b) as part of the BioCreative V CDR task. Distributed via the SciFive repository (Phan et al., 2021).
- **Role in this paper:** Biomedical (non-clinical) benchmark used to evaluate domain generalization across pre-training strategies.

---

### 5.1 Task: Disease Named Entity Recognition

This task is to identify all disease mentions in a biomedical text sentence and output the sentence with disease entities marked up.

#### Task type
Named Entity Recognition (via text-to-text generation)

```md
### Instruction (FLAN-T5 format, Appendix B)
[The paper does not provide a separate FLAN-T5 instruction for BC5CDR-disease beyond the T5-prefix format below.]
### Instruction (T5-prefix format, Appendix B, shared with NCBI-disease)
Sentence: {input} Identify and label disease terms in the sentence:
### Input
A single sentence from a full-text PubMed article.
### Output
The same sentence as input but with all disease mentions enclosed by the markers "disease*" and "*disease". Example: "The patient was diagnosed with disease*breast cancer*disease." The output is converted to BIO-tag sequences (B-disease, I-disease, O) for evaluation.
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material. The paper references the SciFive repository for preprocessed data but does not reproduce example rows. The instruction template and output format description are the only task-level evidence in this paper.
### Search Depth
Paper body + appendix + cached source text. The SciFive repository and original BC5CDR paper were not inspected for this summary.
### Example Type
No example available from the current paper. The instruction template and output format specification are provided but no verbatim PubMed sentence or gold entity markup is quoted.
### Source Dataset / Artifact
BC5CDR-disease corpus (Li et al., 2016b), consisting of 1,500 PubMed articles with disease entity annotations. Preprocessed by SciFive (Phan et al., 2021) and available in the SciFive repository. Original train/dev/test split from the source paper used; this paper merged train+dev for 5-fold cross-validation.
### Task Construction
The BC5CDR corpus annotates disease entity spans in 1,500 PubMed articles. For T5 text-to-text format, the task is reformulated such that the model receives raw text and must produce the same text with disease entities surrounded by "disease*" / "*disease" markers. For evaluation (Appendix E), the generated output is converted to BIO tag sequences and evaluated with seqeval (Nakayama, 2018).
### Fidelity
The instruction template and output format specification are copied verbatim from Appendix A and B. No concrete input/output instance is available from this paper.
### Example
No explicit task example is provided in this paper. The instruction/prompt template from Appendix B and the output format description from Appendix A are the only task-level evidence.
### Example Input
Not available from this paper. The BC5CDR-disease dataset is public via the SciFive repository and contains sentence-level instances, but none are reproduced in this paper.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper. Gold disease entity annotations are part of the BC5CDR-disease dataset but no specific gold-labeled instance is quoted.
```

#### Scoring standard

```md
### Scoring
F1 score, Precision, and Recall at the entity level using span-level evaluation. The paper follows the SciFive (Phan et al., 2021) evaluation protocol: generated sentence outputs are converted to BIO tag sequences (B-disease, I-disease, O) and evaluated using seqeval (Ramshaw and Marcus, 1995; Nakayama, 2018). An entity prediction is counted as correct if both the span boundaries and entity type match.
### Evaluation Dimensions
Entity-level precision, recall, and F1. Span-exact matching for disease entity boundaries.
### Judge Prompt
Not applicable. The evaluation uses deterministic span-level F1 computation via seqeval; no LLM judge is employed.
```

## 6. NCBI-disease

NCBI-disease (Dogan et al., 2014) is an English disease named entity recognition benchmark derived from PubMed abstracts. Similar to BC5CDR-disease, the T5 text-to-text format requires the model to output the input sentence with disease entities enclosed by "disease*" and "*disease" markers. This paper uses the version preprocessed by SciFive (Phan et al., 2021), available in the SciFive repository. In this paper, NCBI-disease serves as one of three biomedical benchmarks (Section 4).

- **Language:** English (inferred from PubMed source; not explicitly stated in this paper)
- **Clinical Stage:** Not applicable — the task operates on biomedical research literature rather than clinical care documents.
- **Source Clinical Document Type:** PubMed abstracts (biomedical literature, not clinical EHR text)
- **Clinical Specialty:** Multi-disease (covers disease entities across biomedical literature)
- **Application Method:** Reused public benchmark; originally introduced by Dogan et al. (2014). Distributed via the SciFive repository (Phan et al., 2021).
- **Role in this paper:** Biomedical (non-clinical) benchmark used to evaluate domain generalization across pre-training strategies.

---

### 6.1 Task: Disease Named Entity Recognition

This task is to identify all disease mentions in a PubMed abstract sentence and output the sentence with disease entities marked up.

#### Task type
Named Entity Recognition (via text-to-text generation)

```md
### Instruction (FLAN-T5 format, Appendix B)
[The paper does not provide a separate FLAN-T5 instruction for NCBI-disease beyond the T5-prefix format below.]
### Instruction (T5-prefix format, Appendix B, shared with BC5CDR-disease)
Sentence: {input} Identify and label disease terms in the sentence:
### Input
A single sentence from a PubMed abstract.
### Output
The same sentence as input but with all disease mentions enclosed by the markers "disease*" and "*disease". The output is converted to BIO-tag sequences (B-disease, I-disease, O) for evaluation.
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material. The paper references the SciFive repository for preprocessed data but does not reproduce example rows. The instruction template and output format description are the only task-level evidence in this paper.
### Search Depth
Paper body + appendix + cached source text. The SciFive repository and original NCBI-disease paper were not inspected for this summary.
### Example Type
No example available from the current paper. The instruction template and output format specification are provided but no verbatim PubMed sentence or gold entity markup is quoted.
### Source Dataset / Artifact
NCBI Disease Corpus (Dogan et al., 2014), consisting of PubMed abstracts annotated with disease mentions. Preprocessed by SciFive (Phan et al., 2021) and available in the SciFive repository. Original train/dev/test split from the source paper used; this paper merged train+dev for 5-fold cross-validation.
### Task Construction
The NCBI Disease Corpus annotates disease entity spans in PubMed abstracts. For T5 text-to-text format, the task is reformulated such that the model receives raw text and must produce the same text with disease entities surrounded by "disease*" / "*disease" markers. For evaluation (Appendix E), the generated output is converted to BIO tag sequences and evaluated with seqeval (Nakayama, 2018).
### Fidelity
The instruction template and output format specification are copied verbatim from Appendix A and B. No concrete input/output instance is available from this paper.
### Example
No explicit task example is provided in this paper. The instruction/prompt template from Appendix B and the output format description from Appendix A are the only task-level evidence.
### Example Input
Not available from this paper. The NCBI-disease dataset is public via the SciFive repository and contains sentence-level instances, but none are reproduced in this paper.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper. Gold disease entity annotations are part of the NCBI-disease dataset but no specific gold-labeled instance is quoted.
```

#### Scoring standard

```md
### Scoring
F1 score, Precision, and Recall at the entity level using span-level evaluation. Same evaluation protocol as BC5CDR-disease: generated output converted to BIO tags, evaluated with seqeval (Ramshaw and Marcus, 1995; Nakayama, 2018).
### Evaluation Dimensions
Entity-level precision, recall, and F1. Span-exact matching for disease entity boundaries.
### Judge Prompt
Not applicable. The evaluation uses deterministic span-level F1 computation via seqeval; no LLM judge is employed.
```

## 7. Clinical Stigmatizing Language

The Clinical Stigmatizing Language benchmark (Harrigian et al., 2023b) characterizes stigmatizing language about patients in clinical text through three multi-class classification sub-tasks: Credibility & Obstinacy, Compliance, and Descriptors. The benchmark is evaluated on two distinct data sources in this paper (Section 5):

- **MIMIC-IV** (Johnson et al., 2023): In-distribution clinical text from the same source system used to pre-train MIMIC-T5. Annotations from Harrigian et al. (2023b).
- **Hospital System (anonymized)**: Out-of-distribution clinical text from a separate anonymized hospital system covering five medical specialties (Internal Medicine, Emergency Medicine, Pediatrics, OB-GYN, Surgery). Annotations from Harrigian et al. (2023b).

This benchmark is the primary out-of-domain generalization test in this paper (Section 5). It is also used in low-resource experiments with 1%, 5%, and 25% downsampled training data (Section 6).

- **Language:** English (inferred from U.S. source clinical text; not explicitly stated in this paper)
- **Clinical Stage:** Inpatient and outpatient clinical encounters (inferred — MIMIC-IV covers ICU and general inpatient; Hospital System covers five specialties)
- **Source Clinical Document Type:** Clinical notes and medical records; the exact note type (e.g., progress notes, discharge summaries) is not specified in this paper.
- **Clinical Specialty:** Multi-specialty (MIMIC-IV); Internal Medicine, Emergency Medicine, Pediatrics, OB-GYN, Surgery (Hospital System anonymized)
- **Application Method:** Reused public benchmark; originally introduced by Harrigian et al. (2023b). MIMIC-IV portion requires PhysioNet credentialed access. Hospital System portion requires IRB approval from the respective institution.
- **Role in this paper:** Out-of-domain generalization benchmark (both MIMIC-IV and Hospital System data sources). Also used in low-resource experiments with downsampled training data (1%, 5%, 25%).

---

### 7.1 Task: Credibility & Obstinacy Classification

This task is to classify a clinical sentence as expressing disbelief, describing a difficult patient, or using exclusionary language, regarding the credibility and obstinacy attributed to the patient by the clinical author.

#### Task type
Multi-class Text Classification

```md
### Instruction (FLAN-T5 format, Appendix B)
Classify this sentence as difficult, disbelief, or exclude, regarding the credibility and obstinacy of the patient: {input}
### Instruction (T5-prefix format, Appendix B)
Keyword prefix: "adamant" before the input text.
### Input
A single clinical sentence from a medical record (MIMIC-IV or Hospital System anonymized).
### Output
One of three class labels: difficult / disbelief / exclude
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material. The paper provides the instruction template and label descriptions but no verbatim clinical sentence example.
### Search Depth
Paper body + appendix + cached source text. Linked source artifacts (MIMIC-IV credentialed data, Harrigian et al. 2023b paper) not inspected for this summary.
### Example Type
No example available from the current paper. The instruction template and class label descriptions are provided but no verbatim clinical sentence or gold label is quoted.
### Source Dataset / Artifact
MIMIC-IV clinical notes (Johnson et al., 2023) annotated by Harrigian et al. (2023b). Hospital System (anonymized) clinical notes from five specialties annotated by Harrigian et al. (2023b). This paper performed 5-fold cross-validation with downsampled training subsets at 1%, 5%, and 25%.
### Task Construction
Clinical sentences from MIMIC-IV and Hospital System were annotated for stigmatizing language categories by Harrigian et al. (2023b). The three sub-tasks (Credibility & Obstinacy, Compliance, Descriptors) are treated as independent multi-class classification problems. The annotation labels are: Disbelief (the author expresses doubt about the patient's account), Difficult (the patient is described as challenging), Exclude (the author uses exclusionary language about the patient).
### Fidelity
The instruction template and class label descriptions are copied from Appendix A and B. No concrete input/output instance is available from this paper.
### Example
No explicit task example is provided in this paper. The instruction/prompt template from Appendix B and the label descriptions from Appendix A are the only task-level evidence.
### Example Input
Not available from this paper. Source datasets require credentialed/IRB access.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper. Gold labels are part of the Harrigian et al. (2023b) dataset but no specific gold-labeled instance is quoted.
```

#### Scoring standard

```md
### Scoring
Macro-F1 score computed using sklearn.metrics. The paper reports mean macro-F1 and 95% confidence intervals across 5-fold cross-validation, using a bootstrap procedure (Appendix E).
### Evaluation Dimensions
Class-level macro-averaged precision, recall, and F1 across the three credibility/obstinacy categories.
### Judge Prompt
Not applicable. The evaluation uses deterministic macro-F1 computation; no LLM judge is employed.
```

---

### 7.2 Task: Compliance Classification

This task is to classify a clinical sentence as expressing negative, neutral, or positive sentiment regarding the patient's compliance with medical advice.

#### Task type
Multi-class Text Classification

```md
### Instruction (FLAN-T5 format, Appendix B)
Classify this sentence as negative, neutral, or positive, regarding the patient's compliance with medical advice: {input}
### Instruction (T5-prefix format, Appendix B)
Keyword prefix: "compliance" before the input text.
### Input
A single clinical sentence from a medical record (MIMIC-IV or Hospital System anonymized).
### Output
One of three class labels: negative / neutral / positive
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material.
### Search Depth
Paper body + appendix + cached source text. Linked source artifacts not inspected for this summary.
### Example Type
No example available from the current paper.
### Source Dataset / Artifact
Same source datasets as Task 7.1 (MIMIC-IV and Hospital System anonymized), annotated by Harrigian et al. (2023b). 5-fold cross-validation; 1%, 5%, and 25% downsampling experiments.
### Task Construction
Clinical sentences annotated for compliance-related sentiment: Negative (patient non-adherent or resistant), Neutral (neutral description of compliance), Positive (patient described as adherent or cooperative).
### Fidelity
Instruction template and label descriptions copied from Appendix A and B. No concrete instance available.
### Example
No explicit task example is provided in this paper.
### Example Input
Not available from this paper. Source datasets require credentialed/IRB access.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper.
```

#### Scoring standard

```md
### Scoring
Macro-F1 score computed using sklearn.metrics, with 95% confidence intervals via bootstrap across 5-fold cross-validation.
### Evaluation Dimensions
Class-level macro-averaged precision, recall, and F1 across the three compliance categories.
### Judge Prompt
Not applicable. The evaluation uses deterministic macro-F1 computation; no LLM judge is employed.
```

---

### 7.3 Task: Descriptors Classification

This task is to classify a clinical sentence regarding the descriptors used to characterize the patient's behavior and demeanor, with four possible categories.

#### Task type
Multi-class Text Classification

```md
### Instruction (FLAN-T5 format, Appendix B)
Classify this sentence as exclude, negative, neutral, or positive, regarding the patient's behavior and demeanor: {input}
### Instruction (T5-prefix format, Appendix B)
Keyword prefix: "other" before the input text.
### Input
A single clinical sentence from a medical record (MIMIC-IV or Hospital System anonymized).
### Output
One of four class labels: exclude / negative / neutral / positive
```

#### Task example

```md
### Example Provenance
No concrete dataset-instance example is provided in the paper body, appendix, or supplementary material.
### Search Depth
Paper body + appendix + cached source text. Linked source artifacts not inspected for this summary.
### Example Type
No example available from the current paper.
### Source Dataset / Artifact
Same source datasets as Task 7.1 and 7.2, annotated by Harrigian et al. (2023b). 5-fold cross-validation; 1%, 5%, and 25% downsampling experiments.
### Task Construction
Clinical sentences annotated for behavioral descriptors: Exclude (exclusionary language about patient behavior), Negative (negative characterization), Neutral (neutral description), Positive (positive characterization). This sub-task has 4 output classes, distinguishing it from the 3-class Credibility & Obstinacy and Compliance sub-tasks.
### Fidelity
Instruction template and label descriptions copied from Appendix A and B. No concrete instance available.
### Example
No explicit task example is provided in this paper.
### Example Input
Not available from this paper. Source datasets require credentialed/IRB access.
### Example Output
Not available from this paper.
### Gold / Reference Answer
Not explicitly provided in this paper.
```

#### Scoring standard

```md
### Scoring
Macro-F1 score computed using sklearn.metrics, with 95% confidence intervals via bootstrap across 5-fold cross-validation.
### Evaluation Dimensions
Class-level macro-averaged precision, recall, and F1 across the four descriptor categories.
### Judge Prompt
Not applicable. The evaluation uses deterministic macro-F1 computation; no LLM judge is employed.
```
