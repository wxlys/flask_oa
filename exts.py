from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
db = SQLAlchemy()
mail = Mail()