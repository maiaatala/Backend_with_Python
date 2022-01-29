from datetime import date
from game import Game
from detail import Detail
from base import Session

from sqlalchemy import desc

def menu():
    print(
        "\n\t+-------+------------+\n"\
        "\t| opcao |    menu    |\n"\
        "\t+-------+------------+\n"\
        "\t| c     | create     |\n"\
        "\t| r     | read       |\n"\
        "\t| u     | update     |\n"\
        "\t| d     | delete     |\n"\
        "\t+-------+------------+\n"\
    )

def read(e = None):
    session = Session()
    while e not in ['name', 'genre','date','price']:
        e = input(("\t Order list by name, genre, date or price?\n> ")).lower()
    if e == 'name':
        games = session.query(Detail)\
            .join(Game)\
            .order_by(Game.name).all()
        print("")
        for game in games:
            print(f"| {game.game.name:>25} | {game.game.genre:^12} | {game.price:^6} | {game.released} |")
        print("")
        session.close()
    if e == 'genre':
        games = session.query(Detail)\
            .join(Game)\
            .order_by(Game.genre).all()
        print("")
        for game in games:
            print(f"| {game.game.name:>25} | {game.game.genre:^12} | {game.price:^6} | {game.released} |")
        print("")
    if e == 'date':
        games = session.query(Detail)\
            .order_by(Detail.released).all()
        print("")
        for game in games:
            print(f"| {game.game.name:>25} | {game.game.genre:^12} | {game.price:^6} | {game.released} |")
        print("")
    if e == 'price':
        games = session.query(Detail)\
            .order_by(Detail.price).all()
        print("")
        for game in games:
            print(f"| {game.game.name:>25} | {game.game.genre:^12} | {game.price:^6} | {game.released} |")
        print("")

def create():
    session = Session()
    g_name = input("\tEnter the name of the game\n> ")
    if (session.query(Game).filter(Game.name.ilike('%'+g_name+'%')).first() is not None):
        print("\t--Game already on database, try updating it--")
    else:
        g_genre = input("\tGenre of the game\n> ")
        if (g_online := ("\tCan the game be played online? (yes/no)\n> ")) == 'yes':
            g_online = True
        else:
            g_online = False
        g_released = date(int(input("\tInt of the year\n> ")), int(input("\tInt of the month\n> ")), int(input("\tInt of the day\n> ")))
        g_price = float(input("\tPrice of the game\n> "))
        game = Game(g_name, g_genre, g_online)
        gamed = Detail(g_price, g_released, game)
        session.add(game, gamed)
        session.commit()
        session.close()
        print("\t--Game Created--")

def update():
    session = Session()
    read('name')
    inp = input("\tName of the game you wish to update\n> ")
    game = session.query(Game)\
        .filter(Game.name.ilike('%'+inp+'%'))\
        .first()
    if game is None:
        print("\t--Game not on database, try creating it--")
    else:
        game_d = session.query(Detail)\
            .filter(Detail.game == game)\
            .first()
        print("\tEnter to skip the data")
        print(f"\tCurrent Name: {game.name}")
        if (inp:=input(("> New: "))):
            game.name = inp
        print(f"\tCurrent Genre: {game.genre}")
        if (inp:=input(("> New: "))):
            game.genre = inp
        print(f"\tCurrent Online Status: {game.online}")
        if (inp:=input(("> New: ").lower()) == "true"):
            game.online = True
        elif inp == "false":
            game.online = False
        
        print(f"\tCurrent Date: {game_d.released}")
        if (inp:=input(("> year: "))):
            year = int(inp)
            month = int(input("> month: "))
            day = int(input("> day: "))
            game_d.date = date(year, month, day)
        
        print(f"\tCurrent Price: {game_d.price}")
        if (inp:=input(("> New: "))):
            game_d.price = float(inp)
        session.commit()
        session.close()
        print("\t--Game Updated--")

def delete():
    session = Session()
    read('name')
    inp = input("\tName of the game you wish to DELETE\n> ")
    game = session.query(Game)\
        .filter(Game.name.ilike('%'+inp+'%'))\
        .first()
    if game is None:
        print("\t--Lucked out, game not on db--")
    else:
        session.delete(game)
        session.commit()
        session.close()
        print("\t--Game Deleted--")

menuing = {
    'c': create,
    'r': read,
    'u': update,
    'd': delete
}

menu()

while(escolha := input("> crud option:   ")) in menuing:
    menuing.get(escolha)()
else:
    print("- byeee.")