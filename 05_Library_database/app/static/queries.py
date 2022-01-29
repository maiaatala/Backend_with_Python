# from book import Book
# from author import Author
# from category import Category, Category_Book
# from publisher import Publisher
# from base import Session

# from ..tables import Author, Book, Category, Category_Book, Publisher, Session, Base, engine

from app import tables as t

session = t.Session()

print("### ALL the books")
books = session.query(t.Book)\
    .all()
# print(books)
for book in books:
    string = ""
    for _ in book.category:
        string += str(_)+"; "
    print(f"{book.title:>24} by {book.author.name} in {string}")
print("")

print("### ALL the authors")
authors = session.query(t.Author).all()
for author in authors:
    print(f"\t{author.name}")
print("")

print("### Books by allen")
books_allen = session.query(t.Book)\
    .join(t.Author)\
    .filter(t.Author.name.ilike('%allen % downey%'))\
    .all()
for book in books_allen:
    print(f"{book.title:>24} by {book.author.name}")
print("")

print("### all the categories")
categories = session.query(Category).all()
for category in categories:
    print(f"{category.type} | {category.book}")
    # print(f"\t{category.type}")
print("")

print("### association table: ")
assos = session.query(Category_Book).all()
for ass in assos:
    print(ass)
print()

print("### All the programming books:")
books_prog = session.query(Book)\
    .join(Category_Book, Category)\
    .filter(Category.type.ilike("programming"))\
    .all()
for book in books_prog:
    print(f"{book.title:>24} by {book.author.name}")
print("")

print("### All the math books:")
books_prog = session.query(Book)\
    .join(Category_Book, Category)\
    .filter(Category.type.ilike("math%"))\
    .all()
if books_prog:
    for book in books_prog:
        print(f"{book.title:>24} by {book.author.name}")
    print("")

session.close()
