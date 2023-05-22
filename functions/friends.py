from WardrobePlanner.classes.db_utils import DBSearch


def add_friend(user):
    friend_username = input("What is the username of the friend you would like to add?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    DBSearch.add_to_friend_list(user.user_id, friend_id)
    return "{} has been added to your friend list.".format(friend_username)


def show_friends_list(user):
    friends_list = DBSearch.get_friends_list(user.user_id)
    return "Here is a list of your friends to share with: {}".format(friends_list)


def delete_friend(user):
    print(show_friends_list(user))
    friend_username = input("What is the username of the friend you would like to delete?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    DBSearch.delete_from_friend_list(friend_id, user.user_id)
    return "{} has been deleted from your friend list.".format(friend_username)



