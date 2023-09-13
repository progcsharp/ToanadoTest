from app.db.db_init import make_session, CollectData


def delete_collect_data(): # Функция для удаления всех данных из таблицы collect_data
    session = make_session() # Открытие сессии
    session.query(CollectData).delete() #Удаление всех существующих данных в таблице
    session.commit() # Коммит в бд
    session.close() # Закрытие сессии
