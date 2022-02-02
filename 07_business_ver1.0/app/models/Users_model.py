from app import db


class User(db.Base):

    full_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String, unique=True, index=True, nullable=False)
    password = db.Column(db.String, nullable=False)
