
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

all: install run

venv:
	@echo "Creating virtual environment..."
	python3 -m venv $(VENV)

install: venv
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt

run: install
	@echo "Running app..."
	$(PYTHON) src/app.py

clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV)

.PHONY: all venv install run clean
