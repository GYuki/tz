from sqlalchemy import Column

from database import db


class UserData(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = Column(db.Integer, unique=True, primary_key=True, nullable=False)
    player_id = Column(db.Integer, unique=True, nullable=False)
    balance = Column(db.Integer, nullable=False, default=1000)

    def __init__(self, player_id):
        db.Model.__init__(self, player_id=player_id)
