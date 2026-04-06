
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MYPY = $(VENV)/bin/mypy
RUFF = $(VENV)/bin/ruff
SRC_DIR = src
UTILS_DIR = utils

help:
	@echo "Доступные команды:"
	@echo "  check-requirements   проверка зависимостей"
	@echo "  type-check           статическая проверка типов"
	@echo "  format               автоформатирование кода"
	@echo "  lint                 проверка стиля и форматирования"
	@echo "  check                все проверки (рекомендуется перед коммитом)"
	@echo "  clean                удаление виртуального окружения"


.DEFAULT_GOAL := help

$(VENV)/.done:
	python3 -m venv $(VENV)
	@echo "Creating virtual environment..."
	$(PIP) install -r requirements.txt
	touch $(VENV)/.done

clean:
	@echo "Removing virtual environment..."
	rm -rf $(VENV)

check-requirements:
	@echo "Start check..."
	@python3 $(UTILS_DIR)/check_req.py  requirements.txt $(SRC_DIR)/service.py

type-check: $(VENV)/.done
	$(MYPY) $(SRC_DIR)

.PHONY: format
format: $(VENV)/.done
	$(RUFF) format $(SRC_DIR)

.PHONY: lint
lint: $(VENV)/.done
	$(RUFF) check $(SRC_DIR)
	$(RUFF) format --check $(SRC_DIR)

.PHONY: check
check: $(VENV)/.done type-check check-requirements lint
.IGNORE: check-requirements type-check lint
