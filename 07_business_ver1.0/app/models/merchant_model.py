from sqlalchemy import null
from app import db


class Merchant(db.Base):
    is_active = db.Column(db.Boolean, default=True)
    corporate_name = db.Column(db.String(255), nullable=False)
    # fancy_name = db.Column(db.String(255), nullable=False)
    # document = db.Column(db.String(14), nullable=False)
    # contact_name = db.Column(db.String(255), nullable=False)
    # contact_mobile = db.Column(db.String(11), nullable=False)
    # merchant_category_code = db.Column(db.String(4), nullable=False)
    email = db.Column(db.String(255))
