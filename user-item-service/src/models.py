from sqlalchemy import Column

from database import db


class UserItem(db.Model):
    __tablename__ = 'user_item'
    __table_args__ = {'extend_existing': True}
    id = Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(db.Integer, index=True, nullable=False)
    item_id = Column(db.Integer, index=True, nullable=False)

    def __init__(self, user_id, item_id):
        db.Model.__init__(self, user_id=user_id, item_id=item_id)
