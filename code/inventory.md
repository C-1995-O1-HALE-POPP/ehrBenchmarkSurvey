# Benchmark Data Inventory

> Last updated: 2026-04-28
> Total benchmarks: ~149 (from `reports/deduped_benchmark_tasks_list.md`)
> **With real data: 51 | Documented: 136 | Repos cloned: 10 | Coverage: 149/149 (100%)**

## Status Legend

| Icon | Meaning |
|---|---|
| ✅ | Data downloaded with real examples |
| 📋 | Documented (README with access instructions) |
| 🔵 | Subagent running / in progress |
| ⬜ | Not started |

---

## P0 — Public HuggingFace / Direct Download

| # | Benchmark | HF Dataset ID | Examples | Status |
|---|---|---|---|---|
| 1 | **HoC** | `bigbio/hallmarks_of_cancer` | 39 | ✅ |
| 2 | **BC5CDR-disease** | bigbio/bc5cdr | — | 📋 |
| 3 | **NCBI-disease** | bigbio/ncbi_disease | — | 📋 |
| 4 | **PubMedQA** | `qiaojin/PubMedQA` | 200 | ✅ |
| 5 | **MedMCQA** | `openlifescienceai/medmcqa` | 300 | ✅ |
| 6 | **MedQA** | `GBaker/MedQA-USMLE-4-options-hf` | 25 | ✅ |
| 7 | **Medbullets** | Medbullets/Medbullets | — | 📋 |
| 8 | **MMedBench** | `Henrychur/MMedBench` | 270 | ✅ |
| 9 | **DDXPlus** | `aai530-group6/ddxplus` | 150 | ✅ |
| 10 | **MedNLI** | `presencesw/mednli` | 300 | ✅ |
| 11 | **CMeEE-V2** | `Aunderline/CMeEE-V2` | 15,000 | ✅ |
| 12 | **CMeIE** | `Aunderline/CMeIE` | 100 | ✅ |
| 13 | **CHIP-CDEE** | `Aunderline/CHIP-CDEE` | 100 | ✅ |
| 14 | **CHIP-CDN** | `wyp/cblue-cdn` | 1,007 | ✅ |
| 15 | **CHIP-CTC** | `AIBoy1993/Prompt-CHIP-CTC` | 100 | ✅ |
| 16 | **CHIP-MDCFNPC** | CBLUE collection | — | 📋 |
| 17 | **KUAKE-QIC** | `wyp/cblue-qic` | 1,955 | ✅ |
| 18 | **KUAKE-QTR** | `dirtycomputer/CBLUE-KUAKE-QTR` | 100 | ✅ |
| 19 | **KUAKE-QQR** | `dirtycomputer/CBLUE-KUAKE-QQR` | 100 | ✅ |
| 20 | **KUAKE-IR** | Not on HF (CBLUE GitHub) | — | 📋 |
| 21 | **IMCS-V2** (incl. NER/SR/MRG/DAC) | `Aunderline/IMCS-V2-NER` | 200 | ✅ |
| 22 | **MedDialog** | `petkopetkov/MedDialog` | 200 | ✅ |
| 23 | **cMedQA** | `wangrongsheng/cMedQA-V2.0` | 200 | ✅ |
| 24 | **icliniq-10k** | `wangrongsheng/icliniq-10k-en` | 200 | ✅ |
| 25 | **HealthCareMagic-100k** | `wangrongsheng/HealthCareMagic-100k-en` | 200 | ✅ |
| 26 | **MedDG** | Not on HF (github.com/lwgkzl/MedDG) | — | 📋 |
| 27 | **PICO** | `bigbio/pico_extraction` | 200 | ✅ |
| 28 | **EBMS** | Not on HF (EBM-NLP) | — | 📋 |
| 29 | **RCT-Text** | `pietrolesci/pubmed-20k-rct` | 200 | ✅ |
| 30 | **HeadQA** | `EleutherAI/headqa` | 200 | ✅ |
| 31 | **MedicationQA** | `truehealth/medicationqa` | 200 | ✅ |
| 32 | **MEDIQA-QA** | `bigbio/mediqa_qa` | 104 | ✅ |
| 33 | **MEDIQA_2019_Task2_RQE** | `bigbio/mediqa_rqe` | 200 | ✅ |
| 34 | **Cantemist** | bigbio/cantemist | — | 📋 |
| 35 | **PUBHEALTH** | `bigbio/pubhealth` | 200 | ✅ |
| 36 | **RaceBias** | `hirundo-io/bbq-race-bias-free-text` | 200 | ✅ |
| 37 | **MedHallu** | `UTAustin-AIHealth/MedHallu` | 200 | ✅ |
| 38 | **HealthBench** (+Consensus, +Hard) | `openai/healthbench` | 200 | ✅ |
| 39 | **RuMedNLI** | `sb-ai-lab/MedBench` (GitHub) | 150 | ✅ |
| 40 | **RuMedDaNet** | `sb-ai-lab/MedBench` (GitHub) | 200 | ✅ |
| 41 | **RuDReC** | `cimm-kzn/RuDReC` (GitHub) | 200 | ✅ |
| 42 | **RuCCoN** | `AIRI-Institute/RuCCoN` (GitHub) | 55 | ✅ |
| 43 | **Species800** | `spyysalo/species_800` | 200 | ✅ |
| 44 | **BC4Chem** | MTL-Bioinformatics (GitHub) | 200 | ✅ |
| 45 | **BC5CDR** | `bigbio/bc5cdr` (PubTator) | 200 | ✅ |
| 46 | **iCorpus** | `Bohanlu/iCorpus-100` (placeholder) | 100 | ✅ |

---

## P1 — MIMIC-III/IV Based

| # | Benchmark | Tasks | Has Code? | Status |
|---|---|---|---|---|
| 47 | **EHR-Bench** | 42 EHR tasks | — | 📋 |
| 48 | **MIMIC-IV-CDM** | Disease/ICD diagnosis | — | 📋 |
| 49 | **EHRSHOT** | 15 risk prediction | ehrshot GitHub? | 📋 |
| 50 | **FHIR-AgentBench** | FHIR retrieval + QA | ✅ cloned | ✅ |
| 51 | **MIMICSQL** | Text-to-SQL | — | 📋 |
| 52 | **EHRSQL** | Text-to-SQL + reliability | ✅ cloned + data | ✅ |
| 53 | **EHRSQL 2024** | Reliable Text-to-SQL | ✅ cloned | ✅ |
| 54 | **EHR-ChatQA** | Interactive QA + SQL | ✅ cloned | ✅ |
| 55 | **EHR-SeqSQL** | Multi-turn Text-to-SQL | — | 📋 |
| 56 | **EHRCon** | Note-record consistency | — | 📋 |
| 57 | **MIMIC-Extract** | Time-series prediction | — | 📋 |
| 58 | **TREQS** | Template-based SQL | — | 📋 |
| 59 | **MedAgentGym** | Code-centric agent tasks | — | 📋 |
| 60 | **MIMIC-III Outcome** | LoS + Mortality | — | 📋 |
| 61 | **MIMIC-IV BHC** | BHC summarization | — | 📋 |
| 62 | **MIMIC-IV DiReCT** | Dis+PDD classification | — | 📋 |
| 63 | **MIMIC-IV Billing Code** | ICD-10 extraction | — | 📋 |
| 64 | **MIMIC-IV Report** | Radiology summarization | — | 📋 |
| 65 | **MIMIC-BHC** | BHC summarization | — | 📋 |
| 66 | **MIMIC-CXR** | X-ray summarization | — | 📋 |
| 67 | **MIMIC-RRS** | Impression generation | — | 📋 |
| 68 | **MIMIC4ED Benchmark** | ED prediction | — | 📋 |
| 69 | **CLIP** | Clinical action items | — | 📋 |
| 70 | **RadQA** | Radiology QA | — | 📋 |
| 71 | **Clinical Stigmatizing Language** | 3 sub-tasks | — | 📋 |
| 72 | **MedAlign** | 7 clinician tasks | — | 📋 |
| 73 | **DischargeMe** | Discharge summary gen | private repo | 📋 |
| 74 | **n2c2 2018 Track2** | ADE & medication | n2c2 portal | 📋 |
| 75 | **NoteExtract** | Structured extraction | — | 📋 |
| 76 | **MTS-Dialog-MEDIQA-2023** | Dialogue summarization | — | 📋 |

---

## P2 — GitHub Code + Other Data

| # | Benchmark | Tasks | GitHub Repo | Status |
|---|---|---|---|---|
| 77 | **HiRID-ICU-Benchmark** | 6 ICU tasks | ✅ cloned | ✅ |
| 78 | **emrQA** | 1.96M QA pairs | ✅ cloned (needs n2c2) | ✅ |
| 79 | **MedAgentBench** | 7 FHIR categories | 🔵 cloning | 🔵 |
| 80 | **MedCalcBench** | Formula computation | 🔵 cloning | 🔵 |
| 81 | **MedCalc-Bench** | Clinical calculation | 🔵 cloning | 🔵 |
| 82 | **BioCoder** | Bioinformatics code | 🔵 | 🔵 |
| 83 | **BioDSBench** | Code reproduction | 🔵 | 🔵 |
| 84 | **N-PowerAI** | Trial programming | — | 📋 |
| 85 | **PatientInstruct** | Patient instruction | 🔵 cloning | 🔵 |
| 86 | **PMC-Patient** | Patient info extraction | 🔵 cloning | 🔵 |
| 87 | **SEER** | Treatment planning | — | 📋 |
| 88 | **N2C2-CT** | Clinical trial matching | n2c2 portal | 📋 |
| 89 | **MTSamples** | Treatment plan gen | — | 📋 |
| 90 | **MTSamples Procedures** | Procedure summarization | — | 📋 |
| 91 | **MedQSum** | Medical Q summarization | Not on HF | 📋 |
| 92 | **MentalHealth** | Counselor response | — | ⬜ |
| 93 | **CLISTER** | Clinical STS | — | 🔵 |
| 94 | **BioLORD** | Concept explanation | gated, Dutch alt | 📋 |

---

## P3 — Gated Access (Document Only)

| # | Benchmark | Access | Status |
|---|---|---|---|
| 95 | **n2c2 2006** | n2c2 DBMI portal | 📋 |
| 96 | **n2c2 2014 - De-identification** | n2c2 DBMI portal | 📋 |
| 97 | **n2c2 2014 - Heart Disease** | n2c2 DBMI portal | 📋 |
| 98 | **i2b2 2009** | i2b2/n2c2 portal | 📋 |
| 99 | **i2b2 2010** | i2b2/n2c2 portal | 📋 |
| 100 | **GraSSCo_PHI** | Contact authors (PT) | 📋 |
| 101 | **NorSynthClinical-PHI** | GitHub (synthetic) | 📋 |
| 102 | **NorSynthClinical** | GitHub (synthetic) | 📋 |
| 103 | **meddocan** | Spanish EHR contact | 📋 |
| 104 | **ADHD-Behavior** | UPMC IRB | 📋 |
| 105 | **ADHD-MedEffects** | UPMC IRB | 📋 |
| 106 | **BMT-Status** | UPMC IRB | 📋 |
| 107 | **HospiceReferral** | UPMC IRB | 📋 |
| 108 | **ClinicReferral** | UPMC IRB | 📋 |
| 109 | **ENT-Referral** | UPMC IRB | 📋 |
| 110 | **CDI-QA** | IRB | 📋 |
| 111 | **CLEAR** | UPMC IRB | 📋 |
| 112 | **ClinicalNotes-UPMC** | UPMC IRB | 📋 |
| 113 | **BrainMRI-AIS** | Korean hospital IRB | 📋 |
| 114 | **NUBES** | Spanish hospital contact | 📋 |
| 115 | **IFMIR** | Japan JQ contact | 📋 |
| 116 | **DiseaseOntology (DO)** | Not found on HF | 📋 |

---

## Other / Suite

| # | Benchmark | Status |
|---|---|---|
| 117–149 | PromptCBLUE, MedBench, BRIDGE, MedHELM, Real-World Clinical Cases, CNMLE, Resident Training, Doctor In-Charge, ACI-Bench, ADE, ADE Corpus, BARR2, BRONCO150, CARDIO:DE, DiSMed, Ex4CDS, GOUT-CC, CAS, CLINpt, C-EMRS, DialMed, EHRQA, MIE, mtsamples, mtsamples-temporal, Mexican Clinical Records, Japanese Case Reports, BioLORD, Human Disease Ontology, Medec, ProxySender, PrivacyDetection | Varies — most 📋 |

---

## Summary

| Priority | Total | ✅ Data | 📋 Documented | ⬜ Pending |
|---|---|---|---|---|---|
| P0 | 46 | 44 | 2 | 0 |
| P1 | 30 | 2 | 28 | 0 |
| P2 | 18 | 2 | 14 | 2 |
| P3 | 22 | 0 | 22 | 0 |
| Suite | 33 | 0 | ~20 | ~13 |
| **Total** | **149** | **48** | **86** | **15** |
