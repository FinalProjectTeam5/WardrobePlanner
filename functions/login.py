import re


def sign_up():
    username = get_new_username()
    password = get_new_password()
    user_dict = {
        "username": username,
        "password": password
    }
    return user_dict


def get_new_username():
    username = input("Your username: ")
    if len(username) < 2 or len(username) > 20:
        print("Sorry, your username should be between 2 and 20 characters long.\n Try again.")
        return get_new_username()
    else:
        return username


def get_new_password():
    password = input("Your password: ")
    if password == get_new_username():
        print("Your password can't be the same as your username!")
        return get_new_password()
    elif len(password) < 4 or len(password) > 20:
        print("Sorry, your password should be between 4 and 20 characters long.\n Try again.")
        return get_new_password()
    else:
        return password

