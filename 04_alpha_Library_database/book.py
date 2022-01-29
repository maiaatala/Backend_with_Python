from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import backref, relationship
from base import Base

# many books to one author
# many books to many categories
# many books to many publishers
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    subtitle = Column(String, nullable=True)
    
    # many books to one author
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship("Author", backref=backref('books', cascade="all, delete, delete-orphan"))

    # many books to one publisher
    publisher_id = Column(Integer, ForeignKey('publishers.id'))
    publisher = relationship("Publisher", backref=backref('books', cascade="all, delete, delete-orphan"))
    
    # many books to many categories 
    category = relationship("Category", secondary="categories_books", back_populates = "book")
    # category = relationship("Category_Book", back_populates="book_all")
    
    def __init__(self, title, subtitle, author, publisher):
        self.title = title.lower()
        self.subtitle = subtitle.lower()
        self.author = author
        self.publisher = publisher
    
    def __repr__(self):
        return (f"<{self.title} | {self.author.name} | {self.category}>")
