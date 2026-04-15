<!-- paper_key: "2023_promptcblue_a_chinese_prompt_tuning_benchmark_for_the_medical_domain" -->
<!-- paper_url: "https://arxiv.org/abs/2310.14151" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *PromptCBLUE: A Chinese Prompt Tuning Benchmark for the Medical Domain*

Source paper: [https://arxiv.org/abs/2310.14151](https://arxiv.org/abs/2310.14151)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2023_promptcblue_a_chinese_prompt_tuning_benchmark_for_the_medical_domain/source.pdf`](../papers/2023_promptcblue_a_chinese_prompt_tuning_benchmark_for_the_medical_domain/source.pdf)
- Extracted text: [`../papers/2023_promptcblue_a_chinese_prompt_tuning_benchmark_for_the_medical_domain/source.txt`](../papers/2023_promptcblue_a_chinese_prompt_tuning_benchmark_for_the_medical_domain/source.txt)
- Ownership constraint: this run updates only the summary file. The registry is intentionally not edited.
- Normalization choice: `PromptCBLUE` is treated as a paper-level umbrella evaluation. Each named PromptCBLUE sub-benchmark / dataset row from Appendix Table 8 is represented as its own constituent benchmark section below, even when several rows come from the same broader source family.
- Normalization choice: benchmark sections describe the PromptCBLUE prompt-tuned reformulation used in this paper, not only the original pre-LLM CBLUE formulation. When the paper explicitly discards or simplifies part of the original task pipeline, that change is documented in the task section.
- Verification note: Appendix A.1 provides one explicit prompt/target example for every sub-task. Those examples are retained below in compact normalized form rather than marked unavailable.
- Verification note: evaluation is deterministic and post-processing based. The paper does not use LLM-as-a-judge evaluation, so every `Judge Prompt` field is marked not applicable.

## Verifier Notes

- Verified the umbrella benchmark scope against Section 3.2 and Appendix Table 8: PromptCBLUE contains 16 constituent sub-benchmarks across five task cohorts, with 82,600 training prompt-response pairs, 7,656 development pairs, and 7,656 test pairs.
- Verified prompt construction, prompt-template review, split sampling, and quality-control claims against Section 3.2.
- Verified metric-family assignments against Section 4.1.
- Verified every task instruction/output/example block against Appendix A.1.
- No judge prompt is available because the paper evaluates generations with regex-based post-processing and deterministic metrics rather than an LLM judge.

## Paper-Level Umbrella Evaluation

PromptCBLUE is a Chinese medical prompt-tuning benchmark introduced by the paper as a prompt-based re-build of the earlier CBLUE benchmark for evaluating Chinese LLMs on biomedical and clinical language understanding tasks. The umbrella benchmark covers **16 constituent sub-benchmarks** grouped into **5 task cohorts**: medical information extraction, medical text classification, medical natural language inference, symptom-status understanding for medical dialogue, and medical content/dialogue generation. The benchmark is explicitly designed for instruction-following evaluation and online leaderboard use rather than only for encoder-style classification.

The paper states that PromptCBLUE converts all CBLUE tasks into instruction-following generation format with a common sample schema containing `input`, `target`, `answer_choices`, `sample_id`, `task_type`, and `task_dataset`. Prompt templates are collected by combining human-written seed prompts with ChatGPT paraphrases and then reviewing them with a panel including medical experts and an NLP researcher. The test ground truths are kept off the public corpus and the benchmark is hosted on the Tianchi platform for evaluation and leaderboard presentation.

- **Language coverage:** Chinese.
- **Constituent sub-benchmark count:** 16.
- **Task cohorts:** medical information extraction, medical text classification, medical natural language inference, symptom status understanding for medical dialogue, medical content/dialogue generation.
- **Total PromptCBLUE size:** 82,600 train / 7,656 dev / 7,656 test prompt-response pairs.
- **Sampling rule:** the paper states that some original CBLUE tasks become very large after prompt filling, so PromptCBLUE caps most tasks at roughly 3,000 to 5,000 training samples and 600 to 800 dev/test samples by uniformly sampling prompt-response pairs from prompt-filled pools.
- **Data quality note:** 5% or 200 samples per task were manually checked by medical annotators, with an average reported mislabeling rate of 0.9%.
- **Benchmark-wide metric rule:** strict instance-level micro-F1 for information extraction tasks plus `IMCS-V2-SR` and `CHIP-MDCFNPC`; macro-F1 for text classification plus `IMCS-V2-DAC`; micro-F1 for natural language inference tasks; ROUGE-L for generation tasks.
- **Judge prompt availability:** not applicable; the paper does not use an LLM judge.

## Benchmark Inventory

| Dataset / Sub-benchmark | Task cohort | Train / Dev / Test | Avg prompt length | Avg target length | PromptCBLUE role |
| --- | --- | --- | --- | --- | --- |
| CMeEE-V2 | Medical information extraction | 5000 / 400 / 400 | 107.88 | 54.03 | Reused CBLUE task reformulated into prompted generation |
| CMeIE | Medical information extraction | 5000 / 400 / 400 | 293.72 | 135.51 | Reused CBLUE task reformulated into prompted generation |
| CHIP-CDEE | Medical information extraction | 3000 / 400 / 400 | 142.61 | 180.93 | Reused CBLUE task reformulated into prompted generation |
| CHIP-CDN | Medical information extraction / normalization | 5000 / 400 / 400 | 281.79 | 10.37 | Reused CBLUE task reformulated into prompted ranking/generation |
| CHIP-CTC | Medical text classification | 6600 / 704 / 704 | 214.61 | 3.81 | Reused CBLUE task reformulated into prompted classification |
| CHIP-STS | Medical natural language inference | 5000 / 400 / 400 | 66.26 | 2.00 | Reused CBLUE task reformulated into prompted semantic matching |
| KUAKE-QIC | Medical text classification | 5500 / 440 / 440 | 81.58 | 4.09 | Reused CBLUE task reformulated into prompted intent classification |
| KUAKE-QTR | Medical natural language inference | 5000 / 400 / 400 | 96.38 | 7.23 | Reused CBLUE task reformulated into prompted relevance grading |
| KUAKE-QQR | Medical natural language inference | 5000 / 400 / 400 | 89.38 | 7.61 | Reused CBLUE task reformulated into prompted semantic relation labeling |
| KUAKE-IR | Medical natural language inference | 5000 / 400 / 400 | 203.33 | 2.78 | Reused CBLUE task reformulated into prompted relevance judgment |
| CHIP-MDCFNPC | Symptom status understanding | 5000 / 400 / 400 | 744.99 | 67.67 | Reused CBLUE task reformulated into prompted dialogue extraction |
| IMCS-V2-SR | Symptom status understanding | 5000 / 400 / 400 | 137.13 | 36.33 | Reused CBLUE task reformulated into prompted dialogue extraction |
| IMCS-V2-NER | Medical information extraction | 5000 / 400 / 400 | 61.66 | 23.65 | Reused CBLUE task reformulated into prompted dialogue NER |
| IMCS-V2-DAC | Medical text classification | 5000 / 512 / 512 | 371.62 | 8.56 | Reused CBLUE task reformulated into prompted dialogue intent classification |
| IMCS-V2-MRG | Medical content generation | 3000 / 400 / 400 | 821.10 | 105.08 | Reused CBLUE task reformulated into prompted report generation |
| MedDG | Medical content generation | 5000 / 400 / 400 | 194.75 | 27.71 | Reused MedDG task reformulated into prompted doctor-response generation |

## 1. CMeEE-V2

CMeEE-V2 is a Chinese medical named entity extraction benchmark reused from CBLUE and reformulated here as an instruction-following generation task. Under PromptCBLUE, the task no longer asks the model to predict span indices; instead, the model must generate all entity mentions under the requested medical entity types for the input sentence.

- **Language:** Chinese.
- **Clinical Stage:** Not explicitly stated; general clinical language understanding.
- **Source Clinical Document Type:** Sentence-level medical text snippets (not explicitly stated).
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted generation and online evaluation.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 107.88; average target length 54.03.

## 1.1 Task: CMeEE-V2

This task is to extract all medical named entities of the requested types from a Chinese medical sentence and return the entity mentions grouped by entity type.

### Task type
Extraction

```md
### Instruction
医学实体识别：[sentence]
实体选项：[entity_types]
答：
Normalized English gloss: identify all medical named entities in the sentence and list the entity mentions for each requested entity type.
### Input
A Chinese medical sentence plus a provided list of entity types to consider.
### Output
A generated list of entity mentions grouped by type, explicitly returning `无` / `None` when no entity of a requested type is present.
```

### Task example

```md
### Example
Example prompt sentence: `外周血白细胞计数常明显升高，伴核左移。`
Requested entity types include diseases, medical test items, hospital departments, body parts, microorganisms, clinical manifestations, and drugs.
Example target: `医学检验项目实体: 外周血白细胞计数`; all other requested types are `无`.
```

### Scoring standard

```md
### Scoring
Instance-level strict micro-F1. A prediction is correct only when the entity mention and its entity type are both correct after post-processing the generated text back into structured instances.
### Evaluation Dimensions
Exact entity mention extraction and exact entity-type assignment.
### Judge Prompt
Not applicable. The paper uses deterministic post-processing and strict micro-F1 rather than an LLM judge.
```

## 2. CMeIE

CMeIE is a Chinese medical triple extraction benchmark reused from CBLUE and reformulated here as prompted generation. PromptCBLUE changes the task from structured triple prediction to generation of head-tail entity pairs under given relation types.

- **Language:** Chinese.
- **Clinical Stage:** Not explicitly stated; general biomedical relation extraction.
- **Source Clinical Document Type:** Sentence-level biomedical / medical text snippets (not explicitly stated).
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted generation.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 293.72; average target length 135.51.

## 2.1 Task: CMeIE

This task is to extract head-tail entity pairs that instantiate requested medical relation types in a Chinese sentence.

### Task type
Extraction

```md
### Instruction
找出句子中的具有[relations]的头尾实体对：[sentence]
Normalized English gloss: find all entity pairs in the sentence that express the requested relation types.
### Input
A Chinese medical sentence plus one or more candidate relation names.
### Output
For each requested relation type, a generated list of head entity and tail entity pairs, or `无` / `None` when no such relation appears.
```

### Task example

```md
### Example
Example prompt sentence concerns `妊娠期高血压` and requests `临床表现` and `同义词` relations.
Example target:
- `临床表现`: `头实体：妊娠期高血压，尾实体：SVR较低`; `头实体：妊娠期高血压，尾实体：心输出量往往会增加`
- `同义词`: `无`
```

### Scoring standard

```md
### Scoring
Instance-level strict micro-F1 over extracted structured relation instances after post-processing the generated text.
### Evaluation Dimensions
Exact correctness of head entity, tail entity, and relation type for each extracted instance.
### Judge Prompt
Not applicable. The paper uses deterministic post-processing and strict micro-F1 rather than an LLM judge.
```

## 3. CHIP-CDEE

CHIP-CDEE is a clinical finding event extraction benchmark reused from CBLUE and reformulated as generation of clinical finding events and their attributes from medical report text. The paper defines each event as a trigger plus occurrence status, descriptor, and anatomical part.

- **Language:** Chinese.
- **Clinical Stage:** Clinical reporting / not explicitly stated.
- **Source Clinical Document Type:** Medical reports.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted generation.
- **Split / Sample Info:** 3000 train / 400 dev / 400 test; average prompt length 142.61; average target length 180.93.

## 3.1 Task: CHIP-CDEE

This task is to extract clinical finding events from a medical report and generate each event together with its occurrence status, descriptor, and anatomical part.

### Task type
Extraction

```md
### Instruction
[sentence]
问题：句子中的临床发现事件及其属性是什么？
说明：临床发现事件由主体词、发生状态、描述词和解剖部位组成。
### Input
A Chinese medical report sentence or passage.
### Output
A list of event descriptions, where each event contains trigger, occurrence status, descriptor, and anatomical part.
```

### Task example

```md
### Example
Example prompt is a hematology report excerpt mentioning bone marrow findings, fish:pml/rara, and lumbar puncture results.
Example target includes:
- `主体词：fish:pml/rara（双色双融合）(15/17)异常；发生状态：否定；描述词：无；解剖部位：无`
- `主体词：骨髓象；发生状态：无；描述词：增生性；解剖部位：骨髓`
```

### Scoring standard

```md
### Scoring
Instance-level strict micro-F1 after converting generated outputs back into structured event instances.
### Evaluation Dimensions
Exact match on the full event instance, including trigger, occurrence status, descriptor, and anatomical part.
### Judge Prompt
Not applicable. The paper uses deterministic post-processing and strict micro-F1 rather than an LLM judge.
```

## 4. CHIP-CDN

CHIP-CDN is a Chinese clinical diagnosis normalization benchmark reused from CBLUE and reformulated as prompted candidate ranking / generation. The paper states that diagnosis descriptions written by doctors are mapped to standardized ICD-10-Beijing disease terms using a candidate pool built from BM25 retrieval plus gold terms in most cases.

- **Language:** Chinese.
- **Clinical Stage:** Diagnosis normalization / coding support.
- **Source Clinical Document Type:** Doctor-written diagnosis descriptions.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE with retrieved candidate standard terms.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 281.79; average target length 10.37.

## 4.1 Task: CHIP-CDN

This task is to map a free-text diagnosis description to one or more standardized ICD-10-Beijing disease terms selected from a candidate list.

### Task type
Extraction

```md
### Instruction
[sentence]
术语选项：[candidate-terms]
说明：从候选的若干个 ICD-10 诊断标准词中选择出与原诊断描述匹配的词。
### Input
A doctor-written diagnosis description plus a shuffled candidate pool of ICD-10-Beijing standard terms retrieved mainly with BM25.
### Output
The selected standardized term or terms that match the original diagnosis description.
```

### Task example

```md
### Example
Example diagnosis description: `主动脉弓缩窄心功能低下`
Example candidate terms include `主动脉缩窄`, `心功能不全`, and distractors.
Example target: `主动脉缩窄，心功能不全`
```

### Scoring standard

```md
### Scoring
Instance-level strict micro-F1 after post-processing selected standardized terms from the generated text.
### Evaluation Dimensions
Exact correctness of the returned standardized diagnosis term set.
### Judge Prompt
Not applicable. The paper uses deterministic post-processing and strict micro-F1 rather than an LLM judge.
```

## 5. CHIP-CTC

CHIP-CTC is a clinical trial eligibility criteria classification benchmark reused from CBLUE and reformulated as prompted label generation. The benchmark asks the model to predict the screening-criteria type from a provided candidate label set and to answer with a rejection option when none of the shown labels fit.

- **Language:** Chinese.
- **Clinical Stage:** Clinical trial screening.
- **Source Clinical Document Type:** Clinical trial eligibility criteria text.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted classification.
- **Split / Sample Info:** 6600 train / 704 dev / 704 test; average prompt length 214.61; average target length 3.81.

## 5.1 Task: CHIP-CTC

This task is to classify a Chinese clinical trial criterion sentence into one of the screening-criteria types shown in the prompt.

### Task type
Classification

```md
### Instruction
[sentence]
这句话是什么临床试验筛选标准类型？
类型选项：[candidate-types]
### Input
A clinical trial criterion sentence plus a candidate label list.
### Output
One selected criterion type; the paper also states the model should answer `Not the above type` when none of the shown labels matches.
```

### Task example

```md
### Example
Example criterion sentence: `过去3个月内有过眼内手术的患者。`
Example target: `治疗或手术`
```

### Scoring standard

```md
### Scoring
Macro-F1 over the predicted criterion labels after extracting the model choice from generated text.
### Evaluation Dimensions
Correct class assignment among the clinical trial screening-criteria categories.
### Judge Prompt
Not applicable. The paper uses deterministic label extraction and macro-F1 rather than an LLM judge.
```

## 6. CHIP-STS

CHIP-STS is a Chinese medical semantic textual similarity / same-meaning judgment benchmark reused from CBLUE and reformulated as prompt-based generation of `相同` or `不同`.

- **Language:** Chinese.
- **Clinical Stage:** Consumer / clinical question understanding.
- **Source Clinical Document Type:** Disease-related question pairs.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted semantic comparison.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 66.26; average target length 2.00.

## 6.1 Task: CHIP-STS

This task is to determine whether two disease-related Chinese questions express the same semantics.

### Task type
Classification

```md
### Instruction
下面两个句子语义是“相同”或“不同”？
"[sentence-1]"，"[sentence-2]"。
选项：[candidate-types]
答：
### Input
A pair of disease-related Chinese questions.
### Output
`相同` / `不同` or an equivalent yes/no rendering listed in the prompt.
```

### Task example

```md
### Example
Example pair:
- `糖尿病的三多一少是什么`
- `灵芝皇和桑唐饮能治好糖尿病吗？`
Example target: `不同`
```

### Scoring standard

```md
### Scoring
Micro-F1 over the binary semantic relation labels after extracting the model choice from generated text.
### Evaluation Dimensions
Correct pairwise semantic-equivalence decision.
### Judge Prompt
Not applicable. The paper uses deterministic label extraction and micro-F1 rather than an LLM judge.
```

## 7. KUAKE-QIC

KUAKE-QIC is an online medical search intent classification benchmark reused from CBLUE and reformulated as candidate-label generation. The paper explicitly drops the high-frequency `other` category from the prompt and requires the model to answer with a fallback rejection string when none of the shown intent labels fits.

- **Language:** Chinese.
- **Clinical Stage:** Consumer health information seeking.
- **Source Clinical Document Type:** Online medical search queries.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted intent classification.
- **Split / Sample Info:** 5500 train / 440 dev / 440 test; average prompt length 81.58; average target length 4.09.

## 7.1 Task: KUAKE-QIC

This task is to classify the intent of a Chinese online medical search query using a provided set of candidate intent labels.

### Task type
Classification

```md
### Instruction
判断下面搜索词的意图：
[query]
选项：[candidate-types]
答：
### Input
A Chinese online medical search query and a candidate set of intent labels.
### Output
One selected intent label; the paper states the model should answer `Not the above type` when no shown label matches.
```

### Task example

```md
### Example
Example query: `武汉传染性尖锐湿疣的治疗方法`
Example target: `治疗方案`
```

### Scoring standard

```md
### Scoring
Macro-F1 over the intent labels after extracting the generated label choice.
### Evaluation Dimensions
Correct classification of query intent among the candidate categories.
### Judge Prompt
Not applicable. The paper uses deterministic label extraction and macro-F1 rather than an LLM judge.
```

## 8. KUAKE-QTR

KUAKE-QTR is a Chinese medical query-title relevance benchmark reused from CBLUE and reformulated as prompted four-way relevance grading between an online medical search query and a webpage title.

- **Language:** Chinese.
- **Clinical Stage:** Consumer health information retrieval.
- **Source Clinical Document Type:** Online medical search query plus webpage title.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted relevance grading.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 96.38; average target length 7.23.

## 8.1 Task: KUAKE-QTR

This task is to grade how semantically related a Chinese medical search query is to a webpage title using one of four relevance labels.

### Task type
Classification

```md
### Instruction
下面的搜索词和页面标题的意思有多相同？
搜索词：[query]
页面标题：[web-page-title]
选项：完全不匹配或者没有参考价值，很少匹配有一些参考价值，部分匹配，完全匹配
### Input
A Chinese medical search query and a webpage title.
### Output
One of the four prompt-defined relevance labels.
```

### Task example

```md
### Example
Example query: `宝宝三周了发烧不玩睡觉`
Example page title: `孩子三周了手足口发烧一天就不烧了就是睡觉打搀`
Example target: `部分匹配`
```

### Scoring standard

```md
### Scoring
Micro-F1 over the four-way relevance labels after extracting the generated label choice.
### Evaluation Dimensions
Correct graded semantic relatedness judgment for the query-title pair.
### Judge Prompt
Not applicable. The paper uses deterministic label extraction and micro-F1 rather than an LLM judge.
```

## 9. KUAKE-QQR

KUAKE-QQR is a Chinese medical query-query semantic relation benchmark reused from CBLUE and reformulated as prompted labeling of the relation between two queries.

- **Language:** Chinese.
- **Clinical Stage:** Consumer health information seeking.
- **Source Clinical Document Type:** Online medical query pairs.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted semantic relation labeling.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 89.38; average target length 7.61.

## 9.1 Task: KUAKE-QQR

This task is to determine the semantic relationship between two Chinese medical queries, including equivalence, subset, superset, or no direct semantic relation.

### Task type
Classification

```md
### Instruction
下面两个句子的语义关系是？
"[sentence-1]"，"[sentence-2]"。
选项：完全一致，后者是前者的语义子集，后者是前者的语义父集，语义毫无关联
### Input
A pair of Chinese medical queries.
### Output
One semantic relation label among equivalence, subset, superset, or unrelated.
```

### Task example

```md
### Example
Example pair:
- `伤口涂什么药好得快`
- `有伤口涂什么药`
Example target: `完全一致`
```

### Scoring standard

```md
### Scoring
Micro-F1 over the semantic relation labels after extracting the generated label choice.
### Evaluation Dimensions
Correct semantic relation classification for the query pair.
### Judge Prompt
Not applicable. The paper uses deterministic label extraction and micro-F1 rather than an LLM judge.
```

## 10. KUAKE-IR

KUAKE-IR is a Chinese medical information retrieval benchmark reused from CBLUE and reformulated into pairwise relevance judgment. Because a full document corpus cannot be passed to an LLM prompt, PromptCBLUE converts the original retrieval setting into a binary query-document relatedness task.

- **Language:** Chinese.
- **Clinical Stage:** Consumer health information retrieval.
- **Source Clinical Document Type:** Online medical query plus retrieved answer/document text.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE as binary relevance judgment.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 203.33; average target length 2.78.

## 10.1 Task: KUAKE-IR

This task is to determine whether a Chinese medical query and a candidate answer/document are relevant to each other.

### Task type
Classification

```md
### Instruction
医疗搜索：[query]
回答内容：[document]
选项：相关，不相关
答：
### Input
A medical search query and a candidate answer/document passage.
### Output
`相关` or `不相关`.
```

### Task example

```md
### Example
Example query: `鼻梁被撞鼻梁矫正手术`
Example document: a passage about nasal bone osteotomy, hospitalization, cost, and insurance reimbursement.
Example target shown in the appendix: `相关`
```

### Scoring standard

```md
### Scoring
Micro-F1 over the binary relevance labels after extracting the generated label choice.
### Evaluation Dimensions
Correct relevance judgment for the query-document pair.
### Judge Prompt
Not applicable. The paper uses deterministic label extraction and micro-F1 rather than an LLM judge.
```

## 11. CHIP-MDCFNPC

CHIP-MDCFNPC is a doctor-patient dialogue clinical-finding status benchmark reused from CBLUE and reformulated as prompted extraction of clinical findings plus status descriptions. The paper preserves the original four-way status semantics but asks the model to output natural-language status descriptions instead of compact labels.

- **Language:** Chinese.
- **Clinical Stage:** Medical consultation dialogue understanding.
- **Source Clinical Document Type:** Patient-doctor dialogue history.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE sub-benchmark, reformulated by PromptCBLUE for prompted dialogue extraction.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 744.99; average target length 67.67.

## 11.1 Task: CHIP-MDCFNPC

This task is to extract clinical findings from a patient-doctor dialogue and assign each finding one of four status descriptions covering positive, negative, unclear, or not-to-be-labeled cases.

### Task type
Extraction

```md
### Instruction
[dialogue-history]
问题：上述问诊对话中临床发现有哪些？这些实体的阴阳性是？
阴阳性选项：已有症状疾病或者假设未来可能发生的疾病等，未患有症状疾病，没有回答/不知道/回答不明确或者模棱两可不好推断，无实际意义的不标注或者和病人当前的状态独立不标注
说明：临床发现是临床医学下病人状态描述的概念集合。
### Input
A patient-doctor dialogue history.
### Output
A list of clinical finding entities and one status description for each entity.
```

### Task example

```md
### Example
Example dialogue discusses menstruation, thyroid findings, medication use, and uncertainty about hypothyroidism.
Example target includes:
- `月经没来：已有症状疾病或者假设未来可能发生的疾病等`
- `甲减：没有回答、不知道、回答不明确或者模棱两可不好推断`
- `月经量多：无实际意义的不标注或者和病人当前的状态独立不标注`
```

### Scoring standard

```md
### Scoring
Instance-level strict micro-F1. A prediction is correct only when both the extracted clinical finding entity and its status are correct.
### Evaluation Dimensions
Exact extraction of the finding entity and exact assignment of its four-way status description.
### Judge Prompt
Not applicable. The paper uses deterministic post-processing and strict micro-F1 rather than an LLM judge.
```

## 12. IMCS-V2-SR

IMCS-V2-SR is a symptom-status benchmark derived from the IMCS-V2 medical dialogue dataset and reformulated as prompted extraction from dialogue context. The paper explicitly simplifies the original CBLUE pipeline by discarding the symptom normalization step and keeping only symptom extraction plus status determination.

- **Language:** Chinese.
- **Clinical Stage:** Online consultation dialogue understanding.
- **Source Clinical Document Type:** Dialogue history plus current utterance in patient-doctor consultation.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE / IMCS-V2 sub-benchmark, reformulated by PromptCBLUE.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 137.13; average target length 36.33.

## 12.1 Task: IMCS-V2-SR

This task is to identify symptoms in the current utterance of a medical dialogue and determine whether the patient has the symptom, does not have it, or the status cannot be determined from context.

### Task type
Extraction

```md
### Instruction
找出当前对话中的症状，并判断阴阳性：
对话历史：[dialogue-history]
当前对话：[current-utterance]
症状阴阳性选项：没有患有该症状，患有该症状，无法根据上下文确定病人是否患有该症状
### Input
Dialogue history plus the current utterance in an online consultation.
### Output
A list of symptom entities mentioned in the current utterance, each paired with one of the three status labels.
```

### Task example

```md
### Example
Example dialogue history describes a baby with cough and possible bronchitis; the current utterance recommends tests and treatment.
Example target includes:
- `肺炎：无法根据上下文确定病人是否患有该症状`
- `感染：患有该症状`
- `咳：患有该症状`
- `痰：患有该症状`
```

### Scoring standard

```md
### Scoring
Instance-level strict micro-F1. A prediction is correct only when both the extracted symptom entity and its status are correct.
### Evaluation Dimensions
Exact symptom extraction and exact three-way status assignment.
### Judge Prompt
Not applicable. The paper uses deterministic post-processing and strict micro-F1 rather than an LLM judge.
```

## 13. IMCS-V2-NER

IMCS-V2-NER is a dialogue named entity extraction benchmark derived from IMCS-V2 and reformulated like CMeEE-V2: the model generates entity mentions for requested dialogue-entity types instead of predicting token spans.

- **Language:** Chinese.
- **Clinical Stage:** Online consultation dialogue understanding.
- **Source Clinical Document Type:** Patient-doctor dialogue utterances.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE / IMCS-V2 sub-benchmark, reformulated by PromptCBLUE.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 61.66; average target length 23.65.

## 13.1 Task: IMCS-V2-NER

This task is to extract requested entity types from a patient-doctor dialogue utterance.

### Task type
Extraction

```md
### Instruction
下面对话中的[entity-labels]实体有哪些？
[utterance]
答：
### Input
A patient-doctor dialogue utterance plus one or more requested entity labels.
### Output
Entity mentions grouped by requested entity type, explicitly returning `无` when none is present.
```

### Task example

```md
### Example
Example utterance: `宝贝也呕吐吗？`
Requested entity types: medical examination/testing, symptom, medical procedure.
Example target:
- `医学检查检验实体：无`
- `症状实体：呕吐`
- `医疗操作实体：无`
```

### Scoring standard

```md
### Scoring
Instance-level strict micro-F1 over extracted entity mentions and entity types after post-processing.
### Evaluation Dimensions
Exact entity mention extraction and exact entity-type assignment.
### Judge Prompt
Not applicable. The paper uses deterministic post-processing and strict micro-F1 rather than an LLM judge.
```

## 14. IMCS-V2-DAC

IMCS-V2-DAC is a dialogue act / intent classification benchmark derived from IMCS-V2 and reformulated as prompted label generation. The paper notes that the original label names were not natural-language friendly and rewrites them into more descriptive intent names.

- **Language:** Chinese.
- **Clinical Stage:** Online consultation dialogue understanding.
- **Source Clinical Document Type:** Patient-doctor dialogue utterances.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE / IMCS-V2 sub-benchmark, reformulated by PromptCBLUE with rewritten label names.
- **Split / Sample Info:** 5000 train / 512 dev / 512 test; average prompt length 371.62; average target length 8.56.

## 14.1 Task: IMCS-V2-DAC

This task is to classify the intent of the current utterance in an online medical consultation dialogue.

### Task type
Classification

```md
### Instruction
确定这句话的意图：
[utterance]
类型选项：[candidate-labels]
### Input
A dialogue utterance plus a set of rewritten natural-language intent labels.
### Output
One selected dialogue intent label.
```

### Task example

```md
### Example
Example utterance: `当时医生说我们单纯支气管炎也不喘就开的药`
Example target: `关于已有检查和治疗的回答`
```

### Scoring standard

```md
### Scoring
Macro-F1 over the rewritten dialogue-intent labels after extracting the generated label choice.
### Evaluation Dimensions
Correct dialogue-intent classification.
### Judge Prompt
Not applicable. The paper uses deterministic label extraction and macro-F1 rather than an LLM judge.
```

## 15. IMCS-V2-MRG

IMCS-V2-MRG is a medical report generation benchmark derived from IMCS-V2 and reformulated as six-section diagnostic report generation from doctor-patient dialogue history.

- **Language:** Chinese.
- **Clinical Stage:** Online consultation summarization / reporting.
- **Source Clinical Document Type:** Patient-doctor dialogue history.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused CBLUE / IMCS-V2 sub-benchmark, reformulated by PromptCBLUE for structured report generation.
- **Split / Sample Info:** 3000 train / 400 dev / 400 test; average prompt length 821.10; average target length 105.08.

## 15.1 Task: IMCS-V2-MRG

This task is to summarize a patient-doctor dialogue and generate a diagnostic/treatment report with six ordered sections: chief complaint, history of present illness, auxiliary examination, past medical history, diagnosis, and recommendations.

### Task type
Generation

```md
### Instruction
问诊对话历史：[dialogue-history]
根据上述对话，给出诊疗报告
说明：诊疗报告分为主诉、现病史、辅助检查、既往史、诊断、建议这六个章节。
### Input
A patient-doctor consultation dialogue history.
### Output
A six-section diagnostic and treatment report in the order specified by the prompt.
```

### Task example

```md
### Example
Example dialogue is a pediatric consultation about intermittent cough, sleep instability, normal temperature, dry cough, and follow-up pediatric evaluation.
Example target:
- `主诉：阵发性咳嗽`
- `现病史：患儿阵发性干咳两天`
- `辅助检查：暂缺`
- `既往史：不详`
- `诊断：咳嗽待查`
- `建议：儿科就诊，听诊肺部`
```

### Scoring standard

```md
### Scoring
ROUGE-L against the reference diagnostic report.
### Evaluation Dimensions
Reference-based overlap quality for the generated six-section report. The paper does not provide finer-grained rubric dimensions beyond ROUGE-L.
### Judge Prompt
Not applicable. The paper uses ROUGE-L rather than an LLM judge.
```

## 16. MedDG

MedDG is a doctor-response generation benchmark reused in PromptCBLUE as prompted dialogue generation. The paper states that the original MedDG setting is entity-centric dialogue generation, but PromptCBLUE currently discards that entity constraint and evaluates only doctor-response generation from dialogue history.

- **Language:** Chinese.
- **Clinical Stage:** Online medical consultation dialogue generation.
- **Source Clinical Document Type:** Patient-doctor dialogue history.
- **Clinical Specialty:** Multi-specialty / not explicitly stated.
- **Application Method:** Reused MedDG task reformulated by PromptCBLUE for direct doctor-response generation.
- **Split / Sample Info:** 5000 train / 400 dev / 400 test; average prompt length 194.75; average target length 27.71.

## 16.1 Task: MedDG

This task is to generate the doctor's next response given the dialogue history and the patient's current utterance.

### Task type
Generation

```md
### Instruction
[dialogue-history]
根据上述对话历史，作为医生应该如何回复？
答：
### Input
A patient-doctor dialogue history ending with the patient's current utterance.
### Output
A generated doctor response.
```

### Task example

```md
### Example
Example dialogue history describes nighttime stomach discomfort, post-meal nausea, headache, dizziness, and nausea in a 19-year-old patient.
Example target doctor response: `胃部感觉难受是怎么难受？反酸烧心打嗝？还是胃疼胃胀？`
```

### Scoring standard

```md
### Scoring
ROUGE-L against the reference doctor response.
### Evaluation Dimensions
Reference-based overlap quality for the generated response. The paper does not provide finer-grained rubric dimensions beyond ROUGE-L.
### Judge Prompt
Not applicable. The paper uses ROUGE-L rather than an LLM judge.
```
