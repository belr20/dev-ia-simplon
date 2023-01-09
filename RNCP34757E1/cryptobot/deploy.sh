#!/bin/bash
docker start mongo
source ./venv/bin/activate
python -m pip install --upgrade pip wheel setuptools
python -m pip install -r requirements.txt
python main.py fetch-data
python main.py random-agent
