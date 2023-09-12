import sys
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

engine = create_engine(f'postgresql://{config["database"]["user"]}:{config["database"]["password"]}@{config["database"]["ip"]}:{config["database"]["port"]}/{config["database"]["db"]}', echo=True)
metadata = MetaData()
Base = declarative_base(metadata=metadata)


def make_session():
    try:
        print("Create transaction...")
        _engine = engine
        _Session = sessionmaker(bind=_engine)
        session = _Session()
        print("Transaction created!")
        return session
    except:
        print(f"Couldn't create transaction!"
              f"Check log's: {sys.exc_info()}")
        raise sys.exc_info()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_request = Column(DateTime)


class CollectData(Base):
    __tablename__ = "collected_data"

    id = Column(Integer, primary_key=True)
    type = Column(String)
    mutability = Column(String)
    description = Column(String)
    syntax_examples = Column(String)


metadata.create_all(engine)
