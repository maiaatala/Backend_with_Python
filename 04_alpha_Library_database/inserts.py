from book import Book
from author import Author
from category import Category, Category_Book
from publisher import Publisher
from base import Base, Session, engine

Base.metadata.create_all(engine)

session = Session()

# creating autor
allen_b = Author("Allen B. Downey")
sun = Author("Sun Tzu")
luiz = Author("Luiz Paulo Favero")
neal = Author('Neal Ford')

# creating publishers
record = Publisher('Record ltda')
elsevier = Publisher('Elsevier Ltda')
reilly = Publisher("O'reilly Media")

# creating books
pense = Book("Pense em Python", "Pense como um cientista da computação", allen_b, reilly)
metodos = Book("Métodos quantitativos", "", luiz, elsevier)
arte = Book("A Arte da Guerra", "", sun, record)
stats = Book("Think Stats", "", allen_b, reilly)
java = Book("Pense Java", "Pense como um cientista da computação", allen_b, reilly)
functional = Book("Functional Thinking", "Paradigm Over Sintax", neal, reilly)

# creating genre
prog = Category("Programming")
math = Category("Mathematics")
strategy = Category("Strategy")

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

#adding all to the db
session.add_all([
    allen_b, sun, luiz,
    pense, metodos, arte, stats, java,
    prog, math, strategy
])

#commiting
session.commit()

session.close()