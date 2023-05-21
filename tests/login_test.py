import unittest
import login
from db_utils import DBSearch


def get_new_username():
    username = input("Your username: ")
    if len(username) < 2 or len(username) > 20:
        print("Sorry, your username should be between 2 and 20 characters long.\n Try again.")
        return get_new_username()
    elif DBSearch.username_check(username):
        print("You already have an account here. Login here: ")
        return login()
    else:
        return username


print(get_new_username())