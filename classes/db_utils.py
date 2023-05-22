import mysql.connector
from WardrobePlanner.classes.config import USER, PASSWORD, HOST


class NoConnection(Exception):
    pass


def connect_to_db():
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database="wardrobe_planner"
    )
    return connection


# to find the functions you can use keywords(login, sign up, items, statuses, friends) in ctrl + f

class DBSearch:

    # login
    @staticmethod
    def username_check(username):
        try:
            db_connection = connect_to_db()
            cur = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            query = "SELECT user_name FROM users;"
            cur.execute(query)
            result = cur.fetchall()
            #print(result)
            return result
        finally:
            cur.close()

    @staticmethod
    def password_check(username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT user_password FROM users WHERE user_name = %s ;""", [username])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()

    @staticmethod
    def get_location():
        pass

    @staticmethod
    def get_user_info(username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT user_id, user_name, user_password FROM users WHERE user_name = %s ;""", [username])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()

    # sign up
    @staticmethod
    def create_new_user(username, password):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""INSERT INTO users (user_name, user_password) VALUES (%s, %s);""", [username, password])
            db_connection.commit()
        finally:
            cursor.close()

    @staticmethod
    def set_hometown(user_id, hometown, lat, long):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""INSERT INTO user_location (user_id, home_town, latitude, longitude) VALUES (%s, %s, %s, %s);""", [user_id, hometown, lat, long])
            db_connection.commit()
        finally:
            cursor.close()


    # is this function nescessary?
    @staticmethod
    def get_user_id(username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT user_id FROM users WHERE user_name = %s ;""", [username])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()


    # friends
    @staticmethod
    def get_friend_user_id(friend_username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT user_ID from users WHERE user_name = %s;""", [friend_username])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()

    @staticmethod
    def add_to_friend_list(user_id, friend_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""INSERT INTO friends (user_id, friend_id) VALUES (%s, %s)""", [user_id, friend_id])
            db_connection.commit()
        finally:
            cursor.close()

    @staticmethod
    def delete_from_friend_list(friend_id, user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""DELETE FROM friends AS f WHERE f.friend_id = %s AND f.user_id = %s)""", [friend_id, user_id])
            db_connection.commit()
        finally:
            cursor.close()

    @staticmethod
    def get_friends_list(user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            # Need to add user id in <-- i'm not sure where to put the %s
            cursor.execute("""SELECT u1.user_id, u1.user_name FROM users AS u1" \
                    "INNER JOIN friends AS f ON u1.user_id = f.user_id" \
                    "INNER JOIN users AS u2 ON f.friend_id = u2.user_id" \
                    "WHERE u2.user_id in (1)" \
                    "AND u1.user_id <> 1" \
                    "ORDER BY u2.user_id;""",
                           [user_id])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()

    # statuses
    @staticmethod
    def show_count_of_clothes_available(user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT COUNT(*) AS count_available_items FROM availability_status AS a 
                        JOIN ownership AS o ON a.item_id = o.item_id 
                        WHERE a.item_status = 'available' 
                        AND o.owner_id = %s;""", [user_id])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()

    @staticmethod
    def show_count_of_clothes_dirty(user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT COUNT(*) AS count_available_items FROM availability_status AS a 
                                   JOIN ownership AS o ON a.item_id = o.item_id 
                                   WHERE a.item_status = 'dirty' 
                                   AND o.owner_id = %s;""", [user_id])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()

    # items
    @staticmethod
    def search_clothes(tags, user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT c.item_description, c.item_ID, o.owner_ID FROM wardrobe_planner.clothes AS c
                                                   INNER JOIN wardrobe_planner.availability_status AS a ON c.item_ID = a.item_ID
                                                   INNER JOIN wardrobe_planner.ownership AS o ON c.item_id = o.item_id
                                                   WHERE a.item_status = 'available'
                                                   %s
                                                   AND c.item_id IN (
                                                       SELECT o.item_id
                                                       FROM wardrobe_planner.ownership AS o
                                                       WHERE o.owner_id IN (
                                                           SELECT f.user_ID
                                                           FROM friends AS f
                                                           WHERE f.friend_ID = %s));""", [tags, user_id])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()

    @staticmethod
    def add_item_to_wardrobe(item_type, item_description, weather_tag, occasion_tag, mood_tag):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""INSERT INTO clothes (item_type, item_description, weather_tag, occasion_tag, mood_tag) " \
                    "VALUES (%s,%s,%s,%s,%s)""", [item_type, item_description, weather_tag, occasion_tag, mood_tag])
            db_connection.commit()
        finally:
            cursor.close()

    @staticmethod
    def delete_item_from_wardrobe(item_description):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            # Need delete item query
        except Exception:
            raise NoConnection
        else:
            cursor.execute("placeholder", [])
            db_connection.commit()
        finally:
            cursor.close()

    # this functions probably needs to be reworked into something else
    @staticmethod
    def get_item_id(item_description):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
        except Exception:
            raise NoConnection
        else:
            cursor.execute("""SELECT item_id FROM clothes WHERE item_description = %s""", [item_description])
            result = cursor.fetchall()
            return result
        finally:
            cursor.close()
