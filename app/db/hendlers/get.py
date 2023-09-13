from typing import Tuple

from app.db.db_init import User, make_session, CollectData


def get_user(login: str) -> dict: # Функция для поиска пользователя в бд
    session = make_session() # Открытие сессии
    user = session.query(User).filter(User.login == login).first() # Поиск пользователя в бд
    session.close() # Закрытие сессии
    return user # Возвращение пользователя


def get_all_collect_data() -> list: # Функция для сбора всех данных таблицы collect_data
    session = make_session() # Открытие сессии
    collect_data = session.query(CollectData).all() # Сбор всех данных таблицы colltct_data
    session.close() # Закрытие сессии
    return collect_data # Возвращение всех данных
