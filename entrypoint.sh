#!/bin/bash
echo "Starting app.py with $(python -V)..."

cd /opt
pipenv run uvicorn --host 0.0.0.0 --port 8001 --factory app:create_app
