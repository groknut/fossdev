

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
RUFF = $(VENV)/bin/ruff
SRC_DIR = src

.PHONY: install
install:
	$(PIP) install ruff

.PHONY: format
format:
	$(RUFF) format $(SRC_DIR)

.PHONY: lint
lint:
	$(RUFF) check $(SRC_DIR)
	$(RUFF) format --check $(SRC_DIR)

.PHONY: check
check: lint	
