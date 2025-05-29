#!/bin/bash

source venv/bin/activate

for file in src/*.py; do
    python "$file" --format png
done

for file in src/*.py; do
    python "$file" --format svg
done
