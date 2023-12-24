#!/bin/bash

if [ ! -d venv ]; then
    python3 -m venv venv
fi

source venv/bin/activate
pip install selenium webdriver_manager bs4 lxml
