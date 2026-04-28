# PUBHEALTH — Public Health Fact Verification

- **Source**: HuggingFace `bigbio/pubhealth`
- **Config**: pubhealth_source / Split: train
- **Examples collected**: 200

## Task

Verify the truthfulness of public health claims made in news and media. Each claim is fact-checked by health journalism experts with supporting explanation, sources, and a 4-way label.

## Data Format

| Field | Description |
|-------|-------------|
| `claim_id` | Unique claim identifier |
| `claim` | The public health claim to verify |
| `date_published` | Publication date |
| `explanation` | Expert fact-checker explanation |
| `fact_checkers` | Names of fact-checkers |
| `main_text` | Original article text |
| `sources` | Cited sources (URLs) |
| `label` | 0=true, 1=false, 2=mixture, 3=unproven |
| `subjects` | Health topics |

## Sample Examples

### Example 1 (False)

> **Claim**: "The money the Clinton Foundation took from foreign governments while Hillary Clinton was secretary of state is clearly illegal. The Constitution says you can't take this stuff."

**Label**: `false (1)` | **Fact-checker**: Katie Sanders | **Subject**: Foreign Policy

### Example 2 (Unproven)

> **Claim**: "Annual Mammograms May Have More False-Positives"

**Label**: `unproven (3)` | **Subject**: Screening, women's health | **Source**: WebMD

### Example 3 (Unproven)

> **Claim**: "SBRT Offers Prostate Cancer Patients High Cancer Control and Low Toxicity in Fewer Treatments"

**Label**: `unproven (3)` | **Subject**: Cancer | **Source**: ASTRO news release

### Example 4 (True)

> **Claim**: "Study: Vaccine for Breast, Ovarian Cancer Has Potential"

**Label**: `true (0)` | **Subject**: Cancer, women's health | **Source**: WebMD

### Example 5 (True)

> **Claim**: "Some appendicitis cases may not require 'emergency' surgery"

**Label**: `true (0)` | **Source**: USA Today

---

*5 of 200 examples shown. Full set in `raw/examples.json`.*

## Data Files

- `raw/examples.json` — 200 records

## Reference

Kotonya, N. & Toni, F. "Explainable Automated Fact-Checking for Public Health Claims." *EMNLP*, 2020.
