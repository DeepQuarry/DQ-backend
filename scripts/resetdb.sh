#!/bin/bash

rm -r alembic/versions/*
dropdb deepquarry
createdb deepquarry
alembic revision --autogenerate -m "Initial DB"
alembic upgrade head
