#!/bin/bash

set -x

# script with set -x
for file in "$@"; do
    if [ -f "$file" ]; then
        process_file "$file"
    fi
done