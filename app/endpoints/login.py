import tornado

from app.config import config
from app.db.hendlers.get import get_user
from app.lib.security import hash_password


class LoginHandler(tornado.web.RequestHandler):
    def post(self):
        if not self.get_cookie("mycookie"):
            login = tornado.escape.json_decode(self.request.body)["login"]
            user = get_user(login)
            password = tornado.escape.json_decode(self.request.body)["password"]
            password = hash_password(password)
            try:
                if user.password == password:
                    self.set_cookie(config["auth"]["name"], config["auth"]["secret"], expires_days=1)
                    self.write({"authorized": True})
                else:
                    self.write({"authorized": False})
            except AttributeError:
                self.write({"error":"User not found"})
        else:
            self.write({"authorized": True})

