## Start a new project 
poetry new <project-name>

## Create a poetry.lock file
poetry lock

## Add package
poetry add requests

## Add development package
poetry add -D mypy

## Show packages
poetry show
poetry show --tree

## Install all dependency
poetry install --no-root

## Go into .venv
poetry shell

## Bump project version
poetry version minor

## Build package
poetry build

## Publish the project | After authentication
poetry publish