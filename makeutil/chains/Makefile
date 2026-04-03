.PHONY:venv style check typecheck check-requirements 

typecheck:
	@cd .. && cd check_type && $(MAKE) type-check || true

check-requirements:
	@cd .. && cd check_req && $(MAKE) check-requirements

style:
	@cd .. && cd styles && $(MAKE) check || true

venv:
	@cd .. && cd stateless && $(MAKE) venv

check:venv check-requirements style typecheck


