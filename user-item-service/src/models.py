from sqlalchemy import Column

from database import db


class UserItem(db.Model):
    __tablename__ = 'user_item'
    __table_args__ = {'extend_existing': True}
    user_id = Column(db.Integer, index=True)
    item_id = Column(db.Integer, index=True)
