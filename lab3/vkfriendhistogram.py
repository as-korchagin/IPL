import get_followers
import get_friends


def start_followers(username):
    get_followers.GetFollowers(username).execute()
    print(username, 'OK')


def start_friends(username):
    get_friends.GetFriends(username).execute()
    print(username, 'OK')


# start_followers("yurydud")
start_friends('dmitrykhitrin')
