from WardrobePlanner.classes.user import User
from WardrobePlanner.functions.login import login
from WardrobePlanner.functions.dashboard_function import dashboard
from logo import logo


def main():
    print(logo)

    while True:
        lets_start = input("1. Log in \n"
                           "2. Register\n")


    # We create the object of user with all None attributes
    user = User
    
    # We use the login function from login file to get user data
    user_data = login()
    
    # We use user_data to change the user object attributes, gonna have to change the home_town part
    user.login(user_data["user_id"], user_data["username"], user_data["password"], user_data["home_town"])
    
    # We redirect user to a dashboard function, in which user can interact with their wardrobe
    return dashboard(user)


if __name__ == "__main__":
    main()
