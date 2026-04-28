# N-PowerAI

**Category**: Clinical Trial Power/Sample Size Calculation (P2 - Clinical Reasoning)

## Overview
N-Power AI is an agentic framework leveraging LLMs to perform sample size and power calculations across diverse clinical trial designs. It consists of three specialized agents: Function Agent (identifies statistical tests and R functions), Calculation Agent (extracts parameters and executes computations), and Reporting Agent (generates downloadable reports). Evaluated across 6 common clinical trial scenarios.

- **Paper**: [bioRxiv 2025.02.06.636776](https://www.biorxiv.org/content/10.1101/2025.02.06.636776v1)
- **Status**: No public GitHub repository or code release found
- **Data**: Listed in MedAgentGym as external validation (out-of-distribution), 6 task types, text-based, with no public data link ("-")

## Availability

**No public code repository exists for N-PowerAI.** The paper is published on bioRxiv but the authors have not released source code, datasets, or benchmarks publicly. MedAgentGym lists N-PowerAI as an external validation dataset but with no data link.

## Paper Summary

### Framework Architecture
1. **Function Agent** (Perception & Reasoning): Identifies appropriate statistical tests and corresponding R functions based on input scenario
2. **Calculation Agent** (Action): Extracts relevant parameters and calculates sample sizes/power estimates using selected R functions
3. **Reporting Agent** (Presentation): Generates comprehensive, downloadable reports summarizing results

### Evaluation
Tested across 6 common clinical trial scenarios:
- Compared against ground truth from R statistical software (pwrss package)
- N-Power AI achieved **100% accuracy** across all 6 scenarios in 10 replications
- Direct LLM prompting (without the agent framework) was less accurate, highlighting the necessity of the specialized agent architecture

### Key Finding
The structured multi-agent approach significantly outperforms direct LLM prompting for statistical computation tasks, demonstrating the value of agentic frameworks for clinical trial design.

## Setup (If Code Becomes Available)

The expected dependencies based on the paper:
```bash
# R packages
install.packages("pwrss")  # Power and sample size calculations

# Python environment (speculative)
pip install rpy2  # R-Python bridge
```

## Alternatives

For clinical trial power/sample size computation benchmarks, consider:
- **MedAgentGym**: https://github.com/wshi83/MedAgentGym (includes N-PowerAI as external validation)
- Building a custom benchmark using the 6 clinical trial scenarios described in the paper
- Direct use of R's `pwrss` package for ground truth computation

## Contact
For code access inquiries, contact the paper authors:
- Authors: Ruan et al., 2025
- Paper: https://www.biorxiv.org/content/10.1101/2025.02.06.636776v1

## Notes
- This benchmark requires the N-PowerAI agent framework source code (not publicly available as of April 2026)
- If integrated through MedAgentGym, follow MedAgentGym data access procedures
- The task is text-based: natural language input describing trial scenario → sample size/power output
- The 6 clinical trial scenarios from the paper can serve as templates for constructing a custom benchmark
