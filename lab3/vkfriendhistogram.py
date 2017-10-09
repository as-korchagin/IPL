import assist_functions

from lab3 import get_friends, get_userid, get_followers


def get_ages(username):
    user_id = get_userid.GetUserId(username).execute()
    age = dict()
    friends = get_friends.GetFriends(str(user_id)).execute()
    for k in friends:
        if k.get("bdate") is not None:
            years = assist_functions.check_date(k)
            if years:
                if age.get(str(years)) is None:
                    age[str(years)] = 1
                else:
                    age[str(years)] += 1
    return age


def start_friends(username):
    age = get_ages(username)
    assist_functions.create_bar_histogram(age, username)
    print(username, "OK")


def start_followers(username):
    get_followers.GetFollowers(username).execute()
    print(username, 'OK')


start_friends('dmitrykhitrin')
