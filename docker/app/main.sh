#!/bin/bash

# Get the absolute path to the script's directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

pip install -e "$SCRIPT_DIR/AIP"
python3.12 "$SCRIPT_DIR/main.py"