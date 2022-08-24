#!/bin/bash
docker start mongo
python main.py fetch-data
python main.py random-agent
