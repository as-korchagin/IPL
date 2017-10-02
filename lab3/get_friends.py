import json

import requests

import base_client
from assist_functions import check_date, create_bar_histogram
from get_userid import GetUserId


class GetFriends(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"

    method = "friends.get?"

    http_method = "GET"

    user_id = None

    username = None

    def __init__(self, username):
        self.username = username
        self.user_id = str(GetUserId(username).execute())

    def _get_data(self, method, http_method):
        response = requests.get(super().generate_url(self.method), self.get_params())
        return self.response_handler(response)

    def get_headers(self):
        return super().get_headers()

    def get_json(self):
        super().get_json()

    def response_handler(self, response):
        age = dict()
        for k in json.loads(response.text).get('response'):
            if k.get("bdate") is not None:
                years = check_date(k)
                if years:
                    if age.get(str(years)) is None:
                        age[str(years)] = 1
                    else:
                        age[str(years)] += 1
        create_bar_histogram(age, self.username)
        return True

    def get_params(self):
        return {"user_id": str(self.user_id),
                "order": "name",
                "fields": "bdate"}
