from WardrobePlanner.classes.db_utils import DBSearch


def add_friend(user_id):
    friend_username = input("What is the username of the friend you would like to add? \n")
    friend_id = DBSearch.get_friend_user_id(friend_username)[0][0]
    friends_list = DBSearch.get_friends_list(user_id)
    for i in range(len(friends_list)):
        if friend_id in friends_list[i]:
            return "You are already friends with {}.".format(friend_username)
    if friend_id == "NULL":
        return "Sorry, that user doesn't exist"
    else:
        DBSearch.add_to_friend_list(user_id, friend_id)
        return "{} has been added to your friend list.".format(friend_username)


def show_friends_list(user_id):
    friends_list = DBSearch.get_friends_list(user_id)
    return "Here is a list of your friends: {}".format(friends_list)


def delete_friend(user_id):
    print(show_friends_list(user_id))
    friend_username = input("What is the username of the friend you would like to delete? \n")
    friend_id = DBSearch.get_friend_user_id(friend_username)[0][0]
    DBSearch.delete_from_friend_list(friend_id, user_id)
    return "{} has been deleted from your friend list.".format(friend_username)

