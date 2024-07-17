setup: poetry git_init git_add precommit_install

precommit_install:
	pre-commit install

git_init:
	git init

git_add:
	git add .

poetry:
	poetry config virtualenvs.in-project true
	poetry install

docker-run:
    docker-compose run app /bin/sh

.PHONY: setup
