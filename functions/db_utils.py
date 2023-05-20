import mysql.connector as mysql
from config import USER, PASSWORD, HOST


class NoConnection(Exception):
    pass


def connect_to_db():
    connection = mysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="mysql_native_password",
        database="wardrobe_planner"
    )
    return connection


class DBSearch:

    @staticmethod
    def username_check(username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "placeholder".format(username)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            result = cursor.fetchall()
            if result == username:
                return True
            else:
                return False
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def all_check(username, password):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "SELECT user_password FROM users WHERE user_name = {}".format(username)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            result = cursor.fetchall()
            if result == password:
                return True
            else:
                return False
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def create_new_user(username, password):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "INSERT INTO users (user_name, user_password) VALUES ({}, {})".format(username, password)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            db_connection.commit()
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def get_user_id(username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "SELECT user_id FROM users WHERE user_name = {}".format(username)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            result = cursor.fetchall()
            return result
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def get_item_id(item_description):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "SELECT item_id FROM clothes WHERE item_description = {}".format(item_description)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            result = cursor.fetchall()
            return result
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def show_user_info(user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "SELECT user_id, user_name, user_password FROM users WHERE user_id = {}".format(user_id)
            
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            result = cursor.fetchall()
            return result
            # I think this will return a dict?
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def get_friend_user_id(friend_username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "SELECT user_ID from users WHERE user_name = {}".format(friend_username)
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

    @staticmethod
    def add_to_friend_list(user_id, friend_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "INSERT INTO friends (user_id, friend_id) VALUES ({}, {})".format(user_id, friend_id)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            db_connection.commit()
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def delete_from_friend_list(friend_id, user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "DELETE FROM friends AS f WHERE f.friend_id = {} AND f.user_id = {})".format(friend_id, user_id)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            db_connection.commit()
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def get_friends_list(user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            #Need to add user id in
            query = "SELECT u1.user_id, u1.user_name FROM users AS u1" \
                    "INNER JOIN friends AS f ON u1.user_id = f.user_id" \
                    "INNER JOIN users AS u2 ON f.friend_id = u2.user_id" \
                    "WHERE u2.user_id in (1)" \
                    "AND u1.user_id <> 1" \
                    "ORDER BY u2.user_id;"
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            db_connection.commit()
        finally:
            if db_connection:
                db_connection.close()

    @staticmethod
    def show_count_of_clothes_available(user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = """SELECT COUNT(*) AS count_available_items FROM availability_status AS a 
            JOIN ownership AS o ON a.item_id = o.item_id 
            WHERE a.item_status = 'available' 
            AND o.owner_id = {}""".format(user_id)

            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            result = cursor.fetchall()
            count = result
            print("You have {} items available in your wardrobe.".format(count))
            return "You have {} items available in your wardrobe.".format(count)

    @staticmethod
    def show_count_of_clothes_dirty(user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = """SELECT COUNT(*) AS count_available_items FROM availability_status AS a 
            JOIN ownership AS o ON a.item_id = o.item_id 
            WHERE a.item_status = 'dirty' 
            AND o.owner_id = {}""".format(user_id)

            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            result = cursor.fetchall()
            count = result
            print("You have {} items in your wardrobe that are dirty.".format(count))
            return "You have {} items in your wardrobe that are dirty.".format(count)

    @staticmethod
    def ask_input():
        input_list = []
        mood = input(
        "What are you feeling like today? Choose one of the options: serious / cheerful / romantic / serious / neutral")

        occasion = input("What's the occasion? Choose one of the options: work / home / sport / date / cleaning / party")

        date = input("Input the date you want to choose the outfit for (YYYY-MM-DD format")

        input_list.append(mood)
        input_list.append(occasion)
        input_list.append(date)

        return input_list

    @staticmethod
    def search_clothes(weather_tag, occasion_tag, mood_tag, user_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = """SELECT c.item_description, c.item_ID, o.owner_ID
                           FROM clothes AS c
                           INNER JOIN availability_status AS a ON c.item_ID = a.item_ID
                           INNER JOIN ownership AS o ON c.item_id = o.item_id
                           WHERE a.item_status = 'available'
                           AND c.weather_tag = %s
                           AND c.occasion_tag = %s
                           AND c.mood_tag = %s
                           AND c.item_id IN (
                               SELECT o.item_id
                               FROM ownership AS o
                               WHERE o.owner_id IN (
                                   SELECT f.user_ID
                                   FROM friends AS f
                                   WHERE f.friend_ID = %s
                               )
                           )"""
            cursor.execute(query, (weather_tag, occasion_tag, mood_tag, user_id))
            result = cursor.fetchall()
            print("These are all items that are matching your search criteria:")
            for item in result:
                item_description = item[0]
                item_id = item[1]
                owner_id = item[2]
                output = "'{}' - item number {} belonging to user {}".format(item_description, item_id, owner_id)
                print(output)
            return result
        except Exception:
            raise NoConnection
