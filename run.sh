#!/bin/bash

# Run the Python commands

docker-compose up --build
# Use "exec" to replace the current shell with the specified command
exec "$@"
