from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

path = "sqlite:///db/library.db"
engine = create_engine(path, echo=False)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
