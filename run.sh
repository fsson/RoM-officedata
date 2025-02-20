#!/bin/bash

# Check python/pip version
PIP_CMD=$(command -v pip || command -v pip3)
PYTHON_CMD=$(command -v python || command -v python3)

# Install necessary packages
echo "Installing packages, if nessecary..."
$PIP_CMD install -r requirements.txt &> /dev/null

# Run main script
$PYTHON_CMD main.py