from datetime import date

from game import Game
from detail import Detail
from base import Base, Session, engine

# creating all the tables 
Base.metadata.create_all(engine)

# creating a session
session = Session()

ds = Game("Dark Souls: Remastered", "RPG", True)
mc = Game("Minecraft: Java", "Sandbox", True)
f3 = Game("Fallout 3", "FPS", False)

ds_details = Detail(129.90, date(2018, 5, 23), ds)
mc_details = Detail(120, date(2011, 11, 18), mc)
f3_details = Detail(39.99, date(2009, 10, 13), f3)

session.add_all([
    ds, mc, f3, ds_details, mc_details, f3_details
])

session.commit()
session.close()