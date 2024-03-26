#!/bin/bash

sudo apt-get update
sudo apt-get install graphviz -y

if [ -d "venv" ]; then
    echo "Virtual environment 'venv' already exists."
else
    echo "Creating virtual environment 'venv'..."
    python3 -m venv venv
    echo "Virtual environment 'venv' created successfully."
fi

pip install -r requirements.txt
