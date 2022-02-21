from enum import unique
from app import db


class Costumer(db.Base):
    is_active = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(255), unique=True)
    # mobile_phone = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255), nullable=False)
    # cpf = db.Column(db.String(11))
