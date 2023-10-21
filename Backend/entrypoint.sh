#!/bin/bash

# Run the Python commands
python3.8 manage.py makemigrations
python3.8 manage.py migrate
python3.8 manage.py runserver 0.0.0.0:8000

# Use "exec" to replace the current shell with the specified command
exec "$@"
