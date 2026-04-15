<!-- paper_key: "2025_medagentgym_a_scalable_agentic_training_environment_for_code_centric_reasoning_in_biomedical_data_science" -->
<!-- paper_url: "https://arxiv.org/abs/2506.04405" -->
<!-- generated_on: "2026-04-15" -->

# Benchmark Summary for *MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science*

Source paper: [https://arxiv.org/abs/2506.04405](https://arxiv.org/abs/2506.04405)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-15`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2025_medagentgym_a_scalable_agentic_training_environment_for_code_centric_reasoning_in_biomedical_data_science/source.pdf`](../papers/2025_medagentgym_a_scalable_agentic_training_environment_for_code_centric_reasoning_in_biomedical_data_science/source.pdf)
- Extracted text: [`../papers/2025_medagentgym_a_scalable_agentic_training_environment_for_code_centric_reasoning_in_biomedical_data_science/source.txt`](../papers/2025_medagentgym_a_scalable_agentic_training_environment_for_code_centric_reasoning_in_biomedical_data_science/source.txt)
- The paper proposes one new integrated benchmark/training environment (`MedAgentGym`) and evaluates on 11 reused public benchmarks/datasets embedded in this environment.
- Normalization assumption: because this paper is organized by dataset domains and executable prompts (Appendix C/G) rather than a single fixed natural-language task list, each included benchmark is mapped to one representative survey task with normalized `Instruction/Input/Output`.
- In-distribution and out-of-distribution roles are taken from Section 5.1 and Appendix C.2/C.3.
- Verifier pass (`2026-04-15`, rerun with updated workflow):
  - Benchmark existence: all 12 benchmark names are explicitly listed in Section 5.1 / Appendix C.
  - Task mapping: 12 task sections are normalized domain-level mappings; this normalization is explicit in Workflow Notes.
  - Example fidelity: task examples are taken from Appendix G prompt blocks and Figure 16/17 when available; where no explicit full worked input-output example exists, the summary explicitly states the absence.
  - Scoring fidelity: scoring blocks are grounded in the paper's metric definitions (Section 4.1 and Appendix E), using SR as primary metric, exact match for explicit-ground-truth database/data-science/bioinformatics tasks, and Acc for open-ended ML tasks.
  - Judge prompt fidelity: all task sections explicitly state that full judge prompts are not provided; no LLM-judge full prompt is fabricated.
  - Inference labeling: normalized/inferred fields remain explicitly marked in benchmark metadata and Workflow Notes.

## 1. MedAgentGym

MedAgentGym is an English-first coding-centric biomedical reasoning benchmark and interactive training environment introduced by the paper. It contains about 72,413 executable task instances across 129 categories from 12 real-world biomedical scenarios, with both full-scale and lightweight leaderboard subsets. The framework unifies structured and open-ended biomedical coding tasks, supports isolated Docker execution, and uses verifiable outputs for automated scoring. Evaluation in the paper covers 8 in-distribution datasets and 4 out-of-distribution datasets under a shared agent scaffold.

- **Language:** English (task prompts are English; dataset contents vary by source benchmark)
- **Clinical Stage:** Mixed clinical and biomedical data science stages (database querying, note verification, medical computation, predictive modeling, biostatistics)
- **Source Clinical Document Type:** Mixed; structured EHR tables serialized for coding tasks, clinical notes, FHIR API interaction traces, and biomedical analysis datasets
- **Clinical Specialty:** Multi-specialty
- **Application Method:** Benchmark introduced in the paper (with public benchmark/training resources release)

---

## 1.1 Task: Clinical Database Querying

This task is to generate executable code (typically SQL-oriented workflows) that answers clinical questions from structured EHR databases.

### Task type
Code Generation + Executable Verification

```md
### Instruction
Given an EHR coding problem and linked clinical tables, write code that derives a concrete answer by generating correct executable queries and returning the final result.
### Input
[Natural-language clinical question, table schema/context, and data directory or database path]
### Output
[Executable code and final answer consistent with ground-truth execution result]
```

### Task example

```md
### Example
Normalized from Appendix G.1 (MIMIC-III Prompt - Main): "You are a biomedical expert in handling EHR data... solve a coding problem with given EHR data... finally give a concrete answer to the question."
This summary task is a normalized mapping for the paper's "clinical database querying" domain (MIMIC-III/eICU/TREQS/EHR-SeqSQL) rather than one standalone benchmark-native task.
```

### Scoring standard

```md
### Scoring
Primary metric is Success Rate (SR). For database tasks with explicit reference outputs, the paper compares executed outputs with references using exact match.
### Evaluation Dimensions
- Session-level success under the benchmark protocol (max 15 interaction turns and 120-second runtime budget).
- Exact-match correctness of execution output against reference solution when explicit ground truth is available.
- Overall leaderboard score is the average across test tasks.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation is metric-based (SR + exact match), not an LLM-as-a-judge rubric.
```

---

## 1.2 Task: Clinical Note Consistency Checking

This task is to verify whether unstructured clinical notes are consistent with structured EHR records and report detected discrepancies.

### Task type
Code Generation + Classification

```md
### Instruction
Given structured EHR records and associated notes, write code that checks cross-source consistency and outputs discrepancy-related results in the required format.
### Input
[Structured database records, note file, and task-specific inconsistency targets]
### Output
[Executable verification code and inconsistency outputs such as counts or binary inconsistency indicators]
```

### Task example

```md
### Example
Normalized from Appendix G.10 (EHRCon Prompt - Part II): tasks provide a database location "{db_location}" and a clinical note CSV "{note_csv}" and require consistency checking between structured records and note text.
No explicit task-specific worked input-output pair is provided in the paper or appendix for this normalized MedAgentGym domain task.
```

### Scoring standard

```md
### Scoring
The paper reports Success Rate (SR) as the primary metric. Task-level scoring for note-consistency tasks is not separately formalized; the benchmark uses executable outcome verification under the shared SR protocol.
### Evaluation Dimensions
- Whether the agent completes the consistency-check objective within interaction/runtime constraints.
- Whether returned outputs satisfy benchmark-required executable/format constraints.
- Aggregate performance is reported through SR and averaged benchmark scores.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. The reported evaluation is not rubric-based LLM judging.
```

---

## 1.3 Task: Medical Computation from Notes

This task is to extract relevant values from patient notes and compute clinical scores or dose-related quantities via code.

### Task type
Code Generation + Numeric Prediction

```md
### Instruction
Given a patient-specific clinical scenario, write Python code to compute the requested medical value and print the final answer.
### Input
[Clinical note text and a target medical calculation query]
### Output
[Executable Python code and computed numeric answer]
```

### Task example

```md
### Example
From Figure 17 (MedCalcBench case): "Using the 2021 CKD-EPI Creatinine equation, what is the patient's Glomerular Filtration Rate (GFR)...? Answer with a decimal number..."
The figure contrasts an incorrect MDRD implementation with a correct CKD-EPI implementation.
```

### Scoring standard

```md
### Scoring
Primary metric is Success Rate (SR). For structured tasks with explicit references, code execution outputs are evaluated by exact match against reference solutions.
### Evaluation Dimensions
- Correct executable implementation of the requested clinical formula.
- Exact-match agreement of produced output with the reference solution where defined.
- Successful completion under benchmark interaction/runtime limits.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation uses deterministic metrics (SR + exact match), not LLM judge rubrics.
```

---

## 1.4 Task: FHIR Workflow Agent Execution

This task is to use programmatic FHIR interactions to complete realistic EHR workflow requests.

### Task type
Code Generation + Tool-use Planning

```md
### Instruction
Given a clinical workflow question and available FHIR function descriptions, write Python code that performs necessary GET/POST interactions and returns final answers in the required JSON-loadable format.
### Input
[Workflow question, FHIR API base URL, function descriptions, answer-format specification]
### Output
[Executable Python script and structured final answers for requested GET/POST tasks]
```

### Task example

```md
### Example
MedAgentBench Prompt – Part I
You are an expert in using FHIR functions to assist medical professionals .
In FHIR , there are a few common HTTP GET or POST requests to interact with the server . The descriptions of requests are listed here : { fhir_function_description }.
You are given a question and a set of possible functions .
Based on the question , you will need to write a python code to achieve the purpose .
1. Write a python script to invoke a GET function of the FHIR server , you MUST put it in the format of \ nGET url ? param_name1 = param_value1 & param_name2 = param_value2 ...
2. Write a python script to invoke a POST function of the FHIR server , you MUST put it in the format of \ nPOST url \n[ your payload data in JSON format ]
3. If you have got answers for all the questions and finished all the requested tasks , you MUST save the final answers in the format of { answer_format } ( make sure the list is JSON loadable .)

MedAgentBench Prompt – Part II
You SHOULD NOT include any other text in the response .
Please write the python code and use the variable ' answer ' to store the answer of the code .
Question : { question }\ n. The FHIR server base URL is { fhir_api_base }. Do not directly write the GET and POST requests .

MedAgentBench Prompt – Answer Format
answer = {" GET ": ["60" ," S2874099 "] , " POST ": [" http :// localhost :8080/ fhir / Observation ", " payload ]}
The answers to the questions are listed in " GET " instead of the get commands , while the post url and payload are listed in " POST ".
```

### Scoring standard

```md
### Scoring
The paper reports SR as primary metric. Task-level metric details specific to MedAgentBench are not separated; completion is evaluated through executable workflow success in the unified benchmark protocol.
### Evaluation Dimensions
- Correct workflow completion with required GET/POST interactions and answer format.
- Runnable code and valid structured output according to task constraints.
- Session success under global runtime/turn limits.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. The published evaluation does not provide an LLM-as-a-judge rubric prompt.
```

---

## 1.5 Task: Bioinformatics Software Coding

This task is to implement functionally correct bioinformatics algorithms or scientific programming solutions with testable behavior.

### Task type
Code Generation + Unit-test Verification

```md
### Instruction
Given a bioinformatics programming prompt and function signature, write a correct Python function that satisfies the provided test or expected-output conditions.
### Input
[Problem description, required function signature, optional context code/test cases]
### Output
[Python function implementation that passes verification checks]
```

### Task example

```md
### Example
Biocoder Prompt
You are an biomedical expert in writing bioinformatics code and answer questions accordingly .
Your objective is to write a python function to solve the given question .
Please only write the function , do not include any other text .
Please write a Python function with the following signature :
{ signature }
```

### Scoring standard

```md
### Scoring
Primary metric is SR. For bioinformatics tasks with explicit references, the paper evaluates execution outputs by exact match to reference solutions.
### Evaluation Dimensions
- Functional correctness of generated code under executable verification.
- Exact-match agreement of produced output with reference when available.
- Session-level success under benchmark runtime/interaction constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation is metric-based (SR + exact match).
```

---

## 1.6 Task: Biomedical Data Analysis Reproduction

This task is to generate analysis code that reproduces biomedical research-style workflows over provided datasets.

### Task type
Code Generation + Workflow Reproduction

```md
### Instruction
Given a biomedical data analysis task and data path, write code that executes the required analysis workflow and produces verifiable task outputs.
### Input
[Task description, dataset directory, and task-specific analysis requirements]
### Output
[Executable analysis code and task-compliant outputs]
```

### Task example

```md
### Example
From Figure 16 (BioDSBench case): "Using the provided function check_reaction_consistency, identify mass-imbalanced reactions... and compute a valid integer mass assignment..."
The figure compares incorrect and correct implementations for this optimization task.
```

### Scoring standard

```md
### Scoring
Primary metric is SR. For data-science tasks with explicit ground truths, execution outputs are compared to references using exact match.
### Evaluation Dimensions
- Correct implementation of required analysis workflow.
- Exact-match of execution output against reference solutions when provided.
- Successful completion within shared interaction/runtime constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Reported scoring is deterministic (SR + exact match), not LLM judge scoring.
```

---

## 1.7 Task: EHR Predictive Modeling

This task is to train ML/DL models on longitudinal EHR features and output task-specific predictions in the required CSV format.

### Task type
Risk Prediction + Code Generation

```md
### Instruction
Given train/validation/test features and labels for an EHR prediction task, write runnable ML/DL code to optimize predictive performance and save test predictions to the specified output file format.
### Input
[Feature and label directories, task name, prediction schema requirements]
### Output
[Executable model-training/inference code and prediction CSV]
```

### Task example

```md
### Example
Normalized from Appendix G.8/G.11-style ML prompt format: prediction file must be a CSV such as
patient_id,prediction
115967096,8192
No explicit task-specific worked prediction instance with a released gold output is provided in the paper appendix for this normalized MedAgentGym domain task.
```

### Scoring standard

```md
### Scoring
For open-ended ML tasks in clinical decision support, the paper evaluates performance with Accuracy (Acc) across provided test cases; SR remains the benchmark-level primary aggregate metric.
### Evaluation Dimensions
- Accuracy of model predictions on provided test labels.
- Valid generation of required prediction file format.
- Session-level completion under benchmark execution constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation uses deterministic task metrics (Acc/SR), not LLM-as-a-judge scoring.
```

---

## 1.8 Task: Biostatistical Power and Sample Size Analysis

This task is to solve statistical design problems in biomedical research by generating precise numeric outputs through code.

### Task type
Code Generation + Statistical Reasoning

```md
### Instruction
Given a biomedical statistics scenario, write code that computes requested quantities such as sample size or power under task constraints and returns precise final values.
### Input
[Statistical problem statement and required design parameters]
### Output
[Executable statistical code and final numeric result]
```

### Task example

```md
### Example
NPowerAI Prompt
You are a scientist conducting biomedical research and constantly facing statistical problems . Sometimes , you need to find the minimum sample size to achieve a specific power . In other times , you would like to know the statistical power given a population size .
```

### Scoring standard

```md
### Scoring
Primary metric is SR. For structured tasks with explicit references, executed outputs are compared to reference solutions via exact match.
### Evaluation Dimensions
- Correct statistical computation aligned with problem constraints.
- Exact-match agreement with reference numeric output when available.
- Completion within benchmark interaction/runtime constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. The scoring described in the paper is deterministic (SR + exact match), not LLM judge based.
```

---

## 2. EHRSQL

EHRSQL is a reused text-to-SQL benchmark integrated into MedAgentGym as in-distribution clinical database querying data. In this paper, EHRSQL contributes MIMIC-III and eICU question-to-query task instances and is used both for benchmarking and trajectory-based training.

- **Language:** English
- **Clinical Stage:** Longitudinal hospital/ICU data querying
- **Source Clinical Document Type:** Structured EHR tables (querying scenarios)
- **Clinical Specialty:** Multi-specialty inpatient/critical care data use
- **Application Method:** Public benchmark reused in paper (in-distribution component of MedAgentGym)

---

## 2.1 Task: Clinical Text-to-SQL Query Solving

This task is to translate clinical natural-language questions into executable SQL logic and derive correct answers from EHR databases.

### Task type
Semantic Parsing + Code Generation

```md
### Instruction
Given a clinical question and EHR table schema context, generate executable query logic and return the final answer.
### Input
[Clinical question, schema/table information, and data location]
### Output
[Executable SQL/Python query workflow and final answer]
```

### Task example

```md
### Example
MIMIC-III Prompt - Main
You are a biomedical expert in handling EHR data and answer questions .
Your objective is to solve a coding problem with given EHR data , with the goal of finally give a concrete answer to the question .
Assume you have knowledge of several tables :
(1) Tables are linked by identifiers which usually have the suffix 'ID '. For example , SUBJECT_ID refers to a unique patient , HADM_ID refers to a unique admission to the hospital , and ICUSTAY_ID refers to a unique admission to an intensive care unit .
(2) Charted events such as notes , laboratory tests , and fluid balance are stored in a series of ' events ' tables . For example the outputevents table contains all measurements related to output for a given patient , while the labevents table contains laboratory test
(3) Tables prefixed with 'd_ ' are dictionary tables and provide definitions for identifiers . For example , every row of chartevents is associated with a single ITEMID which represents the concept measured , but it does not contain the actual name of the measurement . By joining chartevents and d_items on ITEMID , it is possible to identify the concept represented by a given ITEMID .
(4) For the databases , four of them are used to define and track patient stays : admissions , patients , icustays , and transfers . Another four tables are dictionaries for cross - referencing codes against their respective definitions : d_icd_diagnoses , d_icd_procedures , d_items , and d_labitems .

MIMIC-III Prompt - Table information
For different tables , they contain the following information :
(1) ADMISSIONS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ADMITTIME , DISCHTIME , ADMISSION_TYPE , ADMISSION_LOCATION , DISCHARGE_LOCATION , INSURANCE , LANGUAGE , MARITAL_STATUS , ETHNICITY , AGE
(2) CHARTEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , ITEMID , CHARTTIME , VALUENUM , VALUEUOM
(3) COST . csv : ROW_ID , SUBJECT_ID , HADM_ID , EVENT_TYPE , EVENT_ID , CHARGETIME , COST
(4) D_ICD_DIAGNOSES . csv : ROW_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
(5) D_ICD_PROCEDURES . csv : ROW_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
(6) D_ITEMS . csv : ROW_ID , ITEMID , LABEL , LINKSTO
(7) D_LABITEMS . csv : ROW_ID , ITEMID , LABEL
(8) DIAGNOSES_ICD . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICD9_CODE
(9) ICUSTAYS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , FIRST_CAREUNIT , LAST_CAREUNIT , FIRST_WARDID , LAST_WARDID , INTIME
(10) INPUTEVENTS_CV . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , CHARTTIME , ITEMID , AMOUNT
(11) LABEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ITEMID , CHARTTIME , VALUENUM , VALUEUOM
(12) MICROBIOLOGYEVENTS . csv : RROW_ID , SUBJECT_ID , HADM_ID , CHARTTIME , SPEC_TYPE_DESC , ORG_NAME
(13) OUTPUTEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , CHARTTIME , ITEMID , VALUE
(14) PATIENTS . csv : ROW_ID , SUBJECT_ID , GENDER , DOB , DOD
(15) PRESCRIPTIONS . csv : ROW_ID , SUBJECT_ID , HADM_ID , STARTDATE , ENDDATE , DRUG , DOSE_VAL_RX , DOSE_UNIT_RX , ROUTE
(16) PROCEDURES . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICD9_CODE , CHARTTIME
(17) TRANSFERS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , EVENTTYPE , CAREUNIT , WARDID , INTIME , OUTTIME
All the tabls are saved in the data directory {}.

eICU Prompt – Main
You are a biomedical expert in handling EHR data and answer questions .
Your objective is to solve a coding problem with given EHR data , with the goal of finally give a concrete answer to the question .
Assume you have knowledge of several tables :
(1) Tables are linked by identifiers whose name usually ends 'ID '. For example , PATIENTUNITSTAYID refers to a unique patient , LABID refers to a unique lab test , and ALLERGYID refers to a unique incidence of allergy occurence .
(2) Four tables are related to measurements . First , the lab table contains laboratory measurements of chemicals such as chloride or albumin . Secondly , the intake and output ( intakeoutput ) table records all fluid - related measurements such as administered normal saline ( ns ) and urination . Thirdly , the microlab table records measurements of culture of microorganisms . Fourth , the vitalperiod table describes the patients ' vitals during their stay .
(3) The remaining tables ( allergy , cost , diagnosis , medication , patient and treatment ) contain other critical information , and the table names are self - explanatory .
{ EHR_tables }

eICU Prompt – Table Information
For different tables , they contain the following information :
(1) allergy . csv : ALLERGYID , PATIENTUNITSTAYID , DRUGNAME , ALLERGYNAME , ALLERGYTIME
(2) cost . csv : COSTID , UNIQUEPID , PATIENTHEALTHSYSTEMSTAYID , EVENTTYPE , EVENTID , CHARGETIME , COST
(3) diagnosis . csv : DIAGNOSISID , PATIENTUNITSTAYID , ICD9CODE , DIAGNOSISNAME , DIAGNOSISTIME
(4) intakeoutput . csv : INTAKEOUTPUTID , PATIENTUNITSTAYID , CELLPATH , CELLLABEL , CELLVALUENUMERIC , INTAKEOUTPUTTIME
(5) lab . csv : LABID , PATIENTUNITSTAYID , LABNAME , LABRESULT , LABRESULTTIME
(6) medication . csv : MEDICATIONID , PATIENTUNITSTAYID , DRUGNAME , DOSAGE , ROUTEADMIN , DRUGSTARTTIME , DRUGSTOPTIME
(7) microlab . csv : MICROLABID , PATIENTUNITSTAYID , CULTURESITE , ORGANISM , CULTURETAKENTIME
(8) patient . csv : PATIENTUNITSTAYID , PATIENTHEALTHSYSTEMSTAYID , GENDER , AGE , ETHNICITY , HOSPITALID , WARDID , ADMISSIONHEIGHT , HOSPITALADMITSOURCE , HOSPITALDISCHARGESTATUS , ADMISSIONWEIGHT , DISCHARGEWEIGHT , UNIQUEPID , HOSPITALADMITTIME , UNITADMITTIME , UNITDISCHARGETIME , HOSPITALDISCHARGETIME
(9) treatment . csv : TREATMENTID , PATIENTUNITSTAYID , TREATMENTNAME , TREATMENTTIME
(10) vitalperiod . csv : VITALPERIODICID , PATIENTUNITSTAYID , TEMPERATURE , SAO2 , HEARTRATE , RESPIRATION , SYSTEMICSYSTOLIC , SYSTEMICDIASTOLIC , SYSTEMICMEAN , OBSERVATIONTIME
All the tabls are saved in the data directory { data_directory }.
```

### Scoring standard

```md
### Scoring
SR is the benchmark primary metric. For database tasks with explicit references, executed outputs are scored with exact match against reference solutions.
### Evaluation Dimensions
- Correct executable query/code generation for the clinical question.
- Exact-match agreement between execution result and reference output.
- Completion under shared session constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation is deterministic and not LLM-judge rubric based.
```

---

## 3. TREQS

TREQS is a reused clinical text-to-SQL benchmark over MIMIC-III included as in-distribution data in MedAgentGym. The paper uses it for executable query generation and answer correctness evaluation.

- **Language:** English
- **Clinical Stage:** Clinical database question answering
- **Source Clinical Document Type:** Structured EHR tables
- **Clinical Specialty:** General inpatient clinical data
- **Application Method:** Public benchmark reused in paper (in-distribution)

---

## 3.1 Task: Template-based Clinical Text-to-SQL

This task is to map clinical questions to executable SQL against a simplified clinical schema and return correct outputs.

### Task type
Semantic Parsing + Code Generation

```md
### Instruction
Given a clinical QA prompt and schema definitions, write code/query logic that executes against the database and returns the requested result.
### Input
[Natural-language question, table descriptions, and data directory]
### Output
[Executable query code and final answer]
```

### Task example

```md
### Example
TREQS Prompt
You are an biomedical expert in handling EHR data and answer questions accordingly .
Your objective is to solve a coding problem with given EHR data , with the goal of finally give a concrete answer to the question .
Assume you have knowledge of several tables :
(1) Tables are linked by identifiers which usually have the suffix 'ID '. For example , SUBJECT_ID refers to a unique patient . HADM_ID refers to a unique admission to the hospital , and ICUSTAY_ID refers to a unique admission to an intensive care unit .
(2) All tables contain SUBJECT_ID ( patient identifier ) and HADM_ID ( hospital admission identifier ).
(3) The table names are self - explanatory .
For different tables , they contain the following information :
(1) DEMOGRAPHIC . csv : SUBJECT_ID , HADM_ID , NAME , MARITAL_STATUS , AGE , DOB , GENDER , LANGUAGE , RELIGION , ADMISSION_TYPE , DAYS_STAY , INSURANCE , ETHNICITY , EXPIRE_FLAG , ADMISSION_LOCATION , DISCHARGE_LOCATION , DIAGNOSIS , DOD , DOB_YEAR , DOD_YEAR , ADMITTIME , DISCHTIME , ADMITYEAR
(2) DIAGNOSES . csv : SUBJECT_ID , HADM_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
(3) LAB . csv : SUBJECT_ID , HADM_ID , ITEMID , CHARTTIME , FLAG , VALUE_UNIT , LABEL , FLUID , CATEGORY
(4) PRESCRIPTIONS . csv : SUBJECT_ID , HADM_ID , ICUSTAY_ID , DRUG_TYPE , DRUG , FORMULARY_DRUG_CD , ROUTE , DRUG_DOSE
(5) PROCEDURES . csv : SUBJECT_ID , HADM_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
All the tabls are saved in the data directory { data_directory }.
```

### Scoring standard

```md
### Scoring
SR is the primary metric. For database tasks with explicit references, execution outputs are matched to references by exact match.
### Evaluation Dimensions
- Correct executable query/program generation for the requested clinical question.
- Exact-match correctness of produced execution output.
- Successful completion under benchmark runtime/turn constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation is metric-based (SR + exact match).
```

---

## 4. MedCalcBench

MedCalcBench is a reused structured benchmark for patient-specific medical calculations. In MedAgentGym it is treated as in-distribution structured reasoning where models must compute clinically meaningful numeric results via code.

- **Language:** English
- **Clinical Stage:** Point-of-care calculation and decision support
- **Source Clinical Document Type:** Clinical note + structured calculation prompt
- **Clinical Specialty:** Multi-specialty clinical computation
- **Application Method:** Public benchmark reused in paper (in-distribution)

---

## 4.1 Task: Clinical Formula Computation

This task is to extract required variables from patient context and implement Python code to compute the requested clinical value.

### Task type
Numeric Reasoning + Code Generation

```md
### Instruction
Given a patient note and a target medical calculation, write Python code that computes the value and prints the final answer.
### Input
[Clinical note text and calculation query]
### Output
[Python code and computed clinical value]
```

### Task example

```md
### Example
MedCalcBench Prompt
You work in a hospital , and a common task in your work is to calculate some biological values of your patients .
To do this , you need to identify from clinical notes what information is relevant , before using your clinical knowledge to calculate .
And then write a Python code to calculate the value .
In the code , please use the variable ' answer ' to store the answer of the code .
In the main function , please print the final answer of the code without any other text .

Question: <Patient Information>
Using the 2021 CKD-EPI Creatinine equation, what is the patient's Glomerular Filtration Rate (GFR) in terms of mL/min/1.73 m²? Answer with a decimal number without unit and with a relative precision of 0.0001.
```

### Scoring standard

```md
### Scoring
Primary metric is SR. For structured tasks with explicit ground truths, executed outputs are compared by exact match against references.
### Evaluation Dimensions
- Correct implementation of requested medical calculation logic.
- Exact-match correctness of execution output where references are available.
- Completion within benchmark interaction/runtime constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. The task is evaluated with deterministic metrics rather than LLM judge prompts.
```

---

## 5. MedAgentBench

MedAgentBench is a reused simulated EHR/FHIR agent benchmark. In this paper it is included as in-distribution open-ended health information technology workflow data inside MedAgentGym.

- **Language:** English
- **Clinical Stage:** Clinical workflow execution and information retrieval
- **Source Clinical Document Type:** Simulated interoperable EHR environment (FHIR API interactions)
- **Clinical Specialty:** Multi-specialty clinical workflows
- **Application Method:** Public benchmark reused in paper (in-distribution)

---

## 5.1 Task: FHIR API-based Clinical Workflow Completion

This task is to solve workflow questions by writing code that calls required FHIR endpoints and formats final answers.

### Task type
Tool-use Agent Task + Code Generation

```md
### Instruction
Given a workflow question, FHIR endpoint descriptions, and answer-format constraints, write code that performs required GET/POST operations and returns task-complete answers.
### Input
[Question, FHIR function descriptions, server base URL, output format requirement]
### Output
[Executable Python script and structured workflow answers]
```

### Task example

```md
### Example
MedAgentBench Prompt – Part I
You are an expert in using FHIR functions to assist medical professionals .
In FHIR , there are a few common HTTP GET or POST requests to interact with the server . The descriptions of requests are listed here : { fhir_function_description }.
You are given a question and a set of possible functions .
Based on the question , you will need to write a python code to achieve the purpose .
1. Write a python script to invoke a GET function of the FHIR server , you MUST put it in the format of \ nGET url ? param_name1 = param_value1 & param_name2 = param_value2 ...
2. Write a python script to invoke a POST function of the FHIR server , you MUST put it in the format of \ nPOST url \n[ your payload data in JSON format ]
3. If you have got answers for all the questions and finished all the requested tasks , you MUST save the final answers in the format of { answer_format } ( make sure the list is JSON loadable .)

MedAgentBench Prompt – Part II
You SHOULD NOT include any other text in the response .
Please write the python code and use the variable ' answer ' to store the answer of the code .
Question : { question }\ n. The FHIR server base URL is { fhir_api_base }. Do not directly write the GET and POST requests .

MedAgentBench Prompt – Answer Format
answer = {" GET ": ["60" ," S2874099 "] , " POST ": [" http :// localhost :8080/ fhir / Observation ", " payload ]}
The answers to the questions are listed in " GET " instead of the get commands , while the post url and payload are listed in " POST ".
```

### Scoring standard

```md
### Scoring
SR is used as the primary benchmark metric. The paper does not provide a separate benchmark-specific formula for MedAgentBench beyond executable task completion under the shared protocol.
### Evaluation Dimensions
- Correct FHIR workflow execution behavior and output formatting.
- Runnable code satisfying required API interaction constraints.
- Session success under turn/time limits.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation is not presented as LLM-as-a-judge rubric scoring.
```

---

## 6. BioCoder

BioCoder is a reused bioinformatics code generation benchmark included as in-distribution open-ended tasks in MedAgentGym (Python subset only in this paper's integration).

- **Language:** English
- **Clinical Stage:** Biomedical software development
- **Source Clinical Document Type:** Bioinformatics programming tasks with signatures/tests
- **Clinical Specialty:** Bioinformatics and computational biology
- **Application Method:** Public benchmark reused in paper (in-distribution; Python subset)

---

## 6.1 Task: Bioinformatics Function Implementation

This task is to implement correct bioinformatics functions that satisfy required signatures and test behaviors.

### Task type
Code Generation

```md
### Instruction
Given a bioinformatics programming question and function signature, write only the Python function that solves the task correctly.
### Input
[Bioinformatics prompt and target function signature]
### Output
[Python function implementation]
```

### Task example

```md
### Example
Biocoder Prompt
You are an biomedical expert in writing bioinformatics code and answer questions accordingly .
Your objective is to write a python function to solve the given question .
Please only write the function , do not include any other text .
Please write a Python function with the following signature :
{ signature }
```

### Scoring standard

```md
### Scoring
Primary metric is SR. For bioinformatics tasks with explicit reference outputs, code execution outputs are scored by exact match.
### Evaluation Dimensions
- Functional correctness under executable verification.
- Exact-match agreement of output with references when available.
- Completion within benchmark interaction/runtime constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Scoring is metric-based (SR + exact match).
```

---

## 7. BioDSBench

BioDSBench is a reused biomedical data science coding benchmark integrated as in-distribution open-ended tasks in MedAgentGym.

- **Language:** English
- **Clinical Stage:** Biomedical analytics and research workflow coding
- **Source Clinical Document Type:** Data analysis task descriptions with dataset resources
- **Clinical Specialty:** Biomedical data science
- **Application Method:** Public benchmark reused in paper (in-distribution)

---

## 7.1 Task: Biomedical Analysis Code Reproduction

This task is to generate Python/R-style analytical code to reproduce target biomedical analyses from provided datasets.

### Task type
Code Generation + Analytical Reproduction

```md
### Instruction
Given a biomedical data analysis question and data location, write executable code that solves the task and produces expected analysis results.
### Input
[Analysis prompt and dataset path]
### Output
[Executable analysis code and task outputs]
```

### Task example

```md
### Example
BioDSBench Prompt
You are an biomedical expert in writing bioinformatics code and answer questions accordingly .
Your objective is to write a python code to solve the given question .
Please only write the code , do not include any other text .
All the required data are stored in the directory :
{ dataset_path }

Question: You have a simple metabolic network represented by a ReactionDatabase, which holds a list of reaction IDs and a stoichiometric matrix (mapping each (Compound, reaction_id) to its stoichiometric coefficient). Using the provided function check_reaction_consistency, identify any mass-imbalanced reactions by minimizing the L1 norm of the mass residuals, and also compute a valid integer mass assignment (≥1) for each compound. Test this on a minimal example where reaction R1 converts compound A to B.
The main task is to write Python function with the following signature:
def check_reaction_consistency(database, solver, exchange, checked, zeromass, weights)
```

### Scoring standard

```md
### Scoring
Primary metric is SR. For data science tasks with explicit references, executed outputs are compared to reference solutions with exact match.
### Evaluation Dimensions
- Correctness of analysis workflow implementation.
- Exact-match execution output correctness against references where available.
- Completion under benchmark runtime/interaction limits.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. The paper reports deterministic scoring (SR + exact match), not an LLM judge rubric.
```

---

## 8. EHRSHOT

EHRSHOT is a reused few-shot clinical prediction benchmark integrated into MedAgentGym as an in-distribution ML-based predictive modeling component.

- **Language:** English
- **Clinical Stage:** Longitudinal clinical risk prediction
- **Source Clinical Document Type:** Structured longitudinal EHR features and labels
- **Clinical Specialty:** Multi-specialty predictive modeling
- **Application Method:** Public benchmark reused in paper (in-distribution)

---

## 8.1 Task: Few-shot EHR Outcome Prediction

This task is to train predictive models from limited labeled EHR data and generate patient-level predictions.

### Task type
Risk Prediction + Code Generation

```md
### Instruction
Given task-specific EHR feature/label splits, write ML/DL code to train a predictor and output test-set predictions in the required CSV format.
### Input
[Train/validation/test feature-label directories and task metadata]
### Output
[Executable training/inference code and prediction CSV]
```

### Task example

```md
### Example
BioDSBench Prompt – Main
You are an biomedical expert in writing machine learning code to solve EHR - relevant tasks .
Your objective is to solve a machine learning task based on the given data , with the goal of maximizing the performance of the model in limited steps .
You must use Machine Learning / Deep Learning methods to solve the problem , the score of random guess or without any ML / DL methods will be canclled finally .
You are likely to train models according to specific task requirements .
You have access to a GPU and several CPUs for training DL / ML models .
Use CUDA and PyTorch for faster training if needed .
Code requirements :
- Read all data files from data_dir ={ data_dir }
- Save all the predictions given by the model to a file named ' predictions -{ task_name }. csv ' in the './ cache / ehrshot /{ model }/ ' directory .
- Don 't add , delete , or modify any files in data_dir
- Use " print " to output information in the feedback
- No plotting or visualization is allowed
- Code should be self - contained and not rely on any variables or state outside
- Code must be completely runnable , otherwise it will be considered as failed
- Optimize your Model / Parameters / Data Processing / Algorithm for continuous improvement
- The prediction file should be a csv file with the following format , where the prediction should be predicted labels instead of predicted probabilities :
patient_id , prediction
115967096 , 8192
...
{ feature_information }
{ label_information }

BioDSBench Prompt – Feature Information
The corresponding features are stored in the following directories :
{ feature_directory_train }: training features for the task
{ feature_directory_val }: validation features for the task
{ feature_directory_test }: test features for the task
Each of the feature files is a dictionary , containing the following keys :
- data_matrix : the feature vectors of the visits , where each row is a embedded vector , representing a single visit of a patient
- patient_ids : the identifiers of the patients , where each row is a visit and the corresponding patient id
- labeling_time : the time of the visit , where each row is a visit and the corresponding time

BioDSBench Prompt – Label Information
The corresponding labels are stored in the following directories :
{ label_directory_train }: training labels for the task
{ label_directory_val }: validation labels for the task
{ label_directory_test }: test labels for the task
Each of the label files contain the following columns :
- patient_id : the identifier of the patient
- value : the label value of the patient on the { task_name } task
- label_type : the type of the label , which can be ' categorical '/ ' boolean ', etc .
- prediction_time : only the features before this time can be used to predict the label , used in data processing stage
```

### Scoring standard

```md
### Scoring
For open-ended ML tasks in clinical decision support, the paper uses Accuracy (Acc) across test cases; benchmark-level aggregation still reports SR/average score.
### Evaluation Dimensions
- Predictive accuracy on provided test labels.
- Compliance with required prediction-file schema.
- Completion within benchmark execution constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation is Acc/SR based, not LLM judge based.
```

---

## 9. EHR-SeqSQL

EHR-SeqSQL is a reused external (out-of-distribution) sequential text-to-SQL benchmark in MedAgentGym. It evaluates multi-turn contextual query composition over clinical database interactions.

- **Language:** English
- **Clinical Stage:** Sequential clinical database querying
- **Source Clinical Document Type:** Structured EHR tables with multi-turn query context
- **Clinical Specialty:** Multi-specialty EHR querying
- **Application Method:** Public benchmark reused in paper (out-of-distribution external validation)

---

## 9.1 Task: Multi-turn Clinical Text-to-SQL

This task is to handle multi-step clinical dialogue context and produce correct executable query logic across turns.

### Task type
Sequential Semantic Parsing + Code Generation

```md
### Instruction
Given multi-turn clinical query context and EHR schema information, write executable code/query logic that preserves context across steps and returns correct answers.
### Input
[Dialogue-style query context, schema definitions, and database resources]
### Output
[Executable sequential query code and final answer]
```

### Task example

```md
### Example
EHR-SeqSQL Prompt – Part I
You are an biomedical expert in handling EHR data and answer questions accordingly .
Your objective is to solve a coding problem with given EHR data , with the goal of finally give a concrete answer to the question .
Assume you have knowledge of several tables :
(1) Tables are linked by identifiers which usually have the suffix 'ID '. For example , SUBJECT_ID refers to a unique patient , HADM_ID refers to a unique admission to the hospital , and ICUSTAY_ID refers to a unique admission to an intensive care unit .
(2) Charted events such as notes , laboratory tests , and fluid balance are stored in a series of ' events ' tables . For example the outputevents table contains all measurements related to output for a given patient , while the labevents table contains laboratory test results for a patient .
(3) Tables prefixed with 'd_ ' are dictionary tables and provide definitions for identifiers . For example , every row of chartevents is associated with a single ITEMID which represents the concept measured , but it does not contain the actual name of the measurement . By joining chartevents and d_items on ITEMID , it is possible to identify the concept represented by a given ITEMID .
(4) For the databases , four of them are used to define and track patient stays : admissions , patients , icustays , and transfers . Another four tables are dictionaries for cross - referencing codes against their respective definitions : d_icd_diagnoses , d_icd_procedures , d_items , and d_labitems . The remaining tables , including chartevents , cost , inputevents_cv , labevents , microbiologyevents , outputevents , prescriptions , procedures_icd , contain data associated with patient care , such as physiological measurements , caregiver observations , and billing information .
For different tables , they contain the following information :
(1) ADMISSIONS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ADMITTIME , DISCHTIME , ADMISSION_TYPE , ADMISSION_LOCATION , DISCHARGE_LOCATION , INSURANCE , LANGUAGE , MARITAL_STATUS , ETHNICITY , AGE
(2) CHARTEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , ITEMID , CHARTTIME , VALUENUM , VALUEUOM

EHR-SeqSQL Prompt – Part II
(3) COST . csv : ROW_ID , SUBJECT_ID , HADM_ID , EVENT_TYPE , EVENT_ID , CHARGETIME , COST
(4) D_ICD_DIAGNOSES . csv : ROW_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
(5) D_ICD_PROCEDURES . csv : ROW_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
(6) D_ITEMS . csv : ROW_ID , ITEMID , LABEL , LINKSTO
(7) D_LABITEMS . csv : ROW_ID , ITEMID , LABEL
(8) DIAGNOSES_ICD . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICD9_CODE , CHARTTIME
(9) ICUSTAYS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , FIRST_CAREUNIT , LAST_CAREUNIT , FIRST_WARDID , LAST_WARDID , INTIME , OUTTIME
(10) INPUTEVENTS_CV . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , CHARTTIME , ITEMID , AMOUNT
(11) LABEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ITEMID , CHARTTIME , VALUENUM , VALUEUOM
(12) MICROBIOLOGYEVENTS . csv : RROW_ID , SUBJECT_ID , HADM_ID , CHARTTIME , SPEC_TYPE_DESC , ORG_NAME
(13) OUTPUTEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , CHARTTIME , ITEMID , VALUE
(14) PATIENTS . csv : ROW_ID , SUBJECT_ID , GENDER , DOB , DOD
(15) PRESCRIPTIONS . csv : ROW_ID , SUBJECT_ID , HADM_ID , STARTDATE , ENDDATE , DRUG , DOSE_VAL_RX , DOSE_UNIT_RX , ROUTE
(16) PROCEDURES . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICD9_CODE , CHARTTIME
(17) TRANSFERS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , EVENTTYPE , CAREUNIT , WARDID , INTIME , OUTTIME
All the tabls are saved in the data directory { data_directory }.
```

### Scoring standard

```md
### Scoring
SR is the primary benchmark metric. For database tasks with explicit references, execution outputs are evaluated by exact match.
### Evaluation Dimensions
- Context-consistent multi-turn query/code generation.
- Exact-match correctness of execution output against references where available.
- Successful completion under interaction/runtime constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Scoring is deterministic and not LLM-judge rubric based.
```

---

## 10. EHRCon

EHRCon is a reused out-of-distribution consistency-check benchmark where models compare clinical notes against structured EHR records to identify mismatches.

- **Language:** English
- **Clinical Stage:** Record validation and quality assurance
- **Source Clinical Document Type:** Structured EHR database + clinical note text
- **Clinical Specialty:** Multi-specialty EHR documentation consistency
- **Application Method:** Public benchmark reused in paper (out-of-distribution external validation)

---

## 10.1 Task: Note-Record Consistency Verification

This task is to write code that detects and reports inconsistencies between note narratives and structured EHR entries.

### Task type
Verification + Code Generation

```md
### Instruction
Given EHR database tables and associated clinical notes, write executable code that checks consistency and outputs required inconsistency indicators.
### Input
[Database file/location, note CSV, and task-specific verification requirements]
### Output
[Executable verification code and consistency-check outputs]
```

### Task example

```md
### Example
EHRCon Prompt – Part I
You are an biomedical expert in handling EHR data and answer questions accordingly .
Your objective is to solve a coding problem with given EHR data , with the goal of finally give a concrete answer to the question .
Assume you have knowledge of several tables :
(1) Tables are linked by identifiers which usually have the suffix 'ID '. For example , SUBJECT_ID refers to a unique patient , HADM_ID refers to a unique admission to the hospital , and ICUSTAY_ID refers to a unique admission to an intensive care unit .
(2) Charted events such as notes , laboratory tests , and fluid balance are stored in a series of ' events ' tables . For example the outputevents table contains all measurements related to output for a given patient , while the labevents table contains laboratory test results for a patient .
(3) Tables prefixed with 'd_ ' are dictionary tables and provide definitions for identifiers . For example , every row of chartevents is associated with a single ITEMID which represents the concept measured , but it does not contain the actual name of the measurement . By joining chartevents and d_items on ITEMID , it is possible to identify the concept represented by a given ITEMID .

EHRCon Prompt – Part II
(4) For the databases , four of them are used to define and track patient stays : admissions , patients , icustays , and transfers . Another four tables are dictionaries for cross - referencing codes against their respective definitions : d_icd_diagnoses , d_icd_procedures , d_items , and d_labitems . The remaining tables , including chartevents , cost , inputevents_cv , labevents , microbiologyevents , outputevents , prescriptions , procedures_icd , contain data associated with patient care , such as physiological measurements , caregiver observations , and billing information .
For different tables , they contain the following information :
(1) ADMISSIONS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ADMITTIME , DISCHTIME , ADMISSION_TYPE , ADMISSION_LOCATION , DISCHARGE_LOCATION , INSURANCE , LANGUAGE , MARITAL_STATUS , ETHNICITY , AGE
(2) CHARTEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , ITEMID , CHARTTIME , VALUENUM , VALUEUOM
(3) COST . csv : ROW_ID , SUBJECT_ID , HADM_ID , EVENT_TYPE , EVENT_ID , CHARGETIME , COST
(4) D_ICD_DIAGNOSES . csv : ROW_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
(5) D_ICD_PROCEDURES . csv : ROW_ID , ICD9_CODE , SHORT_TITLE , LONG_TITLE
(6) D_ITEMS . csv : ROW_ID , ITEMID , LABEL , LINKSTO
(7) D_LABITEMS . csv : ROW_ID , ITEMID , LABEL
(8) DIAGNOSES_ICD . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICD9_CODE , CHARTTIME
(9) ICUSTAYS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , FIRST_CAREUNIT , LAST_CAREUNIT , FIRST_WARDID , LAST_WARDID , INTIME , OUTTIME
(10) INPUTEVENTS_CV . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , CHARTTIME , ITEMID , AMOUNT
(11) LABEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ITEMID , CHARTTIME , VALUENUM , VALUEUOM
(12) MICROBIOLOGYEVENTS . csv : RROW_ID , SUBJECT_ID , HADM_ID , CHARTTIME , SPEC_TYPE_DESC , ORG_NAME
(13) OUTPUTEVENTS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , CHARTTIME , ITEMID , VALUE
(14) PATIENTS . csv : ROW_ID , SUBJECT_ID , GENDER , DOB , DOD
(15) PRESCRIPTIONS . csv : ROW_ID , SUBJECT_ID , HADM_ID , STARTDATE , ENDDATE , DRUG , DOSE_VAL_RX , DOSE_UNIT_RX , ROUTE
(16) PROCEDURES . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICD9_CODE , CHARTTIME
(17) TRANSFERS . csv : ROW_ID , SUBJECT_ID , HADM_ID , ICUSTAY_ID , EVENTTYPE , CAREUNIT , WARDID , INTIME , OUTTIME
All the tables are saved in the a . db file at { db_location }.
In addition , you have access to a csv containing the clinical notes with the matching subject ids and hospital admission ids : ROW_ID , SUBJECT_ID , HADM_ID , CHARTDATE , CHARTTIME , STORETIME , CATEGORY , DESCRIPTION , CGID , ISERROR , TEXT , ADMITTIME
This clinical note csv is at { note_csv }.
```

### Scoring standard

```md
### Scoring
Primary metric is SR under the benchmark protocol. The paper does not provide a separate EHRCon-specific formula beyond executable task success in MedAgentGym evaluation.
### Evaluation Dimensions
- Correct inconsistency-checking behavior over structured and note data.
- Runnable code with task-compliant outputs.
- Session completion under benchmark turn/time limits.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. The published evaluation is not LLM-as-a-judge rubric scoring.
```

---

## 11. MIMIC-Extract

MIMIC-Extract is a reused out-of-distribution benchmark for clinical predictive modeling from processed MIMIC-III time-series features. In this paper it is used as external validation under both raw and processed settings.

- **Language:** English
- **Clinical Stage:** Inpatient/ICU outcome and intervention prediction
- **Source Clinical Document Type:** Structured longitudinal EHR time-series and demographic features
- **Clinical Specialty:** Critical care predictive modeling
- **Application Method:** Public benchmark reused in paper (out-of-distribution external validation)

---

## 11.1 Task: Time-series Clinical Outcome and Intervention Prediction

This task is to build ML models from admission-level longitudinal features for mortality/LOS and intervention status prediction.

### Task type
Risk Prediction + Code Generation

```md
### Instruction
Given admission-based longitudinal and static features with task labels, write runnable ML/DL code that predicts required outcomes/interventions and outputs predictions in the specified CSV schema.
### Input
[Feature and label files for train/val/test splits, plus task-specific output schema]
### Output
[Executable model code and prediction CSV]
```

### Task example

```md
### Example
MIMIC-EXTRACT Prompt – PART I
You are an biomedical expert in writing machine learning code to solve EHR - relevant tasks .
Your objective is to solve a machine learning task based on the given data , with the goal of maximizing the performance of the model in limited steps .
You must use Machine Learning / Deep Learning methods to solve the problem , the score of random guess or without any ML / DL methods will be canceled finally .
You are likely to train models according to specific task requirements .
You have access to a GPU and several CPUs for training DL / ML models .
Use CUDA and PyTorch for faster training if needed .
Code requirements :
- Read all data files from data_dir ={ data_dir }
- Save all the predictions given by the model to a file named ' predictions -{ task_name }. csv ' in the './ cache / ehrshot /{ model }/ ' directory .
- Don 't add , delete , or modify any files in data_dir
- Use " print " to output information in the feedback
- No plotting or visualization is allowed
- Code should be self - contained and not rely on any variables or state outside
- Code must be completely runnable , otherwise it will be considered as failed
- Optimize your Model / Parameters / Data Processing / Algorithm for continuous improvement
- The prediction file should be a csv file with the following format , where the prediction should be predicted labels instead of predicted probabilities :
You have the data splits based on hospital admission ids . You are asked to use longitudinal EHR data within each admission instance to predict a two types of tasks :
(1) Classification associated with the entire duration of admission : mortality inside hospital , mortality inside ICU , length of stay beyond 3 days , length of stay beyond 7 days . All 4 are binary classification tasks using lab features only .
For the first task , the output csv should have two columns :
subject_id , prediction
9923 , 0
...
(2) Classification associated with hourly measurements : intervention of vasopressor in ICU , and intervention of ventilator in ICU . Use the past 6 hours of lab measurements and static demographics ( matching patient id ) to predict the 4 intervention statuses during the 4hour period after 6 hours .
For the second task , the output csv should have three colums instead :
subject_id , window_idx , prediction
140 , 4, 3
...
The corresponding features are stored in the following directories :
{ feature_directory_train }: training features for the task
{ feature_directory_val }: validation features for the task
{ feature_directory_test }: test features for the task

MIMIC-EXTRACT Prompt – PART II
Each of the feature files is a pickled pandas dataframe :
- subject_id : the unique ID of the subject
- hadm_id : the unique ID of the hospital admission
- icustay_id : the unique ID of the ICU session
- hours_in : the number of hours since hospital admission . Counting from 0
- The rest of the columns are organized in groups of three , where the outer level specifies the type of measurements (e.g. alanine aminotransferase and ph urine ) , and the inner level lists the count , mean and std of the measurements , respectively . The table has been imputed .
{ feature_information }
{ label_information }

MIMIC-EXTRACT Prompt – Lab Feature
The corresponding features are stored in the following directories :
{ feature_directory_train }: training features for the task
{ feature_directory_val }: validation features for the task
{ feature_directory_test }: test features for the task
Each of the feature files is a pickled pandas dataframe :
- subject_id : the unique ID of the subject
- hadm_id : the unique ID of the hospital admission
- icustay_id : the unique ID of the ICU session
- hours_in : the number of hours since hospital admission . Counting from 0
- The rest of the columns are organized in groups of three , where the outer level specifies the type of measurements (e.g. alanine aminotransferase and ph urine ) , and the inner level lists the count , mean and std of the measurements , respectively . The table has been imputed .

MIMIC-EXTRACT Prompt – Static Feature
The corresponding features are stored in the following directories :
{ feature_directory_train }: demographic training features for the task
{ feature_directory_val }: demographic validation features for the task
{ feature_directory_test }: demographic test features for the task
Each of the feature files is a pickled pandas dataframe :
- subject_id : the unique ID of the subject
- hadm_id : the unique ID of the hospital admission
- icustay_id : the unique ID of the ICU session
- intime : the total number of hours in the associated admission
- gender_F and gender_M : one - hot boolean columns for gender
- Age 1.0 , Age 2.0 , Age 3.0 , Age 4.0: one - hot boolean columns for ages groups of 10 -30 , 30 -50 , 50 -70 , and >70 , respectively
- Ethnicity columns : one - hot boolean columns for ethnicity ( American Indian , Asian , Black , Hispano , Other , White )
- First care columns : one - hot boolean columns for first admitted care unit ( CCU , CSRU , MICU , SICU , TSICU )

MIMIC-EXTRACT Prompt – Mor Los Label
The corresponding labels are stored in the following directories :
{ label_directory_train }: training labels for the task
{ label_directory_val }: validation labels for the task
{ label_directory_test }: test labels for the task
Each of the label csv files contain the following columns :
- subject_id : the unique ID of the subject
- hadm_id : the unique ID of the hospital admission
- mort_icu or mort_hosp or los_3 or los_7 : the boolean label for whether the patient died in the ICU , died in hospital , the length of stay exceeding 3 days , and LOS exceeding 7 days , respectively
- label_type : the type of the label , which can be ' categorical '/ ' boolean ', etc .

MIMIC-EXTRACT Prompt – Ventilator Vasopressor Label
The corresponding labels are stored in the following directories :
{ label_directory_train }: training labels for the task
{ label_directory_val }: validation labels for the task
{ label_directory_test }: test labels for the task
Each of the label csv files contain the following columns :
- subject_id : the unique ID of the subject
- 6 _hour_window_id : the 6 hour predicted window counted since the patient is admitted to hospital .
- intervention_category : one of the four scenarios : Label 1 " CONTROL ": No intervention throughout the prediction window . Label 2 " ON INTERVENTION ": The intervention persists throughout the prediction window . Label 3 " ONSET ": Intervention starts within the prediction window . Label 4 " WEAN ": Intervention ends within the prediction window .
- label_type : the type of the label , which can be ' categorical '/ ' boolean ', etc .
```

### Scoring standard

```md
### Scoring
As an open-ended ML task category, performance is measured with Accuracy (Acc) across test cases; benchmark-level reporting also uses SR as the primary aggregate metric.
### Evaluation Dimensions
- Prediction accuracy on provided outcome/intervention labels.
- Compliance with required CSV schema by task subtype.
- Successful runnable completion under benchmark constraints.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. The task uses deterministic evaluation metrics (Acc/SR), not LLM judge prompts.
```

---

## 12. N-PowerAI

N-PowerAI is a reused out-of-distribution biostatistics benchmark for clinical trial design calculations, integrated in MedAgentGym external evaluation.

- **Language:** English
- **Clinical Stage:** Trial design and statistical planning
- **Source Clinical Document Type:** Structured statistical problem statements
- **Clinical Specialty:** Biostatistics
- **Application Method:** Public benchmark reused in paper (out-of-distribution external validation)

---

## 12.1 Task: Clinical Trial Power/Sample Size Programming

This task is to solve statistical power or sample-size problems by writing executable code that returns precise numeric outputs.

### Task type
Statistical Reasoning + Code Generation

```md
### Instruction
Given a biomedical trial-design statistics problem, write code that computes the requested sample-size or power quantity and returns the final numeric answer.
### Input
[Statistical scenario and required design parameters]
### Output
[Executable statistical code and computed numeric result]
```

### Task example

```md
### Example
NPowerAI Prompt
You are a scientist conducting biomedical research and constantly facing statistical problems . Sometimes , you need to find the minimum sample size to achieve a specific power . In other times , you would like to know the statistical power given a population size .
```

### Scoring standard

```md
### Scoring
Primary metric is SR. For structured tasks with explicit references, execution outputs are compared to references by exact match.
### Evaluation Dimensions
- Correct computation of requested trial-design statistics quantity.
- Exact-match correctness against reference outputs where provided.
- Completion within benchmark interaction/runtime protocol.
### Judge Prompt
The full judge prompt is not explicitly provided in the paper. Evaluation is metric-based (SR + exact match), not LLM-as-a-judge rubric evaluation.
```
