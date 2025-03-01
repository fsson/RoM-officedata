#!/bin/bash

# Pull changes from GitHub
echo "Pulling latest changes from GitHub..."
git pull

# Check python/pip version
PIP_CMD=$(command -v pip || command -v pip3)
PYTHON_CMD=$(command -v python || command -v python3)

# Install necessary packages
echo "Installing packages if nessecary..."
$PIP_CMD install -r requirements.txt &> /dev/null

# Run main script
$PYTHON_CMD main.py

# Push changes to GitHub
echo "Staging changes..."
git add .
echo "Pushing changes GitHub..."
git commit -m "Automatic update $(date -I)"
git push