from WardrobePlanner.classes.db_utils import DBSearch


def add_friend(user_id):
    try:
        friend_username = input("What is the username of the friend you would like to add? \n")
        friend_id = DBSearch.get_friend_user_id(friend_username)[0][0]
        friends_list = DBSearch.get_friends_list(user_id)
        for i in range(len(friends_list)):
            if friend_id in friends_list[i]:
                return "You are already friends with {}.".format(friend_username)
        else:
            DBSearch.add_to_friend_list(user_id, friend_id)
            return "{} has been added to your friend list.".format(friend_username)
    except IndexError:
        return "Sorry, that isn't a valid user. Please try again."


def show_friends_list(user_id):
    friends = []
    friends_list = DBSearch.get_friends_list(user_id)
    for friend in friends_list:
        friends.append(friend[1])
    return "Here is a list of your friends: {}.".format(", ".join(friends))


def delete_friend(user_id):
    try:
        print(show_friends_list(user_id))
        friend_username = input("What is the username of the friend you would like to delete? \n")
        friend_id = DBSearch.get_friend_user_id(friend_username)[0][0]
        DBSearch.delete_from_friend_list(friend_id, user_id)
        return "{} has been deleted from your friend list.".format(friend_username)
    except IndexError:
        return "Sorry, that isn't a valid user. Please try again."

