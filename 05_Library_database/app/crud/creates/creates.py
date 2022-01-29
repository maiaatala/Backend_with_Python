from app import tables as t
from app import consults as c
from sqlalchemy.exc import IntegrityError


class NullName(Exception):
    """Raised when the input is null"""


class QuitProcess(Exception):
    """Raised when the confirmation is denied"""


def create_author(op=False):
    try:
        session = t.Session()
        print("\t<< Full name of the Author")
        name = input(">> ")
        if not name:
            raise NullName
        new_author = t.Author(name)
        session.add(new_author)
        session.flush()
        print(
            f"\t<< Confirm adding author '{new_author.name.title()}' to the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except IntegrityError:
        print(f"\t<< Author {name.title()} is already registered in the database.")

    except NullName:
        print("\t<< Author's name cannot be Null. Write their full name next time.")

    except QuitProcess:
        print("\t<< Process aborted.")

    except:
        print("\t<< An unexpected error occurred.")

    else:
        session.commit()
        print("\t<<Author Added succefully!")

    finally:
        session.close()
        if op:
            return c.consult_author(name)


def create_publisher(op=False):
    try:
        session = t.Session()
        print("\t<< Full name of the Publisher")
        name = input(">> ")
        if not name:
            raise NullName
        new_publisher = t.Publisher(name)
        session.add(new_publisher)
        session.flush()
        print(
            f"\t<< Confirm adding Publisher '{new_publisher.name.title()}' to the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except IntegrityError:
        print(f"\t<< Publisher {name.title()} is already registered in the database.")

    except NullName:
        print("\t<< Publisher's name cannot be Null. Write their full name next time.")

    except QuitProcess:
        print("\t<< Process aborted.")

    except:
        print("\t<< An unexpected error occurred.")

    else:
        session.commit()
        print("\t<< Publisher Added succefully!")

    finally:
        session.close()
        if op:
            return c.consult_publisher(name)


def create_category(op=False):
    try:
        session = t.Session()
        print("\t<< Full name of the Category")
        name = input(">> ")
        if not name:
            raise NullName
        new_category = t.Category(name)
        session.add(new_category)
        session.flush()
        print(
            f"\t<< Confirm adding Category '{new_category.type.title()}' to the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except IntegrityError:
        print(f"\t<< Publisher {name.title()} is already registered in the database.")

    except NullName:
        print("\t<< Category's name cannot be Null. Write something next time.")

    except QuitProcess:
        print("\t<< Process aborted.")

    except:
        print("\t<< An unexpected error occurred.")

    else:
        session.commit()
        print("\t<< Category Added succefully!")

    finally:
        session.close()
        if op:
            return c.consult_category(name)


def create_book():
    try:
        session = t.Session()
        print("\t<< Book's Author: ")
        author = c.consult_author(input(">> "))

        while author is None:
            print(
                f"\t<< Author not Found, do you wanna 'search' a new name, 'create' a new Author, or 'quit'?"
            )
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Book's Author: ")
                author = c.consult_author(input(">> "))
            elif choice == "create":
                author = create_author(True)
            elif choice == "quit":
                raise QuitProcess

        print("\t<< Book's Publisher: ")
        publisher = c.consult_publisher((input(">> ")))

        while publisher is None:
            print(
                f"\t<< Publisher not Found, do you wanna 'search' a new name, 'create' a new Publisher, or 'quit'?"
            )
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Book's Publisher: ")
                publisher = c.consult_publisher(input(">> "))
            elif choice == "create":
                publisher = create_publisher(True)
            elif choice == "quit":
                raise QuitProcess

        print("\t Book's FULL Title: ")
        title = input(">> ")
        if not title:
            raise NullName

        print("\t>> How many categories does the book has? (minimum: 1)")
        n_categories = int(input(">> "))
        categories = []
        for i in range(0, n_categories):
            temp_cat = c.consult_category(input(f"\t<< Category {i+1}:\n>> "))
            while temp_cat is None:
                print(
                    f"\t<< Category not Found, do you wanna 'search' for another cateogry,"
                    "'create' a new Category, or 'quit'?"
                )
                if (choice := input(">> ").lower()) == "search":
                    print(f"\t<< Book's {i+1}th category: ")
                    temp_cat = c.consult_category(input(">> "))
                elif choice == "create":
                    temp_cat = create_category(True)
                elif choice == "quit":
                    raise QuitProcess
            categories.append(temp_cat)

        author = session.query(t.Author).filter(t.Author.id == author.id).first()
        publisher = (
            session.query(t.Publisher).filter(t.Publisher.id == publisher.id).first()
        )
        new_book = t.Book(title, author, publisher)
        new_book.category = categories
        session.add(new_book)
        session.flush()

        # confirm new book block
        print(f"\t<< Confirm adding this Book to the database ? (y/n)")
        print("\t+{}+{}+{}+{}+".format("=" * 30, "=" * 30, "=" * 30, "=" * 30))
        print(
            "\t| {:^28} | {:^28} | {:^28} | {:^28} |".format(
                "Book", "Author", "Publisher", "Cathegory"
            )
        )
        print("\t+{}+{}+{}+{}+".format("=" * 30, "=" * 30, "=" * 30, "=" * 30))
        string = ""
        [string := string + str(_) + "; " for _ in new_book.category]
        print(
            f"\t| {new_book.title.title():^29}"
            f"| {new_book.publisher.name.title():^29}"
            f"| {new_book.author.name.title():^29}"
            f"| {string.title():^28} |"
        )
        print("\t+{}+{}+{}+{}+".format("-" * 30, "-" * 30, "-" * 30, "-" * 30))
        if (input(">> ").lower()) == "n":
            raise QuitProcess

    except NullName:
        print("\t<< Book's name cannot be Null. Write something next time.")

    except QuitProcess:
        print("\t<< Process aborted.")

    except ValueError:
        print("\t<< numbers of category IS A NUMBER")

    except:
        print("\t<< An unexpected error occurred.")

    else:
        session.commit()
        print("\t<< Books Added succefully!")

    finally:
        session.close()
