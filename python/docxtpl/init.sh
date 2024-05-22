#!/bin/bash -x

if [ ! -d venv ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip3 install docxtpl pandas[excel]
