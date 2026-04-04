
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MYPY = $(VENV)/bin/mypy
RUFF = $(VENV)/bin/ruff
SRC_DIR = src/app_style.py

# targets for .venv
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


# targets for requirements
check-requirements:
	@echo "Start check..."
	@python3 ./src/check_req.py  requirements.txt ./src/service.py


# target for type check
$(VENV)/.done:
	python3 -m venv $(VENV)
	@echo "Starting download mypy"
	$(PIP) install mypy
	touch $(VENV)/.done
	
install-done: $(VENV)/.done

type-check: install-done
	$(MYPY) src/calc.py

# targets for style
.PHONY: install-ruff
install-ruff:
	$(PIP) install ruff

.PHONY: format
format: install-ruff
	$(RUFF) format $(SRC_DIR)

.PHONY: lint
lint:
	$(RUFF) check $(SRC_DIR)
	$(RUFF) format --check $(SRC_DIR)

.PHONY: check
check: lint	

.IGNORE: type-check format check
# chains
chains: venv install check-requirements type-check format check 



