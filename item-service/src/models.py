from sqlalchemy import Column

from database import db


class Item(db.Model):
    __tablename__ = 'item'
    __table_args__ = {'extend_existing': True}
    id = Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = Column(db.String(100), unique=True, nullable=False)
    price = Column(db.Integer, nullable=False)

    def __init__(self, name, price):
        db.Model.__init__(self, name=name, price=price)
