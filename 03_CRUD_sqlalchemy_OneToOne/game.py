from sqlalchemy import Column, String, Integer, Boolean
from base import Base

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    genre = Column(String)
    online = Column(Boolean)
    
    def __init__(self, name, genre, online):
        self.name = name
        self.genre = genre
        self.online = online