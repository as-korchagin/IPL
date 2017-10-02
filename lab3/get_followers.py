import datetime
import json
import time

import requests

import base_client
from assist_functions import check_date, create_bar_histogram, create_pie_histogram
from get_userid import GetUserId


class GetFollowers(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"

    method = "users.getFollowers?"

    http_method = "GET"

    offset = 0

    user_id = None

    username = None

    def __init__(self, username):
        self.username = username
        self.user_id = str(GetUserId(username).execute())

    def response_handler(self, response):
        sex_age = {
            "1": dict(),
            "2": dict()
        }
        for j in response:
            try:
                if (j.get("bdate") is not None) and (1 <= j.get("sex") <= 2):
                    years = check_date(j)
                    if years:
                        if (sex_age[str(j.get("sex"))]).get(str(years)) is None:
                            (sex_age[str(j.get("sex"))])[str(years)] = 1
                        else:
                            (sex_age[str(j.get("sex"))])[str(years)] += 1
            except KeyError as e:
                print(e)
        create_bar_histogram(sex_age.get("1"), self.username, "Woman-age statistics")
        create_bar_histogram(sex_age.get("2"), self.username, "Man-age statistics")
        create_pie_histogram({
            "Man": list(0 + int(n) for n in sex_age.get("2").keys()),
            "Woman": list(0 + int(n) for n in sex_age.get("1").keys())
        }, self.username, "Man-Woman statistics")
        return True

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
            print("Downloaded: ",
                  round(len(followers) / followers_count * 100, 3),
                  "% ",
                  "Followers: ",
                  followers_count,
                  sep='')
            self.offset += 1000
            response = requests.get(super().generate_url(self.method), self.get_params())
            try:
                followers += json.loads(response.text).get("response").get("items")
                if json.loads(response.text).get("response").get("count") - followers_count < 100:
                    followers_count = json.loads(response.text).get("response").get("count")
            except AttributeError as e:
                open("./Error", "a").write(str(datetime.datetime.now()) + str(e) + "\n")
                open("./Error_data", "a").write(str(datetime.datetime.now()) + "\n" + response.text + "\n\n\n")
                time.sleep(1)
        return self.response_handler(followers)
