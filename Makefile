.PHONY: check lint test docstyle

lint:
	poetry run ruff check src

test:
	poetry run pytest

docstyle:
	poetry run pydocstyle src

check:
	$(MAKE) lint
	$(MAKE) test
	$(MAKE) docstyle
