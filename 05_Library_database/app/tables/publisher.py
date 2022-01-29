from sqlalchemy import Column, String, Integer, ForeignKey, Table
from .base import Base

# ONE publishers to many books
class Publisher(Base):
    __tablename__ = "publishers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __init__(self, name):
        self.name = (" ").join(name.lower().split())

    def __repr__(self):
        return f"Publisher: {self.name}"
