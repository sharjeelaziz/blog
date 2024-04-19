#!/bin/bash

# script with set -o pipefail
set -o pipefail

cat doesnotexist.txt | grep "error" | wc -l
echo "Processing complete for file does not exist. Exit status: $?"

cat file.txt | grep "error" | wc -l
echo "Processing complete. Exit status: $?"