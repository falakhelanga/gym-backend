#!/bin/sh

set -e

echo "Checking mounted volumes..."
ls -la /vol/
ls -la /vol/web

echo "Running as user: $(whoami)"

# Ensure the database is ready before proceeding
/venv/bin/python3 manage.py wait_for_db

echo "Collecting static files..."
/venv/bin/python3 manage.py collectstatic --noinput

echo "Applying database migrations..."
/venv/bin/python3 manage.py migrate

# Start Gunicorn
echo "Starting Gunicorn..."
exec /venv/bin/gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3