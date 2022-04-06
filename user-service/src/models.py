from flask_sqlalchemy import Model
from sqlalchemy import Column

from database import db


class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = Column(db.Integer, unique=True, primary_key=True, nullable=False)
    username = Column(db.String(100), unique=True, nullable=False)
    token: str = ''

    def __init__(self, username):
        db.Model.__init__(self, username=username)
