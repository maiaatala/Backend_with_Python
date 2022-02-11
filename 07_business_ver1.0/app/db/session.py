from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import core

engine = create_engine(core.settings.SQLALCHEMY_DATABASE_URI_TEST)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def get_db() -> Generator:
    try:
        db = Session()
        yield db
    finally:
        db.close()


# am i really using the generator if i keep just importing _db =db.Session!?!?
