# package requirements
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

# my_package imports
from config import Base


class Category_Book(Base):
    __tablename__ = "categories_books"

    categories_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    books_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))

    book = relationship("Book", back_populates="categories_books", lazy="joined")
    category = relationship(
        "Category", back_populates="categories_books", lazy="joined"
    )
