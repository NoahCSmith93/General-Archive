pip3 install --upgrade pip
pip3 install -r requirements.txt

pip install django
pip install dj-database-url
pip install django-environ
pip install gunicorn
pip install psycopg2-binary
pip install whitenoise

python3 manage.py collectstatic --no-input
python3 manage.py migrate