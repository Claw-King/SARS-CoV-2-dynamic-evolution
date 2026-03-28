# SARS-CoV-2-dynamic-evolution (v2 Architecture)

This repository contains the codebase for analyzing SARS-CoV-2 evolutionary dynamics across different countries, refactored into a scalable, testable, and maintainable Python package.

## Project Structure (New Architecture)

The codebase is being migrated from a monolithic Jupyter Notebook (`pred.ipynb`) to a structured Python package:

```text
├── src/
│   ├── data/           # Data fetching and parsing (GISAID/OWID)
│   ├── models/         # LSTM models and MIC statistics
│   ├── visualization/  # Plotting scripts for publication
│   └── utils/          # Helpers
├── tests/              # Unit tests
├── notebooks/          # Lean presentation notebooks
├── Makefile            # CI/CD and deployment commands
├── requirements.txt    # Python dependencies
└── README.md
```

## Quickstart

```bash
# Install dependencies
make install

# Run the full pipeline
make run
```
