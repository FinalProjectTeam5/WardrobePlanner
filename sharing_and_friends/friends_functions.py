"""
add friend - check for logged in user. check database for friend user_id
"""


def add_friend(friend_username):
    accept_decline = input("Do you want to accept friend request from {}? Y or N ".format(friend_username))
    if accept_decline == "Y":
        add_to_friend_list(friend_id)
    else:
        return "{} has not been added to your friend list".format(friend_username)


# def get_user_id():
#     try:
#         db_connection = connect_to_db()
#         cursor = db_connection.cursor()
#         query = "SELECT user_ID from users"
#         cursor.execute(query)
#     except Exception:
#         raise NoConnection
#     else:
#         result = cursor.fetchall()
#         user_id = result
#         return user_id
#     finally:
#         if db_connection:
#             db_connection.close()


def add_to_friend_list(user_id, friend_id):
    try:
        db_connection = connect_to_db()
        cursor = db_connection.cursor()
        query = "INSERT INTO friends (user_id, friend_id) VALUES ({}, {})".format(user_ID, friend_ID)
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

clothing_id = 4


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
            query = "UPDATE availability_status SET availability_status.item_status = 'unavailable' WHERE availability_status.item_id = {}".format(item_id)
            cursor.execute(query)
            return "This item is ready to be shared with you"
        else:
            return "This item is not available to share"
