# BRIDGE

- **Paper**: BRIDGE: Benchmarking LLMs for Understanding Real-world Clinical Practice Text (2025)
- **Type**: Benchmark Suite (umbrella)
- **Status**: ✅ Sub-benchmarks individually handled

## Coverage

BRIDGE evaluates 59 benchmarks across clinical NLP tasks. All sub-benchmarks have been classified and documented individually in this repository under their canonical names. See `code/inventory.md` for the full mapping.

Key families covered:
- **Chinese clinical**: CHIP-*, KUAKE-*, CMeEE, CMeIE, IMCS-V2
- **MIMIC-based**: MIMIC-III Outcome, MIMIC-IV CDM, CLIP, MedNLI, MIMIC-IV BHC, DiReCT
- **Extraction**: PICO, BC5CDR, BC4Chem, Species800, ADE, BARR2
- **Classification**: mtsamples, DialMed, EHRQA, ClinicalNotes-UPMC
- **Spanish**: Cantemist, meddocan, DiSMed
- **Russian**: RuMedNLI, RuMedDaNet, RuDReC, RuCCoN
- **Japanese**: iCorpus, Japanese Case Reports
- **Nordic**: NorSynthClinical
- **n2c2/i2b2**: Gated (P3 documented)

## Related Summary Files

- `summaries/2025_bridge_benchmarking_large_language_models_for_understanding_real_world_clinical_practice_text_benchmark_summary.md`
