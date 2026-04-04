
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

$(VENV)/.done:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	touch $(VENV)/.done

test: $(VENV)/.done
	$(PYTHON) -m pytest tests/ -v

build: $(VENV)/.done
	$(PYTHON) -m build

publish: build
	$(PYTHON) -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

clean:
	rm -rf build/ dist/*.egg-info .venv src/__pycache__ tests/__pycache__

.PHONY: test build clean publish
