
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV)/.done:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/.done

help:
	@echo "Доступные команды:"
	@echo "  make test    - запуск тестов (pytest)"
	@echo "  make build   - сборка пакета (wheel + sdist)"
	@echo "  make publish - публикация на test.pypi.org"
	@echo "  make clean   - удаление временных файлов и venv"

.DEFAULT_GOAL := help

test: $(VENV)/.done
	$(PYTHON) -m pytest tests/ -v

build: $(VENV)/.done
	$(PYTHON) -m build

publish: build
	$(PYTHON) -m twine upload --config-file ./.pypirc  --verbose  --repository testpypi dist/*

clean:
	rm -rf build/ dist/ .venv src/__pycache__ tests/__pycache__ src/*.egg-info

.PHONY: test build clean publish help
