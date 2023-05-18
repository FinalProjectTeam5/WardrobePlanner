from db_utils import DBSearch
# Mark the directories as Sources Root


def sign_up():
    username = get_new_username()
    password = get_new_password()
    user_dict = {
        "username": username,
        "password": password
    }
    DBSearch.create_new_user(user_dict["username"], user_dict["password"])
    print("Created a new user!")
    return login()


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


def get_home_town():
    home_town = input("Your closest big city: ")
    if len(home_town) < 2 or len(home_town) > 20:
        print("Sorry, city name should be between 2 and 20 characters long.\n Try again.")
        return get_home_town()
    else:
        return home_town


def login():

    username = input("Your username: ")
    if DBSearch.username_check(username):
        password = input("Your password: ")
        if DBSearch.all_check(username, password):
            print("You're signed in!")
            return DBSearch.show_user_info(username)
        else:
            print("That's an incorrect password. Try again: ")
            return login()
    else:
        print("You don't have an account here yet. Register here: ")
        return sign_up()


def show_user_id(username):
    user_id = DBSearch.get_user_id(username)
    return user_id
