import datetime
import json
import os

import matplotlib.pyplot as plt

from lab3 import get_friends, get_userid, get_followers


def get_id(username):
    user = get_userid.GetUserId(username).execute()
    if user.get("error_code") == 0:
        return user.get("data")
    terminate({"error_code": 0,
               "data": get_friends.GetFriends(user.get("data")).execute()})


def check_date(user):
    datelist = user.get("bdate").split('.')
    if len(datelist) == 3:
        try:
            years = (int(((datetime.datetime.now().date() -
                           datetime.date(int(datelist[2]),
                                         int(datelist[1]),
                                         int(datelist[0])))
                          .days) / 365.25))
        except ValueError as e:
            open("Error", "a").write(str(e))
            return False
        if years > 70:
            return False
        return years


def get_ages(username):
    user_id = get_id(username)
    age = dict()
    friends = get_friends.GetFriends(str(user_id)).execute()
    for k in json.loads(friends).get('response'):
        if k.get("bdate") is not None:
            years = check_date(k)
            if years:
                if age.get(str(years)) is None:
                    age[str(years)] = 1
                else:
                    age[str(years)] += 1
    return age


def get_followers_func(username):
    sex_age = {
        "1": dict(),
        "2": dict()
    }
    user = get_id(username)
    followers = get_followers.GetFollowers(user).execute()
    for j in followers:
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
    return sex_age


def create_bar_histogram(stat_data, username=None, title="Age statistics"):
    plt.bar(list(int(m) for m in stat_data.keys()),
            list(int(m) for m in stat_data.values()))
    plt.title(title)
    plt.grid(True)
    save_hist(username, "png", title)


def create_pie_histogram(stat_data, username=None, title="Age statistics"):
    plt.pie(list(int(l[0]) for l in stat_data.values()),
            labels=stat_data.keys())
    plt.title(title)
    save_hist(username, "png", title)


def save_hist(name='', fmt='png', postfix=""):
    pwd = os.getcwd()
    if not os.path.exists("./VK_Statics/{}".format(name)):
        os.makedirs("./VK_Statics/{}".format(name))
    path = './VK_Statics/{}/'.format(name)
    os.chdir(path)
    plt.savefig('{}.{}'.format(postfix, fmt), fmt='png')
    os.chdir(pwd)


def terminate(error):
    print(error)
    exit()


def start_friends(username):
    age = get_ages(username)
    create_bar_histogram(age, username)
    print(username, "OK")


def start_followers(username):
    foll_data = get_followers_func(username)
    create_bar_histogram(foll_data.get("1"), username, "Woman-age statistics")
    create_bar_histogram(foll_data.get("2"), username, "Man-age statistics")
    create_pie_histogram({
        "Man": list(0 + int(n) for n in foll_data.get("2").keys()),
        "Woman": list(0 + int(n) for n in foll_data.get("1").keys())
    }, username, "Man-Woman statistics")


start_followers("username")
