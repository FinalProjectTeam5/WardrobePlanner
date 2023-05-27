# from WardrobePlanner.classes.item import Item
from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.functions.manage_wardrobe_dashboard import manage_wardrobe_dashboard
from WardrobePlanner.functions.manage_friends_dashboard import manage_friends_dashboard
from WardrobePlanner.functions.search.search_dashboard import search_dashboard



mainDashboard = Dashboard("on the Main Dashboard",
                          ["Show User Info", "Search Wardrobe", "Manage Wardrobe", "Manage Friends",
                           "Log Out / Exit"])


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
        manage_wardrobe_dashboard(user)
        return dashboard(user)

    elif dashboard_choice == 4:
        # Managing friends
        manage_friends_dashboard(user)
        return dashboard(user)

    elif dashboard_choice == 5:
        # Exits the program
        quit()
        return
