from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import backref, relationship
from .base import Base

# assossiation table to make the communication between categories and books
class Category_Book(Base):
    __tablename__ = "categories_books"

    category_book_id = Column(Integer, primary_key=True)
    categories_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    books_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))

    def __repr__(self):
        return f"Book: {self.books_id} | category: {self.categories_id}"


# many category to many books
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    type = Column(String, unique=True, nullable=False)

    book = relationship("Book", secondary="categories_books", back_populates="category")
    # back_populates is the attribute that allows us to have the cateogry in the book object
    # secondary is the attribute that makes the relationship into a many to many

    def __init__(self, type):
        self.type = (" ").join(type.lower().split())

    def __repr__(self):
        return f"{self.type}"
