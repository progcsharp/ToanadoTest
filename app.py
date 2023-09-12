import asyncio
import tornado

from app.config import config
from app.endpoints.collect_data import CollectDataHandler
from app.endpoints.login import LoginHandler


def make_app():
    return tornado.web.Application([
        (r"/login", LoginHandler),
        (r"/collect_data", CollectDataHandler)
    ])


async def main():
    app = make_app()
    app.listen(config["server"]["port"])

    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
