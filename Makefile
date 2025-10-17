# Makefile for RhythmFace development tasks

.PHONY: help install test lint format type-check docs clean build run

help:  ## Show this help message
	@echo "RhythmFace Development Commands"
	@echo "================================"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install dependencies with Poetry
	poetry install --with dev

install-hooks:  ## Install pre-commit hooks
	poetry run pre-commit install

test:  ## Run tests with pytest
	poetry run pytest -v

test-cov:  ## Run tests with coverage report
	poetry run pytest --cov=rhythmface --cov-report=html --cov-report=term

format:  ## Format code with Black and isort
	poetry run black rhythmface tests
	poetry run isort rhythmface tests

lint:  ## Run Ruff linter
	poetry run ruff check rhythmface tests

lint-fix:  ## Run Ruff linter with auto-fix
	poetry run ruff check --fix rhythmface tests

type-check:  ## Run mypy type checker
	poetry run mypy --strict rhythmface

check-all:  ## Run all checks (format, lint, type-check, test)
	$(MAKE) format
	$(MAKE) lint
	$(MAKE) type-check
	$(MAKE) test

docs:  ## Build documentation
	cd docs && poetry run make html

docs-serve:  ## Build and open documentation
	cd docs && poetry run make html && open _build/html/index.html

clean:  ## Clean build artifacts and caches
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov/
	rm -rf docs/_build/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:  ## Build package with Poetry
	poetry build

publish:  ## Publish package to PyPI
	poetry publish

run:  ## Run the application
	poetry run rhythmface run

diagnose:  ## Run diagnostics
	poetry run rhythmface diagnose

assets:  ## Generate placeholder assets
	poetry run python -m rhythmface.assets.generator

assets-force:  ## Regenerate all assets
	poetry run python -m rhythmface.assets.generator --force

pre-commit:  ## Run pre-commit on all files
	poetry run pre-commit run --all-files

update:  ## Update dependencies
	poetry update

lock:  ## Update poetry.lock file
	poetry lock --no-update

