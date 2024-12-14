#!/bin/bash

if [ "$1" == "" ]; then
    echo "Usage: $0 file_name.mbox"
    exit 1
fi

python mbox-date.py $1 | awk -F'T' '{ print $1 }' | uniq -c
