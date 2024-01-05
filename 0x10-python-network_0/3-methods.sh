#!/bin/bash
# displays all HTTP methods the server will accept.
curl -si "$1" | grep -i Allow | cut -d' ' -f 2-
