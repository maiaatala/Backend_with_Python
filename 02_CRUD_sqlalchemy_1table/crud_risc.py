from modular_crud import *
import os

# linka a engine
engine = sqlalchemy.create_engine("sqlite:///enterprise.db", echo = False)  # echo to see the sql comands
path = "enterprise.db" # the db file


Game = init_db(engine)


''' criar uma sessão '''

Session = sessionmaker(bind=engine)
session = Session()

menuing = {
    'c': create,
    'r': read,
    'u': update,
    'd': delete
}

menu()

while (escolha := input(">>>crud option: ").lower()) in menuing:
    menuing.get(escolha)(session, Game)
else:
    print("     - bye")