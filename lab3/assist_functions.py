import datetime
import os

import matplotlib.pyplot as plt


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


def create_bar_histogram(stat_data, username=None, title="Age statistics"):
    plt.figure()
    plt.bar(list(int(m) for m in stat_data.keys()),
            list(int(m) for m in stat_data.values()))
    plt.title(title)
    plt.grid(True)
    save_hist(username, "png", title)


def create_pie_histogram(stat_data, username=None, title="Age statistics"):
    plt.figure()
    plt.pie(list(stat_data.values()),
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
