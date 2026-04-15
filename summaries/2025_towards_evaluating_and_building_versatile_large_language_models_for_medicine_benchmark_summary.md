<!-- paper_key: "2025_towards_evaluating_and_building_versatile_large_language_models_for_medicine" -->
<!-- paper_url: "https://www.nature.com/articles/s41746-024-01390-4" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *Towards evaluating and building versatile large language models for medicine*

Source paper: [https://www.nature.com/articles/s41746-024-01390-4](https://www.nature.com/articles/s41746-024-01390-4)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Cached PDF: [`../papers/2025_towards_evaluating_and_building_versatile_large_language_models_for_medicine/source.pdf`](../papers/2025_towards_evaluating_and_building_versatile_large_language_models_for_medicine/source.pdf)
- Extracted text: [`../papers/2025_towards_evaluating_and_building_versatile_large_language_models_for_medicine/source.txt`](../papers/2025_towards_evaluating_and_building_versatile_large_language_models_for_medicine/source.txt)
- Normalization choice: `MedS-Bench` is treated here as a paper-level umbrella evaluation rather than a single monolithic benchmark entry. The benchmark sections below are split by constituent dataset / sub-benchmark actually reported by the paper.
- Normalization choice: I keep `MMedBench` as one constituent benchmark with language-specific task sections because Tables 1 and 5 report it that way, even though Supplementary Table 4 appears to count some of its underlying source datasets separately. This reconciliation is an explicit inference.
- Normalization choice: I keep `MIMIC-IV Report` as one constituent dataset with three explicitly reported summarization tasks (`Ultrasound`, `CT`, `MRI`). The supplement says the evaluation covered 1430 cases across multiple modality/body-region combinations, but the paper does not enumerate every such sub-benchmark in the result tables.
- Inventory note: under this normalization, the paper yields **23 directly reported dataset sections** and **43 explicitly named task sections** below. The paper's headline claim of `28 existing datasets` and `52 tasks` likely reflects finer-grained source-dataset accounting inside multilingual / modality-aggregated benchmarks such as `MMedBench` and `MIMIC-IV Report`. That reconciliation is an inference, not a directly stated decomposition.
- Instruction fidelity note: the paper says each dataset was reformatted into an instruction-prompted QA format with hand-crafted definitions, but it does not publish the full per-task benchmark instructions verbatim. Where official MedS-Bench / MedS-Ins task files or preprocessing scripts expose exact definitions, I copy those verbatim; otherwise the `Instruction` block is a normalized paraphrase of the published task description.
- Example-search rerun (`2026-04-15`): the article and supplement still do not print benchmark-specific worked MedS-Bench instances, but the linked official artifacts (`Henrychur/MedS-Bench`, `MAGIC-AI4Med/MedS-Ins`, source benchmark repos, and public PhysioNet landing pages) do expose concrete task files, preprocessing rules, and example-oriented fields. This pass eliminates the remaining empty example placeholders by either inlining artifact-level samples or documenting the exact released input/output construction plus access restrictions when the underlying source data are credential-gated.
- Prompting note: Supplementary `Evaluation Settings` states that all evaluations use a 3-shot prompt template except MCQA tasks, which are evaluated zero-shot to align with prior work. The generic few-shot template is `Case1 ... Case3 ... {Manually Written Definitions} Please learn from the few-shot cases to see what content you have to output. {Input Case}`.
- Metric fidelity note: Supplementary Table 4 appears visually misaligned for Information Extraction and Named Entity Recognition metrics. I follow the main text plus Tables 3 and 6 where metric usage is stated more clearly.
- Registry note: per user instruction, this summary does **not** modify the registry.

## Verifier Notes

- Verified paper-level claims (`11` high-level categories, `28` existing datasets, `52` tasks, instruction-prompted reformatting) against the main article and Supplementary `Task Category Details`.
- Verified benchmark-level test split / sample-count statements against the supplementary PDF downloaded from the article's official supplement.
- Verified the benchmark-wide prompting template and the absence of task-specific published prompt bodies against the supplementary `Evaluation Settings`.
- Verified that the paper uses deterministic reference-based metrics throughout; no LLM-as-a-judge prompt is provided for any MedS-Bench task.
- Verified that the paper itself does not publish benchmark-specific worked examples. Official MedS-Bench task files, MedS-Ins preprocessing scripts, source benchmark repositories, and public PhysioNet landing pages were then used to inline concrete instances or exact task-construction details with explicit artifact provenance.

## Paper-Level Umbrella Evaluation

MedS-Bench is a paper-level umbrella evaluation introduced by the authors to assess medical LLMs beyond multiple-choice exams. The paper states that the umbrella benchmark covers **11 high-level clinical task categories**, is **derived from 28 existing datasets**, and addresses **52 distinct tasks** after converting each source dataset into an instruction-prompted question-answering format. The authors evaluate nine mainstream medical or general LLMs and use MedS-Bench as the evaluation suite paired with MedS-Ins as the training corpus.

- **Task categories covered:** Multilingual Multiple-choice Question Answering, Text Summarization, Information Extraction, Explanation/Rationale, Named Entity Recognition, Diagnosis, Treatment Planning, Clinical Outcome Prediction, Text Classification, Fact Verification, and Natural Language Inference.
- **Prompting setup:** 3-shot few-shot prompting for all non-MCQA tasks; zero-shot for MCQA tasks to align with prior work.
- **Split rule:** official train/test splits were used when available; for datasets without predefined train-test splits, the supplement states they were partitioned at a `9:1` ratio.
- **Cost-control sampling rule:** many large benchmarks were downsampled for evaluation, commonly to `100` cases for long-context summarization tasks and `1500` cases for several other task families; MCQA tasks reused published full-test results where available.
- **Metric families:** Accuracy for single-answer closed-set tasks; macro Precision/Recall/F1 for multi-label classification; BLEU and ROUGE for free-form generation; F1-family metrics for NER, with Table 6 reporting F1 specifically.
- **Judge prompt availability:** none. The benchmark does not use an LLM judge.

## Benchmark Inventory

| Dataset / Sub-benchmark | MedS-Bench Tasks Reported Here | Language | MedS-Bench Role | Notes |
| --- | --- | --- | --- | --- |
| MedQA | 1 | English | Reused source benchmark | 4-option English version only |
| PubMedQA | 2 | English | Reused source benchmark with 2 MedS-Bench reformulations | MCQA plus answer verification |
| MedMCQA | 1 | English | Reused source benchmark | Official test split |
| MMedBench | 11 | Multilingual | Reused source benchmark | 5 MCQA language tasks + 6 rationale tasks |
| MedQSum | 1 | English (inferred) | Reused source benchmark | Summarization with 100 sampled test cases |
| RCT-Text | 1 | English (inferred) | Reused source benchmark | Study-conclusion summarization |
| MIMIC-CXR | 1 | English | Reused source benchmark | X-ray report summarization |
| MIMIC-IV Report | 3 | English | Reused source benchmark | Ultrasound / CT / MRI summarization tasks |
| ADE Corpus | 1 | English | Reused source benchmark | Drug dose extraction only |
| PICO | 3 | English | Reused source benchmark | Participant / intervention / outcome extraction |
| PMC-Patient | 1 | English | Reused source benchmark | Basic demographic extraction |
| PUBHEALTH / PUBLICHEALTH | 2 | English | Reused source benchmark with 2 MedS-Bench reformulations | Explanation plus verification; naming varies across paper |
| Human Disease Ontology (DO) | 1 | English (inferred) | Reused source benchmark | Concept explanation |
| BioLORD | 1 | English (inferred) | Reused source benchmark | Concept explanation |
| BC4Chem | 1 | English | Reused source benchmark | Chemical NER |
| BC5CDR | 2 | English | Reused source benchmark | Chemical NER + disease NER |
| Species800 | 1 | English | Reused source benchmark | Organism NER |
| DDXPlus | 1 | English | Reused source benchmark | Diagnosis from dialogue |
| SEER | 1 | English | Reused source benchmark | Treatment planning |
| MIMIC4ED Benchmark | 3 | English | Reused source benchmark | Hospitalization / 72h ED revisit / critical triage |
| HoC | 1 | English | Reused source benchmark | Multi-label text classification |
| EBMS | 1 | Not explicitly stated | Reused source benchmark | Only sparse benchmark details are given |
| MedNLI | 2 | English | Reused source benchmark with 2 MedS-Bench reformulations | Discriminative + generative entailment |

## 1. MedQA

MedQA is a constituent source benchmark under the MedS-Bench umbrella for medical multiple-choice question answering. The supplement describes it as a collection of medical MCQs with both 4-option and 5-option versions across English, Simplified Chinese, and Traditional Chinese, but the paper explicitly evaluates only the **4-option English version** and uses the official split with **1,273** test samples.

- **Language:** English
- **Clinical Stage:** Medical knowledge assessment (inferred)
- **Source Clinical Document Type:** Exam-style medical multiple-choice questions
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark reformatted into MedS-Bench instruction-QA format
- **Split / Sample Info:** Official test split; 1,273 test samples.

### 1.1 Task: MedQA Multiple-choice Question Answering

This task is to answer an English medical multiple-choice exam question by selecting the single correct option.

### Task type
Question Answering / Classification

- **Task provenance in MedS-Bench:** Reused source task with standardized prompting.
- **Instruction fidelity note:** Exact hand-written benchmark instruction is not provided verbatim; the block below is normalized from the supplement.

```md
### Instruction
Normalized from the published task description: answer the English MedQA medical multiple-choice question by selecting the single correct option from the provided choices.
### Input
A medical exam question with four answer choices.
### Output
One selected answer option. The paper does not explicitly standardize whether this should be returned as a letter, full option text, or another exact output string.
```

### Task example

```md
### Example
Artifact-level example from official `MCQA/task57_medqa_question_answering_en.jsonl` (not printed in the paper):

Input:
Question: A junior orthopaedic surgery resident is completing a carpal tunnel repair with the department chairman as the attending physician. During the case, the resident inadvertently cuts a flexor tendon. The tendon is repaired without complication. The attending tells the resident that the patient will do fine, and there is no need to report this minor complication that will not harm the patient, as he does not want to make the patient worry unnecessarily. He tells the resident to leave this complication out of the operative report. Which of the following is the correct next action for the resident to take?
Options:
A: Disclose the error to the patient and put it in the operative report
B: Tell the attending that he cannot fail to disclose this mistake
C: Report the physician to the ethics committee
D: Refuse to dictate the operative report

Output:
The right answer is B: Tell the attending that he cannot fail to disclose this mistake
```

### Scoring standard

```md
### Scoring
Accuracy against the gold answer option.
### Evaluation Dimensions
Deterministic answer matching only. No additional rubric dimensions are described.
### Judge Prompt
Not applicable. The paper uses deterministic metrics and does not provide an LLM judge prompt.
```

## 2. PubMedQA

PubMedQA appears twice inside MedS-Bench: once as a closed-domain yes/no/maybe question answering benchmark and once as an answer-verification benchmark. The supplement says the original dataset is based on PubMed abstracts and that the MCQA-style evaluation uses the manually labeled `PQA-L` split with **1,000** test samples; the fact-verification reformulation uses **1,188** test samples.

- **Language:** English
- **Clinical Stage:** Medical knowledge / literature interpretation (inferred)
- **Source Clinical Document Type:** Research abstract
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark reformatted into two MedS-Bench tasks
- **Split / Sample Info:** MCQA uses `PQA-L` with 1,000 samples; answer verification uses 1,188 test samples.

### 2.1 Task: PubMedQA Question Answering

This task is to answer a research question from a PubMed abstract with one of the closed-set answers `yes`, `no`, or `maybe`.

### Task type
Question Answering / Classification

- **Task provenance in MedS-Bench:** Reused source task with standardized prompting.
- **Instruction fidelity note:** Normalized from the supplement because the exact benchmark prompt is not published.

```md
### Instruction
Normalized from the published task description: read the PubMed abstract and answer the associated medical research question using one of the allowed labels: yes, no, or maybe.
### Input
A PubMed abstract and its associated research question.
### Output
A single label: yes, no, or maybe.
```

### Task example

```md
### Example
Artifact-level example from official `MCQA/task123_pubmedqa_test_set.json` (not printed in the paper):

Input:
Context: Programmed cell death (PCD) is the regulated death of cells within an organism. The lace plant (Aponogeton madagascariensis) produces perforations in its leaves through PCD. The leaves of the plant consist of a latticework of longitudinal and transverse veins enclosing areoles. PCD occurs in the cells at the center of these areoles and progresses outwards, stopping approximately five cells from the vasculature. The role of mitochondria during PCD has been recognized in animals; however, it has been less studied during PCD in plants. The following paper elucidates the role of mitochondrial dynamics during developmentally regulated PCD in vivo in A. madagascariensis. A single areole within a window stage leaf (PCD is occurring) was divided into three areas based on the progression of PCD; cells that will not undergo PCD (NPCD), cells in early stages of PCD (EPCD), and cells in late stages of PCD (LPCD). Window stage leaves were stained with the mitochondrial dye MitoTracker Red CMXRos and examined. Mitochondrial dynamics were delineated into four categories (M1-M4) based on characteristics including distribution, motility, and membrane potential (ΔΨm). A TUNEL assay showed fragmented nDNA in a gradient over these mitochondrial stages. Chloroplasts and transvacuolar strands were also examined using live cell imaging. The possible importance of mitochondrial permeability transition pore (PTP) formation during PCD was indirectly examined via in vivo cyclosporine A (CsA) treatment. This treatment resulted in lace plant leaves with a significantly lower number of perforations compared to controls, and that displayed mitochondrial dynamics similar to that of non-PCD cells.
Question: Do mitochondria play a role in remodelling lace plant leaves during programmed cell death?

Output:
yes
```

### Scoring standard

```md
### Scoring
Accuracy on the yes / no / maybe label.
### Evaluation Dimensions
Deterministic comparison to the reference label.
### Judge Prompt
Not applicable. No LLM judge is used.
```

### 2.2 Task: PubMedQA Answer Verification

This task is to determine whether a provided answer actually answers the medical question in the released MedS-Bench PubMedQA verification artifact.

### Task type
Fact Verification / Classification

- **Task provenance in MedS-Bench:** MedS-Bench reformulation of the original PubMedQA source benchmark.
- **Instruction fidelity note:** Normalized from the supplement because the exact prompt wording is unavailable.

```md
### Instruction
Official task definition from `Fact_verication/task12_pubmedqa_classification.json`: Given a passage with a question and an answer to that question, classify if the answer actually answers the question into `yes` or `no`. Output `yes` if the answer answers the question and output `no` if the answer does not answer the question.
### Input
In the released MedS-Bench task file, each instance is serialized as:
`Question: ...`
`Answer: ...`
The supporting abstract passage from the original PubMedQA source benchmark is not surfaced in the released instance text.
### Output
One label: `yes` or `no`.
```

### Task example

```md
### Example
Artifact-level example from official `Fact_verication/task12_pubmedqa_classification.json`:

Input:
Question: Is urinary 5-HIAA excretion increased in patients with head and neck paragangliomas?
Answer: Urinary 5-HIAA excretion is within the normal reference range in almost all HNPGL patients. Therefore, this parameter has no clinical relevance in the routine clinical assessment of HNPGL patients.

Output:
no

Gold / Reference:
`output: ["no"]`
```

### Scoring standard

```md
### Scoring
Accuracy on the verification decision.
### Evaluation Dimensions
Deterministic answer-verification correctness only.
### Judge Prompt
Not applicable. No LLM judge is used.
```

## 3. MedMCQA

MedMCQA is used in MedS-Bench as a large-scale English medical multiple-choice benchmark. The supplement states that it contains more than 194K entrance-exam questions, each with four choices, and that the official test split contains **4,183** questions.

- **Language:** English
- **Clinical Stage:** Medical knowledge assessment (inferred)
- **Source Clinical Document Type:** Exam-style medical multiple-choice questions
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark reformatted into MedS-Bench instruction-QA format
- **Split / Sample Info:** Official test split with 4,183 questions.

### 3.1 Task: MedMCQA Multiple-choice Question Answering

This task is to answer a four-option medical exam question by selecting the single correct option.

### Task type
Question Answering / Classification

- **Task provenance in MedS-Bench:** Reused source task with standardized prompting.
- **Instruction fidelity note:** Normalized from the supplement because the exact prompt wording is unavailable.

```md
### Instruction
Normalized from the published task description: answer the medical multiple-choice question by selecting the correct option from the four available choices.
### Input
A medical exam question with four choices.
### Output
One selected answer option. The paper does not explicitly define the exact return string format.
```

### Task example

```md
### Example
Artifact-level example from official `MCQA/task122_medmcqa_test_set.json` (not printed in the paper):

Input:
Question: Which of the following is not true for myelinated nerve fibers:
Options:
A. Impulse through myelinated fibers is slower than non-myelinated fibers
B. Membrane currents are generated at nodes of Ranvier
C. Saltatory conduction of impulses is seen
D. Local anesthesia is effective only when the nerve is not covered by myelin sheath.

Output:
The right answer is A: Impulse through myelinated fibers is slower than non-myelinated fibers
```

### Scoring standard

```md
### Scoring
Accuracy against the gold answer option.
### Evaluation Dimensions
Deterministic answer matching only.
### Judge Prompt
Not applicable. No LLM judge is used.
```

## 4. MMedBench

MMedBench is a multilingual constituent benchmark reused in MedS-Bench for both multiple-choice question answering and answer-rationale generation. The supplement describes it as a multilingual medical MCQA benchmark covering Chinese, English, French, Japanese, Russian, and Spanish, with MCQ source material collected from MedQA, IgakuQA, FrenchMedMCQA, RuMedBench / RuMedDaNet, and HeadQA. The paper reports MCQA results for five non-English language subsets and rationale-generation results for all six languages.

- **Language:** Chinese, English, French, Japanese, Russian, Spanish
- **Clinical Stage:** Medical knowledge assessment and rationale generation (inferred)
- **Source Clinical Document Type:** Exam-style medical QA items with reference rationales
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public multilingual benchmark reformatted into MedS-Bench instruction-QA format
- **Split / Sample Info:** MCQA official split: Chinese 3,426; Japanese 199; French 622; Russian 256; Spanish 2,742. Rationale official split: Chinese 200; English 195; French 189; Japanese 190; Russian 173; Spanish 189.

### 4.1 Task: MMedBench MCQA (Chinese)

This task is to answer a Chinese medical multiple-choice question.

### Task type
Question Answering / Classification

- **Instruction fidelity note:** Normalized from the supplement because the exact prompt wording is unavailable.

```md
### Instruction
Normalized from the published task description: answer the Chinese medical multiple-choice question by selecting the single correct option.
### Input
A Chinese medical multiple-choice question and its answer options.
### Output
One selected answer option.
```

### Task example

```md
### Example
Artifact-level example from official source file `MCQA/task58_medqa_question_answering_zh.jsonl`, which MedS-Bench uses for the Chinese MMedBench subset:

Input:
问题: 经调查证实出现医院感染流行时，医院应报告当地卫生行政部门的时间是（　　）。
选项: A: 2小时	B: 4小时内	C: 12小时内	D: 24小时内

Output:
正确答案是 D: 24小时内
```

### Scoring standard

```md
### Scoring
Accuracy on the selected answer option.
### Evaluation Dimensions
Deterministic answer matching.
### Judge Prompt
Not applicable.
```

### 4.2 Task: MMedBench MCQA (Japanese)

This task is to answer a Japanese medical multiple-choice question.

### Task type
Question Answering / Classification

```md
### Instruction
Normalized from the published task description: answer the Japanese medical multiple-choice question by selecting the single correct option.
### Input
A Japanese medical multiple-choice question and its answer options.
### Output
One selected answer option.
```

### Task example

```md
### Example
Artifact-level example from official source file `MCQA/task59_igakuqa_question_answering.jsonl`, which MedS-Bench uses for the Japanese MMedBench subset:

Input:
質問: 異常呼吸あるいは息切れを主訴とする患者の所見と原因の組合せについて正しいのはどれか。
オプション: A: Coarse crackles --------- 喘息	B: 胸部打診で濁音 --------- 気胸	C: 頸静脈の怒張 --------- 右心不全	D: SpO2 95％（room air）--------- 呼吸不全	E: Cheyne-Stokes呼吸 --------- 上気道閉塞

Output:
正しい答えは C: 頸静脈の怒張 --------- 右心不全 です
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic answer matching.
### Judge Prompt
Not applicable.
```

### 4.3 Task: MMedBench MCQA (French)

This task is to answer a French medical multiple-choice question.

### Task type
Question Answering / Classification

```md
### Instruction
Normalized from the published task description: answer the French medical multiple-choice question by selecting the single correct option.
### Input
A French medical multiple-choice question and its answer options.
### Output
One selected answer option.
```

### Task example

```md
### Example
Artifact-level example from official source file `MCQA/task60_frenchmedmcqa_question_answering.jsonl`, which MedS-Bench uses for the French MMedBench subset:

Input:
Question: Parmi les propositions suivantes, indiquer celle qui est exacte. Dans les conditions physiologiques, le pH le plus élevé est mesuré dans:
Options: A: Le suc gastrique	B: La bile vésiculaire	C: Le suc pancréatique	D: La salive	E: Les sécrétions intestinales

Output:
Les bonnes réponses est C: Le suc pancréatique
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic answer matching.
### Judge Prompt
Not applicable.
```

### 4.4 Task: MMedBench MCQA (Russian)

This task is to answer a Russian medical multiple-choice question.

### Task type
Question Answering / Classification

```md
### Instruction
Normalized from the published task description: answer the Russian medical multiple-choice question by selecting the single correct option.
### Input
A Russian medical multiple-choice question and its answer options.
### Output
One selected answer option.
```

### Task example

```md
### Example
Artifact-level example from official source file `MCQA/task61_rumedbench_question_answering.jsonl`, which MedS-Bench uses for the Russian MMedBench subset:

Input:
Вопрос: Противокашлевое действие бутамирата цитрата обусловлено главным образом воздействием на кашлевой центр в мозге?
Варианты: A: да	B: нет

Output:
Правильные ответ: A: да
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic answer matching.
### Judge Prompt
Not applicable.
```

### 4.5 Task: MMedBench MCQA (Spanish)

This task is to answer a Spanish medical multiple-choice question.

### Task type
Question Answering / Classification

```md
### Instruction
Normalized from the published task description: answer the Spanish medical multiple-choice question by selecting the single correct option.
### Input
A Spanish medical multiple-choice question and its answer options.
### Output
One selected answer option.
```

### Task example

```md
### Example
Artifact-level example from official source file `MCQA/task129_headqa_question_answering.jsonl`, which MedS-Bench uses for the Spanish MMedBench subset:

Input:
Pregunta: Forma fibras extracelulares con gran resistencia a la tensión:
Opciones: A: Fibronectina.	B: Colágeno.	C: Integrinas.	D: Proteoglucanos.

Output:
La respuesta correcta es: B: Colágeno.
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic answer matching.
### Judge Prompt
Not applicable.
```

### 4.6 Task: MMedBench Rationale (Chinese)

This task is to generate an explanation or step-by-step rationale for a Chinese medical QA item when the question and answer are already given.

### Task type
Rationale Generation

```md
### Instruction
Normalized from the published task description: given a Chinese medical question and its answer, generate an explanation or step-by-step reasoning that justifies the answer.
### Input
A Chinese medical question together with its correct answer.
### Output
A free-form rationale or explanation.
```

### Task example

```md
### Example
Artifact-level example from official `Rationale/task51_mmedbench_explanation_chinese_test_only.jsonl`:

Input:
问题: 猩红热多在发热后多久出现皮疹（　　）。
选项: A: 12小时之内	B: 12～48小时	C: 60～72小时	D: 大于96小时
正确答案是 B: 12～48小时。

Output:
选择B的理由是猩红热的临床表现通常遵循特定的时间顺序。猩红热是由A组β溶血性链球菌感染引起的，发病通常伴有高烧和咽痛。皮疹一般在发热后12到48小时内出现，这一时期对应于细菌毒素的产生和体内反应。皮疹最初出现在耳后和颈部，之后可能蔓延到身体其他部分。12小时之内（选项A）通常还未出现皮疹，而60～72小时（选项C）和大于96小时（选项D）则为猩红热的皮疹出现时间已过长，故选B 12～48小时为最佳答案。
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1 against the reference rationale.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the benchmark rationale.
### Judge Prompt
Not applicable. GPT-4 is excluded from this evaluation because the paper states that the rationale component was primarily constructed using GPT-4 outputs.
```

### 4.7 Task: MMedBench Rationale (English)

This task is to generate an explanation or step-by-step rationale for an English medical QA item when the question and answer are already given.

### Task type
Rationale Generation

```md
### Instruction
Normalized from the published task description: given an English medical question and its answer, generate an explanation or step-by-step reasoning that justifies the answer.
### Input
An English medical question together with its correct answer.
### Output
A free-form rationale or explanation.
```

### Task example

```md
### Example
Artifact-level example from official `Rationale/task52_mmedbench_explanation_english_test_only.jsonl` (not printed in the paper):

Input:
Question: Two weeks after undergoing an emergency cardiac catherization with stenting for unstable angina pectoris, a 61-year-old man has decreased urinary output and malaise. He has type 2 diabetes mellitus and osteoarthritis of the hips. Prior to admission, his medications were insulin and naproxen. He was also started on aspirin, clopidogrel, and metoprolol after the coronary intervention. His temperature is 38°C (100.4°F), pulse is 93/min, and blood pressure is 125/85 mm Hg. Examination shows mottled, reticulated purplish discoloration of the feet. Laboratory studies show:
Hemoglobin count 14 g/dL
Leukocyte count 16,400/mm3
Segmented neutrophils 56%
Eosinophils 11%
Lymphocytes 31%
Monocytes 2%
Platelet count 260,000/mm3
Erythrocyte sedimentation rate 68 mm/h
Serum
Urea nitrogen 25 mg/dL
Creatinine 4.2 mg/dL
Renal biopsy shows intravascular spindle-shaped vacuoles. Which of the following is the most likely cause of this patient's symptoms?
Options:
A: Renal papillary necrosis
B: Cholesterol embolization
C: Eosinophilic granulomatosis with polyangiitis
D: Polyarteritis nodosa
Gold answer provided in the official task file: B: Cholesterol embolization

Output:
The most likely cause of this patient's symptoms, considering the clinical presentation and laboratory findings, is B. Cholesterol embolization (also known as atheroembolism). The patient's recent history of cardiac catheterization with stenting raises the possibility of cholesterol crystal embolization, which can occur after vascular procedures. The mottled, reticulated purplish discoloration of the feet (livedo reticularis) and the renal biopsy showing intravascular spindle-shaped vacuoles are characteristic findings of cholesterol crystal embolization. The elevated ESR and eosinophilia could also be associated with this condition. While renal papillary necrosis, polyarteritis nodosa, and eosinophilic granulomatosis with polyangiitis may have similar presentations, the recent cardiac intervention and specific biopsy findings make cholesterol embolization the most likely diagnosis.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic comparison to the reference rationale.
### Judge Prompt
Not applicable.
```

### 4.8 Task: MMedBench Rationale (French)

This task is to generate an explanation or step-by-step rationale for a French medical QA item when the question and answer are already given.

### Task type
Rationale Generation

```md
### Instruction
Normalized from the published task description: given a French medical question and its answer, generate an explanation or step-by-step reasoning that justifies the answer.
### Input
A French medical question together with its correct answer.
### Output
A free-form rationale or explanation.
```

### Task example

```md
### Example
Artifact-level example from official `Rationale/task53_mmedbench_explanation_french_test_only.jsonl`:

Input:
Question: Parmi les propositions suivantes, indiquer celle qui est exacte. Dans les conditions physiologiques, le pH le plus élevé est mesuré dans:
Options: A: Le suc gastrique	B: La bile vésiculaire	C: Le suc pancréatique	D: La salive	E: Les sécrétions intestinales
La bonne réponse est C: Le suc pancréatique.

Output:
La réponse correcte est C, le suc pancréatique. Ceci s'explique par le fait que le suc pancréatique est riche en bicarbonate de sodium, une substance alcaline qui permet de neutraliser l'acidité du chyme en provenance de l'estomac lorsque celui-ci entre dans le duodénum. Son pH se situe aux alentours de 8, ce qui est nettement plus élevé que les autres sécrétions telles que le suc gastrique (pH environ 2), la bile (pH environ 7.0-8.0), la salive (pH environ 6.5-7.5) et les sécrétions intestinales (pH varie, mais est généralement inférieur à celui du suc pancréatique).
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic comparison to the reference rationale.
### Judge Prompt
Not applicable.
```

### 4.9 Task: MMedBench Rationale (Japanese)

This task is to generate an explanation or step-by-step rationale for a Japanese medical QA item when the question and answer are already given.

### Task type
Rationale Generation

```md
### Instruction
Normalized from the published task description: given a Japanese medical question and its answer, generate an explanation or step-by-step reasoning that justifies the answer.
### Input
A Japanese medical question together with its correct answer.
### Output
A free-form rationale or explanation.
```

### Task example

```md
### Example
Artifact-level example from official `Rationale/task54_mmedbench_explanation_japanese_test_only.jsonl`:

Input:
質問: 異常呼吸あるいは息切れを主訴とする患者の所見と原因の組合せについて正しいのはどれか。
オプション: A: Coarse crackles --------- 喘息	B: 胸部打診で濁音 --------- 気胸	C: 頸静脈の怒張 --------- 右心不全	D: SpO2 95％（room air）--------- 呼吸不全	E: Cheyne-Stokes呼吸 --------- 上気道閉塞
正しい答えは C: 頸静脈の怒張 --------- 右心不全 です。

Output:
C選択肢が正しい理由は、頸静脈の怒張は全身の静脈還流が増加し、特に心臓に血液が十分に送り出せない場合に観察される症状です。右心不全においては、右心室のポンプ機能が低下しているため、静脈系に血液が停滞し、頸静脈が怒張するという現象が起こります。他の選択肢が不適切な理由は、A.喘息は粗い喘鳴を伴いますが、粗いラ音（coarse crackles）ではありません。B.気胸では胸部打診で共鳴音（hyperresonance）が観られますが濁音ではない。D. SpO2 95％は軽度の低酸素状態を示していますが、この数値だけで呼吸不全と断定はできません。E. Cheyne-Stokes呼吸は心不全や脳血流動態の異常で見られますが、上気道閉塞とは直接関連しません。
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic comparison to the reference rationale.
### Judge Prompt
Not applicable.
```

### 4.10 Task: MMedBench Rationale (Russian)

This task is to generate an explanation or step-by-step rationale for a Russian medical QA item when the question and answer are already given.

### Task type
Rationale Generation

```md
### Instruction
Normalized from the published task description: given a Russian medical question and its answer, generate an explanation or step-by-step reasoning that justifies the answer.
### Input
A Russian medical question together with its correct answer.
### Output
A free-form rationale or explanation.
```

### Task example

```md
### Example
Artifact-level example from official `Rationale/task55_mmedbench_explanation_russian_test_only.jsonl`:

Input:
Вопрос: Противокашлевое действие бутамирата цитрата обусловлено главным образом воздействием на кашлевой центр в мозге?
Варианты: A: да	B: нет
Правильный ответ: A: да.

Output:
Выбор варианта A обоснован тем, что бутамират цитрат действительно воздействует на кашлевой центр в мозге. Он оказывает центральное противокашлевое действие, подавляя рефлекс кашля на уровне кашлевого центра, который находится в мозговом стволе. Таким образом, бутамират цитрат не оказывает непосредственное влияние на дыхательные пути, а воздействует на механизмы, регулирующие кашель на центральном уровне. Это делает его эффективным при лечении симптоматического кашля различного происхождения, уменьшая частоту и интенсивность кашлевых позывов.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic comparison to the reference rationale.
### Judge Prompt
Not applicable.
```

### 4.11 Task: MMedBench Rationale (Spanish)

This task is to generate an explanation or step-by-step rationale for a Spanish medical QA item when the question and answer are already given.

### Task type
Rationale Generation

```md
### Instruction
Normalized from the published task description: given a Spanish medical question and its answer, generate an explanation or step-by-step reasoning that justifies the answer.
### Input
A Spanish medical question together with its correct answer.
### Output
A free-form rationale or explanation.
```

### Task example

```md
### Example
Artifact-level example from official `Rationale/task56_mmedbench_explanation_spanish_test_only.jsonl`:

Input:
Pregunta: La formación de hueso a partir de un molde de cartílago hialino se denomina:
Opciones: A: Intramembranosa.	B: Trabecular.	C: Endocondral.	D: Aposicional.
La respuesta correcta es C: Endocondral..

Output:
La opción C, "Endocondral", es la correcta porque describe el proceso por el cual el cartílago hialino es progresivamente reemplazado por tejido óseo. Este método de osificación es característico en la formación de huesos largos, donde primero se forma un molde de cartílago y luego, en un proceso regulado por factores de crecimiento, se va calcificando y sustituyendo por hueso. Las otras opciones no corresponden con este proceso: la osificación "Intramembranosa" se da en huesos planos y no parte de cartílago, "Trabecular" se refiere a la microstructura ósea y "Aposicional" al crecimiento en superficie de hueso ya existente.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic comparison to the reference rationale.
### Judge Prompt
Not applicable.
```

## 5. MedQSum

MedQSum is used in MedS-Bench as a text summarization benchmark. Artifact-level discrepancy note: while the paper labels this constituent benchmark `MedQSum`, the official MedS-Ins construction script points to the public **MeQSum** dataset and builds each instance from Excel columns `CHQ -> Summary`. The released artifact is therefore a **consumer health question summarization** task rather than a radiology-style findings-to-impression task. The paper reports evaluation on **100 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Consumer health question understanding / summarization
- **Source Clinical Document Type:** Consumer health question
- **Clinical Specialty:** Multi-specialty consumer-health queries
- **Application Method:** Public MeQSum benchmark reformatted into a MedS-Bench summarization task
- **Split / Sample Info:** 100 randomly sampled evaluation instances.

### 5.1 Task: MedQSum / MeQSum Medical Question Summarization

This task is to summarize a long consumer health question into a short normalized question.

### Task type
Summarization

```md
### Instruction
Official construction script `data_preparing/meqsum_text_summarization.py`: You will be given a long medical question. Your task is to summarize the consumer health question.
### Input
A long consumer health question from the `CHQ` column in `MeQSum_ACL2019_BenAbacha_Demner-Fushman.xlsx`.
### Output
A short question summary from the `Summary` column.
```

### Task example

```md
### Example
Artifact-level example from official `MeQSum_ACL2019_BenAbacha_Demner-Fushman.xlsx` via `data_preparing/meqsum_text_summarization.py`:

Input:
SUBJECT: who and where to get cetirizine - D
MESSAGE: I need/want to know who manufscturs Cetirizine. My Walmart is looking for a new supply and are not getting the recent

Output:
Who manufactures cetirizine?

Gold / Reference:
The script copies the `Summary` column as the gold target. This released artifact does not match the paper's generic ultrasound-style illustrative prompt.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1 against the reference question summary.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the gold `Summary` field.
### Judge Prompt
Not applicable.
```

## 6. RCT-Text

RCT-Text is used in MedS-Bench as a medical evidence summarization benchmark. The supplement says it summarizes medical evidence from clinical studies and that the model receives study titles and abstracts and must output the primary study conclusions. The evaluation uses **100 randomly sampled** instances.

- **Language:** English (inferred)
- **Clinical Stage:** Evidence synthesis / research interpretation (inferred)
- **Source Clinical Document Type:** Study title and abstract
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark reformatted into MedS-Bench summarization task
- **Split / Sample Info:** 100 randomly sampled evaluation instances.

### 6.1 Task: RCT-Text Study Conclusion Summarization

This task is to summarize the primary conclusion of a clinical study from its title and abstract.

### Task type
Summarization

```md
### Instruction
Normalized from the published task description: given the title and abstract of a clinical study, output the study's primary conclusion.
### Input
A clinical study title and abstract.
### Output
A concise conclusion summarizing the study's main finding.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Paper supplement description only. I did not locate a released MedS-Ins preprocessing script or public task file for this constituent benchmark.

Task Construction:
Each instance pairs a study title and abstract with the study's primary conclusion.

Model Input Shape:
Title: <clinical study title>
Abstract: <clinical study abstract>

Model Output Shape:
<concise primary conclusion summarizing the study's main finding>

Gold / Reference Answer:
The benchmark stores the study conclusion text as the BLEU-1 / ROUGE-1 reference.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the reference conclusion.
### Judge Prompt
Not applicable.
```

## 7. MIMIC-CXR

MIMIC-CXR is used in MedS-Bench as a chest X-ray report summarization benchmark. The supplement describes it as a large public dataset of chest radiographs paired with radiology reports and states that the model receives textual descriptions of key X-ray findings and must summarize the pertinent findings. The evaluation uses **100 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Radiology interpretation
- **Source Clinical Document Type:** Chest radiology report
- **Clinical Specialty:** Radiology
- **Application Method:** Public benchmark reformatted into MedS-Bench summarization task
- **Split / Sample Info:** 100 randomly sampled evaluation instances.

### 7.1 Task: MIMIC-CXR X-ray Summarization

This task is to summarize the important findings from a chest X-ray description.

### Task type
Summarization

```md
### Instruction
Official construction script `data_preparing/mimic_cxr_text_summarization.py`: You will be given a description of the important aspects in the Chest X-ray image. Your task is to give a short summary of the most immediately relevant findings.
### Input
The extracted `FINDINGS:` section from a MIMIC-CXR radiology report.
### Output
The extracted `IMPRESSION:` section, i.e. a short summary of the most immediately relevant findings.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Official `data_preparing/mimic_cxr_text_summarization.py` plus source `MIMIC-CXR/cxr-study-list.csv` and the corresponding report files on PhysioNet.

Task Construction:
The script opens each listed report, keeps only reports containing both `FINDINGS:` and `IMPRESSION:`, then sets:
- input = text between `FINDINGS:` and `IMPRESSION:`
- gold output = text after `IMPRESSION:`

Model Input Shape:
FINDINGS: <free-text radiology findings>

Model Output Shape:
<short impression / most immediately relevant findings>

Gold / Reference Answer:
The original `IMPRESSION:` section of the same report.

Access Note:
The underlying MIMIC-CXR reports are hosted on credentialed PhysioNet access, so no public report row is reproduced here.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the reference summary.
### Judge Prompt
Not applicable.
```

## 8. MIMIC-IV Report

MIMIC-IV Report is a MedS-Bench summarization constituent benchmark derived from the radiology-note split of MIMIC-IV. The supplement states that impressions are treated as summaries of findings and that the authors sampled **100 cases for each covered modality and body region**, resulting in **1,430 evaluation cases** overall, although the main paper reports only three aggregated tasks: ultrasound, CT, and MRI summarization.

- **Language:** English
- **Clinical Stage:** Radiology interpretation
- **Source Clinical Document Type:** Radiology report with findings and impression
- **Clinical Specialty:** Radiology
- **Application Method:** Public benchmark reformatted into MedS-Bench summarization task family
- **Split / Sample Info:** 1,430 evaluation cases in total across covered modality / body-region combinations; the main table explicitly reports ultrasound, CT, and MRI tasks.

### 8.1 Task: MIMIC-IV Report Ultrasound Summarization

This task is to summarize the conclusion of an ultrasound radiology report from the findings section.

### Task type
Summarization

```md
### Instruction
Normalized from the published task description: given the findings in an ultrasound radiology report, generate the impression / conclusion.
### Input
An ultrasound report findings section.
### Output
An impression or concise report conclusion.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Official `data_preparing/mimic_iv_modality_anatomy_summaries.py`.

Prompt Template:
Given the detailed finding of Ultrasound imaging diagnostics, summarize the note's conclusion in a few words.

Task Construction:
The script scans `radiology.csv` from MIMIC-IV Note, keeps reports containing `EXAMINATION:`, `INDICATION:`, `FINDINGS:`, and `IMPRESSION:`, detects the modality from the `EXAMINATION:` field, and for ultrasound sets:
- input = extracted `FINDINGS:` section
- gold output = extracted `IMPRESSION:` section

Model Input Shape:
FINDINGS: <ultrasound findings text>

Model Output Shape:
<concise ultrasound impression / conclusion>

Gold / Reference Answer:
The report's `IMPRESSION:` section.

Access Note:
The underlying notes come from credentialed PhysioNet access to MIMIC-IV Note 2.2.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the impression section.
### Judge Prompt
Not applicable.
```

### 8.2 Task: MIMIC-IV Report CT Summarization

This task is to summarize the conclusion of a CT radiology report from the findings section.

### Task type
Summarization

```md
### Instruction
Normalized from the published task description: given the findings in a CT radiology report, generate the impression / conclusion.
### Input
A CT report findings section.
### Output
An impression or concise report conclusion.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Official `data_preparing/mimic_iv_modality_anatomy_summaries.py`.

Prompt Template:
Summarize the CT imaging diagnostics' detailed findings for the {anatomy} into a concise conclusion.

Task Construction:
For CT, the script first requires `EXAMINATION:`, `INDICATION:`, `FINDINGS:`, and `IMPRESSION:` in the report text. It then detects `CT` from `EXAMINATION:` and assigns the report to an anatomy bucket (`Chest`, `Head_and_neck`, `Brain`, `Abdomen`, `Pelvis`, or `Spine`). Each anatomy-specific task uses:
- input = extracted `FINDINGS:` section
- gold output = extracted `IMPRESSION:` section

Model Input Shape:
FINDINGS: <CT findings text>

Model Output Shape:
<concise CT impression / conclusion>

Gold / Reference Answer:
The report's `IMPRESSION:` section. The paper reports an aggregated CT score over these CT sub-benchmarks.

Access Note:
The underlying notes come from credentialed PhysioNet access to MIMIC-IV Note 2.2.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the impression section.
### Judge Prompt
Not applicable.
```

### 8.3 Task: MIMIC-IV Report MRI Summarization

This task is to summarize the conclusion of an MRI radiology report from the findings section.

### Task type
Summarization

```md
### Instruction
Normalized from the published task description: given the findings in an MRI radiology report, generate the impression / conclusion.
### Input
An MRI report findings section.
### Output
An impression or concise report conclusion.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Official `data_preparing/mimic_iv_modality_anatomy_summaries.py`.

Prompt Template:
Summarize the MRI imaging diagnostics' detailed findings for the {anatomy} into a concise conclusion.

Task Construction:
For MRI, the script requires the same four report sections and detects `MRI` from `EXAMINATION:`. It then assigns the note to an anatomy bucket (`Chest`, `Head_and_neck`, `Brain`, `Abdomen`, `Pelvis`, or `Spine`) and uses:
- input = extracted `FINDINGS:` section
- gold output = extracted `IMPRESSION:` section

Model Input Shape:
FINDINGS: <MRI findings text>

Model Output Shape:
<concise MRI impression / conclusion>

Gold / Reference Answer:
The report's `IMPRESSION:` section. The paper reports an aggregated MRI score over these MRI sub-benchmarks.

Access Note:
The underlying notes come from credentialed PhysioNet access to MIMIC-IV Note 2.2.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the impression section.
### Judge Prompt
Not applicable.
```

## 9. ADE Corpus

ADE Corpus is used in MedS-Bench for drug dose extraction. The supplement says the task inputs a sentence together with a mentioned drug name and asks the model to identify the dosage level of that drug. The benchmark is taken from the prompted Super-NaturalInstructions version and split `9:1`, producing **23** evaluation instances.

- **Language:** English
- **Clinical Stage:** Treatment / medication management
- **Source Clinical Document Type:** Sentence-level clinical or biomedical text
- **Clinical Specialty:** Pharmacology
- **Application Method:** Public benchmark reformatted into MedS-Bench extraction task
- **Split / Sample Info:** Prompted source reused from Super-NaturalInstructions; split 9:1; 23 test instances.

### 9.1 Task: ADE Drug Dose Extraction

This task is to extract the dosage level of a specified drug mentioned in a sentence.

### Task type
Information Extraction

```md
### Instruction
Normalized from the published task description: given a sentence and the drug mentioned in it, identify the dosage level for that drug.
### Input
A sentence plus the target drug name.
### Output
The dosage level for the specified drug.
```

### Task example

```md
### Example
Artifact-level example from official `Information_extraction/task29_drug_dose_extraction.json` (not printed in the paper):

Input:
METHODS: Growth retardation was observed in six severely asthmatic children after introduction of high-dose fluticasone propionate treatment (dry powder).
Target drug: fluticasone propionate

Output:
high
```

### Scoring standard

```md
### Scoring
Accuracy, as stated in the main paper for ADE drug dose extraction.
### Evaluation Dimensions
Deterministic comparison against the benchmark's reference dosage answer.
### Judge Prompt
Not applicable.
```

## 10. PICO

PICO is used in MedS-Bench as an information extraction benchmark with three task reformulations: participant extraction, intervention extraction, and outcome extraction. The supplement says the dataset contains 5,000 randomized controlled trial abstracts and that each of the three tasks uses the prompted Super-NaturalInstructions version with a `9:1` split and **43** test instances per task.

- **Language:** English
- **Clinical Stage:** Evidence synthesis / trial interpretation
- **Source Clinical Document Type:** Medical article abstract or study-report sentence
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark reformatted into three MedS-Bench extraction tasks
- **Split / Sample Info:** Prompted source reused from Super-NaturalInstructions; split 9:1; 43 test instances for each task.

### 10.1 Task: PICO Participant Extraction

This task is to extract phrases that describe the study participants.

### Task type
Information Extraction

```md
### Instruction
Normalized from the published task description: identify phrases in the study-report sentence that describe the participants enrolled in the study.
### Input
A sentence from a clinical trial abstract or study report.
### Output
Comma-separated participant-related phrases in the same order as they appear in the text, or `not found` if absent.
```

### Task example

```md
### Example
Artifact-level example from official `Information_extraction/task1_participant_extraction.json`:

Input:
Under Fluoxetine , mPFC activation was up-regulated and normalized in ASD boys relative to controls , but down-regulated in ADHD boys relative to placebo , which was concomitant with worse task performance in ADHD .

Output:
ASD boys, ADHD boys
```

### Scoring standard

```md
### Scoring
Accuracy, per the main paper's evaluation description for PICO extraction tasks.
### Evaluation Dimensions
Deterministic comparison to the reference extracted spans / answers.
### Judge Prompt
Not applicable.
```

### 10.2 Task: PICO Intervention Extraction

This task is to extract phrases that describe the study interventions.

### Task type
Information Extraction

```md
### Instruction
Normalized from the published task description: identify phrases in the study-report sentence that describe the study interventions.
### Input
A sentence from a clinical trial abstract or study report.
### Output
Comma-separated intervention phrases in the same order as they appear in the text, or `not found` if absent.
```

### Task example

```md
### Example
Artifact-level example from official `Information_extraction/task2_intervention_extraction.json`:

Input:
Under Fluoxetine , mPFC activation was up-regulated and normalized in ASD boys relative to controls , but down-regulated in ADHD boys relative to placebo , which was concomitant with worse task performance in ADHD .

Output:
Fluoxetine, placebo
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic comparison to the reference extracted spans / answers.
### Judge Prompt
Not applicable.
```

### 10.3 Task: PICO Outcome Extraction

This task is to extract phrases that describe the study outcomes.

### Task type
Information Extraction

```md
### Instruction
Normalized from the published task description: identify phrases in the study-report sentence that provide information about the study outcomes.
### Input
A sentence from a clinical trial abstract or study report.
### Output
Comma-separated outcome phrases in the same order as they appear in the text, or `not found` if absent.
```

### Task example

```md
### Example
Artifact-level example from official `Information_extraction/task3_outcome_extraction.json`:

Input:
Under Fluoxetine , mPFC activation was up-regulated and normalized in ASD boys relative to controls , but down-regulated in ADHD boys relative to placebo , which was concomitant with worse task performance in ADHD .

Output:
mPFC activation, task performance
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic comparison to the reference extracted spans / answers.
### Judge Prompt
Not applicable.
```

## 11. PMC-Patient

PMC-Patient is used in MedS-Bench for basic patient-information extraction. The supplement describes it as a collection of patient summaries extracted from PMC case reports and says the benchmark asks the model to extract the patient's gender and age. The evaluation uses **1,500 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Patient description extraction
- **Source Clinical Document Type:** Case report / patient summary
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark reformatted into MedS-Bench extraction task
- **Split / Sample Info:** 1,500 randomly sampled evaluation instances.

### 11.1 Task: PMC-Patient Basic Information Extraction

This task is to extract a patient's age and gender from a longer clinical text.

### Task type
Information Extraction

```md
### Instruction
Official task definition from `Information_extraction/task74_pmc_patient_case_report_basic_information_extraction.json`: Assuming you are a clinical assistant. You need to help extract out the patient gender and age information from a long clinical text. Please make your answer clear and strcturable, following the format like `Gender: ... \n\nAge: ... \n\n`.
### Input
An extended patient summary or case-report text.
### Output
The structured answer format used by the released task file:
`Gender: M|F`

`Age: "[[value, 'unit'], ...]"`
```

### Task example

```md
### Example
Artifact-level example from official `Information_extraction/task74_pmc_patient_case_report_basic_information_extraction.json`:

Input:
Secondary reconstruction with spanning plate in situ was done for the left hemi-mandible in an 18-year-old girl. A vascularised iliac crest flap was used and designed according to the template to ascertain the exact shape of the angle of the mandible [Figures and ].

Output:
Gender: F

Age: "[[18.0, 'year']]"
```

### Scoring standard

```md
### Scoring
Accuracy, as stated in the main paper's information-extraction evaluation.
### Evaluation Dimensions
Deterministic comparison to the reference demographic information.
### Judge Prompt
Not applicable.
```

## 12. PUBHEALTH / PUBLICHEALTH

This constituent benchmark appears under two inconsistent names in the paper: `PUBHEALTH` in the supplement and `PUBLICHEALTH` in Table 8. MedS-Bench uses it for both explanation generation and health-fact verification. The supplement states that the explanation task uses **1,235** test samples and the verification task uses **650** test samples.

- **Language:** English
- **Clinical Stage:** Public-health claim explanation / verification
- **Source Clinical Document Type:** Claim-evidence paragraph pair
- **Clinical Specialty:** Public health
- **Application Method:** Public benchmark reformatted into two MedS-Bench tasks
- **Split / Sample Info:** Explanation uses 1,235 test samples; verification uses 650 test samples.

### 12.1 Task: PUBHEALTH Explanation

This task is to produce an explanation for a public-health claim using the supporting material in a provided paragraph.

### Task type
Explanation Generation

```md
### Instruction
Official task definition from `Explanation/task18_test_healthfact_sentence_generation.json`: Generate an explanation for the given claim using the provided supporting material from the paragraph. The explanation should be at least one and at most twelve sentences long.
### Input
A public-health claim together with a supporting paragraph.
### Output
A free-form explanatory justification, one to twelve sentences.
```

### Task example

```md
### Example
Artifact-level example from official `Explanation/task18_test_healthfact_sentence_generation.json`:

Input:
Paragraph: Republicans are praising conservative fiscal policies and the elimination of a voter-approved surtax on the wealthy. Republican House Leader and gubernatorial candidate Ken Fredette claims Democrats are now rushing to increase state spending and grow government. Democratic House Speaker Sara Gideon says Maine’s fiscal health is only as meaningful as the health of its people at a time of an opioid epidemic and a workforce shortage. Democratic Rep. Drew Gattine says the surplus is a chance for a serious discussion about addressing issues like access to health care after voters approved Medicaid expansion in November. Maine’s Economic Forecasting Committee says it expects Republican President Trump’s federal tax reform to spur economic growth. Claim: Lawmakers consider spending, saving $128.5 million surplus.

Output:
Maine legislative leaders differ about what to do, if anything, with a projected $128.5 million surplus this year.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the reference explanation.
### Judge Prompt
Not applicable.
```

### 12.2 Task: PUBHEALTH Health Fact Verification

This task is to classify a public-health claim against the provided paragraph as contradiction, mixed evidence, or support.

### Task type
Fact Verification / Classification

```md
### Instruction
Official task definition from `Fact_verication/task16_test_healthfact_classification.json`: Given a paragraph and a claim, classify it this way: if the claim contradicts the evidence present in the paragraph, output `0`; if the claim has multiple supporting and contradicting evidences, output `1`; if the claim has supporting evidence and the paragraph is in overall favor of the claim, output `2`.
### Input
A public-health paragraph plus a related claim.
### Output
One label from the released task file: `0` = contradiction, `1` = mixed support and contradiction, `2` = supported overall.
```

### Task example

```md
### Example
Artifact-level example from official `Fact_verication/task16_test_healthfact_classification.json`:

Input:
Paragraph: Republicans are praising conservative fiscal policies and the elimination of a voter-approved surtax on the wealthy. Republican House Leader and gubernatorial candidate Ken Fredette claims Democrats are now rushing to increase state spending and grow government. Democratic House Speaker Sara Gideon says Maine’s fiscal health is only as meaningful as the health of its people at a time of an opioid epidemic and a workforce shortage. Democratic Rep. Drew Gattine says the surplus is a chance for a serious discussion about addressing issues like access to health care after voters approved Medicaid expansion in November. Maine’s Economic Forecasting Committee says it expects Republican President Trump’s federal tax reform to spur economic growth. Claim: Lawmakers consider spending, saving $128.5 million surplus.

Output:
2

Gold / Reference:
`2` means the paragraph is overall in favor of the claim.
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic verification correctness.
### Judge Prompt
Not applicable.
```

## 13. Human Disease Ontology (DO)

Human Disease Ontology is used in MedS-Bench as a concept explanation benchmark. The supplement says it provides sustainable descriptions of human disease terms and related medical vocabularies, and that the task asks the model to explain a given medical professional entity. The evaluation uses the entire test set of **1,115** instances.

- **Language:** English (inferred)
- **Clinical Stage:** Medical terminology explanation
- **Source Clinical Document Type:** Ontology concept name and description
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public ontology resource reformatted into MedS-Bench explanation task
- **Split / Sample Info:** Entire test set with 1,115 instances.

### 13.1 Task: DO Entity Explanation

This task is to explain a specified disease-ontology entity.

### Task type
Explanation Generation

```md
### Instruction
Official task definition from `Explanation/task46_do_entity_explanation.json`: Assuming you are a doctor, please explan the following given medical professional entity for me.
### Input
The name of a disease-ontology concept.
### Output
A free-form textual explanation / description of that concept.
```

### Task example

```md
### Example
Artifact-level example from official `Explanation/task46_do_entity_explanation.json`:

Input:
infiltrating ureter transitional cell carcinoma

Output:
Infiltrating urothelial carcinoma that affects the renal pelvis and ureter.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the ontology description.
### Judge Prompt
Not applicable.
```

## 14. BioLORD

BioLORD is used in MedS-Bench as a biomedical concept explanation benchmark. The supplement says it comprises biomedical concept names paired with descriptions, and the task asks the model to elaborate concise concepts into long detailed definitions. The evaluation uses the entire test set of **1,115** instances.

- **Language:** English (inferred)
- **Clinical Stage:** Biomedical concept explanation
- **Source Clinical Document Type:** Concept name and definition pair
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Public benchmark reformatted into MedS-Bench explanation task
- **Split / Sample Info:** Entire test set with 1,115 instances.

### 14.1 Task: BioLORD Concept Explanation

This task is to expand a concise biomedical concept name into a detailed definition.

### Task type
Explanation Generation

```md
### Instruction
Official task definition from `Explanation/task50_biolord_explanation.json`: Given a concise concept, generate a long detailed definition to explain it.
### Input
A biomedical concept name.
### Output
A detailed free-form definition / explanation.
```

### Task example

```md
### Example
Artifact-level example from official `Explanation/task50_biolord_explanation.json`:

Input:
Concept: L-amino-acid dehydrogenase activity (oxidoreductase activity, acting on the CH-NH2 group of donors, NAD or NADP as acceptor)

Output:
oxidoreductase activity, acting on the CH-NH2 group of donors, NAD or NADP as acceptor described as catalysis of the reaction: an L-amino acid + H2O + NAD+ = a 2-oxo acid + NH3 + NADH.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the reference definition.
### Judge Prompt
Not applicable.
```

## 15. BC4Chem

BC4Chem is a chemical named-entity-recognition constituent benchmark in MedS-Bench. The supplement says it contains 10,000 PubMed abstracts with manually annotated chemical mentions and that the evaluation uses **1,500 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Biomedical literature entity extraction
- **Source Clinical Document Type:** PubMed abstract
- **Clinical Specialty:** Biomedical chemistry
- **Application Method:** Public benchmark reformatted into MedS-Bench NER task
- **Split / Sample Info:** 1,500 randomly sampled evaluation instances.

### 15.1 Task: BC4Chem Chemical Recognition

This task is to recognize chemical names in a biomedical abstract.

### Task type
Named Entity Recognition

```md
### Instruction
Official task definition from `NER/task125_test_bc4chem_named_enetity_recognition.json`: Given a sentence, you need to reconize the name of the chemical. There might be several correct answers. If it does not exist, you need to output `There is no related enetity.`.
### Input
A PubMed abstract.
### Output
The chemical mentions as a comma-separated string, or `There is no related enetity.`.
```

### Task example

```md
### Example
Artifact-level example from official `NER/task125_test_bc4chem_named_enetity_recognition.json`:

Input:
Effects of docosahexaenoic acid and methylmercury on child ' s brain development due to consumption of fish by Finnish mother during pregnancy: a probabilistic modeling approach.

Output:
docosahexaenoic acid, methylmercury.
```

### Scoring standard

```md
### Scoring
F1 score is the metric explicitly reported in Table 6. The supplement also indicates that precision / recall / F1-family metrics are used for multi-entity tasks.
### Evaluation Dimensions
Entity-level correctness of the extracted chemical mentions.
### Judge Prompt
Not applicable.
```

## 16. BC5CDR

BC5CDR is reused in MedS-Bench as two NER tasks: chemical recognition and disease recognition. The supplement states that **1,500 randomly sampled** instances are used for each task.

- **Language:** English
- **Clinical Stage:** Biomedical literature entity extraction
- **Source Clinical Document Type:** PubMed abstract
- **Clinical Specialty:** Biomedical chemistry and disease terminology
- **Application Method:** Public benchmark reformatted into two MedS-Bench NER tasks
- **Split / Sample Info:** 1,500 randomly sampled evaluation instances for each task.

### 16.1 Task: BC5CDR Chemical Recognition

This task is to recognize chemical names in a biomedical abstract.

### Task type
Named Entity Recognition

```md
### Instruction
Official task definition from `NER/task126_test_bc5chem_named_enetity_recognition.json`: Given a sentence, you need to reconize the name of the chemical. There might be several correct answers. If it does not exist, you need to output `There is no related enetity.`.
### Input
A PubMed abstract.
### Output
The chemical mentions as a comma-separated string, or `There is no related enetity.`.
```

### Task example

```md
### Example
Artifact-level example from official `NER/task126_test_bc5chem_named_enetity_recognition.json`:

Input:
Torsade de pointes ventricular tachycardia during low dose intermittent dobutamine treatment in a patient with dilated cardiomyopathy and congestive heart failure.

Output:
dobutamine.
```

### Scoring standard

```md
### Scoring
F1 score as reported in Table 6.
### Evaluation Dimensions
Entity-level correctness of extracted chemical mentions.
### Judge Prompt
Not applicable.
```

### 16.2 Task: BC5CDR Disease Recognition

This task is to recognize disease names in a biomedical abstract.

### Task type
Named Entity Recognition

```md
### Instruction
Official task definition from `NER/task127_test_bc5disease_named_enetity_recognition.json`: Given a sentence, you need to reconize the name of the disease. There might be several correct answers. If it does not exist, you need to output `There is no related enetity.`.
### Input
A PubMed abstract.
### Output
The disease mentions as a comma-separated string, or `There is no related enetity.`.
```

### Task example

```md
### Example
Artifact-level example from official `NER/task127_test_bc5disease_named_enetity_recognition.json`:

Input:
Torsade de pointes ventricular tachycardia during low dose intermittent dobutamine treatment in a patient with dilated cardiomyopathy and congestive heart failure.

Output:
Torsade de pointes, ventricular tachycardia, dilated cardiomyopathy, congestive heart failure.
```

### Scoring standard

```md
### Scoring
F1 score as reported in Table 6.
### Evaluation Dimensions
Entity-level correctness of extracted disease mentions.
### Judge Prompt
Not applicable.
```

## 17. Species800

Species800 is used in MedS-Bench as an organism-recognition benchmark. The supplement says it contains 800 PubMed abstracts with organism mentions and that the evaluation uses **1,500 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Biomedical literature entity extraction
- **Source Clinical Document Type:** PubMed abstract
- **Clinical Specialty:** Biomedical organism terminology
- **Application Method:** Public benchmark reformatted into MedS-Bench NER task
- **Split / Sample Info:** 1,500 randomly sampled evaluation instances.

### 17.1 Task: Species800 Organism Recognition

This task is to recognize organism mentions in a biomedical abstract.

### Task type
Named Entity Recognition

```md
### Instruction
Official task definition from `NER/task128_test_species800_named_enetity_recognition.json`: Given a sentence, you need to reconize the name of the organism. There might be several correct answers. If it does not exist, you need to output `There is no related enetity.`.
### Input
A PubMed abstract.
### Output
The organism mentions as a comma-separated string, or `There is no related enetity.`.
```

### Task example

```md
### Example
Artifact-level example from official `NER/task128_test_species800_named_enetity_recognition.json`:

Input:
Streptococcus ursoris sp. nov., isolated from the oral cavities of bears.

Output:
Streptococcus ursoris sp . nov ..
```

### Scoring standard

```md
### Scoring
F1 score as reported in Table 6.
### Evaluation Dimensions
Entity-level correctness of extracted organism mentions.
### Judge Prompt
Not applicable.
```

## 18. DDXPlus

DDXPlus is the diagnosis constituent benchmark in MedS-Bench. The supplement describes it as a large-scale dataset for automatic symptom detection and automatic diagnosis using synthesized patient data and says the evaluation uses **1,500 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Diagnosis
- **Source Clinical Document Type:** Patient dialogue / symptom description
- **Clinical Specialty:** Differential diagnosis / multi-specialty
- **Application Method:** Public benchmark reformatted into MedS-Bench diagnosis task
- **Split / Sample Info:** 1,500 randomly sampled evaluation instances.

### 18.1 Task: DDXPlus Diagnosis

This task is to choose the correct diagnosis from a provided list based on patient dialogue or context.

### Task type
Diagnosis / Classification

```md
### Instruction
Normalized from the published task description: given a patient dialogue or symptom description together with a list of candidate diagnoses, select the most appropriate diagnosis.
### Input
A patient-context dialogue or symptom description plus candidate diagnoses.
### Output
One selected diagnosis from the provided list.
```

### Task example

```md
### Example
Artifact-level example from official `Diagnosis/task130_DDXPlus_text_classification_test.json` (not printed in the paper):

Input:
Age: 49
Sex: F
Initial evidence: Do you have a cough? Yes
Evidence: Do you have pain somewhere, related to your reason for consulting? Yes; Characterize your pain: Haunting; Characterize your pain: Sensitive; Characterize your pain: Tugging; Characterize your pain: Burning; Do you feel pain somewhere? Lower chest; Do you feel pain somewhere? Upper chest; Do you feel pain somewhere? Hypochondrium(r); How intense is the pain? 6; Does the pain radiate to another location? Lower chest; Does the pain radiate to another location? Upper chest; How precisely is the pain located? 3; How fast did the pain appear? 2; Are you significantly overweight compared to people of the same height as you? Yes; Do you drink alcohol excessively or do you have an addiction to alcohol? Yes; Do you have a hiatal hernia? Yes; Have you recently had stools that were black (like coal)? Yes; Do you think you are pregnant or are you currently pregnant? Yes; Do you have a burning sensation that starts in your stomach then goes up into your throat, and can be associated with a bitter taste in your mouth? Yes; Do you have a cough? Yes; Have you traveled out of the country in the last 4 weeks? N; Are your symptoms worse when lying down and alleviated while sitting up? Yes.

Output:
The diagnosis result is Bronchitis.
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic comparison to the gold diagnosis label.
### Judge Prompt
Not applicable.
```

## 19. SEER

SEER is used in MedS-Bench as the treatment-planning benchmark. The supplement says it leverages SEER custom breast-cancer databases with patient records and high-level treatment-plan categories, and that the evaluation uses **1,500 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Treatment planning
- **Source Clinical Document Type:** Structured patient record serialized for prediction (inferred)
- **Clinical Specialty:** Oncology / breast cancer
- **Application Method:** Public benchmark reformatted into MedS-Bench treatment-planning task
- **Split / Sample Info:** 1,500 randomly sampled evaluation instances.

### 19.1 Task: SEER Treatment Planning

This task is to recommend the best treatment decision from a fixed closed set.

### Task type
Treatment Planning / Classification

```md
### Instruction
Normalized from the published task description: given the patient record, select the most appropriate treatment recommendation from the available high-level treatment categories.
### Input
A patient record with attributes relevant to breast-cancer treatment planning.
### Output
One selected treatment category from the benchmark's closed set.
```

### Task example

```md
### Example
Artifact-level example from official `Treatment_planning/task131_SEER_text_classification_test.json` (not printed in the paper):

Input:
Age at diagnosis: 73
Regional nodes positive (1988+): 0
Total number of in situ/malignant tumors for patient: 1
Radiation recode: None/Unknown
Chemotherapy recode: No/Unknown
ER Status Recode Breast Cancer (1990+): Positive
PR Status Recode Breast Cancer (1990+): Negative
CS tumor size (2004-2015): 16
Derived HER2 Recode (2010+): Negative
Regional nodes examined (1988+): 8
COD to site recode: Diseases of Heart
Race recode: White
Sex: Female
Vital status recode (study cutoff used): Dead
Diagnosis_year: 2010
Last_fu _year: 2015
interva_years: 5

Output:
The treatment planning is: No radiation and/or cancer-directed surgery
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic comparison to the gold treatment category.
### Judge Prompt
Not applicable.
```

## 20. MIMIC4ED Benchmark

MIMIC4ED Benchmark is the MedS-Bench constituent benchmark for emergency-department clinical outcome prediction. The supplement states that the benchmark is derived from MIMIC-IV-ED and is split into three tasks: hospitalization, 72-hour ED revisit, and critical triage. Each task uses **1,500 randomly sampled** instances.

- **Language:** English
- **Clinical Stage:** Emergency-department outcome prediction
- **Source Clinical Document Type:** EHR record
- **Clinical Specialty:** Emergency medicine
- **Application Method:** Public benchmark reformatted into three MedS-Bench outcome-prediction tasks
- **Split / Sample Info:** 1,500 randomly sampled evaluation instances for each task.

### 20.1 Task: MIMIC4ED Hospitalization Prediction

This task is to predict whether the patient needs hospitalization.

### Task type
Clinical Outcome Prediction / Classification

```md
### Instruction
Normalized from the published task description: given a patient's EHR, predict whether the patient needs hospitalization.
### Input
An EHR for an emergency-department patient.
### Output
A binary hospitalization decision.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Official `data_preparing/mimic4ed_hospitalization_prediction.py` from MedS-Ins plus the public `mimic4ed-benchmark` workflow repository.

Task Construction:
The script reads `master_dataset.csv`, serializes the patient EHR as newline-separated `key: value` pairs, and uses `outcome_hospitalization` as the gold label.

Model Input Shape:
The official script uses these exact input fields in order:
`age`, `gender`, `n_ed_30d`, `n_ed_90d`, `n_ed_365d`, `n_hosp_30d`, `n_hosp_90d`, `n_hosp_365d`, `n_icu_30d`, `n_icu_90d`, `n_icu_365d`, `triage_temperature`, `triage_heartrate`, `triage_resprate`, `triage_o2sat`, `triage_sbp`, `triage_dbp`, `triage_pain`, `triage_acuity`, `chiefcom_chest_pain`, `chiefcom_abdominal_pain`, `chiefcom_headache`, `chiefcom_shortness_of_breath`, `chiefcom_back_pain`, `chiefcom_cough`, `chiefcom_nausea_vomiting`, `chiefcom_fever_chills`, `chiefcom_syncope`, `chiefcom_dizziness`, `cci_MI`, `cci_CHF`, `cci_PVD`, `cci_Stroke`, `cci_Dementia`, `cci_Pulmonary`, `cci_Rheumatic`, `cci_PUD`, `cci_Liver1`, `cci_DM1`, `cci_DM2`, `cci_Paralysis`, `cci_Renal`, `cci_Cancer1`, `cci_Liver2`, `cci_Cancer2`, `cci_HIV`, `eci_Arrhythmia`, `eci_Valvular`, `eci_PHTN`, `eci_HTN1`, `eci_HTN2`, `eci_NeuroOther`, `eci_Hypothyroid`, `eci_Lymphoma`, `eci_Coagulopathy`, `eci_Obesity`, `eci_WeightLoss`, `eci_FluidsLytes`, `eci_BloodLoss`, `eci_Anemia`, `eci_Alcohol`, `eci_Drugs`, `eci_Psychoses`, `eci_Depression`

Model Output Shape:
The raw `outcome_hospitalization` value from `master_dataset.csv`. The instruction text says the answer should be `True` or `False`.

Gold / Reference Answer:
`outcome_hospitalization`

Access Note:
The public workflow repo requires local copies of credentialed PhysioNet datasets `MIMIC-IV` and `MIMIC-IV-ED` to build `master_dataset.csv`, so no public patient row is reproduced here.
```

### Scoring standard

```md
### Scoring
Accuracy is the metric explicitly reported in Table 7 for MedS-Bench. The supplement notes that binary classification metrics such as accuracy / precision / recall / F1 are relevant in general, but the result table reports accuracy only.
### Evaluation Dimensions
Deterministic comparison to the reference binary outcome.
### Judge Prompt
Not applicable.
```

### 20.2 Task: MIMIC4ED 72-hour ED Revisit Prediction

This task is to predict whether the patient may revisit the emergency department within 72 hours.

### Task type
Clinical Outcome Prediction / Classification

```md
### Instruction
Normalized from the published task description: given a patient's EHR, predict whether the patient will revisit the emergency department within 72 hours.
### Input
An EHR for an emergency-department patient.
### Output
A binary 72-hour revisit decision.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Official `data_preparing/mimic4ed_72h_ed_revisit_disposition.py` from MedS-Ins plus the public `mimic4ed-benchmark` workflow repository.

Task Construction:
The script reads `master_dataset.csv`, serializes the patient EHR as newline-separated `key: value` pairs, and uses `outcome_ed_revisit_3d` as the gold label.

Model Input Shape:
The official script uses these exact input fields in order:
`age`, `gender`, `n_ed_30d`, `n_ed_90d`, `n_ed_365d`, `n_hosp_30d`, `n_hosp_90d`, `n_hosp_365d`, `n_icu_30d`, `n_icu_90d`, `n_icu_365d`, `triage_pain`, `triage_acuity`, `chiefcom_chest_pain`, `chiefcom_abdominal_pain`, `chiefcom_headache`, `chiefcom_shortness_of_breath`, `chiefcom_back_pain`, `chiefcom_cough`, `chiefcom_nausea_vomiting`, `chiefcom_fever_chills`, `chiefcom_syncope`, `chiefcom_dizziness`, `cci_MI`, `cci_CHF`, `cci_PVD`, `cci_Stroke`, `cci_Dementia`, `cci_Pulmonary`, `cci_Rheumatic`, `cci_PUD`, `cci_Liver1`, `cci_DM1`, `cci_DM2`, `cci_Paralysis`, `cci_Renal`, `cci_Cancer1`, `cci_Liver2`, `cci_Cancer2`, `cci_HIV`, `eci_Arrhythmia`, `eci_Valvular`, `eci_PHTN`, `eci_HTN1`, `eci_HTN2`, `eci_NeuroOther`, `eci_Hypothyroid`, `eci_Lymphoma`, `eci_Coagulopathy`, `eci_Obesity`, `eci_WeightLoss`, `eci_FluidsLytes`, `eci_BloodLoss`, `eci_Anemia`, `eci_Alcohol`, `eci_Drugs`, `eci_Psychoses`, `eci_Depression`, `ed_temperature_last`, `ed_heartrate_last`, `ed_resprate_last`, `ed_o2sat_last`, `ed_sbp_last`, `ed_dbp_last`, `ed_los`, `n_med`, `n_medrecon`

Model Output Shape:
The raw `outcome_ed_revisit_3d` value from `master_dataset.csv`.

Gold / Reference Answer:
`outcome_ed_revisit_3d`

Access Note:
The public workflow repo requires local copies of credentialed PhysioNet datasets `MIMIC-IV` and `MIMIC-IV-ED` to build `master_dataset.csv`, so no public patient row is reproduced here.
```

### Scoring standard

```md
### Scoring
Accuracy in the reported MedS-Bench results.
### Evaluation Dimensions
Deterministic comparison to the reference binary outcome.
### Judge Prompt
Not applicable.
```

### 20.3 Task: MIMIC4ED Critical Triage Prediction

This task is to predict whether the patient should be placed into a critical triage queue.

### Task type
Clinical Outcome Prediction / Classification

```md
### Instruction
Normalized from the published task description: given a patient's EHR, predict whether the patient should be classified into a critical triage queue.
### Input
An EHR for an emergency-department patient.
### Output
A binary critical-triage decision.
```

### Task example

```md
### Example
Source Dataset / Artifact:
Official `data_preparing/mimic4ed_critical_triage_prediction.py` from MedS-Ins plus the public `mimic4ed-benchmark` workflow repository.

Task Construction:
The script reads `master_dataset.csv`, serializes the patient EHR as newline-separated `key: value` pairs, and uses `outcome_critical` as the gold label.

Model Input Shape:
The official script uses these exact input fields in order:
`age`, `gender`, `n_ed_30d`, `n_ed_90d`, `n_ed_365d`, `n_hosp_30d`, `n_hosp_90d`, `n_hosp_365d`, `n_icu_30d`, `n_icu_90d`, `n_icu_365d`, `triage_temperature`, `triage_heartrate`, `triage_resprate`, `triage_o2sat`, `triage_sbp`, `triage_dbp`, `triage_pain`, `triage_acuity`, `chiefcom_chest_pain`, `chiefcom_abdominal_pain`, `chiefcom_headache`, `chiefcom_shortness_of_breath`, `chiefcom_back_pain`, `chiefcom_cough`, `chiefcom_nausea_vomiting`, `chiefcom_fever_chills`, `chiefcom_syncope`, `chiefcom_dizziness`, `cci_MI`, `cci_CHF`, `cci_PVD`, `cci_Stroke`, `cci_Dementia`, `cci_Pulmonary`, `cci_Rheumatic`, `cci_PUD`, `cci_Liver1`, `cci_DM1`, `cci_DM2`, `cci_Paralysis`, `cci_Renal`, `cci_Cancer1`, `cci_Liver2`, `cci_Cancer2`, `cci_HIV`, `eci_Arrhythmia`, `eci_Valvular`, `eci_PHTN`, `eci_HTN1`, `eci_HTN2`, `eci_NeuroOther`, `eci_Hypothyroid`, `eci_Lymphoma`, `eci_Coagulopathy`, `eci_Obesity`, `eci_WeightLoss`, `eci_FluidsLytes`, `eci_BloodLoss`, `eci_Anemia`, `eci_Alcohol`, `eci_Drugs`, `eci_Psychoses`, `eci_Depression`

Model Output Shape:
The raw `outcome_critical` value from `master_dataset.csv`.

Gold / Reference Answer:
`outcome_critical`

Access Note:
The public workflow repo requires local copies of credentialed PhysioNet datasets `MIMIC-IV` and `MIMIC-IV-ED` to build `master_dataset.csv`, so no public patient row is reproduced here.
```

### Scoring standard

```md
### Scoring
Accuracy in the reported MedS-Bench results.
### Evaluation Dimensions
Deterministic comparison to the reference binary outcome.
### Judge Prompt
Not applicable.
```

## 21. HoC

HoC is used in MedS-Bench as the text-classification benchmark. The supplement says it contains 1,852 PubMed publication abstracts annotated to 10 hallmarks of cancer and that the benchmark uses the entire test set of **158** instances.

- **Language:** English
- **Clinical Stage:** Biomedical literature classification
- **Source Clinical Document Type:** PubMed abstract
- **Clinical Specialty:** Oncology
- **Application Method:** Public benchmark reformatted into MedS-Bench multi-label classification task
- **Split / Sample Info:** Entire test set with 158 instances.

### 21.1 Task: HoC Hallmarks-of-Cancer Classification

This task is to assign one or more hallmark-of-cancer labels to a biomedical abstract.

### Task type
Multi-label Text Classification

```md
### Instruction
Normalized from the published task description: given a PubMed abstract and the list of candidate hallmark-of-cancer labels, select all labels supported by the abstract.
### Input
A biomedical abstract plus the candidate label list.
### Output
One or more selected hallmark labels.
```

### Task example

```md
### Example
Artifact-level example from official `Text_classification/task106_hoc_text_classification.json` (not printed in the paper):

Input:
MicroRNAs (miRNAs) are involved in cancer development and progression, acting as tumor suppressors or oncogenes. In this study, miRNA profiling was performed on 10 paired bladder cancer (BC) tissues using GeneChip miRNA Array, and 10 differentially expressed miRNAs were identified in BC and adjacent noncancerous tissues. After validation on an expanded cohort of 67 paired BC tissues and 10 human BC cell lines by qRT-PCR, it was found that miR-100 was down-regulated most significantly in cancer tissues. Ectopic restoration of miR-100 expression in BC cells suppressed cell proliferation and motility, induced cell-cycle arrest in vitro, and inhibited tumorigenesis in vivo. Bioinformatic analysis showed that mTOR was a direct target of miR-100, and siRNA-mediated mTOR knockdown phenocopied the effect of miR-100 in BC cell lines. The metastatic nude-mouse model also suggested that miR-100/mTOR regulated cell motility and was associated with tumor metastasis.

Output:
Sustaining proliferative signaling, Evading growth suppressors, Activating invasion and metastasis
```

### Scoring standard

```md
### Scoring
Macro-Precision, macro-Recall, and macro-F1, exactly as reported in Table 7.
### Evaluation Dimensions
Deterministic label-set comparison after the model selects zero or more candidate labels.
### Judge Prompt
Not applicable.
```

## 22. EBMS

EBMS is used in MedS-Bench as a fact-verification benchmark for justification verification. The paper itself is sparse, but the official MedS-Ins preprocessing script links this benchmark to **EBMSummariserCorpus** (`ClinicalInquiries.xml`): each answer snippet (`sniptext`) becomes an input statement and each associated long-form evidence span (`longtext`) becomes the gold justification. The evaluation uses the entire test set of **304** instances.

- **Language:** English (inferred from the released source artifact)
- **Clinical Stage:** Evidence justification / verification
- **Source Clinical Document Type:** Clinical inquiry snippets and supporting evidence spans
- **Clinical Specialty:** Multi-specialty evidence-based medicine
- **Application Method:** EBMSummariserCorpus reformatted into a free-form justification-generation task
- **Split / Sample Info:** Entire test set with 304 instances.

### 22.1 Task: EBMS Justification Verification

This task is to generate a justification-verification output for the EBMS benchmark.

### Task type
Fact Verification / Free-form Generation

```md
### Instruction
Official task definition from `Fact_verication/task100_ebms_answer_vertification.json`: Provide a justification or evidence to support a given statement.
### Input
A statement extracted from an EBMS answer snippet (`sniptext`).
### Output
A free-form justification / evidence span (`longtext`).
```

### Task example

```md
### Example
Artifact-level example from official `Fact_verication/task100_ebms_answer_vertification.json`:

Input:
Multiple randomized controlled trials (RCTs) demonstrate the effectiveness of both allergen immunotherapy and antihistamines, with or without nasal steroids, in the treatment of seasonal allergic rhinitis.

Output:
For patients requiring medication, studies comparing antihistamines with nasal corticosteroids have documented the superiority of intranasal steroids for symptom control of allergic rhinitis.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1, as stated for EBMS in the fact-verification section.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the reference free-form output.
### Judge Prompt
Not applicable.
```

## 23. MedNLI

MedNLI is used in MedS-Bench as the natural-language-inference constituent benchmark. The supplement says the authors divide it into two tasks: a discriminative entailment task and a generative entailment task. Each uses the entire test set of **1,422** instances.

- **Language:** English
- **Clinical Stage:** Clinical inference from patient history
- **Source Clinical Document Type:** Clinical premise / hypothesis pair grounded in patient medical histories
- **Clinical Specialty:** Clinical text reasoning / multi-specialty
- **Application Method:** Public benchmark reformatted into two MedS-Bench NLI tasks
- **Split / Sample Info:** Entire test set with 1,422 instances for each task.

### 23.1 Task: MedNLI Entailment (Discriminative)

This task is to decide whether a clinical hypothesis is entailed by a clinical premise.

### Task type
Natural Language Inference / Classification

```md
### Instruction
Official MedS-Ins construction script `data_preparing/mednli_textual_entailment_generator.py`: In medical, a practical task is to perform textual inference. You will be presented with a formal clinical premise statement and a hypothesis statement formatted as `Sentence1: ...\n\nSentence2: ...`. Choose one: `entailment`, `contradiction`, or `neutral`.
### Input
A clinical premise plus a hypothesis statement.
### Output
One label from the released task definition: `entailment`, `contradiction`, or `neutral`.
```

### Task example

```md
### Example
Artifact-level example from the official MedNLI description on PhysioNet and the released MedS-Ins construction script:

Input:
Sentence1: Labs were notable for Cr 1.7 (baseline 0.5 per old records) and lactate 2.4.

Sentence2: Patient has elevated Cr

Output:
Entailment

Gold / Reference:
The official MedNLI sample record labels this pair as `entailment`.
```

### Scoring standard

```md
### Scoring
Accuracy.
### Evaluation Dimensions
Deterministic comparison to the gold entailment label.
### Judge Prompt
Not applicable.
```

### 23.2 Task: MedNLI Entailment (Generative)

This task is to generate a coherent hypothesis statement from a formal clinical premise.

### Task type
Natural Language Inference / Generation

```md
### Instruction
Official MedS-Ins construction script `data_preparing/mednli_textual_entailment_generator.py`: Your task is to perform textual entailment. You will be presented with a formal clinical premise statement and must write a hypothesis statement based on it.
### Input
A formal clinical premise (`sentence1`). The released MedS-Ins script keeps only source pairs whose original `gold_label` is `entailment`.
### Output
The gold entailment hypothesis (`sentence2`) rewritten as the reference generation target.
```

### Task example

```md
### Example
Artifact-level generative example reconstructed directly from the official MedS-Ins construction rule and the official MedNLI sample record:

Input:
Labs were notable for Cr 1.7 (baseline 0.5 per old records) and lactate 2.4.

Output:
Patient has elevated Cr.

Gold / Reference:
The generative MedS-Bench task takes the original MedNLI entailment pair, drops `sentence2` from the prompt, and uses that same `sentence2` as the BLEU / ROUGE reference.
```

### Scoring standard

```md
### Scoring
BLEU-1 and ROUGE-1.
### Evaluation Dimensions
Deterministic lexical-overlap comparison with the reference hypothesis.
### Judge Prompt
Not applicable.
```
