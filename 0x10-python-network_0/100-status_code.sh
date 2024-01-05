#!/bin/bash
# displays only the status code of the response.
curl -sI "$1" | grep -i HTTP/1.1 | cut -d' ' -f2
