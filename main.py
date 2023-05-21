from WardrobePlanner.classes.user import User
from WardrobePlanner.classes.db_utils import DBSearch
from WardrobePlanner.functions.login import login, sign_up
from WardrobePlanner.functions.dashboard_function import dashboard
from logo import logo


def main():
    # We create the object of user with all None attributes


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
                user_data = DBSearch.show_user_info(username)
                #print(user_data)

                # We use user_data to change the user object attributes, gonna have to change the home_town part
                user = User(user_data[0][0], user_data[0][1], user_data[0][2], "hometown")
                #print(user.user_id, user.username)
                break
            elif lets_start == "2":
                sign_up()

                break
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
