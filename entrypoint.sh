#!/bin/sh

cd /watts_app

python manage.py makemigrations
python manage.py migrate --noinput
python excel_to_json
python manage.py loaddata fixture.json
python manage.py runserver 0.0.0.0:8000
