#!/bin/bash

URL="$1"

curl -s "$URL" | grep -o '"[^"]*"' | cut -d'"' -f2
