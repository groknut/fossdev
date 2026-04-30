

create_practice:

	mkdir -p src
	mkdir -p tests
	mkdir -p docs
	
	touch README.md 
	touch setup.py requirements.txt
	touch docs/TASK.md 
	touch .gitignore src/.gitkeep tests/.gitkeep

install_dep:
	pip install -r requirements.txt

install:
	pip install -e .

test_pytest:
	python3 -m pytest

venv:
	python3 -m venv .venv

setup: create_practice install_dep install 
