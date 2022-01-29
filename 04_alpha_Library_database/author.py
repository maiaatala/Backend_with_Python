from sqlalchemy import Column, String, Integer
from base import Base

# F_id's -> children

# one author to many books
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __init__(self, name):
        self.name = name.lower()

    def __repr__(self):
        return (f"Author: {self.name}")
