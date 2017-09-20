import datetime
import json

from lab3 import get_friends, get_userid


def get_ages(username):
    user = get_userid.GetUserId(username).execute()
    if user.get("error_code") != 0:
        return user
    friends = get_friends.GetFriends(user.get("data")).execute()
    age = dict()
    for i in json.loads(friends).get('response'):
        if i.get("bdate") is not None:
            datelist = i.get("bdate").split('.')
            if len(datelist) == 3:
                years = (int(((datetime.datetime.now().date() -
                               datetime.date(int(datelist[2]),
                                             int(datelist[1]),
                                             int(datelist[0])))
                              .days) / 365.25))
                if years > 70:
                    continue
                if age.get(str(years)) is None:
                    age[str(years)] = 1
                else:
                    age[str(years)] += 1
    return age


age = get_ages(input())
for i in sorted(age.keys()):
    print(i, '#' * age.get(i))
