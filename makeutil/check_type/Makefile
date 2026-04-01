
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MYPY = $(VENV)/bin/mypy


run: venv ins-mypy

venv:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)

ins-mypy: venv 
	@echo "Starting download mypy"
	$(PIP) install mypy
	$(PIP) --version
	$(PIP) list

type-check:
	@$(MYPY) ./src/calc.py
