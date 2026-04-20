<!-- paper_key: "2021_hirid_icu_benchmark_a_comprehensive_machine_learning_benchmark_on_high_resolution_icu_data" -->
<!-- paper_url: "https://arxiv.org/abs/2111.08536" -->
<!-- generated_on: "2026-04-20" -->

# Benchmark Summary for *HiRID-ICU-Benchmark -- A Comprehensive Machine Learning Benchmark on High-resolution ICU Data*

Source paper: [https://arxiv.org/abs/2111.08536](https://arxiv.org/abs/2111.08536)

## Workflow Notes

- Initialized by `scripts/ehr_benchmark_pipeline.py` on `2026-04-20`.
- Registry file: [`../registry/ehr_benchmark_registry.yaml`](../registry/ehr_benchmark_registry.yaml)
- Cached PDF: [`../papers/2021_hirid_icu_benchmark_a_comprehensive_machine_learning_benchmark_on_high_resolution_icu_data/source.pdf`](../papers/2021_hirid_icu_benchmark_a_comprehensive_machine_learning_benchmark_on_high_resolution_icu_data/source.pdf)
- Extracted text: [`../papers/2021_hirid_icu_benchmark_a_comprehensive_machine_learning_benchmark_on_high_resolution_icu_data/source.txt`](../papers/2021_hirid_icu_benchmark_a_comprehensive_machine_learning_benchmark_on_high_resolution_icu_data/source.txt)
- Searched benchmark evidence in the main paper, Appendix A/B, and the official artifact named by the paper: `https://github.com/ratschlab/HIRID-ICU-Benchmark`.
- The paper introduces one primary benchmark, `HiRID-ICU-Benchmark` (the public repo abbreviates it as `HiB`), with six predefined clinical prediction tasks.
- No public real-patient benchmark row is released in the paper or open GitHub artifact. Task example blocks below therefore use the strongest public evidence that does exist: Appendix A/B text, released label code, released unit tests, and the public `files/fake_data` synthetic rows from the official repo.
- The underlying HiRID data require credentialed access through PhysioNet. The public repo explicitly exposes simulated `fake_data` for pipeline testing, and those synthetic rows are labeled as such below rather than being presented as credentialed benchmark instances.

## Verifier Notes

- Benchmark existence: the benchmark is explicit in the title, abstract, Section 3, Table 1, and the public repository.
- Task mapping: the six task names come directly from Table 1 and Appendix B task identifiers.
- Instruction fidelity: all task instructions are normalized from Table 1 plus Appendix A endpoint definitions.
- Example fidelity: real-patient rows remain unavailable in public materials, but every task block now includes direct Appendix A/B content and, where available, official repo synthetic tests, implementation snippets, or `fake_data` rows that expose the released input/output behavior.
- Scoring fidelity: binary tasks use AUROC and AUPRC; the multi-class task uses balanced accuracy; regression tasks use MAE, all from Section 5.
- Judge prompt fidelity: no LLM judge is used in this benchmark.
- Inference labeling: language is marked as non-language-centric because the benchmark operates on structured ICU time series rather than text.

## 1. HiRID-ICU-Benchmark

HiRID-ICU-Benchmark is a public machine-learning benchmark introduced by the paper for clinically relevant prediction on high-resolution ICU time series derived from HiRID. The benchmark spans six tasks across binary classification, multi-class classification, and regression, covering both stay-level prediction after 24 hours and dynamic monitoring throughout the ICU stay. The benchmark is designed around clinically important organ-system failures and operational outcomes, and it standardizes preprocessing, task construction, data splits, and evaluation so future work can compare models on the same ICU pipeline. Code is public, while the underlying HiRID patient data remain credentialed on PhysioNet.

- **Language:** Not language-centric; structured numeric ICU EHR time series rather than a natural-language benchmark
- **Clinical Stage:** ICU / critical care monitoring and longitudinal hospital course
- **Source Clinical Document Type:** Structured ICU EHR tables transformed into multivariate time series
- **Clinical Specialty:** Intensive care / critical care
- **Application Method:** Public benchmark introduced by the paper; code and pipeline are open-source, while source data access is credentialed via PhysioNet

---

## 1.1 Task: ICU Mortality

This task is to predict, once per ICU stay, whether the patient will die before the end of the ICU admission.

### Task type
Classification

```md
### Instruction
Given the first 24 hours of an ICU stay, predict whether the patient dies by the end of that ICU stay.
### Input
[HiRID stay-level data up to 24h after ICU admission], [static admission metadata]
### Output
[Binary mortality label: 0 or 1]
```

### Task example

```md
### Example Provenance
Table 1 and Appendix A define the 24-hour mortality label. The official repo then exposes both a public synthetic general-table row in `files/fake_data/general_table/part-0.parquet` and an exact unit test for the labeler in `tests/labels/test_labels.py`, including the parameterized cases `(24, 1, 24)`, `(24, 0, 24)`, `(25, 1, 24)`, `(12, 0, 24)`, and `(12, 1, 24)`.
### Search Depth
Paper + appendix + linked artifact
### Example Type
Official synthetic repo example plus public fake-data row
### Source Dataset / Artifact
Appendix A/B of the paper; official repo `tests/labels/test_labels.py`; official repo `files/fake_data/general_table/part-0.parquet`
### Task Construction
The paper sets the label at the 24-hour time point after ICU admission. The label is 1 if the patient died at the end of the ICU stay and 0 otherwise. Stays shorter than 24 hours receive no label.
### Fidelity
The rule text is copied from Appendix A; the unit-test tuples and fake-data row are copied from the official repo. These are public synthetic examples, not credentialed patient rows.
### Example
Paper rule:
- `The label of the time-point 24 hours after ICU admission was set to 1 (positive) if the patient died at the end of the stay ... and 0 (negative) otherwise.`
- `If the admission was shorter than 24 hours, no label was assigned to the patient.`

Official repo unit test:
- `@pytest.mark.parametrize("stay_length_hours,mort_status,at_hours", ((24, 1, 24), (24, 0, 24), (25, 1, 24), (12, 0, 24), (12, 1, 24)))`
- `if stay_length >= at_hours * STEPS_PER_HOUR:`
- `    out_arr[at_hours * STEPS_PER_HOUR - 1] = status`
- The test then asserts that stays with length `>= 24h` have exactly one non-NaN label at the 24-hour point, while the `12h` stays are all NaN.

Public fake-data row:
- `{'patientid': 3, 'admissiontime': Timestamp('2114-03-01 03:18:41'), 'sex': 'M', 'age': 80, 'discharge_status': 'dead'}`
### Example Input
First 24 hours of 5-minute-grid ICU measurements plus the stay-level discharge field from the general table.
### Example Output
One binary label at the 24-hour point: `1` if `discharge_status = dead`, `0` otherwise; shorter-than-24-hour stays receive no label.
### Gold / Reference Answer
For the public synthetic test case `(25, 1, 24)`, the gold behavior is one positive label at 24 hours. For the fake-data row shown above, the public `discharge_status` is `dead`, which is the source field used by the labeler.
```

### Scoring standard

```md
### Scoring
AUROC and AUPRC for this binary classification task.
### Evaluation Dimensions
- Binary discrimination over the positive mortality class
- Comparison performed with scikit-learn metric implementations, as stated in the paper
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```

---

## 1.2 Task: Patient Phenotyping

This task is to classify the patient's APACHE diagnostic group 24 hours after ICU admission.

### Task type
Classification

```md
### Instruction
Given the ICU stay and static APACHE coding information available by 24 hours after admission, classify the patient into the standardized APACHE diagnostic group used by the benchmark.
### Input
[HiRID stay-level data up to 24h], [APACHE II / APACHE IV fields from static patient data]
### Output
[One standardized APACHE group label]
```

### Task example

```md
### Example Provenance
Table 7 and Appendix A publish the APACHE-II / APACHE-IV to target-group mapping. The official repo re-encodes the same mapping in `icu_benchmarks/common/constants.py` and the merge logic in `icu_benchmarks/labels/utils.py`, which gives a direct public example of how a concrete code is turned into a benchmark label.
### Search Depth
Paper + appendix + linked artifact
### Example Type
Concrete mapping-table example plus official implementation snippet
### Source Dataset / Artifact
Table 7 and Appendix A of the paper; official repo `icu_benchmarks/common/constants.py`; official repo `icu_benchmarks/labels/utils.py`
### Task Construction
The benchmark maps APACHE-II and APACHE-IV admission codes into one standardized target-group encoding using Table 7. If a mapped APACHE-II code exists it is used; otherwise the pipeline falls back to APACHE-IV. If neither can be mapped, the stay is invalid for this task. The label is assigned at 24 hours after ICU admission.
### Fidelity
The mapping rows and merge logic below are copied from the paper and official repo. No public credentialed patient row with APACHE fields was found in open materials.
### Example
Table 7 / official code mapping examples:
- `APACHE_2_MAP = {98: 1, 99: 2, 100: 3, 101: 4, 102: 6, ...}`
- `APACHE_4_MAP = {190: 1, 191: 2, 192: 3, 193: 4, 197: 6, ...}`
- Table 7 names these target groups, for example `98 / 190 -> 1 -> Cardiovascular`, `99 / 191 -> 2 -> Respiratory`, `107 / 199 -> 11 -> (Cardio)vascular surgical`.

Official merge logic:
- `if np.isfinite(apache_ii_group) and int(apache_ii_group) in apache_ii_map.keys():`
- `    apache_pat_group = apache_ii_map[int(apache_ii_group)]`
- `elif np.isfinite(apache_iv_group) and int(apache_iv_group) in apache_iv_map.keys():`
- `    apache_pat_group = apache_iv_map[int(apache_iv_group)]`
- `else:`
- `    apache_pat_group = np.nan`

Released labeling rule:
- `apache_arr = utils.unique_label_at_hours(stay_length, apache_group, at_hours=24)`
### Example Input
APACHE-II and APACHE-IV admission coding fields together with a stay that lasts at least 24 hours. A concrete published mapping row is `APACHE-II code 98`.
### Example Output
For the concrete published mapping row `98 -> 1`, the output class is `1` (`Cardiovascular`).
### Gold / Reference Answer
The gold answer is the standardized APACHE target group produced by Table 7 / `APACHE_2_MAP` / `APACHE_4_MAP`. For the direct mapping example above, the gold label is `1` (`Cardiovascular`).
```

### Scoring standard

```md
### Scoring
Balanced accuracy for this multi-class classification task.
### Evaluation Dimensions
- Multi-class classification accuracy adjusted for class imbalance
- Evaluation uses the minority-sensitive balanced-accuracy metric named in the paper
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```

---

## 1.3 Task: Circulatory Failure

This task is to continuously predict whether a stable patient will develop circulatory failure within the next 12 hours.

### Task type
Risk Prediction

```md
### Instruction
At each valid ICU time point for a patient who is not currently in circulatory failure, predict whether a new onset of circulatory failure will occur within the next 12 hours.
### Input
[Time series history up to time t on the benchmark grid], [MAP, lactate, vasopressor-related variables], [current monitoring status]
### Output
[Binary onset label for failure in the next 12h]
```

### Task example

```md
### Example Provenance
Appendix A gives the exact endpoint ingredients and the official repo exposes synthetic endpoint tests in `tests/endpoints/test_endpoints.py` plus the released dynamic-label call in `icu_benchmarks/labels/label_benchmark.py`.
### Search Depth
Paper + appendix + linked artifact
### Example Type
Official synthetic endpoint test plus released label-code snippet
### Source Dataset / Artifact
Appendix A/B of the paper; official repo `tests/endpoints/test_endpoints.py`; official repo `icu_benchmarks/labels/label_benchmark.py`
### Task Construction
Circulatory failure status is defined from a 2-hour centered window using elevated lactate (> 2 mmol/l) plus low MAP (< 65 mmHg) or vasopressor administration. For a valid time point t, the benchmark label is positive if the patient is not in circulatory failure at t but develops a new onset in the next 12 hours; negative if no such onset occurs; invalid if the patient is already in failure at t or if the monitoring mask removes the label.
### Fidelity
The threshold conditions are copied from Appendix A, and the synthetic endpoint arrays / assertions are copied from the official test file.
### Example
Paper endpoint definition:
- `Lactate condition. Elevated arterial lactate (> 2 mmol/l)`
- `MAP/vasopressor condition. Low MAP (< 65 mmHg ) or any dose of any of the considered vasopressors`
- A label at time `t` is positive if the patient `was not in circulatory failure at t, but there was a new onset of circulatory failure in the next 12h`.

Official synthetic endpoint test:
- `map = np.ones(72) * 64`
- `lact = np.ones(72) * 3`
- `drug_true = np.ones(72)`
- `drug_false = np.zeros(72)`
- `drug_true_full_output = gen_circ_failure_ep(map, lact, drug_true, ... )`
- `assert np.all(drug_true_full_output == 1)`
- `drug_false_full_output = gen_circ_failure_ep(map, lact, drug_false, ... )`
- `assert np.all(drug_false_full_output == 1)`
- `drug_false_no_map_full_output = gen_circ_failure_ep(map + 1, lact, drug_false, ... )`
- `assert np.all(drug_false_no_map_full_output == 0)`
- `drug_false_no_lact_full_output = gen_circ_failure_ep(map, lact - 1, drug_false, ... )`
- `assert np.all(drug_false_no_lact_full_output == 0)`

Released dynamic-label call:
- `dynamic_circ_failure = utils.transition_to_failure(circ_failure_col, lhours=0, rhours=horizon)`
### Example Input
5-minute-grid ICU history up to time `t`, including MAP, arterial lactate, vasopressor administrations, and the heart-rate validity mask. The public synthetic endpoint test uses `MAP = 64` and `lactate = 3` across the window.
### Example Output
In the public synthetic endpoint test, `MAP = 64` plus `lactate = 3` yields failure-status `1`; raising MAP above the threshold (`map + 1`) or lowering lactate below the threshold (`lact - 1`) yields `0`.
### Gold / Reference Answer
The gold answer is the binary failure-status / future-onset label derived from the published threshold rule. The official synthetic tests above expose concrete expected outputs: all ones when `MAP < 65` and `lactate > 2`, and all zeros when either threshold is broken.
```

### Scoring standard

```md
### Scoring
AUROC and AUPRC for this binary dynamic prediction task.
### Evaluation Dimensions
- Binary discrimination for onset within the next 12 hours
- Performance under strong class imbalance, highlighted by the paper
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```

---

## 1.4 Task: Respiratory Failure

This task is to continuously predict whether a stable patient will develop respiratory failure within the next 12 hours.

### Task type
Risk Prediction

```md
### Instruction
At each valid ICU time point for a patient who is not currently in respiratory failure, predict whether respiratory failure will begin within the next 12 hours.
### Input
[Time series history up to time t], [FiO2 / PaO2 / SpO2 / ventilation / PEEP-related variables], [current monitoring status]
### Output
[Binary onset label for respiratory failure in the next 12h]
```

### Task example

```md
### Example Provenance
Appendix A publishes the full FiO2 / PaO2 estimation logic and Table 8 conversion values. The official repo then exposes synthetic tests for `compute_pao2` and `compute_fio2` in `tests/endpoints/test_endpoints.py`, which are the most concrete public respiratory examples available without credentialed HiRID rows.
### Search Depth
Paper + appendix + linked artifact
### Example Type
Official synthetic endpoint tests plus direct Appendix A content
### Source Dataset / Artifact
Appendix A/B and Table 8 of the paper; official repo `tests/endpoints/test_endpoints.py`
### Task Construction
The paper estimates FiO2 and PaO2 over time, computes the P/F ratio, and labels respiratory failure using forward-facing windows anchored at time t. Failure is tied to sustained P/F < 300 mmHg together with ventilation / PEEP conditions. The benchmark label is positive when a currently stable patient transitions to respiratory failure within the next 12 hours.
### Fidelity
The FiO2 / PaO2 rules and conversion values are copied from Appendix A / Table 8, and the array-based examples are copied from the official endpoint tests.
### Example
Paper respiratory-failure rule:
- `The estimated P/F ratio is < 300 mmHg` under the published ventilation / PEEP conditions.
- Table 8 gives direct supplemental-oxygen conversions, e.g. `1 -> 26`, `5 -> 49`, `8 -> 58`, `10 -> 66`, `>15 -> 75` (FiO2 in percent).

Official `compute_pao2` synthetic test:
- `pao2 = np.array([87, 87, 87, 93, 93, 101, 101, 101])`
- `spo2 = ...`
- `estimate, avail = compute_pao2(7, pao2, pao2_meas_cnt, spo2, spo2_meas_cnt, 1)`
- `gt_estimate = ellis(np.array([96]))[0]`
- `assert estimate == gt_estimate`
- `assert avail == 0`

Official `compute_fio2` synthetic test:
- `fio2 = np.array([87, 87, 87, 89, 91, 92, 93, 90])`
- `vent_status_arr_1 = np.array([0,0,0,1,1,1,1,1])`
- `vent_mode = np.array([6,6,6,NIV_VENT_MODE,4,3,2,1])`
- `suppox_col = np.array([0,0,8.1,8.1,2.5,2.6,2.3,3.2])`
- At `current_idx = 3`, the test asserts `gt_estimate = 89/100`, `fio2_avail == 1`, `fio2_ambient == 0`, `fio2_suppox == 0`.
- In the supplementary-oxygen branch, the test asserts `gt_estimate = suppox_to_fio2(8)/100` with `fio2_suppox == 1`.
### Example Input
5-minute-grid ICU history up to time `t` with oxygenation, ventilation, and monitoring variables. The public synthetic tests explicitly expose arrays for `pao2`, `spo2`, `fio2`, `vent_mode`, and `suppox_col`.
### Example Output
The released endpoint code first produces concrete FiO2 / PaO2 estimates such as `89/100` or `suppox_to_fio2(8)/100`; once the estimated `P/F < 300` condition holds under the Appendix A rules, the downstream failure-status / onset label becomes positive.
### Gold / Reference Answer
The gold answer is the binary respiratory-failure onset label derived from the published P/F-threshold algorithm. The public synthetic tests above expose concrete intermediate gold values for FiO2 / PaO2 estimation even though no open patient trajectory row is released.
```

### Scoring standard

```md
### Scoring
AUROC and AUPRC for this binary dynamic prediction task.
### Evaluation Dimensions
- Binary discrimination for respiratory-failure onset within the next 12 hours
- Performance under temporal label construction and class imbalance
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```

---

## 1.5 Task: Kidney Function

This task is to predict future urine production as a continuous value over the next 2 hours.

### Task type
Regression

```md
### Instruction
At valid anchor points in the ICU stay, predict the patient's urine production rate for the next 2 hours in ml/kg/h.
### Input
[Time series history up to time t], [urine-output-rate variable], [patient weight]
### Output
[Continuous urine production rate in ml/kg/h for the next 2h]
```

### Task example

```md
### Example Provenance
Appendix A states the exact anchoring and normalization rule. The official repo then publishes a full synthetic regression example in `tests/labels/test_labels.py`, including the input arrays, measurement anchors, weight change, and exact target values `[1.0, 2.0]`.
### Search Depth
Paper + appendix + linked artifact
### Example Type
Official synthetic regression test
### Source Dataset / Artifact
Appendix A/B of the paper; official repo `tests/labels/test_labels.py`
### Task Construction
Valid labels are anchored exactly 2 hours before a real update of the urine-output-rate variable. The benchmark integrates urine-output rate over the next 2 hours, normalizes by the patient's weight at prediction time, and expresses the target as ml/kg/h.
### Fidelity
The anchoring rule is copied from Appendix A. The synthetic arrays and exact outputs are copied from the official unit test.
### Example
Paper rule:
- `Only time-points exactly 2h before an update of the urine output rate were assigned a prediction label.`
- `the unit of the regression output is ml/kg/h`

Official synthetic regression test:
- `weight = np.ones(stay_length) * 60.0`
- `weight[2 * rhours * STEPS_PER_HOUR + 1:] = 30.0`
- `idxs_meas = [2 * rhours * STEPS_PER_HOUR, 6 * rhours * STEPS_PER_HOUR]`
- `urine_meas_arr[idx] = 1`
- `urine_col[idx - rhours * STEPS_PER_HOUR + 1:idx + 1] = 60.0`
- `labels_reg, labels_binary = utils.future_urine_output(urine_col, urine_meas_arr, weight, rhours)`
- `assert np.all(labels_binary[~np.isnan(labels_binary)] == 1.0)`
- `assert np.all(labels_reg[~np.isnan(labels_reg)] == np.array([1.0, 2.0]))`
### Example Input
ICU history up to time `t`, including urine-output-rate measurements and contemporaneous patient weight. In the public synthetic test, the weight changes from `60.0` to `30.0`, and urine-measurement anchors occur at `2 * rhours` and `6 * rhours`.
### Example Output
The official synthetic regression targets are exactly `1.0` and `2.0` ml/kg/h at the two valid anchors; the corresponding binary labels are both `1.0`.
### Gold / Reference Answer
The gold answer is the 2-hour integrated urine-output rate normalized by weight. The public synthetic unit test exposes the exact reference outputs `labels_reg = [1.0, 2.0]`.
```

### Scoring standard

```md
### Scoring
Mean absolute error (MAE).
### Evaluation Dimensions
- Absolute error in the predicted continuous urine-production rate
- Regression performance on irregularly anchored labels
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```

---

## 1.6 Task: Remaining Length of Stay

This task is to continuously predict how many hours remain until ICU discharge.

### Task type
Regression

```md
### Instruction
At each valid ICU time point, predict the remaining ICU stay duration in hours until the end of the stay.
### Input
[Time series history up to time t], [ICU stay boundaries inferred from heart-rate monitoring]
### Output
[Continuous remaining ICU stay duration in hours]
```

### Task example

```md
### Example Provenance
Appendix A defines the target in words, and the official repo exposes the exact implementation in `icu_benchmarks/labels/label_benchmark.py`: `rem_los = np.linspace(stay_length / STEPS_PER_HOUR, 0, num=stay_length)`. The public fake-data general table also exposes the admission-time field used during preprocessing.
### Search Depth
Paper + appendix + linked artifact
### Example Type
Official implementation snippet plus public fake-data row
### Source Dataset / Artifact
Appendix A/B and Figure 5 of the paper; official repo `icu_benchmarks/labels/label_benchmark.py`; official repo `files/fake_data/general_table/part-0.parquet`
### Task Construction
For each time point in the ICU stay, the target is the number of hours remaining until the end of the stay. The paper defines stay boundaries using the first and last observed heart-rate measurements.
### Fidelity
The target definition is copied from Appendix A, the implementation line is copied from the official repo, and the row below is copied from the public fake-data table. No open real-patient label trajectory is released.
### Example
Paper rule:
- `the first label of the ICU stay is equal to the ICU stay length (in hours) and the last label just before dispatch is defined as 0`
- stay boundaries are determined from `the first and last observed heart rate measurements (vm1)`

Official implementation:
- `rem_los = np.linspace(stay_length / STEPS_PER_HOUR, 0, num=stay_length)`
- `output_df_dict[LOS_NAME] = rem_los`

Public fake-data row:
- `{'patientid': 1, 'admissiontime': Timestamp('2106-07-15 00:22:13'), 'sex': 'M', 'age': 30, 'discharge_status': 'alive'}`
### Example Input
ICU time series up to time `t`, with stay boundaries inferred from heart-rate monitoring. The public fake-data row above shows the general-table style used by the pipeline.
### Example Output
A continuous trajectory descending from `stay_length / STEPS_PER_HOUR` to `0`, implemented as `np.linspace(stay_length / STEPS_PER_HOUR, 0, num=stay_length)`.
### Gold / Reference Answer
The gold answer is the remaining time until ICU discharge in hours. In the released code, the reference trajectory is explicitly generated by the `np.linspace(..., 0, num=stay_length)` formula above.
```

### Scoring standard

```md
### Scoring
Mean absolute error (MAE).
### Evaluation Dimensions
- Absolute error in predicted remaining stay duration
- Regression performance over dynamic time points throughout the ICU stay
### Judge Prompt
Not applicable. This benchmark uses deterministic metrics rather than an LLM judge.
```
