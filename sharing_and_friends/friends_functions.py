"""
add friend - check for logged in user. check database for friend user_id
"""


def add_friend(username):
    friend_username = input("What is the username of the friend you would like to add?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    user_id = DBSearch.get_user_id(username)
    DBSearch.add_to_friend_list(user_id, friend_id)
    print("{} has been added to your friend list.".format(friend_username))


def delete_friend(username):
    friend_username = input("What is the username of the friend you would like to delete?")
    friend_id = DBSearch.get_friend_user_id(friend_username)
    DBSearch.delete_from_friend_list(friend_id)
    print("{} has been deleted from your friend list.".format(friend_username))


def get_friend_user_id(friend_id):
    try:
        db_connection = connect_to_db()
        cursor = db_connection.cursor()
        query = "SELECT user_ID from users WHERE username = {}".format(friend_id)
        cursor.execute(query)
    except Exception:
        raise NoConnection
    else:
        result = cursor.fetchall()
        user_id = result
        return user_id
    finally:
        if db_connection:
            db_connection.close()


def add_to_friend_list(user_id, friend_id):
    try:
        db_connection = connect_to_db()
        cursor = db_connection.cursor()
        query = "INSERT INTO friends (userid, friendid) VALUES ({}, {})".format(user_id, friend_id)
        cursor.execute(query)
    except Exception:
        raise NoConnection
    else:
        db_connection.commit()
    finally:
        if db_connection:
            db_connection.close()


def delete_from_friend_list(friend_id):
    try:
        db_connection = connect_to_db()
        cursor = db_connection.cursor()
        query = "DELETE FROM friends AS f WHERE f.friendid = {})".format(friend_id)
        cursor.execute(query)
    except Exception:
        raise NoConnection
    else:
        db_connection.commit()
    finally:
        if db_connection:
            db_connection.close()


"""
Check status, if available, change to unavailable. If not available return cannot be borrowed.
"""

def get_item_availability():
    item_description = input("What is the item you would like to borrow?")
    item_id = DBSearch.get_item_id(item_description)
    DBSearch.check_availability(item_id)


def check_availability(item_id):

    try:
        db_connection = connect_to_db()
        cursor = db_connection.cursor()
        query = "SELECT item_status from availability_status WHERE item_id = {}".format(item_id)
        cursor.execute(query)
    except Exception:
        raise NoConnection
    else:
        result = cursor.fetchall()
        if result == "available":
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "UPDATE availability_status AS a SET a.item_status = 'taken' WHERE a.item_id = {}".format(item_id)
            cursor.execute(query)
            return "This item is ready to be shared with you"
        else:
            return "This item is not available to share"
