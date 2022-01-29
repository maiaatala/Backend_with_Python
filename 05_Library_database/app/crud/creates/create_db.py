from app import tables as t


def init_db():
    t.Base.metadata.create_all(t.engine)
    session = t.Session()
    session.commit()
    session.close()
