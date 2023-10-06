import os
# my_app.py
from settings import db_server, db_user, db_password

server = os.getenv('MY_APP_DB_SERVER', 'localhost')
user = os.getenv('MY_APP_DB_USER', 'myapp')
password = os.getenv('MY_APP_DB_PASSWORD', '')


