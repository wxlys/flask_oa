from exts import db
from datetime import datetime

class UserModle(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now)