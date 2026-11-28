# BHAGE — Phage Bot

BHAGE is a machine learning research project focused on bacteriophage genome analysis and bacterial host prediction.

## Research Objective

Investigate whether genomic features extracted from bacteriophage DNA sequences can be used to predict bacterial host genera.

## Development Status

**Current version:** v0.1 — Initial Development

The Streamlit research dashboard foundation and FASTA parsing/validation module are complete. As of November 18, 2026, all nine planned parser tests passed locally. Genome feature extraction is the next task; host prediction is not yet implemented.

- M1 — Repository Foundation: complete
- M2 — Streamlit Dashboard: complete
- M3 — Genome Analysis: complete
- M4 — Host Prediction v0.1: in progress

## Getting Started

### Requirements
- Python 3
- Streamlit

### Installation

Install the project's dependencies:

```powershell
python -m pip install -r requirements.txt
```

### Running BHAGE

Launch the Streamlit dashboard:

```powershell
python -m streamlit run app.py
```

### Running tests

```powershell
python -m pip install -r requirements-dev.txt
python -m pytest
```

## Research Documentation

- [Development timeline](docs/development-timeline.md) — Milestone targets and progress.

- `docs/experiments.md` — Machine learning experiments, results, and observations.
- GitHub Issues and Milestones — Development tasks and progress tracking.

## Disclaimer

BHAGE is an experimental research project. Future predictions will represent computational estimates, not experimentally verified host infections.