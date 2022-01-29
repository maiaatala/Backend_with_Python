from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import backref, relationship
from base import Base

class Category_Book(Base):
    __tablename__ = "categories_books"
    
    category_book_id = Column(Integer,primary_key=True)    
    categories_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    books_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"))
    
    # don't think i need these??
    # book = relationship('Book', backref='category_categories_books')
    # category = relationship('Category', backref='book_categories_books')
    
    def __repr__(self):
        return(f"Book: {self.books_id} | category: {self.categories_id}")

# many category to many books
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    type = Column(String)

    book = relationship("Book", secondary="categories_books", back_populates="category")
    
    def __init__(self, type):
        self.type = type.lower()
    
    def __repr__(self):
        return (f"{self.type}")
