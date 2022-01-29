# package dependencies
from sqlalchemy_utils import database_exists, create_database

# my_package requirementes
from config import path, Session, engine, Base


def init_db():
    if not database_exists(path):
        create_database(path)
        session = Session()
        with session as s:
            Base.metadata.create_all(engine)
            session.commit()
