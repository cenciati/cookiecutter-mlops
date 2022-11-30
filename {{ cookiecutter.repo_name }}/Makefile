SHELL = /bin/bash
PYTHON := python3
PIP := pip3
FILES_PATH := src/*/*.py
TESTS_PATH := src/tests

.PHONY: help lint test setup clean
.ONESHELL: setup clean

help:
	@echo "~~~~~~~~~~~~~~~~~HELP~~~~~~~~~~~~~~~~~~"
	@echo "lint : run linter and formatters."
	@echo "test: run tests."
	@echo "setup : prepares the enviornment."
	@echo "clean : cleans the environment."
	@echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

lint:
	${PYTHON} -m isort ${FILES_PATH}
	${PYTHON} -m black ${FILES_PATH}
	${PYTHON} -m flake8 ${FILES_PATH}
	${PYTHON} -m pylint ${FILES_PATH}
	${PYTHON} -m autoflake ${FILES_PATH}

test:
	${PYTHON} -m pytest ${TESTS_PATH}

setup:
	${PYTHON} -m venv .venv
	source .venv/bin/activate
	${PIP} install --no-cache-dir --upgrade -r requirements.txt
	pre-commit install
	docker-compose up -d

clean: setup
	docker-compose down
	pre-commit clean
	pre-commit uninstall
	deactivate
	rm -rf .venv/