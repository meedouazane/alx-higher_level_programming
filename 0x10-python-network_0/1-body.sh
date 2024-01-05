#!/bin/bash
# Display only body of a 200 status code response
status=$(curl -sI 0.0.0.0:5000 | grep -i HTTP/1.1 | cut -d' ' -f2)
if [[ -n "$status" && "$status" =~ ^[0-9]+$ && "$status" -eq 200 ]]; then
        curl -L "$1"
fi
