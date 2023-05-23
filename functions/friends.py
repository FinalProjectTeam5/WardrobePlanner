from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.dashboard_function import dashboard

def add_friend(user):
    friend_username = input("What is the username of the friend you would like to add?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    if friend_id == "NULL":
        print("Sorry, that user doesn't exist")
    else:
        DBSearch.add_to_friend_list(user.user_id, friend_id)
        print("{} has been added to your friend list.".format(friend_username))
    return dashboard(user)


def show_friends_list(user):
    friends_list = DBSearch.get_friends_list(user.user_id)
    print("Here is a list of your friends to share with: {}".format(friends_list))
    return dashboard(user)


def delete_friend(user):
    print(show_friends_list(user))
    friend_username = input("What is the username of the friend you would like to delete?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    DBSearch.delete_from_friend_list(friend_id, user.user_id)
    print("{} has been deleted from your friend list.".format(friend_username))
    return dashboard(user)



