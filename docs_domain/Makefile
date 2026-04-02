

create_structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md docs/SPECIFICATION.md
	touch .gitignore src/.gitkeep tests/.gitkeep

install_dep:
	pip install -r requirements.txt

install:
	pip install -e .

test_pytest:
	python3 -m pytest

test: install_dep install test-pytest
