from app import db


class User(db.Base):

    # full_name = db.Column(db.String(128), nullable=False)
    username = db.Column(
        db.String(255), unique=True, index=True, nullable=False
    )  # change to username
    password = db.Column(db.String(255), nullable=False)
    # is_active = db.Column(db.Boolean, default=True)
