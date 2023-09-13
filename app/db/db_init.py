import sys
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

engine = create_engine(f'postgresql://{config["database"]["user"]}:{config["database"]["password"]}@{config["database"]["ip"]}:{config["database"]["port"]}/{config["database"]["db"]}', echo=False) # Соединение с бд
metadata = MetaData()
Base = declarative_base(metadata=metadata)


def make_session(): # Функция для открытия сесссии бд
    try:
        _engine = engine
        _Session = sessionmaker(bind=_engine)
        session = _Session()
        return session
    except:
        print(f"Couldn't create transaction!"
              f"Check log's: {sys.exc_info()}")
        raise sys.exc_info()


class User(Base): # Модель User
    __tablename__ = "users" # Название таблицы в базе данных

    # Поля модели User
    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    last_request = Column(DateTime)


class CollectData(Base): # Мщдель CollectData
    __tablename__ = "collected_data" # Название таблицы в базе данных

    # Поля модели CollectData
    id = Column(Integer, primary_key=True)
    type = Column(String)
    mutability = Column(String)
    description = Column(String)
    syntax_examples = Column(String)


metadata.create_all(engine) # Создание таблиц в базе данных при запуске
