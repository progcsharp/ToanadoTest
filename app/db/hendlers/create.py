from app.db.db_init import make_session, User, CollectData
from app.lib.security import hash_password


def create_user(login: str, password: str) -> bool: # Функция для создание нвого юзера
    session = make_session() # Открытие сессии
    password = hash_password(password) # Хеширование пароля
    user = User(login=login, password=password) # Создание нового юзера
    session.add(user) # Добавление экземпляра класса User в коммит
    session.commit() # Коммит в бд
    session.close() # Закрытие сессии
    return True


def create_collect_data(collect_data: list) -> bool: # Функция для записи информации в таблицу collect_data
    session = make_session() # Открытие сессии
    collect_data = CollectData(type=collect_data[0], mutability=collect_data[1],
                               description=collect_data[2], syntax_examples=collect_data[3]) # Создание новой строки в таблице collect_data
    session.add(collect_data) # Добавление экземпляра класса CollectData в коммит
    session.commit() # Коммит в бд
    session.close() # Закрытие сессии
    return True

