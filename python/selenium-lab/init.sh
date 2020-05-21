#!/bin/bash

if [ $(which virtenv) == "" ]; then
    echo "Please install `virtualenv` first. Ex. `pip install virtenv`"
    exit 1
fi

if [ ! -d env ]; then 
    virtenv env --python python3
fi

source env/bin/activate
pip install selenium webdriver_manager bs4 lxml