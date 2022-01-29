from sqlalchemy import Column, String, Integer, ForeignKey, Table
from base import Base

# ONE publishers to many books
class Publisher(Base):
    __tablename__ = "publishers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name.lower()
    
    def __repr__(self):
        return(f'Publisher: {self.name}')
