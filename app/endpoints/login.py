import tornado

from app.config import config
from app.db.hendlers.get import get_user
from app.lib.security import hash_password


class LoginHandler(tornado.web.RequestHandler): # Класс для utl /login
    def post(self): # Функция для post запроса
        if not self.get_cookie("mycookie") == config["auth"]["secret"]:
            login = tornado.escape.json_decode(self.request.body)["login"] # Получение login пользователя из данных запроса
            user = get_user(login) # вызов функции для проверки существования пользователя в бд
            password = tornado.escape.json_decode(self.request.body)["password"] # Получение password пользователя из данных запроса
            password = hash_password(password) # вызов функции для хеширования пароля
            try:
                if user.password == password: # Проверки правильности пароля
                    self.set_cookie(config["auth"]["name"], config["auth"]["secret"], expires_days=1) # создание куки
                    self.write({"authorized": True}) # Ответ пользователю о успешной авторизации
                else:
                    self.write({"authorized": "wrong password"}) # Ответ пользователю о неверном пароле
            except AttributeError:
                self.write({"error":"User not found"}) # Ответ пользователю о неверном логине
        else:
            self.write({"authorized": True}) # Ответ пользователю о успешной авторизации

