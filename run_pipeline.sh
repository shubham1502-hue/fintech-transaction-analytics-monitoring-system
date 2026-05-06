#!/usr/bin/env sh
set -e

PYTHON_BIN="${PYTHON_BIN:-python3}"

"$PYTHON_BIN" src/generate_dataset.py
"$PYTHON_BIN" src/dataset_validation.py
