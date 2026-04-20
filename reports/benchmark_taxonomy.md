# Benchmark Taxonomy

This document organizes the benchmarks currently summarized in this repository into a practical multidimensional taxonomy.

Scope:
- Coverage target is the current benchmark-section inventory in `summaries/*.md` plus a few umbrella benchmark families that are described in workflow notes but do not appear as standalone `##` benchmark headers.
- Benchmark names are preserved as they appear in the summary documents.
- When the same benchmark is reused in multiple papers, the taxonomy labels describe the benchmark itself, not a specific reuse context.
- A few names are effectively aliases in the current corpus, such as `MIMIC-IV CDM` and `MIMIC-IV-CDM`; they are kept as separate strings for traceability but assigned the same family labels.

## Label Legend

`task`
- `MCQ`: multiple-choice QA / closed-set exam QA
- `CLS`: classification / labeling / verification
- `SIM`: semantic similarity / NLI / relevance judgment
- `EXT`: extraction / sequence labeling / structured slot filling
- `COD`: normalization / coding / canonical mapping
- `SUM`: summarization / note construction / evidence extraction
- `GEN`: free-form answer / explanation / response generation
- `RET`: retrieval / grounding
- `SQL`: text-to-SQL / database semantic parsing
- `CODE`: code generation / executable problem solving
- `CALC`: numeric clinical calculation
- `ACT`: action execution / workflow operation
- `MIX`: benchmark mixes multiple task forms

`interaction`
- `ST-S`: single-turn, short/closed-form input
- `ST-L`: single-turn, long-context input
- `MT-X`: multi-utterance transcript as static input, one final output
- `INT`: genuinely interactive multi-turn dialogue
- `AGT`: tool-using / API-using / executable agent loop
- `MIX`: benchmark intentionally mixes several interaction regimes

`source`
- `EXAM`: exam questions / expert-authored QA items
- `LIT`: biomedical literature, ontology, or abstract-derived text
- `SEHR`: structured EHR tables, coded event streams, SQL schemas, or FHIR resources
- `NOTE`: free-text clinical notes, discharge summaries, case reports, chief complaints
- `RAD`: radiology / imaging reports
- `DIAL`: patient-doctor dialogue, consultation record, portal/chat transcript
- `WEB`: consumer medical questions, search queries, web/forum QA
- `MIX`: multi-source benchmark suite or mixed record types

`role`
- `CORE`: standalone benchmark / dataset
- `VAR`: released variant or difficulty split of a core benchmark
- `SUITE`: umbrella benchmark family / benchmark suite

Interpretation note:
- The taxonomy uses a primary family assignment, so some benchmarks that span multiple abilities are placed under the family that best matches their dominant evaluation goal.

## 1. Executable EHR Querying, Tool Use, and Code-Centric Reasoning

- `MIMICSQL`, `EHRSQL`, `EHRSQL 2024 Shared Task`, `EHR-SeqSQL`, `TREQS`: `task=SQL`; `interaction=ST-S`; `source=SEHR`; `role=CORE`
- `EHR-ChatQA`: `task=SQL+GEN`; `interaction=INT`; `source=SEHR`; `role=CORE`
- `FHIR-AgentBench`, `MedAgentBench`: `task=RET+ACT`; `interaction=AGT`; `source=SEHR`; `role=CORE`
- `MedAgentGym`: `task=CODE+ACT`; `interaction=AGT`; `source=MIX`; `role=CORE`
- `BioCoder`, `BioDSBench`: `task=CODE`; `interaction=AGT`; `source=MIX`; `role=CORE`
- `EHRCon`, `MIMIC-Extract`: `task=CODE+CLS`; `interaction=AGT`; `source=MIX`; `role=CORE`
- `MedCalcBench`: `task=CODE+CALC`; `interaction=AGT`; `source=NOTE`; `role=CORE`
- `MedCalc-Bench`: `task=CALC`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `N-PowerAI`: `task=CODE+CALC`; `interaction=AGT`; `source=MIX`; `role=CORE`

## 2. Clinical Prediction, Diagnosis, and Decision Support

- `EHR-Bench`, `EHRSHOT`: `task=CLS`; `interaction=ST-L`; `source=SEHR`; `role=CORE`
- `MIMIC-IV CDM`, `MIMIC-IV-CDM`, `MIMIC-III Outcome`, `Brateca`, `Mexican Clinical Records`, `GOUT-CC`: `task=CLS`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `MIMIC4ED Benchmark`: `task=CLS`; `interaction=ST-L`; `source=MIX`; `role=CORE`
- `BrainMRI-AIS`, `MIMIC-IV DiReCT`: `task=CLS`; `interaction=ST-L`; `source=RAD`; `role=CORE`
- `DDXPlus`: `task=CLS`; `interaction=ST-L`; `source=DIAL`; `role=CORE`
- `SEER`: `task=GEN`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `DialMed`: `task=CLS`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `EHRQA`: `task=MIX`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `Real-World Clinical Cases`: `task=MIX`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `MedAlign`: `task=MIX`; `interaction=ST-L`; `source=MIX`; `role=CORE`
- `N2C2-CT`, `CHIP-CTC`: `task=CLS`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `n2c2 2014 - Heart Disease Challenge`: `task=CLS`; `interaction=ST-L`; `source=NOTE`; `role=CORE`

## 3. Extraction, Coding, Normalization, and De-identification

- `BC4Chem`, `BC5CDR`, `Species800`: `task=EXT`; `interaction=ST-S`; `source=LIT`; `role=CORE`
- `ADE Corpus`, `PICO`, `PMC-Patient`: `task=EXT`; `interaction=ST-L`; `source=LIT`; `role=CORE`
- `ADE`, `BARR2`, `CMeEE-V2`, `CMeIE`, `CHIP-CDEE`, `CLINpt`, `DiSMed`, `Ex4CDS`, `iCorpus`, `RuDReC`, `RuCCoN`, `IFMIR`, `CARDIO:DE`, `BRONCO150`, `meddocan`, `n2c2 2006`, `n2c2 2018 Track2`: `task=EXT`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `n2c2 2014 - De-identification`, `NorSynthClinical-PHI`, `GraSSCo_PHI`: `task=EXT`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `NUBES`: `task=EXT`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `MIE`, `IMCS-V2-NER`, `IMCS-V2-SR`, `CHIP-MDCFNPC`: `task=EXT`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `CHIP-CDN`, `CARES`, `Cantemist`, `CLEF eHealth 2020 - CodiEsp`, `MIMIC-IV Billing Code`, `C-EMRS`: `task=COD`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `ClinicalNotes-UPMC`, `CLIP`, `NoteExtract`: `task=CLS/EXT`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `CAS`: `task=EXT+SUM`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `NorSynthClinical`: `task=EXT`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `i2b2 2009`, `i2b2 2010`, `mtsamples-temporal`: `task=EXT`; `interaction=ST-L`; `source=NOTE`; `role=CORE`

## 4. Semantic Matching, NLI, and Query / Topic Understanding

- `CHIP-STS`, `KUAKE-QTR`, `KUAKE-QQR`, `KUAKE-IR`, `MEDIQA_2019_Task2_RQE`, `MedNLI`, `MedSTS`, `RuMedNLI`, `CLISTER`, `Japanese Case Reports`, `RuMedDaNet`: `task=SIM`; `interaction=ST-S`; `source=LIT/NOTE/WEB`; `role=CORE`
- `KUAKE-QIC`: `task=CLS`; `interaction=ST-S`; `source=WEB`; `role=CORE`
- `IMCS-V2-DAC`: `task=CLS`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `IMCS-V2`: `task=MIX`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `mtsamples`: `task=CLS`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `HoC`: `task=CLS`; `interaction=ST-S`; `source=LIT`; `role=CORE`

## 5. Summarization, Documentation, and Doctor-Response Generation

- `MIMIC-CXR`, `MIMIC-IV Report`, `MIMIC-RRS`, `MIMIC-BHC`, `MIMIC-IV BHC`, `DischargeMe`: `task=SUM`; `interaction=ST-L`; `source=RAD/NOTE`; `role=CORE`
- `ACI-Bench`: `task=SUM`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `MTS-Dialog-MEDIQA-2023`: `task=SUM+CLS`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `MedDialog`, `MedDG`, `cMedQA`, `icliniq-10k`, `HealthCareMagic-100k`: `task=GEN`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `MedicationQA`, `MEDIQA-QA`: `task=GEN`; `interaction=ST-S`; `source=WEB`; `role=CORE`
- `PatientInstruct`, `IMCS-V2-MRG`: `task=GEN`; `interaction=MT-X`; `source=DIAL/NOTE`; `role=CORE`
- `MTSamples`, `MTSamples Procedures`: `task=GEN`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `MedQSum`, `RCT-Text`: `task=SUM`; `interaction=ST-L`; `source=LIT`; `role=CORE`

## 6. Knowledge QA, Exam QA, and Literature / Ontology Reasoning

- `MedQA`, `MedMCQA`, `HeadQA`, `Medbullets`, `MMedBench`, `Chinese Medical Licensing Examination (CNMLE)`, `Resident Standardization Training Examination`, `Doctor In-Charge Qualification Examination`: `task=MCQ`; `interaction=ST-S`; `source=EXAM`; `role=CORE`
- `PubMedQA`: `task=CLS/GEN`; `interaction=ST-S`; `source=LIT`; `role=CORE`
- `PUBHEALTH / PUBLICHEALTH`: `task=CLS+GEN`; `interaction=ST-S`; `source=LIT`; `role=CORE`
- `Human Disease Ontology (DO)`, `BioLORD`: `task=GEN`; `interaction=ST-S`; `source=LIT`; `role=CORE`
- `EBMS`: `task=GEN`; `interaction=ST-L`; `source=LIT`; `role=CORE`

## 7. Safety, Privacy, Bias, Quality, and Compliance

- `HealthBench`: `task=GEN`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `HealthBench Consensus`, `HealthBench Hard`: `task=CLS/GEN`; `interaction=MT-X`; `source=DIAL`; `role=VAR`
- `RaceBias`, `MedHallu`: `task=CLS`; `interaction=ST-S`; `source=LIT`; `role=CORE`
- `Medec`: `task=CLS+GEN`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `CLEAR`, `ADHD-Behavior`, `ADHD-MedEffects`, `BMT-Status`, `HospiceReferral`, `ClinicReferral`, `ENT-Referral`, `CDI-QA`: `task=CLS/QA`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `PrivacyDetection`, `ProxySender`: `task=CLS`; `interaction=MT-X`; `source=DIAL`; `role=CORE`
- `MedConfInfo`: `task=CLS`; `interaction=ST-L`; `source=NOTE`; `role=CORE`
- `MentalHealth`: `task=GEN`; `interaction=MT-X`; `source=DIAL`; `role=CORE`

## 8. Benchmark Suites and Variants

- `MedHELM (Umbrella Evaluation Framework)`: `task=MIX`; `interaction=MIX`; `source=MIX`; `role=SUITE`
- `MedBench`: `task=MIX`; `interaction=MIX`; `source=MIX`; `role=SUITE`
- `BRIDGE`: `task=MIX`; `interaction=MIX`; `source=MIX`; `role=SUITE`
- `PromptCBLUE`: `task=MIX`; `interaction=MIX`; `source=MIX`; `role=SUITE`
- `MedS-Bench`: `task=MIX`; `interaction=MIX`; `source=MIX`; `role=SUITE`

## 9. Short Takeaways

- The repository is dominated by two macro-clusters: `clinical text structuring` (`EXT/COD/CLS`) and `EHR/agentic/executable reasoning` (`SQL/CODE/ACT`).
- `interaction` is highly bimodal: most classic benchmarks are `ST-S` or `ST-L`, while a smaller but increasingly important set (`EHR-ChatQA`, `FHIR-AgentBench`, `MedAgentBench`, `MedAgentGym`) is genuinely `INT` or `AGT`.
- `source` is split mainly across `NOTE`, `SEHR`, `DIAL`, and `LIT`; very few benchmarks are pure `RAD`, and those are mostly diagnostic or summarization-oriented.
- Safety-oriented benchmarks in this repo are mostly `response quality / privacy / compliance` evaluations rather than pure knowledge tests.
- Several names that look similar actually land in different parts of the taxonomy: for example `MTSamples` is treatment-plan generation from notes, while `mtsamples` in BRIDGE is document/specialty classification; `MedCalc-Bench` is single-turn note-based calculation, while `MedCalcBench` in MedAgentGym is executable code-centric clinical computation.
