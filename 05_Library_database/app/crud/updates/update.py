from app import tables as t
from app import consults as c
from sqlalchemy.exc import IntegrityError


class NullName(Exception):
    """Raised when the input is null"""


class QuitProcess(Exception):
    """Raised when the confirmation is denied"""


def update_author():
    try:
        print("\t<< Enter current name of the Author you want to change: ")
        name = input(">> ")
        if not name:
            raise NullName
        author = c.consult_author(name)

        while author is None:
            print(
                f"\t<< Author not Found, do you wanna 'search' a new name, or 'quit'?"
            )
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Author's name: ")
                author = c.consult_author(input(">> "))
            elif choice == "quit":
                raise QuitProcess

        session = t.Session()
        author = session.query(t.Author).filter(t.Author.id == author.id).first()
        print(f"\t>> Type the new name for {author.name.title()}")
        # i need to query it again like this, so the program understands that i am selecting a table line, not just a random object
        name = input(">>").lower()
        if not name:
            raise NullName
        author.name = name
        session.flush()

        print(
            f"\t<< Confirm the change to '{author.name.title()}' in the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except QuitProcess:
        print("\t<< Process aborted.")

    except NullName:
        print("\t<< Author's name cannot be Null. Write something next time.")

    else:
        session.commit()
        print("\t<< Name succefully changed.")

    finally:
        session.close()


def update_category():
    try:
        print("\t<< Enter current name of the Category you wanna change: ")
        name = input(">> ")
        if not name:
            raise NullName
        category = c.consult_category(name)

        while category is None:
            print(
                f"\t<< Category not Found, do you wanna 'search' a new name, or 'quit'?"
            )
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Category's name: ")
                category = c.consult_category(input(">> "))
            elif choice == "quit":
                raise QuitProcess

        session = t.Session()
        category = (
            session.query(t.Category).filter(t.Category.id == category.id).first()
        )
        print(f"\t>> Type the new name for {category.type.title()}")
        # i need to query it again like this, so the program understands that i am selecting a table line, not just a random object
        name = input(">>").lower()
        if not name:
            raise NullName
        category.type = name
        session.flush()

        print(
            f"\t<< Confirm the change to '{category.type.title()}' in the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except QuitProcess:
        print("\t<< Process aborted.")

    except NullName:
        print("\t<< Category's name cannot be Null. Write something next time.")

    else:
        session.commit()
        print("\t<< Name succefully changed.")

    finally:
        session.close()


def update_publisher():
    try:
        print("\t<< Enter current name of the Publisher you want to change: ")
        name = input(">>")
        if not name:
            raise NullName
        publisher = c.consult_publisher(name)

        while publisher is None:
            print(
                f"\t<< Publisher not Found, do you wanna 'search' a new name, or 'quit'?"
            )
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Publisher's name: ")
                publisher = c.consult_publisher(input(">>"))
            elif choice == "quit":
                raise QuitProcess

        session = t.Session()
        publisher = (
            session.query(t.Publisher).filter(t.Publisher.id == publisher.id).first()
        )
        print(f"\t>> Type the new name for {publisher.name.title()}")
        # i need to query it again like this, so the program understands that i am selecting a table line, not just a random object
        name = input(">>").lower().split()
        if not name:
            raise NullName
        publisher.name = name
        session.flush()

        print(
            f"\t<< Confirm the change to '{publisher.name.title()}' in the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except QuitProcess:
        print("\t<< Process aborted.")

    except NullName:
        print("\t<< Publisher's name cannot be Null. Write something next time.")

    else:
        session.commit()
        print("\t<< Name succefully changed.")

    finally:
        session.close()


def update_book():
    try:
        session = t.Session()
        print("\t<< Enter current title of the Book you want to change: ")
        title = input(">>")
        if not title:
            raise NullName
        book = c.consult_book(title)

        while book is None:
            print(f"\t<< Book not Found, do you wanna 'search' again, or 'quit'?")
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Book's title: ")
                book = c.consult_book(input(">>"))
            elif choice == "quit":
                raise QuitProcess

        book = session.query(t.Book).filter(t.Book.id == book.id).first()

        urs_choice = "title author category categories publisher quit q".split()
        print(
            "\t<<< Do you wanna update the 'title', 'author', 'publisher' or 'categories' of the book? or 'quit'"
        )
        urs_inp = input(">> ").lower().strip()
        while urs_inp not in urs_choice:
            print("\t<< let's that try again... ")
            print(
                "\t<<< Do you wanna upate the 'title', 'author' or 'categories' of the book? or 'quit'"
            )
            urs_inp = input(">> ").lower().strip()

        if urs_inp == "q" or urs_inp == "quit":
            raise QuitProcess

        elif urs_inp == "title":
            print(f"\t>> Type the new title for the book {book.title.title()}")
            book.title = input(">>").lower()
            session.flush()

        elif urs_inp == "author":
            print(f"\t>> Type the correct author for the book {book.title.title()}")
            author = c.consult_author(input(">> "))
            while author is None:
                print(
                    f"\t<< Author not Found, do you wanna 'search' a new name, or 'quit'?"
                )
                if (choice := input(">> ").lower()) == "search":
                    print("\t<< Book's new Author: ")
                    author = c.consult_author(input(">> "))
                elif choice == "quit":
                    raise QuitProcess
            # author = session.query(t.Author).filter(t.Author.id == author.id).first()
            book.author = author
            session.flush()

        elif urs_inp == "category" or urs_inp == "categories":
            print("\t>> How many categories does the book has? (minimum: 1)")
            n_categories = int(input(">> "))
            if n_categories < 1:
                raise ValueError
            categories = []
            for i in range(0, n_categories):
                temp_cat = c.consult_category(input(f"\t<< Category {i+1}:\n>> "))
                while temp_cat is None:
                    print(
                        f"\t<< Category not Found, do you wanna 'search' for another cateogry, or 'quit'?"
                    )
                    if (choice := input(">> ").lower()) == "search":
                        print(f"\t<< Book's {i+1}th category: ")
                        temp_cat = c.consult_category(input(">> "))
                    elif choice == "quit":
                        raise QuitProcess
                # temp_cat = (
                #     session.query(t.Category)
                #     .filter(t.Category.type.id == temp_cat.id)
                #     .first()
                # )
                categories.append(temp_cat)
            book.category.clear()
            session.flush()
            book.category = categories
            session.flush()

        elif urs_inp == "publisher":
            print(f"\t>> Type the correct publisher for the book {book.title.title()}")
            publisher = c.consult_publisher(input(">> "))
            while publisher is None:
                print(
                    f"\t<< Publisher not Found, do you wanna 'search' a new name, or 'quit'?"
                )
                if (choice := input(">> ").lower()) == "search":
                    print("\t<< Book's new Publisher: ")
                    publisher = c.consult_publisher(input(">> "))
                elif choice == "quit":
                    raise QuitProcess
            # author = session.query(t.Author).filter(t.Author.id == author.id).first()
            book.publisher = publisher
            session.flush()

        # confirm book change
        print(f"\t<< Confirm the change of the book in the database ? (y/n)")
        print("\t+{}+{}+{}+{}+".format("=" * 30, "=" * 30, "=" * 30, "=" * 30))
        print(
            "\t| {:^28} | {:^28} | {:^28} | {:^28} |".format(
                "Book", "Author", "Publisher", "Cathegory"
            )
        )
        print("\t+{}+{}+{}+{}+".format("=" * 30, "=" * 30, "=" * 30, "=" * 30))
        string = ""
        [string := string + str(_) + "; " for _ in book.category]
        print(
            f"\t| {book.title.title():^29}"
            f"| {book.publisher.name.title():^29}"
            f"| {book.author.name.title():^29}"
            f"| {string.title():^28} |"
        )
        print("\t+{}+{}+{}+{}+".format("-" * 30, "-" * 30, "-" * 30, "-" * 30))
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except ValueError:
        print("\t<< number of category must be an INTENGER above 1")

    except QuitProcess:
        print("\t<< Process Aborted")

    except NullName:
        print("\t<< Publisher's name cannot be Null. Write something next time.")

    else:
        session.commit()
        print("\t<< Name succefully changed.")

    finally:
        session.close()
