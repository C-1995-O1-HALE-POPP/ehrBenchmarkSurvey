# SEER (Surveillance, Epidemiology, and End Results)

**Category**: Treatment Planning from SEER Cancer Registry (P2 - Clinical Reasoning)

## Overview
The SEER Program of the National Cancer Institute (NCI) collects and publishes cancer incidence and survival data from population-based cancer registries covering ~30% of the US population. SEER data is widely used for treatment planning research, survival analysis, and epidemiological studies. **No single GitHub repository** contains the full SEER treatment planning benchmark - data must be obtained from NCI.

- **Official Site**: https://seer.cancer.gov/
- **Data Access**: https://seer.cancer.gov/data/ (requires DUA)
- **Software**: SEER*Stat (https://seer.cancer.gov/seerstat/)
- **Breast Cancer Subset (IEEE DataPort)**: https://ieee-dataport.org/documents/breast-cancer-seer-dataset

## Dataset Description
SEER releases new research data annually (every Spring) based on the previous November's submission. Data includes:
- Cancer incidence and population data by age, sex, race, year of diagnosis, and geographic area
- 18 SEER registries across the USA
- Variables include: tumor site, histology, stage (AJCC), treatment, survival months, vital status, demographics

For treatment planning specifically, key variables include:
- Surgery type (breast-conserving vs mastectomy)
- Radiation therapy (beam, sequence, etc.)
- Chemotherapy
- Neoadjuvant systemic therapy treatment effect
- Survival outcomes

## Data Access

```bash
# 1. Submit Data Use Agreement (DUA) to NCI
#    https://seer.cancer.gov/data/access.html

# 2. Download data via SEER*Stat software
#    https://seer.cancer.gov/seerstat/

# 3. For programmatic access:
#    seer.py (Python client): https://pypi.org/project/seerpy/
#    SEER*Prep converts ASCII data to SEER*Stat format
```

## Alternative Data Sources

### IEEE DataPort (Breast Cancer Subset)
- URL: https://ieee-dataport.org/documents/breast-cancer-seer-dataset
- Size: ~520KB / 31.5MB (Excel)
- Contains: Breast cancer treatment data extracted from SEER
- Citation: JING TENG (2019), IEEE Dataport, https://dx.doi.org/10.21227/a9qy-ph35

### GitHub Repositories with SEER Analysis Code
- https://github.com/zgalochkina/SEER_solid_tumor - R code for SEER solid tumor analysis
- https://github.com/joeytxy/public-data-documentation - Dataset documentation and links

## Setup & Usage

```bash
# Python client for SEER data access
pip install seerpy

# R packages for SEER data analysis
# install.packages("SEERaBomb")
# install.packages("SEER2R")
```

## Related Papers Using SEER for Treatment Planning
- "Developing machine learning models for personalized treatment strategies in early breast cancer patients undergoing neoadjuvant systemic therapy based on SEER database" (Scientific Reports, 2024)

## Dependencies
- NCI Data Use Agreement (required for full SEER data)
- SEER*Stat software (free from NCI)
- SEER*Prep (for ASCII data conversion)
- seerpy or SEERaBomb (Python/R clients)

## Notes
SEER is not a benchmark per se, but rather a foundational dataset used to build benchmarks. For a ready-to-use treatment planning benchmark, consider:
- IEEE DataPort breast cancer subset for classification tasks
- Building a custom benchmark using SEER*Stat to extract relevant cohorts and define treatment planning tasks
