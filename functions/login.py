from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.identifying_the_city_and_getting_coordinates import getting_hometown


def sign_up():
    username = get_new_username()
    password = get_new_password()
    hometown = getting_hometown()
    user_dict = {
        "username": username,
        "password": password,
        "hometown": hometown[0],
        "latitude": hometown[1][0],
        "longitude": hometown[1][0]
    }
    print(user_dict)
    DBSearch.create_new_user(user_dict["username"], user_dict["password"])
    print("New user created! You can start planning your wardrobe!")
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
    results = DBSearch.username_check(username)
    #print(results)
    found_ya = False
    for result in results:
        if username == result[0]:
            found_ya = True
            break
    if found_ya:
        password_given = input("Your password: ")
        password_in_database = fetch_password(username)
        #print(password_in_database)
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
