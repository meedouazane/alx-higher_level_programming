#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument
curl -X POST -s --data-ascii "$2" "$1"
