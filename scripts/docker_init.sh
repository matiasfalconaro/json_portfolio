#!/bin/bash

set -e

echo "=========================================="
echo "Portfolio Application Initialization"
echo "=========================================="

echo "Waiting for MongoDB to be ready..."
until nc -z mongo 27017; do
  echo "MongoDB is unavailable - sleeping"
  sleep 2
done
echo "✓ MongoDB is ready!"

echo "Initializing database collections..."
python -c "from database.db import init_collections; init_collections()"
echo "✓ Database collections initialized!"

echo "Loading portfolio data from resume.json..."
python portfolio/data.py
echo "✓ Portfolio data loaded!"

echo "Checking for admin user..."
python -c "
from database.repository import get_user, create_user
import os

username = os.getenv('DEFAULT_ADMIN_USER', 'admin')
password = os.getenv('DEFAULT_ADMIN_PASSWORD', '')

if not get_user(username):
    if password:
        create_user(username, password)
        print(f'✓ Default admin user \"{username}\" created!')
        print('⚠ IMPORTANT: Change the default password in production!')
    else:
        print('⚠ No default admin user created. Set DEFAULT_ADMIN_USER and DEFAULT_ADMIN_PASSWORD environment variables.')
        print('  Or use: docker exec -it <container> python scripts/create_admin_user.py')
else:
    print(f'✓ Admin user \"{username}\" already exists.')
"

echo "=========================================="
echo "Starting Reflex application..."
echo "=========================================="

exec reflex run --backend-host 0.0.0.0 --loglevel debug
