from db_utils import DBSearch


def add_friend(username):
    friend_username = input("What is the username of the friend you would like to add?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    user_id = DBSearch.get_user_id(username)
    DBSearch.add_to_friend_list(user_id, friend_id)
    print("{} has been added to your friend list.".format(friend_username))


def delete_friend():
    friend_username = input("What is the username of the friend you would like to delete?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    DBSearch.delete_from_friend_list(friend_id)
    print("{} has been deleted from your friend list.".format(friend_username))