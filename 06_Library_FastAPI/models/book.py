# package requirements
from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

# my_package imports
from config import Base

# many books to one author
# many books to many categories
# many books to one publishers
class Book(Base):
    __tablename__ = "books"

    title = Column(String, nullable=False)
    subtitle = Column(String)
    publish_date = Column(Date)

    # many boooks to one author
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship(
        "Author",
        back_populates="books",
        lazy="joined",
    )

    # many books to many categories
    categories_books = relationship(
        "Category_Book",
        back_populates="book",
        lazy="joined",
        cascade="all, delete, delete-orphan",
    )

    def __repr__(self):
        return f"<{self.title}> <self.categories_books>"


# the back_populates will allow the search to be bidirectional
# the backref books WILL CREATE a author.books relationship on the PARENT table (Author) that is a LIST
# lazy= joined will load the necessary information into the schemas
