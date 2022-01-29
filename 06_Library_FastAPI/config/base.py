from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.exc import SADeprecationWarning, SQLAlchemyError
from .db import Session

from icecream import ic


@as_declarative()
class Base:
    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.utcnow)

    def add_and_save(self):
        try:
            session = Session()
            data = self
            session.add(data)
            session.commit()
            session.refresh(data)
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        else:
            return data
        finally:
            session.close()

    @classmethod
    def get_all(self):
        try:
            session = Session()
            data = session.query(self).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        else:
            return data
        finally:
            session.close()

    @classmethod
    def generic_get(self, kwargs):
        try:
            session = Session()
            data = session.query(self)
            for k, v in kwargs.items():
                if v is not None:
                    ic(k, v)
                    data = data.filter(getattr(self, k) == v)
            data = data.all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        else:
            return data
        finally:
            session.close()

    @classmethod
    def generic_get_list(self, kwargs):
        try:
            kwargs = list(kwargs.items())
            session = Session()
            data = session.query(self).filter(
                getattr((self), kwargs[0][0]) == kwargs[0][1]
            )
            for li in kwargs[1:]:
                data = data.filter(getattr((self), li[0]) == li[1])
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        else:
            return data.all()
        finally:
            session.close()

    @classmethod
    def get(self, id):
        try:
            session = Session()
            data = session.query(self).filter_by(id=id).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        else:
            return data
        finally:
            session.close()

    @classmethod
    def update(self, id, **kwargs):
        try:
            data = self.get(id)
            for k, v in kwargs.items():
                if v and hasattr(data, k):
                    setattr(data, k, v)
            data.add_and_save()
        except Exception as e:
            raise e

    @classmethod
    def delete(self, id):
        try:
            data = self.get(id)
            session = Session()
            session.delete(data)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            session.close()
