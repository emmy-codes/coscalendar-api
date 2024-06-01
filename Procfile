release: python manage.py makemigrations && python manage.py migrate
web: gunicorn coscalendar_api.wsgi