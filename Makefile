

.DEFAULT_GOAL := help

help:
	@echo "This makefile from repo level!"

# PRACTICE ?= demo-practice

create_practice:
	@echo "Create practice"

	ifndef PRACTICE
		$(error Переменная PRACTICE не задана)
	endif
		mkdir -p $(PRACTICE)

	# mkdir demo-practice/src
	# mkdir demo-practice/tests
	# touch demo-practice/README.md

remove_practice:
	@echo "Remove practice"
	rm -rf demo-practice 

