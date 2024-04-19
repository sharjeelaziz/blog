#!/bin/bash

# script without set -x
for file in "$@"; do
    if [ -f "$file" ]; then
        process_file "$file"
    fi
done