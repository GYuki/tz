from flask_sqlalchemy import Model
from sqlalchemy import Column

from database import db


class User(Model):
    __tablename__ = 'user'
    id = Column(db.Int(), unique=True, primary_key=True, nullable=False)
    username = Column(db.String(100), unique=True, nullable=False)
    token: str = ''
