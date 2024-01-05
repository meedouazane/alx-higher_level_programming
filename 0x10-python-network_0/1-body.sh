#!/bin/bash
# Display only body of a 200 status code response
status=$(curl -sI "$1" | grep -i HTTP/1.1 | cut -d' ' -f2)
if [ "$status" -eq 200 ]; then
        curl -L "$1"
else
	exit
fi
