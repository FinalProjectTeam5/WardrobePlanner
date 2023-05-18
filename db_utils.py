import mysql.connector as mysql
from config import USER, PASSWORD, HOST


class NoConnection(Exception):
    pass


def connect_to_db():
    connection = mysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin="[our database] password",
        database="[our database]"
    )
    return connection


class DBSearch:

    @staticmethod
    def username_check(username):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "SELECT user_name FROM users WHERE user_id = {}".format(username)
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
            # This query will have to be changed to the database naming and structure
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

    def get_friend_user_id(friend_id):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "SELECT user_ID from users WHERE user_name = {}".format(friend_id)
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
            query = "INSERT INTO friends (user_id, friend_id) VALUES ({}, {})".format(user_id, friend_id)
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
            query = "DELETE FROM friends AS f WHERE f.friend_id = {})".format(friend_id)
            cursor.execute(query)
        except Exception:
            raise NoConnection
        else:
            db_connection.commit()
        finally:
            if db_connection:
                db_connection.close()


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
                query = "UPDATE availability_status AS a SET a.item_status = 'taken' WHERE a.item_id = {}".format(
                    item_id)
                cursor.execute(query)
                return "This item is ready to be shared with you"
            else:
                return "This item is not available to share"

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




"""Functions below are just drafts for your feedback and need to be revised please"""


    # 1. first we ask input of mood/occasion/date:

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

    # 2. a separate function to create a weather tag.
    # Giving the tag after input of date and connecting to API?

    #def create_weather_tag():
        #input = ask_input()
        #date = input[2]

        #then connect to API and get result of the apparent max temperature.
        # in the end, give output:
        # if temperature < 0, weather_tag = "freezing"
        #elif temperature >=0 and temperature < 10, weather_tag = "mild'
        #.....

    #3. thanks to 2 functions above we have all the tags and can run a search in our wardrobe
    # and wardrobes of everybody who shares clothes with us:

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
