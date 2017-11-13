import json

import base_client
from assist_functions import terminate


class GetUserId(base_client.BaseClient):
    method = "users.get?"

    http_method = "GET"

    username = None

    def __init__(self, username):
        self.username = str(username)

    def get_params(self):
        return {
            "user_ids": self.username
        }

    def response_handler(self, response):
        try:
            user_id = json.loads(response.text).get("response")[0].get("uid")
            return user_id
        except TypeError:
            terminate({
                "error_code": int(json.loads(response.text).get("error").get("error_code")),
                "data": json.loads(response.text).get("error").get("error_msg")
            })
