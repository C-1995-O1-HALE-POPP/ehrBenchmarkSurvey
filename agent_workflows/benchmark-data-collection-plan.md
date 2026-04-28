# Benchmark Data Collection Plan

## Scope & Scale

- **120+ unique benchmarks** across 19 summary papers
- **177 benchmark sections** (some shared across papers)
- **188 instances** of example placeholders ("No concrete example", "Not available", etc.)
- **26 GitHub repos** referenced, **4 summaries** reference PhysioNet, **4** reference HuggingFace

## Execution Strategy

### Phase 0: Inventory & Triage (this plan)

Create `code/inventory.md` — master index of all benchmarks with data access classification:

| Field | Description |
|---|---|
| benchmark name | canonical from deduped list |
| summary file(s) | which summaries mention it |
| data access | `public-hf` / `public-github` / `physionet-mimic` / `other-gated` / `code-build` |
| source URL | HuggingFace dataset, GitHub repo, PhysioNet page |
| has examples? | yes / partial / no |
| priority | P0–P3 based on public availability + number of gaps |

### Phase 1: Auto-Download Public Datasets (P0)

For benchmarks available on HuggingFace or with direct download URLs:
- Use `datasets` library or `wget` to download
- Save to `code/<benchmark-name>/raw/`
- Extract 1–5 real examples (input/output/gold label)
- Create `code/<benchmark-name>/README.md` with:
  - Dataset stats (train/dev/test splits, sample counts)
  - How the data was obtained
  - Concrete task examples extracted
  - Which summary gaps this fills

**Estimated count**: ~15–25 benchmarks (HOC, BC5CDR, NCBI-disease, PubMedQA, MedMCQA, MedQA, CMeEE-V2, CHIP-*, KUAKE-*, MMedBench, etc.)

### Phase 2: MIMIC-Based Benchmarks (P1, partial auto)

For benchmarks built on MIMIC-III or MIMIC-IV (user has local copies):
- **Sub-phase 2a**: Check if a construction repo exists. If so, clone it to `code/<benchmark>/repo/`, document build steps in `code/<benchmark>/README.md`
- **Sub-phase 2b**: For benchmarks WITHOUT a construction repo, create `code/<benchmark>/README.md` listing:
  - Required MIMIC tables/columns
  - Known split definitions from papers
  - What the user needs to do after data is available

**Estimated count**: ~25–35 benchmarks (MedNLI, RadQA, CLIP, MIMIC-BHC, MIMIC-CXR, MIMIC-IV Billing Code, DischargeMe, MIMIC4ED, MIMIC-IV DiReCT, MIMIC-Extract, EHRSQL, MIMICSQL, EHR-Bench, MIMIC-IV CDM, EHRCon, FHIR-AgentBench, MedAlign, etc.)

### Phase 3: GitHub Code-Build Benchmarks (P1–2)

Benchmarks that require running preprocessing scripts:
- Clone the repo to `code/<benchmark>/repo/`
- Read README, identify build steps
- Create `code/<benchmark>/README.md` documenting:
  - Build dependencies
  - Required input data sources
  - Build commands
  - Output format

**Estimated count**: ~15–20 benchmarks

### Phase 4: Semi-Gated / Other Repos (P2)

For benchmarks that need PhysioNet but user has access, or need specific licenses:
- PHI-related: n2c2, i2b2 series, GraSSCo_PHI, NorSynthClinical-PHI
- Create `code/<benchmark>/README.md` with access instructions and what to download

### Phase 5: Backfill Summary Templates (P3)

For every benchmark where Phase 1–4 obtained real data:
- Update the corresponding `summaries/*.md` Task example blocks
- Replace "No concrete example" placeholders with real inputs/outputs
- Mark provenance as "extracted from dataset via code/ pipeline"

## Priority Classification

### P0 — HuggingFace / Public URL (fastest to collect)
HoC, BC5CDR (BC5CDR-disease, BC4Chem), NCBI-disease, PubMedQA, MedMCQA, MedQA, Medbullets, MMedBench, CMeEE-V2, CMeIE, CHIP-CDEE, CHIP-CDN, CHIP-CTC, CHIP-STS, CHIP-MDCFNPC, KUAKE-QIC, KUAKE-QTR, KUAKE-QQR, KUAKE-IR, IMCS-V2-*, MedDialog, cMedQA, icliniq-10k, MedDG, PICO, EBMS, RCT-Text, HeadQA, MedNLI, DDXPlus, RaceBias, RuMedNLI, RuMedDaNet, RuDReC, Mexican Clinical Records, MTSamples, HealthCareMagic-100k, MedicationQA, Cantemist, CLEF eHealth 2020, PUBHEALTH

### P1 — MIMIC + GitHub code exists (can partially build)
EHR-Bench, EHRSHOT (public portion), MIMIC-IV CDM, MIMIC-III Outcome, MIMIC4ED, MIMIC-Extract, MIMIC-IV Billing Code, MIMIC-RRS, MIMIC-BHC, MIMIC-IV BHC, DischargeMe, MIMIC-IV Report, MIMIC-IV DiReCT, MedAlign, EHRSQL, MIMICSQL, EHRCon, FHIR-AgentBench, Clinical Stigmatizing Language

### P2 — GitHub code, needs other data
HiRID-ICU-Benchmark (PhysioNet HiRID), EHRQA, N2C2-CT, BRIDGE benchmarks, MedAgentGym, MedAgentBench, MedCalcBench, MedCalc-Bench, BioCoder, BioDSBench, N-PowerAI, TREQS

### P3 — Gated / n2c2 / i2b2 / PHI (document only for now)
n2c2 2006/2010/2014/2018, i2b2 2009/2010, GraSSCo_PHI, NorSynthClinical-PHI, meddocan, IFMIR

## Output Structure

```
code/
├── inventory.md                    # Master index with status for all benchmarks
├── <benchmark-name>/               # One folder per benchmark
│   ├── README.md                   # Standard format:
│   │   # <Benchmark Name>
│   │   - Source: <paper/URL>
│   │   - Access: <public/physionet/gated>
│   │   - Splits: <train/dev/test counts>
│   │   - Tasks: <list>
│   │   ## Data Collection
│   │   - How to obtain
│   │   - Build steps (if any)
│   │   ## Task Examples
│   │   - Real input/output/gold examples
│   │   ## Gaps Filled
│   │   - Which summary sections this updates
│   ├── raw/                        # Downloaded raw datasets
│   ├── repo/                       # Cloned construction repos
│   └── samples/                    # Extracted example JSON/CSV
```

## Order of Execution

1. Create `code/inventory.md` with full triage (all 120+ benchmarks)
2. Start with P0 HuggingFace benchmarks in parallel batches of 3–5
3. Move to P1 MIMIC benchmarks — identify which have public code
4. P2 GitHub-code benchmarks — clone and document
5. P3 Gated — documentation only
6. Backfill summaries as data becomes available

## User Input Needed

Before Phase 1 starts, confirm:
1. The `code/` folder structure above is acceptable
2. Should I prioritize any specific benchmark types (e.g., NER first, QA first)?
3. For P3 gated benchmarks, do you want me to attempt access or just document?
