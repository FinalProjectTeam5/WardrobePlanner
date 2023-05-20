from functions import search_clothes as search
from functions import login as login_function
from functions.db_utils import DBSearch as DB
from functions import user_dashboard as dashboard_function


class User:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.password = None
        self.home_town = None
        self.status = False

    def login(self, user_id, username, password, home_town):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.home_town = home_town
        self.status = True

    def logout(self):
        self.user_id = None
        self.username = None
        self.password = None
        self.home_town = None
        self.status = False


class Item:
    def __init__(self, user_id):
        self.owner_id = user_id
        self.item_id = None
        self.item_type = None
        self.item_description = None
        self.weather_tag = None
        self.occasion_tag = None
        self.mood_tag = None

    def manage_item(self, item_type, item_description, weather_tag, occasion_tag, mood_tag):
        self.item_id = search.show_item_id(item_description)
        self.item_type = item_type
        self.item_description = item_description
        self.weather_tag = weather_tag
        self.occasion_tag = occasion_tag
        self.mood_tag = mood_tag

    def delete_item(self):
        self.owner_id = None
        self.item_id = None
        self.item_type = None
        self.item_description = None
        self.weather_tag = None
        self.occasion_tag = None
        self.mood_tag = None


def dashboard(account):

    user = account
    
    # We use the dashboard function to get the user to tell us what they want
    dashboard_choice = dashboard_function.user_dashboard_choice()
    
    # Depending on user choice we'll go into further sub-dashboards or show results, 
    # after completing a sub-function the user is taken back to the beginning of the dashboard function
    if dashboard_choice == 1:
        # Show user info
        user_info = DB.show_user_info(user.user_id)
        print(user_info)
        return dashboard(user)

    elif dashboard_choice == 2:
        pass
        # The wardrobe search function will be called here

    elif dashboard_choice == 3:
        # Managing the wardrobe
        sub_dashboard_3_choice = dashboard_function.sub_dashboard_manage_wardrobe()

        if sub_dashboard_3_choice == 1:
            pass
        # Add items to wardrobe


        elif sub_dashboard_3_choice == 2:
            pass
        # Delete items

        elif sub_dashboard_3_choice == 3:
            pass
        # Do laundry


    elif dashboard_choice == 4:
        # Managing friends
        sub_dashboard_4_choice = dashboard_function.sub_dashboard_manage_friends()

        if sub_dashboard_4_choice == 1:
            pass
        # Add friends

        elif sub_dashboard_4_choice == 2:
            pass
        # Delete friends

        elif sub_dashboard_4_choice == 3:
            pass
        # Show friends


    elif dashboard_choice == 5:
        # Exits the dashboard and returns to main; can log in again
        user.logout()
        return main()


def main():
    # We create the object of user with all None attributes
    user = User
    
    # We use the login function from login file to get user data
    user_data = login_function.login()
    
    # We use user_data to change the user object attributes, gonna have to change the home_town part
    user.login(user_data["user_id"], user_data["username"], user_data["password"], user_data["home_town"])
    
    # We redirect user to a dashboard function, in which user can interact with their wardrobe
    return dashboard(user)


if __name__ == "__main__":
    main()
