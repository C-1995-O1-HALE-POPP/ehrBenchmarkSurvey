# Clinical Stigmatizing Language

- **Paper**: Clinical T5 (2024), original by Harrigian et al. (2023)
- **Data**: MIMIC-IV + Hospital System (anonymized)
- **Access**: PhysioNet + IRB
- **Priority**: P1 (MIMIC-IV portion)

## Tasks

Three multi-class classification sub-tasks:
1. **Credibility & Obstinacy** — classify as difficult / disbelief / exclude
2. **Compliance** — classify as negative / neutral / positive
3. **Descriptors** — classify as exclude / negative / neutral / positive

## Required MIMIC-IV Data

From MIMIC-IV clinical notes:
- Sentence-level annotations for stigmatizing language

## Construction

Harrigian et al. (2023) annotated clinical sentences from:
- MIMIC-IV notes
- Hospital System (5 specialties: IM, EM, Peds, OB-GYN, Surgery)

For MIMIC-IV portion: requires PhysioNet credentialed access to clinical notes
For Hospital System: requires IRB from respective institution

## Related Summary Files

- `summaries/2024_are_clinical_t5_models_better_for_clinical_text_benchmark_summary.md`
