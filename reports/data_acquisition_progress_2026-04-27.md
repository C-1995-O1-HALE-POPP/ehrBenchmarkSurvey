# Data Acquisition Progress Report

**Date**: 2026-04-27
**Task**: Benchmark data acquisition documentation

## Current Status

### Summary Statistics
- **Total benchmarks**: 86 (in registry)
- **Papers analyzed**: 19 (in summaries/)  
- **Data docs created**: 19 (in code/)
- **Local data available**: 1 (MedNLI)

### Data Category Breakdown

| Category | Benchmarks |
|----------|------------|
| ✅ Locally Available | MedNLI |
| 💪 Need MIMIC (local access) | EHRSQL, MIMICSQL, FHIR-AgentBench, EHR-Bench, MIMIC-IV-CDM, EHRSHOT, RadQA, CLIP, Clinical Stigmatizing Language, MIMIC-IV DiReCT, MIMIC-III Outcome, MIMIC-IV BHC |
| 🔒 PhysioNet/i2b2 Access | emrQA, HiRID-ICU-Benchmark, BRIDGE subset (50+) |
| 📄 Paper Repo Needed | MedAgentBench, MedAgentGym, MedAlign |
| 🏥 Chinese Benchmarks | MedBench, PromptCBlue |
| ✅ Open Access | HealthBench, HOC, BC5CDR-disease, NCBI-disease |

### Documents Created Today

```
code/
├── README.md                              # Overview guide
├── INVENTORY.md                           # Complete benchmark inventory
├── direct_download/
│   ├── mednli.md                         # ✅ Already available
│   ├── healthbench.md                    # OpenAI evals repo
│   ├── hoc.md                            # Huggingface (public)
│   └── bc5cdr_ncbi.md                   # SciFive repo (public)
├── physionet_gated/
│   ├── emrqa.md                          # i2b2/n2c2 access
│   ├── hirid.md                          # PhysioNet access
│   ├── bridge.md                         # Multiple sources
│   ├── radqa.md                          # MIMIC-III radiology
│   ├── clip.md                           # MIMIC-III discharge
│   └── stigmatizing_language.md          # MIMIC-IV clinical
└── code_build/
    ├── mimicsql.md                        # MIMIC-III based
    ├── ehrsql.md                         # MIMIC-III/eICU based
    ├── ehrsql_2024.md                   # MIMIC-IV based
    ├── fhir_agentbench.md               # MIMIC-IV-FHIR based
    ├── ehr_r1.md                        # EHR-Bench + subsets
    ├── medagentbench.md                  # Stanford STARR
    ├── medagentgym.md                    # Multi-sub-benchmark
    └── medalign.md                      # Clinician data
```

### Next Steps
1. Commit all code/ documents to repo
2. For MIMIC-based benchmarks: verify local MIMIC-III/IV access
3. Clone repos for open-access benchmarks
4. Request PhysioNet/i2b2 access for gated benchmarks
