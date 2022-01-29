from book import Book
from author import Author
from publisher import Publisher
from category import Category, Category_Book
from base import Session

session = Session()

print("### all the books")
books = session.query(Book).all()
for book in books:
    string = ""
    for _ in book.category:
        string += str(_)+"; "
    print(f"{book.title.title():>24} by {book.author.name.title():<18} published by {book.publisher.name.title():<15} in {string}")
print("")

print('### all books by reilly media')
books = session.query(Book).join(Publisher)\
    .filter(Publisher.name.ilike('%reilly%')).all()
for book in books:
    print(f"{book.title.title():>24} by {book.author.name.title():<18}")
print("")

print("### All books by Reilly in strategy")
books = session.query(Book).join(Category_Book, Category).join(Publisher)\
    .filter(Publisher.name.ilike('%reilly%')).filter(Category.type.ilike('%strategy%')).all()
for book in books:
    print(f"{book.title.title():>24} by {book.author.name.title():<18}")
print("")

session.close()

# # deleting publisher        WORKS!
# session = Session()
# elsevier = session.query(Publisher).filter(Publisher.name.ilike('%elsevier%')).first()
# if elsevier:
#     session.delete(elsevier)
#     session.commit()

# print("### all the books")
# books = session.query(Book).all()
# for book in books:
#     string = ""
#     for _ in book.category:
#         string += str(_)+"; "
#     print(f"{book.title.title():>24} by {book.author.name.title():<18} published by {book.publisher.name.title():<15} in {string}")
# print("")
# session.close()