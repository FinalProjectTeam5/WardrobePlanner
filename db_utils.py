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
            query = "SELECT username FROM users WHERE username = {}".format(username)
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
            query = "SELECT password FROM users WHERE username = {}".format(username)
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
    def create_new_user(username, password, city):
        try:
            db_connection = connect_to_db()
            cursor = db_connection.cursor()
            query = "INSERT INTO users (username, password, city) VALUES ({}, {}, {})".format(username, password, city)
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
            query = "SELECT user_id FROM users WHERE username = {}".format(username)
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
            query = "SELECT user_id, username, password, home_town FROM users WHERE user_id = {}".format(user_id)
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



