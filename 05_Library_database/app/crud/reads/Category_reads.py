from app import tables as t
from app import header as h


def show_all_categories():
    session = t.Session()
    categories = session.query(t.Category).order_by(t.Category.type).all()
    h.theader("category")
    # print(categories)
    for category in categories:
        print(f"\t| {category.type.title():^28} |")
        print("\t+{}+".format("-" * 30))
    print("")
    session.close()


def search_category(name):
    session = t.Session()
    sep = "%"
    # name_s = name.split()
    name_s = sep + sep.join(name) + sep
    category = session.query(t.Category).filter(t.Category.type.ilike(name_s)).all()
    if category:
        h.theader("category")
        for c in category:
            print(f"\t| {c.type.title():^28} |")
            print("\t+{}+".format("-" * 30))
        print("")
    else:
        print(f"\t{name} isn't on the database\n")
    # return category ?
    # Do i keep it as a show function, os a a utility function??
    session.close()
