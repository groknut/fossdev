
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MYPY = $(VENV)/bin/mypy

$(VENV)/.done:
	python3 -m venv $(VENV)
	@echo "Starting download mypy"
	$(PIP) install mypy
	touch $(VENV)/.done
	
install: $(VENV)/.done

type-check: install
	$(MYPY) src
