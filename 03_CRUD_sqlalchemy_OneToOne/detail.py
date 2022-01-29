from sqlalchemy import Column, Float, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, backref
from base import Base

class Detail(Base):
    __tablename__ = 'details'

    id = Column(Integer, primary_key=True)
    price = Column(Float)
    released = Column(Date)
    game_id = Column(Integer, ForeignKey('games.id'))
    game = relationship("Game", backref=backref("details", cascade="all,delete,delete-orphan"), uselist=False)

    def __init__(self, price, released, game):
        self.price = price
        self.released = released
        self.game = game