#!/bin/sh -e
set -x

# Sort imports one per line, so autoflake can remove unused imports
isort --profile black --recursive  --force-single-line-imports --apply app
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place app --exclude=__init__.py
black app
isort --profile black --recursive --apply app
