from app import tables as t
from app import consults as c
from app.crud import reads as r
from sqlalchemy.exc import OperationalError


class QuitProcess(Exception):
    """Raised when the confirmation is denied"""


class NullName(Exception):
    """Raised when the input is null"""


def delete_author():
    try:
        session = t.Session()
        print("\t<< Enter current name of the Author you want to delete: ")
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
        # i need to query it again like this, so the program understands that i am selecting a table line, not just a random object
        # author = session.query(t.Author).filter(t.Author.id == author.id).first()

        # books_affected = session.query(t.Book).join(t.Author).filter(t.Author.id == author.id).order_by(t.Book.title).all()
        print("\t << Books that will be DELETED with the author: ")
        r.books_by(author.name, "author")

        print(
            f"\t<< Confirm the DELETION of '{author.name.title()}' AND ALL THEIR BOOKS in the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

        session.delete(author)
        session.flush()

    except QuitProcess:
        print("\t<< Process aborted.")

    except NullName:
        print("\t<< Author's name cannot be Null. Write something next time.")

    except OperationalError:
        print("\t<< Db file is not here!")

    except Exception:
        print("\t<< Oops. something happened.")

    else:
        session.commit()
        print("\t<< Author succefully deleted.")

    finally:
        session.close()


def delete_publisher():
    try:
        session = t.Session()
        print("\t<< Enter current name of the Publisher you want to delete: ")
        name = input(">> ")
        if not name:
            raise NullName
        publisher = c.consult_publisher(name)

        while publisher is None:
            print(
                f"\t<< Publisher not Found, do you wanna 'search' a new name, or 'quit'?"
            )
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Publisher's name: ")
                publisher = c.consult_publisher(input(">> "))
            elif choice == "quit":
                raise QuitProcess
        # i need to query it again like this, so the program understands that i am selecting a table line, not just a random object
        # author = session.query(t.Author).filter(t.Author.id == author.id).first()

        print("\t << Books that will be DELETED with the Publisher: ")
        r.books_by(publisher.name, "publisher")

        print(
            f"\t<< Confirm the DELETION of '{publisher.name.title()}' and ALL IT'S BOOKS in the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

        session.delete(publisher)
        session.flush()

    except QuitProcess:
        print("\t<< Process aborted.")

    except NullName:
        print("\t<< Publisher's name cannot be Null. Write something next time.")

    except OperationalError:
        print("\t<< Db file is not here!")

    except Exception:
        print("\t<< Oops. something happened.")

    else:
        session.commit()
        print("\t<< Publisher succefully deleted.")

    finally:
        session.close()


def delete_book():
    try:
        session = t.Session()
        print("\t<< Enter current title of the Book you want to delete: ")
        title = input(">> ")
        if not title:
            raise NullName
        book = c.consult_book(title)

        while book is None:
            print(f"\t<< Book not Found, do you wanna 'search' a new name, or 'quit'?")
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Book's title: ")
                book = c.consult_book(input(">> "))
            elif choice == "quit":
                raise QuitProcess
        # i need to query it again like this, so the program understands that i am selecting a table line, not just a random object
        # author = session.query(t.Author).filter(t.Author.id == author.id).first()

        print("\t << Book that will be deleted: ")
        r.search_books(book.title)

        print(
            f"\t<< Confirm the DELETION of '{book.title.title()}' in the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

        session.delete(book)
        session.flush()

    except QuitProcess:
        print("\t<< Process aborted.")

    except NullName:
        print("\t<< Book's name cannot be Null. Write something next time.")

    except OperationalError:
        print("\t<< Db file is not here!")

    except Exception:
        print("\t<< Oops. something happened.")

    else:
        session.commit()
        print("\t<< Book succefully deleted.")

    finally:
        session.close()


def delete_genre():
    try:
        session = t.Session()
        print("\t<< Enter current name of the Category you want to delete: ")
        name = input(">> ")
        if not name:
            raise NullName
        genre = c.consult_category(name)

        while genre is None:
            print(
                f"\t<< Category not Found, do you wanna 'search' a new name, or 'quit'?"
            )
            if (choice := input(">> ").lower()) == "search":
                print("\t<< Category's name: ")
                genre = c.consult_publisher(input(">> "))
            elif choice == "quit":
                raise QuitProcess
        # i need to query it again like this, so the program understands that i am selecting a table line, not just a random object
        # author = session.query(t.Author).filter(t.Author.id == author.id).first()

        print("\t << Books that will be affected by Genre deletion: ")
        r.books_by(genre.type, "genre")

        print(
            f"\t<< Confirm the DELETION of '{genre.type.title()}' in the database? (y/n)"
        )
        if (input(">> ").lower()) == "n":
            raise QuitProcess

        session.delete(genre)
        session.flush()

    except QuitProcess:
        print("\t<< Process aborted.")

    except NullName:
        print("\t<< Category's name cannot be Null. Write something next time.")

    except OperationalError:
        print("\t<< Db file is not here!")

    except Exception:
        print("\t<< Oops. something happened.")

    else:
        session.commit()
        print("\t<< Category succefully deleted.")

    finally:
        session.close()
