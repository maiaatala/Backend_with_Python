from app import tables as t
from app import header as h
from sqlalchemy.exc import OperationalError

# show
def show_all_authors():
    try:
        session = t.Session()
        authors = session.query(t.Author).order_by(t.Author.name).all()
        h.theader("author")
        for author in authors:
            print(f"\t| {author.name.title():^28} |")
            print("\t+{}+".format("-" * 30))
        print("")

    except OperationalError:
        print("\tNo database to be found")

    except:
        print("\tAn unexpected error occurred.")

    finally:
        session.close()


def search_author(name):
    sep = "%"
    name_s = sep + sep.join(name) + sep
    try:
        session = t.Session()
        author = session.query(t.Author).filter(t.Author.name.ilike(name_s)).all()
        if author:
            h.theader("author")
            for a in author:
                print(f"\t| {a.name.title():^28} |")
                print("\t+{}+".format("-" * 30))
            print("")
        else:
            print(f"\t{name} isn't on the database\n")

    except OperationalError:
        print("\tNo database to be found")

    except:
        print("\tAn unexpected error occurred.")

    finally:
        session.close()
