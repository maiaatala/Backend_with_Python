# from book import t.Book
# from author import t.Author
# from category import t.Category, Category_Book
# from publisher import t.Publisher
# from base import Base, Session, engine

from app import tables as t

t.Base.metadata.create_all(t.engine)

session = t.Session()

# creating autor
allen_b = t.Author("Allen B. Downey")
sun = t.Author("Sun Tzu")
luiz = t.Author("Luiz Paulo Favero")
neal = t.Author("Neal Ford")

# creating publishers
record = t.Publisher("Record ltda")
elsevier = t.Publisher("Elsevier Ltda")
reilly = t.Publisher("O'reilly Media")

# creating books
pense = t.Book("Pense em Python", allen_b, reilly)
metodos = t.Book("Métodos quantitativos", luiz, elsevier)
arte = t.Book("A Arte da Guerra", sun, record)
stats = t.Book("Think Stats", allen_b, reilly)
java = t.Book("Pense Java", allen_b, reilly)
functional = t.Book("Functional Thinking", neal, reilly)

# creating genre
prog = t.Category("Programming")
math = t.Category("Mathematics")
strategy = t.Category("Strategy")

# add books to category     # BOTH METODOS WORK! NEEDS TO BE A LIST
prog.book = [pense, stats, java, functional]
math.book = [metodos, stats]
strategy.book = [arte, functional]

# add category to the books  # BOTH METODOS WORK! NEEDS TO BE A LIST
# pense.category = [prog]
# metodos.category = [math]
# arte.category = [strategy]
# stats.category = [math, prog]
# java.category = [prog]
# functional.category = [prog, strategy]

# adding all to the db
session.add_all(
    [
        allen_b,
        sun,
        luiz,
        pense,
        metodos,
        arte,
        stats,
        java,
        prog,
        math,
        strategy,
        record,
        elsevier,
        reilly,
    ]
)

# session.add_all([record, elsevier, reilly])

# commiting
session.commit()

session.close()
