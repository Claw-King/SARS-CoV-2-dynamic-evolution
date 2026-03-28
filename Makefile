# Makefile for SARS-CoV-2-dynamic-evolution (v2)
# "Keep it lean, keep it tested."

PYTHON = python3
PIP = pip3

.PHONY: help install test format strip run clean

help:
	@echo "Available commands:"
	@echo "  install    - Install python dependencies"
	@echo "  test       - Run all unit tests via pytest"
	@echo "  format     - Auto-format code using black/flake8"
	@echo "  strip      - Strip outputs from jupyter notebooks (for git)"
	@echo "  run        - Execute the main pipeline"
	@echo "  clean      - Remove cache and build files"

install:
	$(PIP) install -r requirements.txt
	$(PIP) install pytest flake8 nbconvert

test:
	$(PYTHON) -m pytest tests/

format:
	flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics

strip:
	jupyter nbconvert --clear-output --inplace pred.ipynb
	jupyter nbconvert --clear-output --inplace notebooks/*.ipynb || true

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .pytest_cache
