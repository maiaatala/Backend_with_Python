from datetime import date
from game import Game
from detail import Detail
from base import Session

from sqlalchemy import desc

session = Session()

games = session.query(Game).all()
print("### All Games:")
for game in games:
    print(f"{game.name:>25} has the genre of {game.genre} ")
print('')

print("### Games with online mode")
games = session.query(Game)\
    .filter(Game.online)\
    .all()
print("### All Games:")
for game in games:
    print(f"{game.name:>25} can be played online")
print('')

print("### Games releaser after 2018:")
new = session.query(Detail)\
    .filter(Detail.released > date(2018, 1, 1))\
    .all()
for games in new:
    print(F"{games.game.name:>25} was released on {games.released}" )
print('')

print("### Games by price")
games = session.query(Detail)\
    .order_by(Detail.price)\
    .all()
for game in games:
    print(F"{game.game.name:>25} is a {game.game.genre} with the price of {game.price}")
print("")

print("### all the details")
details = session.query(Detail).all()
for d in details:
    print(F"{d.game.name:>25}: {d.released} | {d.price}")
print("")

# update details !!! WORKS
ms = session.query(Detail)\
    .join(Game)\
    .filter(Game.name.ilike('%minecraft%'))\
    .first()

ms.released = date(2020, 1, 1)
session.commit()

print("### all the details")
details = session.query(Detail).all()
for d in details:
    print(F"{d.game.name:>25}: {d.released} | {d.price}")
print("")

## delete parent !! WORKS

ms = session.query(Game)\
    .filter(Game.name.ilike('%minecraft%'))\
    .first()

session.delete(ms)
session.commit()

print("### all the details")
details = session.query(Detail).all()
for d in details:
    print(F"{d.game.name:>25}: {d.released} | {d.price}")
print("")

games = session.query(Game).all()
print("### All Games:")
for game in games:
    print(f"{game.name:>25} has the genre of {game.genre} ")
print('')

# UPDATE PARENT NAME, WORKS

ds = session.query(Game)\
    .filter(Game.name.ilike('%dark%'))\
    .first()
ds.name = "Dark souls: Prepare to die"
session.commit()

print("### all the details")
details = session.query(Detail).all()
for d in details:
    print(F"{d.game.name:>25}: {d.released} | {d.price}")
print("")

session.close()