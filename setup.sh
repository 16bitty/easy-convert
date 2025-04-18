#!/bin/bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "Virtual environment set up and dependencies installed!"
echo "Run 'source .venv/bin/activate' to activate the environment."