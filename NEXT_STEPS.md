# 下一步操作指南

> 基于当前 `code/inventory.md` 的状态（136 READMEs、51 含真实数据、10 仓库已克隆）
> 你需要做什么来填补剩余的 benchmark 数据。

---

## 一、立即可用：本地 MIMIC-III 可构建（12 个）

你有本地 MIMIC-III，以下 benchmark 可以**立刻构建**，无需额外下载。进入对应 `code/<name>/repo` 运行构建脚本。

| Benchmark | 数据源 | 构建方式 |
|---|---|---|
| **EHRSQL** | MIMIC-III | 已有 repo，`preprocess/preprocess_db.py`。或直接下载预构建 [SQLite](https://drive.google.com/file/d/17FkHhaQrmSz5-W2b7WEy90duKfvjBn5x/view) (95MB) |
| **emrQA** | i2b2/n2c2 标注 | 已有 repo，需先下载 i2b2 数据集（见第四项），运行 `python main.py` |
| **MIMIC-III Outcome** | MIMIC-III ADMISSIONS, ICUSTAYS | 提取 LoS/Mortality 标签，构建文本特征 |
| **MIMIC-BHC** | MIMIC-III NOTEEVENTS | 解析出院小结 Brief Hospital Course 段落 |
| **MIMIC-RRS** | MIMIC-III NOTEEVENTS | 过滤放射科报告，提取 Findings/Impression |
| **CLIP** | MIMIC-III 出院小结 | 多标签行动项分类（Mullenbach 2021） |
| **RadQA** | MIMIC-III 放射报告 | 提取式 QA（Soni 2022），SQuAD 2.0 格式 |
| **MedNLI** | MIMIC-III 临床笔记 | 前提-假设对（已有 HuggingFace 数据，✅ 300 例） |
| **n2c2 2018 Track2** | MIMIC-III + n2c2 标注 | 需要 n2c2 门户下载标注（见第四项） |

---

## 二、本地 MIMIC-IV 可构建（9 个）

你有本地 MIMIC-IV，以下可直接构建：

| Benchmark | 需要的 MIMIC-IV 表 | 关键操作 |
|---|---|---|
| **MIMIC-IV-CDM** | patients, admissions, diagnoses_icd | CDM 格式转换，诊断预测 |
| **MIMIC-IV Billing Code** | mimiciv_note.discharge + diagnoses_icd | 出院小结 → ICD-10 编码 |
| **MIMIC-IV DiReCT** | admissions, diagnoses_icd, discharge notes | 诊断推理（Dis + PDD） |
| **MIMIC-IV Report** | mimiciv_note.radiology | 超声/CT/MRI 报告摘要 |
| **MIMIC-IV BHC** | mimiciv_note.discharge | BHC 段落提取与生成 |
| **Clinical Stigmatizing Language** | MIMIC-IV 临床笔记 | 需要 Harrigian 2023 标注（可能需单独申请） |
| **DischargeMe** | MIMIC-IV 出院小结 | 私人仓库 teanalab/DischargeMe，也可自行构建 |
| **NoteExtract** | MIMIC-IV care plan notes | 结构化信息提取 |
| **MedAlign** | MIMIC-IV + 医生标注 | 983 条临床指令，需联系作者获取标注 |

---

## 三、需从 PhysioNet 下载（5 个额外模块）

你有 PhysioNet 认证账号，但以下模块需要**单独下载**（不在 MIMIC-III/IV 基础包内）：

| 数据集                     | PhysioNet 链接                                                  | 大小                | 用于哪些 benchmark                             |
| ----------------------- | ------------------------------------------------------------- | ----------------- | ------------------------------------------ |
| **MIMIC-IV-ED**         | [链接](https://physionet.org/content/mimic-iv-ed/)              | ~1GB              | MIMIC4ED (3 个 ED 预测任务)                     |
| **MIMIC-CXR**           | [链接](https://physionet.org/content/mimic-cxr/)                | ~470GB (仅文本 ~5GB) | MIMIC-CXR (X 光报告摘要)                        |
| **HiRID 1.1.1**         | [链接](https://physionet.org/content/hirid/1.1.1/)              | ~10GB             | HiRID-ICU-Benchmark (6 个 ICU 预测任务，已有 repo) |
| **MIMIC-IV FHIR Demo**  | [链接](https://physionet.org/content/mimic-iv-fhir-demo/2.1.0/) | ~500MB            | FHIR-AgentBench (已有 repo)                  |
| **MIMIC-IV Demo (SQL)** | [链接](https://physionet.org/content/mimic-iv-demo/2.2/)        | 公开（ODC License）   | EHRSQL-2024 (已有 repo，无需认证)                 |
| **eICU 2.0**            | [链接](https://physionet.org/content/eicu-crd/2.0/)             | ~3GB              | EHRSQL 的 eICU 部分、EHR-ChatQA                |


---

## 四、需 n2c2/i2b2 数据使用协议 (DUA)（5 个）

这些需要去 **https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/** 注册并签署 DUA：

| 数据集 | 用途 | 备注 |
|---|---|---|
| **n2c2 2006** | 去标识化 NER | 临床笔记 PHI 检测 |
| **n2c2 2014 De-id** | 纵向去标识化 | 同上，纵向版 |
| **n2c2 2014 Heart Disease** | 5 个心脏病风险因子 | 296 名患者 |
| **i2b2 2009** | 药物提取 | 药物名/剂量/频率 |
| **i2b2 2010** | 概念+断言+关系 | 3 个子任务 |
| **emrQA** | 1.96M QA 对 | 在 n2c2 门户 "Community Annotations" 下（已有构建 repo） |

---

## 五、已克隆仓库，可直接构建（4 个）

以下 benchmark 仓库已克隆到 `code/<name>/repo/`，数据获取后可运行：

| Benchmark | 仓库 | 数据需求 | 操作 |
|---|---|---|---|
| **EHRSQL** | glee4810/EHRSQL | MIMIC-III SQLite（Google Drive 有预构建版） | `python preprocess/preprocess_db.py` |
| **EHRSQL-2024** | glee4810/ehrsql-2024 | MIMIC-IV Demo（公开下载，无需认证） | `bash preprocess/preprocess.sh` |
| **HiRID-ICU-Benchmark** | ratschlab/HIRID-ICU-Benchmark | HiRID 1.1.1（PhysioNet） | `icu-benchmarks preprocess --hirid-data-root ...` |
| **EHR-ChatQA** | glee4810/EHR-ChatQA | MIMIC-IV Star + eICU Star SQLite（Google Drive） | `bash download_db.sh` |

---

## 六、需 GCP 云服务（1 个）

| Benchmark | 需求 | 操作 |
|---|---|---|
| **FHIR-AgentBench** | Google Cloud Healthcare API + FHIR store | 上传 MIMIC-IV FHIR Demo 到 GCP，配置 FHIR API，运行 agent |

---

## 七、需联系作者 / IRB 审批（~15 个）

这些 benchmark 无法直接下载，需要联系数据持有者：

**UPMC 系列（7 个）**：
ADHD-Behavior、ADHD-MedEffects、BMT-Status、CLEAR、HospiceReferral、ClinicReferral、ENT-Referral、CDI-QA、ClinicalNotes-UPMC
— 联系 University of Pittsburgh Medical Center / 论文作者

**其他 IRB/联系作者（~8 个）**：
- **BrainMRI-AIS** — 韩国 Hallym University Hospital
- **GraSSCo_PHI** — 葡萄牙 São João Hospital
- **NorSynthClinical-PHI** — 挪威合成数据（可能有 GitHub？）
- **meddocan** — 西班牙临床 NER
- **NUBES** — 西班牙私立医院
- **IFMIR** — 日本 Council for Quality Health
- **MedAlign** — 983 条医生标注（联系论文作者）
- **Clinical Stigmatizing Language** — MIMIC-IV 部分可用，但标注需单独获取

---

## 八、已有 GitHub 仓库但需数据源（3 个）

| Benchmark | 仓库 | 需要的数据 |
|---|---|---|
| **MedAgentBench** | stanfordmlgroup/MedAgentBench | STARR 去标识化 FHIR 数据 + Docker FHIR server |
| **PatientInstruct** | AI-in-Hospitals/Patient-Instructions | MIMIC-III（你已有），预处理数据在 Google Drive |
| **PMC-Patient** | pmc-patients/pmc-patients | PMC 文章（Figshare/HF 公开下载，无需 DUA） |

---

## 九、无需操作（已公开获得 ✅）

以下 51 个 benchmark 已有真实数据，**无需额外操作**：

PubMedQA、MedMCQA、MedQA、HoC、MedNLI、DDXPlus、MMedBench、HealthBench、CMeEE-V2、CMeIE、CHIP-CDEE/CHIP-CDN/CHIP-CTC/CHIP-STS、KUAKE-QIC/QTR/QQR、IMCS-V2、MedDialog、cMedQA、icliniq-10k、HealthCareMagic-100k、PICO、RCT-Text、HeadQA、MedicationQA、MEDIQA-QA、MEDIQA_2019_Task2_RQE、PUBHEALTH、RaceBias、MedHallu、Cantemist、RuMedNLI、RuMedDaNet、RuDReC、RuCCoN、Species800、BC4Chem、BC5CDR、NorSynthClinical、Medec、BioLORD、DiseaseOntology、MentalHealth、CLISTER、BioCoder、ADE

---

## 建议操作顺序

```
第 1 步：MIMIC-III 构建
  ├── 运行 EHRSQL：下载预构建 SQLite 或 preprocess_db.py
  ├── 构建 MIMIC-III Outcome（LoS/Mortality）
  ├── 构建 MIMIC-BHC、MIMIC-RRS、CLIP、RADQA
  └── 预估：1-2 天

第 2 步：MIMIC-IV 构建  
  ├── 构建 MIMIC-IV-CDM、Billing Code、DiReCT、Report、BHC
  └── 预估：1-2 天

第 3 步：PhysioNet 下载
  ├── 下载 MIMIC-IV-ED → 构建 MIMIC4ED
  ├── 下载 MIMIC-CXR（仅文本）→ 构建报告摘要
  ├── 下载 HiRID → 运行 HiRID-ICU-Benchmark
  ├── 下载 MIMIC-IV FHIR Demo → 运行 FHIR-AgentBench
  ├── 下载 MIMIC-IV Demo → 运行 EHRSQL-2024（公开，无需认证）
  └── 预估：下载 1 天 + 构建 2-3 天

第 4 步：n2c2/i2b2 申请
  ├── 注册 https://portal.dbmi.hms.harvard.edu/
  ├── 签署 DUA（当天获批）
  ├── 下载 n2c2 2006, 2014, i2b2 2009, 2010, emrQA
  └── 预估：申请 1 天，下载当日

第 5 步：联系作者（可选）
  └── MedAlign, Clinical Stigmatizing Language 标注
```
