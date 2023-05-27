
# from WardrobePlanner.classes.item import Item
from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.functions.friends import add_friend, delete_friend, show_friends_list
from WardrobePlanner.functions.manage_wardrobe import add_item, delete_item, laundry, add_item_id, notification_laundry
from WardrobePlanner.functions.search.search_dashboard import search_dashboard



mainDashboard = Dashboard("on the Main Dashboard",
                          ["Show User Info", "Search Wardrobe", "Manage Wardrobe", "Manage Friends",
                           "Log Out / Exit"])


manageWardrobeDashboard = Dashboard("in Manage Wardrobe", ["Add Items To Your Wardrobe",
                                                           "Delete Items From Your Wardrobe",
                                                           "Do Laundry",
                                                           "Back to main dashboard"])

manageFriendsDashboard = Dashboard("in Manage Friends", ["Show Friends",
                                                         "Add Friends",
                                                         "Delete Friends",
                                                         "Back to main dashboard"])


def dashboard(user):
    print("\n \n")
    # We use the dashboard function to get the user to tell us what they want
    # dashboard_choice = dashboard_function.user_dashboard_choice()

    options_count = mainDashboard.generate_menu()
    dashboard_choice = mainDashboard.get_users_choice(options_count)
    # Depending on user choice we'll go into further sub-dashboards or show results,
    # after completing a sub-function the user is taken back to the beginning of the dashboard function
    if dashboard_choice == 1:
        # Show user info
        print("User name: {}\n"
              "User password: {} \n"
              "User hometown: {} \n".format(user.username, user.password, user.home_town))
        return dashboard(user)

    elif dashboard_choice == 2:
        # Search the wardrobe
        search_dashboard(user)
        return dashboard(user)

    elif dashboard_choice == 3:
        # Managing the wardrobe
        options_count = manageWardrobeDashboard.generate_menu()
        sub_dashboard_3_choice = manageWardrobeDashboard.get_users_choice(options_count)

        if sub_dashboard_3_choice == 1:
            item_id = add_item_id(user.user_id)[0][0]
            item_added = add_item(item_id)
            print(item_added)
            return dashboard(user)
        # Add items to wardrobe

        elif sub_dashboard_3_choice == 2:
            item_deleted = delete_item()
            print(item_deleted)
            return dashboard(user)
        # Delete items

        elif sub_dashboard_3_choice == 3:
            print(notification_laundry(user.user_id))
            laundry_decision = laundry(user.user_id)
            print(laundry_decision)
            return dashboard(user)
        # Do laundry

    elif dashboard_choice == 4:
        # Managing friends
        options_count = manageFriendsDashboard.generate_menu()
        sub_dashboard_4_choice = manageFriendsDashboard.get_users_choice(options_count)

        if sub_dashboard_4_choice == 1:
            friend_list = show_friends_list(user.user_id)
            print(friend_list)
            return dashboard(user)
        # Show friends

        elif sub_dashboard_4_choice == 2:
            friend_added = add_friend(user.user_id)
            print(friend_added)
            return dashboard(user)
        # Add friends

        elif sub_dashboard_4_choice == 3:
            friend_deleted = delete_friend(user.user_id)
            print(friend_deleted)
            return dashboard(user)
        # Delete friends

    elif dashboard_choice == 5:
        # Exits the dashboard and returns to main; can log in again
        quit()
        return
