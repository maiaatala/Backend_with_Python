from app import db


def drop_db():
    db.Base.metadata.drop_all(bind=db.engine)
