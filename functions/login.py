from db_utils import DBSearch
# Mark the directories as Sources Root


def sign_up():
    username = get_new_username()
    password = get_new_password()
    city = get_city()
    user_dict = {
        "username": username,
        "password": password,
        "city": city
    }
    return user_dict


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


def get_city():
    city = input("Your closest big city: ")
    if len(city) < 2 or len(city) > 20:
        print("Sorry, city name should be between 2 and 20 characters long.\n Try again.")
        return get_city()
    else:
        return city


def login():

    username = input("Your username: ")
    if DBSearch.username_check(username):
        password = input("Your password: ")
        if DBSearch.all_check(username, password):
            print("You're signed in!")
            # Here's going to be a return of a main menu function or user dashboard or sth
            pass
        else:
            print("That's an incorrect password. Try again: ")
            return login()
    else:
        print("You don't have an account here yet. Register here: ")
        return sign_up()

