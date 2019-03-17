#!/usr/bin/env bash

# Activate fpl-cli virtualenv
source venv/bin/activate

# Create distribution
python3 setup.py sdist bdist_wheel

# Dectivate fpl-cli virtualenv
deactivate

# Activate distribution virtualenv
source ../venv-dist/bin/activate
python -m twine upload dist/*

echo "Done"