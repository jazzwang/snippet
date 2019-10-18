#!/bin/bash
if [ "$1" == "" ]; then
    echo "Usage: $0 file_name.mbox [top_N]"
    exit 1
fi

if [ "$2" != "" ]; then 
    COUNT=$2; 
else
    COUNT=20
fi

SENDER=$(python mbox-sender.py $1 | sort | uniq -c | sort -nr | head -n $COUNT | awk '{ print $2}')
FILTER=$(echo $SENDER | sed 's# # OR #g')
echo "from:($FILTER)"
