import tornado

from app.db.hendlers.get import get_all_collect_data


class CollectDataHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("mycookie"):
            response = {"data": [], "count": 0}
            collect_data = get_all_collect_data()
            for data in collect_data:
                data = data.__dict__
                data.pop("_sa_instance_state")
                response["data"].append(data)

            response["count"] = len(collect_data)
            self.write(response)
        else:
            self.write({"error": "invalid credentials"})