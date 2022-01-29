# from book import Book
# from author import Author
# from category import Category, Category_Book
# from publisher import Publisher
# from base import Session

from tables import *

# Deleting
# session = Session()
# deleting category     WORKS
# math = session.query(Category).filter(Category.type.ilike('math%')).first()
# if math:
#     print(math)
#     needed_update = session.query(Book).join(Category_Book, Category).filter(Category.type.ilike('math%')).all()
#     session.delete(math)
#     session.commit()
    # for book in needed_update:
    #     print(f"\tEnter new category for {book.title}\n\tCurrent categories: {book.category}")
    #     inp = input("> ")
    #     new = Category(inp)
    #     book.category.append(new)
# deleting Book     WORKS
# pense = session.query(Book).filter(Book.title.ilike("pense em python")).first()
# session.delete(pense)
# session.commit()
# session.close()

# deleting author, DELETES ALL BOOKS BY THAT AUTHOR WORKS
# session = Session()
# allen = session.query(Author).filter(Author.name.ilike('%allen%')).first()
# if allen:
#     session.delete(allen)
#     session.commit()
# session.close()

# # UPDATING WORKS
# stats = session.query(Book).filter(Book.title.ilike("%stats")).first()
# if stats:
#     math = session.query(Category).filter(Category.type.ilike("%math%")).first()
#     # YOU HAVE TO WORK IT LIKE A LIST
#     stats.category.clear()
#     stats.category.append(math)
#     session.commit()

## popping a book from category WORKS!
# session = Session()
# stats = session.query(Book).filter(Book.title.ilike('think stats')).first()
# prog = session.query(Category).filter(Category.type.ilike('%prog%')).first()
# if stats in prog.book:
#     prog.book.remove(stats)
#     session.commit()
# session.close()

# print("### ALL the books")
# session = Session()
# books = session.query(Book)\
#     .all()
# for book in books:
#     string = ""
#     for _ in book.category:
#         string += str(_)+"; "
#     print(f"{book.title:>24} by {book.author.name} in {string}")
# print("")
# session.close()

# print("### all the categories")
# session = Session()
# categories = session.query(Category).all()
# for category in categories:
#     print(f"{category.type} | {category.book}")
#     # print(f"\t{category.type}")
# print("")
# session.close()

# print("### association table: ")
# assos = session.query(Category_Book).all()
# for ass in assos:
#     print(ass)
# print()