import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float # coluna e os tipos de dado da coluna


def menu():
    print("""+-------+------------+
| opcao |    menu    |
+-------+------------+
| c     | create     |
| r     | read       |
| u     | update     |
| d     | delete     |
+-------+------------+""")

def init_db(engine):

    Base = declarative_base()

    class Game(Base):
        __tablename__ = 'users' # obrigatorios, nome da tabela

        id = Column(Integer, primary_key=True)  # nome da coluna =  tipo e se é primary_key ou não
        name = Column(String(50), nullable=False)
        category = Column(String(50))
        rank = Column(Float)
        price = Column(Float)

        def __repr__(self):
            return (f"<User(name={self.name}, category={self.category}, Rank={self.rank}, preço={self.price})")

    ''' criar a tabela no banco de dados '''
    # precisa ser apos a declaração das tabelas.
    Base.metadata.create_all(engine) # comunica com a engine (que ta ligada ao banco de dado) para criar as tabelas

    return Game

def create(session, Game):
    # input of the entry
    game_query = Game()
    urs_input = input("Enter the name of the game: ").title()
    if urs_input:
        # precisa do first()
        if (session.query(Game).filter_by(name = urs_input).first() is not None):
            print('--Game already on the database, try updating it.--')
        else:
            game_query.name = urs_input
            game_query.category = input("Enter the category of the game: ")
            game_query.rank = float(input("Enter the rank of the game: "))
            game_query.price = float(input("Enter the price of the game: "))
            # print(game_query)
            # commiting the entry
            session.add(game_query)
            session.commit()
            print("--Game Created in database!--")
    else:
        print("--Deve inserir um nome!--")

def read(session, Game):
    # viewing the table
    order = 'rank'
    print("\t\t------ CURRENT TABLE ------")
    # to do, the dec() doesn't make sense when it comes to price
    # ask how the user wants the table to be ordered.
    for instance in session.query(Game).order_by(getattr(Game, order).desc()).order_by(Game.name):
        print(("{:<2} | {:^20} | {:^15} | {:^8.2f} | {:<4.1f}").format(instance.id, instance.name, instance.category, instance.price, instance.rank))

def update(session, Game):
    urs_input = input("Name of game to update: ").title()
    query_game = session.query(Game).filter_by(name = urs_input).first()
    if (query_game):
        print(f"current name: {query_game.name}")
        urs_input = input("\tNew name: ")
        if urs_input:
            query_game.name = urs_input.title()
        
        print(f"current category: {query_game.category}")
        urs_input = input("\tNew category: ")
        if urs_input:
            query_game.category = urs_input
        
        print(f"current rank: {query_game.rank}")
        urs_input = input("\tNew rank: ")
        if urs_input:
            query_game.rank = float(urs_input)
        
        print(f"current price: {query_game.price}")
        urs_input = input("\tNew price: ")
        if urs_input:
            query_game.price = float(urs_input)
        
        session.commit()
        print("--game updated in database!--")
    else:
        print("--Game not in database, try creating it.--")

def delete(session, Game):
    urs_input = input("Name of game to delete: ").title()
    query_game = session.query(Game).filter_by(name = urs_input).first()
    if (query_game):
        session.delete(query_game) # delete
        session.commit()
        print("--Game deleted from database!--")
    else:
        print("--Lucky you, game was never here--")
