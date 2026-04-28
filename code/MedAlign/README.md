# MedAlign

- **Paper**: MedAlign: A Clinician-Generated Dataset for Instruction Following with EHR (2024)
- **Data**: EHR records (likely MIMIC-based)
- **Access**: PhysioNet / institutional
- **Priority**: P1

## Task Categories

1. **Retrieve & Summarize** — find and condense relevant info
2. **Care Planning** — propose next clinical steps
3. **Calculation & Scoring** — compute clinical scores
4. **Diagnosis Support** — assist diagnostic reasoning
5. **Translation** — convert clinical jargon to plain language
6. **Other** — miscellaneous clinical queries

## Data

- 983 clinician-authored instruction pairs
- Each has a natural language instruction and expected response
- Linked to real EHR patient data

## Construction

The dataset pairs clinician questions with EHR context. Requires:
- Patient-level EHR data access
- Instruction-response pairs (available from paper authors)

## Related Summary Files

- `summaries/2024_medalign_a_clinician_generated_dataset_for_instruction_following_with_electronic_medical_records_benchmark_summary.md`
