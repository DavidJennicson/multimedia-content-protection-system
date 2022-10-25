import random

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from uuid import uuid4
db= SQLAlchemy()
def get_uuid():
    return uuid4().hex

class Users(db.Model):
    __tablename__="users"
    id=db.Column(db.String(12),primary_key=True,unique=True,default=get_uuid)
    email=db.Column(db.String(356),unique=True)
    name=db.Column(db.String(100))
    password=db.Column(db.Text,nullable=False)


class Otp(db.Model):
    __tablename__="otpverification"
    id = db.Column(db.String(400), primary_key=True, unique=True)
    email=db.Column(db.String(356))
    generated_otp= db.Column(db.Integer(),unique=True)
    ctime = db.Column(db.DateTime, default=datetime.now)
    utime = db.Column(db.DateTime, default=datetime.now)
