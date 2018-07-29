#!/usr/bin/env bash
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt
