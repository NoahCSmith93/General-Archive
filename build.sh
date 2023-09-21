pip install -r requirements.txt

pip install django
pip install dj-database-url
pip install django-environ
pip install gunicorn
pip install psycopg2-binary
pip install whitenoise

python manage.py collectstatic --no-input
python manage.py migrate