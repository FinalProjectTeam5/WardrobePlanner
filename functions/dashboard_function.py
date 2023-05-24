from WardrobePlanner.classes.db_utils import DBSearch
# from WardrobePlanner.classes.item import Item
from WardrobePlanner.classes.dashboard_class import Dashboard
from WardrobePlanner.functions.friends import add_friend, delete_friend, show_friends_list
from WardrobePlanner.functions.manage_wardrobe import add_item, delete_item, laundry, add_item_id
from WardrobePlanner.functions.search.tag_prompts import prompt_user, formatting_tags
from WardrobePlanner.functions.search.results_handling import display_results, what_user_wants_to_do_with_the_results


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
            number_of_results = display_results(search_results, user)
            decision = what_user_wants_to_do_with_the_results(search_results, number_of_results, user)
            print(search_results)
        elif sub_dashboard_2_choice == 2:
            user_tags = prompt_user(user)
            tags = formatting_tags(user_tags)
            print(tags)
            search_results = DBSearch.search_clothes(tags, user.user_id)
            number_of_results = display_results(search_results, user)
            decision = what_user_wants_to_do_with_the_results(search_results, number_of_results, user)
            print(search_results)
        else:
            return dashboard(user)

    elif dashboard_choice == 3:
        # Managing the wardrobe
        options_count = manageWardrobeDashboard.generate_menu()
        sub_dashboard_3_choice = manageWardrobeDashboard.get_users_choice(options_count)

        if sub_dashboard_3_choice == 1:
            item_id = add_item_id(user.user_id)
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
            laundry_decision = laundry(user.user_id)
            print(laundry_decision)
            return dashboard(user)
        # Do laundry

    elif dashboard_choice == 4:
        # Managing friends
        options_count = manageFriendsDashboard.generate_menu()
        sub_dashboard_4_choice = manageFriendsDashboard.get_users_choice(options_count)

        if sub_dashboard_4_choice == 1:
            friend_list = show_friends_list(user)
            print(friend_list)
            return dashboard(user)
        # Show friends

        elif sub_dashboard_4_choice == 2:
            friend_added = add_friend(user)
            print(friend_added)
            return dashboard(user)
        # Add friends

        elif sub_dashboard_4_choice == 2:
            friend_deleted = delete_friend(user)
            print(friend_deleted)
            return dashboard(user)
        # Delete friends

    elif dashboard_choice == 5:
        # Exits the dashboard and returns to main; can log in again
        quit()
        return
