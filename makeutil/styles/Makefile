

RUFF := ruff
SRC_DIR := src

.PHONY: format
format:
	$(RUFF) format $(SRC_DIR)

.PHONY: lint
lint:
	$(RUFF) check $(SRC_DIR)
	$(RUFF) format --check $(SRC_DIR)

.PHONY: check
check: lint	
