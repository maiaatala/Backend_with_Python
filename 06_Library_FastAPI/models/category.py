# package requirements
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

# my_package imports
from config import Base


# many category to many books
class Category(Base):
    __tablename__ = "categories"

    name = Column(String, nullable=False, unique=True)

    categories_books = relationship(
        "Category_Book",
        back_populates="category",
        lazy="joined",
        cascade="all, delete, delete-orphan",
    )

    def __repr__(self):
        return f"<{self.name}>"
