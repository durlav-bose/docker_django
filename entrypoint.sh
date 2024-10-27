# entrypoint.sh
#!/bin/sh

# Wait for database if you're using PostgreSQL
# python manage.py wait_for_db

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Start server
python manage.py runserver 0.0.0.0:8000