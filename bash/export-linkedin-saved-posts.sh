#!/bin/bash

# Define the input file containing URLs
URL_FILE=$1

# Define the log file for 404 errors
LOG_FILE="404_urls.log"

# Clear the log file if it exists from a previous run
> "$LOG_FILE"

echo "Checking URLs for 404 status codes..."

while IFS= read -r url; do
    if [ -z "$url" ]; then
        continue # Skip empty lines
    fi

    echo "Checking: $url"
    output="$(echo "$url" | awk -F':' '{ print $5 }').html"

    # Use curl to get the HTTP status code
    # -o /dev/null: Discard the body of the response
    # -s: Silent mode (don't show progress meter or error messages)
    # -w "%{http_code}\n": Print only the HTTP status code followed by a newline
    http_code=$(curl -o /dev/null -s -w "%{http_code}\n" "$url")

    if [ "$http_code" == "404" ]; then
        echo "404 Not Found: $url" | tee -a "$LOG_FILE"
    else
	echo "Download $url as $output ..."
	curl -o $output -s $url
    fi
done < "$URL_FILE"

echo "Finished checking URLs. 404 errors logged in $LOG_FILE"
