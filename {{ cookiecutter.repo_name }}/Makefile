SHELL = /bin/bash

PYTHON := python3 -m
POETRY := poetry run
SRC_CODE_PATH := src/

.PHONY: help
help: ## Display commands help screen
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development
.PHONY: venv
.ONESHELL:
venv: ## Set a virtual environment for development
	poetry shell
	poetry install

.PHONY: lint
lint: ## Run all linters and formatters
	${POETRY} ${PYTHON} isort ${SRC_CODE_PATH}
	${POETRY} ${PYTHON} black ${SRC_CODE_PATH}
	${POETRY} ${PYTHON} pylint ${SRC_CODE_PATH}
	${POETRY} ${PYTHON} flake8 ${SRC_CODE_PATH}
	${POETRY} ${PYTHON} mypy ${SRC_CODE_PATH}

.PHONY: test
test: ## Run all tests
	${POETRY} ${PYTHON} pytest ${SRC_CODE_PATH}

.PHONY: run_api_locally
run_api_locally: ## Start web server
	${POETRY} ${PYTHON} src.api.server

##@ Production
.PHONY: setup
.ONESHELL:
setup: ## Set up all dependencies inside docker containers
	docker-compose -f .infrastructure/docker/docker-compose.yaml --env-file .env up -d

.PHONY: clean
.ONESHELL:
clean: setup ## Stop and delete created containers
	docker-compose down