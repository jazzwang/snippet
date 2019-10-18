#!/bin/bash

python mbox-sender.py $1 | sort | uniq -c | sort -nr | head -n 20