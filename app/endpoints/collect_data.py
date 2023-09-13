import tornado

from app.config import config
from app.db.hendlers.get import get_all_collect_data


class CollectDataHandler(tornado.web.RequestHandler): # Класс для utl /collect_data
    def get(self): # Функция для get запроса
        if self.get_cookie("mycookie") == config["auth"]["secret"]: # Проврка на наличие куки у пользователя
            response = {"data": [], "count": 0} # Шаблон ответа пользователю
            collect_data = get_all_collect_data() # Вызов функции для получения информации с бд
            for data in collect_data: # Цикл по плученной информации с бд
                data = data.__dict__ # Преобразовния данных в словарь
                data.pop("_sa_instance_state") # Удаление не нужной информации
                response["data"].append(data) # Добавление информации в массив ответа

            response["count"] = len(collect_data) # Получение количество записей
            self.write(response) # Ответ пользователю
        else:
            self.write({"error": "invalid credentials"}) # Информация об ошибке неавторизированного пользователя