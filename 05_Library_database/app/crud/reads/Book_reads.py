from app import tables as t
from app import header as h


def show_all_books():
    session = t.Session()
    books = session.query(t.Book).order_by(t.Book.title).all()
    h.theader("book")

    for book in books:
        string = ""
        for _ in book.category:
            string += str(_) + "; "
        print(
            f"\t| {book.title.title():^29}"
            f"| {book.publisher.name.title():^29}"
            f"| {book.author.name.title():^29}"
            f"| {string.title():^28} |"
        )
        print("\t+{}+{}+{}+{}+".format("-" * 30, "-" * 30, "-" * 30, "-" * 30))
    print("")
    session.close()


""" author, publisher, genre """


def books_by(name, by_option):
    session = t.Session()
    sep = "%"
    name_s = sep + sep.join(name) + sep
    if by_option == "author":
        author = session.query(t.Author).filter(t.Author.name.ilike(name_s)).first()
        books = (
            session.query(t.Book)
            .join(t.Author)
            .filter(t.Author.name == author.name)
            .order_by(t.Book.title)
            .all()
        )

        print(f"\t\tBooks by {author.name.title()}:")
        h.theader("book")
        for book in books:
            string = ""
            [string := string + str(_) + "; " for _ in book.category]
            print(
                f"\t| {book.title.title():^29}"
                f"| {book.publisher.name.title():^29}"
                f"| {book.author.name.title():^29}"
                f"| {string.title():^28} |"
            )
            print("\t+{}+{}+{}+{}+".format("-" * 30, "-" * 30, "-" * 30, "-" * 30))
        print("")

    elif by_option == "publisher":
        publisher = (
            session.query(t.Publisher).filter(t.Publisher.name.ilike(name_s)).first()
        )
        books = (
            session.query(t.Book)
            .join(t.Publisher)
            .filter(t.Publisher.name == publisher.name)
            .order_by(t.Book.title)
            .all()
        )

        print(f"\t\tBooks by {publisher.name.title()}:")
        h.theader("book")
        for book in books:
            string = ""
            [string := string + str(_) + "; " for _ in book.category]
            print(
                f"\t| {book.title.title():^29}"
                f"| {book.publisher.name.title():^29}"
                f"| {book.author.name.title():^29}"
                f"| {string.title():^28} |"
            )
            print("\t+{}+{}+{}+{}+".format("-" * 30, "-" * 30, "-" * 30, "-" * 30))
        print("")

    elif by_option == "genre":
        genre = session.query(t.Category).filter(t.Category.type.ilike(name_s)).first()
        books = (
            session.query(t.Book)
            .join(t.Category_Book, t.Category)
            .filter(t.Category.type == genre.type)
            .order_by(t.Book.title)
            .all()
        )

        print(f"\t\tBooks in {genre.type.title()}:")
        h.theader("book")
        for book in books:
            string = ""
            [string := string + str(_) + "; " for _ in book.category]
            print(
                f"\t| {book.title.title():^29}"
                f"| {book.publisher.name.title():^29}"
                f"| {book.author.name.title():^29}"
                f"| {string.title():^28} |"
            )
            print("\t+{}+{}+{}+{}+".format("-" * 30, "-" * 30, "-" * 30, "-" * 30))
        print()

    else:
        print("No data can be found for the requested search")

    session.close()


def search_books(title):
    session = t.Session()
    sep = "%"
    title_s = sep + sep.join(title) + sep
    book = session.query(t.Book).filter(t.Book.title.ilike(title_s)).all()
    if book:
        h.theader("book")
        for b in book:
            string = ""
            [string := string + str(_) + "; " for _ in b.category]
            print(
                f"\t| {b.title.title():^29}"
                f"| {b.publisher.name.title():^29}"
                f"| {b.author.name.title():^29}"
                f"| {string.title():^28} |"
            )
            print("\t+{}+{}+{}+{}+".format("-" * 30, "-" * 30, "-" * 30, "-" * 30))
        print()
    session.close()
