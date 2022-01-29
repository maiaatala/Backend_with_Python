from app import tables as t
from app import header as h


def show_all_publishers():
    session = t.Session()
    publishers = session.query(t.Publisher).order_by(t.Publisher.name).all()
    h.theader("publisher")
    for publisher in publishers:
        print(f"\t| {publisher.name.title():^28} |")
        print("\t+{}+".format("-" * 30))
    print("")
    session.close()


def search_publisher(name):
    session = t.Session()
    sep = "%"
    # name_s = name.split()
    name_s = sep + sep.join(name) + sep
    publisher = session.query(t.Publisher).filter(t.Publisher.name.ilike(name_s)).all()
    if publisher:
        h.theader("Publisher")
        for p in publisher:
            print(f"\t| {p.name.title():^28} |")
            print("\t+{}+".format("-" * 30))
        print("")
    else:
        print(f"\t{name} isn't on the database\n")
    # return Publisher ?
    # Do i keep it as a show function, os a a utility function??
    session.close()
