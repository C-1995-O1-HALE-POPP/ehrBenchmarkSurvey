# Benchmark Summary for *EHR-R1: A Reasoning-Enhanced Foundational Language Model*

Source paper: [arXiv:2510.25628](https://arxiv.org/pdf/2510.25628)

This document summarizes the benchmarks used in the paper in a survey-friendly Markdown format. It follows the style of the provided reference file, but adds a short normalization note:

- The paper gives benchmark-level descriptions and one-line task instructions.
- The `Input` and `Output` blocks below are normalized survey-style rewrites so the entries match a consistent benchmark catalog format.
- For `EHR-Bench`, the PDF appendix has a few line-wrap / alignment issues. Task names are standardized mainly according to Supplementary Table 3, while the corresponding instructions are mapped from Supplementary Table 4 by semantic alignment.

---

## 1. EHR-Bench

EHR-Bench is a benchmark introduced by the paper and derived from MIMIC-IV. It is the primary in-distribution evaluation benchmark for the proposed model. The benchmark spans 42 tasks across 12 subtypes and two major task families: decision making and risk prediction. The authors first transform structured MIMIC-IV hospital events into Markdown-like free text, then create a patient-level split to avoid leakage between train and test. The final benchmark contains 21K test samples. The benchmark covers longitudinal hospital decision support scenarios such as next-step admissions, transfers, diagnoses, tests, procedures, medications, and ICU events, as well as risk prediction problems such as mortality, readmission, ICU transfer, emergency reattendance, and length of stay.

- **Language:** English (inferred from the U.S. source EHR systems; not explicitly stated in the paper)  
- **Clinical Stage:** Longitudinal hospital course, including ED visit, admission, diagnosis, treatment, ICU care, discharge, and post-discharge outcome prediction  
- **Source Clinical Document Type:** Structured MIMIC-IV EHR events serialized into Markdown-like free text  
- **Clinical Specialty:** Multi-specialty inpatient care, emergency medicine, intensive care, laboratory medicine, radiology, and pharmacy  
- **Application Method:** Benchmark introduced in the paper; derived from MIMIC-IV with patient-level split and test-set construction described in Section 4.2.1  

---

## 1.1 Task: EHR-Bench-Admissions

This task predicts the next admission-related event from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Admissions suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Admission suggestion item(s)]
```

---

## 1.2 Task: EHR-Bench-Transfer

This task predicts the next transfer-related event from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Transfers suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Transfer suggestion item(s)]
```

---

## 1.3 Task: EHR-Bench-OMR

This task predicts the next online medical record (OMR) item suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Online Medical Record suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[OMR item suggestion(s)]
```

---

## 1.4 Task: EHR-Bench-Labevents

This task predicts the next laboratory test event suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Labotary Test Events suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Laboratory test event suggestion(s)]
```

---

## 1.5 Task: EHR-Bench-Microbiologyevents

This task predicts the next microbiology test event suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Microbiology Test Events suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Microbiology test event suggestion(s)]
```

---

## 1.6 Task: EHR-Bench-Radiology

This task predicts the next radiology examination suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Radiology Examinations suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Radiology examination suggestion(s)]
```

---

## 1.7 Task: EHR-Bench-Diagnose ICD

This task predicts the next diagnosis suggestion at ICD granularity from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Diagnoses International Classification of Diseases Item suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Diagnosis suggestion item(s) at ICD granularity]
```

---

## 1.8 Task: EHR-Bench-Diagnose CCS

This task predicts the next diagnosis suggestion at CCS granularity from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Diagnoses Clinical Classifications Software Item suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Diagnosis suggestion item(s) at CCS granularity]
```

---

## 1.9 Task: EHR-Bench-Diagnosis ICD

This task predicts the next ED diagnosis suggestion at ICD granularity from the prior event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next ED Diagnoses on International Classification of Diseases suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[ED diagnosis suggestion item(s) at ICD granularity]
```

---

## 1.10 Task: EHR-Bench-Diagnosis CCS

This task predicts the next ED diagnosis suggestion at CCS granularity from the prior event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next ED Diagnoses on Clinical Classifications Software Item suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[ED diagnosis suggestion item(s) at CCS granularity]
```

---

## 1.11 Task: EHR-Bench-Procedures ICD

This task predicts the next procedure suggestion at ICD granularity from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Procedures International Classification of Diseases Item suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Procedure suggestion item(s) at ICD granularity]
```

---

## 1.12 Task: EHR-Bench-Procedures CCS

This task predicts the next procedure suggestion at CCS granularity from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Procedures Clinical Classifications Software Item suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Procedure suggestion item(s) at CCS granularity]
```

---

## 1.13 Task: EHR-Bench-Services

This task predicts the next service suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Services suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Service suggestion item(s)]
```

---

## 1.14 Task: EHR-Bench-POE

This task predicts the next provider order entry suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Provider Order Entry suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Provider order entry suggestion item(s)]
```

---

## 1.15 Task: EHR-Bench-EMAR

This task predicts the next electronic medication administration record suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Electronic Medicine Administration Record suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[EMAR suggestion item(s)]
```

---

## 1.16 Task: EHR-Bench-Prescriptions

This task predicts the next prescription suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Prescriptions suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Prescription suggestion item(s)]
```

---

## 1.17 Task: EHR-Bench-Prescriptions ATC

This task predicts the next prescription suggestion at ATC granularity from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Anatomical Therapeutic Chemical Classification Prescriptions suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Prescription suggestion item(s) at ATC granularity]
```

---

## 1.18 Task: EHR-Bench-Medrecon

This task predicts the next ED medication reconciliation suggestion from the prior event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next ED Medrecon suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[ED medication reconciliation suggestion item(s)]
```

---

## 1.19 Task: EHR-Bench-Medrecon ATC

This task predicts the next ED medication reconciliation suggestion at ATC granularity from the prior event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next ED Medrecon on Anatomical Therapeutic Chemical (ATC) Classification suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[ED medication reconciliation suggestion item(s) at ATC granularity]
```

---

## 1.20 Task: EHR-Bench-Ingredientevents

This task predicts the next ICU ingredient event suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Ingredient Events suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Ingredient event suggestion item(s)]
```

---

## 1.21 Task: EHR-Bench-Datetimeevents

This task predicts the next ICU datetime event suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Datetime Events suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Datetime event suggestion item(s)]
```

---

## 1.22 Task: EHR-Bench-Procedureevents

This task predicts the next ICU procedure event suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Procedure Events suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Procedure event suggestion item(s)]
```

---

## 1.23 Task: EHR-Bench-Inputevents

This task predicts the next ICU input event suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Input Events suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Input event suggestion item(s)]
```

---

## 1.24 Task: EHR-Bench-Outputevents

This task predicts the next ICU output event suggestion from the prior hospital event sequence.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Output Events suggestion for the patient.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
[Output event suggestion item(s)]
```

---

## 1.25 Task: EHR-Bench-ED Hospitalization

This task predicts whether a patient will be hospitalized after an emergency department visit.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will be hospitalized after the emergency room visit.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.26 Task: EHR-Bench-ED ICU Transfer 12Hour

This task predicts whether a patient will be transferred to the ICU within 12 hours after the emergency room visit.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will be transferred to the ICU within 12 hours after the emergency room.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.27 Task: EHR-Bench-ED Critical Outcomes

This task predicts whether a patient will either die during hospitalization or be transferred to the ICU within 12 hours after the emergency room visit.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die during hospitalization or will be transferred to the ICU within 12 hours after the emergency room.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.28 Task: EHR-Bench-Readmission 30Day

This task predicts whether a patient will be readmitted to the hospital within 30 days.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will be readmitted to the hospital within 30 days.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.29 Task: EHR-Bench-Readmission 60Day

This task predicts whether a patient will be readmitted to the hospital within 60 days.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will be readmitted to the hospital within 60 days.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.30 Task: EHR-Bench-ICU Readmission

This task predicts whether a patient will be admitted to the ICU again during the same hospitalization.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will be admitted to the ICU again during this hospitalization.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.31 Task: EHR-Bench-ED Reattendance 3Day

This task predicts whether a patient will return to the emergency department within 72 hours after the emergency visit.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will return to the emergency department within 72 hours after the emergency visit.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.32 Task: EHR-Bench-LengthOfStay 3Day

This task predicts whether the patient's hospital stay will exceed 3 days.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient's hospital stay will exceed 3 days.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.33 Task: EHR-Bench-LengthOfStay 7Day

This task predicts whether the patient's hospital stay will exceed 7 days.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient's hospital stay will exceed 7 days.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.34 Task: EHR-Bench-ICU Stay 7Day

This task predicts whether the patient will stay in the ICU for more than 7 days.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will stay in the ICU for more than 7 days.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.35 Task: EHR-Bench-ICU Stay 14Day

This task predicts whether the patient will stay in the ICU for more than 14 days.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will stay in the ICU for more than 14 days.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.36 Task: EHR-Bench-ED Inpatient Mortality

This task predicts whether a patient seen in the emergency department will die during the ensuing hospitalization.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die during hospitalization.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.37 Task: EHR-Bench-Inpatient Mortality

This task predicts whether a patient will die during hospitalization.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die during hospitalization.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.38 Task: EHR-Bench-ICU Mortality 1Day

This task predicts whether a patient will die within 1 day in the ICU setting.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die within 1 day.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.39 Task: EHR-Bench-ICU Mortality 2Day

This task predicts whether a patient will die within 2 days in the ICU setting.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die within 2 day.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.40 Task: EHR-Bench-ICU Mortality 3Day

This task predicts whether a patient will die within 3 days in the ICU setting.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die within 3 day.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.41 Task: EHR-Bench-ICU Mortality 7Day

This task predicts whether a patient will die within 7 days in the ICU setting.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die within 7 day.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.42 Task: EHR-Bench-ICU Mortality 14Day

This task predicts whether a patient will die within 14 days in the ICU setting.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will die within 14 day.
### Input
[Chronologically formatted hospital event sequence in Markdown-like free text]
### Output
yes / no
```

---

## 1.43 EHR-Bench Notes

- The paper reports 24 decision-making tasks and 18 risk-prediction tasks, for 42 tasks in total.
- Decision-making tasks are evaluated with **F1** as multi-label generation / entity recommendation problems.
- Risk-prediction tasks are evaluated with **AUROC** as binary classification problems.
- The benchmark uses a patient-level split and limits the observable history to a 24-hour window, with samples containing 10 to 100 historical events.
- The free-text input is not an original clinical note; it is a Markdown serialization of structured EHR events.

---

## 2. MIMIC-IV-CDM

MIMIC-IV-CDM is an external generalization benchmark used in the paper. It is also derived from MIMIC-IV, but it uses a different preprocessing pipeline and task formulation from EHR-Bench. Unlike EHR-Bench, the context is not organized as a chronological timeline; instead, the benchmark keeps the most recent information for each event type. The paper uses it to test whether the model generalizes across a domain shift in EHR task design. The benchmark focuses on diagnostic accuracy for four diseases: appendicitis, cholecystitis, diverticulitis, and pancreatitis. Two diagnostic granularities are evaluated: main disease diagnosis and ICD-level diagnosis.

- **Language:** English (inferred from the U.S. source EHR system; not explicitly stated in the paper)  
- **Clinical Stage:** Diagnostic workup during hospital visit  
- **Source Clinical Document Type:** Structured MIMIC-IV EHR events reformatted into Markdown-like free text without chronological timestamps  
- **Clinical Specialty:** Acute care / hospital medicine, with emphasis on abdominal disease diagnosis  
- **Application Method:** Public benchmark reused in the paper and reformatted by the authors into Markdown-style free text for LLM evaluation  

---

## 2.1 Task: MIMIC-IV-CDM-Main Disease Diagnoses

This task predicts the patient's main disease diagnosis among the benchmark's target diseases.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the main Diagnoses of Diseases Item suggestion for the patients.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
[Main disease diagnosis suggestion]
```

---

## 2.2 Task: MIMIC-IV-CDM-ICD Code Diagnoses

This task predicts the patient's diagnosis at ICD-code granularity.

### Task type
Decision Making

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please give the next Diagnoses in International Classification of Diseases Item suggestion for the patients.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
[ICD-level diagnosis suggestion(s)]
```

---

## 2.3 MIMIC-IV-CDM Notes

- The paper uses this benchmark to test generalization across task formulation rather than across institution.
- The benchmark is still MIMIC-IV-based, but it differs from EHR-Bench because it uses the most recent event information rather than a chronological event stream.
- In this paper, MIMIC-IV-CDM is evaluated with **F1**.

---

## 3. EHRSHOT

EHRSHOT is the paper's out-of-distribution benchmark for testing generalization to a different healthcare system. It is a public dataset from Stanford Medicine and includes EHR data from 7,000 patients in its public portion. The paper evaluates 14 risk-prediction tasks in three subtypes: operational outcomes, anticipating lab test results, and assignment of new diagnoses. Because the original benchmark uses many medical codes directly, the authors convert the data into Markdown-like free text, use descriptive mappings for codes, manually repair some unmapped code systems, and enrich the most frequent measurement and observation items with units, normal ranges, and anomaly indicators.

- **Language:** English (inferred from Stanford Medicine EHR data; not explicitly stated in the paper)  
- **Clinical Stage:** Longitudinal hospital outcome prediction and future diagnosis risk prediction  
- **Source Clinical Document Type:** Structured Stanford EHR data converted into Markdown-like free text with code-to-text mapping and lab/observation enrichment  
- **Clinical Specialty:** Multi-specialty longitudinal EHR benchmark, covering operational outcomes, lab tests, and new diagnoses  
- **Application Method:** Public benchmark reused in the paper and reformatted by the authors for LLM-based zero-shot and few-shot evaluation  

---

## 3.1 Task: EHRSHOT-Length of Stay

This task predicts whether a patient's total hospital length of stay will be at least 7 days.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether a patient's total length of stay during a visit to the hospital will be at least 7 days.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.2 Task: EHRSHOT-Readmission

This task predicts whether a patient will be re-admitted to the hospital within 30 days after discharge.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether a patient will be re-admitted to the hospital within 30 days after being discharged from a visit.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.3 Task: EHRSHOT-ICU Transfer

This task predicts whether a patient will be transferred to the ICU during the hospital visit.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether a patient will be transferred to the ICU during a visit to the hospital.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.4 Task: EHRSHOT-Anemia

This task predicts whether an anemia lab result will come back as normal.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether an anemia lab comes back as normal (>=120 g/L).
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.5 Task: EHRSHOT-Hyperkalemia

This task predicts whether a hyperkalemia-related lab result will come back as normal.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether a hyperkalemia lab comes back as normal(<=5.5 mmol/L).
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.6 Task: EHRSHOT-Hyponatremia

This task predicts whether a hyponatremia-related lab result will come back as normal.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether a hyponatremia lab comes back as normal (>=135 mmol/L).
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.7 Task: EHRSHOT-Hypoglycemia

This task predicts whether a hypoglycemia-related lab result will come back as normal.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether a hypoglycemia lab comes back as normal (>=3.9 mmol/L).
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.8 Task: EHRSHOT-Thrombocytopenia

This task predicts whether a thrombocytopenia-related lab result will come back as normal.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether a thrombocytopenia lab comes back as normal (>=150 10^9/L).
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.9 Task: EHRSHOT-Acute MI

This task predicts whether the patient will receive a first diagnosis of acute myocardial infarction within the next year.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will have his first diagnosis of an acute myocardial infarction within the next year.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.10 Task: EHRSHOT-Celiac

This task predicts whether the patient will receive a first diagnosis of celiac disease within the next year.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will have his first diagnosis of celiac disease within the next year.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.11 Task: EHRSHOT-Hyperlipidemia

This task predicts whether the patient will receive a first diagnosis of hyperlipidemia within the next year.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will have his first diagnosis of hyperlipidemia within the next year.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.12 Task: EHRSHOT-Hypertension

This task predicts whether the patient will receive a first diagnosis of essential hypertension within the next year.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will have his first diagnosis of essential hypertension within the next year.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.13 Task: EHRSHOT-Lupus

This task predicts whether the patient will receive a first diagnosis of lupus within the next year.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will have his first diagnosis of lupus within the next year.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.14 Task: EHRSHOT-Pancan

This task predicts whether the patient will receive a first diagnosis of pancreatic cancer within the next year.

### Task type
Risk Prediction

```md
### Instruction
Given the sequence of events that have occurred in a hospital, please predict whether the patient will have his first diagnosis of pancreatic cancer within the next year.
### Input
[Hospital EHR context reformatted as Markdown-like free text]
### Output
yes / no
```

---

## 3.15 EHRSHOT Notes

- The benchmark contains 14 risk-prediction tasks across three subtypes: operational outcomes, anticipating lab test results, and assignment of new diagnoses.
- In this paper, EHRSHOT is used for both zero-shot and few-shot generalization evaluation.
- The paper reports **AUROC** for EHRSHOT.
- Compared with EHR-Bench and MIMIC-IV-CDM, EHRSHOT introduces an institutional domain shift because it comes from Stanford Medicine rather than MIMIC-IV.

