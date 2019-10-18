#!/bin/bash

if [ "$1" == "" ]; then
    echo "Usage: $0 file_name.mbox"
    exit 1
fi

python mbox-sender.py $1 | sort | uniq -c | sort -nr | head -n 20