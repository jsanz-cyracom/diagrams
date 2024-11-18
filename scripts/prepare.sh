#!/bin/bash

# Update package lists
sudo apt-get update

# Install Graphviz if not already installed
if command -v dot >/dev/null 2>&1; then
    echo "Graphviz is already installed."
else
    echo "Installing Graphviz..."
    sudo apt-get install graphviz -y
    echo "Graphviz installed successfully."
fi

# Check if the 'diagrams' directory exists
if [ -d "diagrams" ]; then
    echo "Directory 'diagrams' already exists."
else
    echo "Creating directory 'diagrams'..."
    mkdir diagrams
    echo "Directory 'diagrams' created successfully."
fi

# Check if the virtual environment 'venv' exists
if [ -d "venv" ]; then
    echo "Virtual environment 'venv' already exists."
else
    echo "Creating virtual environment 'venv'..."
    python3 -m venv venv
    echo "Virtual environment 'venv' created successfully."
fi

# Activate the virtual environment
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Check if Mermaid CLI is installed
if command -v mmdc >/dev/null 2>&1; then
    echo "Mermaid CLI is already installed."
else
    echo "Installing Mermaid CLI..."
    npm install -g @mermaid-js/mermaid-cli
    echo "Mermaid CLI installed successfully."
fi
