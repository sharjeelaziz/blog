#!/bin/bash

execution_time=$((RANDOM % 5 + 1))

execution_time_seconds=$((execution_time * 60))

failure_chance=$((RANDOM % 100 + 1))

echo "Deployment will take will $execution_time minutes."
sleep $execution_time_seconds

# Check if deployment should fail (10% chance)
if [ $failure_chance -le 10 ]; then
  echo "Tests failed!"
  exit 1
else
  echo "All tests passed!"
  exit 0
fi
