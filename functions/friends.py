from db_utils import DBSearch


def add_friend(username):
    friend_username = input("What is the username of the friend you would like to add?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    user_id = DBSearch.get_user_id(username)
    DBSearch.add_to_friend_list(user_id, friend_id)
    return "{} has been added to your friend list.".format(friend_username)


def delete_friend(username):
    friend_username = input("What is the username of the friend you would like to delete?")
    user_id = DBSearch.get_user_id(username)
    friend_id = DBSearch.get_friend_user_id(friend_username)
    DBSearch.delete_from_friend_list(friend_id, user_id)
    return "{} has been deleted from your friend list.".format(friend_username)


def show_friends_list(user_id):
    friends_list = DBSearch.get_friends_list(user_id)
    return "Here is a list of your friends to share with: {}".format(friends_list)
