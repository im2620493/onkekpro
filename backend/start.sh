#!/bin/bash

retry=10
echo -n "Trying migrations"
for i in $(seq $retry)
do
  echo -n .
  python manage.py migrate && break
  sleep 1
done

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    python manage.py createsuperuser --no-input
fi

python manage.py collectstatic --noinput

echo "=Starting runserver="
gunicorn app.wsgi:application \
         --bind 0.0.0.0:8001
