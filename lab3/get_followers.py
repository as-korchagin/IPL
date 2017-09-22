import datetime
import json

import requests

from lab3 import get_friends


class GetFollowers(get_friends.GetFriends):
    method = "users.getFollowers?"

    offset = 0

    user_id = None

    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(user_id)

    def response_handler(self, response):
        return super().response_handler(response)

    def get_params(self):
        return {"user_id": str(self.user_id),
                "order": "name",
                "count": 1000,
                "offset": self.offset,
                "fields": "bdate, sex"}

    def _get_data(self, method, http_method):
        followers = list()
        response = requests.get(super().generate_url(self.method), self.get_params())
        followers += json.loads(response.text).get("response").get("items")
        followers_count = json.loads(response.text).get("response").get("count")
        print("Almost:", followers_count)
        while len(followers) < followers_count:
            print("Downloaded:", round(len(followers) / followers_count * 100, 2), "%", "Followers: ", followers_count)
            self.offset += 1000
            response = requests.get(super().generate_url(self.method), self.get_params())
            try:
                followers += json.loads(response.text).get("response").get("items")
                if json.loads(response.text).get("response").get("count") - followers_count < 100:
                    followers_count = json.loads(response.text).get("response").get("count")
            except AttributeError as e:
                open("./Error", "a").write(str(datetime.datetime.now()) + str(e) + "\n")
        return followers
