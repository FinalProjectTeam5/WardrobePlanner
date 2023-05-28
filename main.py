from WardrobePlanner.classes.user import User
from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.login import login, sign_up
from WardrobePlanner.functions.dashboard_function import dashboard
from logo import logo


def main():

    # Starting screen
    print(logo)
    try:
        while True:
            lets_start = input("1. Log in \n"
                               "2. Register\n"
                               "3. Quit \n")
            if lets_start == "1":
                # We use the login function from login file to get user data
                username = login()
                user_data = DBSearch.get_user_info(username)
                user_id = user_data[0][0]
                user_location = DBSearch.get_location(user_id)
                user = User(user_data[0][0], user_data[0][1], user_data[0][2], user_location[0][0], user_location[0][1], user_location[0][2])
                break
            elif lets_start == "2":
                # We use the signup function from login file to create a new user
                sign_up()
                #break
            elif lets_start == "3":
                quit()
            else:
                print("Please choose an option from the list. Try again.")
    except ValueError:
        print("Sorry that's not a number, try again!")

    # We redirect user to a dashboard function, in which user can interact with their wardrobe
    return dashboard(user)


if __name__ == "__main__":
    main()
