import json

import requests

import base_client
from assist_functions import terminate


class GetUserId(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"

    method = "users.get?"

    http_method = "GET"

    username = None

    def __init__(self, username):
        self.username = str(username)

    def get_params(self):
        return {
            "user_ids": self.username
        }

    def get_json(self):
        super().get_json()

    def get_headers(self):
        super().get_headers()

    def response_handler(self, response):
        try:
            user_id = json.loads(response.text).get("response")[0].get("uid")
            return user_id
        except TypeError:
            terminate({
                "error_code": int(json.loads(response.text).get("error").get("error_code")),
                "data": json.loads(response.text).get("error").get("error_msg")
            })

    def _get_data(self, method, http_method):
        response = requests.get(super().generate_url(self.method), self.get_params())
        return self.response_handler(response)
