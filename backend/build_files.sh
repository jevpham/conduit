pip install -r requirements.txt
python manage.py collectstatic
python manage.py migrate
python manage.py shell -c "from django.db import connection; connection.cursor()"