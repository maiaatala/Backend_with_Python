from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# / / / nome das pastas / nome do arquivo
engine = create_engine("sqlite:///one to one/jogo.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()