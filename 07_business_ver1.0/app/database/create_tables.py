from app import db, models, core


def init_db():
    session = db.Session()
    db.Base.metadata.create_all(db.engine)
    session.commit()
    session.close()
