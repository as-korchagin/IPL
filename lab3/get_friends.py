import json

import requests

from lab3 import base_client


class GetFriends(base_client.BaseClient):
    method = "friends.get?"

    http_method = "GET"

    user_id = None

    def __init__(self, user_id):
        self.user_id = user_id

    def _get_data(self, method, http_method):
        response = requests.get(super().generate_url(self.method), self.get_params())
        return self.response_handler(response)

    def get_headers(self):
        return super().get_headers()

    def get_json(self):
        super().get_json()

    def response_handler(self, response):
        return (json.loads(response.text)).get('response')

    def get_params(self):
        return {"user_id": str(self.user_id),
                "order": "name",
                "fields": "bdate"}
