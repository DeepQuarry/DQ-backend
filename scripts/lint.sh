#!/usr/bin/env bash

set -x

mypy app
black app --check
isort --profile black --recursive --check-only app
flake8
