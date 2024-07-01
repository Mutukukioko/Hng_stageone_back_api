web: gunicorn back_api.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn back_api.wsg