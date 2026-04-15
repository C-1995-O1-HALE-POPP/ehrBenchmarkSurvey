<!-- paper_key: "2024_medalign_a_clinician_generated_dataset_for_instruction_following_with_electronic_medical_records" -->
<!-- paper_url: "https://ojs.aaai.org/index.php/AAAI/article/view/30205" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *MedAlign: A Clinician-Generated Dataset for Instruction Following with Electronic Medical Records*

Source paper: [https://ojs.aaai.org/index.php/AAAI/article/view/30205](https://ojs.aaai.org/index.php/AAAI/article/view/30205)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2024_medalign_a_clinician_generated_dataset_for_instruction_following_with_electronic_medical_records/source.pdf`](../papers/2024_medalign_a_clinician_generated_dataset_for_instruction_following_with_electronic_medical_records/source.pdf)
- Extracted text: [`../papers/2024_medalign_a_clinician_generated_dataset_for_instruction_following_with_electronic_medical_records/source.txt`](../papers/2024_medalign_a_clinician_generated_dataset_for_instruction_following_with_electronic_medical_records/source.txt)
- Ownership for this run is limited to this summary file. The registry was intentionally not edited.
- Normalization choice: this paper introduces one benchmark, `MedAlign`. The six instruction categories in Table 2 are represented below as survey task families; Appendix Table S2 confirms that these expand into 20 subcategories.
- Appendix/arXiv HTML rerun (`2026-04-15`): incorporated Appendix C instruction-collection fields, Appendix D Table S2 taxonomy and Table S3 sample responses, Appendix F Figure S4 synthetic XML example, and Appendix R Figure S9 standard generation prompt.
- No train/dev/test split is explicitly stated in the paper. The paper instead reports a full instruction pool plus a clinician-annotated evaluation subset.

## Benchmark Inventory

- `MedAlign` benchmark introduced in this paper.
- Task families explicitly named in Table 2: `Retrieve & Summarize`, `Care Planning`, `Calculation & Scoring`, `Diagnosis Support`, `Translation`, and `Other`.
- Appendix Table S2 decomposes these into 20 subcategories: `Retrieve Medical History`, `Determine Plan of Care`, `Retrieve Imaging Studies`, `Retrieve Demographics`, `Retrieve Medication Information`, `Retrieve Laboratory Studies`, `Calculate Numerical Measures`, `Provide Diagnosis Assistance`, `Provide Risk Assessment`, `Retrieve Social History`, `Provide Patient Education Information`, `Retrieve Vitals`, `Retrieve Appointment Information`, `Retrieve Genetic and Family History`, `Retrieve Institutional Policies`, `Retrieve Provider Referrals`, `Retrieve Communications with Patient`, `Translate Materials`, `Retrieve Coding & Billing Information`, and `Other`.

## 1. MedAlign

MedAlign is an English (inferred) benchmark for evaluating instruction following over longitudinal electronic health records. It is built from clinician-authored natural language questions and imperative instructions, paired with de-identified EHR records from the authors' academic medical center, represented in OMOP CDM and serialized into XML markup. The paper reports 1,314 raw submitted instructions from 15 clinicians across 7 specialties, 983 deduplicated instructions after removing near-duplicates with ROUGE-L similarity above 0.7, 407 deduplicated instructions tagged as applicable to patients generally, and 303 instruction-EHR pairs with clinician-written reference responses used for formal model evaluation on 276 longitudinal patient EHRs. Instructions were collected independently of a specific chart, then matched to candidate EHRs using BM25; for 303 instructions, at least one of the top 5 retrieved EHRs was relevant according to manual review. Benchmark access is stated to be under a research data use agreement.

- **Language:** English (inferred from the example instructions and the US academic-clinical setting; not explicitly labeled in the paper)
- **Clinical Stage:** Longitudinal inpatient and ambulatory care across the hospital course (inferred from the paper's description of comprehensive longitudinal EHRs from inpatient and ambulatory settings)
- **Source Clinical Document Type:** Structured and unstructured longitudinal EHR data serialized into XML markup
- **Clinical Specialty:** Multi-specialty: Internal Medicine, Neurology, Radiology, Cardiology, Oncology, Surgery, and Primary Care
- **Application Method:** Benchmark introduced in the paper; de-identified dataset shared under a research data use agreement

### Evaluation protocol shared across MedAlign task families

- The main benchmarked subset consists of 303 instruction-EHR pairs with clinician-written reference responses.
- Nine clinicians evaluated responses from 6 LLMs. Clinicians did not review their own responses or instructions they had originally submitted.
- Each response received a binary correctness judgment and a relative quality ranking against the other model outputs for the same instruction; ties were allowed.
- A response was marked `incorrect` if it met at least one stated criterion:
  1. It was not clinically appropriate based on the available EHR information.
  2. It included errors that, if corrected, would change the clinical interpretation.
  3. It did not address the instruction.
- Responses not marked incorrect were deemed correct.
- The paper also studies automated ranking proxies against clinician rankings using Kendall's Tau. COMET had the strongest reported average correlation with human rankings (0.37), followed by BERTScore (0.34), METEOR (0.32), chrF++ (0.29), GoogleBLEU (0.29), ROUGE-L (0.27), BLEURT (0.25), LENS (0.18), and UniEval variants (0.09-0.27 depending on dimension).
- The shared generation prompt is explicitly shown in Appendix Figure S9:

```md
Instruction: Answer the following question based on the EHR:
###
Question: """{Question}"""
EHR: """{EHR}"""
```

---

## 1.1 Task: Retrieve & Summarize

This task family covers free-form clinician requests to retrieve information from the longitudinal EHR and summarize it in concise clinically useful text. Appendix Table S2 breaks this family into subcategories including `Retrieve Medical History`, `Retrieve Imaging Studies`, `Retrieve Demographics`, `Retrieve Medication Information`, `Retrieve Laboratory Studies`, `Retrieve Social History`, `Provide Patient Education Information`, `Retrieve Vitals`, `Retrieve Appointment Information`, `Retrieve Genetic and Family History`, `Retrieve Institutional Policies`, `Retrieve Provider Referrals`, `Retrieve Communications with Patient`, and `Retrieve Coding & Billing Information`. Table 2 reports 667 total instructions in this family, of which 223 belong to the 303-item clinician-response subset.

### Task type

Generation / Summarization

```md
### Instruction
No single canonical instruction is defined for this task family. MedAlign groups many free-form clinician-authored retrieval-and-summarization requests under this category.
### Input
A clinician-written natural language instruction plus a longitudinal patient EHR serialized into XML, containing structured and unstructured events ordered over time.
### Output
A brief clinically relevant free-text summary grounded in the supplied EHR at the record's time anchor.
```

### Task example

The paper provides explicit examples for this task family in Figure 1, Appendix Figure S4, and Appendix Table S3.

```md
### Example
Standard generation prompt from Appendix Figure S9:
Instruction: Answer the following question based on the EHR:
###
Question: """{Question}"""
EHR: """{EHR}"""

Synthetic appendix example from Figure S4:
Instruction: Summarize from the EHR the strokes that the patient had and their associated neurologic deficits.
Answer: The patient had strokes in the L basal ganglia in 2018 and multiple strokes in 2022: R occipital, left temporal, L frontal. The patient had right sided weakness associated with the 2018 stroke after which she was admitted to rehab. She then had a left sided hemianopsia related to the 2022 stroke.

Concrete benchmark sample with gold references from Appendix Table S3:
Instruction: Has she ever been on a statin before?
Gold standard reference answer 1: Yes, she has been on a statin before but she had side effects of myositis and GI issues. Had GI upset with simvastatin, nausea with crestor, vomiting wtih pravastatin, fluvastatin cannot tolerate
Gold standard reference answer 2: Patient on pravastatin and simvastatin, but these were stopped due to muscle pain and because they were ineffective.
Gold standard reference answer 3: Yes, this patient has been on pravastatin and simvastatin before.
```

### Scoring standard

```md
### Scoring
For benchmark evaluation, model outputs on the clinician-response subset were reviewed by clinicians for binary correctness and relative ranking against the other model outputs for the same instruction. Automated metrics were also compared against clinician rankings, but those metrics do not replace the benchmark's primary human review.
### Evaluation Dimensions
- Clinician binary correctness:
  1. Response is clinically appropriate given the EHR.
  2. Response does not contain interpretation-changing errors.
  3. Response addresses the instruction.
- Clinician preference ranking among model outputs, with ties allowed, based on which answer is most clinically relevant and appropriate.
- Automated ranking proxies reported at the benchmark level: COMET, BERTScore, METEOR, chrF++, GoogleBLEU, ROUGE-L, BLEURT, LENS, and UniEval dimensions.
### Judge Prompt
Not applicable. The paper uses clinician judges rather than an LLM judge. The shared model-generation prompt is documented above from Appendix Figure S9.
```

---

## 1.2 Task: Care Planning

This task family covers instructions that ask the model to synthesize the current or longitudinal care plan for a patient, often integrating testing history, exacerbations, and treatments. Appendix Table S2 defines the underlying subcategory as `Determine Plan of Care`: `Determine a future plan of care for the patient. If a diagnosis was made, then the planned treatment. If the patient is deemed healthy, then the planned prevention. Plan of care could include follow up tests, imaging to be done in the future.` Table 2 reports 136 total instructions in this family, of which 22 belong to the clinician-response subset.

### Task type

Generation / Care Planning

```md
### Instruction
No single canonical instruction is defined for this task family. The category groups free-form clinician-authored requests related to care-plan synthesis from the EHR.
### Input
A care-planning instruction plus a longitudinal XML-serialized EHR containing structured data and narrative documentation from one or more encounters.
### Output
A brief care-plan-oriented summary or recommendation grounded in the EHR information available up to the time anchor.
```

### Task example

The paper provides an explicit representative instruction for this category in Table 2, but no paired gold response or full worked example for this category in the locally cached paper.

```md
### Example
Representative instruction from Table 2: "Summarize the asthma care plan for this patient including relevant diagnostic testing, exacerbation history, and treatments."
```

### Scoring standard

```md
### Scoring
Same benchmark-level evaluation protocol as Section 1: clinician binary correctness on the gold-response subset, clinician ranking of model outputs for the same instruction, and benchmark-level analysis of automated metrics against clinician rankings.
### Evaluation Dimensions
- Clinician correctness criteria are the three paper-defined incorrectness conditions.
- Quality ranking is based on clinical relevance and appropriateness, with ties allowed.
- No task-family-specific rubric beyond the shared benchmark protocol is explicitly provided.
### Judge Prompt
Not applicable. No LLM judge is used. The shared model-generation prompt is documented above from Appendix Figure S9.
```

---

## 1.3 Task: Calculation & Scoring

This task family covers instructions that ask the model to compute, estimate, or score a clinically meaningful quantity from the record. Appendix Table S2 splits this family into `Calculate Numerical Measures` (`Using standardized tools and scores (BMI, TIMI, CHADS2VASC, ABCD2Score) calculate numerical assessments about current state or future risk`) and `Provide Risk Assessment` (`Provide information on risk of developing new diagnoses or complications of a diagnosis based on known clinical research`). Table 2 reports 70 total instructions in this family, of which 13 belong to the clinician-response subset.

### Task type

Risk Prediction / Calculation

```md
### Instruction
No single canonical instruction is defined for this task family. The category groups free-form clinician-authored requests that require a calculation, score, or explicit risk estimate from the EHR.
### Input
A calculation-oriented instruction plus longitudinal EHR context in XML form.
### Output
A concise calculated or estimated result, optionally with supporting rationale, grounded in the available EHR information.
```

### Task example

The paper provides an explicit representative instruction for this category in Table 2, but no paired gold response or full worked example for this category in the locally cached paper.

```md
### Example
Representative instruction from Table 2: "Identify the risk of stroke in the next 7 days for this TIA patient."
```

### Scoring standard

```md
### Scoring
Same benchmark-level evaluation protocol as Section 1. The paper does not provide a distinct deterministic numeric scoring rule for this task family; outputs are judged by clinicians for correctness and ranked for quality on the clinician-response subset.
### Evaluation Dimensions
- Response must be clinically appropriate given the EHR.
- Response must not contain errors that would change the clinical interpretation.
- Response must address the requested calculation or scoring task.
- Relative ranking is based on clinical relevance and appropriateness.
### Judge Prompt
Not applicable. No LLM judge prompt is provided because the evaluation uses clinician reviewers. The shared model-generation prompt is documented above from Appendix Figure S9.
```

---

## 1.4 Task: Diagnosis Support

This task family covers instructions that ask the model to propose or organize diagnostic reasoning from the available EHR evidence. Appendix Table S2 defines the relevant subcategory as `Provide Diagnosis Assistance`: `Provide a differential diagnosis`. Table 2 reports 33 total instructions in this family, of which 4 belong to the clinician-response subset.

### Task type

Decision Making / Differential Diagnosis

```md
### Instruction
No single canonical instruction is defined for this task family. The category groups free-form diagnostic-support requests authored by clinicians.
### Input
A diagnostic-support instruction plus longitudinal EHR content in XML form; the example in Table 2 specifically mentions information included under the HPI.
### Output
A brief diagnosis-oriented answer, such as a differential diagnosis, grounded in the supplied EHR evidence.
```

### Task example

The paper provides an explicit representative instruction for this category in Table 2, but no paired gold response or full worked example for this category in the locally cached paper.

```md
### Example
Representative instruction from Table 2: "Based on the information I've included under HPI, what is a reasonable differential diagnosis?"
```

### Scoring standard

```md
### Scoring
Same benchmark-level evaluation protocol as Section 1. The paper does not define a diagnosis-family-specific rubric beyond clinician correctness judgments and cross-model ranking.
### Evaluation Dimensions
- Clinical appropriateness given the EHR.
- No interpretation-changing errors.
- Directly addresses the diagnostic-support instruction.
- Ranking based on the most clinically relevant and appropriate response, with ties allowed.
### Judge Prompt
Not applicable. The evaluation uses clinicians rather than an LLM judge. The shared model-generation prompt is documented above from Appendix Figure S9.
```

---

## 1.5 Task: Translation

This task family covers translation requests grounded in patient-facing clinical materials or instructions from the EHR workflow. Appendix Table S2 defines the relevant subcategory as `Translate Materials`: `Translate documents and instructions from one language to another language`. Table 2 reports 2 total instructions in this family, and 0 instructions from this family appear in the clinician-response subset used for formal benchmark scoring.

### Task type

Translation

```md
### Instruction
No single canonical instruction is defined for this task family. The category groups free-form clinician-authored translation requests.
### Input
A translation instruction plus EHR-linked or patient-facing source text that needs translation.
### Output
A translated version of the requested clinical content in the target language.
```

### Task example

The paper provides an explicit representative instruction for this category in Table 2, but no paired gold response or formal evaluation example is available in the locally cached paper.

```md
### Example
Representative instruction from Table 2: "I have a patient that speaks only French. Please translate these FDG-PET exam preparation instructions for her."
```

### Scoring standard

```md
### Scoring
The paper defines the same benchmark-level evaluation protocol, but Table 2 reports zero clinician-response examples for this category. Therefore, no task-family-specific scored translation subset is explicitly available in the paper.
### Evaluation Dimensions
Not explicitly available for this task family because no scored examples are reported in the clinician-response subset. The only explicit scoring rubric in the paper is the shared clinician correctness/ranking protocol used on the 303 evaluated instruction-EHR pairs overall.
### Judge Prompt
Not applicable. No LLM judge is used. The shared model-generation prompt is documented above from Appendix Figure S9.
```

---

## 1.6 Task: Other

This task family is a residual category for clinician-authored instructions that do not cleanly fit the other five top-level groups. Appendix Table S2 defines this bucket simply as `Instructions that do not fit into any of the other categories`. Table 2 reports 75 total instructions in this family, of which 41 belong to the clinician-response subset.

### Task type

Other / Workflow Prioritization

```md
### Instruction
No single canonical instruction is defined for this task family. It captures remaining free-form clinician-authored instructions outside the other named categories.
### Input
A miscellaneous instruction plus the relevant longitudinal XML-serialized EHR context.
### Output
A clinically useful text response that fulfills the instruction; the exact output format depends on the underlying request.
```

### Task example

The paper provides an explicit representative instruction for this category in Table 2, but no paired gold response or fuller worked example for this category in the locally cached paper.

```md
### Example
Representative instruction from Table 2: "What patients on my service should be prioritized for discharge today?"
```

### Scoring standard

```md
### Scoring
Same benchmark-level evaluation protocol as Section 1: clinician binary correctness and clinician ranking on the gold-response subset, plus benchmark-level comparison to automated metrics.
### Evaluation Dimensions
- Clinical appropriateness given the EHR.
- No interpretation-changing errors.
- Response addresses the instruction.
- Relative ranking based on clinical relevance and appropriateness.
### Judge Prompt
Not applicable. The benchmark uses clinician review, not an LLM judge. The shared model-generation prompt is documented above from Appendix Figure S9.
```

## Verifier Notes

- Benchmark count in this summary: 1 (`MedAlign`).
- Task-family count in this summary: 6, corresponding exactly to the six explicit categories listed in Table 2.
- Explicit worked examples are now available from Figure 1, Appendix Figure S4, and Appendix Table S3.
- Appendix-only details used in this summary now include Appendix C instruction-collection fields, Appendix D Table S2 taxonomy, Appendix F Figure S4 synthetic XML example, and Appendix R Figure S9 standard generation prompt.
- No registry changes were made in this run.
