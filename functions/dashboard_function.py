from WardrobePlanner.classes.db_utils import DBSearch
# from WardrobePlanner.classes.item import Item
from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.functions.tag_prompts import prompt_user, formatting_tags



mainDashboard = Dashboard("on the Main Dashboard",
                               ["Show User Info", "Search Wardrobe", "Manage Wardrobe", "Manage Friends",
                                "Log Out / Exit"])

searchDashboard = Dashboard("in Search", ["Search all available",
                                                  "Search through tags",
                                                  "Back to main dashboard"])

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
        options_count = searchDashboard.generate_menu()
        sub_dashboard_2_choice = searchDashboard.get_users_choice(options_count)
        if sub_dashboard_2_choice == 1:
            tags = ""
            search_results = DBSearch.search_clothes(tags, user.user_id)
            print(search_results)
        elif sub_dashboard_2_choice == 2:
            user_tags = prompt_user()
            tags = formatting_tags(user_tags)
            search_results = DBSearch.search_clothes(tags, user.user_id)
            print(search_results)
        else:
            return dashboard(user)


    elif dashboard_choice == 3:
        # Managing the wardrobe
        options_count = manageWardrobeDashboard.generate_menu()
        sub_dashboard_3_choice = manageWardrobeDashboard.get_users_choice(options_count)

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
        options_count = manageFriendsDashboard.generate_menu()
        sub_dashboard_4_choice = manageFriendsDashboard.get_users_choice(options_count)

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
        quit()
        return
