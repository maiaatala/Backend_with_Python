# package requirements
from sqlalchemy import Column, Date, String
from sqlalchemy.orm import relationship

# my_package imports
from config import Base


class Author(Base):
    __tablename__ = "authors"
    name = Column(String, nullable=False, unique=True)
    birthdate = Column(Date)
    books = relationship(
        "Book",
        back_populates="author",
        cascade="all, delete, delete-orphan",
        lazy="joined",
    )
