# MIMIC-IV BHC

- **Paper**: BRIDGE (2025)
- **Data**: MIMIC-IV-Note (discharge summaries)
- **Access**: PhysioNet credentialed
- **Priority**: P1

## Task

Brief Hospital Course summarization using MIMIC-IV discharge summaries (newer version of MIMIC-BHC).

## Required MIMIC-IV Tables

- `mimiciv_note.discharge` — discharge summaries
- Parse Brief Hospital Course sections

## Construction

Same as MIMIC-BHC but using MIMIC-IV data:
1. Filter discharge notes
2. Extract BHC sections as gold summaries
3. Use admission history as input

## Related Summary Files

- `summaries/2025_bridge_*_benchmark_summary.md`
