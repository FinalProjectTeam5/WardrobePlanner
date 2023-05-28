from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.date_and_geolocation.identifying_the_city_and_getting_coordinates import getting_hometown


def sign_up():
    username = get_new_username()
    if username == False:
        return login()
    password = get_new_password(username)
    hometown = "again"
    while hometown == "again":
        hometown = getting_hometown()

    print(hometown)

    if hometown == False:
        user_dict = {
            "username": username,
            "password": password,
            "hometown": None,
            "latitude": None,
            "longitude": None
        }
    else:
        user_dict = {
            "username": username,
            "password": password,
            "hometown": hometown[0],
            "latitude": hometown[1][0],
            "longitude": hometown[1][1]
        }
    DBSearch.create_new_user(user_dict["username"], user_dict["password"])
    user_id = DBSearch.get_user_id(username)[0][0]
    DBSearch.set_hometown(user_id, user_dict["hometown"], user_dict["latitude"], user_dict["longitude"])
    print("New user created! You can start planning your wardrobe!")
    return


def get_new_username():
    username = input("Your username: ")
    if len(username) < 2 or len(username) > 20:
        print("Sorry, your username should be between 2 and 20 characters long.\n Try again.")
        return get_new_username()
    else:
        results = DBSearch.username_check()
        found_ya = False
        for result in results:
            if username == result[0]:
                found_ya = True
                break
        if found_ya:
            print("You already have an account here. Login here: ")
            return False
        else:
            return username


def get_new_password(username):
    password = input("Your password: ")
    if password == username:
        print("Your password can't be the same as your username!")
        return get_new_password(username)
    elif len(password) < 4 or len(password) > 20:
        print("Sorry, your password should be between 4 and 20 characters long.\n Try again.")
        return get_new_password(username)
    else:
        return password


def fetch_password(username):
    return DBSearch.password_check(username)


def verify_password(password_given, password_in_database ):
    if password_given == password_in_database[0][0]:
        print("You're signed in!")
        return True
    else:
        print("That's an incorrect password. Try again: ")
        return login()


def login():
    username = input("Your username: ")
    results = DBSearch.username_check()
    found_ya = False
    for result in results:
        if username == result[0]:
            found_ya = True
            break
    if found_ya:
        password_given = input("Your password: ")
        password_in_database = fetch_password(username)
        if verify_password(password_given, password_in_database):
            return username
    else:
        try:
            while True:
                user_choice = input("You don't have an account here yet.\n"
                                    "1. Register\n"
                                    "2. Try Again\n"
                                    "3. Quit\n")
                if user_choice == "1":
                    return sign_up()
                elif user_choice == "2":
                    return login()
                elif user_choice == "3":
                    quit()
                else:
                    print("Please choose an option from the list. Try again.")
        except ValueError:
            print("Sorry that's not a number, try again!")


def show_user_id(username):
    user_id = DBSearch.get_user_id(username)
    return user_id
