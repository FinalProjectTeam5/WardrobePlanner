import search_clothes as search
import login as login
import user_dashboard as dashboard
from db_utils import DBSearch as DB


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
    dashboard_choice = dashboard.user_dashboard_choice()

    if dashboard_choice == 1:
        # Show user info
        user_info = DB.show_user_info(user.user_id)
        print(user_info)
        return dashboard(user)

    elif dashboard_choice == 2:
        # The wardrobe search function will be called here

    elif dashboard_choice == 3:
        # Manage wardrobe function will be called here

    elif dashboard_choice == 4:
        # Change status of all clothes to available

    elif dashboard_choice == 5:
        user.logout()
        return main()


def main():
    # We create the object of user with all None attributes
    user = User

    user_data = login.login()

    user.login(user_data["user_id"], user_data["username"], user_data["password"], user_data["home_town"])

    return dashboard(user)


if __name__ == "__main__":
    main()