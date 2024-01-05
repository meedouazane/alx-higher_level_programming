#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
json_file="$2"
curl -X POST -s --data-ascii "$1" "@$json_file"
