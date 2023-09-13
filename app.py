import asyncio
import tornado

from app.config import config
from app.endpoints.collect_data import CollectDataHandler
from app.endpoints.login import LoginHandler


def make_app():
    return tornado.web.Application([
        (r"/login", LoginHandler), # Добавление url для авторизации
        (r"/collect_data", CollectDataHandler) # Добавление url для получения данных
    ])


async def main():
    app = make_app() # Вызов функции для инициализации веб приложения
    app.listen(config["server"]["port"]) # Определние слушающего порта

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main()) # Запуск приложения
