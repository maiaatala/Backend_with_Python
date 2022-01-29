from app import tables as t
from sqlalchemy.exc import OperationalError, MultipleResultsFound, NoResultFound


def consult_author(name):
    sep = "%"
    name_s = sep + sep.join(name) + sep

    try:
        session = t.Session()
        author = session.query(t.Author).filter(t.Author.name.ilike(name_s)).one()

    except OperationalError:
        author = None

    except MultipleResultsFound:
        author = None
        print(
            "\t<< Multiple results were found for that search, try to be more specific!"
        )

    except NoResultFound:
        author = None

    except:
        author = None

    finally:
        session.close()
        return author


def consult_publisher(name):
    sep = "%"
    name_s = sep + sep.join(name) + sep

    try:
        session = t.Session()
        publisher = (
            session.query(t.Publisher).filter(t.Publisher.name.ilike(name_s)).one()
        )

    except OperationalError:
        publisher = None

    except MultipleResultsFound:
        publisher = None
        print(
            "\t<< Multiple results were found for that search, try to be more specific!"
        )

    except NoResultFound:
        publisher = None

    except:
        publisher = None

    finally:
        session.close()
        return publisher


def consult_category(name):
    sep = "%"
    name_s = sep + sep.join(name) + sep

    try:
        session = t.Session()
        category = session.query(t.Category).filter(t.Category.type.ilike(name_s)).one()

    except MultipleResultsFound:
        category = None
        print(
            "\t<< Multiple results were found for that search, try to be more specific!"
        )

    except OperationalError:
        category = None

    except NoResultFound:
        category = None

    except:
        category = None

    finally:
        session.close()
        return category


def consult_book(title):
    sep = "%"
    title_s = sep + sep.join(title) + sep

    try:
        session = t.Session()
        book = session.query(t.Book).filter(t.Book.title.ilike(title_s)).one()
        # if (l := len(book)) > 1:
        #     print(
        #         "\t<< Multiple results found! specify the book's ID from the followig list:"
        #     )
        #     for b in book:
        #         print(f"\t    {b.id}: {b.title.title()} from {b.author.title()}")
        #     i = int(input(">> "))
        #     book = session.query(t.Book).filter(t.Book.id == i).one()
        # else:
        #     print(book)

    except MultipleResultsFound:
        book = None
        print("\t<< Multiple books were found, try to be more specific!")

    except OperationalError:
        book = None

    except ValueError:
        print("\t<< The book's ID must be a NUMBER")

    except IndexError:
        print("\t<< Type a number that exists in the list!")

    except:
        book = None

    finally:
        session.close()
        return book


def orphan_books_list(name, op):
    pass
